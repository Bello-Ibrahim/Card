"""File format handling shared by the file-oriented connectors."""

from __future__ import annotations

from pathlib import PurePosixPath
from typing import TYPE_CHECKING, Any

from reconx.common.errors import UnsupportedFormatError
from reconx.config.enums import FileFormat
from reconx.config.models import SourceSpec

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, DataFrameReader, SparkSession
    from pyspark.sql.types import StructType

EXTENSION_FORMATS: dict[str, FileFormat] = {
    ".csv": FileFormat.CSV,
    ".tsv": FileFormat.CSV,
    ".psv": FileFormat.CSV,
    ".txt": FileFormat.CSV,
    ".dat": FileFormat.CSV,
    ".json": FileFormat.JSON,
    ".jsonl": FileFormat.JSON,
    ".ndjson": FileFormat.JSON,
    ".parquet": FileFormat.PARQUET,
    ".pq": FileFormat.PARQUET,
    ".orc": FileFormat.ORC,
    ".avro": FileFormat.AVRO,
    ".xlsx": FileFormat.EXCEL,
    ".xlsm": FileFormat.EXCEL,
    ".xls": FileFormat.EXCEL,
}

#: Options accepted per format, with platform defaults.
CSV_DEFAULTS: dict[str, str] = {
    "header": "true",
    "inferSchema": "false",
    "delimiter": ",",
    "quote": '"',
    "escape": '"',
    "encoding": "UTF-8",
    "mode": "PERMISSIVE",
    "nullValue": "",
    "ignoreLeadingWhiteSpace": "true",
    "ignoreTrailingWhiteSpace": "true",
    "multiLine": "false",
}
JSON_DEFAULTS: dict[str, str] = {"multiLine": "false", "mode": "PERMISSIVE", "encoding": "UTF-8"}


def detect_format(path: str | None, declared: FileFormat | None = None) -> FileFormat:
    if declared:
        return declared
    if not path:
        raise UnsupportedFormatError("Cannot detect file format: no path and no explicit format")
    suffixes = PurePosixPath(path.split("?")[0]).suffixes
    for suffix in reversed(suffixes):
        fmt = EXTENSION_FORMATS.get(suffix.lower())
        if fmt:
            return fmt
    raise UnsupportedFormatError(
        f"Cannot infer the file format of '{path}'. Set 'format' explicitly.",
        details={"supported": sorted({f.value for f in EXTENSION_FORMATS.values()})},
    )


def build_read_options(source: SourceSpec, fmt: FileFormat) -> dict[str, str]:
    """Merge platform defaults with user options for the given format."""
    options: dict[str, str] = {}
    if fmt in (FileFormat.CSV, FileFormat.DELIMITED, FileFormat.TEXT):
        options.update(CSV_DEFAULTS)
        if source.schema_spec is None or source.schema_spec.mode.value == "infer":
            options["inferSchema"] = "true"
    elif fmt == FileFormat.JSON:
        options.update(JSON_DEFAULTS)
    if source.recursive:
        options["recursiveFileLookup"] = "true"
    if source.file_pattern:
        options["pathGlobFilter"] = source.file_pattern
    for key, value in source.options.items():
        if value is None:
            continue
        options[key] = str(value).lower() if isinstance(value, bool) else str(value)
    return options


def build_write_options(output_options: dict[str, Any], fmt: FileFormat) -> dict[str, str]:
    options: dict[str, str] = {}
    if fmt in (FileFormat.CSV, FileFormat.DELIMITED):
        options.update({"header": "true", "delimiter": ",", "quoteAll": "false", "escape": '"'})
    for key, value in (output_options or {}).items():
        if value is None:
            continue
        options[key] = str(value).lower() if isinstance(value, bool) else str(value)
    return options


def spark_format_name(fmt: FileFormat) -> str:
    mapping = {
        FileFormat.CSV: "csv",
        FileFormat.DELIMITED: "csv",
        FileFormat.TEXT: "csv",
        FileFormat.JSON: "json",
        FileFormat.PARQUET: "parquet",
        FileFormat.ORC: "orc",
        FileFormat.AVRO: "avro",
    }
    if fmt not in mapping:
        raise UnsupportedFormatError(
            f"Format '{fmt.value}' cannot be read natively by Spark",
            details={"hint": "Excel is handled by the Excel connector"},
        )
    return mapping[fmt]


def read_files(
    spark: SparkSession,
    path: str,
    fmt: FileFormat,
    options: dict[str, str],
    schema: StructType | None = None,
) -> DataFrame:
    """Distributed read of a path/glob with the configured format and schema."""
    reader: DataFrameReader = spark.read.format(spark_format_name(fmt)).options(**options)
    if schema is not None:
        reader = reader.schema(schema)
    return reader.load(path)
