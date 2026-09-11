"""MongoDB client, collection names and index management."""

from __future__ import annotations

import functools
from typing import Any

from pymongo import ASCENDING, DESCENDING, MongoClient
from pymongo.database import Database
from pymongo.errors import PyMongoError

from reconx.common.errors import ConfigurationError
from reconx.common.logging import get_logger
from reconx.config.settings import Settings, get_settings

log = get_logger(__name__)


class Collections:
    DEFINITIONS = "reconciliation_definitions"
    VERSIONS = "reconciliation_versions"
    CONNECTIONS = "connections"
    RUNS = "runs"
    LEG_RUNS = "leg_runs"
    SCHEDULE_STATE = "schedule_state"
    LOCKS = "locks"
    USERS = "users"
    AUDIT = "audit_log"
    EVENTS_OUTBOX = "events_outbox"
    ADVISOR_SESSIONS = "advisor_sessions"
    COLUMN_PROFILES = "column_profiles"


@functools.lru_cache(maxsize=4)
def _client_for(uri: str, tls: bool, timeout_ms: int, pool: int) -> MongoClient:
    return MongoClient(
        uri,
        tls=tls,
        serverSelectionTimeoutMS=timeout_ms,
        maxPoolSize=pool,
        appname="reconx",
        retryWrites=True,
        tz_aware=True,
    )


def get_mongo_client(settings: Settings | None = None) -> MongoClient:
    settings = settings or get_settings()
    return _client_for(
        settings.mongo.uri,
        settings.mongo.tls,
        settings.mongo.server_selection_timeout_ms,
        settings.mongo.max_pool_size,
    )


def get_database(settings: Settings | None = None) -> Database:
    settings = settings or get_settings()
    return get_mongo_client(settings)[settings.mongo.database]


def ping(settings: Settings | None = None) -> dict[str, Any]:
    settings = settings or get_settings()
    client = get_mongo_client(settings)
    try:
        result = client.admin.command("ping")
        info = client.server_info()
        return {"ok": bool(result.get("ok")), "version": info.get("version")}
    except PyMongoError as exc:
        raise ConfigurationError(f"MongoDB not reachable: {exc}") from exc


def ensure_indexes(db: Database | None = None, settings: Settings | None = None) -> list[str]:
    """Create every index the platform relies on.  Safe to run repeatedly."""
    db = db if db is not None else get_database(settings)
    created: list[str] = []

    def _index(collection: str, keys: Any, **kwargs: Any) -> None:
        name = db[collection].create_index(keys, **kwargs)
        created.append(f"{collection}.{name}")

    _index(Collections.DEFINITIONS, [("reconId", ASCENDING)], unique=True, name="uq_recon_id")
    _index(Collections.DEFINITIONS, [("status", ASCENDING), ("enabled", ASCENDING)], name="ix_status")
    _index(Collections.DEFINITIONS, [("product", ASCENDING), ("customer", ASCENDING)], name="ix_prod_cust")
    _index(Collections.DEFINITIONS, [("tags", ASCENDING)], name="ix_tags")
    _index(Collections.DEFINITIONS, [("updatedAt", DESCENDING)], name="ix_updated")

    _index(
        Collections.VERSIONS,
        [("reconId", ASCENDING), ("version", DESCENDING)],
        unique=True,
        name="uq_recon_version",
    )

    _index(Collections.CONNECTIONS, [("connectionId", ASCENDING)], unique=True, name="uq_connection_id")
    _index(Collections.CONNECTIONS, [("type", ASCENDING), ("environment", ASCENDING)], name="ix_type_env")

    _index(Collections.RUNS, [("runId", ASCENDING)], unique=True, name="uq_run_id")
    _index(Collections.RUNS, [("reconId", ASCENDING), ("startTime", DESCENDING)], name="ix_recon_start")
    _index(Collections.RUNS, [("status", ASCENDING), ("startTime", DESCENDING)], name="ix_status_start")
    _index(
        Collections.RUNS,
        [("idempotencyKey", ASCENDING)],
        unique=True,
        partialFilterExpression={"idempotencyKey": {"$type": "string"}},
        name="uq_idempotency_key",
    )
    _index(Collections.RUNS, [("businessDate", DESCENDING)], name="ix_business_date")

    _index(Collections.LEG_RUNS, [("runId", ASCENDING), ("legId", ASCENDING)], unique=True, name="uq_leg_run")

    _index(Collections.SCHEDULE_STATE, [("reconId", ASCENDING)], unique=True, name="uq_schedule_recon")
    _index(Collections.SCHEDULE_STATE, [("nextRunAt", ASCENDING)], name="ix_next_run")

    _index(Collections.LOCKS, [("lockId", ASCENDING)], unique=True, name="uq_lock_id")
    _index(Collections.LOCKS, [("expiresAt", ASCENDING)], expireAfterSeconds=0, name="ttl_lock")

    _index(Collections.USERS, [("username", ASCENDING)], unique=True, name="uq_username")

    _index(Collections.AUDIT, [("timestamp", DESCENDING)], name="ix_audit_ts")
    _index(Collections.AUDIT, [("entityType", ASCENDING), ("entityId", ASCENDING)], name="ix_audit_entity")

    _index(Collections.EVENTS_OUTBOX, [("status", ASCENDING), ("createdAt", ASCENDING)], name="ix_outbox")
    _index(Collections.ADVISOR_SESSIONS, [("sessionId", ASCENDING)], unique=True, name="uq_advisor_session")
    _index(Collections.ADVISOR_SESSIONS, [("updatedAt", DESCENDING)], name="ix_advisor_updated")
    _index(
        Collections.COLUMN_PROFILES,
        [("runId", ASCENDING), ("legId", ASCENDING), ("sourceId", ASCENDING)],
        name="ix_profile_run",
    )
    _index(Collections.COLUMN_PROFILES, [("reconId", ASCENDING), ("createdAt", DESCENDING)], name="ix_profile_recon")

    log.info("mongo.indexes_ensured", count=len(created))
    return created
