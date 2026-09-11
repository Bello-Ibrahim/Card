"""Pydantic models describing a reconciliation definition.

These models are the contract between the UI, the API, MongoDB and the Spark
engine.  They are intentionally permissive on input (accepting both camelCase
and snake_case, and the shorthand forms used in the YAML examples) but strict
on semantics - see :mod:`reconx.config.validation` for cross-field rules.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from reconx.common.timeutils import utcnow
from reconx.config.enums import (
    AggregateFunction,
    ComparisonRule,
    ConditionOperator,
    ConditionType,
    DataQualityAction,
    DataQualityCheckType,
    DefinitionStatus,
    EventFailureMode,
    FileFormat,
    LogicalOperator,
    MatchCategory,
    NotifyOn,
    OutputType,
    ScheduleType,
    SchemaMode,
    SourceType,
    TransformType,
    WriteMode,
)

RESERVED_PREFIX = "__reconx"


def _to_camel(value: str) -> str:
    head, *tail = value.split("_")
    return head + "".join(part.capitalize() for part in tail)


class ReconXModel(BaseModel):
    """Base model: camelCase on the wire, snake_case in Python."""

    model_config = ConfigDict(
        alias_generator=_to_camel,
        populate_by_name=True,
        extra="forbid",
        use_enum_values=False,
        str_strip_whitespace=True,
    )

    def dump(self) -> dict[str, Any]:
        """Canonical persistence form (aliases, enums as values, no Nones dropped)."""
        return self.model_dump(by_alias=True, mode="json", exclude_none=True)


# --------------------------------------------------------------------------- #
# Normalisation / key definition
# --------------------------------------------------------------------------- #
class Normalization(ReconXModel):
    """Value normalisation applied before keys are built or fields compared."""

    trim: bool = True
    case: Literal["none", "upper", "lower"] = "none"
    null_as: str | None = Field(default="", description="Replacement for NULL when building keys")
    strip_leading_zeros: bool = False
    remove_characters: str | None = Field(default=None, description="Regex of characters to strip")
    numeric_scale: int | None = Field(default=None, ge=0, le=18)
    date_format: str | None = Field(default=None, description="Output format, e.g. yyyy-MM-dd")
    parse_date_formats: list[str] = Field(default_factory=list)
    pad_left: int | None = Field(default=None, ge=0, le=64)
    pad_character: str = "0"
    expression: str | None = Field(
        default=None,
        description="Spark SQL expression; the column is available as ${col}",
    )


class KeyMapping(ReconXModel):
    """One component of the reconciliation key."""

    model_config = ConfigDict(
        alias_generator=_to_camel, populate_by_name=True, extra="allow", str_strip_whitespace=True
    )

    left: str | None = None
    right: str | None = None
    alias: str | None = None
    normalization: Normalization | None = None

    def resolve(self, left_source: str, right_source: str) -> KeyMapping:
        """Support the ``{source_a: col, source_b: col}`` shorthand."""
        if self.left and self.right:
            return self
        extras = {k: v for k, v in (self.model_extra or {}).items() if isinstance(v, str)}
        left = self.left or extras.get(left_source)
        right = self.right or extras.get(right_source)
        if left is None or right is None:
            # positional fallback for anonymous shorthand
            values = [v for k, v in extras.items() if k not in {"left", "right", "alias"}]
            if len(values) >= 2:
                left, right = values[0], values[1]
            elif len(values) == 1:
                left = right = values[0]
        if not left or not right:
            raise ValueError(
                "Key mapping must define 'left'/'right' or "
                f"'{left_source}'/'{right_source}' column names (got {extras or self.model_dump()})"
            )
        return self.model_copy(update={"left": left, "right": right})

    @property
    def key_alias(self) -> str:
        return self.alias or (self.left or "key")


class FieldComparison(ReconXModel):
    """A field-level comparison executed for keys present on both sides."""

    model_config = ConfigDict(
        alias_generator=_to_camel, populate_by_name=True, extra="allow", str_strip_whitespace=True
    )

    left: str | None = None
    right: str | None = None
    name: str | None = None
    rule: ComparisonRule = ComparisonRule.EXACT
    tolerance: float | None = None
    tolerance_unit: Literal["absolute", "percent", "seconds", "minutes", "hours", "days"] | None = None
    expression: str | None = Field(
        default=None,
        description="Spark SQL boolean expression using left.<col> / right.<col> aliases",
    )
    normalization: Normalization | None = None
    null_equals_null: bool = True
    case_sensitive: bool = True
    critical: bool = Field(default=True, description="Non-critical mismatches are reported but not fatal")

    def resolve(self, left_source: str, right_source: str) -> FieldComparison:
        if self.left and self.right:
            return self
        extras = {k: v for k, v in (self.model_extra or {}).items() if isinstance(v, str)}
        left = self.left or extras.get(left_source) or extras.get("sourceField")
        right = self.right or extras.get(right_source) or extras.get("targetField")
        if not left and not right:
            values = [
                v
                for k, v in extras.items()
                if k not in {"rule", "comparison", "tolerance", "expression", "name"}
            ]
            if len(values) >= 2:
                left, right = values[0], values[1]
            elif len(values) == 1:
                left = right = values[0]
        if not left or not right:
            raise ValueError("Field comparison must define left/right (or sourceField/targetField)")
        return self.model_copy(update={"left": left, "right": right})

    @model_validator(mode="before")
    @classmethod
    def _accept_comparison_alias(cls, data: Any) -> Any:
        if isinstance(data, dict) and "comparison" in data and "rule" not in data:
            data = {**data, "rule": data.pop("comparison")}
        return data

    @property
    def field_name(self) -> str:
        return self.name or self.left or "field"



class MatchRule(ReconXModel):
    """A named group of field comparisons - one *matching logic*.

    A leg may carry several matching logics (e.g. "amount & currency agree" OR
    "external reference agrees").  Comparisons inside a rule are combined with
    ``operator``; rules themselves are combined by :class:`MatchLogic`.
    """

    id: str = Field(default="rule_1", pattern=r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")
    name: str | None = None
    description: str | None = None
    enabled: bool = True
    operator: LogicalOperator = Field(
        default=LogicalOperator.AND, description="How the comparisons inside this rule combine"
    )
    negate: bool = Field(default=False, description="Invert the rule outcome (NOT)")
    comparisons: list[FieldComparison] = Field(min_length=1)

    @property
    def label(self) -> str:
        return self.name or self.id

    def resolve(self, left_source: str, right_source: str) -> MatchRule:
        return self.model_copy(
            update={"comparisons": [c.resolve(left_source, right_source) for c in self.comparisons]}
        )


class MatchLogic(ReconXModel):
    """Boolean combination of matching logics, optionally nested.

    ``operator`` says how the direct ``rules`` and nested ``groups`` combine:
    with ``AND`` every rule must hold for a record pair to be MATCHED, with
    ``OR`` any single rule is enough.  ``negate`` applies NOT to the whole
    group, so arbitrary boolean expressions can be expressed from the UI.
    """

    id: str | None = None
    name: str | None = None
    operator: LogicalOperator = LogicalOperator.AND
    negate: bool = False
    rules: list[MatchRule] = Field(default_factory=list)
    groups: list[MatchLogic] = Field(default_factory=list)

    @model_validator(mode="after")
    def _validate(self) -> MatchLogic:
        if not self.rules and not self.groups:
            raise ValueError("matchLogic requires at least one rule or nested group")
        ids = [r.id for r in self.rules]
        if len(set(ids)) != len(ids):
            raise ValueError(f"duplicate matching-rule ids within a group: {ids}")
        return self

    def resolve(self, left_source: str, right_source: str) -> MatchLogic:
        return self.model_copy(
            update={
                "rules": [r.resolve(left_source, right_source) for r in self.rules],
                "groups": [g.resolve(left_source, right_source) for g in self.groups],
            }
        )

    def all_rules(self) -> list[MatchRule]:
        out = [r for r in self.rules if r.enabled]
        for group in self.groups:
            out.extend(group.all_rules())
        return out

    def all_comparisons(self) -> list[FieldComparison]:
        return [c for rule in self.all_rules() for c in rule.comparisons]

    def describe(self) -> str:
        """Readable boolean expression, e.g. ``NOT (amount_rule AND ref_rule)``."""
        parts = [
            (f"NOT {r.label}" if r.negate else r.label) for r in self.rules if r.enabled
        ] + [g.describe() for g in self.groups]
        if not parts:
            return "TRUE"
        joined = f" {self.operator.value} ".join(parts)
        expr = joined if len(parts) == 1 else f"({joined})"
        return f"NOT {expr}" if self.negate else expr


MatchLogic.model_rebuild()


class AggregateComparison(ReconXModel):
    """Aggregate-level reconciliation (COUNT / SUM / MIN / MAX / AVG)."""

    name: str | None = None
    function: AggregateFunction = AggregateFunction.COUNT
    left_field: str | None = None
    right_field: str | None = None
    group_by: list[KeyMapping] = Field(default_factory=list)
    tolerance: float = 0.0
    tolerance_unit: Literal["absolute", "percent"] = "absolute"

    @property
    def label(self) -> str:
        base = self.name or f"{self.function.value}({self.left_field or '*'})"
        return base

    @model_validator(mode="after")
    def _validate_fields(self) -> AggregateComparison:
        if self.function != AggregateFunction.COUNT and not (self.left_field and self.right_field):
            raise ValueError(f"Aggregate {self.function.value} requires leftField and rightField")
        return self


# --------------------------------------------------------------------------- #
# Schema / data quality / transformations
# --------------------------------------------------------------------------- #
class SchemaField(ReconXModel):
    name: str
    type: str = "string"
    nullable: bool = True
    description: str | None = None


class SchemaSpec(ReconXModel):
    mode: SchemaMode = SchemaMode.INFER
    fields: list[SchemaField] = Field(default_factory=list)
    allow_extra_columns: bool = True
    fail_on_missing_columns: bool = True
    coerce_types: bool = True

    @model_validator(mode="after")
    def _fields_required(self) -> SchemaSpec:
        if self.mode in (SchemaMode.EXPLICIT, SchemaMode.VALIDATE) and not self.fields:
            raise ValueError(f"schema.mode={self.mode.value} requires at least one field")
        return self


class DataQualityCheck(ReconXModel):
    id: str | None = None
    type: DataQualityCheckType
    columns: list[str] = Field(default_factory=list)
    on_failure: DataQualityAction = DataQualityAction.STOP
    threshold: float | None = Field(default=None, description="Max failing ratio (0-1) or absolute count")
    min_rows: int | None = None
    max_rows: int | None = None
    min_value: float | None = None
    max_value: float | None = None
    pattern: str | None = None
    expected_type: str | None = None
    date_format: str | None = None
    sql: str | None = Field(default=None, description="Boolean Spark SQL expression that must hold")
    description: str | None = None

    @model_validator(mode="after")
    def _validate(self) -> DataQualityCheck:
        needs_columns = {
            DataQualityCheckType.NOT_NULL,
            DataQualityCheckType.UNIQUE,
            DataQualityCheckType.COLUMN_EXISTS,
            DataQualityCheckType.DATA_TYPE,
            DataQualityCheckType.DATE_VALID,
            DataQualityCheckType.RANGE,
            DataQualityCheckType.REGEX,
        }
        if self.type in needs_columns and not self.columns:
            raise ValueError(f"Data quality check '{self.type.value}' requires 'columns'")
        if self.type == DataQualityCheckType.CUSTOM_SQL and not self.sql:
            raise ValueError("custom_sql data quality check requires 'sql'")
        if self.type == DataQualityCheckType.ROW_COUNT and self.min_rows is None and self.max_rows is None:
            raise ValueError("row_count check requires minRows and/or maxRows")
        return self


class Transformation(ReconXModel):
    """A single declarative transformation step."""

    model_config = ConfigDict(
        alias_generator=_to_camel, populate_by_name=True, extra="allow", str_strip_whitespace=True
    )

    id: str | None = None
    type: TransformType
    description: str | None = None
    # select / drop / distinct / dedupe
    columns: list[str] = Field(default_factory=list)
    # rename
    mapping: dict[str, str] = Field(default_factory=dict)
    # cast / fill_null / derive
    fields: dict[str, str] = Field(default_factory=dict)
    # filter / join condition
    condition: str | None = None
    expression: str | None = None
    # sql
    sql: str | None = None
    view_name: str | None = None
    # aggregate
    group_by: list[str] = Field(default_factory=list)
    aggregations: dict[str, str] = Field(default_factory=dict)
    # join / union
    with_source: str | None = None
    join_type: str = "inner"
    join_keys: list[str] = Field(default_factory=list)
    # dedupe / order
    order_by: list[str] = Field(default_factory=list)
    keep: Literal["first", "last", "any"] = "first"
    ascending: bool = True
    # limit / repartition
    limit: int | None = None
    num_partitions: int | None = None
    partition_by: list[str] = Field(default_factory=list)
    # normalize / string / date ops
    normalization: Normalization | None = None
    operation: str | None = None
    format: str | None = None
    value: Any = None

    @model_validator(mode="after")
    def _validate_required(self) -> Transformation:
        t = self.type
        if t in (TransformType.SELECT, TransformType.DROP) and not self.columns:
            raise ValueError(f"transformation '{t.value}' requires 'columns'")
        if t == TransformType.RENAME and not self.mapping:
            raise ValueError("transformation 'rename' requires 'mapping'")
        if t == TransformType.CAST and not self.fields:
            raise ValueError("transformation 'cast' requires 'fields' (column -> type)")
        if t == TransformType.DERIVE and not self.fields:
            raise ValueError("transformation 'derive' requires 'fields' (column -> SQL expression)")
        if t == TransformType.FILTER and not (self.condition or self.expression):
            raise ValueError("transformation 'filter' requires 'condition'")
        if t in (TransformType.SQL, TransformType.TEMP_VIEW) and not self.sql:
            raise ValueError(f"transformation '{t.value}' requires 'sql'")
        if t == TransformType.TEMP_VIEW and not self.view_name:
            raise ValueError("transformation 'temp_view' requires 'viewName'")
        if t == TransformType.AGGREGATE and not self.aggregations:
            raise ValueError("transformation 'aggregate' requires 'aggregations'")
        if t == TransformType.JOIN and not (self.with_source and (self.join_keys or self.condition)):
            raise ValueError("transformation 'join' requires 'withSource' and 'joinKeys' or 'condition'")
        if t == TransformType.UNION and not self.with_source:
            raise ValueError("transformation 'union' requires 'withSource'")
        if t == TransformType.NORMALIZE and not (self.columns and self.normalization):
            raise ValueError("transformation 'normalize' requires 'columns' and 'normalization'")
        if t == TransformType.LIMIT and not self.limit:
            raise ValueError("transformation 'limit' requires 'limit'")
        return self


# --------------------------------------------------------------------------- #
# Sources / outputs
# --------------------------------------------------------------------------- #

class VariableSpec(ReconXModel):
    """A user-supplied string variable usable anywhere in the configuration.

    Variables are referenced as ``${name}`` in queries, table names, paths,
    filters and connection fields, and are rendered at run time by
    :mod:`reconx.common.templating`.  Declaring them here lets the UI prompt the
    officer for values (with defaults) and lets validation flag typos.
    """

    name: str = Field(pattern=r"^[a-zA-Z_][a-zA-Z0-9_]{0,63}$")
    label: str | None = None
    description: str | None = None
    default: str | None = None
    type: Literal["string", "number", "date", "boolean", "choice"] = "string"
    choices: list[str] = Field(default_factory=list)
    required: bool = True
    prompt_at_run: bool = Field(
        default=False, description="Ask the operator for a value when starting a manual run"
    )

    @model_validator(mode="after")
    def _validate(self) -> VariableSpec:
        if self.type == "choice" and not self.choices:
            raise ValueError(f"variable '{self.name}': type 'choice' requires 'choices'")
        if self.required and self.default is None and not self.prompt_at_run:
            # Not fatal: the value may come from run parameters or the standard
            # built-ins (business_date and friends).
            pass
        return self


class SourceSpec(ReconXModel):
    """An input dataset for a leg."""

    id: str = Field(pattern=r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")
    name: str | None = None
    type: SourceType
    connection_ref: str | None = Field(default=None, description="Connection document id")
    description: str | None = None

    # location - meaning depends on type
    path: str | None = None
    bucket: str | None = None
    table: str | None = None
    query: str | None = None
    topic: str | None = None
    view: str | None = Field(default=None, description="Temp view name for type=temp_view")
    leg_ref: str | None = Field(default=None, description="Producing leg id for type=leg_output")
    leg_output_ref: str | None = Field(default=None, description="Output id inside the producing leg")
    inline_rows: list[dict[str, Any]] = Field(default_factory=list)

    #: SQL dialect the ``query`` is written in.  Purely declarative - the query
    #: is sent to the database verbatim - but it drives UI syntax hints and the
    #: preview behaviour.
    dialect: Literal["generic", "mssql", "postgresql", "mysql", "oracle", "db2", "sqlite"] = "generic"

    format: FileFormat | None = None
    file_pattern: str | None = None
    recursive: bool = False
    options: dict[str, Any] = Field(default_factory=dict)

    schema_spec: SchemaSpec | None = Field(default=None, alias="schema")
    transformations: list[Transformation] = Field(default_factory=list)
    data_quality: list[DataQualityCheck] = Field(default_factory=list)
    filter: str | None = None
    register_temp_view: str | None = None
    repartition: int | None = None
    cache: bool = False
    broadcast: bool = Field(default=False, description="Hint Spark to broadcast this side of the join")

    @model_validator(mode="after")
    def _validate_location(self) -> SourceSpec:
        t = self.type
        if t in (SourceType.S3, SourceType.STORAGEGRID) and not self.path:
            raise ValueError(f"source '{self.id}': type {t.value} requires 'path'")
        if t in (SourceType.FILESYSTEM, SourceType.EXCEL, SourceType.SFTP) and not self.path:
            raise ValueError(f"source '{self.id}': type {t.value} requires 'path'")
        if t == SourceType.JDBC and not (self.table or self.query):
            raise ValueError(f"source '{self.id}': jdbc source requires 'table' or 'query'")
        if t == SourceType.KAFKA and not self.topic:
            raise ValueError(f"source '{self.id}': kafka source requires 'topic'")
        if t == SourceType.TEMP_VIEW and not self.view:
            raise ValueError(f"source '{self.id}': temp_view source requires 'view'")
        if t == SourceType.LEG_OUTPUT and not self.leg_ref:
            raise ValueError(f"source '{self.id}': leg_output source requires 'legRef'")
        if t == SourceType.INLINE and not self.inline_rows:
            raise ValueError(f"source '{self.id}': inline source requires 'inlineRows'")
        needs_connection = {
            SourceType.S3,
            SourceType.STORAGEGRID,
            SourceType.SFTP,
            SourceType.JDBC,
            SourceType.KAFKA,
        }
        if t in needs_connection and not self.connection_ref:
            raise ValueError(f"source '{self.id}': type {t.value} requires 'connectionRef'")
        if self.id.startswith(RESERVED_PREFIX):
            raise ValueError(f"source id '{self.id}' uses the reserved prefix '{RESERVED_PREFIX}'")
        return self


class OutputSpec(ReconXModel):
    """Where reconciliation results (or exceptions) are written."""

    id: str | None = None
    type: OutputType = OutputType.NONE
    connection_ref: str | None = None
    path: str | None = None
    table: str | None = None
    topic: str | None = None
    view: str | None = None
    format: FileFormat = FileFormat.PARQUET
    mode: WriteMode = WriteMode.APPEND
    partition_by: list[str] = Field(default_factory=list)
    categories: list[MatchCategory] = Field(
        default_factory=list, description="Empty = all categories"
    )
    columns: list[str] = Field(default_factory=list)
    options: dict[str, Any] = Field(default_factory=dict)
    max_records_per_file: int | None = None
    compression: str | None = None
    enabled: bool = True

    @model_validator(mode="after")
    def _validate_target(self) -> OutputSpec:
        t = self.type
        if t == OutputType.JDBC and not self.table:
            raise ValueError("jdbc output requires 'table'")
        if t in (OutputType.S3, OutputType.STORAGEGRID, OutputType.FILESYSTEM, OutputType.SFTP) and not self.path:
            raise ValueError(f"{t.value} output requires 'path'")
        if t == OutputType.KAFKA and not self.topic:
            raise ValueError("kafka output requires 'topic'")
        if t == OutputType.TEMP_VIEW and not self.view:
            raise ValueError("temp_view output requires 'view'")
        needs_connection = (
            OutputType.JDBC, OutputType.S3, OutputType.STORAGEGRID, OutputType.KAFKA, OutputType.SFTP
        )
        if t in needs_connection and not self.connection_ref:
            raise ValueError(f"{t.value} output requires 'connectionRef'")
        return self



class ExceptionColumn(ReconXModel):
    """A business column carried into the exceptions output.

    Exceptions are what an officer actually works from, so they need context -
    the customer name, the trade date, the account - not just the key and the
    field that broke.  Declare those columns here and the engine copies them
    onto every exception record for the leg.

    Shorthand: a bare string (``"trade_date"``) means "take this column from the
    left source, falling back to the right one when the record only exists on
    the right".
    """

    model_config = ConfigDict(
        alias_generator=_to_camel, populate_by_name=True, extra="forbid", str_strip_whitespace=True
    )

    alias: str = Field(pattern=r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")
    left: str | None = Field(default=None, description="Column name on the left source")
    right: str | None = Field(default=None, description="Column name on the right source")
    source: Literal["left", "right", "coalesce", "both"] = "coalesce"
    label: str | None = None

    @model_validator(mode="before")
    @classmethod
    def _accept_shorthand(cls, data: Any) -> Any:
        if isinstance(data, str):
            return {"alias": data, "left": data, "right": data, "source": "coalesce"}
        if isinstance(data, dict):
            data = dict(data)
            if "column" in data and "alias" not in data:
                data["alias"] = data["column"]
            if "column" in data:
                column = data.pop("column")
                data.setdefault("left", column)
                data.setdefault("right", column)
        return data

    @model_validator(mode="after")
    def _validate(self) -> ExceptionColumn:
        if not self.left and not self.right:
            raise ValueError(f"exception column '{self.alias}' must define 'left' and/or 'right'")
        if self.source == "left" and not self.left:
            raise ValueError(f"exception column '{self.alias}': source 'left' requires 'left'")
        if self.source == "right" and not self.right:
            raise ValueError(f"exception column '{self.alias}': source 'right' requires 'right'")
        return self


class MatchingOptions(ReconXModel):
    """Per-leg switches controlling how matching behaves."""

    null_equals_null: bool = True
    case_insensitive_keys: bool = False
    trim_keys: bool = True
    key_separator: str = "|"
    duplicate_detection: bool = True
    fail_on_duplicates: bool = False
    treat_duplicates_as_exceptions: bool = True
    broadcast_smaller_side: bool = True
    ignore_extra_left_columns: bool = False
    exception_threshold: int | None = Field(
        default=None, description="Absolute number of exceptions above which the run is PARTIAL_SUCCESS"
    )
    exception_threshold_percent: float | None = Field(default=None, ge=0, le=100)
    max_exception_records: int = Field(
        default=1_000_000, description="Safety cap on exception rows persisted per leg"
    )
    include_matched_in_output: bool = True
    comparison_columns_in_exceptions: bool = True


class LegSpec(ReconXModel):
    """One reconciliation step in the DAG."""

    id: str = Field(pattern=r"^[A-Za-z_][A-Za-z0-9_]{0,63}$")
    name: str | None = None
    description: str | None = None
    enabled: bool = True
    sources: list[SourceSpec] = Field(min_length=1)
    left_source: str | None = None
    right_source: str | None = None
    keys: list[KeyMapping] = Field(default_factory=list)
    comparisons: list[FieldComparison] = Field(
        default_factory=list, description="Simple form: all comparisons ANDed together"
    )
    match_logic: MatchLogic | None = Field(
        default=None,
        description="Advanced form: several matching logics combined with AND/OR/NOT",
    )
    aggregates: list[AggregateComparison] = Field(default_factory=list)
    matching: MatchingOptions = Field(default_factory=MatchingOptions)
    pre_transformations: list[Transformation] = Field(default_factory=list)
    post_transformations: list[Transformation] = Field(default_factory=list)
    outputs: list[OutputSpec] = Field(default_factory=list)
    exception_output: OutputSpec | None = None
    exception_columns: list[ExceptionColumn] = Field(
        default_factory=list,
        description="Source columns copied onto every exception record for context",
    )
    depends_on: list[str] = Field(default_factory=list)
    data_quality: list[DataQualityCheck] = Field(default_factory=list)
    register_result_view: str | None = None
    continue_on_failure: bool = False

    @model_validator(mode="after")
    def _resolve(self) -> LegSpec:
        ids = [s.id for s in self.sources]
        if len(set(ids)) != len(ids):
            raise ValueError(f"leg '{self.id}': duplicate source ids {ids}")
        if self.left_source and self.left_source not in ids:
            raise ValueError(f"leg '{self.id}': leftSource '{self.left_source}' is not one of {ids}")
        if self.right_source and self.right_source not in ids:
            raise ValueError(f"leg '{self.id}': rightSource '{self.right_source}' is not one of {ids}")
        left = self.left_source or ids[0]
        right = self.right_source or (ids[1] if len(ids) > 1 else ids[0])
        if left == right and len(ids) > 1:
            raise ValueError(f"leg '{self.id}': left and right source must differ")
        object.__setattr__(self, "left_source", left)
        object.__setattr__(self, "right_source", right)
        if len(ids) > 1 and not self.keys:
            raise ValueError(f"leg '{self.id}': at least one reconciliation key mapping is required")
        object.__setattr__(self, "keys", [k.resolve(left, right) for k in self.keys])
        object.__setattr__(self, "comparisons", [c.resolve(left, right) for c in self.comparisons])
        if self.match_logic is not None:
            object.__setattr__(self, "match_logic", self.match_logic.resolve(left, right))
        for agg in self.aggregates:
            object.__setattr__(agg, "group_by", [g.resolve(left, right) for g in agg.group_by])
        # implicit dependencies from leg_output sources
        implicit = {s.leg_ref for s in self.sources if s.type == SourceType.LEG_OUTPUT and s.leg_ref}
        object.__setattr__(self, "depends_on", sorted(set(self.depends_on) | implicit))
        return self

    def effective_match_logic(self) -> MatchLogic | None:
        """Normalised matching logic.

        Legs configured with the simple ``comparisons`` list are transparently
        promoted to a single AND rule so the engine has one code path.
        """
        if self.match_logic is not None:
            return self.match_logic
        if self.comparisons:
            return MatchLogic(
                operator=LogicalOperator.AND,
                rules=[
                    MatchRule(
                        id="default_rule",
                        name="Field comparisons",
                        operator=LogicalOperator.AND,
                        comparisons=list(self.comparisons),
                    )
                ],
            )
        return None

    def all_comparisons(self) -> list[FieldComparison]:
        logic = self.effective_match_logic()
        return logic.all_comparisons() if logic else []

    @property
    def left(self) -> SourceSpec:
        return next(s for s in self.sources if s.id == self.left_source)

    @property
    def right(self) -> SourceSpec:
        return next(s for s in self.sources if s.id == self.right_source)

    @property
    def extra_sources(self) -> list[SourceSpec]:
        return [s for s in self.sources if s.id not in {self.left_source, self.right_source}]


# --------------------------------------------------------------------------- #
# Conditions / schedule / notifications / events / retention
# --------------------------------------------------------------------------- #
class ConditionSpec(ReconXModel):
    """Recursive data-availability condition tree."""

    id: str | None = None
    type: ConditionType | None = None
    operator: ConditionOperator | None = None
    conditions: list[ConditionSpec] = Field(default_factory=list)
    description: str | None = None

    connection_ref: str | None = None
    path: str | None = None
    bucket: str | None = None
    file_pattern: str | None = None
    min_count: int = 1
    max_count: int | None = None
    min_size_bytes: int = 1
    query: str | None = None
    expected: Any = None
    comparator: Literal["gt", "gte", "lt", "lte", "eq", "ne"] = "gt"
    threshold: float = 0
    topic: str | None = None
    consumer_group: str | None = None
    min_messages: int = 1
    recon_id: str | None = None
    lookback_hours: int = 24
    negate: bool = False

    @model_validator(mode="after")
    def _validate(self) -> ConditionSpec:
        if self.operator and self.type:
            raise ValueError("condition cannot define both 'operator' and 'type'")
        if self.operator:
            if not self.conditions:
                raise ValueError(f"composite condition '{self.operator.value}' requires nested conditions")
            if self.operator == ConditionOperator.NOT and len(self.conditions) != 1:
                raise ValueError("NOT condition requires exactly one nested condition")
            return self
        if not self.type:
            raise ValueError("condition requires either 'type' or 'operator'")
        t = self.type
        if t in (ConditionType.FILE_EXISTS, ConditionType.S3_FILE_EXISTS, ConditionType.SFTP_FILE_EXISTS,
                 ConditionType.FILE_COUNT, ConditionType.FILE_SIZE) and not self.path:
            raise ValueError(f"condition '{t.value}' requires 'path'")
        if t in (ConditionType.JDBC_QUERY, ConditionType.CUSTOM_SQL) and not self.query:
            raise ValueError(f"condition '{t.value}' requires 'query'")
        if t == ConditionType.KAFKA_AVAILABLE and not self.topic:
            raise ValueError("condition 'kafka_available' requires 'topic'")
        if t == ConditionType.RECONCILIATION_SUCCEEDED and not self.recon_id:
            raise ValueError("condition 'reconciliation_succeeded' requires 'reconId'")
        needs_conn = {
            ConditionType.S3_FILE_EXISTS,
            ConditionType.SFTP_FILE_EXISTS,
            ConditionType.JDBC_QUERY,
            ConditionType.CUSTOM_SQL,
            ConditionType.KAFKA_AVAILABLE,
        }
        if t in needs_conn and not self.connection_ref:
            raise ValueError(f"condition '{t.value}' requires 'connectionRef'")
        return self

    @property
    def is_composite(self) -> bool:
        return self.operator is not None


ConditionSpec.model_rebuild()


class RetryConfig(ReconXModel):
    max_attempts: int = Field(default=1, ge=1, le=20)
    initial_delay_seconds: float = Field(default=60, ge=0)
    max_delay_seconds: float = Field(default=1800, ge=0)
    multiplier: float = Field(default=2.0, ge=1.0)
    jitter: bool = True
    retry_on_data_unavailable: bool = False


class ScheduleSpec(ReconXModel):
    enabled: bool = True
    type: ScheduleType = ScheduleType.MANUAL
    expression: str | None = Field(default=None, description="Cron expression for type=cron")
    interval_seconds: int | None = Field(default=None, ge=30)
    time: str | None = Field(default=None, pattern=r"^\d{2}:\d{2}$", description="HH:MM for daily/weekly/monthly")
    days_of_week: list[int] = Field(default_factory=list, description="0=Monday .. 6=Sunday")
    day_of_month: int | None = Field(default=None, ge=1, le=31)
    run_at: datetime | None = Field(default=None, description="Fire time for type=once")
    timezone: str = "UTC"
    start_date: datetime | None = None
    end_date: datetime | None = None
    paused: bool = False
    catch_up: bool = False
    misfire_grace_seconds: int = 900
    retries: RetryConfig = Field(default_factory=RetryConfig)
    timeout_minutes: int = Field(default=180, ge=1)
    max_concurrent_runs: int = Field(default=1, ge=1, le=50)
    business_date_offset_days: int = 0
    wait_for_data_minutes: int = Field(
        default=120, ge=0, description="How long to keep re-checking conditions before SKIPPED"
    )

    @model_validator(mode="after")
    def _validate(self) -> ScheduleSpec:
        if self.type == ScheduleType.CRON and not self.expression:
            raise ValueError("cron schedule requires 'expression'")
        if self.type == ScheduleType.INTERVAL and not self.interval_seconds:
            raise ValueError("interval schedule requires 'intervalSeconds'")
        if self.type in (ScheduleType.DAILY, ScheduleType.WEEKLY, ScheduleType.MONTHLY) and not self.time:
            raise ValueError(f"{self.type.value} schedule requires 'time' (HH:MM)")
        if self.type == ScheduleType.WEEKLY and not self.days_of_week:
            raise ValueError("weekly schedule requires 'daysOfWeek'")
        if self.type == ScheduleType.MONTHLY and self.day_of_month is None:
            raise ValueError("monthly schedule requires 'dayOfMonth'")
        if self.type == ScheduleType.ONCE and not self.run_at:
            raise ValueError("once schedule requires 'runAt'")
        if self.expression:
            from croniter import croniter

            if not croniter.is_valid(self.expression):
                raise ValueError(f"invalid cron expression '{self.expression}'")
        return self


class EmailNotification(ReconXModel):
    enabled: bool = True
    recipients: list[str] = Field(default_factory=list)
    cc: list[str] = Field(default_factory=list)
    on: list[NotifyOn] = Field(default_factory=lambda: [NotifyOn.SUCCESS, NotifyOn.FAILURE])

    @model_validator(mode="before")
    @classmethod
    def _accept_yaml_on_key(cls, data: Any) -> Any:
        """Tolerate YAML 1.1 turning a bare ``on:`` key into the boolean ``True``.

        ``on:`` is the natural name for "notify on these outcomes", and YAML
        parsers resolve it to ``True`` unless it is quoted.  Rather than making
        every author remember to write ``"on":``, accept the boolean key (and
        the explicit ``notifyOn`` alias) here.
        """
        if isinstance(data, dict):
            data = dict(data)
            for alias in (True, "notifyOn", "notify_on"):
                if alias in data and "on" not in data:
                    data["on"] = data.pop(alias)
                else:
                    data.pop(alias, None)
        return data
    subject_prefix: str = "[RECON]"
    include_metrics: bool = True
    include_exception_sample: bool = True
    exception_sample_size: int = Field(default=20, ge=0, le=500)
    exception_threshold: int | None = None

    @field_validator("recipients", "cc")
    @classmethod
    def _validate_emails(cls, values: list[str]) -> list[str]:
        for value in values:
            if "@" not in value or value.startswith("@") or value.endswith("@"):
                raise ValueError(f"invalid email address '{value}'")
        return values


class NotificationSpec(ReconXModel):
    email: EmailNotification = Field(default_factory=EmailNotification)


class EventsSpec(ReconXModel):
    enabled: bool = True
    topic_prefix: str | None = None
    on_failure: EventFailureMode = EventFailureMode.WARN_ONLY
    include_metrics: bool = True
    emit_stage_events: bool = True
    emit_exception_events: bool = False
    exception_event_limit: int = Field(default=1000, ge=0)
    extra_headers: dict[str, str] = Field(default_factory=dict)


class RetentionSpec(ReconXModel):
    runs_days: int = Field(default=365, ge=1)
    exceptions_days: int = Field(default=90, ge=1)
    results_days: int = Field(default=90, ge=1)
    events_days: int = Field(default=30, ge=1)
    archive_to: OutputSpec | None = None


class SparkOverrides(ReconXModel):
    driver_cores: int | None = Field(default=None, ge=1, le=64)
    driver_memory: str | None = None
    executor_cores: int | None = Field(default=None, ge=1, le=64)
    executor_memory: str | None = None
    executor_instances: int | None = Field(default=None, ge=1, le=1000)
    dynamic_allocation: bool | None = None
    shuffle_partitions: int | None = Field(default=None, ge=1, le=100_000)
    broadcast_threshold_mb: int | None = Field(default=None, ge=-1, le=8192)
    extra_conf: dict[str, str] = Field(default_factory=dict)


# --------------------------------------------------------------------------- #
# Root definition
# --------------------------------------------------------------------------- #
class ReconciliationDefinition(ReconXModel):
    """A complete, versioned reconciliation definition."""

    recon_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_.-]{1,127}$")
    name: str
    description: str | None = None
    version: int = Field(default=1, ge=1)
    status: DefinitionStatus = DefinitionStatus.DRAFT
    enabled: bool = True
    product: str | None = None
    customer: str | None = None
    environment: str | None = None
    owner: str | None = None
    tags: list[str] = Field(default_factory=list)

    legs: list[LegSpec] = Field(default_factory=list)
    conditions: ConditionSpec | None = None
    schedule: ScheduleSpec = Field(default_factory=ScheduleSpec)
    notifications: NotificationSpec = Field(default_factory=NotificationSpec)
    events: EventsSpec = Field(default_factory=EventsSpec)
    retention: RetentionSpec = Field(default_factory=RetentionSpec)
    spark: SparkOverrides = Field(default_factory=SparkOverrides)
    data_quality: list[DataQualityCheck] = Field(default_factory=list)
    idempotency_dimensions: list[str] = Field(
        default_factory=lambda: ["business_date"],
        description="Variables forming the idempotency key together with reconId+version",
    )
    variables: list[VariableSpec] = Field(
        default_factory=list,
        description="Declared ${variables} usable in queries, table names, paths and filters",
    )
    parameters: dict[str, Any] = Field(
        default_factory=dict, description="Default values for variables, overridable per run"
    )

    created_by: str | None = None
    created_at: datetime | None = None
    updated_by: str | None = None
    updated_at: datetime | None = None
    activated_by: str | None = None
    activated_at: datetime | None = None
    change_comment: str | None = None
    latest_draft_version: int | None = Field(
        default=None,
        description="Newest saved version when it is not the one currently ACTIVE",
    )

    @model_validator(mode="after")
    def _validate(self) -> ReconciliationDefinition:
        ids = [leg.id for leg in self.legs]
        if len(set(ids)) != len(ids):
            raise ValueError(f"duplicate leg ids: {ids}")
        known = set(ids)
        for leg in self.legs:
            for dep in leg.depends_on:
                if dep not in known:
                    raise ValueError(f"leg '{leg.id}' depends on unknown leg '{dep}'")
        if self.created_at is None:
            object.__setattr__(self, "created_at", utcnow())
        return self

    @property
    def enabled_legs(self) -> list[LegSpec]:
        return [leg for leg in self.legs if leg.enabled]

    def connection_refs(self) -> set[str]:
        refs: set[str] = set()
        for leg in self.legs:
            for source in leg.sources:
                if source.connection_ref:
                    refs.add(source.connection_ref)
            for output in [*leg.outputs, leg.exception_output]:
                if output and output.connection_ref:
                    refs.add(output.connection_ref)
        for cond in _walk_conditions(self.conditions):
            if cond.connection_ref:
                refs.add(cond.connection_ref)
        return refs


def declared_variable_defaults(definition: ReconciliationDefinition) -> dict[str, Any]:
    """Variable defaults: declared defaults first, overridden by ``parameters``."""
    values: dict[str, Any] = {
        variable.name: variable.default
        for variable in definition.variables
        if variable.default is not None
    }
    values.update({k: v for k, v in definition.parameters.items() if v is not None})
    return values


def _walk_conditions(condition: ConditionSpec | None) -> list[ConditionSpec]:
    if condition is None:
        return []
    if condition.is_composite:
        out: list[ConditionSpec] = []
        for child in condition.conditions:
            out.extend(_walk_conditions(child))
        return out
    return [condition]
