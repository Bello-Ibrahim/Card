"""Excel (XLSX/XLSM/XLS) connector.

Spark has no native Excel reader.  Rather than pretend otherwise, this
connector reads the workbook with openpyxl on the driver and parallelises the
resulting rows into a DataFrame.  That is correct for the file sizes Excel is
actually used for; a hard row cap (``maxRows``, default 1,000,000) prevents a
surprise OOM on the driver and produces an explicit, actionable error instead.

Production guidance (see docs/CONNECTORS.md): for very large spreadsheets,
convert to Parquet/CSV upstream, or add the ``com.crealytics:spark-excel``
package and configure the source with ``format: csv`` on the converted output.
"""

from __future__ import annotations

import time
from pathlib import Path
from typing import TYPE_CHECKING, Any

from reconx.common.errors import ConnectorError, SchemaMismatchError
from reconx.common.logging import get_logger
from reconx.config.enums import SourceType
from reconx.connectors.base import (
    ConnectionTestResult,
    DataSourceConnector,
    OutputContext,
    SourceContext,
    register_connector,
)

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)

DEFAULT_MAX_ROWS = 1_000_000


@register_connector
class ExcelConnector(DataSourceConnector):
    source_types = (SourceType.EXCEL,)
    display_name = "Excel workbook (XLSX/XLSM)"
    supports_listing = False

    def read(self, config: SourceContext, spark: SparkSession) -> DataFrame:
        paths = self._materialise(config)
        return self.read_local(paths, config, spark)

    def read_local(self, paths: list[str], config: SourceContext, spark: SparkSession) -> DataFrame:
        source = config.source
        sheet = source.options.get("sheetName") or source.options.get("sheet")
        header_row = int(source.options.get("headerRow", 1))
        skip_rows = int(source.options.get("skipRows", 0))
        max_rows = int(source.options.get("maxRows", DEFAULT_MAX_ROWS))
        has_header = str(source.options.get("header", "true")).lower() != "false"

        rows: list[dict[str, Any]] = []
        columns: list[str] = []
        for path in paths:
            sheet_columns, sheet_rows = _read_workbook(
                path,
                sheet_name=sheet,
                header_row=header_row,
                skip_rows=skip_rows,
                has_header=has_header,
                max_rows=max_rows - len(rows),
            )
            if not columns:
                columns = sheet_columns
            elif sheet_columns != columns:
                raise SchemaMismatchError(
                    f"Excel files have inconsistent columns: {columns} vs {sheet_columns}",
                    details={"file": path},
                )
            rows.extend(sheet_rows)
            if len(rows) >= max_rows:
                raise ConnectorError(
                    f"Excel source '{source.id}' exceeds maxRows={max_rows}",
                    details={
                        "hint": "Convert the workbook to Parquet/CSV upstream, or raise the 'maxRows' option "
                        "after confirming the driver has enough memory"
                    },
                )
        log.info("excel.read", files=len(paths), rows=len(rows), columns=len(columns))
        if not rows:
            from pyspark.sql.types import StringType, StructField, StructType

            schema = StructType([StructField(c, StringType(), True) for c in columns or ["value"]])
            return spark.createDataFrame([], schema)

        explicit_schema = None
        if source.schema_spec and source.schema_spec.mode.value in ("explicit", "validate"):
            from reconx.spark.schema import build_struct_type

            explicit_schema = build_struct_type(source.schema_spec)
        parallelism = max(1, min(200, len(rows) // 50_000 + 1))
        rdd = spark.sparkContext.parallelize(rows, parallelism)
        if explicit_schema is not None:
            from pyspark.sql import functions as F

            df = spark.createDataFrame(rdd.map(lambda r: {k: (str(v) if v is not None else None) for k, v in r.items()}))
            for field in explicit_schema.fields:
                if field.name in df.columns:
                    df = df.withColumn(field.name, F.col(field.name).cast(field.dataType))
            return df
        return spark.createDataFrame(rdd)

    def _materialise(self, config: SourceContext) -> list[str]:
        """Bring the workbook onto local disk, whatever the underlying storage is."""
        source = config.source
        path = source.path or ""
        connection = config.connection
        conn_type = str(connection.type) if connection else "filesystem"
        staging = Path(config.staging_dir) / (config.run_id or "adhoc") / f"excel-{source.id}"
        staging.mkdir(parents=True, exist_ok=True)

        if conn_type in ("s3", "storagegrid"):
            from reconx.connectors.s3 import S3Connector

            s3 = S3Connector()
            files = s3.list_files(config.resolved_config, path, source.file_pattern)
            targets = []
            for info in [f for f in files if not f.is_directory] or [None]:
                uri = info.path if info else path
                local = staging / uri.rsplit("/", 1)[-1]
                s3.download(config.resolved_config, uri, str(local))
                targets.append(str(local))
            return targets
        if conn_type == "sftp":
            from reconx.connectors.sftp import SftpConnector

            return SftpConnector().download_files(
                config.resolved_config, path, str(staging), pattern=source.file_pattern
            )
        base = (config.resolved_config or {}).get("basePath", "")
        local_path = Path(base) / path if base and not path.startswith("/") else Path(path)
        if local_path.is_dir():
            pattern = source.file_pattern or "*.xls*"
            return [str(p) for p in sorted(local_path.glob(pattern))]
        if not local_path.exists():
            raise ConnectorError(f"Excel file '{local_path}' does not exist")
        return [str(local_path)]

    def write(self, dataframe: DataFrame, config: OutputContext) -> dict[str, Any]:
        """Write an XLSX workbook.

        Guarded by ``maxRows`` because producing a workbook necessarily collects
        rows onto the driver.
        """
        try:
            from openpyxl import Workbook
        except ImportError as exc:  # pragma: no cover
            raise ConnectorError("openpyxl is required to write Excel output") from exc

        max_rows = int(config.option("maxRows", 200_000))
        count = dataframe.count()
        if count > max_rows:
            raise ConnectorError(
                f"Refusing to write {count:,} rows to Excel (maxRows={max_rows:,})",
                details={"hint": "Use a Parquet/CSV output for large result sets"},
            )
        path = Path(config.output.path or "")
        path.parent.mkdir(parents=True, exist_ok=True)
        workbook = Workbook(write_only=True)
        sheet = workbook.create_sheet(str(config.option("sheetName", "Results")))
        sheet.append(list(dataframe.columns))
        for row in dataframe.toLocalIterator():
            sheet.append([row[c] for c in dataframe.columns])
        workbook.save(str(path))
        log.info("excel.write", path=str(path), rows=count)
        return {"target": str(path), "rows": count, "format": "excel"}

    def test_connection(self, config: dict[str, Any]) -> ConnectionTestResult:
        started = time.time()
        try:
            import openpyxl  # noqa: F401
        except ImportError:
            return ConnectionTestResult(False, "openpyxl is not installed")
        return ConnectionTestResult(
            True,
            "Excel support available (openpyxl); the workbook location is tested via its storage connection",
            latency_ms=int((time.time() - started) * 1000),
        )

    def validate(self, config: dict[str, Any]) -> list[str]:
        return []


def _read_workbook(
    path: str,
    *,
    sheet_name: str | None,
    header_row: int,
    skip_rows: int,
    has_header: bool,
    max_rows: int,
) -> tuple[list[str], list[dict[str, Any]]]:
    try:
        from openpyxl import load_workbook
    except ImportError as exc:  # pragma: no cover
        raise ConnectorError("openpyxl is required to read Excel files") from exc

    workbook = load_workbook(filename=path, read_only=True, data_only=True)
    try:
        if sheet_name:
            if sheet_name not in workbook.sheetnames:
                raise ConnectorError(
                    f"Sheet '{sheet_name}' not found in '{path}'",
                    details={"availableSheets": workbook.sheetnames},
                )
            worksheet = workbook[sheet_name]
        else:
            worksheet = workbook[workbook.sheetnames[0]]

        columns: list[str] = []
        rows: list[dict[str, Any]] = []
        for index, raw_row in enumerate(worksheet.iter_rows(values_only=True), start=1):
            if index < header_row:
                continue
            if index == header_row and has_header:
                columns = [
                    (str(value).strip() if value is not None else f"col_{i + 1}")
                    for i, value in enumerate(raw_row)
                ]
                continue
            if not columns:
                columns = [f"col_{i + 1}" for i in range(len(raw_row))]
            if index <= header_row + skip_rows:
                continue
            if all(value is None for value in raw_row):
                continue
            rows.append(
                {
                    columns[i] if i < len(columns) else f"col_{i + 1}": (
                        str(value) if value is not None else None
                    )
                    for i, value in enumerate(raw_row)
                }
            )
            if len(rows) >= max_rows:
                break
        return columns, rows
    finally:
        workbook.close()
