"""Local / shared filesystem connector (also used for NFS and mounted volumes).

Every node in the cluster must see the same path - that is a property of the
deployment (PVC / NFS mount), not of this connector, and it is called out in
the deployment documentation.
"""

from __future__ import annotations

import fnmatch
import os
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any

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


@register_connector
class FilesystemConnector(DataSourceConnector):
    source_types = (SourceType.FILESYSTEM,)
    display_name = "Local / mounted filesystem"
    supports_listing = True

    def read(self, config: SourceContext, spark: SparkSession) -> DataFrame:
        source = config.source
        path = self._resolve_path(config.resolved_config.get("basePath", ""), source.path or "")
        fmt = detect_format(path, source.format)
        if fmt == FileFormat.EXCEL:
            from reconx.connectors.excel import ExcelConnector

            return ExcelConnector().read(config, spark)
        options = build_read_options(source, fmt)
        schema = _schema_of(source)
        log.info("filesystem.read", path=path, format=fmt.value, options_count=len(options))
        return read_files(spark, path, fmt, options, schema)

    def write(self, dataframe: DataFrame, config: OutputContext) -> dict[str, Any]:
        output = config.output
        path = self._resolve_path(config.resolved_config.get("basePath", ""), output.path or "")
        fmt = output.format or FileFormat.PARQUET
        options = build_write_options(output.options, fmt)
        if output.compression:
            options["compression"] = output.compression
        writer = dataframe.write.format(spark_format_name(fmt)).mode(output.mode.value).options(**options)
        if output.partition_by:
            writer = writer.partitionBy(*output.partition_by)
        if output.max_records_per_file:
            writer = writer.option("maxRecordsPerFile", str(output.max_records_per_file))
        writer.save(path)
        log.info("filesystem.write", path=path, format=fmt.value, mode=output.mode.value)
        return {"target": path, "format": fmt.value, "mode": output.mode.value}

    def test_connection(self, config: dict[str, Any]) -> ConnectionTestResult:
        started = time.time()
        base = config.get("basePath", "/")
        path = Path(base)
        if not path.exists():
            if config.get("createMissingDirectories", True):
                try:
                    path.mkdir(parents=True, exist_ok=True)
                except OSError as exc:
                    return ConnectionTestResult(False, f"Cannot create base path '{base}': {exc}")
            else:
                return ConnectionTestResult(False, f"Base path '{base}' does not exist")
        readable = os.access(path, os.R_OK)
        writable = os.access(path, os.W_OK)
        if not readable:
            return ConnectionTestResult(False, f"Base path '{base}' is not readable")
        if config.get("writable", True) and not writable:
            return ConnectionTestResult(False, f"Base path '{base}' is not writable")
        return ConnectionTestResult(
            True,
            f"Filesystem path '{base}' is accessible",
            latency_ms=int((time.time() - started) * 1000),
            details={"readable": readable, "writable": writable},
        )

    def validate(self, config: dict[str, Any]) -> list[str]:
        problems = self._require(config, "basePath")
        base = config.get("basePath")
        if base and not str(base).startswith("/"):
            problems.append("'basePath' must be an absolute path")
        return problems

    def list_files(self, config: dict[str, Any], path: str, pattern: str | None = None) -> list[FileInfo]:
        target = Path(self._resolve_path(config.get("basePath", ""), path))
        base, glob = _split_glob(str(target))
        base_path = Path(base)
        if not base_path.exists():
            return []
        candidates: list[Path]
        if base_path.is_file():
            candidates = [base_path]
        elif glob:
            candidates = sorted(base_path.glob(glob))
        else:
            candidates = sorted(p for p in base_path.iterdir())
        results: list[FileInfo] = []
        for candidate in candidates:
            if pattern and not fnmatch.fnmatch(candidate.name, pattern):
                continue
            try:
                stat = candidate.stat()
            except OSError:  # pragma: no cover - race with a mover process
                continue
            results.append(
                FileInfo(
                    path=str(candidate),
                    size_bytes=stat.st_size,
                    modified_at=datetime.fromtimestamp(stat.st_mtime, tz=UTC),
                    is_directory=candidate.is_dir(),
                )
            )
        return results

    @staticmethod
    def _resolve_path(base: str, path: str) -> str:
        if not path:
            raise ConnectorError("Filesystem source requires a path")
        if path.startswith(("/", "file:", "hdfs:", "s3a:", "s3:")):
            return path
        return str(Path(base or "/") / path)


def _split_glob(path: str) -> tuple[str, str | None]:
    """Split ``/data/in/*.csv`` into ``('/data/in', '*.csv')``."""
    parts = Path(path).parts
    for index, part in enumerate(parts):
        if any(ch in part for ch in "*?["):
            return str(Path(*parts[:index]) if index else "/"), str(Path(*parts[index:]))
    return path, None


def _schema_of(source: Any) -> Any:
    from reconx.spark.schema import build_struct_type

    if source.schema_spec and source.schema_spec.mode.value in ("explicit", "validate"):
        return build_struct_type(source.schema_spec)
    return None


def check_path_available(
    connector: DataSourceConnector,
    config: dict[str, Any],
    path: str,
    *,
    pattern: str | None = None,
    min_count: int = 1,
    min_size_bytes: int = 1,
) -> tuple[bool, dict[str, Any]]:
    """Shared availability check used by the condition evaluator."""
    try:
        files = [f for f in connector.list_files(config, path, pattern) if not f.is_directory]
    except ConnectionFailedError:
        raise
    except Exception as exc:
        raise ConnectionFailedError(f"Could not list '{path}': {exc}") from exc
    non_empty = [f for f in files if f.size_bytes >= min_size_bytes]
    details = {
        "matchedFiles": len(files),
        "filesMeetingSize": len(non_empty),
        "totalBytes": sum(f.size_bytes for f in files),
        "sample": [f.to_dict() for f in files[:5]],
    }
    return len(non_empty) >= min_count, details
