"""Declarative transformation engine.

Every transformation is expressed as data (see
:class:`~reconx.config.models.Transformation`) and executed with the Spark
DataFrame API.  User-supplied SQL is validated by
:mod:`reconx.security.sql_guard` before it reaches Spark; arbitrary Python is
never executed.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from reconx.common.errors import TransformationError
from reconx.common.logging import get_logger
from reconx.common.templating import render_deep
from reconx.config.enums import TransformType
from reconx.config.models import Normalization, Transformation
from reconx.security.sql_guard import assert_identifier, assert_read_only, assert_safe_expression
from reconx.spark.schema import parse_data_type

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession
    from pyspark.sql.column import Column

log = get_logger(__name__)


def normalise_column(column: Column, rules: Normalization | None) -> Column:
    """Apply the configured normalisation chain to a single column."""
    from pyspark.sql import functions as F

    if rules is None:
        return column
    result = column
    if rules.expression:
        assert_safe_expression(rules.expression, context="normalization.expression")
        result = F.expr(rules.expression.replace("${col}", "__value__"))
    if rules.parse_date_formats:
        parsed = F.to_timestamp(result.cast("string"), rules.parse_date_formats[0])
        for fmt in rules.parse_date_formats[1:]:
            parsed = F.coalesce(parsed, F.to_timestamp(result.cast("string"), fmt))
        result = parsed
    if rules.date_format:
        result = F.date_format(result, rules.date_format)
    if rules.numeric_scale is not None:
        result = F.round(result.cast("decimal(38,18)"), rules.numeric_scale)
    result = result.cast("string") if rules.trim or rules.case != "none" or rules.strip_leading_zeros else result
    if rules.trim:
        result = F.trim(result)
    if rules.remove_characters:
        result = F.regexp_replace(result, rules.remove_characters, "")
    if rules.case == "upper":
        result = F.upper(result)
    elif rules.case == "lower":
        result = F.lower(result)
    if rules.strip_leading_zeros:
        result = F.regexp_replace(result, "^0+(?=.)", "")
    if rules.pad_left:
        result = F.lpad(result, rules.pad_left, rules.pad_character)
    if rules.null_as is not None:
        result = F.coalesce(result, F.lit(rules.null_as))
    return result


class TransformationEngine:
    """Applies a list of transformations to a DataFrame."""

    def __init__(self, spark: SparkSession, variables: dict[str, Any] | None = None) -> None:
        self.spark = spark
        self.variables = variables or {}

    def apply_all(
        self,
        dataframe: DataFrame,
        transformations: list[Transformation],
        *,
        context: str = "transform",
        sources: dict[str, DataFrame] | None = None,
    ) -> DataFrame:
        result = dataframe
        for index, transformation in enumerate(transformations):
            label = transformation.id or f"{context}[{index}]:{transformation.type.value}"
            try:
                result = self.apply(result, transformation, sources=sources)
            except TransformationError:
                raise
            except Exception as exc:
                raise TransformationError(
                    f"Transformation '{label}' failed: {exc}",
                    details={"type": transformation.type.value, "context": context},
                ) from exc
            log.debug("transform.applied", step=label, type=transformation.type.value)
        return result

    def apply(
        self,
        dataframe: DataFrame,
        transformation: Transformation,
        *,
        sources: dict[str, DataFrame] | None = None,
    ) -> DataFrame:
        from pyspark.sql import functions as F

        spec = _rendered(transformation, self.variables)
        kind = spec.type

        if kind == TransformType.SELECT:
            _assert_columns_exist(dataframe, spec.columns, "select")
            return dataframe.select(*spec.columns)

        if kind == TransformType.DROP:
            return dataframe.drop(*spec.columns)

        if kind == TransformType.RENAME:
            result = dataframe
            for old, new in spec.mapping.items():
                assert_identifier(new, context="rename.target")
                if old not in result.columns:
                    raise TransformationError(f"rename: column '{old}' does not exist")
                result = result.withColumnRenamed(old, new)
            return result

        if kind == TransformType.CAST:
            result = dataframe
            for column, type_name in spec.fields.items():
                if column not in result.columns:
                    raise TransformationError(f"cast: column '{column}' does not exist")
                result = result.withColumn(column, F.col(column).cast(parse_data_type(type_name)))
            return result

        if kind == TransformType.FILTER:
            condition = spec.condition or spec.expression or ""
            assert_safe_expression(condition, context="filter.condition")
            return dataframe.filter(F.expr(condition))

        if kind == TransformType.DERIVE:
            result = dataframe
            for column, expression in spec.fields.items():
                assert_identifier(column, context="derive.column")
                assert_safe_expression(expression, context=f"derive.{column}")
                result = result.withColumn(column, F.expr(expression))
            return result

        if kind in (TransformType.SQL, TransformType.TEMP_VIEW):
            sql = spec.sql or ""
            assert_read_only(sql, context=f"{kind.value}.sql")
            input_view = f"__reconx_input_{abs(hash(sql)) % 10_000}"
            dataframe.createOrReplaceTempView(input_view)
            try:
                rendered_sql = sql.replace("${input}", input_view)
                result = self.spark.sql(rendered_sql)
            finally:
                if kind == TransformType.SQL:
                    self.spark.catalog.dropTempView(input_view)
            if kind == TransformType.TEMP_VIEW and spec.view_name:
                assert_identifier(spec.view_name, context="temp_view.viewName")
                result.createOrReplaceTempView(spec.view_name)
                log.info("transform.temp_view_registered", view=spec.view_name)
                return dataframe  # the view is a side effect; the pipeline continues unchanged
            return result

        if kind == TransformType.DEDUPLICATE:
            columns = spec.columns or dataframe.columns
            _assert_columns_exist(dataframe, columns, "deduplicate")
            if spec.order_by:
                from pyspark.sql.window import Window

                order = [
                    F.col(c).asc() if spec.ascending else F.col(c).desc()
                    for c in spec.order_by
                ]
                if spec.keep == "last":
                    order = [F.col(c).desc() if spec.ascending else F.col(c).asc() for c in spec.order_by]
                window = Window.partitionBy(*columns).orderBy(*order)
                return (
                    dataframe.withColumn("__reconx_rn", F.row_number().over(window))
                    .filter(F.col("__reconx_rn") == 1)
                    .drop("__reconx_rn")
                )
            return dataframe.dropDuplicates(columns)

        if kind == TransformType.DISTINCT:
            return dataframe.select(*spec.columns).distinct() if spec.columns else dataframe.distinct()

        if kind == TransformType.AGGREGATE:
            aggregations = []
            for alias, expression in spec.aggregations.items():
                assert_identifier(alias, context="aggregate.alias")
                assert_safe_expression(expression, context=f"aggregate.{alias}")
                aggregations.append(F.expr(expression).alias(alias))
            if spec.group_by:
                _assert_columns_exist(dataframe, spec.group_by, "aggregate.groupBy")
                return dataframe.groupBy(*spec.group_by).agg(*aggregations)
            return dataframe.agg(*aggregations)

        if kind == TransformType.JOIN:
            other = (sources or {}).get(spec.with_source or "")
            if other is None:
                other = self._view_or_fail(spec.with_source or "")
            if spec.condition:
                assert_safe_expression(spec.condition, context="join.condition")
                return dataframe.join(other, F.expr(spec.condition), spec.join_type)
            return dataframe.join(other, on=spec.join_keys, how=spec.join_type)

        if kind == TransformType.UNION:
            other = (sources or {}).get(spec.with_source or "") or self._view_or_fail(spec.with_source or "")
            return dataframe.unionByName(other, allowMissingColumns=True)

        if kind == TransformType.FILL_NULL:
            if spec.fields:
                return dataframe.fillna({k: _coerce_literal(v) for k, v in spec.fields.items()})
            if spec.columns:
                return dataframe.fillna(_coerce_literal(spec.value), subset=spec.columns)
            return dataframe.fillna(_coerce_literal(spec.value))

        if kind == TransformType.DROP_NULL:
            return dataframe.dropna(subset=spec.columns or None)

        if kind == TransformType.NORMALIZE:
            result = dataframe
            for column in spec.columns:
                if column not in result.columns:
                    raise TransformationError(f"normalize: column '{column}' does not exist")
                result = result.withColumn(column, normalise_column(F.col(column), spec.normalization))
            return result

        if kind == TransformType.DATE_FORMAT:
            result = dataframe
            for column in spec.columns:
                result = result.withColumn(
                    column, F.date_format(F.col(column), spec.format or "yyyy-MM-dd")
                )
            return result

        if kind == TransformType.STRING_OP:
            operation = (spec.operation or "trim").lower()
            operations = {
                "trim": F.trim,
                "upper": F.upper,
                "lower": F.lower,
                "ltrim": F.ltrim,
                "rtrim": F.rtrim,
                "initcap": F.initcap,
                "reverse": F.reverse,
            }
            if operation not in operations:
                raise TransformationError(
                    f"string_op: unsupported operation '{operation}'",
                    details={"supported": sorted(operations)},
                )
            result = dataframe
            for column in spec.columns:
                result = result.withColumn(column, operations[operation](F.col(column)))
            return result

        if kind == TransformType.LIMIT:
            return dataframe.limit(int(spec.limit or 1000))

        if kind == TransformType.ORDER_BY:
            order = [
                F.col(c).asc() if spec.ascending else F.col(c).desc() for c in (spec.order_by or spec.columns)
            ]
            return dataframe.orderBy(*order)

        if kind == TransformType.REPARTITION:
            if spec.partition_by:
                return (
                    dataframe.repartition(spec.num_partitions, *spec.partition_by)
                    if spec.num_partitions
                    else dataframe.repartition(*spec.partition_by)
                )
            return dataframe.repartition(int(spec.num_partitions or 200))

        raise TransformationError(f"Unsupported transformation type '{kind}'")

    def _view_or_fail(self, name: str) -> DataFrame:
        assert_identifier(name, context="transformation.withSource")
        existing = {t.name for t in self.spark.catalog.listTables()}
        if name not in existing:
            raise TransformationError(
                f"Transformation references unknown source/view '{name}'",
                details={"availableViews": sorted(existing)},
            )
        return self.spark.table(name)


def _rendered(transformation: Transformation, variables: dict[str, Any]) -> Transformation:
    if not variables:
        return transformation
    data = transformation.model_dump(by_alias=False)
    return Transformation.model_validate(render_deep(data, variables, strict=False))


def _assert_columns_exist(dataframe: DataFrame, columns: list[str], context: str) -> None:
    missing = [c for c in columns if c not in dataframe.columns and "(" not in c and c != "*"]
    if missing:
        raise TransformationError(
            f"{context}: column(s) {missing} not found",
            details={"available": dataframe.columns},
        )


def _coerce_literal(value: Any) -> Any:
    if isinstance(value, str):
        lowered = value.lower()
        if lowered in ("true", "false"):
            return lowered == "true"
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
    return value if value is not None else ""
