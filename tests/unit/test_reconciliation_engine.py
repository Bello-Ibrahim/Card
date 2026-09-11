"""Reconciliation engine semantics (runs against a local SparkSession)."""

from __future__ import annotations

import pytest

from reconx.config.models import LegSpec
from reconx.spark.keys import KEY_COLUMN, add_reconciliation_key, describe_key
from reconx.spark.reconciliation.comparisons import describe_comparison, translate_expression
from reconx.spark.reconciliation.engine import ReconciliationEngine

pytestmark = [pytest.mark.unit, pytest.mark.spark]

LEFT_ROWS = [
    ("US", "0001", "T1001", "100.50", "USD", "REF-1", "2026-09-10"),
    ("US", "0002", "T1002", "250.00", "usd", "REF-2", "2026-09-10"),
    ("UK", "0003", "T1003", "300.75", "GBP", "REF-3", "2026-09-10"),
    ("UK", "0004", "T1004", "410.00", "GBP", "REF-4", "2026-09-10"),
    ("US", "0005", "T1005", "500.25", "USD", "REF-5", "2026-09-10"),
    ("US", "0006", "T1006", "600.00", "USD", "REF-6", "2026-09-10"),
    ("US", "0006", "T1006", "600.00", "USD", "REF-6", "2026-09-10"),
]
RIGHT_ROWS = [
    ("US", "1", "T1001", "100.50", "USD", "REF-1", "2026-09-10"),
    ("US", "2", "T1002", "250.01", "USD", "REF-2", "2026-09-10"),
    ("UK", "3", "T1003", "999.99", "GBP", "REF-3", "2026-09-10"),
    ("UK", "4", "T1004", "410.00", "EUR", "REF-X", "2026-09-10"),
    ("US", "7", "T1007", "700.00", "USD", "REF-7", "2026-09-10"),
]
COLUMNS = ["country", "customer_id", "transaction_id", "amount", "currency", "ext_ref", "trade_date"]


@pytest.fixture
def frames(spark):
    return (
        spark.createDataFrame(LEFT_ROWS, COLUMNS),
        spark.createDataFrame(RIGHT_ROWS, COLUMNS),
    )


def _leg(**overrides):
    payload = {
        "id": "leg1",
        "sources": [
            {"id": "source_a", "type": "inline", "inlineRows": [{"x": 1}]},
            {"id": "source_b", "type": "inline", "inlineRows": [{"x": 1}]},
        ],
        "keys": [
            {"left": "customer_id", "right": "customer_id", "alias": "customer_id",
             "normalization": {"trim": True, "stripLeadingZeros": True}},
            {"left": "transaction_id", "right": "transaction_id", "alias": "transaction_id"},
        ],
    }
    payload.update(overrides)
    return LegSpec.model_validate(payload)


class TestKeys:
    def test_normalisation_makes_padded_ids_match(self, spark, frames):
        left, right = frames
        leg = _leg()
        left_keyed = add_reconciliation_key(left, leg.keys, side="left", options=leg.matching)
        right_keyed = add_reconciliation_key(right, leg.keys, side="right", options=leg.matching)
        left_keys = {row[KEY_COLUMN] for row in left_keyed.select(KEY_COLUMN).collect()}
        right_keys = {row[KEY_COLUMN] for row in right_keyed.select(KEY_COLUMN).collect()}
        assert "1|T1001" in left_keys and "1|T1001" in right_keys

    def test_null_key_component_is_distinguishable_from_empty_string(self, spark):
        frame = spark.createDataFrame([(None, "a"), ("", "b")], "k string, v string")
        leg = LegSpec.model_validate(
            {
                "id": "leg",
                "sources": [
                    {"id": "a", "type": "inline", "inlineRows": [{"x": 1}]},
                    {"id": "b", "type": "inline", "inlineRows": [{"x": 1}]},
                ],
                "keys": [{"left": "k", "right": "k"}],
                "matching": {"nullEqualsNull": False},
            }
        )
        keyed = add_reconciliation_key(frame, leg.keys, side="left", options=leg.matching)
        values = [row[KEY_COLUMN] for row in keyed.select(KEY_COLUMN).collect()]
        assert "<NULL>" in values
        assert "" in values

    def test_key_description_reflects_normalisation(self):
        leg = _leg()
        description = describe_key(leg.keys, leg.matching)
        assert "STRIP_ZEROS" in description and "TRIM" in description


class TestClassification:
    def test_categories_are_assigned_correctly(self, spark, frames):
        left, right = frames
        leg = _leg(
            comparisons=[
                {"left": "amount", "right": "amount", "rule": "numeric_tolerance", "tolerance": 0.01},
                {"left": "currency", "right": "currency", "rule": "case_insensitive"},
            ]
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        categories = {
            row["recon_key"]: row["match_category"]
            for row in result.result.select("recon_key", "match_category").collect()
        }
        assert categories["1|T1001"] == "MATCHED"
        assert categories["2|T1002"] == "MATCHED"        # 0.01 is within tolerance
        assert categories["3|T1003"] == "MISMATCH"       # amount differs materially
        assert categories["4|T1004"] == "MISMATCH"       # currency differs
        assert categories["5|T1005"] == "LEFT_ONLY"
        assert categories["7|T1007"] == "RIGHT_ONLY"

    def test_metrics_are_consistent(self, spark, frames):
        left, right = frames
        leg = _leg(comparisons=[{"left": "amount", "right": "amount", "rule": "numeric_exact"}])
        metrics = ReconciliationEngine(spark).reconcile(leg, left, right).metrics
        assert metrics.left_records == 7
        assert metrics.right_records == 5
        assert metrics.left_only == 3       # T1005 plus the two duplicate T1006 rows
        assert metrics.right_only == 1
        assert metrics.duplicates_left == 2
        assert metrics.duplicate_keys == 1
        assert metrics.matched + metrics.unmatched > 0
        assert 0 <= metrics.match_percentage <= 100

    def test_duplicates_are_counted_even_when_one_sided(self, spark, frames):
        left, right = frames
        metrics = ReconciliationEngine(spark).reconcile(_leg(), left, right).metrics
        assert metrics.duplicates_left == 2
        assert metrics.duplicate_keys == 1

    def test_duplicate_on_both_sides_is_categorised(self, spark):
        columns = ["k", "amount"]
        left = spark.createDataFrame([("A", "1"), ("A", "1")], columns)
        right = spark.createDataFrame([("A", "1"), ("A", "1")], columns)
        leg = LegSpec.model_validate(
            {
                "id": "leg",
                "sources": [
                    {"id": "a", "type": "inline", "inlineRows": [{"x": 1}]},
                    {"id": "b", "type": "inline", "inlineRows": [{"x": 1}]},
                ],
                "keys": [{"left": "k", "right": "k"}],
                "comparisons": [{"left": "amount", "right": "amount"}],
            }
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        categories = {row["match_category"] for row in result.result.collect()}
        assert categories == {"DUPLICATE_BOTH"}

    def test_empty_right_side_yields_only_left_only(self, spark, frames):
        left, _ = frames
        empty = left.limit(0)
        result = ReconciliationEngine(spark).reconcile(_leg(), left, empty)
        assert result.metrics.left_only == 7
        assert result.metrics.matched == 0


class TestMatchingLogic:
    def test_or_rules_match_when_either_holds(self, spark, frames):
        left, right = frames
        leg = _leg(
            matchLogic={
                "operator": "OR",
                "rules": [
                    {
                        "id": "value_rule",
                        "name": "Values",
                        "operator": "AND",
                        "comparisons": [
                            {"left": "amount", "right": "amount", "rule": "numeric_tolerance",
                             "tolerance": 0.01},
                            {"left": "currency", "right": "currency", "rule": "case_insensitive"},
                        ],
                    },
                    {
                        "id": "reference_rule",
                        "name": "Reference",
                        "comparisons": [{"left": "ext_ref", "right": "ext_ref", "rule": "trimmed"}],
                    },
                ],
            }
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        categories = {
            row["recon_key"]: row["match_category"] for row in result.result.collect()
        }
        # T1003 fails on amount but its external reference agrees -> matched under OR.
        assert categories["3|T1003"] == "MATCHED"
        # T1004 fails both rules -> still a mismatch.
        assert categories["4|T1004"] == "MISMATCH"

    def test_and_rules_require_every_rule(self, spark, frames):
        left, right = frames
        leg = _leg(
            matchLogic={
                "operator": "AND",
                "rules": [
                    {
                        "id": "value_rule",
                        "name": "Values",
                        "comparisons": [
                            {"left": "amount", "right": "amount", "rule": "numeric_tolerance",
                             "tolerance": 0.01}
                        ],
                    },
                    {
                        "id": "reference_rule",
                        "name": "Reference",
                        "comparisons": [{"left": "ext_ref", "right": "ext_ref", "rule": "trimmed"}],
                    },
                ],
            }
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        categories = {row["recon_key"]: row["match_category"] for row in result.result.collect()}
        assert categories["3|T1003"] == "MISMATCH"
        assert categories["1|T1001"] == "MATCHED"

    def test_failed_rules_are_reported_per_row(self, spark, frames):
        left, right = frames
        leg = _leg(
            matchLogic={
                "operator": "OR",
                "rules": [
                    {"id": "amount_rule", "name": "Amount",
                     "comparisons": [{"left": "amount", "right": "amount", "rule": "numeric_exact"}]},
                    {"id": "ref_rule", "name": "Reference",
                     "comparisons": [{"left": "ext_ref", "right": "ext_ref", "rule": "trimmed"}]},
                ],
            }
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        row = next(r for r in result.result.collect() if r["recon_key"] == "3|T1003")
        assert "Amount" in row["failed_rules"]
        assert "Reference" in row["matched_rules"]
        assert "amount" in row["mismatched_fields"]

    def test_rule_metrics_are_produced(self, spark, frames):
        left, right = frames
        leg = _leg(
            matchLogic={
                "operator": "OR",
                "rules": [
                    {"id": "r1", "name": "R1",
                     "comparisons": [{"left": "amount", "right": "amount", "rule": "numeric_exact"}]},
                ],
            }
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        assert result.rule_metrics[0]["ruleName"] == "R1"
        assert result.rule_metrics[0]["passed"] + result.rule_metrics[0]["failed"] > 0

    def test_negated_rule_inverts_the_outcome(self, spark):
        columns = ["k", "v"]
        left = spark.createDataFrame([("A", "1")], columns)
        right = spark.createDataFrame([("A", "1")], columns)
        leg = LegSpec.model_validate(
            {
                "id": "leg",
                "sources": [
                    {"id": "a", "type": "inline", "inlineRows": [{"x": 1}]},
                    {"id": "b", "type": "inline", "inlineRows": [{"x": 1}]},
                ],
                "keys": [{"left": "k", "right": "k"}],
                "matchLogic": {
                    "rules": [
                        {"id": "r", "name": "R", "negate": True,
                         "comparisons": [{"left": "v", "right": "v", "rule": "exact"}]}
                    ]
                },
            }
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        assert result.result.collect()[0]["match_category"] == "MISMATCH"


class TestComparisonRules:
    @pytest.mark.parametrize(
        "rule,left_value,right_value,tolerance,expected",
        [
            ("exact", "abc", "abc", None, "MATCHED"),
            ("exact", "abc", "ABC", None, "MISMATCH"),
            ("case_insensitive", " abc ", "ABC", None, "MATCHED"),
            ("trimmed", " abc ", "abc", None, "MATCHED"),
            ("numeric_tolerance", "100.00", "100.005", 0.01, "MATCHED"),
            ("numeric_tolerance", "100.00", "100.50", 0.01, "MISMATCH"),
            ("percentage_tolerance", "100.00", "100.90", 1.0, "MATCHED"),
            ("percentage_tolerance", "100.00", "102.00", 1.0, "MISMATCH"),
            ("numeric_exact", "100.0", "100.00", None, "MATCHED"),
            ("contains", "REF", "XREFX", None, "MATCHED"),
            ("always_match", "a", "b", None, "MATCHED"),
        ],
    )
    def test_rules(self, spark, rule, left_value, right_value, tolerance, expected):
        left = spark.createDataFrame([("K1", left_value)], ["k", "v"])
        right = spark.createDataFrame([("K1", right_value)], ["k", "v"])
        comparison = {"left": "v", "right": "v", "rule": rule}
        if tolerance is not None:
            comparison["tolerance"] = tolerance
        leg = LegSpec.model_validate(
            {
                "id": "leg",
                "sources": [
                    {"id": "a", "type": "inline", "inlineRows": [{"x": 1}]},
                    {"id": "b", "type": "inline", "inlineRows": [{"x": 1}]},
                ],
                "keys": [{"left": "k", "right": "k"}],
                "comparisons": [comparison],
            }
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        assert result.result.collect()[0]["match_category"] == expected

    def test_null_equals_null_by_default(self, spark):
        schema = "k string, v string"
        left = spark.createDataFrame([("K1", None)], schema)
        right = spark.createDataFrame([("K1", None)], schema)
        leg = LegSpec.model_validate(
            {
                "id": "leg",
                "sources": [
                    {"id": "a", "type": "inline", "inlineRows": [{"x": 1}]},
                    {"id": "b", "type": "inline", "inlineRows": [{"x": 1}]},
                ],
                "keys": [{"left": "k", "right": "k"}],
                "comparisons": [{"left": "v", "right": "v", "rule": "exact"}],
            }
        )
        assert ReconciliationEngine(spark).reconcile(leg, left, right).result.collect()[0][
            "match_category"
        ] == "MATCHED"

    def test_null_versus_value_never_matches(self, spark):
        left = spark.createDataFrame([("K1", None)], "k string, v string")
        right = spark.createDataFrame([("K1", "x")], "k string, v string")
        leg = LegSpec.model_validate(
            {
                "id": "leg",
                "sources": [
                    {"id": "a", "type": "inline", "inlineRows": [{"x": 1}]},
                    {"id": "b", "type": "inline", "inlineRows": [{"x": 1}]},
                ],
                "keys": [{"left": "k", "right": "k"}],
                "comparisons": [{"left": "v", "right": "v", "rule": "exact"}],
            }
        )
        assert ReconciliationEngine(spark).reconcile(leg, left, right).result.collect()[0][
            "match_category"
        ] == "MISMATCH"

    def test_custom_expression_with_side_aliases(self, spark):
        left = spark.createDataFrame([("K1", "100.00")], ["k", "amount"])
        right = spark.createDataFrame([("K1", "100.005")], ["k", "amount"])
        leg = LegSpec.model_validate(
            {
                "id": "leg",
                "sources": [
                    {"id": "source_a", "type": "inline", "inlineRows": [{"x": 1}]},
                    {"id": "source_b", "type": "inline", "inlineRows": [{"x": 1}]},
                ],
                "keys": [{"left": "k", "right": "k"}],
                "comparisons": [
                    {
                        "left": "amount",
                        "right": "amount",
                        "rule": "expression",
                        "expression": "ABS(left.amount - right.amount) <= 0.01",
                    }
                ],
            }
        )
        assert ReconciliationEngine(spark).reconcile(leg, left, right).result.collect()[0][
            "match_category"
        ] == "MATCHED"

    def test_expression_translation(self):
        assert (
            translate_expression("ABS(left.amount - right.amount) <= 0.01", "source_a", "source_b")
            == "ABS(l__amount - r__amount) <= 0.01"
        )
        assert (
            translate_expression("source_a.x = source_b.y", "source_a", "source_b") == "l__x = r__y"
        )

    def test_comparison_descriptions(self):
        from reconx.config.models import FieldComparison

        comparison = FieldComparison.model_validate(
            {"left": "amount", "right": "amount", "rule": "numeric_tolerance", "tolerance": 0.01}
        )
        assert describe_comparison(comparison) == "ABS(amount - amount) <= 0.01"


class TestExceptions:
    def test_exceptions_carry_field_detail_and_context(self, spark, frames):
        left, right = frames
        leg = _leg(
            comparisons=[
                {"left": "amount", "right": "amount", "rule": "numeric_exact"},
                {"left": "currency", "right": "currency", "rule": "exact"},
            ],
            exceptionColumns=[
                "trade_date",
                {"alias": "country", "left": "country", "right": "country"},
                {"alias": "both_currency", "left": "currency", "right": "currency", "source": "both"},
            ],
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        rows = result.exceptions.collect()
        assert rows, "expected exception records"

        mismatches = [r for r in rows if r["exception_type"] == "MISMATCH"]
        assert mismatches
        for row in mismatches:
            assert row["field"] is not None
            assert row["context_columns"]["trade_date"] == "2026-09-10"
            assert row["context_columns"]["country"] in ("US", "UK")

        left_only = [r for r in rows if r["exception_type"] == "LEFT_ONLY"]
        assert left_only and left_only[0]["source"] == "source_a"
        # 'both' mode shows the two sides side by side; for a one-sided record the
        # missing side is blank rather than absent.
        assert "|" in left_only[0]["context_columns"]["both_currency"]

    def test_exception_key_components_are_named(self, spark, frames):
        left, right = frames
        result = ReconciliationEngine(spark).reconcile(_leg(), left, right)
        row = result.exceptions.collect()[0]
        assert set(row["key_components"].keys()) == {"customer_id", "transaction_id"}

    def test_exception_cap_is_respected(self, spark, frames):
        left, right = frames
        result = ReconciliationEngine(spark).reconcile(_leg(), left, right, max_exception_records=2)
        assert result.exceptions.count() == 2


class TestAggregates:
    def test_scalar_aggregate_break_is_detected(self, spark, frames):
        left, right = frames
        leg = _leg(
            aggregates=[
                {"name": "total", "function": "SUM", "leftField": "amount", "rightField": "amount",
                 "tolerance": 0.01}
            ]
        )
        result = ReconciliationEngine(spark).reconcile(leg, left, right)
        aggregate = result.aggregate_results[0]
        assert aggregate["matched"] is False
        assert aggregate["difference"] > 0

    def test_count_aggregate(self, spark, frames):
        left, right = frames
        leg = _leg(aggregates=[{"name": "rows", "function": "COUNT"}])
        aggregate = ReconciliationEngine(spark).reconcile(leg, left, right).aggregate_results[0]
        assert aggregate["leftValue"] == 7
        assert aggregate["rightValue"] == 5

    def test_grouped_aggregate_reports_breaking_groups(self, spark, frames):
        left, right = frames
        leg = _leg(
            aggregates=[
                {
                    "name": "by_country",
                    "function": "SUM",
                    "leftField": "amount",
                    "rightField": "amount",
                    "groupBy": [{"left": "country", "right": "country"}],
                    "tolerance": 0.01,
                }
            ]
        )
        aggregate = ReconciliationEngine(spark).reconcile(leg, left, right).aggregate_results[0]
        assert aggregate["groups"] >= 2
        assert aggregate["breakCount"] >= 1
