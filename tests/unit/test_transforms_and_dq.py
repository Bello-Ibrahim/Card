"""Transformation engine, schema handling and data-quality checks."""

from __future__ import annotations

import pytest

from reconx.common.errors import DataQualityError, TransformationError, ValidationError
from reconx.config.models import DataQualityCheck, SchemaSpec, Transformation
from reconx.spark.dq import DataQualityRunner
from reconx.spark.schema import apply_schema, build_struct_type, compare_schemas, normalise_type
from reconx.spark.transforms import TransformationEngine

pytestmark = [pytest.mark.unit, pytest.mark.spark]


@pytest.fixture
def frame(spark):
    return spark.createDataFrame(
        [
            ("A", " x ", "100.5", "2026-09-10", "USD"),
            ("B", "y", "200.0", "2026-09-11", "usd"),
            ("C", "z", None, "2026-09-12", "GBP"),
            ("C", "z", None, "2026-09-12", "GBP"),
        ],
        "id string, name string, amount string, trade_date string, currency string",
    )


class TestTransformations:
    def test_select_and_drop(self, spark, frame):
        engine = TransformationEngine(spark)
        selected = engine.apply(frame, Transformation.model_validate({"type": "select", "columns": ["id", "name"]}))
        assert selected.columns == ["id", "name"]
        dropped = engine.apply(frame, Transformation.model_validate({"type": "drop", "columns": ["name"]}))
        assert "name" not in dropped.columns

    def test_rename_and_cast(self, spark, frame):
        engine = TransformationEngine(spark)
        renamed = engine.apply(
            frame, Transformation.model_validate({"type": "rename", "mapping": {"name": "label"}})
        )
        assert "label" in renamed.columns
        cast = engine.apply(
            frame, Transformation.model_validate({"type": "cast", "fields": {"amount": "double"}})
        )
        assert dict(cast.dtypes)["amount"] == "double"

    def test_filter_and_derive(self, spark, frame):
        engine = TransformationEngine(spark)
        filtered = engine.apply(
            frame, Transformation.model_validate({"type": "filter", "condition": "id = 'A'"})
        )
        assert filtered.count() == 1
        derived = engine.apply(
            frame,
            Transformation.model_validate(
                {"type": "derive", "fields": {"upper_name": "UPPER(TRIM(name))"}}
            ),
        )
        assert derived.select("upper_name").first()["upper_name"] == "X"

    def test_sql_transformation_uses_the_input_placeholder(self, spark, frame):
        engine = TransformationEngine(spark)
        result = engine.apply(
            frame,
            Transformation.model_validate(
                {"type": "sql", "sql": "SELECT id, amount FROM ${input} WHERE id <> 'C'"}
            ),
        )
        assert result.columns == ["id", "amount"]
        assert result.count() == 2

    def test_temp_view_registration_leaves_the_pipeline_unchanged(self, spark, frame):
        engine = TransformationEngine(spark)
        result = engine.apply(
            frame,
            Transformation.model_validate(
                {"type": "temp_view", "viewName": "filtered_view", "sql": "SELECT * FROM ${input} WHERE id = 'A'"}
            ),
        )
        assert result.count() == frame.count()
        assert spark.table("filtered_view").count() == 1

    def test_deduplicate_keeps_one_row_per_key(self, spark, frame):
        engine = TransformationEngine(spark)
        result = engine.apply(
            frame, Transformation.model_validate({"type": "deduplicate", "columns": ["id"]})
        )
        assert result.count() == 3

    def test_deduplicate_with_ordering(self, spark, frame):
        engine = TransformationEngine(spark)
        result = engine.apply(
            frame,
            Transformation.model_validate(
                {"type": "deduplicate", "columns": ["id"], "orderBy": ["trade_date"], "keep": "last"}
            ),
        )
        assert result.count() == 3

    def test_aggregate(self, spark, frame):
        engine = TransformationEngine(spark)
        result = engine.apply(
            frame,
            Transformation.model_validate(
                {"type": "aggregate", "groupBy": ["currency"], "aggregations": {"total": "SUM(amount)"}}
            ),
        )
        assert "total" in result.columns

    def test_normalize(self, spark, frame):
        engine = TransformationEngine(spark)
        result = engine.apply(
            frame,
            Transformation.model_validate(
                {
                    "type": "normalize",
                    "columns": ["currency"],
                    "normalization": {"trim": True, "case": "upper"},
                }
            ),
        )
        assert {row["currency"] for row in result.collect()} == {"USD", "GBP"}

    def test_fill_null(self, spark, frame):
        engine = TransformationEngine(spark)
        result = engine.apply(
            frame, Transformation.model_validate({"type": "fill_null", "fields": {"amount": "0"}})
        )
        assert result.filter("amount IS NULL").count() == 0

    def test_chained_transformations(self, spark, frame):
        engine = TransformationEngine(spark)
        result = engine.apply_all(
            frame,
            [
                Transformation.model_validate({"type": "filter", "condition": "amount IS NOT NULL"}),
                Transformation.model_validate({"type": "cast", "fields": {"amount": "double"}}),
                Transformation.model_validate({"type": "derive", "fields": {"doubled": "amount * 2"}}),
            ],
        )
        assert result.select("doubled").first()["doubled"] == 201.0

    def test_variables_are_rendered_into_transformations(self, spark, frame):
        engine = TransformationEngine(spark, variables={"target_date": "2026-09-10"})
        result = engine.apply(
            frame,
            Transformation.model_validate(
                {"type": "filter", "condition": "trade_date = '${target_date}'"}
            ),
        )
        assert result.count() == 1

    def test_unknown_column_raises_a_clear_error(self, spark, frame):
        engine = TransformationEngine(spark)
        with pytest.raises(TransformationError) as error:
            engine.apply(frame, Transformation.model_validate({"type": "select", "columns": ["nope"]}))
        assert "not found" in str(error.value)

    def test_dangerous_sql_is_blocked(self, spark, frame):
        engine = TransformationEngine(spark)
        with pytest.raises((ValidationError, TransformationError)):
            engine.apply(
                frame, Transformation.model_validate({"type": "sql", "sql": "DROP TABLE something"})
            )


class TestSchema:
    def test_type_aliases(self):
        assert normalise_type("int") == "integer"
        assert normalise_type("bigint") == "long"
        assert normalise_type("datetime") == "timestamp"

    def test_explicit_schema_casts_columns(self, spark, frame):
        spec = SchemaSpec.model_validate(
            {
                "mode": "explicit",
                "fields": [
                    {"name": "id", "type": "string"},
                    {"name": "amount", "type": "double"},
                ],
                "allowExtraColumns": True,
            }
        )
        result = apply_schema(frame, spec, source_id="s")
        assert dict(result.dtypes)["amount"] == "double"

    def test_validate_mode_reports_missing_columns(self, spark, frame):
        from reconx.common.errors import SchemaMismatchError

        spec = SchemaSpec.model_validate(
            {"mode": "validate", "fields": [{"name": "missing_column", "type": "string"}]}
        )
        with pytest.raises(SchemaMismatchError):
            apply_schema(frame, spec, source_id="s")

    def test_evolve_mode_adds_missing_columns_as_nulls(self, spark, frame):
        spec = SchemaSpec.model_validate(
            {
                "mode": "evolve",
                "fields": [{"name": "id", "type": "string"}, {"name": "new_field", "type": "string"}],
                "allowExtraColumns": True,
            }
        )
        result = apply_schema(frame, spec, source_id="s")
        assert "new_field" in result.columns
        assert result.filter("new_field IS NOT NULL").count() == 0

    def test_struct_type_construction(self):
        spec = SchemaSpec.model_validate(
            {"mode": "explicit", "fields": [{"name": "a", "type": "decimal(18,2)"}]}
        )
        assert build_struct_type(spec).fields[0].dataType.simpleString() == "decimal(18,2)"

    def test_compare_schemas_reports_differences(self, spark, frame):
        spec = SchemaSpec.model_validate(
            {
                "mode": "validate",
                "fields": [{"name": "id", "type": "string"}, {"name": "amount", "type": "double"}],
            }
        )
        comparison = compare_schemas(spec, frame)
        assert comparison["compatible"] is False
        assert "amount" in comparison["typeMismatches"]


class TestDataQuality:
    def test_not_null_failure_stops_the_run(self, spark, frame):
        report = DataQualityRunner().run(
            frame,
            [DataQualityCheck.model_validate({"type": "not_null", "columns": ["amount"]})],
            source_id="s",
        )
        assert not report.passed
        assert report.blocking_failures
        with pytest.raises(DataQualityError):
            report.raise_if_blocking()

    def test_threshold_tolerates_a_few_failures(self, spark, frame):
        report = DataQualityRunner().run(
            frame,
            [DataQualityCheck.model_validate({"type": "not_null", "columns": ["amount"], "threshold": 0.75})],
            source_id="s",
        )
        assert report.passed

    def test_continue_with_warning_is_not_blocking(self, spark, frame):
        report = DataQualityRunner().run(
            frame,
            [
                DataQualityCheck.model_validate(
                    {"type": "not_null", "columns": ["amount"], "onFailure": "CONTINUE_WITH_WARNING"}
                )
            ],
            source_id="s",
        )
        assert not report.passed
        assert not report.blocking_failures
        assert report.warnings
        report.raise_if_blocking()  # does not raise

    def test_row_count_bounds(self, spark, frame):
        report = DataQualityRunner().run(
            frame, [DataQualityCheck.model_validate({"type": "row_count", "minRows": 10})], source_id="s"
        )
        assert not report.passed

    def test_unique_detects_duplicates(self, spark, frame):
        report = DataQualityRunner().run(
            frame, [DataQualityCheck.model_validate({"type": "unique", "columns": ["id"]})], source_id="s"
        )
        assert not report.passed
        assert report.results[0].failed_records == 1

    def test_column_exists(self, spark, frame):
        report = DataQualityRunner().run(
            frame,
            [DataQualityCheck.model_validate({"type": "column_exists", "columns": ["id", "ghost"]})],
            source_id="s",
        )
        assert not report.passed
        assert "ghost" in report.results[0].details["missing"]

    def test_custom_sql_check(self, spark, frame):
        report = DataQualityRunner().run(
            frame,
            [DataQualityCheck.model_validate({"type": "custom_sql", "sql": "id IS NOT NULL"})],
            source_id="s",
        )
        assert report.passed

    def test_regex_check(self, spark, frame):
        report = DataQualityRunner().run(
            frame,
            [
                DataQualityCheck.model_validate(
                    {"type": "regex", "columns": ["trade_date"], "pattern": r"^\d{4}-\d{2}-\d{2}$"}
                )
            ],
            source_id="s",
        )
        assert report.passed

    def test_multiple_checks_run_in_one_pass(self, spark, frame):
        report = DataQualityRunner().run(
            frame,
            [
                DataQualityCheck.model_validate({"type": "not_null", "columns": ["id"]}),
                DataQualityCheck.model_validate({"type": "row_count", "minRows": 1}),
                DataQualityCheck.model_validate({"type": "column_exists", "columns": ["currency"]}),
            ],
            source_id="s",
        )
        assert report.passed
        assert len(report.results) == 3
