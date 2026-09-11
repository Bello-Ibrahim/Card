"""Audit trail.

Every state-changing operation is recorded with actor, action, target, the
old/new version and a field-level diff.  Records go to MongoDB (queryable from
the UI) and, best-effort, to the JDBC ``audit_log`` table for long-term
reporting.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from pymongo.collection import Collection
from pymongo.database import Database

from reconx.common.logging import get_logger, scrub
from reconx.common.timeutils import utcnow

log = get_logger(__name__)

AUDIT_COLLECTION = "audit_log"


class AuditAction:
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    ACTIVATE = "ACTIVATE"
    DISABLE = "DISABLE"
    ARCHIVE = "ARCHIVE"
    ROLLBACK = "ROLLBACK"
    EXECUTE = "EXECUTE"
    CANCEL = "CANCEL"
    TEST = "TEST"
    LOGIN = "LOGIN"
    LOGIN_FAILED = "LOGIN_FAILED"
    LOGOUT = "LOGOUT"
    SCHEDULE_PAUSE = "SCHEDULE_PAUSE"
    SCHEDULE_RESUME = "SCHEDULE_RESUME"
    PERMISSION_DENIED = "PERMISSION_DENIED"


def diff_documents(old: Mapping[str, Any] | None, new: Mapping[str, Any] | None) -> dict[str, Any]:
    """Shallow-but-recursive diff of two configuration documents."""
    old = old or {}
    new = new or {}
    changes: dict[str, Any] = {}
    for key in sorted(set(old) | set(new)):
        if key in {"_id", "updatedAt", "createdAt", "version"}:
            continue
        before, after = old.get(key), new.get(key)
        if before == after:
            continue
        if isinstance(before, Mapping) and isinstance(after, Mapping):
            nested = diff_documents(before, after)
            if nested:
                changes[key] = nested
        else:
            changes[key] = {"before": scrub({key: before})[key], "after": scrub({key: after})[key]}
    return changes


class AuditLogger:
    """Writes audit records; never raises into the caller's path."""

    def __init__(self, database: Database, metrics_repository: Any | None = None) -> None:
        self.db = database
        self.metrics = metrics_repository

    @property
    def collection(self) -> Collection:
        return self.db[AUDIT_COLLECTION]

    def ensure_indexes(self) -> None:
        self.collection.create_index([("timestamp", -1)], name="ix_audit_ts")
        self.collection.create_index([("entityType", 1), ("entityId", 1)], name="ix_audit_entity")
        self.collection.create_index("actor", name="ix_audit_actor")

    def record(
        self,
        *,
        action: str,
        entity_type: str,
        entity_id: str,
        actor: str,
        details: Mapping[str, Any] | None = None,
        old_version: int | None = None,
        new_version: int | None = None,
        changes: Mapping[str, Any] | None = None,
        success: bool = True,
        source_ip: str | None = None,
        user_agent: str | None = None,
    ) -> None:
        record = {
            "timestamp": utcnow(),
            "action": action,
            "entityType": entity_type,
            "entityId": entity_id,
            "actor": actor,
            "success": success,
            "oldVersion": old_version,
            "newVersion": new_version,
            "changes": scrub(dict(changes)) if changes else None,
            "details": scrub(dict(details)) if details else None,
            "sourceIp": source_ip,
            "userAgent": user_agent,
        }
        try:
            self.collection.insert_one(dict(record))
        except Exception as exc:
            log.error("audit.mongo_write_failed", error=str(exc), action=action, entity_id=entity_id)
        if self.metrics is not None:
            try:
                self.metrics.record_audit(record)
            except Exception as exc:
                log.warning("audit.jdbc_write_failed", error=str(exc))
        log.info(
            "audit",
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            actor=actor,
            success=success,
        )

    def query(
        self,
        *,
        entity_type: str | None = None,
        entity_id: str | None = None,
        actor: str | None = None,
        action: str | None = None,
        limit: int = 200,
        skip: int = 0,
    ) -> list[dict[str, Any]]:
        query: dict[str, Any] = {}
        if entity_type:
            query["entityType"] = entity_type
        if entity_id:
            query["entityId"] = entity_id
        if actor:
            query["actor"] = actor
        if action:
            query["action"] = action
        cursor = self.collection.find(query, {"_id": False}).sort("timestamp", -1).skip(skip).limit(limit)
        return list(cursor)
