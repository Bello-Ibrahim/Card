"""Temporary view / previous-leg-output connector.

These sources do not touch an external system: they resolve a Spark temporary
view registered earlier in the same job (by a transformation, a source, or a
previous leg's result).  This is what makes multi-leg reconciliation work
without round-tripping results through storage.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from reconx.common.errors import ConfigurationError
from reconx.common.logging import get_logger
from reconx.config.enums import SourceType
from reconx.connectors.base import (
    ConnectionTestResult,
    DataSourceConnector,
    OutputContext,
    SourceContext,
    register_connector,
)
from reconx.security.sql_guard import assert_identifier

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)


@register_connector
class TempViewConnector(DataSourceConnector):
    source_types = (SourceType.TEMP_VIEW, SourceType.LEG_OUTPUT, SourceType.INLINE)
    display_name = "Spark temporary view / previous leg output"

    def read(self, config: SourceContext, spark: SparkSession) -> DataFrame:
        source = config.source
        if source.type == SourceType.INLINE:
            log.info("inline.read", source=source.id, rows=len(source.inline_rows))
            return spark.createDataFrame(source.inline_rows)
        view = source.view or _leg_view_name(source.leg_ref, source.leg_output_ref)
        assert_identifier(view, context=f"source.{source.id}.view")
        existing = {t.name for t in spark.catalog.listTables()}
        if view not in existing:
            raise ConfigurationError(
                f"Temporary view '{view}' does not exist",
                details={
                    "source": source.id,
                    "availableViews": sorted(existing),
                    "hint": "Check leg execution order - a producing leg must run first",
                },
            )
        log.info("temp_view.read", view=view, source=source.id)
        return spark.table(view)

    def write(self, dataframe: DataFrame, config: OutputContext) -> dict[str, Any]:
        view = config.output.view or ""
        assert_identifier(view, context="output.view")
        dataframe.createOrReplaceTempView(view)
        log.info("temp_view.write", view=view)
        return {"target": view, "type": "temp_view"}

    def test_connection(self, config: dict[str, Any]) -> ConnectionTestResult:
        return ConnectionTestResult(True, "Temporary views are in-job resources - nothing to test")

    def validate(self, config: dict[str, Any]) -> list[str]:
        return []


def _leg_view_name(leg_ref: str | None, output_ref: str | None = None) -> str:
    if not leg_ref:
        raise ConfigurationError("leg_output source requires 'legRef'")
    return f"{leg_ref}__{output_ref}" if output_ref else f"{leg_ref}__result"


def leg_result_view(leg_id: str, output_id: str | None = None) -> str:
    return _leg_view_name(leg_id, output_id)
