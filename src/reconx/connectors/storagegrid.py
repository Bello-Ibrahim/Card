"""NetApp StorageGRID connector.

StorageGRID speaks the S3 API, so the transport is shared with
:mod:`reconx.connectors.s3`.  What differs is the defaults and the validation:
an explicit endpoint is mandatory, path-style addressing is the norm, the
region is a tenant-defined string rather than an AWS region, and operators
frequently terminate TLS with an internal CA (hence ``sslVerify``).
"""

from __future__ import annotations

import time
from typing import Any

from reconx.config.enums import SourceType
from reconx.connectors.base import ConnectionTestResult, register_connector
from reconx.connectors.s3 import S3Connector, boto3_client


@register_connector
class StorageGridConnector(S3Connector):
    source_types = (SourceType.STORAGEGRID,)
    display_name = "NetApp StorageGRID (S3 API)"

    @staticmethod
    def _with_defaults(config: dict[str, Any]) -> dict[str, Any]:
        merged = dict(config)
        merged.setdefault("pathStyleAccess", True)
        merged.setdefault("region", "us-east-1")
        endpoint = str(merged.get("endpoint", ""))
        merged.setdefault("sslEnabled", endpoint.startswith("https://"))
        return merged

    def prepare_spark(self, spark: Any, config: dict[str, Any]) -> None:
        super().prepare_spark(spark, self._with_defaults(config))

    def read(self, config: Any, spark: Any) -> Any:
        config.resolved_config = self._with_defaults(config.resolved_config)
        return super().read(config, spark)

    def write(self, dataframe: Any, config: Any) -> dict[str, Any]:
        config.resolved_config = self._with_defaults(config.resolved_config)
        return super().write(dataframe, config)

    def list_files(self, config: dict[str, Any], path: str, pattern: str | None = None) -> list[Any]:
        return super().list_files(self._with_defaults(config), path, pattern)

    def test_connection(self, config: dict[str, Any]) -> ConnectionTestResult:
        config = self._with_defaults(config)
        started = time.time()
        try:
            client = boto3_client(config)
            bucket = config.get("bucket")
            if bucket:
                client.head_bucket(Bucket=bucket)
                message = f"StorageGRID bucket '{bucket}' is reachable"
                details: dict[str, Any] = {"bucket": bucket, "endpoint": config.get("endpoint")}
            else:
                buckets = client.list_buckets().get("Buckets", [])
                message = f"StorageGRID endpoint reachable ({len(buckets)} bucket(s))"
                details = {"buckets": [b["Name"] for b in buckets[:20]], "endpoint": config.get("endpoint")}
            details["tenantAccountId"] = config.get("tenantAccountId")
            return ConnectionTestResult(
                True, message, latency_ms=int((time.time() - started) * 1000), details=details
            )
        except Exception as exc:
            return ConnectionTestResult(
                False,
                f"StorageGRID connection failed: {type(exc).__name__}: {exc}",
                latency_ms=int((time.time() - started) * 1000),
                details={"endpoint": config.get("endpoint")},
            )

    def validate(self, config: dict[str, Any]) -> list[str]:
        problems = super().validate(self._with_defaults(config))
        if not config.get("endpoint"):
            problems.append("'endpoint' is required for StorageGRID (there is no default AWS endpoint)")
        return problems
