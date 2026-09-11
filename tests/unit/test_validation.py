"""DAG validation, cycle detection and SQL safety checks."""

from __future__ import annotations

import pytest

from reconx.common.errors import CyclicDependencyError, ValidationError
from reconx.config.models import ReconciliationDefinition
from reconx.config.validation import (
    build_dependency_graph,
    detect_cycles,
    topological_stages,
    validate_definition,
)
from reconx.security.sql_guard import (
    assert_read_only,
    assert_safe_expression,
    assert_table_name,
    quote_literal,
)

pytestmark = pytest.mark.unit


class TestDag:
    def test_stages_group_parallelisable_legs(self):
        graph = {"a": set(), "b": set(), "c": {"a", "b"}, "d": {"c"}}
        assert topological_stages(graph) == [["a", "b"], ["c"], ["d"]]

    def test_direct_cycle_is_detected(self):
        assert detect_cycles({"a": {"b"}, "b": {"a"}})

    def test_transitive_cycle_is_detected(self):
        cycles = detect_cycles({"a": {"b"}, "b": {"c"}, "c": {"a"}})
        assert cycles and len(cycles[0]) == 4

    def test_topological_sort_raises_on_a_cycle(self):
        with pytest.raises(CyclicDependencyError):
            topological_stages({"a": {"b"}, "b": {"a"}})

    def test_self_dependency_is_a_cycle(self):
        assert detect_cycles({"a": {"a"}})

    def test_graph_is_built_from_leg_dependencies(self, sample_definition):
        definition = ReconciliationDefinition.model_validate(sample_definition)
        assert build_dependency_graph(definition.legs) == {"transaction_leg": set()}


class TestDefinitionValidation:
    def test_valid_definition_passes(self, sample_definition):
        definition = ReconciliationDefinition.model_validate(sample_definition)
        report = validate_definition(definition, available_connections={"local_files": "filesystem"})
        assert report.valid, [issue.message for issue in report.errors]

    def test_unknown_connection_is_an_error(self, sample_definition):
        definition = ReconciliationDefinition.model_validate(sample_definition)
        report = validate_definition(definition, available_connections={})
        assert not report.valid
        assert any("does not exist" in issue.message for issue in report.errors)

    def test_connection_type_mismatch_is_an_error(self, sample_definition):
        definition = ReconciliationDefinition.model_validate(sample_definition)
        report = validate_definition(definition, available_connections={"local_files": "kafka"})
        assert any("cannot use a 'kafka' connection" in issue.message for issue in report.errors)

    def test_cyclic_legs_are_reported_not_raised(self):
        definition = ReconciliationDefinition.model_validate(
            {
                "reconId": "cyclic_recon",
                "name": "Cyclic",
                "legs": [
                    {
                        "id": "one",
                        "sources": [
                            {"id": "x", "type": "leg_output", "legRef": "two"},
                            {"id": "y", "type": "filesystem", "path": "/y"},
                        ],
                        "keys": [{"left": "id", "right": "id"}],
                    },
                    {
                        "id": "two",
                        "sources": [
                            {"id": "z", "type": "leg_output", "legRef": "one"},
                            {"id": "w", "type": "filesystem", "path": "/w"},
                        ],
                        "keys": [{"left": "id", "right": "id"}],
                    },
                ],
            }
        )
        report = validate_definition(definition)
        assert not report.valid
        assert any("Cyclic leg dependency" in issue.message for issue in report.errors)

    def test_dangerous_sql_in_a_source_query_is_rejected(self):
        definition = ReconciliationDefinition.model_validate(
            {
                "reconId": "sql_recon",
                "name": "SQL",
                "legs": [
                    {
                        "id": "leg",
                        "sources": [
                            {
                                "id": "a",
                                "type": "jdbc",
                                "connectionRef": "db",
                                "query": "SELECT * FROM t; DROP TABLE t",
                            },
                            {"id": "b", "type": "jdbc", "connectionRef": "db", "table": "t2"},
                        ],
                        "keys": [{"left": "id", "right": "id"}],
                    }
                ],
            }
        )
        report = validate_definition(definition, available_connections={"db": "jdbc"})
        assert not report.valid
        assert any("multiple SQL statements" in issue.message for issue in report.errors)

    def test_missing_tolerance_is_reported(self, sample_definition):
        sample_definition["legs"][0]["matchLogic"]["rules"][0]["comparisons"][0].pop("tolerance")
        definition = ReconciliationDefinition.model_validate(sample_definition)
        report = validate_definition(definition, available_connections={"local_files": "filesystem"})
        assert any("requires 'tolerance'" in issue.message for issue in report.errors)

    def test_execution_order_is_reported(self):
        definition = ReconciliationDefinition.model_validate(
            {
                "reconId": "multi_leg",
                "name": "Multi",
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
        report = validate_definition(definition)
        assert report.execution_order == [["first"], ["second"]]


class TestSqlGuard:
    @pytest.mark.parametrize(
        "statement",
        [
            "SELECT * FROM transactions",
            "WITH cte AS (SELECT 1 AS x) SELECT * FROM cte",
            "SELECT TOP (100) t.[Amount] FROM [dbo].[Transactions] AS t WITH (NOLOCK)",
            "SELECT * FROM t FETCH FIRST 10 ROWS ONLY",
            "select count(*) from t where d = '2026-09-10' -- trailing comment",
        ],
    )
    def test_read_only_statements_are_allowed(self, statement):
        assert assert_read_only(statement) == statement

    @pytest.mark.parametrize(
        "statement",
        [
            "DROP TABLE transactions",
            "SELECT 1; DELETE FROM t",
            "INSERT INTO t VALUES (1)",
            "UPDATE t SET x = 1",
            "SELECT java_method('java.lang.Runtime', 'getRuntime')",
            "SELECT * INTO OUTFILE '/tmp/x' FROM t",
            "EXEC xp_cmdshell 'dir'",
            "TRUNCATE TABLE t",
            "",
        ],
    )
    def test_dangerous_statements_are_rejected(self, statement):
        with pytest.raises(ValidationError):
            assert_read_only(statement)

    @pytest.mark.parametrize(
        "name",
        ["transactions", "dbo.Transactions", "[dbo].[Transactions]", '"schema"."table"', "`db`.`tbl`"],
    )
    def test_valid_table_names(self, name):
        assert assert_table_name(name)

    @pytest.mark.parametrize("name", ["t; DROP TABLE x", "t--c", "EXEC sp_who", "a b", ""])
    def test_invalid_table_names(self, name):
        with pytest.raises(ValidationError):
            assert_table_name(name)

    def test_expressions_allow_arithmetic_but_not_ddl(self):
        assert assert_safe_expression("ABS(left.amount - right.amount) <= 0.01")
        with pytest.raises(ValidationError):
            assert_safe_expression("1=1; DROP TABLE t")

    def test_literals_are_escaped(self):
        assert quote_literal("O'Brien") == "'O''Brien'"
