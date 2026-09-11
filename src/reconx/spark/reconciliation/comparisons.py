"""Field comparison semantics and matching-logic evaluation.

Each :class:`~reconx.config.models.FieldComparison` becomes a boolean Spark
column.  Rules combine those booleans with AND/OR/NOT, and
:class:`~reconx.config.models.MatchLogic` combines rules the same way - which
is what lets an operator say "amounts agree AND currencies agree, OR the
external reference agrees".
"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from reconx.common.errors import ReconciliationError
from reconx.common.logging import get_logger
from reconx.config.enums import ComparisonRule, LogicalOperator
from reconx.config.models import FieldComparison, MatchLogic, MatchRule
from reconx.security.sql_guard import assert_safe_expression
from reconx.spark.reconciliation.constants import (
    FIELD_COLUMN_PREFIX,
    LEFT_PREFIX,
    RIGHT_PREFIX,
    RULE_COLUMN_PREFIX,
)
from reconx.spark.transforms import normalise_column

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame
    from pyspark.sql.column import Column

log = get_logger(__name__)

#: Aliases a user may write in a custom comparison expression.
_LEFT_ALIASES = ("left", "l", "source", "a")
_RIGHT_ALIASES = ("right", "r", "target", "b")

_SECONDS_PER_UNIT = {
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
    "days": 86400,
}


def translate_expression(expression: str, left_source: str, right_source: str) -> str:
    """Rewrite ``left.amount`` / ``source_a.amount`` into the joined column names."""
    translated = expression
    for alias in (*_LEFT_ALIASES, left_source):
        if alias:
            translated = re.sub(rf"\b{re.escape(alias)}\.(\w+)", rf"{LEFT_PREFIX}\1", translated)
    for alias in (*_RIGHT_ALIASES, right_source):
        if alias:
            translated = re.sub(rf"\b{re.escape(alias)}\.(\w+)", rf"{RIGHT_PREFIX}\1", translated)
    return translated


def field_columns(comparison: FieldComparison) -> tuple[str, str]:
    return f"{LEFT_PREFIX}{comparison.left}", f"{RIGHT_PREFIX}{comparison.right}"


def comparison_column(
    joined: DataFrame,
    comparison: FieldComparison,
    *,
    left_source: str,
    right_source: str,
) -> Column:
    """Build the boolean column implementing one field comparison.

    NULL semantics: two NULLs compare equal when ``nullEqualsNull`` is set
    (the default); a NULL against a value never matches.  Rows where the key
    exists on only one side are excluded from field comparison by the engine,
    so this only ever runs on genuine both-sides pairs.
    """
    from pyspark.sql import functions as F

    left_column, right_column = field_columns(comparison)

    if comparison.rule == ComparisonRule.ALWAYS_MATCH:
        return F.lit(True)

    if comparison.rule == ComparisonRule.EXPRESSION:
        if not comparison.expression:
            raise ReconciliationError(
                f"Comparison '{comparison.field_name}' uses rule 'expression' but defines none"
            )
        assert_safe_expression(comparison.expression, context=f"comparison.{comparison.field_name}")
        translated = translate_expression(comparison.expression, left_source, right_source)
        return F.expr(translated)

    for column in (left_column, right_column):
        if column not in joined.columns:
            raise ReconciliationError(
                f"Comparison '{comparison.field_name}' references missing column "
                f"'{column.removeprefix(LEFT_PREFIX).removeprefix(RIGHT_PREFIX)}'",
                details={
                    "available": [
                        c.removeprefix(LEFT_PREFIX).removeprefix(RIGHT_PREFIX)
                        for c in joined.columns
                        if c.startswith((LEFT_PREFIX, RIGHT_PREFIX))
                    ][:60]
                },
            )

    left = normalise_column(F.col(left_column), comparison.normalization)
    right = normalise_column(F.col(right_column), comparison.normalization)

    rule = comparison.rule
    if rule == ComparisonRule.EXACT:
        core = left.eqNullSafe(right) if comparison.null_equals_null else (left == right)
        if not comparison.case_sensitive:
            core = F.upper(left.cast("string")).eqNullSafe(F.upper(right.cast("string")))
        return core

    if rule == ComparisonRule.CASE_INSENSITIVE:
        core = F.upper(F.trim(left.cast("string"))).eqNullSafe(F.upper(F.trim(right.cast("string"))))
    elif rule == ComparisonRule.TRIMMED:
        core = F.trim(left.cast("string")).eqNullSafe(F.trim(right.cast("string")))
    elif rule == ComparisonRule.NUMERIC_EXACT:
        core = left.cast("decimal(38,10)").eqNullSafe(right.cast("decimal(38,10)"))
    elif rule == ComparisonRule.NUMERIC_TOLERANCE:
        tolerance = float(comparison.tolerance or 0.0)
        core = F.abs(left.cast("decimal(38,10)") - right.cast("decimal(38,10)")) <= F.lit(tolerance)
    elif rule == ComparisonRule.PERCENTAGE_TOLERANCE:
        tolerance = float(comparison.tolerance or 0.0)
        left_num = left.cast("decimal(38,10)")
        right_num = right.cast("decimal(38,10)")
        denominator = F.greatest(F.abs(left_num), F.lit(0).cast("decimal(38,10)"))
        core = F.when(
            denominator == 0, F.abs(left_num - right_num) == 0
        ).otherwise(F.abs(left_num - right_num) / denominator * 100 <= F.lit(tolerance))
    elif rule == ComparisonRule.DATE_TOLERANCE:
        unit = comparison.tolerance_unit or "seconds"
        multiplier = _SECONDS_PER_UNIT.get(str(unit), 1)
        tolerance_seconds = float(comparison.tolerance or 0.0) * multiplier
        core = (
            F.abs(
                F.unix_timestamp(left.cast("timestamp")) - F.unix_timestamp(right.cast("timestamp"))
            )
            <= F.lit(tolerance_seconds)
        )
    elif rule == ComparisonRule.DATE_ONLY:
        core = F.to_date(left.cast("timestamp")).eqNullSafe(F.to_date(right.cast("timestamp")))
    elif rule == ComparisonRule.CONTAINS:
        # Column.contains accepts another Column; instr() would require a literal.
        core = F.upper(right.cast("string")).contains(F.upper(left.cast("string")))
    else:  # pragma: no cover - enum is exhaustive
        raise ReconciliationError(f"Unsupported comparison rule '{rule}'")

    both_null = left.isNull() & right.isNull()
    either_null = left.isNull() | right.isNull()
    if comparison.null_equals_null:
        return F.when(both_null, F.lit(True)).when(either_null, F.lit(False)).otherwise(core)
    return F.when(either_null, F.lit(False)).otherwise(core)


def field_column_name(comparison: FieldComparison, rule_id: str) -> str:
    return f"{FIELD_COLUMN_PREFIX}{rule_id}__{comparison.field_name}"


def rule_column_name(rule_id: str) -> str:
    return f"{RULE_COLUMN_PREFIX}{rule_id}"


def add_comparison_columns(
    joined: DataFrame,
    logic: MatchLogic,
    *,
    left_source: str,
    right_source: str,
) -> tuple[DataFrame, dict[str, list[str]]]:
    """Materialise one boolean column per comparison and per rule.

    Returns the enriched DataFrame and a mapping of rule id -> field column
    names, which the engine uses to build per-field metrics and exceptions.
    """
    from pyspark.sql import functions as F

    result = joined
    rule_fields: dict[str, list[str]] = {}

    for rule in logic.all_rules():
        field_columns_for_rule: list[str] = []
        for comparison in rule.comparisons:
            column_name = field_column_name(comparison, rule.id)
            result = result.withColumn(
                column_name,
                comparison_column(
                    result, comparison, left_source=left_source, right_source=right_source
                ),
            )
            field_columns_for_rule.append(column_name)
        rule_fields[rule.id] = field_columns_for_rule

        combined = _combine([F.col(c) for c in field_columns_for_rule], rule.operator)
        if rule.negate:
            combined = ~combined
        result = result.withColumn(rule_column_name(rule.id), combined)

    return result, rule_fields


def evaluate_match_logic(logic: MatchLogic) -> Column:
    """Combine already-materialised rule columns into the final match flag."""
    from pyspark.sql import functions as F

    terms: list[Column] = [F.col(rule_column_name(rule.id)) for rule in logic.rules if rule.enabled]
    terms.extend(evaluate_match_logic(group) for group in logic.groups)
    if not terms:
        return F.lit(True)
    combined = _combine(terms, logic.operator)
    return ~combined if logic.negate else combined


def _combine(terms: list[Column], operator: LogicalOperator) -> Column:
    from pyspark.sql import functions as F

    if not terms:
        return F.lit(True)
    combined = terms[0]
    for term in terms[1:]:
        combined = (combined & term) if operator == LogicalOperator.AND else (combined | term)
    return combined


def describe_comparison(comparison: FieldComparison) -> str:
    """Human readable rendering used by the UI and the advisor."""
    rule = comparison.rule
    left, right = comparison.left, comparison.right
    if rule == ComparisonRule.EXPRESSION:
        return comparison.expression or "expression"
    if rule == ComparisonRule.NUMERIC_TOLERANCE:
        return f"ABS({left} - {right}) <= {comparison.tolerance}"
    if rule == ComparisonRule.PERCENTAGE_TOLERANCE:
        return f"ABS({left} - {right}) / ABS({left}) * 100 <= {comparison.tolerance}%"
    if rule == ComparisonRule.DATE_TOLERANCE:
        return f"ABS({left} - {right}) <= {comparison.tolerance} {comparison.tolerance_unit or 'seconds'}"
    if rule == ComparisonRule.CASE_INSENSITIVE:
        return f"UPPER(TRIM({left})) = UPPER(TRIM({right}))"
    if rule == ComparisonRule.TRIMMED:
        return f"TRIM({left}) = TRIM({right})"
    if rule == ComparisonRule.DATE_ONLY:
        return f"DATE({left}) = DATE({right})"
    if rule == ComparisonRule.CONTAINS:
        return f"{right} CONTAINS {left}"
    if rule == ComparisonRule.ALWAYS_MATCH:
        return "always true"
    return f"{left} = {right}"


def describe_rule(rule: MatchRule) -> str:
    joiner = f" {rule.operator.value} "
    body = joiner.join(describe_comparison(c) for c in rule.comparisons)
    return f"NOT ({body})" if rule.negate else body
