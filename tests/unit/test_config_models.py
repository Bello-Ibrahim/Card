"""Configuration model semantics."""

from __future__ import annotations

import pytest
from pydantic import ValidationError as PydanticValidationError

from reconx.config.enums import ComparisonRule, LogicalOperator
from reconx.config.models import (
    ExceptionColumn,
    LegSpec,
    MatchLogic,
    ReconciliationDefinition,
    declared_variable_defaults,
)

pytestmark = pytest.mark.unit


def _leg(**overrides):
    payload = {
        "id": "leg1",
        "sources": [
            {"id": "source_a", "type": "filesystem", "path": "/a.csv", "format": "csv"},
            {"id": "source_b", "type": "filesystem", "path": "/b.csv", "format": "csv"},
        ],
        "keys": [{"left": "id", "right": "id"}],
    }
    payload.update(overrides)
    return LegSpec.model_validate(payload)


class TestKeyShorthand:
    def test_source_named_shorthand_resolves(self):
        leg = _leg(keys=[{"source_a": "customer_id", "source_b": "cust_id"}])
        assert leg.keys[0].left == "customer_id"
        assert leg.keys[0].right == "cust_id"

    def test_single_value_shorthand_applies_to_both_sides(self):
        leg = _leg(keys=[{"source_a": "customer_id"}])
        assert leg.keys[0].left == leg.keys[0].right == "customer_id"

    def test_missing_key_on_two_sided_leg_is_rejected(self):
        with pytest.raises(PydanticValidationError):
            _leg(keys=[])


class TestComparisonShorthand:
    def test_source_target_field_aliases(self):
        leg = _leg(
            comparisons=[
                {"sourceField": "amount", "targetField": "amount", "comparison": "numeric_tolerance",
                 "tolerance": 0.01}
            ]
        )
        comparison = leg.comparisons[0]
        assert comparison.left == "amount"
        assert comparison.rule == ComparisonRule.NUMERIC_TOLERANCE
        assert comparison.tolerance == 0.01


class TestMatchLogic:
    def test_simple_comparisons_are_promoted_to_a_single_and_rule(self):
        leg = _leg(comparisons=[{"left": "amount", "right": "amount"}])
        logic = leg.effective_match_logic()
        assert logic is not None
        assert logic.operator == LogicalOperator.AND
        assert len(logic.rules) == 1
        assert logic.rules[0].id == "default_rule"

    def test_multiple_rules_combine_with_the_chosen_operator(self):
        leg = _leg(
            matchLogic={
                "operator": "OR",
                "rules": [
                    {"id": "a", "name": "Amounts", "comparisons": [{"left": "amount", "right": "amount"}]},
                    {"id": "b", "name": "Reference", "comparisons": [{"left": "ref", "right": "ref"}]},
                ],
            }
        )
        logic = leg.effective_match_logic()
        assert logic.describe() == "(Amounts OR Reference)"
        assert len(leg.all_comparisons()) == 2

    def test_nested_groups_and_negation(self):
        logic = MatchLogic.model_validate(
            {
                "operator": "AND",
                "rules": [{"id": "a", "name": "A", "comparisons": [{"left": "x", "right": "x"}]}],
                "groups": [
                    {
                        "operator": "OR",
                        "negate": True,
                        "rules": [
                            {"id": "b", "name": "B", "comparisons": [{"left": "y", "right": "y"}]},
                            {"id": "c", "name": "C", "comparisons": [{"left": "z", "right": "z"}]},
                        ],
                    }
                ],
            }
        )
        assert logic.describe() == "(A AND NOT (B OR C))"
        assert len(logic.all_rules()) == 3

    def test_duplicate_rule_ids_are_rejected(self):
        with pytest.raises(PydanticValidationError):
            MatchLogic.model_validate(
                {
                    "rules": [
                        {"id": "same", "comparisons": [{"left": "x", "right": "x"}]},
                        {"id": "same", "comparisons": [{"left": "y", "right": "y"}]},
                    ]
                }
            )

    def test_empty_match_logic_is_rejected(self):
        with pytest.raises(PydanticValidationError):
            MatchLogic.model_validate({"operator": "AND"})


class TestExceptionColumns:
    def test_string_shorthand(self):
        column = ExceptionColumn.model_validate("trade_date")
        assert column.alias == column.left == column.right == "trade_date"
        assert column.source == "coalesce"

    def test_column_key_shorthand(self):
        column = ExceptionColumn.model_validate({"column": "account_no"})
        assert column.alias == "account_no"
        assert column.left == "account_no"

    def test_side_specific_column(self):
        column = ExceptionColumn.model_validate({"alias": "status", "right": "status", "source": "right"})
        assert column.left is None
        assert column.source == "right"

    def test_source_left_without_left_column_is_rejected(self):
        with pytest.raises(PydanticValidationError):
            ExceptionColumn.model_validate({"alias": "x", "right": "y", "source": "left"})


class TestSourceValidation:
    def test_jdbc_source_requires_table_or_query(self):
        with pytest.raises(PydanticValidationError):
            LegSpec.model_validate(
                {
                    "id": "leg",
                    "sources": [{"id": "a", "type": "jdbc", "connectionRef": "db"}],
                }
            )

    def test_mssql_dialect_and_variables_are_preserved(self):
        leg = LegSpec.model_validate(
            {
                "id": "leg",
                "sources": [
                    {
                        "id": "a",
                        "type": "jdbc",
                        "connectionRef": "db",
                        "dialect": "mssql",
                        "query": "SELECT TOP (10) * FROM ${tbl} WHERE d = '${business_date}'",
                    },
                    {"id": "b", "type": "jdbc", "connectionRef": "db", "table": "[dbo].[Ledger]"},
                ],
                "keys": [{"left": "id", "right": "id"}],
            }
        )
        assert leg.sources[0].dialect == "mssql"
        assert "${tbl}" in leg.sources[0].query
        assert leg.sources[1].table == "[dbo].[Ledger]"

    def test_reserved_source_id_prefix_is_rejected(self):
        with pytest.raises(PydanticValidationError):
            LegSpec.model_validate(
                {
                    "id": "leg",
                    "sources": [{"id": "__reconx_x", "type": "filesystem", "path": "/a"}],
                }
            )


class TestDefinition:
    def test_variable_defaults_are_overridden_by_parameters(self, sample_definition):
        definition = ReconciliationDefinition.model_validate(sample_definition)
        definition = definition.model_copy(update={"parameters": {"business_unit": "RETAIL"}})
        assert declared_variable_defaults(definition) == {
            "ledger_table": "ledger",
            "business_unit": "RETAIL",
        }

    def test_leg_output_source_creates_an_implicit_dependency(self):
        definition = ReconciliationDefinition.model_validate(
            {
                "reconId": "recon_dag",
                "name": "R",
                "legs": [
                    {
                        "id": "first",
                        "sources": [
                            {"id": "a", "type": "filesystem", "path": "/a"},
                            {"id": "b", "type": "filesystem", "path": "/b"},
                        ],
                        "keys": [{"left": "id", "right": "id"}],
                    },
                    {
                        "id": "second",
                        "sources": [
                            {"id": "prev", "type": "leg_output", "legRef": "first"},
                            {"id": "c", "type": "filesystem", "path": "/c"},
                        ],
                        "keys": [{"left": "id", "right": "id"}],
                    },
                ],
            }
        )
        assert definition.legs[1].depends_on == ["first"]

    def test_connection_refs_are_collected(self, sample_definition):
        definition = ReconciliationDefinition.model_validate(sample_definition)
        assert definition.connection_refs() == {"local_files"}

    def test_invalid_cron_is_rejected(self, sample_definition):
        sample_definition["schedule"]["expression"] = "not a cron"
        with pytest.raises(PydanticValidationError):
            ReconciliationDefinition.model_validate(sample_definition)
