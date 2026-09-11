"""The reconciliation engine.

Design constraints that shape this module:

* **Never collect large data to the driver.**  Classification, duplicate
  detection, field comparison and metrics are all expressed as Spark
  transformations; only small aggregate result rows (one row of counters) ever
  reach the driver.
* **One pass for metrics.**  Every counter is computed in a single ``agg`` so a
  100M-row reconciliation does not trigger a dozen separate shuffles.
* **Full outer join** is the backbone: it yields matched, left-only and
  right-only in one shuffle, and field comparisons then split matched into
  MATCHED / MISMATCH.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from reconx.common.errors import ReconciliationError
from reconx.common.logging import get_logger
from reconx.config.enums import EXCEPTION_CATEGORIES, AggregateFunction, MatchCategory
from reconx.config.models import AggregateComparison, LegSpec, MatchLogic
from reconx.spark.keys import KEY_COLUMN, KEY_PART_PREFIX, add_reconciliation_key, key_component_aliases
from reconx.spark.reconciliation.comparisons import (
    add_comparison_columns,
    evaluate_match_logic,
    field_column_name,
    rule_column_name,
)
from reconx.spark.reconciliation.constants import (
    CATEGORY_COLUMN,
    FAILED_RULES_COLUMN,
    LEFT_DUP_COLUMN,
    LEFT_PREFIX,
    LEFT_PRESENT_COLUMN,
    MATCH_COLUMN,
    MATCHED_RULES_COLUMN,
    MISMATCHED_FIELDS_COLUMN,
    RIGHT_DUP_COLUMN,
    RIGHT_PREFIX,
    RIGHT_PRESENT_COLUMN,
)

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)


@dataclass
class LegMetrics:
    """Counters produced by one leg."""

    leg_id: str
    left_records: int = 0
    right_records: int = 0
    left_distinct_keys: int = 0
    right_distinct_keys: int = 0
    matched: int = 0
    mismatched: int = 0
    left_only: int = 0
    right_only: int = 0
    duplicates_left: int = 0
    duplicates_right: int = 0
    duplicate_keys: int = 0
    exceptions: int = 0
    field_mismatches: int = 0
    read_time_ms: int = 0
    process_time_ms: int = 0
    write_time_ms: int = 0

    @property
    def total_records(self) -> int:
        return self.left_records + self.right_records

    @property
    def unmatched(self) -> int:
        return self.mismatched + self.left_only + self.right_only

    @property
    def match_percentage(self) -> float | None:
        denominator = self.matched + self.unmatched
        return round(self.matched / denominator * 100, 4) if denominator else None

    def to_dict(self) -> dict[str, Any]:
        return {
            "legId": self.leg_id,
            "leftRecords": self.left_records,
            "rightRecords": self.right_records,
            "leftDistinctKeys": self.left_distinct_keys,
            "rightDistinctKeys": self.right_distinct_keys,
            "matched": self.matched,
            "mismatched": self.mismatched,
            "leftOnly": self.left_only,
            "rightOnly": self.right_only,
            "duplicatesLeft": self.duplicates_left,
            "duplicatesRight": self.duplicates_right,
            "duplicateKeys": self.duplicate_keys,
            "exceptions": self.exceptions,
            "fieldMismatches": self.field_mismatches,
            "totalRecords": self.total_records,
            "unmatched": self.unmatched,
            "matchPercentage": self.match_percentage,
            "readTimeMs": self.read_time_ms,
            "processTimeMs": self.process_time_ms,
            "writeTimeMs": self.write_time_ms,
        }


@dataclass
class LegResult:
    """Everything one leg produces."""

    leg_id: str
    result: DataFrame
    exceptions: DataFrame
    metrics: LegMetrics
    field_metrics: list[dict[str, Any]] = field(default_factory=list)
    rule_metrics: list[dict[str, Any]] = field(default_factory=list)
    aggregate_results: list[dict[str, Any]] = field(default_factory=list)
    key_description: str = ""
    match_logic_description: str = ""


class ReconciliationEngine:
    """Executes a single leg: key -> duplicates -> join -> classify -> metrics."""

    def __init__(self, spark: SparkSession) -> None:
        self.spark = spark

    # ------------------------------------------------------------------ main
    def reconcile(
        self,
        leg: LegSpec,
        left: DataFrame,
        right: DataFrame,
        *,
        max_exception_records: int | None = None,
    ) -> LegResult:
        from pyspark.sql import functions as F

        options = leg.matching
        logic = leg.effective_match_logic()

        left_keyed = add_reconciliation_key(left, leg.keys, side="left", options=options)
        right_keyed = add_reconciliation_key(right, leg.keys, side="right", options=options)

        if options.duplicate_detection:
            left_keyed = _with_duplicate_count(left_keyed, LEFT_DUP_COLUMN)
            right_keyed = _with_duplicate_count(right_keyed, RIGHT_DUP_COLUMN)
        else:
            left_keyed = left_keyed.withColumn(LEFT_DUP_COLUMN, F.lit(1))
            right_keyed = right_keyed.withColumn(RIGHT_DUP_COLUMN, F.lit(1))

        left_prefixed = _prefix_columns(left_keyed, LEFT_PREFIX, keep={KEY_COLUMN, LEFT_DUP_COLUMN})
        right_prefixed = _prefix_columns(right_keyed, RIGHT_PREFIX, keep={KEY_COLUMN, RIGHT_DUP_COLUMN})

        if options.broadcast_smaller_side:
            # AQE decides at runtime; the hint only nudges when statistics are absent.
            right_prefixed = _maybe_broadcast(right_prefixed, leg)

        joined = left_prefixed.join(right_prefixed, on=KEY_COLUMN, how="full_outer")

        joined = joined.withColumn(
            LEFT_PRESENT_COLUMN, F.col(LEFT_DUP_COLUMN).isNotNull()
        ).withColumn(RIGHT_PRESENT_COLUMN, F.col(RIGHT_DUP_COLUMN).isNotNull())

        rule_fields: dict[str, list[str]] = {}
        if logic is not None:
            joined, rule_fields = add_comparison_columns(
                joined, logic, left_source=leg.left_source or "left", right_source=leg.right_source or "right"
            )
            joined = joined.withColumn(MATCH_COLUMN, evaluate_match_logic(logic))
        else:
            joined = joined.withColumn(MATCH_COLUMN, F.lit(True))

        joined = self._classify(joined, leg, logic, rule_fields)
        joined = self._annotate(joined, logic, rule_fields)

        metrics, field_metrics, rule_metrics = self._compute_metrics(joined, leg, logic, rule_fields)
        exceptions = self._build_exceptions(
            joined, leg, logic, rule_fields, limit=max_exception_records or options.max_exception_records
        )
        aggregates = self._reconcile_aggregates(leg, left_keyed, right_keyed)

        from reconx.spark.keys import describe_key

        return LegResult(
            leg_id=leg.id,
            result=_public_result(joined, leg),
            exceptions=exceptions,
            metrics=metrics,
            field_metrics=field_metrics,
            rule_metrics=rule_metrics,
            aggregate_results=aggregates,
            key_description=describe_key(leg.keys, options),
            match_logic_description=logic.describe() if logic else "presence only",
        )

    # -------------------------------------------------------------- classify
    def _classify(
        self,
        joined: DataFrame,
        leg: LegSpec,
        logic: MatchLogic | None,
        rule_fields: dict[str, list[str]],
    ) -> DataFrame:
        from pyspark.sql import functions as F

        options = leg.matching
        left_dup = F.coalesce(F.col(LEFT_DUP_COLUMN), F.lit(0)) > 1
        right_dup = F.coalesce(F.col(RIGHT_DUP_COLUMN), F.lit(0)) > 1

        category = F.when(
            ~F.col(LEFT_PRESENT_COLUMN), F.lit(MatchCategory.RIGHT_ONLY.value)
        ).when(~F.col(RIGHT_PRESENT_COLUMN), F.lit(MatchCategory.LEFT_ONLY.value))

        if options.duplicate_detection and options.treat_duplicates_as_exceptions:
            category = (
                category.when(left_dup & right_dup, F.lit(MatchCategory.DUPLICATE_BOTH.value))
                .when(left_dup, F.lit(MatchCategory.DUPLICATE_LEFT.value))
                .when(right_dup, F.lit(MatchCategory.DUPLICATE_RIGHT.value))
            )

        category = category.when(F.col(MATCH_COLUMN), F.lit(MatchCategory.MATCHED.value)).otherwise(
            F.lit(MatchCategory.MISMATCH.value)
        )
        return joined.withColumn(CATEGORY_COLUMN, category)

    def _annotate(
        self, joined: DataFrame, logic: MatchLogic | None, rule_fields: dict[str, list[str]]
    ) -> DataFrame:
        """Attach the arrays of failing fields / rules used by reports and the advisor."""
        from pyspark.sql import functions as F

        if logic is None:
            return (
                joined.withColumn(MISMATCHED_FIELDS_COLUMN, F.array().cast("array<string>"))
                .withColumn(MATCHED_RULES_COLUMN, F.array().cast("array<string>"))
                .withColumn(FAILED_RULES_COLUMN, F.array().cast("array<string>"))
            )

        both_present = F.col(LEFT_PRESENT_COLUMN) & F.col(RIGHT_PRESENT_COLUMN)
        field_terms = []
        for rule in logic.all_rules():
            for comparison in rule.comparisons:
                column = field_column_name(comparison, rule.id)
                field_terms.append(
                    F.when(both_present & ~F.coalesce(F.col(column), F.lit(False)), F.lit(comparison.field_name))
                )
        matched_rule_terms = [
            F.when(both_present & F.coalesce(F.col(rule_column_name(r.id)), F.lit(False)), F.lit(r.label))
            for r in logic.all_rules()
        ]
        failed_rule_terms = [
            F.when(both_present & ~F.coalesce(F.col(rule_column_name(r.id)), F.lit(False)), F.lit(r.label))
            for r in logic.all_rules()
        ]

        def _array(terms: list[Any]) -> Any:
            """Array of the non-null labels (higher-order filter, no UDF)."""
            if not terms:
                return F.array().cast("array<string>")
            return F.filter(F.array(*terms), lambda item: item.isNotNull())

        return (
            joined.withColumn(MISMATCHED_FIELDS_COLUMN, _array(field_terms))
            .withColumn(MATCHED_RULES_COLUMN, _array(matched_rule_terms))
            .withColumn(FAILED_RULES_COLUMN, _array(failed_rule_terms))
        )

    # --------------------------------------------------------------- metrics
    def _compute_metrics(
        self,
        joined: DataFrame,
        leg: LegSpec,
        logic: MatchLogic | None,
        rule_fields: dict[str, list[str]],
    ) -> tuple[LegMetrics, list[dict[str, Any]], list[dict[str, Any]]]:
        """Single-pass metric computation over the classified DataFrame."""
        from pyspark.sql import functions as F

        both_present = F.col(LEFT_PRESENT_COLUMN) & F.col(RIGHT_PRESENT_COLUMN)

        def count_when(condition: Any, alias: str) -> Any:
            return F.sum(F.when(condition, F.lit(1)).otherwise(F.lit(0))).alias(alias)

        aggregations: list[Any] = [
            F.count(F.lit(1)).alias("rows"),
            count_when(F.col(CATEGORY_COLUMN) == MatchCategory.MATCHED.value, "matched"),
            count_when(F.col(CATEGORY_COLUMN) == MatchCategory.MISMATCH.value, "mismatched"),
            count_when(F.col(CATEGORY_COLUMN) == MatchCategory.LEFT_ONLY.value, "left_only"),
            count_when(F.col(CATEGORY_COLUMN) == MatchCategory.RIGHT_ONLY.value, "right_only"),
            # Duplicates are counted from the occurrence counters rather than the
            # category, so a key that is duplicated *and* one-sided is reported
            # as both LEFT_ONLY and a duplicate instead of losing one signal.
            count_when(
                F.col(LEFT_PRESENT_COLUMN) & (F.coalesce(F.col(LEFT_DUP_COLUMN), F.lit(0)) > 1),
                "duplicates_left",
            ),
            count_when(
                F.col(RIGHT_PRESENT_COLUMN) & (F.coalesce(F.col(RIGHT_DUP_COLUMN), F.lit(0)) > 1),
                "duplicates_right",
            ),
            F.countDistinct(
                F.when(
                    (F.coalesce(F.col(LEFT_DUP_COLUMN), F.lit(0)) > 1)
                    | (F.coalesce(F.col(RIGHT_DUP_COLUMN), F.lit(0)) > 1),
                    F.col(KEY_COLUMN),
                )
            ).alias("duplicate_keys"),
            count_when(
                F.col(CATEGORY_COLUMN).isin(*[c.value for c in EXCEPTION_CATEGORIES]), "exception_rows"
            ),
            F.sum(F.coalesce(F.size(F.col(MISMATCHED_FIELDS_COLUMN)), F.lit(0))).alias("field_mismatches"),
            F.countDistinct(F.when(F.col(LEFT_PRESENT_COLUMN), F.col(KEY_COLUMN))).alias("left_keys"),
            F.countDistinct(F.when(F.col(RIGHT_PRESENT_COLUMN), F.col(KEY_COLUMN))).alias("right_keys"),
            F.sum(F.when(F.col(LEFT_PRESENT_COLUMN), F.lit(1)).otherwise(F.lit(0))).alias("left_rows"),
            F.sum(F.when(F.col(RIGHT_PRESENT_COLUMN), F.lit(1)).otherwise(F.lit(0))).alias("right_rows"),
        ]

        field_aliases: list[tuple[str, str, str]] = []  # (alias, ruleId, fieldName)
        if logic is not None:
            for rule in logic.all_rules():
                rule_alias = f"rule_{rule.id}"
                aggregations.append(
                    count_when(both_present & ~F.coalesce(F.col(rule_column_name(rule.id)), F.lit(False)),
                               f"{rule_alias}__failed")
                )
                aggregations.append(
                    count_when(both_present & F.coalesce(F.col(rule_column_name(rule.id)), F.lit(False)),
                               f"{rule_alias}__passed")
                )
                for comparison in rule.comparisons:
                    alias = f"field_{rule.id}__{comparison.field_name}".replace(".", "_")
                    aggregations.append(
                        count_when(
                            both_present
                            & ~F.coalesce(F.col(field_column_name(comparison, rule.id)), F.lit(False)),
                            alias,
                        )
                    )
                    field_aliases.append((alias, rule.id, comparison.field_name))

        row = joined.agg(*aggregations).collect()[0].asDict()

        metrics = LegMetrics(
            leg_id=leg.id,
            left_records=int(row.get("left_rows") or 0),
            right_records=int(row.get("right_rows") or 0),
            left_distinct_keys=int(row.get("left_keys") or 0),
            right_distinct_keys=int(row.get("right_keys") or 0),
            matched=int(row.get("matched") or 0),
            mismatched=int(row.get("mismatched") or 0),
            left_only=int(row.get("left_only") or 0),
            right_only=int(row.get("right_only") or 0),
            duplicates_left=int(row.get("duplicates_left") or 0),
            duplicates_right=int(row.get("duplicates_right") or 0),
            duplicate_keys=int(row.get("duplicate_keys") or 0),
            field_mismatches=int(row.get("field_mismatches") or 0),
        )
        metrics.exceptions = int(row.get("exception_rows") or 0)

        field_metrics = [
            {
                "legId": leg.id,
                "ruleId": rule_id,
                "fieldName": field_name,
                "mismatchCount": int(row.get(alias) or 0),
                "comparedCount": int(row.get("matched") or 0) + int(row.get("mismatched") or 0),
            }
            for alias, rule_id, field_name in field_aliases
        ]
        rule_metrics = []
        if logic is not None:
            for rule in logic.all_rules():
                passed = int(row.get(f"rule_{rule.id}__passed") or 0)
                failed = int(row.get(f"rule_{rule.id}__failed") or 0)
                rule_metrics.append(
                    {
                        "legId": leg.id,
                        "ruleId": rule.id,
                        "ruleName": rule.label,
                        "operator": rule.operator.value,
                        "passed": passed,
                        "failed": failed,
                        "passRate": round(passed / (passed + failed) * 100, 4) if (passed + failed) else None,
                    }
                )

        log.info(
            "reconciliation.metrics",
            leg_id=leg.id,
            matched=metrics.matched,
            mismatched=metrics.mismatched,
            left_only=metrics.left_only,
            right_only=metrics.right_only,
            match_percentage=metrics.match_percentage,
        )
        return metrics, field_metrics, rule_metrics

    # ------------------------------------------------------------ exceptions
    def _build_exceptions(
        self,
        joined: DataFrame,
        leg: LegSpec,
        logic: MatchLogic | None,
        rule_fields: dict[str, list[str]],
        *,
        limit: int,
    ) -> DataFrame:
        """One row per (key, exception) - field mismatches are exploded per field.

        Exceptions are first-class records: an operator never has to read Spark
        logs to know what failed.
        """
        from pyspark.sql import functions as F
        from pyspark.sql.types import (
            ArrayType,
            StringType,
            StructField,
            StructType,
        )

        exception_categories = [
            MatchCategory.MISMATCH.value,
            MatchCategory.LEFT_ONLY.value,
            MatchCategory.RIGHT_ONLY.value,
            MatchCategory.DUPLICATE_LEFT.value,
            MatchCategory.DUPLICATE_RIGHT.value,
            MatchCategory.DUPLICATE_BOTH.value,
        ]
        failures = joined.filter(F.col(CATEGORY_COLUMN).isin(exception_categories))

        detail_struct = StructType(
            [
                StructField("field", StringType(), True),
                StructField("rule", StringType(), True),
                StructField("expectedValue", StringType(), True),
                StructField("actualValue", StringType(), True),
            ]
        )

        detail_terms: list[Any] = []
        if logic is not None:
            for rule in logic.all_rules():
                for comparison in rule.comparisons:
                    column = field_column_name(comparison, rule.id)
                    left_column = f"{LEFT_PREFIX}{comparison.left}"
                    right_column = f"{RIGHT_PREFIX}{comparison.right}"
                    if left_column not in joined.columns or right_column not in joined.columns:
                        continue
                    detail_terms.append(
                        F.when(
                            ~F.coalesce(F.col(column), F.lit(False)),
                            F.struct(
                                F.lit(comparison.field_name).alias("field"),
                                F.lit(rule.label).alias("rule"),
                                F.col(left_column).cast("string").alias("expectedValue"),
                                F.col(right_column).cast("string").alias("actualValue"),
                            ),
                        )
                    )

        if detail_terms:
            details = F.filter(F.array(*detail_terms), lambda item: item.isNotNull())
        else:
            details = F.lit(None).cast(ArrayType(detail_struct))

        context_map = _context_map(joined, leg)

        key_aliases = key_component_aliases(leg.keys)
        key_map = F.create_map(
            *[
                item
                for column, alias in key_aliases.items()
                for item in (
                    F.lit(alias),
                    F.coalesce(
                        F.col(f"{LEFT_PREFIX}{column}").cast("string"),
                        F.col(f"{RIGHT_PREFIX}{column}").cast("string"),
                    ),
                )
            ]
        ) if key_aliases else F.create_map()

        enriched = (
            failures.withColumn("__details", details)
            .withColumn("__key_map", key_map)
            .withColumn("__context", context_map)
        )

        mismatch_rows = (
            enriched.filter(F.col(CATEGORY_COLUMN) == MatchCategory.MISMATCH.value)
            .withColumn("__detail", F.explode_outer(F.col("__details")))
            .select(
                F.col(KEY_COLUMN).alias("reconciliation_key"),
                F.lit(leg.id).alias("leg_id"),
                F.col(CATEGORY_COLUMN).alias("exception_type"),
                F.lit(leg.left_source).alias("source"),
                F.col("__detail.field").alias("field"),
                F.col("__detail.rule").alias("rule"),
                F.col("__detail.expectedValue").alias("expected_value"),
                F.col("__detail.actualValue").alias("actual_value"),
                F.col("__key_map").alias("key_components"),
                F.col("__context").alias("context_columns"),
                F.coalesce(F.col(LEFT_DUP_COLUMN), F.lit(0)).alias("left_occurrences"),
                F.coalesce(F.col(RIGHT_DUP_COLUMN), F.lit(0)).alias("right_occurrences"),
            )
        )

        other_rows = (
            enriched.filter(F.col(CATEGORY_COLUMN) != MatchCategory.MISMATCH.value)
            .select(
                F.col(KEY_COLUMN).alias("reconciliation_key"),
                F.lit(leg.id).alias("leg_id"),
                F.col(CATEGORY_COLUMN).alias("exception_type"),
                F.when(
                    F.col(CATEGORY_COLUMN).isin(
                        MatchCategory.LEFT_ONLY.value, MatchCategory.DUPLICATE_LEFT.value
                    ),
                    F.lit(leg.left_source),
                )
                .otherwise(F.lit(leg.right_source))
                .alias("source"),
                F.lit(None).cast("string").alias("field"),
                F.lit(None).cast("string").alias("rule"),
                F.lit(None).cast("string").alias("expected_value"),
                F.lit(None).cast("string").alias("actual_value"),
                F.col("__key_map").alias("key_components"),
                F.col("__context").alias("context_columns"),
                F.coalesce(F.col(LEFT_DUP_COLUMN), F.lit(0)).alias("left_occurrences"),
                F.coalesce(F.col(RIGHT_DUP_COLUMN), F.lit(0)).alias("right_occurrences"),
            )
        )

        exceptions = mismatch_rows.unionByName(other_rows)
        if limit and limit > 0:
            exceptions = exceptions.limit(limit)
        return exceptions

    # ------------------------------------------------------------ aggregates
    def _reconcile_aggregates(
        self, leg: LegSpec, left: DataFrame, right: DataFrame
    ) -> list[dict[str, Any]]:
        """Aggregate-level reconciliation (COUNT / SUM / MIN / MAX / AVG)."""
        from pyspark.sql import functions as F

        if not leg.aggregates:
            return []

        results: list[dict[str, Any]] = []
        for aggregate in leg.aggregates:
            left_expression = _aggregate_expression(aggregate, side="left")
            right_expression = _aggregate_expression(aggregate, side="right")

            if aggregate.group_by:
                left_keys = [g.left for g in aggregate.group_by if g.left]
                right_keys = [g.right for g in aggregate.group_by if g.right]
                left_agg = left.groupBy(*left_keys).agg(left_expression.alias("__left_value"))
                right_agg = right.groupBy(*right_keys).agg(right_expression.alias("__right_value"))
                for left_key, right_key in zip(left_keys, right_keys, strict=True):
                    right_agg = right_agg.withColumnRenamed(right_key, f"__grp_{left_key}")
                    left_agg = left_agg.withColumnRenamed(left_key, f"__grp_{left_key}")
                group_columns = [f"__grp_{k}" for k in left_keys]
                joined = left_agg.join(right_agg, on=group_columns, how="full_outer")
                difference = F.abs(
                    F.coalesce(F.col("__left_value").cast("decimal(38,10)"), F.lit(0))
                    - F.coalesce(F.col("__right_value").cast("decimal(38,10)"), F.lit(0))
                )
                tolerance_column = (
                    difference <= F.lit(float(aggregate.tolerance))
                    if aggregate.tolerance_unit == "absolute"
                    else difference
                    <= F.abs(F.coalesce(F.col("__left_value").cast("decimal(38,10)"), F.lit(0)))
                    * F.lit(float(aggregate.tolerance) / 100.0)
                )
                summary = joined.agg(
                    F.count(F.lit(1)).alias("groups"),
                    F.sum(F.when(tolerance_column, F.lit(0)).otherwise(F.lit(1))).alias("breaks"),
                ).collect()[0]  # bounded: one aggregate row
                sample = (
                    joined.filter(~tolerance_column)
                    .limit(50)
                    .collect()  # bounded: 50-row break sample
                )
                results.append(
                    {
                        "legId": leg.id,
                        "name": aggregate.label,
                        "function": aggregate.function.value,
                        "groupBy": left_keys,
                        "groups": int(summary["groups"] or 0),
                        "breakCount": int(summary["breaks"] or 0),
                        "matched": int(summary["breaks"] or 0) == 0,
                        "tolerance": aggregate.tolerance,
                        "sample": [
                            {
                                **{k: row[k] for k in group_columns},
                                "leftValue": _number(row["__left_value"]),
                                "rightValue": _number(row["__right_value"]),
                            }
                            for row in sample
                        ],
                    }
                )
            else:
                left_value = left.agg(left_expression.alias("value")).collect()[0]["value"]
                right_value = right.agg(right_expression.alias("value")).collect()[0]["value"]
                left_number = _number(left_value)
                right_number = _number(right_value)
                difference = (
                    abs(left_number - right_number)
                    if left_number is not None and right_number is not None
                    else None
                )
                if difference is None:
                    matched = left_value == right_value
                elif aggregate.tolerance_unit == "percent":
                    denominator = abs(left_number) if left_number else 0
                    matched = (
                        difference <= denominator * aggregate.tolerance / 100.0
                        if denominator
                        else difference == 0
                    )
                else:
                    matched = difference <= aggregate.tolerance
                results.append(
                    {
                        "legId": leg.id,
                        "name": aggregate.label,
                        "function": aggregate.function.value,
                        "groupBy": [],
                        "leftValue": left_number if left_number is not None else str(left_value),
                        "rightValue": right_number if right_number is not None else str(right_value),
                        "difference": difference,
                        "tolerance": aggregate.tolerance,
                        "matched": bool(matched),
                        "breakCount": 0 if matched else 1,
                    }
                )
            log.info("reconciliation.aggregate", leg_id=leg.id, name=aggregate.label)
        return results


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def _with_duplicate_count(dataframe: DataFrame, column: str) -> DataFrame:
    from pyspark.sql import functions as F
    from pyspark.sql.window import Window

    window = Window.partitionBy(KEY_COLUMN)
    return dataframe.withColumn(column, F.count(F.lit(1)).over(window))


def _prefix_columns(dataframe: DataFrame, prefix: str, *, keep: set[str]) -> DataFrame:
    from pyspark.sql import functions as F

    return dataframe.select(
        *[
            F.col(f"`{column}`").alias(column if column in keep else f"{prefix}{column}")
            for column in dataframe.columns
        ]
    )


def _maybe_broadcast(dataframe: DataFrame, leg: LegSpec) -> DataFrame:
    from pyspark.sql import functions as F

    if leg.right.broadcast:
        return F.broadcast(dataframe)
    return dataframe


def _public_result(joined: DataFrame, leg: LegSpec) -> DataFrame:
    """Rename engine columns to stable, business-friendly output names."""
    from pyspark.sql import functions as F

    from reconx.spark.reconciliation.constants import PUBLIC_RENAMES

    key_aliases = key_component_aliases(leg.keys)
    selections: list[Any] = [F.col(KEY_COLUMN).alias("recon_key")]
    for column, alias in key_aliases.items():
        selections.append(
            F.coalesce(
                F.col(f"{LEFT_PREFIX}{column}").cast("string"),
                F.col(f"{RIGHT_PREFIX}{column}").cast("string"),
            ).alias(f"key_{alias}")
        )
    selections.append(F.col(CATEGORY_COLUMN).alias(PUBLIC_RENAMES[CATEGORY_COLUMN]))
    selections.append(F.col(MISMATCHED_FIELDS_COLUMN).alias(PUBLIC_RENAMES[MISMATCHED_FIELDS_COLUMN]))
    selections.append(F.col(MATCHED_RULES_COLUMN).alias(PUBLIC_RENAMES[MATCHED_RULES_COLUMN]))
    selections.append(F.col(FAILED_RULES_COLUMN).alias(PUBLIC_RENAMES[FAILED_RULES_COLUMN]))
    selections.append(
        F.coalesce(F.col(LEFT_DUP_COLUMN), F.lit(0)).alias(PUBLIC_RENAMES[LEFT_DUP_COLUMN])
    )
    selections.append(
        F.coalesce(F.col(RIGHT_DUP_COLUMN), F.lit(0)).alias(PUBLIC_RENAMES[RIGHT_DUP_COLUMN])
    )

    for column in joined.columns:
        if column.startswith(LEFT_PREFIX) and not column.startswith(f"{LEFT_PREFIX}{KEY_PART_PREFIX}"):
            selections.append(F.col(f"`{column}`").alias(f"left_{column[len(LEFT_PREFIX):]}"))
        elif column.startswith(RIGHT_PREFIX) and not column.startswith(f"{RIGHT_PREFIX}{KEY_PART_PREFIX}"):
            selections.append(F.col(f"`{column}`").alias(f"right_{column[len(RIGHT_PREFIX):]}"))
    return joined.select(*selections)


def _context_map(joined: DataFrame, leg: LegSpec) -> Any:
    """Map of the configured business columns carried onto exception records.

    Missing columns are skipped with a warning rather than failing the run: a
    context column is for readability, and losing one must never cost an
    officer the exception itself.
    """
    from pyspark.sql import functions as F

    if not leg.exception_columns:
        return F.create_map().cast("map<string,string>")

    entries: list[Any] = []
    for column in leg.exception_columns:
        left_column = f"{LEFT_PREFIX}{column.left}" if column.left else None
        right_column = f"{RIGHT_PREFIX}{column.right}" if column.right else None
        available_left = left_column in joined.columns if left_column else False
        available_right = right_column in joined.columns if right_column else False

        if column.source == "left" and available_left:
            value = F.col(f"`{left_column}`").cast("string")
        elif column.source == "right" and available_right:
            value = F.col(f"`{right_column}`").cast("string")
        elif column.source == "both" and (available_left or available_right):
            left_value = F.col(f"`{left_column}`").cast("string") if available_left else F.lit(None)
            right_value = F.col(f"`{right_column}`").cast("string") if available_right else F.lit(None)
            value = F.concat_ws(
                " | ",
                F.coalesce(left_value, F.lit("")),
                F.coalesce(right_value, F.lit("")),
            )
        elif available_left or available_right:
            left_value = F.col(f"`{left_column}`").cast("string") if available_left else F.lit(None)
            right_value = F.col(f"`{right_column}`").cast("string") if available_right else F.lit(None)
            value = F.coalesce(left_value, right_value)
        else:
            log.warning(
                "reconciliation.exception_column_missing",
                leg_id=leg.id,
                alias=column.alias,
                left=column.left,
                right=column.right,
            )
            continue
        entries.extend([F.lit(column.alias), value])

    if not entries:
        return F.create_map().cast("map<string,string>")
    return F.create_map(*entries)


def _aggregate_expression(aggregate: AggregateComparison, *, side: str) -> Any:
    from pyspark.sql import functions as F

    column_name = aggregate.left_field if side == "left" else aggregate.right_field
    function = aggregate.function
    if function == AggregateFunction.COUNT:
        return F.count(F.col(column_name)) if column_name else F.count(F.lit(1))
    if not column_name:
        raise ReconciliationError(f"Aggregate {function.value} requires a field for the {side} side")
    column = F.col(column_name)
    if function == AggregateFunction.COUNT_DISTINCT:
        return F.countDistinct(column)
    if function == AggregateFunction.SUM:
        return F.sum(column.cast("decimal(38,10)"))
    if function == AggregateFunction.MIN:
        return F.min(column)
    if function == AggregateFunction.MAX:
        return F.max(column)
    if function == AggregateFunction.AVG:
        return F.avg(column.cast("decimal(38,10)"))
    raise ReconciliationError(f"Unsupported aggregate function '{function}'")


def _number(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
