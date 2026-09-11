"""S3 / S3-compatible object storage connector.

Reads and writes go through Spark's ``s3a://`` filesystem so the data path is
fully distributed - the driver never downloads the dataset.  Only metadata
operations (listing for availability conditions, connection tests, Excel
staging) use boto3.

No AWS-specific assumption is hard-coded: a custom ``endpoint``, path-style
access, a non-AWS region string and disabled SSL verification are all
supported, which is what makes MinIO / Ceph / StorageGRID work.
"""

from __future__ import annotations

import fnmatch
import time
from datetime import UTC
from typing import TYPE_CHECKING, Any
from urllib.parse import urlparse

from reconx.common.errors import ConnectionFailedError, ConnectorError
from reconx.common.logging import get_logger
from reconx.config.enums import FileFormat, SourceType
from reconx.connectors.base import (
    ConnectionTestResult,
    DataSourceConnector,
    FileInfo,
    OutputContext,
    SourceContext,
    register_connector,
)
from reconx.connectors.formats import (
    build_read_options,
    build_write_options,
    detect_format,
    read_files,
    spark_format_name,
)

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)


def s3a_uri(path: str, bucket: str | None = None, base_path: str | None = None) -> str:
    """Normalise ``s3://``/``s3a://``/relative paths into an ``s3a://`` URI."""
    if path.startswith("s3a://"):
        return path
    if path.startswith(("s3://", "s3n://")):
        return "s3a://" + path.split("://", 1)[1]
    if not bucket:
        raise ConnectorError(
            f"Path '{path}' is relative but the connection defines no bucket",
            details={"hint": "Use a full s3://bucket/key path or set 'bucket' on the connection"},
        )
    prefix = "/".join(part.strip("/") for part in (base_path or "", path) if part)
    return f"s3a://{bucket}/{prefix}"


def split_s3_uri(uri: str) -> tuple[str, str]:
    parsed = urlparse(uri if "://" in uri else f"s3a://{uri}")
    return parsed.netloc, parsed.path.lstrip("/")


def hadoop_conf_for(config: dict[str, Any], *, prefix: str = "fs.s3a") -> dict[str, str]:
    """Hadoop configuration entries implementing this connection."""
    conf: dict[str, str] = {
        f"{prefix}.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
        f"{prefix}.path.style.access": str(bool(config.get("pathStyleAccess", False))).lower(),
        f"{prefix}.connection.ssl.enabled": str(bool(config.get("sslEnabled", True))).lower(),
        f"{prefix}.connection.timeout": str(config.get("connectionTimeoutMs", 30_000)),
        f"{prefix}.connection.maximum": str(config.get("maxConnections", 64)),
        f"{prefix}.attempts.maximum": "5",
        f"{prefix}.fast.upload": "true",
        f"{prefix}.aws.credentials.provider": (
            "com.amazonaws.auth.DefaultAWSCredentialsProviderChain"
            if config.get("useInstanceProfile")
            else "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider"
        ),
    }
    if config.get("endpoint"):
        conf[f"{prefix}.endpoint"] = str(config["endpoint"])
    if config.get("region"):
        conf[f"{prefix}.endpoint.region"] = str(config["region"])
    if not config.get("useInstanceProfile"):
        if config.get("accessKey"):
            conf[f"{prefix}.access.key"] = str(config["accessKey"])
        if config.get("secretKey"):
            conf[f"{prefix}.secret.key"] = str(config["secretKey"])
        if config.get("sessionToken"):
            conf[f"{prefix}.session.token"] = str(config["sessionToken"])
            conf[f"{prefix}.aws.credentials.provider"] = (
                "org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider"
            )
    for key, value in (config.get("extraProperties") or {}).items():
        conf[key if key.startswith("fs.") else f"{prefix}.{key}"] = str(value)
    return conf


def boto3_client(config: dict[str, Any]) -> Any:
    try:
        import boto3
        from botocore.config import Config as BotoConfig
    except ImportError as exc:  # pragma: no cover - packaging guard
        raise ConnectorError("boto3 is required for S3 metadata operations") from exc

    boto_config = BotoConfig(
        signature_version="s3v4",
        s3={"addressing_style": "path" if config.get("pathStyleAccess") else "auto"},
        connect_timeout=int(config.get("connectionTimeoutMs", 30_000)) // 1000,
        read_timeout=int(config.get("socketTimeoutMs", 60_000)) // 1000,
        retries={"max_attempts": 3, "mode": "standard"},
    )
    kwargs: dict[str, Any] = {
        "region_name": config.get("region", "us-east-1"),
        "config": boto_config,
        "verify": bool(config.get("sslVerify", True)),
    }
    if config.get("endpoint"):
        kwargs["endpoint_url"] = config["endpoint"]
    if not config.get("useInstanceProfile"):
        kwargs["aws_access_key_id"] = config.get("accessKey")
        kwargs["aws_secret_access_key"] = config.get("secretKey")
        if config.get("sessionToken"):
            kwargs["aws_session_token"] = config["sessionToken"]
    return boto3.client("s3", **kwargs)


@register_connector
class S3Connector(DataSourceConnector):
    source_types = (SourceType.S3,)
    display_name = "Amazon S3 / S3-compatible object storage"
    supports_listing = True

    def prepare_spark(self, spark: SparkSession, config: dict[str, Any]) -> None:
        hadoop = spark.sparkContext._jsc.hadoopConfiguration()
        for key, value in hadoop_conf_for(config).items():
            hadoop.set(key, value)

    def read(self, config: SourceContext, spark: SparkSession) -> DataFrame:
        self.prepare_spark(spark, config.resolved_config)
        source = config.source
        uri = s3a_uri(
            source.path or "",
            source.bucket or config.conn("bucket"),
            config.conn("basePath"),
        )
        fmt = detect_format(uri, source.format)
        if fmt == FileFormat.EXCEL:
            from reconx.connectors.excel import ExcelConnector

            return ExcelConnector().read(config, spark)
        options = build_read_options(source, fmt)
        schema = None
        if source.schema_spec and source.schema_spec.mode.value in ("explicit", "validate"):
            from reconx.spark.schema import build_struct_type

            schema = build_struct_type(source.schema_spec)
        log.info("s3.read", uri=uri, format=fmt.value, endpoint=config.conn("endpoint"))
        return read_files(spark, uri, fmt, options, schema)

    def write(self, dataframe: DataFrame, config: OutputContext) -> dict[str, Any]:
        spark = dataframe.sparkSession
        self.prepare_spark(spark, config.resolved_config)
        output = config.output
        uri = s3a_uri(output.path or "", config.conn("bucket"), config.conn("basePath"))
        fmt = output.format or FileFormat.PARQUET
        options = build_write_options(output.options, fmt)
        if output.compression:
            options["compression"] = output.compression
        writer = dataframe.write.format(spark_format_name(fmt)).mode(output.mode.value).options(**options)
        if output.partition_by:
            writer = writer.partitionBy(*output.partition_by)
        if output.max_records_per_file:
            writer = writer.option("maxRecordsPerFile", str(output.max_records_per_file))
        writer.save(uri)
        log.info("s3.write", uri=uri, format=fmt.value, mode=output.mode.value)
        return {"target": uri, "format": fmt.value, "mode": output.mode.value}

    def test_connection(self, config: dict[str, Any]) -> ConnectionTestResult:
        started = time.time()
        try:
            client = boto3_client(config)
            bucket = config.get("bucket")
            if bucket:
                client.head_bucket(Bucket=bucket)
                listing = client.list_objects_v2(Bucket=bucket, MaxKeys=1, Prefix=config.get("basePath") or "")
                details = {"bucket": bucket, "objectsFound": listing.get("KeyCount", 0)}
                message = f"Bucket '{bucket}' is reachable"
            else:
                buckets = client.list_buckets().get("Buckets", [])
                details = {"buckets": [b["Name"] for b in buckets[:20]], "bucketCount": len(buckets)}
                message = f"Endpoint reachable ({len(buckets)} bucket(s) visible)"
            return ConnectionTestResult(
                True, message, latency_ms=int((time.time() - started) * 1000), details=details
            )
        except Exception as exc:
            return ConnectionTestResult(
                False,
                f"S3 connection failed: {type(exc).__name__}: {exc}",
                latency_ms=int((time.time() - started) * 1000),
            )

    def validate(self, config: dict[str, Any]) -> list[str]:
        problems: list[str] = []
        if not config.get("useInstanceProfile"):
            problems.extend(self._require(config, "accessKey", "secretKey"))
        if config.get("endpoint") and not str(config["endpoint"]).startswith(("http://", "https://")):
            problems.append("'endpoint' must start with http:// or https://")
        if config.get("endpoint", "").startswith("http://") and config.get("sslEnabled", True):
            problems.append("'sslEnabled' should be false for an http:// endpoint")
        return problems

    def list_files(self, config: dict[str, Any], path: str, pattern: str | None = None) -> list[FileInfo]:

        client = boto3_client(config)
        uri = s3a_uri(path, config.get("bucket"), config.get("basePath"))
        bucket, key = split_s3_uri(uri)
        prefix, glob = _split_s3_glob(key)
        paginator = client.get_paginator("list_objects_v2")
        results: list[FileInfo] = []
        try:
            for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
                for obj in page.get("Contents", []):
                    obj_key = obj["Key"]
                    if glob and not fnmatch.fnmatch(obj_key, f"{prefix}{glob}" if prefix else glob):
                        continue
                    if pattern and not fnmatch.fnmatch(obj_key.rsplit("/", 1)[-1], pattern):
                        continue
                    modified = obj.get("LastModified")
                    results.append(
                        FileInfo(
                            path=f"s3a://{bucket}/{obj_key}",
                            size_bytes=int(obj.get("Size", 0)),
                            modified_at=modified.astimezone(UTC) if modified else None,
                            is_directory=obj_key.endswith("/"),
                        )
                    )
        except Exception as exc:
            raise ConnectionFailedError(f"S3 listing failed for '{uri}': {exc}") from exc
        return results

    def download(self, config: dict[str, Any], uri: str, destination: str) -> str:
        """Fetch a single object to the local staging directory (Excel only)."""
        client = boto3_client(config)
        bucket, key = split_s3_uri(s3a_uri(uri, config.get("bucket"), config.get("basePath")))
        client.download_file(bucket, key, destination)
        return destination


def _split_s3_glob(key: str) -> tuple[str, str | None]:
    parts = key.split("/")
    for index, part in enumerate(parts):
        if any(ch in part for ch in "*?["):
            prefix = "/".join(parts[:index])
            return (prefix + "/" if prefix else ""), "/".join(parts[index:])
    return key, None
