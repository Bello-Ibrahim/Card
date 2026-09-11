"""Shared pytest fixtures.

Design notes
------------
* **Spark** sessions are expensive: one module-scoped local session is shared by
  every Spark test.
* **MongoDB** is replaced by ``mongomock`` so repository and API tests run
  without a server.  The integration suite (``-m integration``) runs the same
  code against the real MongoDB from ``docker compose``.
* **The metrics database** uses SQLite by default and PostgreSQL when
  ``RECONX_TEST_POSTGRES_URL`` is set, which is how the vendor-neutral SQL is
  verified against a real RDBMS.
"""

from __future__ import annotations

import os
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import pytest

SRC = Path(__file__).resolve().parents[1] / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

os.environ.setdefault("RECONX_ENVIRONMENT", "test")
os.environ.setdefault("LOG_LEVEL", "WARNING")
os.environ.setdefault("LOG_FORMAT", "console")
os.environ.setdefault("KAFKA_ENABLED", "false")
os.environ.setdefault("RECONX_SECURITY_ENCRYPTION_KEY", "test-encryption-key-for-unit-tests")
os.environ.setdefault("RECONX_SECURITY_JWT_SECRET", "test-jwt-secret-value-at-least-32-bytes-long")
os.environ.setdefault("RECONX_BCRYPT_ROUNDS", "4")  # keep password hashing fast in tests


def _jdbc_jars() -> str:
    """JDBC drivers to put on the test Spark classpath.

    ``scripts/fetch-jdbc-drivers.sh`` downloads them into ``.jars``; tests that
    need a relational source are skipped when they are absent rather than
    failing with an opaque ClassNotFoundException.
    """
    explicit = os.getenv("SPARK_EXTRA_JARS")
    if explicit:
        return explicit
    jars_directory = Path(__file__).resolve().parents[1] / ".jars"
    if not jars_directory.is_dir():
        return ""
    return ",".join(str(jar) for jar in sorted(jars_directory.glob("*.jar")))


@pytest.fixture(scope="session")
def spark() -> Iterator[Any]:
    """A local SparkSession shared by the whole test session."""
    pytest.importorskip("pyspark")
    from pyspark.sql import SparkSession

    builder = (
        SparkSession.builder.master("local[2]")
        .appName("reconx-tests")
        .config("spark.sql.shuffle.partitions", "4")
        .config("spark.ui.enabled", "false")
        .config("spark.sql.session.timeZone", "UTC")
        .config("spark.driver.host", "127.0.0.1")
    )
    jars = _jdbc_jars()
    if jars:
        builder = builder.config("spark.jars", jars).config("spark.driver.extraClassPath", jars.replace(",", ":"))
    session = builder.getOrCreate()
    session.sparkContext.setLogLevel("ERROR")
    yield session
    session.stop()


@pytest.fixture(scope="session")
def spark_has_jdbc_driver(spark: Any) -> bool:
    """Whether a JDBC driver is on the Spark classpath (see ``.jars``)."""
    return bool(_jdbc_jars())


@pytest.fixture
def mongo_db() -> Iterator[Any]:
    """An in-memory MongoDB substitute."""
    mongomock = pytest.importorskip("mongomock")
    client = mongomock.MongoClient()
    yield client["reconx_test"]
    client.close()


@pytest.fixture
def metrics_repository(tmp_path: Path) -> Iterator[Any]:
    """Metrics repository backed by SQLite (or PostgreSQL when configured)."""
    from sqlalchemy import create_engine

    from reconx.metrics.repository import MetricsRepository

    url = os.getenv("RECONX_TEST_POSTGRES_URL") or f"sqlite:///{tmp_path / 'metrics.db'}"
    engine = create_engine(url)
    repository = MetricsRepository(engine=engine)
    if os.getenv("RECONX_TEST_POSTGRES_URL"):
        from reconx.metrics.models import metadata

        metadata.drop_all(engine, checkfirst=True)
    repository.create_schema()
    yield repository
    repository.close()


@pytest.fixture
def sample_definition() -> dict[str, Any]:
    """A realistic two-leg definition used across the suite."""
    return {
        "reconId": "payments_daily_recon",
        "name": "Payments Daily Reconciliation",
        "product": "PAYMENTS",
        "customer": "CUSTOMER_A",
        "status": "DRAFT",
        "variables": [
            {"name": "ledger_table", "default": "ledger", "label": "Ledger table"},
            {"name": "business_unit", "default": "CORP", "type": "choice", "choices": ["CORP", "RETAIL"]},
        ],
        "legs": [
            {
                "id": "transaction_leg",
                "name": "Transactions vs ledger",
                "sources": [
                    {
                        "id": "source_a",
                        "type": "filesystem",
                        "connectionRef": "local_files",
                        "path": "/data/a.csv",
                        "format": "csv",
                    },
                    {
                        "id": "source_b",
                        "type": "filesystem",
                        "connectionRef": "local_files",
                        "path": "/data/b.csv",
                        "format": "csv",
                    },
                ],
                "keys": [{"left": "customer_id", "right": "customer_id", "alias": "customer_id"}],
                "matchLogic": {
                    "operator": "OR",
                    "rules": [
                        {
                            "id": "value_rule",
                            "name": "Amount and currency agree",
                            "operator": "AND",
                            "comparisons": [
                                {
                                    "left": "amount",
                                    "right": "amount",
                                    "rule": "numeric_tolerance",
                                    "tolerance": 0.01,
                                },
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
                "exceptionColumns": ["trade_date", {"alias": "country", "left": "country", "right": "country"}],
            }
        ],
        "schedule": {"type": "cron", "expression": "0 2 * * *", "timezone": "UTC"},
    }


@pytest.fixture
def connection_definitions() -> dict[str, Any]:
    from reconx.config.connections import ConnectionDefinition

    return {
        "local_files": ConnectionDefinition.model_validate(
            {
                "connectionId": "local_files",
                "name": "Local files",
                "type": "filesystem",
                "config": {"basePath": "/"},
            }
        )
    }


@pytest.fixture
def csv_sources(tmp_path: Path) -> dict[str, Path]:
    """Two small CSV feeds with deliberate, realistic differences."""
    left = tmp_path / "source_a.csv"
    right = tmp_path / "source_b.csv"
    left.write_text(
        "country,customer_id,transaction_id,amount,currency,trade_date,ext_ref\n"
        "US,0001,T1001,100.50,USD,2026-09-10,REF-1\n"
        "US,0002,T1002,250.00,usd,2026-09-10,REF-2\n"
        "UK,0003,T1003,300.75,GBP,2026-09-10,REF-3\n"
        "UK,0004,T1004,410.00,GBP,2026-09-10,REF-4\n"
        "US,0005,T1005,500.25,USD,2026-09-10,REF-5\n"
        "US,0006,T1006,600.00,USD,2026-09-10,REF-6\n"
        "US,0006,T1006,600.00,USD,2026-09-10,REF-6\n",
        encoding="utf-8",
    )
    right.write_text(
        "country,customer_id,transaction_id,amount,currency,trade_date,ext_ref\n"
        "US,1,T1001,100.50,USD,2026-09-10,REF-1\n"
        "US,2,T1002,250.01,USD,2026-09-10,REF-2\n"
        "UK,3,T1003,999.99,GBP,2026-09-10,REF-3\n"
        "UK,4,T1004,410.00,EUR,2026-09-10,REF-X\n"
        "US,7,T1007,700.00,USD,2026-09-10,REF-7\n",
        encoding="utf-8",
    )
    return {"left": left, "right": right}
