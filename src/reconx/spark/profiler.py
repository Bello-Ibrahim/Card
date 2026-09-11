"""Column profiling and matching-candidate discovery.

This is the evidence base for the reconciliation advisor: instead of guessing,
the advisor reads real statistics computed here - uniqueness, null density,
whitespace/case/leading-zero anomalies, cross-source value overlap and the
observed spread of numeric differences.

Everything is computed with Spark aggregations.  The only data that reaches the
driver are small summary rows and a handful of sample values, so profiling a
billion-row table is safe.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import TYPE_CHECKING, Any

from reconx.common.logging import get_logger

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame

log = get_logger(__name__)

#: Cap on how many columns take part in the (more expensive) overlap analysis.
MAX_OVERLAP_CANDIDATES = 8
NUMERIC_TYPES = ("int", "bigint", "smallint", "tinyint", "double", "float", "decimal", "long", "short")
TEMPORAL_TYPES = ("date", "timestamp")


@dataclass
class ColumnProfile:
    name: str
    data_type: str
    total_rows: int
    null_count: int
    distinct_count: int
    min_length: int | None = None
    max_length: int | None = None
    blank_count: int = 0
    whitespace_count: int = 0
    case_variant_count: int = 0
    leading_zero_count: int = 0
    numeric_min: float | None = None
    numeric_max: float | None = None
    sample_values: list[str] = field(default_factory=list)

    @property
    def null_ratio(self) -> float:
        return round(self.null_count / self.total_rows, 6) if self.total_rows else 0.0

    @property
    def uniqueness(self) -> float:
        """Distinct non-null values / non-null rows (1.0 = candidate key)."""
        non_null = self.total_rows - self.null_count
        return round(self.distinct_count / non_null, 6) if non_null else 0.0

    @property
    def is_numeric(self) -> bool:
        return any(self.data_type.startswith(t) for t in NUMERIC_TYPES)

    @property
    def is_temporal(self) -> bool:
        return any(self.data_type.startswith(t) for t in TEMPORAL_TYPES)

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data.update(
            {
                "nullRatio": self.null_ratio,
                "uniqueness": self.uniqueness,
                "isNumeric": self.is_numeric,
                "isTemporal": self.is_temporal,
            }
        )
        return data


@dataclass
class KeyCandidate:
    """A column (or column pair) that could serve as a reconciliation key."""

    left_column: str
    right_column: str
    score: float
    left_uniqueness: float
    right_uniqueness: float
    left_null_ratio: float
    right_null_ratio: float
    overlap_ratio: float | None = None
    raw_overlap_ratio: float | None = None
    normalization_hint: str | None = None
    reasons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "leftColumn": self.left_column,
            "rightColumn": self.right_column,
            "score": round(self.score, 4),
            "leftUniqueness": self.left_uniqueness,
            "rightUniqueness": self.right_uniqueness,
            "leftNullRatio": self.left_null_ratio,
            "rightNullRatio": self.right_null_ratio,
            "overlapRatio": self.overlap_ratio,
            "rawOverlapRatio": self.raw_overlap_ratio,
            "normalizationHint": self.normalization_hint,
            "reasons": self.reasons,
        }


@dataclass
class ComparisonCandidate:
    """A column pair suitable for value comparison, with a suggested rule."""

    left_column: str
    right_column: str
    suggested_rule: str
    reason: str
    tolerance: float | None = None
    tolerance_unit: str | None = None
    score: float = 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "leftColumn": self.left_column,
            "rightColumn": self.right_column,
            "suggestedRule": self.suggested_rule,
            "reason": self.reason,
            "tolerance": self.tolerance,
            "toleranceUnit": self.tolerance_unit,
            "score": round(self.score, 4),
        }


def profile_dataframe(
    dataframe: DataFrame,
    *,
    max_columns: int = 80,
    sample_values: int = 3,
) -> list[ColumnProfile]:
    """Profile every column in a single Spark pass (plus one small sample pass)."""
    from pyspark.sql import functions as F

    columns = dataframe.columns[:max_columns]
    if not columns:
        return []

    aggregations: list[Any] = [F.count(F.lit(1)).alias("__total")]
    types = {f.name: f.dataType.simpleString() for f in dataframe.schema.fields}

    for column in columns:
        quoted = F.col(f"`{column}`")
        as_string = quoted.cast("string")
        aggregations.extend(
            [
                F.sum(F.when(quoted.isNull(), F.lit(1)).otherwise(F.lit(0))).alias(f"null__{column}"),
                F.approx_count_distinct(quoted, 0.02).alias(f"distinct__{column}"),
                F.min(F.length(as_string)).alias(f"minlen__{column}"),
                F.max(F.length(as_string)).alias(f"maxlen__{column}"),
                F.sum(F.when(F.trim(as_string) == "", F.lit(1)).otherwise(F.lit(0))).alias(
                    f"blank__{column}"
                ),
                F.sum(
                    F.when(as_string.isNotNull() & (F.trim(as_string) != as_string), F.lit(1)).otherwise(
                        F.lit(0)
                    )
                ).alias(f"ws__{column}"),
                F.sum(F.when(as_string.rlike("^0[0-9]+$"), F.lit(1)).otherwise(F.lit(0))).alias(
                    f"lz__{column}"
                ),
                F.approx_count_distinct(F.upper(F.trim(as_string)), 0.02).alias(f"udistinct__{column}"),
            ]
        )
        if any(types.get(column, "").startswith(t) for t in NUMERIC_TYPES):
            aggregations.extend(
                [
                    F.min(quoted.cast("double")).alias(f"min__{column}"),
                    F.max(quoted.cast("double")).alias(f"max__{column}"),
                ]
            )

    row = dataframe.agg(*aggregations).collect()[0].asDict()
    total = int(row.get("__total") or 0)

    samples: dict[str, list[str]] = {}
    if sample_values and total:
        sample_rows = dataframe.limit(max(sample_values * 4, 12)).collect()
        for column in columns:
            values: list[str] = []
            for sample_row in sample_rows:
                value = sample_row[column]
                if value is not None and str(value) not in values:
                    values.append(str(value)[:120])
                if len(values) >= sample_values:
                    break
            samples[column] = values

    profiles: list[ColumnProfile] = []
    for column in columns:
        distinct = int(row.get(f"distinct__{column}") or 0)
        upper_distinct = int(row.get(f"udistinct__{column}") or 0)
        profiles.append(
            ColumnProfile(
                name=column,
                data_type=types.get(column, "string"),
                total_rows=total,
                null_count=int(row.get(f"null__{column}") or 0),
                distinct_count=distinct,
                min_length=_int_or_none(row.get(f"minlen__{column}")),
                max_length=_int_or_none(row.get(f"maxlen__{column}")),
                blank_count=int(row.get(f"blank__{column}") or 0),
                whitespace_count=int(row.get(f"ws__{column}") or 0),
                case_variant_count=max(0, distinct - upper_distinct),
                leading_zero_count=int(row.get(f"lz__{column}") or 0),
                numeric_min=_float_or_none(row.get(f"min__{column}")),
                numeric_max=_float_or_none(row.get(f"max__{column}")),
                sample_values=samples.get(column, []),
            )
        )
    log.info("profiler.profiled", columns=len(profiles), rows=total)
    return profiles


def suggest_keys(
    left: DataFrame,
    right: DataFrame,
    left_profiles: list[ColumnProfile],
    right_profiles: list[ColumnProfile],
    *,
    measure_overlap: bool = True,
    max_candidates: int = MAX_OVERLAP_CANDIDATES,
) -> list[KeyCandidate]:
    """Rank column pairs by how well they would work as a reconciliation key."""
    right_by_name = {p.name: p for p in right_profiles}
    right_by_lower = {p.name.lower(): p for p in right_profiles}

    candidates: list[KeyCandidate] = []
    for left_profile in left_profiles:
        right_profile = right_by_name.get(left_profile.name) or right_by_lower.get(left_profile.name.lower())
        if right_profile is None:
            continue
        reasons: list[str] = []
        # Uniqueness on both sides drives the score; nulls and low cardinality hurt.
        score = (left_profile.uniqueness + right_profile.uniqueness) / 2
        score *= 1 - max(left_profile.null_ratio, right_profile.null_ratio)
        if left_profile.name.lower().endswith(("_id", "id", "_no", "_number", "_ref", "reference")):
            score += 0.15
            reasons.append("name looks like an identifier")
        if left_profile.uniqueness > 0.99 and right_profile.uniqueness > 0.99:
            reasons.append("values are unique on both sides")
        elif left_profile.uniqueness < 0.2:
            reasons.append("low cardinality - only useful as part of a composite key")
        if left_profile.is_temporal or right_profile.is_temporal:
            score -= 0.2
            reasons.append("temporal column - usually a filter, not a key")
        if left_profile.is_numeric and _looks_monetary(left_profile.name):
            score -= 0.35
            reasons.append("monetary column - normally reconciled as a value, not used as a key")

        hint = None
        if left_profile.whitespace_count or right_profile.whitespace_count:
            hint = "trim"
            reasons.append("padded values detected - enable trim")
        if left_profile.case_variant_count or right_profile.case_variant_count:
            hint = "trim+upper" if hint else "upper"
            reasons.append("mixed case detected - enable case normalisation")
        if left_profile.leading_zero_count != right_profile.leading_zero_count:
            hint = f"{hint}+strip_leading_zeros" if hint else "strip_leading_zeros"
            reasons.append("leading zeros differ between sources")

        candidates.append(
            KeyCandidate(
                left_column=left_profile.name,
                right_column=right_profile.name,
                score=max(0.0, min(score, 1.3)),
                left_uniqueness=left_profile.uniqueness,
                right_uniqueness=right_profile.uniqueness,
                left_null_ratio=left_profile.null_ratio,
                right_null_ratio=right_profile.null_ratio,
                normalization_hint=hint,
                reasons=reasons,
            )
        )

    candidates.sort(key=lambda c: c.score, reverse=True)
    if measure_overlap and candidates:
        _measure_overlap(left, right, candidates[:max_candidates])
        for candidate in candidates[:max_candidates]:
            if candidate.overlap_ratio is not None:
                candidate.score = candidate.score * 0.6 + candidate.overlap_ratio * 0.4
                if candidate.overlap_ratio < 0.5:
                    candidate.reasons.append(
                        f"only {candidate.overlap_ratio:.0%} of values are found on both sides"
                    )
                if (
                    candidate.raw_overlap_ratio is not None
                    and candidate.overlap_ratio - candidate.raw_overlap_ratio > 0.05
                ):
                    candidate.reasons.append(
                        "normalising (trim/upper/leading zeros) materially improves the overlap"
                    )
        candidates.sort(key=lambda c: c.score, reverse=True)
    return candidates


def _measure_overlap(left: DataFrame, right: DataFrame, candidates: list[KeyCandidate]) -> None:
    """Measure how many distinct values actually appear on both sides."""
    from pyspark.sql import functions as F

    for candidate in candidates:
        try:
            left_values = (
                left.select(
                    F.col(f"`{candidate.left_column}`").cast("string").alias("raw")
                )
                .filter(F.col("raw").isNotNull())
                .select(
                    F.col("raw"),
                    F.regexp_replace(F.upper(F.trim(F.col("raw"))), "^0+(?=.)", "").alias("norm"),
                )
                .distinct()
            )
            right_values = (
                right.select(F.col(f"`{candidate.right_column}`").cast("string").alias("raw"))
                .filter(F.col("raw").isNotNull())
                .select(
                    F.col("raw"),
                    F.regexp_replace(F.upper(F.trim(F.col("raw"))), "^0+(?=.)", "").alias("norm"),
                )
                .distinct()
            )
            stats = (
                left_values.alias("l")
                .join(right_values.alias("r"), F.col("l.norm") == F.col("r.norm"), "full_outer")
                .agg(
                    F.sum(F.when(F.col("l.norm").isNotNull(), F.lit(1)).otherwise(F.lit(0))).alias("left_n"),
                    F.sum(
                        F.when(
                            F.col("l.norm").isNotNull() & F.col("r.norm").isNotNull(), F.lit(1)
                        ).otherwise(F.lit(0))
                    ).alias("both_n"),
                    F.sum(
                        F.when(F.col("l.raw") == F.col("r.raw"), F.lit(1)).otherwise(F.lit(0))
                    ).alias("raw_n"),
                )
                .collect()[0]  # bounded: one aggregate row
            )
            left_n = int(stats["left_n"] or 0)
            candidate.overlap_ratio = round(int(stats["both_n"] or 0) / left_n, 4) if left_n else 0.0
            candidate.raw_overlap_ratio = round(int(stats["raw_n"] or 0) / left_n, 4) if left_n else 0.0
        except Exception as exc:
            log.warning("profiler.overlap_failed", column=candidate.left_column, error=str(exc))


def suggest_comparisons(
    left_profiles: list[ColumnProfile],
    right_profiles: list[ColumnProfile],
    *,
    exclude: set[str] | None = None,
) -> list[ComparisonCandidate]:
    """Suggest a comparison rule per shared column, based on observed data."""
    exclude = exclude or set()
    right_by_name = {p.name: p for p in right_profiles}
    right_by_lower = {p.name.lower(): p for p in right_profiles}

    suggestions: list[ComparisonCandidate] = []
    for left_profile in left_profiles:
        if left_profile.name in exclude:
            continue
        right_profile = right_by_name.get(left_profile.name) or right_by_lower.get(left_profile.name.lower())
        if right_profile is None:
            continue

        if left_profile.is_numeric or right_profile.is_numeric:
            magnitude = max(abs(left_profile.numeric_max or 0), abs(left_profile.numeric_min or 0))
            looks_monetary = _looks_monetary(left_profile.name)
            suggestions.append(
                ComparisonCandidate(
                    left_column=left_profile.name,
                    right_column=right_profile.name,
                    suggested_rule="numeric_tolerance" if looks_monetary else "numeric_exact",
                    tolerance=0.01 if looks_monetary else None,
                    tolerance_unit="absolute" if looks_monetary else None,
                    reason=(
                        "monetary-looking numeric column - a small absolute tolerance absorbs "
                        f"rounding differences (observed magnitude up to {magnitude:,.2f})"
                        if looks_monetary
                        else "numeric column - compare exactly unless rounding differences are expected"
                    ),
                    score=0.9 if looks_monetary else 0.7,
                )
            )
        elif left_profile.is_temporal or right_profile.is_temporal:
            suggestions.append(
                ComparisonCandidate(
                    left_column=left_profile.name,
                    right_column=right_profile.name,
                    suggested_rule="date_only",
                    reason="temporal column - compare the calendar date to ignore time-of-day and timezone skew",
                    score=0.8,
                )
            )
        else:
            has_case = left_profile.case_variant_count or right_profile.case_variant_count
            has_space = left_profile.whitespace_count or right_profile.whitespace_count
            if has_case:
                rule, reason, score = (
                    "case_insensitive",
                    "mixed-case values observed - an exact comparison would report false breaks",
                    0.85,
                )
            elif has_space:
                rule, reason, score = (
                    "trimmed",
                    "padded values observed - trim before comparing",
                    0.8,
                )
            else:
                rule, reason, score = ("exact", "clean string column - exact comparison is appropriate", 0.6)
            suggestions.append(
                ComparisonCandidate(
                    left_column=left_profile.name,
                    right_column=right_profile.name,
                    suggested_rule=rule,
                    reason=reason,
                    score=score,
                )
            )

    suggestions.sort(key=lambda s: s.score, reverse=True)
    return suggestions


def profile_summary(
    left: DataFrame,
    right: DataFrame,
    *,
    left_id: str = "left",
    right_id: str = "right",
    measure_overlap: bool = True,
) -> dict[str, Any]:
    """Full profiling payload persisted with a run and consumed by the advisor."""
    left_profiles = profile_dataframe(left)
    right_profiles = profile_dataframe(right)
    key_candidates = suggest_keys(left, right, left_profiles, right_profiles, measure_overlap=measure_overlap)
    top_keys = {c.left_column for c in key_candidates[:3] if c.score >= 0.7}
    comparison_candidates = suggest_comparisons(left_profiles, right_profiles, exclude=top_keys)
    left_names = {p.name for p in left_profiles}
    right_names = {p.name for p in right_profiles}
    return {
        "leftSourceId": left_id,
        "rightSourceId": right_id,
        "leftColumns": [p.to_dict() for p in left_profiles],
        "rightColumns": [p.to_dict() for p in right_profiles],
        "sharedColumns": sorted(left_names & right_names),
        "leftOnlyColumns": sorted(left_names - right_names),
        "rightOnlyColumns": sorted(right_names - left_names),
        "keyCandidates": [c.to_dict() for c in key_candidates[:15]],
        "comparisonCandidates": [c.to_dict() for c in comparison_candidates[:25]],
    }


MONETARY_TOKENS = ("amount", "amt", "value", "price", "balance", "total", "fee", "charge", "cost", "sum")


def _looks_monetary(name: str) -> bool:
    lowered = name.lower()
    return any(token in lowered for token in MONETARY_TOKENS)


def _int_or_none(value: Any) -> int | None:
    try:
        return int(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def _float_or_none(value: Any) -> float | None:
    try:
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None
