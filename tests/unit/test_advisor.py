"""Advisor: difference classification, recommendations and chat routing."""

from __future__ import annotations

import pytest

from reconx.advisor.chat import AdvisorContext, ReconAdvisor, detect_intent
from reconx.advisor.recommender import (
    advise_from_profile,
    advise_from_run,
    classify_difference,
    profile_differences,
    suggest_match_logic,
)

pytestmark = pytest.mark.unit


class TestDifferenceClassification:
    @pytest.mark.parametrize(
        "expected,actual,kind",
        [
            ("USD", "usd", "case_only"),
            (" abc ", "abc", "whitespace_only"),
            ("0001234", "1234", "leading_zeros"),
            ("100.00", "100.005", "numeric_small"),
            ("100.00", "250.00", "numeric_large"),
            ("2026-09-10", "10/09/2026", "date_format"),
            ("2026-09-10", "2026-09-11", "date_offset"),
            ("ABCDEFGH", "ABCDE", "truncation"),
            ("abc", None, "one_side_missing"),
            ("abc", "abc", "identical"),
            ("REF-1", "XYZ-9", "unrelated"),
        ],
    )
    def test_classification(self, expected, actual, kind):
        assert classify_difference(expected, actual) == kind

    def test_profile_aggregates_the_dominant_kind(self):
        rows = [
            {"expected_value": "USD", "actual_value": "usd"},
            {"expected_value": "GBP", "actual_value": "gbp"},
            {"expected_value": "EUR", "actual_value": "EUR "},
        ]
        profile = profile_differences(rows)
        kind, share = profile.dominant()
        assert kind == "case_only"
        assert share == pytest.approx(2 / 3, abs=0.01)
        assert profile.total == 3

    def test_numeric_delta_is_tracked(self):
        profile = profile_differences(
            [{"expected_value": "100.00", "actual_value": "100.02"},
             {"expected_value": "50.00", "actual_value": "50.005"}]
        )
        assert profile.max_numeric_delta == pytest.approx(0.02, abs=1e-6)


class TestRunAdvice:
    def _run(self, **overrides):
        run = {
            "run_id": "r1",
            "recon_id": "recon",
            "status": "SUCCESS",
            "records_read": 1000,
            "duration_ms": 60_000,
        }
        run.update(overrides)
        return run

    def test_high_symmetric_one_sided_rate_suggests_a_key_problem(self):
        legs = [
            {
                "leg_id": "leg1",
                "matched": 10,
                "mismatched": 0,
                "left_only": 45,
                "right_only": 45,
                "recon_key": "customer_id",
            }
        ]
        advice = advise_from_run(self._run(), legs, [], [])
        titles = " ".join(a.title for a in advice)
        assert "matched on one side only" in titles
        detail = next(a for a in advice if "one side only" in a.title).detail
        assert "does not line up" in detail

    def test_duplicates_produce_actionable_advice(self):
        legs = [{"leg_id": "leg1", "matched": 100, "duplicates_left": 5, "duplicates_right": 0}]
        advice = advise_from_run(self._run(), legs, [], [])
        duplicate_advice = next(a for a in advice if a.category.value == "DUPLICATES")
        assert duplicate_advice.suggested_config["transformation"]["type"] == "deduplicate"

    def test_case_only_differences_recommend_case_insensitive(self):
        legs = [{"leg_id": "leg1", "matched": 90, "mismatched": 10}]
        exceptions = [
            {"leg_id": "leg1", "field": "currency", "expected_value": "USD", "actual_value": "usd"}
            for _ in range(8)
        ]
        field_metrics = [
            {"leg_id": "leg1", "field_name": "currency", "mismatch_count": 10, "compared_count": 100}
        ]
        advice = advise_from_run(self._run(), legs, field_metrics, exceptions)
        currency_advice = next(a for a in advice if a.field_name == "currency")
        assert currency_advice.suggested_config["comparison"]["rule"] == "case_insensitive"

    def test_small_numeric_differences_recommend_a_tolerance(self):
        legs = [{"leg_id": "leg1", "matched": 90, "mismatched": 10}]
        exceptions = [
            {"leg_id": "leg1", "field": "amount", "expected_value": "100.00", "actual_value": "100.004"}
            for _ in range(6)
        ]
        advice = advise_from_run(self._run(), legs, [], exceptions)
        amount_advice = next(a for a in advice if a.field_name == "amount")
        assert amount_advice.suggested_config["comparison"]["rule"] == "numeric_tolerance"
        assert amount_advice.suggested_config["comparison"]["tolerance"] == 0.01

    def test_large_numeric_differences_are_not_papered_over(self):
        legs = [{"leg_id": "leg1", "matched": 90, "mismatched": 10}]
        exceptions = [
            {"leg_id": "leg1", "field": "amount", "expected_value": "100.00", "actual_value": "875.00"}
            for _ in range(6)
        ]
        advice = advise_from_run(self._run(), legs, [], exceptions)
        amount_advice = next(a for a in advice if a.field_name == "amount")
        assert amount_advice.suggested_config["comparison"]["rule"] == "numeric_exact"
        assert "genuine breaks" in amount_advice.detail

    def test_rule_that_never_matches_is_flagged(self):
        legs = [
            {
                "leg_id": "leg1",
                "matched": 50,
                "mismatched": 50,
                "ruleMetrics": [{"ruleId": "r1", "ruleName": "Reference", "passed": 0, "failed": 100}],
            }
        ]
        advice = advise_from_run(self._run(), legs, [], [])
        assert any("never matched" in a.title for a in advice)

    def test_always_matching_rule_is_flagged_as_redundant(self):
        legs = [
            {
                "leg_id": "leg1",
                "matched": 100,
                "ruleMetrics": [
                    {"ruleId": "r1", "ruleName": "A", "passed": 100, "failed": 0},
                    {"ruleId": "r2", "ruleName": "B", "passed": 60, "failed": 40},
                ],
            }
        ]
        advice = advise_from_run(self._run(), legs, [], [])
        assert any("always matched" in a.title for a in advice)

    def test_failed_run_is_critical(self):
        advice = advise_from_run(
            self._run(status="FAILED", error_message="Connection refused"), [], [], []
        )
        assert advice[0].severity.value == "CRITICAL"

    def test_slow_run_gets_performance_advice(self):
        advice = advise_from_run(self._run(duration_ms=2_400_000), [{"leg_id": "l", "matched": 1}], [], [])
        assert any(a.category.value == "PERFORMANCE" for a in advice)

    def test_healthy_leg_produces_a_positive_note(self):
        legs = [{"leg_id": "leg1", "matched": 1000, "mismatched": 0, "left_only": 0, "right_only": 0}]
        advice = advise_from_run(self._run(), legs, [], [])
        assert any("matched 100.0%" in a.title or "healthy" in a.detail for a in advice)


class TestProfileAdvice:
    def _profile(self):
        return {
            "legId": "leg1",
            "sharedColumns": ["customer_id", "amount", "currency"],
            "leftOnlyColumns": [],
            "rightOnlyColumns": [],
            "leftColumns": [
                {"name": "customer_id", "nullRatio": 0.0, "total_rows": 100, "uniqueness": 1.0}
            ],
            "rightColumns": [],
            "keyCandidates": [
                {
                    "leftColumn": "customer_id",
                    "rightColumn": "customer_id",
                    "score": 0.95,
                    "leftUniqueness": 1.0,
                    "rightUniqueness": 1.0,
                    "leftNullRatio": 0.0,
                    "rightNullRatio": 0.0,
                    "overlapRatio": 0.98,
                    "rawOverlapRatio": 0.10,
                    "normalizationHint": "trim+strip_leading_zeros",
                    "reasons": ["values are unique on both sides"],
                }
            ],
            "comparisonCandidates": [
                {
                    "leftColumn": "amount",
                    "rightColumn": "amount",
                    "suggestedRule": "numeric_tolerance",
                    "tolerance": 0.01,
                    "toleranceUnit": "absolute",
                    "reason": "monetary column",
                    "score": 0.9,
                },
                {
                    "leftColumn": "currency",
                    "rightColumn": "currency",
                    "suggestedRule": "case_insensitive",
                    "reason": "mixed case",
                    "score": 0.85,
                },
            ],
        }

    def test_key_recommendation_includes_normalisation(self):
        advice = advise_from_profile(self._profile())
        key_advice = next(a for a in advice if a.category.value == "KEY_SELECTION")
        assert key_advice.suggested_config["keys"][0]["normalization"]["stripLeadingZeros"] is True

    def test_normalisation_gap_is_flagged_as_a_warning(self):
        advice = advise_from_profile(self._profile())
        normalisation = next(a for a in advice if a.category.value == "NORMALIZATION")
        assert normalisation.severity.value == "WARNING"
        assert "10.0%" in normalisation.detail or "10%" in normalisation.detail

    def test_no_shared_columns_is_reported(self):
        advice = advise_from_profile(
            {"keyCandidates": [], "leftOnlyColumns": ["a"], "rightOnlyColumns": ["b"]}
        )
        assert advice[0].category.value == "KEY_SELECTION"
        assert "no column names in common" in advice[0].detail

    def test_match_logic_suggestion_splits_values_and_references(self):
        profile = self._profile()
        profile["comparisonCandidates"].append(
            {
                "leftColumn": "ext_ref",
                "rightColumn": "ext_ref",
                "suggestedRule": "trimmed",
                "reason": "reference",
                "score": 0.7,
            }
        )
        logic = suggest_match_logic(profile, key_columns=["customer_id"])
        rule_ids = {rule["id"] for rule in logic["rules"]}
        assert "value_rule" in rule_ids
        assert "reference_rule" in rule_ids
        assert logic["operator"] == "AND"


class TestChatRouting:
    @pytest.mark.parametrize(
        "question,intent",
        [
            ("Why did records not match?", "unmatched"),
            ("Which columns should I match on?", "key_selection"),
            ("What tolerance should I set on amount?", "tolerance"),
            ("Should I combine my rules with AND or OR?", "matching_logic"),
            ("What do the duplicates mean?", "duplicates"),
            ("Summarise this run", "summary"),
            ("Why is it so slow?", "performance"),
            ("hello", "help"),
            ("What are the top exceptions?", "exceptions"),
        ],
    )
    def test_intent_detection(self, question, intent):
        assert detect_intent(question) == intent

    def test_answer_without_a_run_is_still_useful(self):
        advisor = ReconAdvisor()
        reply = advisor.answer("Summarise this run", AdvisorContext(), allow_llm=False)
        assert "no completed run" in reply.text.lower()

    def test_unmatched_answer_cites_real_numbers(self):
        advisor = ReconAdvisor()
        context = AdvisorContext(
            recon_id="recon",
            run_id="r1",
            run={"run_id": "r1", "status": "SUCCESS", "records_read": 100},
            legs=[
                {
                    "leg_id": "leg1",
                    "matched": 10,
                    "mismatched": 0,
                    "left_only": 45,
                    "right_only": 45,
                    "recon_key": "customer_id",
                }
            ],
        )
        reply = advisor.answer("Why did records not match?", context, allow_llm=False)
        assert "45" in reply.text
        assert reply.intent == "unmatched"
        assert "does not line up" in reply.text

    def test_matching_logic_answer_explains_and_versus_or(self):
        advisor = ReconAdvisor()
        reply = advisor.answer(
            "Should I use AND or OR for my matching rules?", AdvisorContext(), allow_llm=False
        )
        assert "AND across rules" in reply.text
        assert "OR across rules" in reply.text

    def test_duplicate_answer_reports_zero_cleanly(self):
        advisor = ReconAdvisor()
        context = AdvisorContext(run={"status": "SUCCESS"}, legs=[{"leg_id": "l", "matched": 5}])
        reply = advisor.answer("Are there duplicates?", context, allow_llm=False)
        assert "No duplicate" in reply.text

    def test_reply_serialisation(self):
        advisor = ReconAdvisor()
        reply = advisor.answer("help", AdvisorContext(), allow_llm=False)
        payload = reply.to_dict()
        assert set(payload) >= {"text", "advice", "intent", "source", "citations"}
