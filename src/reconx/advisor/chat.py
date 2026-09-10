"""The reconciliation advisor chatbot.

The advisor answers a reconciliation officer's questions about a run - why
records did not match, which columns to match on, what tolerance to use, what
the duplicates mean - and returns concrete configuration it can apply.

It is **evidence-first and deterministic by default**: every answer is built
from the run metrics, field metrics, exception samples and column profiles that
the platform already stored, so it works offline, is reproducible, and never
invents a number.  When ``ADVISOR_LLM_ENABLED=true`` and an API key is present,
the same evidence bundle is additionally sent to Claude to phrase a richer
narrative answer - the deterministic findings are still shown, and a failure to
reach the model degrades silently back to the built-in answer.
"""

from __future__ import annotations

import os
import re
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Any

from reconx.advisor.models import Advice, sort_advice
from reconx.advisor.recommender import (
    advise_from_profile,
    advise_from_run,
    profile_differences,
    suggest_match_logic,
)
from reconx.common.logging import get_logger
from reconx.common.timeutils import format_duration, utcnow
from reconx.config.enums import AdviceCategory, AdviceSeverity, LogicalOperator

log = get_logger(__name__)

MAX_EXCEPTION_SAMPLE = 400


@dataclass
class AdvisorContext:
    """The evidence bundle an answer is built from."""

    recon_id: str | None = None
    run_id: str | None = None
    definition: dict[str, Any] | None = None
    run: dict[str, Any] | None = None
    legs: list[dict[str, Any]] = field(default_factory=list)
    field_metrics: list[dict[str, Any]] = field(default_factory=list)
    exceptions: list[dict[str, Any]] = field(default_factory=list)
    exception_summary: list[dict[str, Any]] = field(default_factory=list)
    profiles: list[dict[str, Any]] = field(default_factory=list)
    recent_runs: list[dict[str, Any]] = field(default_factory=list)

    @property
    def has_run(self) -> bool:
        return bool(self.run)

    def to_dict(self) -> dict[str, Any]:
        return {
            "reconId": self.recon_id,
            "runId": self.run_id,
            "run": self.run,
            "legs": self.legs,
            "fieldMetrics": self.field_metrics[:50],
            "exceptionSummary": self.exception_summary[:50],
            "exceptionSamples": self.exceptions[:25],
            "profiles": [
                {
                    "legId": p.get("legId"),
                    "keyCandidates": p.get("keyCandidates", [])[:8],
                    "comparisonCandidates": p.get("comparisonCandidates", [])[:10],
                    "sharedColumns": p.get("sharedColumns", []),
                }
                for p in self.profiles
            ],
        }


@dataclass
class AdvisorReply:
    """One answer: prose, the advice behind it, and applicable configuration."""

    text: str
    advice: list[Advice] = field(default_factory=list)
    suggested_config: dict[str, Any] | None = None
    citations: list[str] = field(default_factory=list)
    intent: str = "general"
    source: str = "rules"

    def to_dict(self) -> dict[str, Any]:
        return {
            "text": self.text,
            "advice": [a.to_dict() for a in self.advice],
            "suggestedConfig": self.suggested_config,
            "citations": self.citations,
            "intent": self.intent,
            "source": self.source,
            "generatedAt": utcnow().isoformat(),
        }


#: Intent -> keyword triggers.  Order matters: the first match wins.
INTENT_PATTERNS: list[tuple[str, tuple[str, ...]]] = [
    ("key_selection", ("which column", "what column", "match on", "matching column", "key", "join on", "identifier")),
    ("matching_logic", ("matching logic", "match rule", "and or", "combine", "operator", "multiple rule", "or rule", "and rule")),
    ("unmatched", ("unmatched", "not match", "didn't match", "did not match", "left only", "right only", "one side", "missing record", "break")),
    ("tolerance", ("tolerance", "rounding", "decimal", "amount differ", "small difference", "penny", "cent")),
    ("duplicates", ("duplicate", "dupe", "more than one", "repeated")),
    ("exceptions", ("exception", "top break", "biggest issue", "what failed", "failures")),
    ("performance", ("slow", "performance", "took long", "speed", "faster", "optimis", "optimiz")),
    ("data_quality", ("data quality", "null", "empty", "missing value", "schema", "completeness")),
    ("schedule", ("schedule", "cron", "condition", "availability", "wait for data", "trigger")),
    ("summary", ("summary", "summarise", "summarize", "how did", "overview", "status", "result", "explain the run")),
    ("help", ("help", "what can you do", "capabilities", "how do i use")),
]

GREETING_RE = re.compile(r"^\s*(hi|hello|hey|good (morning|afternoon|evening))\b", re.IGNORECASE)


def detect_intent(question: str) -> str:
    if GREETING_RE.match(question or ""):
        return "help"
    lowered = (question or "").lower()
    for intent, keywords in INTENT_PATTERNS:
        if any(keyword in lowered for keyword in keywords):
            return intent
    return "general"


class ReconAdvisor:
    """Builds evidence bundles and answers questions about them."""

    def __init__(
        self,
        *,
        metrics_repository: Any | None = None,
        recon_repository: Any | None = None,
        run_repository: Any | None = None,
        mongo_db: Any | None = None,
        settings: Any | None = None,
    ) -> None:
        from reconx.config.settings import get_settings

        self.metrics = metrics_repository
        self.recon_repository = recon_repository
        self.run_repository = run_repository
        self.mongo_db = mongo_db
        self.settings = settings or get_settings()

    # ----------------------------------------------------------- evidence
    def build_context(
        self,
        *,
        recon_id: str | None = None,
        run_id: str | None = None,
        include_profiles: bool = True,
    ) -> AdvisorContext:
        context = AdvisorContext(recon_id=recon_id, run_id=run_id)

        if self.metrics is not None:
            try:
                if run_id:
                    context.run = self.metrics.get_run(run_id)
                elif recon_id:
                    runs = self.metrics.list_runs(recon_id=recon_id, limit=1)
                    context.run = runs[0] if runs else None
                if context.run:
                    context.run_id = context.run.get("run_id") or run_id
                    context.recon_id = context.run.get("recon_id") or recon_id
                    context.legs = self.metrics.list_leg_runs(context.run_id)
                    context.field_metrics = self.metrics.list_field_metrics(context.run_id)
                    context.exceptions = self.metrics.list_exceptions(
                        run_id=context.run_id, limit=MAX_EXCEPTION_SAMPLE
                    )
                    context.exception_summary = self.metrics.exception_summary(context.run_id)
                if context.recon_id:
                    context.recent_runs = self.metrics.list_runs(recon_id=context.recon_id, limit=10)
            except Exception as exc:
                log.warning("advisor.metrics_unavailable", error=str(exc)[:200])

        if self.recon_repository is not None and (recon_id or context.recon_id):
            try:
                context.definition = self.recon_repository.get_raw(recon_id or context.recon_id)
            except Exception as exc:
                log.debug("advisor.definition_unavailable", error=str(exc)[:200])

        if include_profiles and self.mongo_db is not None:
            try:
                from reconx.config.store import Collections

                query: dict[str, Any] = {}
                if context.run_id:
                    query["runId"] = context.run_id
                elif context.recon_id:
                    query["reconId"] = context.recon_id
                if query:
                    context.profiles = list(
                        self.mongo_db[Collections.COLUMN_PROFILES]
                        .find(query, {"_id": False})
                        .sort("createdAt", -1)
                        .limit(5)
                    )
                    if not context.profiles and context.recon_id:
                        context.profiles = list(
                            self.mongo_db[Collections.COLUMN_PROFILES]
                            .find({"reconId": context.recon_id}, {"_id": False})
                            .sort("createdAt", -1)
                            .limit(2)
                        )
            except Exception as exc:
                log.debug("advisor.profiles_unavailable", error=str(exc)[:200])

        # Enrich leg dicts with the rule metrics stored alongside the run.
        for leg in context.legs:
            leg.setdefault("ruleMetrics", [])
        return context

    def advise(self, context: AdvisorContext) -> list[Advice]:
        """All advice derivable from the current evidence bundle."""
        advice: list[Advice] = []
        if context.run:
            advice.extend(
                advise_from_run(
                    context.run,
                    context.legs,
                    context.field_metrics,
                    context.exceptions,
                    definition=context.definition,
                    profiles=context.profiles,
                )
            )
        elif context.profiles:
            for profile in context.profiles:
                advice.extend(advise_from_profile(profile, leg_id=profile.get("legId")))
        return sort_advice(advice)

    # -------------------------------------------------------------- answer
    def answer(
        self,
        question: str,
        context: AdvisorContext,
        *,
        history: Sequence[dict[str, str]] | None = None,
        allow_llm: bool = True,
    ) -> AdvisorReply:
        intent = detect_intent(question)
        advice = self.advise(context)
        reply = self._deterministic_answer(question, intent, context, advice)

        if allow_llm and self._llm_enabled():
            enriched = self._llm_answer(question, context, advice, history=history)
            if enriched:
                reply.text = enriched
                reply.source = "rules+llm"
        return reply

    # ------------------------------------------------------- rule answers
    def _deterministic_answer(
        self, question: str, intent: str, context: AdvisorContext, advice: list[Advice]
    ) -> AdvisorReply:
        handlers = {
            "help": self._answer_help,
            "summary": self._answer_summary,
            "unmatched": self._answer_unmatched,
            "key_selection": self._answer_key_selection,
            "matching_logic": self._answer_matching_logic,
            "tolerance": self._answer_tolerance,
            "duplicates": self._answer_duplicates,
            "exceptions": self._answer_exceptions,
            "performance": self._answer_performance,
            "data_quality": self._answer_data_quality,
            "schedule": self._answer_schedule,
        }
        handler = handlers.get(intent, self._answer_general)
        reply = handler(context, advice)
        reply.intent = intent
        if context.run_id:
            reply.citations.append(f"run {context.run_id}")
        if context.recon_id:
            reply.citations.append(f"reconciliation {context.recon_id}")
        return reply

    def _answer_help(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        scope = (
            f"I am looking at run `{context.run_id}` of **{context.recon_id}**."
            if context.has_run
            else "Pick a reconciliation or a run and I will analyse it."
        )
        return AdvisorReply(
            text=(
                f"I am the reconciliation advisor. {scope}\n\n"
                "I can help you with:\n"
                "- **Why records did not match** - I separate real breaks from key/formatting problems\n"
                "- **Which columns to match on** - ranked key candidates with measured value overlap\n"
                "- **Which comparison rule to use** - I classify the actual differences (case, whitespace, "
                "leading zeros, rounding, date format) and recommend the rule that fits\n"
                "- **Matching logic** - how to combine several matching rules with AND / OR\n"
                "- **Duplicates, data quality, tolerances, performance and scheduling**\n\n"
                "Ask me things like *\"why did 40% of records not match?\"*, *\"what should I use as the "
                "key?\"*, *\"what tolerance should I set on amount?\"* or *\"should I combine these rules "
                "with AND or OR?\"*"
            ),
            advice=advice[:3],
        )

    def _answer_summary(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        if not context.has_run:
            return AdvisorReply(
                text="I have no completed run to summarise yet. Run the reconciliation and ask me again.",
                advice=advice[:5],
            )
        run = context.run or {}
        lines = [
            f"**{run.get('recon_name') or context.recon_id}** - run `{context.run_id}` finished with status "
            f"**{run.get('status')}**"
            + (f" for business date {run.get('business_date')}" if run.get("business_date") else "")
            + ".",
            "",
            f"- Records read: **{int(run.get('records_read') or 0):,}**",
            f"- Matched: **{int(run.get('records_matched') or 0):,}**"
            + (
                f" ({run.get('match_percentage')}%)"
                if run.get("match_percentage") is not None
                else ""
            ),
            f"- Unmatched: **{int(run.get('records_unmatched') or 0):,}**",
            f"- Exceptions: **{int(run.get('exceptions') or 0):,}**",
            f"- Duplicates: **{int(run.get('duplicates') or 0):,}**",
            f"- Duration: **{format_duration(run.get('duration_ms'))}**",
        ]
        if context.legs:
            lines += ["", "**Per leg**"]
            for leg in context.legs:
                lines.append(
                    f"- `{leg.get('leg_id')}`: matched {int(leg.get('matched') or 0):,}, "
                    f"mismatch {int(leg.get('mismatched') or 0):,}, "
                    f"left-only {int(leg.get('left_only') or 0):,}, "
                    f"right-only {int(leg.get('right_only') or 0):,}"
                    + (f" - key: `{leg.get('recon_key')}`" if leg.get("recon_key") else "")
                )
        top = [a for a in advice if a.severity in (AdviceSeverity.CRITICAL, AdviceSeverity.WARNING)][:3]
        if top:
            lines += ["", "**What needs your attention**"]
            lines += [f"- {a.title}" for a in top]
        else:
            lines += ["", "Nothing in this run looks like a configuration problem."]
        return AdvisorReply(text="\n".join(lines), advice=advice[:6])

    def _answer_unmatched(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        if not context.legs:
            return AdvisorReply(
                text="I need a completed run to explain unmatched records. Run the reconciliation first.",
                advice=advice[:5],
            )
        lines: list[str] = []
        relevant = [
            a
            for a in advice
            if a.category in (AdviceCategory.KEY_SELECTION, AdviceCategory.NORMALIZATION, AdviceCategory.MATCHING_RULE)
        ]
        for leg in context.legs:
            leg_id = leg.get("leg_id")
            matched = int(leg.get("matched") or 0)
            left_only = int(leg.get("left_only") or 0)
            right_only = int(leg.get("right_only") or 0)
            mismatched = int(leg.get("mismatched") or 0)
            total = matched + left_only + right_only + mismatched
            if not total:
                continue
            lines.append(f"**Leg `{leg_id}`** - key `{leg.get('recon_key')}`")
            lines.append(
                f"- {left_only:,} left-only, {right_only:,} right-only, {mismatched:,} value mismatches "
                f"out of {total:,} ({(left_only + right_only + mismatched) / total:.1%} unmatched)"
            )
            if left_only and right_only:
                ratio = min(left_only, right_only) / max(left_only, right_only)
                if ratio > 0.5:
                    lines.append(
                        "- Both sides have a similar number of one-sided records. That pattern almost always "
                        "means the **key does not line up** rather than data being genuinely absent - the "
                        "same business records are sitting on both sides under different key values."
                    )
                else:
                    lines.append(
                        "- The imbalance suggests one feed is genuinely missing records (timing cut-off, "
                        "filter, or an incomplete extract)."
                    )
            elif left_only or right_only:
                side = "left" if left_only else "right"
                lines.append(
                    f"- Only the {side} side has unmatched records, so this looks like a completeness or "
                    "cut-off difference rather than a key problem."
                )
            if mismatched:
                fields = [
                    m
                    for m in context.field_metrics
                    if str(m.get("leg_id")) == str(leg_id) and int(m.get("mismatch_count") or 0) > 0
                ]
                if fields:
                    worst = sorted(fields, key=lambda m: -int(m.get("mismatch_count") or 0))[:3]
                    lines.append(
                        "- Value mismatches are driven by: "
                        + ", ".join(
                            f"`{m.get('field_name')}` ({int(m.get('mismatch_count') or 0):,} breaks)"
                            for m in worst
                        )
                    )
            lines.append("")

        if relevant:
            lines.append("**Recommended changes**")
            for item in relevant[:4]:
                lines.append(f"- {item.title} - {item.detail}")
        else:
            lines.append(
                "I could not find a formatting or key-normalisation explanation in the sampled exceptions, "
                "so these are most likely genuine breaks to investigate with the source teams."
            )
        suggested = next((a.suggested_config for a in relevant if a.suggested_config), None)
        return AdvisorReply(text="\n".join(lines).strip(), advice=relevant[:6], suggested_config=suggested)

    def _answer_key_selection(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        key_advice = [
            a for a in advice if a.category in (AdviceCategory.KEY_SELECTION, AdviceCategory.NORMALIZATION)
        ]
        if not context.profiles:
            fallback = self._key_advice_from_run(context)
            if fallback:
                return fallback
            return AdvisorReply(
                text=(
                    "I have no column profile for these sources yet, so I cannot rank key candidates from "
                    "measured data. Run the reconciliation with source profiling enabled (**Analyse sources** "
                    "in the designer, or `--profile` on the job) and I will rank every shared column by "
                    "uniqueness, null density and how many values actually appear on both sides."
                ),
                advice=key_advice[:5],
            )

        lines: list[str] = []
        suggested: dict[str, Any] | None = None
        for profile in context.profiles:
            leg_id = profile.get("legId")
            candidates = profile.get("keyCandidates", [])[:6]
            if not candidates:
                continue
            lines.append(f"**Key candidates for leg `{leg_id}`** (ranked)")
            lines.append("")
            lines.append("| Column | Uniqueness | Nulls | Values on both sides | Notes |")
            lines.append("|---|---|---|---|---|")
            for candidate in candidates:
                overlap = candidate.get("overlapRatio")
                lines.append(
                    f"| `{candidate['leftColumn']}` | {candidate['leftUniqueness']:.0%} | "
                    f"{candidate['leftNullRatio']:.1%} | "
                    f"{overlap:.0%} | {'; '.join(candidate.get('reasons', [])[:2]) or '-'} |"
                    if overlap is not None
                    else f"| `{candidate['leftColumn']}` | {candidate['leftUniqueness']:.0%} | "
                    f"{candidate['leftNullRatio']:.1%} | not measured | "
                    f"{'; '.join(candidate.get('reasons', [])[:2]) or '-'} |"
                )
            lines.append("")

        recommendation = next(
            (a for a in key_advice if a.category == AdviceCategory.KEY_SELECTION and a.suggested_config), None
        )
        if recommendation:
            lines.append(f"**Recommendation:** {recommendation.title}")
            lines.append(recommendation.detail)
            suggested = recommendation.suggested_config
        normalisation = [a for a in key_advice if a.category == AdviceCategory.NORMALIZATION]
        if normalisation:
            lines.append("")
            lines.append("**Normalisation you should enable**")
            for item in normalisation[:4]:
                lines.append(f"- {item.title}: {item.detail}")
        return AdvisorReply(text="\n".join(lines).strip(), advice=key_advice[:6], suggested_config=suggested)

    def _key_advice_from_run(self, context: AdvisorContext) -> AdvisorReply | None:
        """Without profiles, infer key problems from the exception pattern."""
        if not context.legs:
            return None
        lines = []
        for leg in context.legs:
            left_only = int(leg.get("left_only") or 0)
            right_only = int(leg.get("right_only") or 0)
            matched = int(leg.get("matched") or 0)
            if not (left_only or right_only):
                continue
            lines.append(
                f"Leg `{leg.get('leg_id')}` currently keys on `{leg.get('recon_key')}` and left "
                f"{left_only:,} left-only / {right_only:,} right-only records against {matched:,} matched."
            )
        if not lines:
            return None
        lines.append("")
        lines.append(
            "To rank alternative key columns from measured data (uniqueness, nulls, and how many values "
            "actually appear on both sides), re-run with source profiling enabled - then ask me again."
        )
        return AdvisorReply(text="\n".join(lines))

    def _answer_matching_logic(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        rule_advice = [a for a in advice if a.category == AdviceCategory.MATCHING_RULE]
        lines = [
            "**How matching logic works here**",
            "",
            "A leg can carry several *matching logics* (rules). Each rule groups the field comparisons that "
            "belong together, and you choose how the comparisons inside a rule combine (AND / OR) and how "
            "the rules themselves combine (AND / OR, optionally negated).",
            "",
            "- **AND across rules** - every rule must hold. Use it when each rule checks a different "
            "dimension that must all agree (amount *and* currency *and* value date). It is stricter and "
            "produces more breaks.",
            "- **OR across rules** - any single rule is enough. Use it when there are alternative ways to "
            "prove the same economic match (the amounts agree, *or* the external reference agrees). It is "
            "how you stop a known, benign difference in one field from creating a break.",
            "",
        ]
        if context.legs:
            lines.append("**What your run used**")
            for leg in context.legs:
                if leg.get("match_logic"):
                    lines.append(f"- `{leg.get('leg_id')}`: `{leg.get('match_logic')}`")
            lines.append("")
        if context.field_metrics:
            noisy = sorted(context.field_metrics, key=lambda m: -int(m.get("mismatch_count") or 0))[:3]
            noisy = [m for m in noisy if int(m.get("mismatch_count") or 0) > 0]
            if noisy:
                lines.append("**Evidence from this run**")
                for metric in noisy:
                    compared = int(metric.get("compared_count") or 0)
                    mismatch = int(metric.get("mismatch_count") or 0)
                    share = f"{mismatch / compared:.1%}" if compared else "n/a"
                    lines.append(
                        f"- `{metric.get('field_name')}` failed on {mismatch:,} of {compared:,} compared "
                        f"pairs ({share}) under rule '{metric.get('rule_name')}'"
                    )
                lines.append("")
                lines.append(
                    "If one of those fields is known to differ legitimately, move it into its own rule and "
                    "combine the rules with **OR** - the pair still matches when the other rule holds, and "
                    "you keep the field's difference visible in `mismatched_fields`."
                )
        suggested: dict[str, Any] | None = None
        if context.profiles:
            key_columns = [
                candidate["leftColumn"]
                for profile in context.profiles
                for candidate in profile.get("keyCandidates", [])[:2]
            ]
            logic = suggest_match_logic(
                context.profiles[0], operator=LogicalOperator.AND, key_columns=key_columns
            )
            if logic:
                suggested = {"matchLogic": logic}
                lines.append("")
                lines.append(
                    "Based on the profiled columns I have drafted a two-rule matching logic you can apply "
                    "and then switch between AND and OR."
                )
        return AdvisorReply(text="\n".join(lines).strip(), advice=rule_advice[:6], suggested_config=suggested)

    def _answer_tolerance(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        tolerance_advice = [
            a for a in advice if a.category in (AdviceCategory.TOLERANCE, AdviceCategory.MATCHING_RULE)
        ]
        numeric = [
            row
            for row in context.exceptions
            if row.get("expected_value") is not None and row.get("actual_value") is not None
        ]
        if not numeric:
            return AdvisorReply(
                text=(
                    "There are no value differences in this run's exception sample, so no tolerance is "
                    "needed. Tolerances only help when the same record carries slightly different values on "
                    "the two sides (rounding, FX precision, fees applied at a different stage)."
                ),
                advice=tolerance_advice[:4],
            )
        by_field: dict[str, list[dict[str, Any]]] = {}
        for row in numeric:
            if row.get("field"):
                by_field.setdefault(str(row["field"]), []).append(row)

        lines = ["**Observed differences by field**", ""]
        suggested: dict[str, Any] | None = None
        for field_name, rows in sorted(by_field.items(), key=lambda item: -len(item[1]))[:6]:
            difference = profile_differences(rows)
            kind, share = difference.dominant()
            detail = f"- `{field_name}`: {len(rows):,} sampled breaks, mostly **{kind.replace('_', ' ')}** ({share:.0%})"
            if difference.max_numeric_delta is not None:
                detail += f", largest difference {difference.max_numeric_delta:,.6g}"
            if difference.max_seconds_delta is not None:
                detail += f", largest time gap {difference.max_seconds_delta / 3600:.1f}h"
            lines.append(detail)
        lines.append("")
        applicable = [a for a in tolerance_advice if a.suggested_config]
        if applicable:
            lines.append("**Recommendation**")
            for item in applicable[:3]:
                lines.append(f"- {item.title}")
                lines.append(f"  {item.detail}")
            suggested = applicable[0].suggested_config
            lines.append("")
            lines.append(
                "A word of caution: a tolerance hides a difference, it does not explain it. Set it to the "
                "smallest value that absorbs the known rounding behaviour, and keep the field in its own "
                "matching rule so you can still see how often it drifts."
            )
        return AdvisorReply(text="\n".join(lines).strip(), advice=tolerance_advice[:6], suggested_config=suggested)

    def _answer_duplicates(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        duplicate_advice = [a for a in advice if a.category == AdviceCategory.DUPLICATES]
        total_left = sum(int(leg.get("duplicates_left") or 0) for leg in context.legs)
        total_right = sum(int(leg.get("duplicates_right") or 0) for leg in context.legs)
        if not (total_left or total_right):
            return AdvisorReply(
                text="No duplicate reconciliation keys were detected in this run - matching is unambiguous.",
                advice=[],
            )
        samples = [
            row
            for row in context.exceptions
            if int(row.get("left_occurrences") or 0) > 1 or int(row.get("right_occurrences") or 0) > 1
        ][:5]
        lines = [
            f"**{total_left:,} left-side and {total_right:,} right-side records share a key with another "
            "record.** Matching is ambiguous for those keys: the engine cannot tell which record on one side "
            "corresponds to which on the other, so the pairing (and any value comparison) is unreliable.",
            "",
            "Two ways to fix it, in order of preference:",
            "1. **Make the key unique** - add the component that distinguishes the records (line number, "
            "sequence, timestamp, or a settlement leg id). This is correct because it reflects the real "
            "grain of the data.",
            "2. **Deduplicate the feed** - add a `deduplicate` transformation on the key columns, ordered by "
            "a timestamp, keeping `last`. Only do this when the extra rows are genuinely restatements.",
        ]
        if samples:
            lines += ["", "**Sample duplicated keys**"]
            for row in samples:
                lines.append(
                    f"- `{row.get('reconciliation_key')}` - {row.get('left_occurrences')} left / "
                    f"{row.get('right_occurrences')} right occurrence(s)"
                )
        return AdvisorReply(
            text="\n".join(lines),
            advice=duplicate_advice[:3],
            suggested_config=duplicate_advice[0].suggested_config if duplicate_advice else None,
        )

    def _answer_exceptions(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        if not context.exception_summary and not context.exceptions:
            return AdvisorReply(text="This run produced no exceptions.", advice=advice[:3])
        lines = ["**Exception breakdown**", ""]
        for row in context.exception_summary[:12]:
            field_part = f" on `{row.get('field')}`" if row.get("field") else ""
            lines.append(
                f"- `{row.get('leg_id')}` - **{row.get('exception_type')}**{field_part}: "
                f"{int(row.get('count') or 0):,}"
            )
        samples = context.exceptions[:5]
        if samples:
            lines += ["", "**Sample records**", ""]
            lines.append("| Key | Type | Field | Expected | Actual |")
            lines.append("|---|---|---|---|---|")
            for row in samples:
                lines.append(
                    f"| `{str(row.get('reconciliation_key'))[:40]}` | {row.get('exception_type')} | "
                    f"{row.get('field') or '-'} | {str(row.get('expected_value'))[:30]} | "
                    f"{str(row.get('actual_value'))[:30]} |"
                )
        top = [a for a in advice if a.severity != AdviceSeverity.INFO][:3]
        if top:
            lines += ["", "**What I would change**"]
            lines += [f"- {a.title}" for a in top]
        return AdvisorReply(text="\n".join(lines), advice=advice[:6])

    def _answer_performance(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        performance = [a for a in advice if a.category == AdviceCategory.PERFORMANCE]
        run = context.run or {}
        lines = []
        if run:
            lines += [
                f"Run `{context.run_id}` took **{format_duration(run.get('duration_ms'))}** for "
                f"{int(run.get('records_read') or 0):,} records "
                f"(read {format_duration(run.get('read_time_ms'))}, "
                f"process {format_duration(run.get('process_time_ms'))}, "
                f"write {format_duration(run.get('write_time_ms'))}).",
                "",
            ]
        lines += [
            "**Levers that matter, in the order I would try them**",
            "1. **Read less** - push filters into the source (a JDBC `query` instead of a whole table, a "
            "date-partitioned path instead of a full bucket scan) and select only the columns you reconcile.",
            "2. **Right-size the shuffle** - `spark.shufflePartitions` should be roughly 2-3x total executor "
            "cores; too few partitions serialises the join, too many floods the scheduler with tiny tasks.",
            "3. **Let AQE work** - adaptive query execution and skew-join handling are on by default; do not "
            "disable them for large joins.",
            "4. **Broadcast the small side** - if one feed is a small reference set, mark it `broadcast: true` "
            "to avoid a shuffle entirely.",
            "5. **Add executors** - only after the above; more executors on a badly shaped job just costs more.",
        ]
        return AdvisorReply(text="\n".join(lines), advice=performance[:4])

    def _answer_data_quality(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        quality = [a for a in advice if a.category == AdviceCategory.DATA_QUALITY]
        lines = [
            "**Data quality is the cheapest place to catch a bad reconciliation.** A run that reconciles a "
            "truncated feed will report thousands of one-sided breaks that have nothing to do with the "
            "matching configuration.",
            "",
            "Checks worth adding to every source:",
            "- `not_null` on each key component (`onFailure: STOP`)",
            "- `row_count` with a `minRows` floor - catches empty or partial extracts",
            "- `unique` on the key columns - catches duplicated feeds before they distort matching",
            "- `schema` when the producer's format is contractual",
        ]
        if quality:
            lines += ["", "**Specific to your data**"]
            for item in quality[:5]:
                lines.append(f"- {item.title}: {item.detail}")
        return AdvisorReply(
            text="\n".join(lines),
            advice=quality[:5],
            suggested_config=quality[0].suggested_config if quality else None,
        )

    def _answer_schedule(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        definition = context.definition or {}
        schedule = definition.get("schedule") or {}
        conditions = definition.get("conditions")
        lines = []
        if schedule:
            lines.append(
                f"This reconciliation is scheduled as **{schedule.get('type')}**"
                + (f" (`{schedule.get('expression')}`)" if schedule.get("expression") else "")
                + f" in {schedule.get('timezone', 'UTC')}."
            )
        if conditions:
            lines.append(
                "It already has data-availability conditions, so the scheduler waits for the data instead of "
                "failing on an empty feed."
            )
        else:
            lines.append(
                "It has **no data-availability conditions**. Without them a run that fires before the feed "
                "lands will report every record as one-sided. Add a condition such as `s3_file_exists` on the "
                "input path or a `jdbc_query` that counts today's rows, and the scheduler will hold the run in "
                "`WAITING_FOR_DATA` until the data is there."
            )
        lines += [
            "",
            "Other scheduling settings worth checking:",
            "- `waitForDataMinutes` - how long to keep re-checking before giving up (the run is then SKIPPED, "
            "not FAILED)",
            "- `retries` - exponential backoff for transient source failures",
            "- `maxConcurrentRuns` - keep at 1 unless runs are genuinely partitioned by business date",
            "- `idempotencyDimensions` - `recon_id + business_date + version` prevents two scheduler nodes "
            "from starting the same logical run",
        ]
        return AdvisorReply(text="\n".join(lines), advice=advice[:3])

    def _answer_general(self, context: AdvisorContext, advice: list[Advice]) -> AdvisorReply:
        if not advice:
            return self._answer_help(context, advice)
        summary = self._answer_summary(context, advice)
        lines = [summary.text, "", "**My recommendations**"]
        for item in advice[:5]:
            lines.append(f"- **{item.title}** - {item.detail}")
        return AdvisorReply(
            text="\n".join(lines),
            advice=advice[:6],
            suggested_config=next((a.suggested_config for a in advice if a.suggested_config), None),
        )

    # ----------------------------------------------------------------- LLM
    def _llm_enabled(self) -> bool:
        return (
            os.getenv("ADVISOR_LLM_ENABLED", "false").lower() == "true"
            and bool(os.getenv("ANTHROPIC_API_KEY"))
        )

    def _llm_answer(
        self,
        question: str,
        context: AdvisorContext,
        advice: list[Advice],
        *,
        history: Sequence[dict[str, str]] | None = None,
    ) -> str | None:
        """Optional narrative answer grounded in the same evidence bundle."""
        import json

        try:
            import httpx
        except ImportError:  # pragma: no cover - optional dependency
            return None

        payload = {
            "model": os.getenv("ADVISOR_LLM_MODEL", "claude-sonnet-5"),
            "max_tokens": int(os.getenv("ADVISOR_LLM_MAX_TOKENS", "1200")),
            "system": (
                "You are the reconciliation advisor inside the ReconX platform, helping a reconciliation "
                "officer. Answer ONLY from the supplied evidence JSON and findings. Never invent numbers, "
                "column names or values; if the evidence does not answer the question, say what is missing "
                "and what to run to get it. Be concise and concrete, use markdown, and prefer specific "
                "configuration advice (key columns, normalisation, comparison rule, tolerance, AND/OR "
                "matching logic) over generalities."
            ),
            "messages": [
                *[
                    {"role": m.get("role", "user"), "content": m.get("content", "")}
                    for m in (history or [])[-6:]
                    if m.get("content")
                ],
                {
                    "role": "user",
                    "content": (
                        f"Question: {question}\n\n"
                        f"Evidence:\n```json\n{json.dumps(context.to_dict(), default=str)[:60000]}\n```\n\n"
                        f"Deterministic findings:\n```json\n"
                        f"{json.dumps([a.to_dict() for a in advice[:12]], default=str)[:20000]}\n```"
                    ),
                },
            ],
        }
        try:
            response = httpx.post(
                os.getenv("ANTHROPIC_API_URL", "https://api.anthropic.com/v1/messages"),
                headers={
                    "x-api-key": os.environ["ANTHROPIC_API_KEY"],
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json",
                },
                json=payload,
                timeout=float(os.getenv("ADVISOR_LLM_TIMEOUT", "45")),
            )
            response.raise_for_status()
            blocks = response.json().get("content", [])
            text = "\n".join(block.get("text", "") for block in blocks if block.get("type") == "text")
            return text.strip() or None
        except Exception as exc:
            log.warning("advisor.llm_failed", error=str(exc)[:200])
            return None
