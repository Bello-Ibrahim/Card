"""End-to-end pipeline test.

Exercises the vertical slice the platform is built around:

    CSV file  ─┐
               ├─ Spark reconciliation ─┬─ leg 1 result ─┐
    JDBC table ┘                        │                ├─ leg 2 (multi-leg DAG)
                                        │  settlements ──┘
                                        ├─ metrics + exceptions to the JDBC database
                                        ├─ Kafka completion event
                                        ├─ e-mail notification (real SMTP conversation)
                                        └─ advisor findings from the persisted evidence
"""

from __future__ import annotations

import sqlite3
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest

from reconx.advisor.chat import ReconAdvisor
from reconx.config.connections import ConnectionDefinition
from reconx.config.enums import RunStatus, TriggerType
from reconx.config.models import ReconciliationDefinition
from reconx.events.publisher import NullEventPublisher
from reconx.spark.io import StaticConnectionProvider
from reconx.spark.job import METRICS_CONNECTION_ID, ReconciliationJob, RunOptions

pytestmark = [pytest.mark.e2e, pytest.mark.spark]


# --------------------------------------------------------------------------- #
# A real (in-process) SMTP server so the notification path is genuinely tested
# --------------------------------------------------------------------------- #
class _CapturingHandler:
    def __init__(self) -> None:
        self.messages: list[dict[str, Any]] = []

    async def handle_DATA(self, server: Any, session: Any, envelope: Any) -> str:  # noqa: N802
        self.messages.append(
            {
                "from": envelope.mail_from,
                "to": list(envelope.rcpt_tos),
                "content": envelope.content.decode("utf-8", errors="replace"),
            }
        )
        return "250 Message accepted for delivery"


def _free_port() -> int:
    import socket

    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


@pytest.fixture
def smtp_server() -> Iterator[tuple[_CapturingHandler, int]]:
    """A real SMTP server on localhost, so the notification path is genuinely exercised."""
    from aiosmtpd.controller import Controller

    handler = _CapturingHandler()
    port = _free_port()
    controller = Controller(handler, hostname="127.0.0.1", port=port)
    controller.start()
    try:
        yield handler, port
    finally:
        controller.stop()


@pytest.fixture
def sqlite_ledger(tmp_path: Path) -> Path:
    """A JDBC (SQLite) source standing in for the general ledger."""
    database = tmp_path / "ledger.db"
    connection = sqlite3.connect(database)
    connection.execute(
        "CREATE TABLE ledger ("
        " country TEXT, customer_id TEXT, transaction_id TEXT, amount TEXT,"
        " currency TEXT, trade_date TEXT, ext_ref TEXT, business_date TEXT)"
    )
    connection.executemany(
        "INSERT INTO ledger VALUES (?,?,?,?,?,?,?,?)",
        [
            ("US", "1", "T1001", "100.50", "USD", "2026-09-10", "REF-1", "2026-09-10"),
            ("US", "2", "T1002", "250.01", "USD", "2026-09-10", "REF-2", "2026-09-10"),
            ("UK", "3", "T1003", "999.99", "GBP", "2026-09-10", "REF-3", "2026-09-10"),
            ("UK", "4", "T1004", "410.00", "EUR", "2026-09-10", "REF-X", "2026-09-10"),
            ("US", "7", "T1007", "700.00", "USD", "2026-09-10", "REF-7", "2026-09-10"),
            ("US", "9", "T9999", "1.00", "USD", "2026-09-09", "REF-9", "2026-09-09"),
        ],
    )
    connection.commit()
    connection.close()
    return database


@pytest.fixture
def settlements(tmp_path: Path) -> Path:
    path = tmp_path / "settlements.csv"
    path.write_text(
        "transaction_id,settled_amount,settlement_date,status\n"
        "T1001,100.50,2026-09-11,SETTLED\n"
        "T1002,250.00,2026-09-11,SETTLED\n"
        "T1003,300.75,2026-09-11,PENDING\n",
        encoding="utf-8",
    )
    return path


def _definition(csv_left: Path, ledger: Path, settlements_path: Path, output_dir: Path) -> dict[str, Any]:
    return {
        "reconId": "payments_e2e_recon",
        "name": "Payments E2E Reconciliation",
        "product": "PAYMENTS",
        "customer": "CUSTOMER_A",
        "status": "ACTIVE",
        "variables": [{"name": "ledger_table", "default": "ledger"}],
        "events": {"enabled": True, "onFailure": "WARN_ONLY"},
        "notifications": {
            "email": {
                "enabled": True,
                "recipients": ["recon.officer@example.com"],
                "cc": ["supervisor@example.com"],
                "on": ["SUCCESS", "FAILURE", "PARTIAL_SUCCESS"],
                "includeExceptionSample": True,
            }
        },
        "legs": [
            {
                "id": "transaction_leg",
                "name": "Transactions vs ledger",
                "sources": [
                    {
                        "id": "source_a",
                        "type": "filesystem",
                        "connectionRef": "local_files",
                        "path": str(csv_left),
                        "format": "csv",
                        "dataQuality": [
                            {"type": "not_null", "columns": ["customer_id", "transaction_id"]},
                            {"type": "row_count", "minRows": 1},
                        ],
                    },
                    {
                        "id": "source_b",
                        "type": "jdbc",
                        "connectionRef": "ledger_db",
                        "dialect": "sqlite",
                        "query": (
                            "SELECT country, customer_id, transaction_id, amount, currency, "
                            "trade_date, ext_ref FROM ${ledger_table} "
                            "WHERE business_date = '${business_date}'"
                        ),
                    },
                ],
                "leftSource": "source_a",
                "rightSource": "source_b",
                "keys": [
                    {"left": "country", "right": "country", "alias": "country"},
                    {
                        "left": "customer_id",
                        "right": "customer_id",
                        "alias": "customer_id",
                        "normalization": {"trim": True, "stripLeadingZeros": True},
                    },
                    {"left": "transaction_id", "right": "transaction_id", "alias": "transaction_id"},
                ],
                "matchLogic": {
                    "operator": "OR",
                    "rules": [
                        {
                            "id": "value_rule",
                            "name": "Amount and currency agree",
                            "operator": "AND",
                            "comparisons": [
                                {"left": "amount", "right": "amount", "rule": "numeric_tolerance",
                                 "tolerance": 0.01},
                                {"left": "currency", "right": "currency", "rule": "case_insensitive"},
                            ],
                        },
                        {
                            "id": "reference_rule",
                            "name": "External reference agrees",
                            "comparisons": [{"left": "ext_ref", "right": "ext_ref", "rule": "trimmed"}],
                        },
                    ],
                },
                "exceptionColumns": [
                    "trade_date",
                    {"alias": "country", "left": "country", "right": "country"},
                    {"alias": "ledger_currency", "right": "currency", "source": "right"},
                ],
                "aggregates": [
                    {"name": "total_amount", "function": "SUM", "leftField": "amount",
                     "rightField": "amount", "tolerance": 0.01}
                ],
                "outputs": [
                    {
                        "id": "results",
                        "type": "filesystem",
                        "connectionRef": "local_files",
                        "path": str(output_dir / "transaction_leg"),
                        "format": "parquet",
                        "mode": "overwrite",
                    }
                ],
            },
            {
                "id": "settlement_leg",
                "name": "Matched transactions vs settlements",
                "sources": [
                    {
                        "id": "previous_leg",
                        "type": "leg_output",
                        "legRef": "transaction_leg",
                        "transformations": [
                            {"type": "filter", "condition": "match_category = 'MATCHED'"},
                            {"type": "select", "columns": ["key_transaction_id", "left_amount"]},
                            {
                                "type": "rename",
                                "mapping": {"key_transaction_id": "transaction_id", "left_amount": "amount"},
                            },
                        ],
                    },
                    {
                        "id": "settlement",
                        "type": "filesystem",
                        "connectionRef": "local_files",
                        "path": str(settlements_path),
                        "format": "csv",
                    },
                ],
                "leftSource": "previous_leg",
                "rightSource": "settlement",
                "keys": [{"left": "transaction_id", "right": "transaction_id", "alias": "transaction_id"}],
                "comparisons": [
                    {"left": "amount", "right": "settled_amount", "rule": "numeric_tolerance",
                     "tolerance": 0.01}
                ],
                "exceptionColumns": [{"alias": "settlement_status", "right": "status", "source": "right"}],
            },
        ],
        "schedule": {"type": "cron", "expression": "0 2 * * *", "timezone": "UTC"},
    }


def _metrics_connection_for(metrics_repository: Any) -> ConnectionDefinition:
    """Point the internal metrics connection at the database the test uses.

    The job writes exceptions to the metrics database through Spark JDBC; the
    assertions read them back through the repository, so both must address the
    same database.
    """
    from reconx.config.settings import sqlalchemy_to_jdbc

    url = metrics_repository.engine.url
    jdbc_url = sqlalchemy_to_jdbc(str(url.render_as_string(hide_password=False)))
    return ConnectionDefinition.model_validate(
        {
            "connectionId": METRICS_CONNECTION_ID,
            "name": "Test metrics database",
            "type": "jdbc",
            "config": {
                "databaseType": url.get_backend_name(),
                "jdbcUrl": jdbc_url,
                "username": url.username,
                "password": url.password,
                "database": url.database,
            },
        }
    )


@pytest.fixture
def connections(sqlite_ledger: Path, metrics_repository) -> dict[str, ConnectionDefinition]:
    return {
        "local_files": ConnectionDefinition.model_validate(
            {
                "connectionId": "local_files",
                "name": "Local files",
                "type": "filesystem",
                "config": {"basePath": "/"},
            }
        ),
        "ledger_db": ConnectionDefinition.model_validate(
            {
                "connectionId": "ledger_db",
                "name": "Ledger",
                "type": "jdbc",
                "config": {
                    "databaseType": "sqlite",
                    "jdbcUrl": f"jdbc:sqlite:{sqlite_ledger}",
                    "database": str(sqlite_ledger),
                },
            }
        ),
        METRICS_CONNECTION_ID: _metrics_connection_for(metrics_repository),
    }


class TestEndToEndPipeline:
    @pytest.fixture(autouse=True)
    def _configure_smtp(self, smtp_server, monkeypatch):
        handler, port = smtp_server
        self.smtp_handler = handler
        monkeypatch.setenv("SMTP_HOST", "127.0.0.1")
        monkeypatch.setenv("SMTP_PORT", str(port))
        monkeypatch.setenv("SMTP_USE_TLS", "false")
        monkeypatch.setenv("SMTP_FROM_ADDRESS", "reconx@example.com")
        from reconx.config.settings import reset_settings_cache

        reset_settings_cache()
        yield
        reset_settings_cache()

    def test_full_pipeline(
        self, spark, tmp_path, csv_sources, sqlite_ledger, settlements, connections, metrics_repository
    ):
        from reconx.config.settings import get_settings

        settings = get_settings()
        settings.staging_dir = str(tmp_path / "staging")

        output_dir = tmp_path / "out"
        definition = ReconciliationDefinition.model_validate(
            _definition(csv_sources["left"], sqlite_ledger, settlements, output_dir)
        )
        events = NullEventPublisher()
        options = RunOptions(
            run_id="e2e-run-1",
            business_date="2026-09-10",
            trigger_type=TriggerType.MANUAL,
            triggered_by="pytest",
            profile_sources=True,
        )

        job = ReconciliationJob(
            definition,
            StaticConnectionProvider(connections),
            options,
            settings=settings,
            spark=spark,
            metrics=metrics_repository,
            events=events,
        )
        summary = job.run()

        # ---- 1. the run itself -------------------------------------------
        assert summary.status is RunStatus.SUCCESS, summary.error
        assert summary.metrics["recordsRead"] > 0
        assert len(summary.legs) == 2

        transaction_leg = next(leg for leg in summary.legs if leg["legId"] == "transaction_leg")
        assert transaction_leg["matched"] == 3          # T1001, T1002 (tolerance), T1003 (OR on ext_ref)
        assert transaction_leg["mismatched"] == 1       # T1004: both rules fail
        assert transaction_leg["leftOnly"] == 3         # T1005 + duplicated T1006
        assert transaction_leg["rightOnly"] == 1        # T1007
        assert transaction_leg["duplicatesLeft"] == 2

        # The JDBC source was filtered by ${business_date}: the 2026-09-09 row is excluded.
        assert transaction_leg["rightRecords"] == 5

        # ---- 2. multi-leg DAG --------------------------------------------
        settlement_leg = next(leg for leg in summary.legs if leg["legId"] == "settlement_leg")
        assert settlement_leg["stage"] == 1
        assert settlement_leg["leftRecords"] == 3       # only the matched transactions flowed through
        assert settlement_leg["matched"] >= 2

        # ---- 3. outputs ---------------------------------------------------
        written = list((output_dir / "transaction_leg").glob("*.parquet"))
        assert written, "parquet output was not written"
        result_frame = spark.read.parquet(str(output_dir / "transaction_leg"))
        assert "match_category" in result_frame.columns
        assert "run_id" in result_frame.columns

        # ---- 4. metrics database -----------------------------------------
        run_row = metrics_repository.get_run("e2e-run-1")
        assert run_row["status"] == "SUCCESS"
        assert run_row["records_matched"] == summary.metrics["recordsMatched"]

        leg_rows = metrics_repository.list_leg_runs("e2e-run-1")
        assert {row["leg_id"] for row in leg_rows} == {"transaction_leg", "settlement_leg"}
        assert leg_rows[0]["match_logic"]

        field_metrics = metrics_repository.list_field_metrics("e2e-run-1")
        assert any(row["field_name"] == "currency" for row in field_metrics)

        source_metrics = metrics_repository.list_source_metrics("e2e-run-1")
        assert {row["source_id"] for row in source_metrics} >= {"source_a", "source_b"}
        assert any(row["data_quality_passed"] for row in source_metrics)

        # ---- 5. exceptions with configured context columns ---------------
        exceptions = metrics_repository.list_exceptions(run_id="e2e-run-1")
        assert exceptions
        import json as _json

        mismatch = next(row for row in exceptions if row["exception_type"] == "MISMATCH")
        context = _json.loads(mismatch["context_columns"])
        assert context["trade_date"] == "2026-09-10"
        assert context["country"] == "UK"
        assert context["ledger_currency"] == "EUR"      # taken from the right side only
        assert mismatch["field"] in ("currency", "ext_ref")

        # ---- 6. Kafka events ---------------------------------------------
        event_types = [event.event_type for event in events.events]
        assert "RECONCILIATION_STARTED" in event_types
        assert "RECONCILIATION_COMPLETED" in event_types
        completion = next(e for e in events.events if e.event_type == "RECONCILIATION_COMPLETED")
        assert completion.run_id == "e2e-run-1"
        assert completion.records_matched == summary.metrics["recordsMatched"]
        assert completion.status == "SUCCESS"

        # ---- 7. e-mail notification (real SMTP conversation) --------------
        assert self.smtp_handler.messages, "no e-mail was delivered"
        message = self.smtp_handler.messages[0]
        assert "recon.officer@example.com" in message["to"]
        assert "supervisor@example.com" in message["to"]
        assert "Payments E2E Reconciliation" in message["content"]
        assert "2026-09-10" in message["content"]

        # ---- 8. advisor over the persisted evidence -----------------------
        advisor = ReconAdvisor(metrics_repository=metrics_repository)
        context_bundle = advisor.build_context(run_id="e2e-run-1")
        assert context_bundle.run is not None
        assert context_bundle.legs

        advice = advisor.advise(context_bundle)
        assert advice, "the advisor produced no findings"
        categories = {item.category.value for item in advice}
        assert categories & {"KEY_SELECTION", "DUPLICATES", "MATCHING_RULE", "TOLERANCE", "COVERAGE"}

        reply = advisor.answer("Why did records not match?", context_bundle, allow_llm=False)
        assert "transaction_leg" in reply.text
        assert reply.intent == "unmatched"

        duplicates_reply = advisor.answer("What about duplicates?", context_bundle, allow_llm=False)
        assert "ambiguous" in duplicates_reply.text

    def test_exception_close_out_after_a_run(self, metrics_repository):
        """An officer closes a break produced by a run, with an auditable reason."""
        metrics_repository.record_exceptions(
            [
                {
                    "run_id": "e2e-run-2",
                    "recon_id": "payments_e2e_recon",
                    "leg_id": "transaction_leg",
                    "business_date": "2026-09-10",
                    "reconciliation_key": "UK|4|T1004",
                    "exception_type": "MISMATCH",
                    "field": "currency",
                    "expected_value": "GBP",
                    "actual_value": "EUR",
                    "context_columns": {"trade_date": "2026-09-10", "country": "UK"},
                }
            ]
        )
        exception_id = metrics_repository.list_exceptions(run_id="e2e-run-2")[0]["id"]

        result = metrics_repository.update_exception_status(
            [exception_id],
            status="RESOLVED",
            comment="Ledger booked the FX leg in EUR; economically equivalent. Confirmed with Treasury.",
            actor="jane.officer",
            resolution_code="FX_RATE",
        )
        assert result["updated"] == 1

        record = metrics_repository.get_exception(exception_id)
        assert record["status"] == "RESOLVED"
        assert record["resolved_by"] == "jane.officer"
        assert record["resolution_code"] == "FX_RATE"

        comments = metrics_repository.list_exception_comments(exception_id)
        assert comments[0]["status_before"] == "OPEN"
        assert comments[0]["status_after"] == "RESOLVED"
        assert "Treasury" in comments[0]["comment"]

        assert metrics_repository.exception_status_summary(recon_id="payments_e2e_recon")["RESOLVED"] >= 1
