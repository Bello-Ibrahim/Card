"""Schema declaration, validation and evolution."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from reconx.common.errors import SchemaMismatchError, ValidationError
from reconx.common.logging import get_logger
from reconx.config.enums import SchemaMode
from reconx.config.models import SchemaSpec

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame
    from pyspark.sql.types import DataType, StructType

log = get_logger(__name__)

TYPE_ALIASES: dict[str, str] = {
    "str": "string",
    "text": "string",
    "varchar": "string",
    "char": "string",
    "int": "integer",
    "int32": "integer",
    "int64": "long",
    "bigint": "long",
    "smallint": "short",
    "tinyint": "byte",
    "number": "decimal(38,10)",
    "numeric": "decimal(38,10)",
    "money": "decimal(38,4)",
    "float64": "double",
    "float32": "float",
    "bool": "boolean",
    "datetime": "timestamp",
    "datetime2": "timestamp",
    "ts": "timestamp",
}


def normalise_type(type_name: str) -> str:
    cleaned = (type_name or "string").strip().lower()
    return TYPE_ALIASES.get(cleaned, cleaned)


def parse_data_type(type_name: str) -> DataType:
    from pyspark.sql.types import _parse_datatype_string

    try:
        return _parse_datatype_string(normalise_type(type_name))
    except Exception as exc:
        raise ValidationError(f"Unknown data type '{type_name}'") from exc


def build_struct_type(spec: SchemaSpec) -> StructType:
    """Translate a declarative schema into a Spark ``StructType``."""
    from pyspark.sql.types import StructField, StructType

    if not spec.fields:
        raise ValidationError("Cannot build a schema without fields")
    return StructType(
        [
            StructField(field.name, parse_data_type(field.type), field.nullable)
            for field in spec.fields
        ]
    )


def schema_to_spec_fields(dataframe: DataFrame) -> list[dict[str, Any]]:
    return [
        {"name": field.name, "type": field.dataType.simpleString(), "nullable": field.nullable}
        for field in dataframe.schema.fields
    ]


def apply_schema(dataframe: DataFrame, spec: SchemaSpec | None, *, source_id: str = "source") -> DataFrame:
    """Validate/coerce/evolve ``dataframe`` against the declared schema."""
    if spec is None or spec.mode == SchemaMode.INFER:
        return dataframe
    from pyspark.sql import functions as F

    declared = {field.name: field for field in spec.fields}
    actual = {field.name: field for field in dataframe.schema.fields}

    missing = [name for name in declared if name not in actual]
    extra = [name for name in actual if name not in declared]

    if missing and spec.fail_on_missing_columns and spec.mode in (SchemaMode.VALIDATE, SchemaMode.EXPLICIT):
        raise SchemaMismatchError(
            f"Source '{source_id}' is missing declared column(s): {', '.join(sorted(missing))}",
            details={"missing": sorted(missing), "actual": sorted(actual), "sourceId": source_id},
        )
    if extra and not spec.allow_extra_columns:
        raise SchemaMismatchError(
            f"Source '{source_id}' has undeclared column(s): {', '.join(sorted(extra))}",
            details={"extra": sorted(extra), "sourceId": source_id},
        )

    result = dataframe
    if spec.mode == SchemaMode.EVOLVE and missing:
        # Schema evolution: add declared-but-absent columns as typed NULLs so
        # downstream logic (keys, comparisons) keeps working across versions.
        for name in missing:
            field = declared[name]
            result = result.withColumn(name, F.lit(None).cast(parse_data_type(field.type)))
        log.info("schema.evolved", source=source_id, added_columns=sorted(missing))

    if spec.coerce_types:
        for name, field in declared.items():
            if name not in result.columns:
                continue
            target = parse_data_type(field.type)
            if result.schema[name].dataType != target:
                result = result.withColumn(name, F.col(name).cast(target))

    if spec.mode in (SchemaMode.EXPLICIT, SchemaMode.EVOLVE) and not spec.allow_extra_columns:
        result = result.select(*[name for name in declared if name in result.columns])
    return result


def compare_schemas(expected: SchemaSpec, dataframe: DataFrame) -> dict[str, Any]:
    """Report differences without raising - used by the UI's validation page."""
    declared = {f.name: normalise_type(f.type) for f in expected.fields}
    actual = {f.name: f.dataType.simpleString() for f in dataframe.schema.fields}
    type_mismatches = {
        name: {"expected": declared[name], "actual": actual[name]}
        for name in declared
        if name in actual and declared[name] != actual[name]
    }
    return {
        "missing": sorted(set(declared) - set(actual)),
        "extra": sorted(set(actual) - set(declared)),
        "typeMismatches": type_mismatches,
        "compatible": not (set(declared) - set(actual)) and not type_mismatches,
    }
