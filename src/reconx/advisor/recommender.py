"""The recommendation engine behind the reconciliation advisor.

Everything here is derived from evidence the platform already collected:

* **column profiles** (uniqueness, nulls, case/whitespace/leading-zero anomalies,
  cross-source value overlap) written by :mod:`reconx.spark.profiler`
* **run and leg metrics** from the metrics database
* **field metrics** (which comparison failed, how often)
* **exception samples** - the actual expected/actual value pairs, which are
  classified to tell a *formatting* difference from a *real* break

The output is a list of :class:`~reconx.advisor.models.Advice`, several of which
carry a ready-to-apply ``suggestedConfig`` fragment the UI can paste straight
into the reconciliation designer.
"""

from __future__ import annotations

import math
import re
from collections.abc import Iterable, Mapping, Sequence
from datetime import datetime
from typing import Any

from reconx.advisor.models import Advice, DifferenceProfile, sort_advice
from reconx.common.logging import get_logger
from reconx.config.enums import AdviceCategory, AdviceSeverity, LogicalOperator

log = get_logger(__name__)

C = AdviceCategory
S = AdviceSeverity

_DATE_PATTERNS = (
    "%Y-%m-%d",
    "%d/%m/%Y",
    "%m/%d/%Y",
    "%Y/%m/%d",
    "%d-%b-%Y",
    "%Y%m%d",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%dT%H:%M:%S",
    "%d.%m.%Y",
)
_NUMERIC_RE = re.compile(r"^-?[\d,]*\.?\d+$")


# --------------------------------------------------------------------------- #
# Difference classification
# --------------------------------------------------------------------------- #
def _parse_number(value: str) -> float | None:
    cleaned = value.strip().replace(",", "").replace(" ", "")
    if not cleaned or not _NUMERIC_RE.match(cleaned.replace(",", "")):
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None


def _parse_date(value: str) -> tuple[datetime, str] | None:
    text = value.strip()
    for pattern in _DATE_PATTERNS:
        try:
            return datetime.strptime(text, pattern), pattern
        except ValueError:
            continue
    return None


def classify_difference(expected: Any, actual: Any) -> str:
    """Classify one expected/actual pair into a difference *kind*."""
    if expected is None or actual is None or expected == "" or actual == "":
        return "one_side_missing"
    left, right = str(expected), str(actual)
    if left == right:
        return "identical"
    if left.strip() == right.strip():
        return "whitespace_only"
    if left.strip().lower() == right.strip().lower():
        return "case_only"
    if left.strip().lstrip("0") == right.strip().lstrip("0") and (
        left.strip().startswith("0") or right.strip().startswith("0")
    ):
        return "leading_zeros"

    left_number, right_number = _parse_number(left), _parse_number(right)
    if left_number is not None and right_number is not None:
        delta = abs(left_number - right_number)
        magnitude = max(abs(left_number), abs(right_number), 1.0)
        return "numeric_small" if delta / magnitude <= 0.01 else "numeric_large"

    left_date, right_date = _parse_date(left), _parse_date(right)
    if left_date and right_date:
        if left_date[0] == right_date[0]:
            return "date_format"
        return "date_offset"

    shorter, longer = sorted([left.strip(), right.strip()], key=len)
    if shorter and longer.startswith(shorter) and len(shorter) >= 3:
        return "truncation"
    return "unrelated"


def profile_differences(exceptions: Iterable[Mapping[str, Any]]) -> DifferenceProfile:
    """Aggregate difference kinds over a sample of exception rows."""
    profile = DifferenceProfile()
    for row in exceptions:
        expected, actual = row.get("expected_value"), row.get("actual_value")
        if expected is None and actual is None:
            continue
        kind = classify_difference(expected, actual)
        if kind == "identical":
            continue
        profile.total += 1
        attribute = {
            "case_only": "case_only",
            "whitespace_only": "whitespace_only",
            "leading_zeros": "leading_zeros",
            "numeric_small": "numeric_small",
            "numeric_large": "numeric_large",
            "date_format": "date_format",
            "date_offset": "date_offset",
            "one_side_missing": "one_side_missing",
            "truncation": "truncation",
        }.get(kind, "unrelated")
        setattr(profile, attribute, getattr(profile, attribute) + 1)

        if kind in ("numeric_small", "numeric_large"):
            left_number, right_number = _parse_number(str(expected)), _parse_number(str(actual))
            if left_number is not None and right_number is not None:
                delta = abs(left_number - right_number)
                profile.max_numeric_delta = max(profile.max_numeric_delta or 0.0, delta)
        if kind == "date_offset":
            left_date, right_date = _parse_date(str(expected)), _parse_date(str(actual))
            if left_date and right_date:
                seconds = abs((left_date[0] - right_date[0]).total_seconds())
                profile.max_seconds_delta = max(profile.max_seconds_delta or 0.0, seconds)
    return profile


# --------------------------------------------------------------------------- #
# Advice from column profiles (design time)
# --------------------------------------------------------------------------- #
def advise_from_profile(profile: Mapping[str, Any], *, leg_id: str | None = None) -> list[Advice]:
    """Recommend keys, normalisation and comparison rules before a run exists."""
    advice: list[Advice] = []
    key_candidates = list(profile.get("keyCandidates", []))
    comparison_candidates = list(profile.get("comparisonCandidates", []))

    if not key_candidates:
        advice.append(
            Advice(
                category=C.KEY_SELECTION,
                severity=S.WARNING,
                title="No shared columns found between the two sources",
                detail=(
                    "The two datasets have no column names in common, so no reconciliation key can be "
                    "suggested automatically. Map the columns explicitly (left/right) or add a rename "
                    "transformation to align the names first."
                ),
                evidence={
                    "leftOnlyColumns": profile.get("leftOnlyColumns", [])[:20],
                    "rightOnlyColumns": profile.get("rightOnlyColumns", [])[:20],
                },
                confidence=0.9,
                leg_id=leg_id,
            )
        )
        return advice

    strong = [c for c in key_candidates if c["score"] >= 0.75]
    composite = _suggest_composite_key(key_candidates)
    if composite:
        advice.append(
            Advice(
                category=C.KEY_SELECTION,
                severity=S.SUGGESTION,
                title=f"Suggested reconciliation key: {' + '.join(c['leftColumn'] for c in composite)}",
                detail=_describe_key_suggestion(composite),
                evidence={
                    "candidates": [
                        {
                            "column": c["leftColumn"],
                            "score": c["score"],
                            "uniqueness": c["leftUniqueness"],
                            "overlap": c["overlapRatio"],
                            "reasons": c["reasons"],
                        }
                        for c in composite
                    ]
                },
                suggested_config={"keys": _key_config(composite)},
                confidence=min(0.95, 0.5 + 0.15 * len(composite) + (composite[0]["score"] / 4)),
                leg_id=leg_id,
            )
        )

    for candidate in key_candidates[:6]:
        hint = candidate.get("normalizationHint")
        overlap = candidate.get("overlapRatio")
        raw_overlap = candidate.get("rawOverlapRatio")
        if hint and overlap is not None and raw_overlap is not None and overlap - raw_overlap > 0.02:
            advice.append(
                Advice(
                    category=C.NORMALIZATION,
                    severity=S.WARNING if overlap - raw_overlap > 0.3 else S.SUGGESTION,
                    title=f"'{candidate['leftColumn']}' needs normalisation before matching",
                    detail=(
                        f"Only {raw_overlap:.1%} of the raw values in '{candidate['leftColumn']}' appear on "
                        f"both sides, but {overlap:.1%} match once {hint.replace('+', ' + ')} normalisation is "
                        "applied. Without it these records would be reported as one-sided breaks."
                    ),
                    evidence={
                        "rawOverlap": raw_overlap,
                        "normalisedOverlap": overlap,
                        "hint": hint,
                        "reasons": candidate.get("reasons", []),
                    },
                    suggested_config={"normalization": _normalization_config(hint)},
                    confidence=0.85,
                    leg_id=leg_id,
                    field_name=candidate["leftColumn"],
                )
            )

    for candidate in comparison_candidates[:10]:
        rule = candidate["suggestedRule"]
        if rule == "exact":
            continue
        advice.append(
            Advice(
                category=C.MATCHING_RULE,
                severity=S.SUGGESTION,
                title=f"Compare '{candidate['leftColumn']}' with rule '{rule}'",
                detail=candidate["reason"],
                evidence={"score": candidate["score"]},
                suggested_config={
                    "comparison": {
                        "left": candidate["leftColumn"],
                        "right": candidate["rightColumn"],
                        "rule": rule,
                        **({"tolerance": candidate["tolerance"]} if candidate.get("tolerance") else {}),
                        **(
                            {"toleranceUnit": candidate["toleranceUnit"]}
                            if candidate.get("toleranceUnit")
                            else {}
                        ),
                    }
                },
                confidence=float(candidate.get("score", 0.6)),
                leg_id=leg_id,
                field_name=candidate["leftColumn"],
            )
        )

    for side in ("leftColumns", "rightColumns"):
        for column in profile.get(side, []):
            if column.get("nullRatio", 0) > 0.5 and column["name"] in {
                c["leftColumn"] for c in key_candidates[:5]
            }:
                advice.append(
                    Advice(
                        category=C.DATA_QUALITY,
                        severity=S.WARNING,
                        title=f"'{column['name']}' is {column['nullRatio']:.0%} NULL on the {side[:-7]} side",
                        detail=(
                            "A key component that is mostly NULL will collapse many records onto the same "
                            "key and produce spurious duplicates. Choose a different key column, or add a "
                            "data-quality check so the run stops when the feed is incomplete."
                        ),
                        evidence={"nullRatio": column["nullRatio"], "totalRows": column["total_rows"]},
                        suggested_config={
                            "dataQuality": {
                                "type": "not_null",
                                "columns": [column["name"]],
                                "onFailure": "STOP",
                            }
                        },
                        confidence=0.8,
                        field_name=column["name"],
                        leg_id=leg_id,
                    )
                )
    if strong:
        advice.append(
            Advice(
                category=C.COVERAGE,
                severity=S.INFO,
                title=f"{len(strong)} column(s) look like usable key components",
                detail=", ".join(
                    f"{c['leftColumn']} (uniqueness {c['leftUniqueness']:.0%}"
                    + (f", overlap {c['overlapRatio']:.0%}" if c.get("overlapRatio") is not None else "")
                    + ")"
                    for c in strong[:6]
                ),
                evidence={"count": len(strong)},
                confidence=0.6,
                leg_id=leg_id,
            )
        )
    return sort_advice(advice)


def _suggest_composite_key(candidates: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    """Pick the smallest set of columns that plausibly identifies a record."""
    usable = [c for c in candidates if c["score"] >= 0.45 and c.get("leftNullRatio", 0) < 0.5]
    if not usable:
        return []
    best = usable[0]
    if best["leftUniqueness"] >= 0.99 and best["rightUniqueness"] >= 0.99:
        return [best]
    # Combine until the product of uniqueness suggests a unique key.
    chosen: list[Mapping[str, Any]] = []
    combined_uniqueness = 0.0
    for candidate in usable[:4]:
        chosen.append(candidate)
        combined_uniqueness = 1 - math.prod(1 - min(c["leftUniqueness"], 0.999) for c in chosen)
        if combined_uniqueness >= 0.995:
            break
    return chosen


def _describe_key_suggestion(candidates: Sequence[Mapping[str, Any]]) -> str:
    parts = []
    for candidate in candidates:
        detail = f"{candidate['leftColumn']} (uniqueness {candidate['leftUniqueness']:.0%}"
        if candidate.get("overlapRatio") is not None:
            detail += f", {candidate['overlapRatio']:.0%} of values found on both sides"
        detail += ")"
        parts.append(detail)
    body = "; ".join(parts)
    hints = {c.get("normalizationHint") for c in candidates if c.get("normalizationHint")}
    suffix = (
        f" Apply {', '.join(sorted(h.replace('+', ' + ') for h in hints))} normalisation to these components."
        if hints
        else ""
    )
    return f"Build the reconciliation key from {body}.{suffix}"


def _key_config(candidates: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    keys: list[dict[str, Any]] = []
    for candidate in candidates:
        entry: dict[str, Any] = {
            "left": candidate["leftColumn"],
            "right": candidate["rightColumn"],
            "alias": candidate["leftColumn"],
        }
        if candidate.get("normalizationHint"):
            entry["normalization"] = _normalization_config(candidate["normalizationHint"])
        keys.append(entry)
    return keys


def _normalization_config(hint: str) -> dict[str, Any]:
    config: dict[str, Any] = {"trim": True}
    if "upper" in hint:
        config["case"] = "upper"
    if "strip_leading_zeros" in hint:
        config["stripLeadingZeros"] = True
    return config


# --------------------------------------------------------------------------- #
# Advice from a completed run
# --------------------------------------------------------------------------- #
def advise_from_run(
    run: Mapping[str, Any],
    legs: Sequence[Mapping[str, Any]],
    field_metrics: Sequence[Mapping[str, Any]],
    exceptions: Sequence[Mapping[str, Any]],
    *,
    definition: Mapping[str, Any] | None = None,
    profiles: Sequence[Mapping[str, Any]] | None = None,
) -> list[Advice]:
    """Explain a completed run and recommend concrete configuration changes."""
    advice: list[Advice] = []
    status = str(run.get("status", ""))

    if status == "FAILED":
        advice.append(
            Advice(
                category=C.OPERATIONS,
                severity=S.CRITICAL,
                title="The run failed before producing results",
                detail=(
                    f"Error: {run.get('error_message') or run.get('errorMessage') or 'no message recorded'}. "
                    "Fix the underlying cause and re-run; results below (if any) are partial."
                ),
                evidence={"status": status, "runId": run.get("run_id") or run.get("runId")},
                confidence=1.0,
            )
        )

    exceptions_by_leg: dict[str, list[Mapping[str, Any]]] = {}
    for row in exceptions:
        exceptions_by_leg.setdefault(str(row.get("leg_id") or row.get("legId") or ""), []).append(row)

    for leg in legs:
        leg_id = str(leg.get("leg_id") or leg.get("legId") or "")
        advice.extend(_advise_leg(leg, leg_id, exceptions_by_leg.get(leg_id, []), field_metrics))

    advice.extend(_advise_performance(run, legs))

    if profiles:
        for profile in profiles:
            advice.extend(advise_from_profile(profile, leg_id=profile.get("legId")))

    return sort_advice(advice)


def _advise_leg(
    leg: Mapping[str, Any],
    leg_id: str,
    leg_exceptions: Sequence[Mapping[str, Any]],
    field_metrics: Sequence[Mapping[str, Any]],
) -> list[Advice]:
    advice: list[Advice] = []
    matched = int(leg.get("matched") or 0)
    mismatched = int(leg.get("mismatched") or 0)
    left_only = int(leg.get("left_only") or leg.get("leftOnly") or 0)
    right_only = int(leg.get("right_only") or leg.get("rightOnly") or 0)
    duplicates_left = int(leg.get("duplicates_left") or leg.get("duplicatesLeft") or 0)
    duplicates_right = int(leg.get("duplicates_right") or leg.get("duplicatesRight") or 0)
    left_records = int(leg.get("left_records") or leg.get("leftRecords") or 0)
    right_records = int(leg.get("right_records") or leg.get("rightRecords") or 0)
    total = matched + mismatched + left_only + right_only

    # --- key quality -------------------------------------------------------
    one_sided = left_only + right_only
    if total and one_sided / total > 0.3:
        both_sides_high = left_only > 0 and right_only > 0
        advice.append(
            Advice(
                category=C.KEY_SELECTION,
                severity=S.CRITICAL if one_sided / total > 0.6 else S.WARNING,
                title=f"{one_sided:,} of {total:,} records ({one_sided / total:.0%}) matched on one side only",
                detail=(

                        "Records are unmatched on both sides in similar proportions, which is the classic "
                        "signature of a key that does not line up (formatting differences, a missing key "
                        "component, or the wrong column). Profile the sources and check the value overlap "
                        "of each key component before treating these as genuine breaks."
                        if both_sides_high
                        else "One feed contains records the other does not. If that is expected (timing "
                        "cut-off, in-flight items) add a filter or a data-availability condition; otherwise "
                        "the feed is incomplete."

                ),
                evidence={
                    "leftOnly": left_only,
                    "rightOnly": right_only,
                    "matched": matched,
                    "leftRecords": left_records,
                    "rightRecords": right_records,
                    "reconKey": leg.get("recon_key") or leg.get("reconKey"),
                },
                confidence=0.75 if both_sides_high else 0.6,
                leg_id=leg_id,
            )
        )

    # --- duplicates --------------------------------------------------------
    if duplicates_left or duplicates_right:
        advice.append(
            Advice(
                category=C.DUPLICATES,
                severity=S.WARNING,
                title=f"Duplicate keys detected ({duplicates_left:,} left / {duplicates_right:,} right)",
                detail=(
                    "More than one record shares the same reconciliation key, so matching is ambiguous. "
                    "Either add a key component that makes records unique (a sequence number, a timestamp, "
                    "or a line id), or deduplicate the feed with a 'deduplicate' transformation keeping the "
                    "latest record per key."
                ),
                evidence={
                    "duplicatesLeft": duplicates_left,
                    "duplicatesRight": duplicates_right,
                    "duplicateKeys": leg.get("duplicate_keys") or leg.get("duplicateKeys"),
                },
                suggested_config={
                    "transformation": {
                        "type": "deduplicate",
                        "columns": ["<key columns>"],
                        "orderBy": ["<timestamp column>"],
                        "keep": "last",
                    }
                },
                confidence=0.8,
                leg_id=leg_id,
            )
        )

    # --- field-level differences ------------------------------------------
    by_field: dict[str, list[Mapping[str, Any]]] = {}
    for row in leg_exceptions:
        if row.get("field"):
            by_field.setdefault(str(row["field"]), []).append(row)

    leg_field_metrics = {
        str(m.get("field_name") or m.get("fieldName")): m
        for m in field_metrics
        if str(m.get("leg_id") or m.get("legId")) == leg_id
    }

    for field_name, rows in sorted(by_field.items(), key=lambda item: -len(item[1])):
        difference = profile_differences(rows)
        kind, share = difference.dominant()
        metric = leg_field_metrics.get(field_name, {})
        mismatch_count = int(metric.get("mismatch_count") or metric.get("mismatchCount") or len(rows))
        compared = int(metric.get("compared_count") or metric.get("comparedCount") or 0)
        rate = (mismatch_count / compared) if compared else None
        suggestion = _rule_for_difference(kind, difference, field_name)
        if suggestion is None:
            continue
        rule, explanation, config, confidence = suggestion
        advice.append(
            Advice(
                category=C.TOLERANCE if "tolerance" in rule else C.MATCHING_RULE,
                severity=S.SUGGESTION if share >= 0.5 else S.INFO,
                title=f"'{field_name}': {share:.0%} of breaks are {kind.replace('_', ' ')} - use '{rule}'",
                detail=explanation,
                evidence={
                    "mismatchCount": mismatch_count,
                    "comparedCount": compared,
                    "mismatchRate": round(rate, 4) if rate is not None else None,
                    "differenceProfile": difference.to_dict(),
                    "samples": [
                        {"expected": r.get("expected_value"), "actual": r.get("actual_value")}
                        for r in rows[:3]
                    ],
                },
                suggested_config={"comparison": config},
                confidence=confidence * (0.6 + 0.4 * share),
                leg_id=leg_id,
                field_name=field_name,
            )
        )

    # --- matching-rule effectiveness --------------------------------------
    rule_metrics = leg.get("ruleMetrics") or leg.get("rule_metrics") or []
    for rule_metric in rule_metrics:
        passed = int(rule_metric.get("passed") or 0)
        failed = int(rule_metric.get("failed") or 0)
        if passed + failed == 0:
            continue
        if passed == 0:
            advice.append(
                Advice(
                    category=C.MATCHING_RULE,
                    severity=S.WARNING,
                    title=f"Matching logic '{rule_metric.get('ruleName')}' never matched",
                    detail=(
                        f"All {failed:,} compared pairs failed this rule. Either the columns it compares are "
                        "not populated on both sides, the comparison rule is too strict, or the rule is "
                        "redundant. Review it before relying on the results."
                    ),
                    evidence=dict(rule_metric),
                    confidence=0.85,
                    leg_id=leg_id,
                )
            )
        elif failed == 0 and len(rule_metrics) > 1:
            advice.append(
                Advice(
                    category=C.MATCHING_RULE,
                    severity=S.INFO,
                    title=f"Matching logic '{rule_metric.get('ruleName')}' always matched",
                    detail=(
                        "This rule passed on every compared pair, so it is not discriminating between "
                        "matches and breaks. With an OR combination it makes the other rules redundant - "
                        "consider AND, or remove it."
                    ),
                    evidence=dict(rule_metric),
                    confidence=0.7,
                    leg_id=leg_id,
                )
            )

    # --- aggregates --------------------------------------------------------
    for aggregate in leg.get("aggregates") or []:
        if not aggregate.get("matched", True):
            advice.append(
                Advice(
                    category=C.COVERAGE,
                    severity=S.WARNING,
                    title=f"Aggregate '{aggregate.get('name')}' does not balance",
                    detail=(
                        f"{aggregate.get('function')} differs between the two sides "
                        f"(left {aggregate.get('leftValue')}, right {aggregate.get('rightValue')}, "
                        f"difference {aggregate.get('difference')}). Record-level matching can look healthy "
                        "while totals disagree when records are missing or duplicated - reconcile the "
                        "one-sided records first."
                    ),
                    evidence=dict(aggregate),
                    confidence=0.9,
                    leg_id=leg_id,
                )
            )

    if total and matched / total >= 0.99 and not duplicates_left and not duplicates_right:
        advice.append(
            Advice(
                category=C.COVERAGE,
                severity=S.INFO,
                title=f"Leg '{leg_id}' matched {matched / total:.1%} of records",
                detail="This leg is healthy - no configuration change is indicated.",
                evidence={"matched": matched, "total": total},
                confidence=0.9,
                leg_id=leg_id,
            )
        )
    return advice


def _rule_for_difference(
    kind: str, difference: DifferenceProfile, field_name: str
) -> tuple[str, str, dict[str, Any], float] | None:
    """Map a dominant difference kind to a concrete comparison-rule change."""
    if kind == "case_only":
        return (
            "case_insensitive",
            f"The values are identical apart from letter case (e.g. 'usd' vs 'USD'). Comparing "
            f"'{field_name}' case-insensitively removes these breaks without weakening the check.",
            {"rule": "case_insensitive"},
            0.9,
        )
    if kind == "whitespace_only":
        return (
            "trimmed",
            f"The values differ only by surrounding whitespace. Trim '{field_name}' before comparing.",
            {"rule": "trimmed"},
            0.9,
        )
    if kind == "leading_zeros":
        return (
            "expression",
            f"One side pads '{field_name}' with leading zeros. Normalise the column (stripLeadingZeros) "
            "or compare with an expression that strips them.",
            {
                "rule": "expression",
                "expression": (
                    f"regexp_replace(trim(left.{field_name}), '^0+(?=.)', '') = "
                    f"regexp_replace(trim(right.{field_name}), '^0+(?=.)', '')"
                ),
            },
            0.85,
        )
    if kind == "numeric_small":
        delta = difference.max_numeric_delta or 0.01
        tolerance = _round_tolerance(delta)
        return (
            "numeric_tolerance",
            f"The differences are small rounding-scale amounts (largest observed: {delta:.6g}). A tolerance "
            f"of {tolerance} absorbs them while still catching real value breaks.",
            {"rule": "numeric_tolerance", "tolerance": tolerance, "toleranceUnit": "absolute"},
            0.85,
        )
    if kind == "numeric_large":
        return (
            "numeric_exact",
            "The amounts differ materially - these look like genuine breaks rather than a formatting or "
            "rounding issue. Investigate the source data before relaxing the comparison.",
            {"rule": "numeric_exact"},
            0.8,
        )
    if kind == "date_format":
        return (
            "date_only",
            f"'{field_name}' holds the same instant written in different formats. Compare it as a date "
            "(date_only) or normalise both sides with a date format.",
            {"rule": "date_only"},
            0.85,
        )
    if kind == "date_offset":
        seconds = difference.max_seconds_delta or 0
        hours = max(1, round(seconds / 3600))
        return (
            "date_tolerance",
            f"The timestamps differ by up to {seconds / 3600:.1f} hour(s), which usually means a timezone or "
            f"cut-off difference. A date tolerance of {hours} hour(s) covers it - confirm the timezone "
            "handling of both feeds first.",
            {"rule": "date_tolerance", "tolerance": hours, "toleranceUnit": "hours"},
            0.7,
        )
    if kind == "truncation":
        return (
            "expression",
            f"One side stores a truncated version of '{field_name}'. Compare a fixed prefix on both sides "
            "rather than the whole value.",
            {
                "rule": "expression",
                "expression": (
                    f"substr(trim(left.{field_name}), 1, 20) = substr(trim(right.{field_name}), 1, 20)"
                ),
            },
            0.6,
        )
    if kind == "one_side_missing":
        return (
            "exact",
            f"'{field_name}' is populated on one side only. That is a data completeness problem, not a "
            "matching-rule problem - add a not_null data-quality check so the run stops when the field is "
            "missing, or exclude it from the comparison if it is genuinely optional.",
            {"rule": "exact", "nullEqualsNull": True},
            0.75,
        )
    return None


def _round_tolerance(delta: float) -> float:
    """Round a raw delta up to a sane, human tolerance (0.01, 0.05, 0.1, 1 ...)."""
    if delta <= 0:
        return 0.01
    for candidate in (0.01, 0.05, 0.1, 0.5, 1.0, 5.0, 10.0, 50.0, 100.0):
        if delta <= candidate:
            return candidate
    return round(delta * 1.1, 2)


def _advise_performance(run: Mapping[str, Any], legs: Sequence[Mapping[str, Any]]) -> list[Advice]:
    advice: list[Advice] = []
    duration = run.get("duration_ms") or run.get("durationMs")
    records = int(run.get("records_read") or run.get("recordsRead") or 0)
    if duration and duration > 1_800_000:
        advice.append(
            Advice(
                category=C.PERFORMANCE,
                severity=S.SUGGESTION,
                title=f"The run took {duration / 60000:.0f} minutes",
                detail=(
                    "For long-running reconciliations, check the Spark configuration: raise "
                    "spark.shufflePartitions for large joins, enable dynamic allocation, and make sure "
                    "source filters are pushed down (use a JDBC 'query' rather than reading a whole table)."
                ),
                evidence={"durationMs": duration, "recordsRead": records},
                confidence=0.6,
            )
        )
    read_ms = int(run.get("read_time_ms") or run.get("readTimeMs") or 0)
    if duration and read_ms and read_ms / duration > 0.6:
        advice.append(
            Advice(
                category=C.PERFORMANCE,
                severity=S.SUGGESTION,
                title=f"{read_ms / duration:.0%} of the run was spent reading sources",
                detail=(
                    "Reading dominates this run. Narrow the data at the source: select only the columns you "
                    "reconcile, filter by business date in the query/path, and prefer Parquet over CSV where "
                    "you control the feed."
                ),
                evidence={"readTimeMs": read_ms, "durationMs": duration},
                confidence=0.65,
            )
        )
    return advice


# --------------------------------------------------------------------------- #
# Suggested matching logic (multi-rule)
# --------------------------------------------------------------------------- #
def suggest_match_logic(
    profile: Mapping[str, Any],
    *,
    operator: LogicalOperator = LogicalOperator.AND,
    key_columns: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Build a ready-to-use multi-rule matching logic from a column profile.

    Value-bearing columns (amounts, dates, quantities) go into one rule, and
    reference/identifier columns into a second one, so an operator can combine
    them with AND (both must agree) or OR (either is enough).
    """
    excluded = set(key_columns or [])
    value_comparisons: list[dict[str, Any]] = []
    reference_comparisons: list[dict[str, Any]] = []
    other_comparisons: list[dict[str, Any]] = []

    for candidate in profile.get("comparisonCandidates", []):
        column = candidate["leftColumn"]
        if column in excluded:
            continue
        comparison: dict[str, Any] = {
            "left": column,
            "right": candidate["rightColumn"],
            "rule": candidate["suggestedRule"],
        }
        if candidate.get("tolerance") is not None:
            comparison["tolerance"] = candidate["tolerance"]
        if candidate.get("toleranceUnit"):
            comparison["toleranceUnit"] = candidate["toleranceUnit"]
        lowered = column.lower()
        if candidate["suggestedRule"].startswith("numeric") or candidate["suggestedRule"].startswith("date"):
            value_comparisons.append(comparison)
        elif any(token in lowered for token in ("ref", "reference", "id", "number", "no")):
            reference_comparisons.append(comparison)
        else:
            other_comparisons.append(comparison)

    rules: list[dict[str, Any]] = []
    if value_comparisons:
        rules.append(
            {
                "id": "value_rule",
                "name": "Values agree",
                "operator": LogicalOperator.AND.value,
                "comparisons": value_comparisons[:6],
            }
        )
    if reference_comparisons:
        rules.append(
            {
                "id": "reference_rule",
                "name": "References agree",
                "operator": LogicalOperator.AND.value,
                "comparisons": reference_comparisons[:4],
            }
        )
    if other_comparisons and len(rules) < 3:
        rules.append(
            {
                "id": "attribute_rule",
                "name": "Attributes agree",
                "operator": LogicalOperator.AND.value,
                "comparisons": other_comparisons[:6],
            }
        )
    if not rules:
        return {}
    return {"operator": operator.value, "rules": rules}
