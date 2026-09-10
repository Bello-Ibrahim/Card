"""Advice records produced by the reconciliation advisor."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from reconx.config.enums import AdviceCategory, AdviceSeverity


@dataclass
class Advice:
    """A single, evidence-backed recommendation for a reconciliation officer."""

    category: AdviceCategory
    severity: AdviceSeverity
    title: str
    detail: str
    evidence: dict[str, Any] = field(default_factory=dict)
    suggested_config: dict[str, Any] | None = None
    confidence: float = 0.7
    leg_id: str | None = None
    field_name: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "category": self.category.value,
            "severity": self.severity.value,
            "title": self.title,
            "detail": self.detail,
            "evidence": self.evidence,
            "suggestedConfig": self.suggested_config,
            "confidence": round(self.confidence, 3),
            "legId": self.leg_id,
            "field": self.field_name,
        }


SEVERITY_ORDER = {
    AdviceSeverity.CRITICAL: 0,
    AdviceSeverity.WARNING: 1,
    AdviceSeverity.SUGGESTION: 2,
    AdviceSeverity.INFO: 3,
}


def sort_advice(items: list[Advice]) -> list[Advice]:
    return sorted(items, key=lambda a: (SEVERITY_ORDER[a.severity], -a.confidence))


@dataclass
class DifferenceProfile:
    """How a set of observed value differences actually differ."""

    total: int = 0
    case_only: int = 0
    whitespace_only: int = 0
    leading_zeros: int = 0
    numeric_small: int = 0
    numeric_large: int = 0
    date_format: int = 0
    date_offset: int = 0
    one_side_missing: int = 0
    truncation: int = 0
    unrelated: int = 0
    max_numeric_delta: float | None = None
    max_seconds_delta: float | None = None

    def dominant(self) -> tuple[str, float]:
        """Return the most common difference kind and its share."""
        counts = {
            "case_only": self.case_only,
            "whitespace_only": self.whitespace_only,
            "leading_zeros": self.leading_zeros,
            "numeric_small": self.numeric_small,
            "numeric_large": self.numeric_large,
            "date_format": self.date_format,
            "date_offset": self.date_offset,
            "one_side_missing": self.one_side_missing,
            "truncation": self.truncation,
            "unrelated": self.unrelated,
        }
        if not self.total:
            return "unknown", 0.0
        kind, count = max(counts.items(), key=lambda item: item[1])
        return kind, round(count / self.total, 4)

    def to_dict(self) -> dict[str, Any]:
        kind, share = self.dominant()
        return {
            "total": self.total,
            "dominantKind": kind,
            "dominantShare": share,
            "caseOnly": self.case_only,
            "whitespaceOnly": self.whitespace_only,
            "leadingZeros": self.leading_zeros,
            "numericSmall": self.numeric_small,
            "numericLarge": self.numeric_large,
            "dateFormat": self.date_format,
            "dateOffset": self.date_offset,
            "oneSideMissing": self.one_side_missing,
            "truncation": self.truncation,
            "unrelated": self.unrelated,
            "maxNumericDelta": self.max_numeric_delta,
            "maxSecondsDelta": self.max_seconds_delta,
        }
