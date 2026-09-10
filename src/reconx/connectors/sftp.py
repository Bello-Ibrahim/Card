"""SFTP connector.

Spark cannot read ``sftp://`` natively.  Files are staged into a shared staging
directory (a PVC/NFS mount in Kubernetes, or a local directory in dev) and then
read by Spark from there, so the *reconciliation* itself is still distributed.
The staging location is configurable and documented in the deployment guide.
"""

from __future__ import annotations

import fnmatch
import gzip
import os
import shutil
import stat as stat_module
import time
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any

from reconx.common.errors import ConnectionFailedError, ConnectorError
from reconx.common.logging import get_logger
from reconx.common.retry import call_with_retry
from reconx.config.enums import FileFormat, SourceType
from reconx.connectors.base import (
    ConnectionTestResult,
    DataSourceConnector,
    FileInfo,
    OutputContext,
    SourceContext,
    register_connector,
)
from reconx.connectors.formats import build_read_options, detect_format, read_files, spark_format_name

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)


@contextmanager
def sftp_session(config: dict[str, Any]) -> Any:
    """Open an authenticated SFTP session (password or private key)."""
    try:
        import paramiko
    except ImportError as exc:  # pragma: no cover - packaging guard
        raise ConnectorError("paramiko is required for the SFTP connector") from exc

    client = paramiko.SSHClient()
    known_hosts = config.get("knownHosts")
    if known_hosts and Path(known_hosts).is_file():
        client.load_host_keys(known_hosts)
    else:
        client.load_system_host_keys()
    if config.get("strictHostKeyChecking", True):
        client.set_missing_host_key_policy(paramiko.RejectPolicy())
    else:
        # Explicit opt-out, only ever used in development environments.
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # noqa: S507

    pkey = None
    if config.get("privateKey"):
        import io

        key_material = io.StringIO(str(config["privateKey"]))
        passphrase = config.get("privateKeyPassphrase")
        last_error: Exception | None = None
        for key_class in (paramiko.Ed25519Key, paramiko.ECDSAKey, paramiko.RSAKey):
            try:
                key_material.seek(0)
                pkey = key_class.from_private_key(key_material, password=passphrase)
                break
            except Exception as exc:
                last_error = exc
        if pkey is None:
            raise ConnectorError(f"Could not parse the configured SFTP private key: {last_error}")

    try:
        client.connect(
            hostname=config["host"],
            port=int(config.get("port", 22)),
            username=config.get("username"),
            # A password may accompany a key (some servers require both factors).
            password=config.get("password"),
            pkey=pkey,
            timeout=int(config.get("timeoutSeconds", 30)),
            banner_timeout=int(config.get("timeoutSeconds", 30)),
            auth_timeout=int(config.get("timeoutSeconds", 30)),
            compress=bool(config.get("compression", False)),
            look_for_keys=False,
            allow_agent=False,
        )
    except Exception as exc:
        raise ConnectionFailedError(
            f"SFTP connection to {config.get('host')}:{config.get('port', 22)} failed: {exc}"
        ) from exc
    sftp = client.open_sftp()
    try:
        yield sftp
    finally:
        try:
            sftp.close()
        finally:
            client.close()


@register_connector
class SftpConnector(DataSourceConnector):
    source_types = (SourceType.SFTP,)
    display_name = "SFTP server"
    supports_listing = True

    def read(self, config: SourceContext, spark: SparkSession) -> DataFrame:
        source = config.source
        remote_path = _join(config.conn("basePath", "/"), source.path or "")
        staging = Path(config.staging_dir) / (config.run_id or "adhoc") / (source.id or "sftp")
        staging.mkdir(parents=True, exist_ok=True)
        downloaded = self.download_files(
            config.resolved_config,
            remote_path,
            str(staging),
            pattern=source.file_pattern,
            retry_policy=config.retry_policy,
        )
        if not downloaded:
            raise ConnectionFailedError(
                f"No files matched '{remote_path}'"
                + (f" with pattern '{source.file_pattern}'" if source.file_pattern else "")
            )
        fmt = detect_format(downloaded[0], source.format)
        if fmt == FileFormat.EXCEL:
            from reconx.connectors.excel import ExcelConnector

            return ExcelConnector().read_local(downloaded, config, spark)
        options = build_read_options(source, fmt)
        schema = None
        if source.schema_spec and source.schema_spec.mode.value in ("explicit", "validate"):
            from reconx.spark.schema import build_struct_type

            schema = build_struct_type(source.schema_spec)
        log.info("sftp.read", remote=remote_path, staged=len(downloaded), format=fmt.value)
        return read_files(spark, str(staging), fmt, options, schema)

    def write(self, dataframe: DataFrame, config: OutputContext) -> dict[str, Any]:
        """Write locally, then upload the produced part files over SFTP."""
        output = config.output
        staging = Path(config.staging_dir) / (config.run_id or "adhoc") / "sftp-out"
        staging.mkdir(parents=True, exist_ok=True)
        fmt = output.format or FileFormat.CSV
        local_dir = staging / (output.id or "output")
        dataframe.coalesce(int(config.option("coalesce", 1))).write.format(
            spark_format_name(fmt)
        ).mode("overwrite").options(header="true").save(f"file://{local_dir}")
        uploaded: list[str] = []
        remote_dir = _join(config.conn("basePath", "/"), output.path or "")
        with sftp_session(config.resolved_config) as sftp:
            _mkdirs(sftp, remote_dir)
            for part in sorted(local_dir.glob("part-*")):
                remote_name = f"{remote_dir.rstrip('/')}/{output.id or 'output'}-{part.name}"
                sftp.put(str(part), remote_name)
                uploaded.append(remote_name)
        log.info("sftp.write", remote_dir=remote_dir, files=len(uploaded))
        return {"target": remote_dir, "filesUploaded": len(uploaded), "files": uploaded[:20]}

    def test_connection(self, config: dict[str, Any]) -> ConnectionTestResult:
        started = time.time()
        try:
            with sftp_session(config) as sftp:
                base = config.get("basePath", "/")
                entries = sftp.listdir(base)
                return ConnectionTestResult(
                    True,
                    f"Connected to {config.get('host')} - '{base}' contains {len(entries)} entrie(s)",
                    latency_ms=int((time.time() - started) * 1000),
                    details={"basePath": base, "sample": entries[:10]},
                )
        except Exception as exc:
            return ConnectionTestResult(
                False,
                f"SFTP connection failed: {type(exc).__name__}: {exc}",
                latency_ms=int((time.time() - started) * 1000),
            )

    def validate(self, config: dict[str, Any]) -> list[str]:
        problems = self._require(config, "host", "username")
        if not config.get("password") and not config.get("privateKey"):
            problems.append("either 'password' or 'privateKey' must be provided")
        if not config.get("strictHostKeyChecking", True):
            problems.append(
                "WARNING: 'strictHostKeyChecking' is disabled - acceptable in dev only"
            )
        return problems

    def list_files(self, config: dict[str, Any], path: str, pattern: str | None = None) -> list[FileInfo]:
        target = _join(config.get("basePath", "/"), path)
        directory, glob = _split_remote_glob(target)
        effective_pattern = pattern or glob
        with sftp_session(config) as sftp:
            try:
                attrs = sftp.listdir_attr(directory)
            except FileNotFoundError:
                return []
            except OSError as exc:
                raise ConnectionFailedError(f"SFTP listing failed for '{directory}': {exc}") from exc
            results: list[FileInfo] = []
            for attr in attrs:
                name = attr.filename
                if effective_pattern and not fnmatch.fnmatch(name, effective_pattern):
                    continue
                results.append(
                    FileInfo(
                        path=f"{directory.rstrip('/')}/{name}",
                        size_bytes=int(attr.st_size or 0),
                        modified_at=(
                            datetime.fromtimestamp(attr.st_mtime, tz=UTC) if attr.st_mtime else None
                        ),
                        is_directory=bool(attr.st_mode and stat_module.S_ISDIR(attr.st_mode)),
                    )
                )
            return results

    def download_files(
        self,
        config: dict[str, Any],
        remote_path: str,
        destination: str,
        *,
        pattern: str | None = None,
        retry_policy: Any = None,
    ) -> list[str]:
        """Download matching files, transparently decompressing ``.gz``."""
        from reconx.common.retry import RetryPolicy

        policy = retry_policy or RetryPolicy()
        files = call_with_retry(
            lambda: self.list_files(config, remote_path, pattern),
            policy=policy,
            operation="sftp.list",
        )
        files = [f for f in files if not f.is_directory]
        if not files and not any(ch in remote_path for ch in "*?["):
            files = [FileInfo(path=remote_path)]
        downloaded: list[str] = []
        Path(destination).mkdir(parents=True, exist_ok=True)
        with sftp_session(config) as sftp:
            for info in files:
                name = info.path.rsplit("/", 1)[-1]
                local = Path(destination) / name
                call_with_retry(
                    lambda p=info.path, target=str(local): sftp.get(p, target),
                    policy=policy,
                    operation="sftp.get",
                )
                if name.endswith(".gz"):
                    unzipped = Path(destination) / name[:-3]
                    with gzip.open(local, "rb") as src, open(unzipped, "wb") as dst:
                        shutil.copyfileobj(src, dst)
                    os.remove(local)
                    local = unzipped
                downloaded.append(str(local))
        log.info("sftp.downloaded", count=len(downloaded), destination=destination)
        return downloaded


def _join(base: str, path: str) -> str:
    if not path:
        return base or "/"
    if path.startswith("/"):
        return path
    return f"{(base or '/').rstrip('/')}/{path.lstrip('/')}"


def _split_remote_glob(path: str) -> tuple[str, str | None]:
    parts = path.split("/")
    for index, part in enumerate(parts):
        if any(ch in part for ch in "*?["):
            return "/".join(parts[:index]) or "/", "/".join(parts[index:])
    return path, None


def _mkdirs(sftp: Any, remote_dir: str) -> None:
    current = ""
    for part in remote_dir.strip("/").split("/"):
        current = f"{current}/{part}"
        try:
            sftp.stat(current)
        except FileNotFoundError:
            sftp.mkdir(current)
