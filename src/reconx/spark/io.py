"""Source reading and result writing.

``SourceReader`` turns a :class:`~reconx.config.models.SourceSpec` into a
validated, transformed DataFrame: resolve connection -> resolve secrets ->
render ``${variables}`` -> connector read -> schema -> transformations ->
data-quality.  ``ResultWriter`` does the reverse for outputs.
"""

from __future__ import annotations

import re
import time
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Protocol

from reconx.common.errors import ConfigurationError, NotFoundError
from reconx.common.logging import get_logger
from reconx.common.retry import RetryPolicy, call_with_retry
from reconx.common.templating import render_deep
from reconx.config.connections import SECRET_FIELDS, ConnectionDefinition
from reconx.config.enums import MatchCategory, OutputType, SourceType
from reconx.config.models import OutputSpec, SourceSpec
from reconx.connectors import OutputContext, SourceContext, get_connector
from reconx.security.secrets import SecretResolver, get_secret_resolver
from reconx.spark.dq import DataQualityReport, DataQualityRunner
from reconx.spark.schema import apply_schema
from reconx.spark.transforms import TransformationEngine

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)


class ConnectionProvider(Protocol):
    """Anything that can hand back a connection definition by id."""

    def get(self, connection_id: str) -> ConnectionDefinition: ...


@dataclass
class StaticConnectionProvider:
    """In-memory provider (tests, CLI runs with a YAML bundle)."""

    connections: dict[str, ConnectionDefinition] = field(default_factory=dict)

    def get(self, connection_id: str) -> ConnectionDefinition:
        if connection_id not in self.connections:
            raise NotFoundError(f"Connection '{connection_id}' not found")
        return self.connections[connection_id]


@dataclass
class ReadResult:
    source_id: str
    dataframe: DataFrame
    row_count: int | None
    read_time_ms: int
    data_quality: DataQualityReport | None = None
    schema_fields: list[dict[str, Any]] = field(default_factory=list)


class SourceReader:
    """Reads and prepares one source."""

    def __init__(
        self,
        spark: SparkSession,
        connections: ConnectionProvider,
        *,
        variables: dict[str, Any] | None = None,
        secret_resolver: SecretResolver | None = None,
        staging_dir: str = "/tmp/reconx-staging",  # noqa: S108
        retry_policy: RetryPolicy | None = None,
        run_id: str | None = None,
        recon_id: str | None = None,
    ) -> None:
        self.spark = spark
        self.connections = connections
        self.variables = variables or {}
        self.secrets = secret_resolver or get_secret_resolver()
        self.staging_dir = staging_dir
        self.retry_policy = retry_policy or RetryPolicy()
        self.run_id = run_id
        self.recon_id = recon_id
        self.transformer = TransformationEngine(spark, self.variables)
        self.dq_runner = DataQualityRunner()

    def resolve_connection(self, connection_ref: str | None) -> tuple[ConnectionDefinition | None, dict[str, Any]]:
        if not connection_ref:
            return None, {}
        connection = self.connections.get(connection_ref)
        if not connection.enabled:
            raise ConfigurationError(f"Connection '{connection_ref}' is disabled")
        resolved = self.secrets.resolve_mapping(connection.config, SECRET_FIELDS)
        resolved = render_deep(resolved, self.variables, strict=False)
        return connection, resolved

    def read(self, source: SourceSpec, *, leg_id: str | None = None) -> ReadResult:
        started = time.time()
        rendered = SourceSpec.model_validate(
            render_deep(source.model_dump(by_alias=True), self.variables, strict=False)
        )
        _assert_variables_resolved(
            {"query": rendered.query, "table": rendered.table, "path": rendered.path,
             "topic": rendered.topic, "filter": rendered.filter},
            context=f"source '{rendered.id}'",
            available=self.variables,
        )
        connection, resolved_config = self.resolve_connection(rendered.connection_ref)
        context = SourceContext(
            source=rendered,
            connection=connection,
            resolved_config=resolved_config,
            variables=self.variables,
            run_id=self.run_id,
            recon_id=self.recon_id,
            leg_id=leg_id,
            staging_dir=self.staging_dir,
            retry_policy=self.retry_policy,
        )
        connector = get_connector(rendered.type)
        dataframe = call_with_retry(
            lambda: connector.read(context, self.spark),
            policy=self.retry_policy,
            operation=f"read.{rendered.type.value}.{rendered.id}",
        )

        dataframe = apply_schema(dataframe, rendered.schema_spec, source_id=rendered.id)

        if rendered.filter:
            from pyspark.sql import functions as F

            from reconx.security.sql_guard import assert_safe_expression

            assert_safe_expression(rendered.filter, context=f"source.{rendered.id}.filter")
            dataframe = dataframe.filter(F.expr(rendered.filter))

        if rendered.transformations:
            dataframe = self.transformer.apply_all(
                dataframe, rendered.transformations, context=f"source.{rendered.id}"
            )

        if rendered.repartition:
            dataframe = dataframe.repartition(rendered.repartition)
        if rendered.cache:
            dataframe = dataframe.cache()

        report: DataQualityReport | None = None
        if rendered.data_quality:
            report = self.dq_runner.run(
                dataframe,
                rendered.data_quality,
                source_id=rendered.id,
                schema_spec=rendered.schema_spec,
            )
            report.raise_if_blocking()

        if rendered.register_temp_view:
            dataframe.createOrReplaceTempView(rendered.register_temp_view)
            log.info("source.temp_view_registered", source=rendered.id, view=rendered.register_temp_view)

        elapsed = int((time.time() - started) * 1000)
        row_count = None
        if rendered.cache or rendered.type in (SourceType.INLINE,):
            row_count = dataframe.count()

        log.info(
            "source.read",
            source=rendered.id,
            type=rendered.type.value,
            leg_id=leg_id,
            read_time_ms=elapsed,
            columns=len(dataframe.columns),
        )
        return ReadResult(
            source_id=rendered.id,
            dataframe=dataframe,
            row_count=row_count,
            read_time_ms=elapsed,
            data_quality=report,
            schema_fields=[
                {"name": f.name, "type": f.dataType.simpleString(), "nullable": f.nullable}
                for f in dataframe.schema.fields
            ],
        )


class ResultWriter:
    """Writes leg results / exceptions to the configured outputs."""

    def __init__(
        self,
        connections: ConnectionProvider,
        *,
        variables: dict[str, Any] | None = None,
        secret_resolver: SecretResolver | None = None,
        staging_dir: str = "/tmp/reconx-staging",  # noqa: S108
        retry_policy: RetryPolicy | None = None,
        run_id: str | None = None,
        recon_id: str | None = None,
    ) -> None:
        self.connections = connections
        self.variables = variables or {}
        self.secrets = secret_resolver or get_secret_resolver()
        self.staging_dir = staging_dir
        self.retry_policy = retry_policy or RetryPolicy()
        self.run_id = run_id
        self.recon_id = recon_id

    def write(
        self,
        dataframe: DataFrame,
        output: OutputSpec,
        *,
        leg_id: str | None = None,
        add_run_columns: bool = True,
    ) -> dict[str, Any]:
        from pyspark.sql import functions as F

        if not output.enabled or output.type == OutputType.NONE:
            return {"skipped": True, "reason": "output disabled"}

        started = time.time()
        rendered = OutputSpec.model_validate(
            render_deep(output.model_dump(by_alias=True), self.variables, strict=False)
        )
        _assert_variables_resolved(
            {"path": rendered.path, "table": rendered.table, "topic": rendered.topic},
            context=f"output '{rendered.id or rendered.type.value}'",
            available=self.variables,
        )

        data = dataframe
        if rendered.categories:
            wanted = [c.value if isinstance(c, MatchCategory) else str(c) for c in rendered.categories]
            if "match_category" in data.columns:
                data = data.filter(F.col("match_category").isin(wanted))
        if rendered.columns:
            available = [c for c in rendered.columns if c in data.columns]
            data = data.select(*available)
        if add_run_columns:
            if "run_id" not in data.columns:
                data = data.withColumn("run_id", F.lit(self.run_id))
            if "recon_id" not in data.columns:
                data = data.withColumn("recon_id", F.lit(self.recon_id))
            if leg_id and "leg_id" not in data.columns:
                data = data.withColumn("leg_id", F.lit(leg_id))
            business_date = self.variables.get("business_date")
            if business_date and "business_date" not in data.columns:
                data = data.withColumn("business_date", F.lit(str(business_date)))
        # Complex types (arrays/maps) cannot be written over JDBC.
        if rendered.type == OutputType.JDBC:
            data = _flatten_complex_columns(data)

        connection = None
        resolved_config: dict[str, Any] = {}
        if rendered.connection_ref:
            connection = self.connections.get(rendered.connection_ref)
            resolved_config = self.secrets.resolve_mapping(connection.config, SECRET_FIELDS)
            resolved_config = render_deep(resolved_config, self.variables, strict=False)

        context = OutputContext(
            output=rendered,
            connection=connection,
            resolved_config=resolved_config,
            variables=self.variables,
            run_id=self.run_id,
            recon_id=self.recon_id,
            leg_id=leg_id,
            staging_dir=self.staging_dir,
            retry_policy=self.retry_policy,
        )
        connector = get_connector(_output_source_type(rendered.type))
        result = call_with_retry(
            lambda: connector.write(data, context),
            policy=self.retry_policy,
            operation=f"write.{rendered.type.value}",
        )
        elapsed = int((time.time() - started) * 1000)
        log.info(
            "output.written",
            output=rendered.id or rendered.type.value,
            type=rendered.type.value,
            leg_id=leg_id,
            write_time_ms=elapsed,
        )
        return {**result, "writeTimeMs": elapsed, "outputId": rendered.id, "type": rendered.type.value}


_UNRESOLVED_RE = re.compile(r"\$\{([a-zA-Z_][a-zA-Z0-9_]*)")


def _assert_variables_resolved(
    values: dict[str, Any], *, context: str, available: dict[str, Any]
) -> None:
    """Fail with a clear message rather than sending ``${var}`` to a database.

    Rendering is non-strict so partial configuration can be previewed, but by
    the time a statement or path is executed every variable must have a value -
    otherwise the failure surfaces as an opaque driver syntax error.
    """
    missing: dict[str, list[str]] = {}
    for field_name, value in values.items():
        if not isinstance(value, str):
            continue
        names = _UNRESOLVED_RE.findall(value)
        if names:
            missing[field_name] = sorted(set(names))
    if missing:
        raise ConfigurationError(
            f"{context}: unresolved variable(s) "
            + ", ".join(f"${{{name}}} in '{field}'" for field, names in missing.items() for name in names),
            details={
                "unresolved": missing,
                "availableVariables": sorted(available.keys()),
                "hint": "Declare the variable on the reconciliation, or pass it as a run parameter",
            },
        )


def _output_source_type(output_type: OutputType) -> SourceType:
    mapping = {
        OutputType.JDBC: SourceType.JDBC,
        OutputType.S3: SourceType.S3,
        OutputType.STORAGEGRID: SourceType.STORAGEGRID,
        OutputType.FILESYSTEM: SourceType.FILESYSTEM,
        OutputType.KAFKA: SourceType.KAFKA,
        OutputType.TEMP_VIEW: SourceType.TEMP_VIEW,
        OutputType.SFTP: SourceType.SFTP,
    }
    if output_type not in mapping:
        raise ConfigurationError(f"Output type '{output_type}' has no connector")
    return mapping[output_type]


def _flatten_complex_columns(dataframe: DataFrame) -> DataFrame:
    """Render array/map/struct columns as strings so JDBC writes succeed."""
    from pyspark.sql import functions as F

    result = dataframe
    for field_ in dataframe.schema.fields:
        type_name = field_.dataType.simpleString()
        if type_name.startswith(("array", "map", "struct")):
            if type_name.startswith("array"):
                result = result.withColumn(field_.name, F.concat_ws(",", F.col(field_.name)))
            else:
                result = result.withColumn(field_.name, F.to_json(F.col(field_.name)))
    return result
