"""Generic JDBC connector.

Vendor neutral by construction: the driver class, URL and properties all come
from the connection definition.  Predicate pushdown (``query``), column pruning
and partitioned reads (``partitionColumn``/``numPartitions``) are supported so
large tables never funnel through a single connection.
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any

from reconx.common.errors import ConnectionFailedError, ConnectorError
from reconx.common.logging import get_logger
from reconx.config.connections import DEFAULT_DRIVERS, JdbcConnectionConfig
from reconx.config.enums import SourceType
from reconx.config.settings import jdbc_to_sqlalchemy
from reconx.connectors.base import (
    ConnectionTestResult,
    DataSourceConnector,
    OutputContext,
    SourceContext,
    register_connector,
)
from reconx.security.sql_guard import assert_read_only, assert_table_name

if TYPE_CHECKING:  # pragma: no cover
    from pyspark.sql import DataFrame, SparkSession

log = get_logger(__name__)


def build_jdbc_properties(config: dict[str, Any]) -> dict[str, str]:
    typed = JdbcConnectionConfig.model_validate(config)
    properties: dict[str, str] = {
        "user": config.get("username") or "",
        "password": config.get("password") or "",
        "driver": typed.resolved_driver() or DEFAULT_DRIVERS.get(typed.database_type.lower(), ""),
        "fetchsize": str(typed.fetch_size),
        "batchsize": str(typed.batch_size),
        "queryTimeout": str(typed.query_timeout_seconds),
        "isolationLevel": typed.isolation_level,
    }
    if typed.session_init_statement:
        assert_read_only(typed.session_init_statement, context="sessionInitStatement")
        properties["sessionInitStatement"] = typed.session_init_statement
    for key, value in (typed.extra_properties or {}).items():
        properties[key] = str(value)
    return {k: v for k, v in properties.items() if v != ""}


def jdbc_url_of(config: dict[str, Any]) -> str:
    return JdbcConnectionConfig.model_validate(config).resolved_url()


@register_connector
class JdbcConnector(DataSourceConnector):
    source_types = (SourceType.JDBC,)
    display_name = "JDBC relational database"

    def read(self, config: SourceContext, spark: SparkSession) -> DataFrame:
        source = config.source
        conn = config.resolved_config
        url = jdbc_url_of(conn)
        properties = build_jdbc_properties(conn)
        reader = spark.read.format("jdbc").option("url", url).options(**properties)

        if source.query:
            assert_read_only(source.query, context=f"source.{source.id}.query")
            reader = reader.option("query", source.query)
        else:
            table = source.table or ""
            assert_table_name(table, context=f"source.{source.id}.table")
            schema_name = conn.get("schema") or conn.get("dbSchema")
            qualified = f"{schema_name}.{table}" if schema_name and "." not in table else table
            reader = reader.option("dbtable", qualified)

        partition_column = source.options.get("partitionColumn") or conn.get("partitionColumn")
        num_partitions = source.options.get("numPartitions") or conn.get("numPartitions")
        if partition_column and num_partitions:
            lower = source.options.get("lowerBound") or conn.get("lowerBound")
            upper = source.options.get("upperBound") or conn.get("upperBound")
            if lower is None or upper is None:
                raise ConnectorError(
                    f"source '{source.id}': partitioned JDBC reads require lowerBound and upperBound"
                )
            reader = reader.options(
                partitionColumn=str(partition_column),
                numPartitions=str(num_partitions),
                lowerBound=str(lower),
                upperBound=str(upper),
            )
            log.info("jdbc.partitioned_read", column=partition_column, partitions=num_partitions)

        for key, value in source.options.items():
            if key not in {"partitionColumn", "numPartitions", "lowerBound", "upperBound"}:
                reader = reader.option(key, str(value))

        log.info("jdbc.read", url=_safe_url(url), table=source.table, has_query=bool(source.query))
        return reader.load()

    def write(self, dataframe: DataFrame, config: OutputContext) -> dict[str, Any]:
        output = config.output
        conn = config.resolved_config
        url = jdbc_url_of(conn)
        properties = build_jdbc_properties(conn)
        table = output.table or ""
        assert_table_name(table, context="output.table")
        schema_name = conn.get("schema") or conn.get("dbSchema")
        qualified = f"{schema_name}.{table}" if schema_name and "." not in table else table
        writer = (
            dataframe.write.format("jdbc")
            .option("url", url)
            .option("dbtable", qualified)
            .options(**properties)
            .mode(output.mode.value)
        )
        for key, value in (output.options or {}).items():
            writer = writer.option(key, str(value))
        if output.options.get("truncate"):
            writer = writer.option("truncate", "true")
        writer.save()
        log.info("jdbc.write", table=qualified, mode=output.mode.value)
        return {"target": qualified, "mode": output.mode.value}

    def test_connection(self, config: dict[str, Any]) -> ConnectionTestResult:
        started = time.time()
        url = None
        try:
            url = jdbc_url_of(config)
            sqlalchemy_url = jdbc_to_sqlalchemy(url, config.get("username"), config.get("password"))
            from sqlalchemy import create_engine, text

            engine = create_engine(
                sqlalchemy_url,
                pool_pre_ping=True,
                connect_args={"connect_timeout": int(config.get("connectTimeoutSeconds", 10))}
                if sqlalchemy_url.startswith(("postgresql", "mysql"))
                else {},
            )
            with engine.connect() as connection:
                version = connection.execute(text("SELECT 1")).scalar()
            engine.dispose()
            return ConnectionTestResult(
                True,
                f"Connected to {config.get('databaseType', 'database')} at {_safe_url(url)}",
                latency_ms=int((time.time() - started) * 1000),
                details={"probe": version, "url": _safe_url(url)},
            )
        except ImportError as exc:
            return ConnectionTestResult(
                False,
                (
                    f"No Python driver installed for '{config.get('databaseType')}' - the connection test "
                    f"needs one ({exc}). Spark itself only needs the JDBC jar."
                ),
            )
        except Exception as exc:
            return ConnectionTestResult(
                False,
                f"JDBC connection failed: {type(exc).__name__}: {exc}",
                latency_ms=int((time.time() - started) * 1000),
                details={"url": _safe_url(url) if url else None},
            )

    def validate(self, config: dict[str, Any]) -> list[str]:
        problems: list[str] = []
        try:
            typed = JdbcConnectionConfig.model_validate(config)
            typed.resolved_url()
            if not typed.resolved_driver():
                problems.append(
                    f"no default JDBC driver known for '{typed.database_type}' - set 'driver' explicitly"
                )
        except Exception as exc:
            problems.append(str(exc))
        if not config.get("username"):
            problems.append("'username' is required")
        if not config.get("password"):
            problems.append("'password' is required (use a secret reference)")
        return problems

    def execute_scalar(self, config: dict[str, Any], query: str) -> Any:
        """Run a read-only scalar query (used by availability conditions)."""
        assert_read_only(query, context="condition.query")
        url = jdbc_to_sqlalchemy(jdbc_url_of(config), config.get("username"), config.get("password"))
        from sqlalchemy import create_engine, text

        engine = create_engine(url, pool_pre_ping=True)
        try:
            with engine.connect() as connection:
                result = connection.execute(text(query))
                row = result.fetchone()
                return row[0] if row else None
        except Exception as exc:
            raise ConnectionFailedError(f"JDBC condition query failed: {exc}") from exc
        finally:
            engine.dispose()


def preview_query(
    config: dict[str, Any],
    *,
    query: str | None = None,
    table: str | None = None,
    limit: int = 100,
    variables: dict[str, Any] | None = None,
    timeout_seconds: int = 60,
) -> dict[str, Any]:
    """Run a read-only query and return the first ``limit`` rows.

    Used by the "Preview query" action in the reconciliation designer so an
    officer can validate a hand-written statement - including ``${variable}``
    substitution in the query *and* in table names - before saving the
    configuration.

    The row cap is enforced by streaming the cursor and stopping after
    ``limit`` rows, so it works with any dialect (SQL Server ``TOP``, Oracle
    ``FETCH FIRST``, PostgreSQL ``LIMIT``) and never rewrites the user's SQL.
    """
    from reconx.common.templating import build_run_variables, render

    if not query and not table:
        raise ConnectorError("Provide either a query or a table to preview")

    render_variables = build_run_variables(extra=variables or {})
    if query:
        statement = render(query, render_variables, strict=False)
        assert_read_only(statement, context="preview.query")
    else:
        rendered_table = render(str(table), render_variables, strict=False)
        assert_table_name(rendered_table, context="preview.table")
        statement = f"SELECT * FROM {rendered_table}"

    url = jdbc_to_sqlalchemy(jdbc_url_of(config), config.get("username"), config.get("password"))
    from sqlalchemy import create_engine, text

    engine = create_engine(url, pool_pre_ping=True)
    started = time.time()
    try:
        with engine.connect() as connection:
            result = connection.execution_options(stream_results=True).execute(text(statement))
            columns = list(result.keys())
            rows: list[dict[str, Any]] = []
            for row in result:
                rows.append({column: _jsonable(value) for column, value in zip(columns, row, strict=False)})
                if len(rows) >= limit:
                    break
            truncated = bool(result.fetchone())
        return {
            "columns": columns,
            "rows": rows,
            "rowCount": len(rows),
            "truncated": truncated,
            "elapsedMs": int((time.time() - started) * 1000),
            "statement": statement,
        }
    except Exception as exc:
        raise ConnectionFailedError(
            f"Query preview failed: {type(exc).__name__}: {str(exc)[:800]}",
            details={"statement": statement[:2000]},
        ) from exc
    finally:
        engine.dispose()


def list_tables(config: dict[str, Any], *, schema: str | None = None, limit: int = 500) -> list[dict[str, Any]]:
    """List tables/views visible to the connection (populates UI pickers)."""
    url = jdbc_to_sqlalchemy(jdbc_url_of(config), config.get("username"), config.get("password"))
    from sqlalchemy import create_engine, inspect

    engine = create_engine(url, pool_pre_ping=True)
    try:
        inspector = inspect(engine)
        target_schema = schema or config.get("schema") or config.get("dbSchema")
        entries: list[dict[str, Any]] = []
        schemas = [target_schema] if target_schema else (inspector.get_schema_names() or [None])
        for schema_name in schemas[:20]:
            for table in inspector.get_table_names(schema=schema_name)[:limit]:
                entries.append({"schema": schema_name, "name": table, "type": "TABLE"})
            for view in inspector.get_view_names(schema=schema_name)[:limit]:
                entries.append({"schema": schema_name, "name": view, "type": "VIEW"})
            if len(entries) >= limit:
                break
        return entries[:limit]
    except Exception as exc:
        raise ConnectionFailedError(f"Could not list tables: {type(exc).__name__}: {exc}") from exc
    finally:
        engine.dispose()


def _jsonable(value: Any) -> Any:
    from datetime import date, datetime
    from decimal import Decimal

    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, (bytes, bytearray)):
        return f"<{len(value)} bytes>"
    return value


def _safe_url(url: str | None) -> str:
    """Strip any credentials that a user embedded in a JDBC URL before logging."""
    if not url:
        return ""
    import re

    return re.sub(r"(password|user)=([^&;]*)", r"\1=***", url, flags=re.IGNORECASE)
