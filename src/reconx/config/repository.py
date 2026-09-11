"""MongoDB repositories for definitions, connections and runs.

Versioning contract
-------------------
* ``reconciliation_definitions`` holds exactly one *head* document per
  ``reconId`` - the version the platform executes.
* ``reconciliation_versions`` is append-only: every save writes a new,
  immutable version document.  Nothing is ever overwritten destructively, so
  rollback is simply "publish version N again as version N+1".
* An ACTIVE definition can never be silently mutated: saving over an ACTIVE
  head creates a new version and requires an explicit activation to take
  effect (``activate_version``).
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pymongo import ReturnDocument
from pymongo.database import Database
from pymongo.errors import DuplicateKeyError

from reconx.common.errors import ConflictError, NotFoundError, ValidationError
from reconx.common.ids import idempotency_key
from reconx.common.logging import get_logger
from reconx.common.timeutils import utcnow
from reconx.config.connections import SECRET_FIELDS, ConnectionDefinition
from reconx.config.enums import DefinitionStatus, RunStatus, TriggerType
from reconx.config.models import ReconciliationDefinition
from reconx.config.store import Collections
from reconx.security.audit import AuditAction, AuditLogger, diff_documents

log = get_logger(__name__)


def _as_datetime(value: Any) -> datetime | None:
    """Coerce a stored timestamp back to a datetime (documents may hold ISO strings)."""
    if value is None or isinstance(value, datetime):
        return value
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:  # pragma: no cover - defensive
        return None


def _without_id(document: dict[str, Any] | None) -> dict[str, Any] | None:
    """Drop MongoDB's ``_id`` from a returned document.

    Done in code rather than with a projection: ``find_one_and_update`` with an
    ``_id``-excluding projection behaves inconsistently across MongoDB drivers
    and in-memory doubles, and the field is never part of our domain model.
    """
    if document is None:
        return None
    return {k: v for k, v in document.items() if k != "_id"}


_EDITABLE_STATUSES = {DefinitionStatus.DRAFT, DefinitionStatus.ACTIVE, DefinitionStatus.DISABLED}


class ReconciliationRepository:
    """Versioned CRUD for reconciliation definitions."""

    def __init__(self, database: Database, audit: AuditLogger | None = None) -> None:
        self.db = database
        self.audit = audit or AuditLogger(database)

    # ---------------------------------------------------------------- read
    def get(self, recon_id: str, *, version: int | None = None) -> ReconciliationDefinition:
        doc = self.get_raw(recon_id, version=version)
        return ReconciliationDefinition.model_validate(doc)

    def get_raw(self, recon_id: str, *, version: int | None = None) -> dict[str, Any]:
        if version is None:
            doc = self.db[Collections.DEFINITIONS].find_one({"reconId": recon_id}, {"_id": False})
        else:
            doc = self.db[Collections.VERSIONS].find_one(
                {"reconId": recon_id, "version": version}, {"_id": False}
            )
        if not doc:
            suffix = f" version {version}" if version else ""
            raise NotFoundError(f"Reconciliation '{recon_id}'{suffix} not found")
        return doc

    def find_optional(self, recon_id: str) -> ReconciliationDefinition | None:
        doc = self.db[Collections.DEFINITIONS].find_one({"reconId": recon_id}, {"_id": False})
        return ReconciliationDefinition.model_validate(doc) if doc else None

    def list(
        self,
        *,
        status: str | None = None,
        product: str | None = None,
        customer: str | None = None,
        environment: str | None = None,
        enabled: bool | None = None,
        tag: str | None = None,
        search: str | None = None,
        limit: int = 200,
        skip: int = 0,
    ) -> list[dict[str, Any]]:
        query: dict[str, Any] = {}
        if status:
            query["status"] = status
        if product:
            query["product"] = product
        if customer:
            query["customer"] = customer
        if environment:
            query["environment"] = environment
        if enabled is not None:
            query["enabled"] = enabled
        if tag:
            query["tags"] = tag
        if search:
            query["$or"] = [
                {"reconId": {"$regex": search, "$options": "i"}},
                {"name": {"$regex": search, "$options": "i"}},
                {"description": {"$regex": search, "$options": "i"}},
            ]
        cursor = (
            self.db[Collections.DEFINITIONS]
            .find(query, {"_id": False})
            .sort("updatedAt", -1)
            .skip(skip)
            .limit(limit)
        )
        return list(cursor)

    def count(self, **filters: Any) -> int:
        query = {k: v for k, v in filters.items() if v is not None}
        return self.db[Collections.DEFINITIONS].count_documents(query)

    def list_versions(self, recon_id: str, *, limit: int = 100) -> list[dict[str, Any]]:
        cursor = (
            self.db[Collections.VERSIONS]
            .find({"reconId": recon_id}, {"_id": False})
            .sort("version", -1)
            .limit(limit)
        )
        return list(cursor)

    def list_active(self) -> list[ReconciliationDefinition]:
        docs = self.db[Collections.DEFINITIONS].find(
            {"status": DefinitionStatus.ACTIVE.value, "enabled": True}, {"_id": False}
        )
        out: list[ReconciliationDefinition] = []
        for doc in docs:
            try:
                out.append(ReconciliationDefinition.model_validate(doc))
            except Exception as exc:
                log.error("repository.invalid_definition", recon_id=doc.get("reconId"), error=str(exc))
        return out

    # --------------------------------------------------------------- write
    def create(self, definition: ReconciliationDefinition, *, actor: str) -> ReconciliationDefinition:
        existing = self.db[Collections.DEFINITIONS].find_one({"reconId": definition.recon_id})
        if existing:
            raise ConflictError(f"Reconciliation '{definition.recon_id}' already exists")
        now = utcnow()
        doc = definition.model_copy(
            update={
                "version": 1,
                "status": definition.status or DefinitionStatus.DRAFT,
                "created_at": now,
                "created_by": actor,
                "updated_at": now,
                "updated_by": actor,
            }
        ).dump()
        try:
            self.db[Collections.DEFINITIONS].insert_one(dict(doc))
        except DuplicateKeyError as exc:
            raise ConflictError(f"Reconciliation '{definition.recon_id}' already exists") from exc
        self.db[Collections.VERSIONS].insert_one(dict(doc))
        self.audit.record(
            action=AuditAction.CREATE,
            entity_type="reconciliation",
            entity_id=definition.recon_id,
            actor=actor,
            new_version=1,
        )
        return ReconciliationDefinition.model_validate(doc)

    def save_new_version(
        self,
        definition: ReconciliationDefinition,
        *,
        actor: str,
        comment: str | None = None,
        expected_version: int | None = None,
        activate: bool = False,
    ) -> ReconciliationDefinition:
        """Append a new immutable version.  The previous version is untouched."""
        current = self.get_raw(definition.recon_id)
        current_version = int(current.get("version", 1))
        if expected_version is not None and expected_version != current_version:
            raise ConflictError(
                f"Concurrent modification: expected version {expected_version}, "
                f"current is {current_version}",
                details={"currentVersion": current_version},
            )
        current_status = DefinitionStatus(current.get("status", DefinitionStatus.DRAFT.value))
        if current_status == DefinitionStatus.ARCHIVED:
            raise ConflictError("Archived reconciliations cannot be modified; clone it instead")

        new_version = current_version + 1
        now = utcnow()
        # A new version of an ACTIVE definition stays DRAFT until explicitly activated,
        # so an operator can never accidentally change what production is executing.
        status = (
            DefinitionStatus.ACTIVE
            if activate
            else (DefinitionStatus.DRAFT if current_status == DefinitionStatus.ACTIVE else current_status)
        )
        doc = definition.model_copy(
            update={
                "version": new_version,
                "status": status,
                "created_at": _as_datetime(current.get("createdAt")),
                "created_by": current.get("createdBy"),
                "updated_at": now,
                "updated_by": actor,
                "change_comment": comment,
                "activated_at": now if activate else None,
                "activated_by": actor if activate else None,
            }
        ).dump()
        self.db[Collections.VERSIONS].insert_one(dict(doc))
        if activate or current_status != DefinitionStatus.ACTIVE:
            self.db[Collections.DEFINITIONS].replace_one({"reconId": definition.recon_id}, dict(doc))
        else:
            # Keep executing the active head, but track that a newer draft exists.
            self.db[Collections.DEFINITIONS].update_one(
                {"reconId": definition.recon_id},
                {"$set": {"latestDraftVersion": new_version, "updatedAt": now, "updatedBy": actor}},
            )
        self.audit.record(
            action=AuditAction.UPDATE,
            entity_type="reconciliation",
            entity_id=definition.recon_id,
            actor=actor,
            old_version=current_version,
            new_version=new_version,
            changes=diff_documents(current, doc),
            details={"comment": comment, "activated": activate},
        )
        log.info(
            "repository.version_saved",
            recon_id=definition.recon_id,
            version=new_version,
            status=str(status),
            activated=activate,
        )
        return ReconciliationDefinition.model_validate(doc)

    def activate_version(
        self, recon_id: str, version: int | None = None, *, actor: str
    ) -> ReconciliationDefinition:
        """Promote a version to ACTIVE (the version the scheduler executes)."""
        current = self.get_raw(recon_id)
        target = self.get_raw(recon_id, version=version) if version else current
        status = DefinitionStatus(target.get("status", DefinitionStatus.DRAFT.value))
        if status == DefinitionStatus.ARCHIVED:
            raise ConflictError("Cannot activate an archived version")
        now = utcnow()
        doc = {
            **target,
            "status": DefinitionStatus.ACTIVE.value,
            "enabled": True,
            "activatedAt": now,
            "activatedBy": actor,
            "updatedAt": now,
            "updatedBy": actor,
        }
        self.db[Collections.DEFINITIONS].replace_one({"reconId": recon_id}, dict(doc), upsert=True)
        self.db[Collections.VERSIONS].update_one(
            {"reconId": recon_id, "version": doc["version"]},
            {"$set": {"status": DefinitionStatus.ACTIVE.value, "activatedAt": now, "activatedBy": actor}},
        )
        self.audit.record(
            action=AuditAction.ACTIVATE,
            entity_type="reconciliation",
            entity_id=recon_id,
            actor=actor,
            old_version=int(current.get("version", 1)),
            new_version=int(doc["version"]),
        )
        return ReconciliationDefinition.model_validate(doc)

    def rollback(self, recon_id: str, version: int, *, actor: str, comment: str | None = None) -> ReconciliationDefinition:
        """Republish a historical version as a brand-new version.

        History is never rewritten - rolling back to v3 creates v(N+1) whose
        content equals v3, which keeps the audit trail linear and honest.
        """
        historical = self.get_raw(recon_id, version=version)
        current = self.get_raw(recon_id)
        current_version = int(current.get("version", 1))
        if version == current_version:
            raise ConflictError(f"Version {version} is already the current version")
        payload = {
            k: v
            for k, v in historical.items()
            if k not in {"version", "status", "updatedAt", "updatedBy", "activatedAt", "activatedBy"}
        }
        definition = ReconciliationDefinition.model_validate(payload)
        restored = self.save_new_version(
            definition,
            actor=actor,
            comment=comment or f"Rollback to version {version}",
            activate=DefinitionStatus(current.get("status")) == DefinitionStatus.ACTIVE,
        )
        self.audit.record(
            action=AuditAction.ROLLBACK,
            entity_type="reconciliation",
            entity_id=recon_id,
            actor=actor,
            old_version=current_version,
            new_version=restored.version,
            details={"rolledBackTo": version},
        )
        return restored

    def set_status(
        self, recon_id: str, status: DefinitionStatus, *, actor: str, enabled: bool | None = None
    ) -> ReconciliationDefinition:
        current = self.get_raw(recon_id)
        update: dict[str, Any] = {"status": status.value, "updatedAt": utcnow(), "updatedBy": actor}
        if enabled is not None:
            update["enabled"] = enabled
        elif status == DefinitionStatus.DISABLED:
            update["enabled"] = False
        elif status == DefinitionStatus.ACTIVE:
            update["enabled"] = True
        doc = _without_id(
            self.db[Collections.DEFINITIONS].find_one_and_update(
                {"reconId": recon_id}, {"$set": update}, return_document=ReturnDocument.AFTER
            )
        )
        action = {
            DefinitionStatus.ACTIVE: AuditAction.ACTIVATE,
            DefinitionStatus.DISABLED: AuditAction.DISABLE,
            DefinitionStatus.ARCHIVED: AuditAction.ARCHIVE,
        }.get(status, AuditAction.UPDATE)
        self.audit.record(
            action=action,
            entity_type="reconciliation",
            entity_id=recon_id,
            actor=actor,
            old_version=int(current.get("version", 1)),
            new_version=int(current.get("version", 1)),
            details={"status": status.value},
        )
        return ReconciliationDefinition.model_validate(doc)

    def clone(
        self, recon_id: str, new_id: str, *, actor: str, new_name: str | None = None
    ) -> ReconciliationDefinition:
        source = self.get_raw(recon_id)
        payload = {
            k: v
            for k, v in source.items()
            if k
            not in {
                "version",
                "status",
                "createdAt",
                "createdBy",
                "updatedAt",
                "updatedBy",
                "activatedAt",
                "activatedBy",
                "latestDraftVersion",
            }
        }
        payload["reconId"] = new_id
        payload["name"] = new_name or f"{source.get('name')} (copy)"
        payload["status"] = DefinitionStatus.DRAFT.value
        definition = ReconciliationDefinition.model_validate(payload)
        created = self.create(definition, actor=actor)
        self.audit.record(
            action=AuditAction.CREATE,
            entity_type="reconciliation",
            entity_id=new_id,
            actor=actor,
            details={"clonedFrom": recon_id},
        )
        return created

    def archive(self, recon_id: str, *, actor: str) -> ReconciliationDefinition:
        return self.set_status(recon_id, DefinitionStatus.ARCHIVED, actor=actor, enabled=False)

    def distinct(self, field: str) -> list[str]:
        return sorted(v for v in self.db[Collections.DEFINITIONS].distinct(field) if v)


class ConnectionRepository:
    """CRUD for connections with automatic secret encryption on write."""

    def __init__(self, database: Database, audit: AuditLogger | None = None, resolver: Any | None = None) -> None:
        self.db = database
        self.audit = audit or AuditLogger(database)
        if resolver is None:
            from reconx.security.secrets import get_secret_resolver

            resolver = get_secret_resolver()
        self.resolver = resolver

    def _encrypt_secrets(self, config: dict[str, Any], previous: dict[str, Any] | None = None) -> dict[str, Any]:
        """Encrypt new secrets; keep the stored value when the UI sends the mask."""
        out = dict(config)
        for field in SECRET_FIELDS:
            value = out.get(field)
            if value is None or value == "":
                continue
            if value == "********":
                if previous and field in previous:
                    out[field] = previous[field]
                else:
                    out.pop(field, None)
                continue
            if isinstance(value, str):
                out[field] = self.resolver.encrypt_for_storage(value)
        return out

    def create(self, connection: ConnectionDefinition, *, actor: str) -> ConnectionDefinition:
        if self.db[Collections.CONNECTIONS].find_one({"connectionId": connection.connection_id}):
            raise ConflictError(f"Connection '{connection.connection_id}' already exists")
        now = utcnow()
        doc = connection.model_copy(
            update={"created_at": now, "created_by": actor, "updated_at": now, "updated_by": actor}
        ).dump()
        doc["config"] = self._encrypt_secrets(doc.get("config", {}))
        self.db[Collections.CONNECTIONS].insert_one(dict(doc))
        self.audit.record(
            action=AuditAction.CREATE,
            entity_type="connection",
            entity_id=connection.connection_id,
            actor=actor,
            details={"type": str(connection.type)},
        )
        return ConnectionDefinition.model_validate(doc)

    def update(self, connection: ConnectionDefinition, *, actor: str) -> ConnectionDefinition:
        current = self.get_raw(connection.connection_id)
        doc = connection.model_copy(
            update={
                "created_at": _as_datetime(current.get("createdAt")),
                "created_by": current.get("createdBy"),
                "updated_at": utcnow(),
                "updated_by": actor,
            }
        ).dump()
        doc["config"] = self._encrypt_secrets(doc.get("config", {}), current.get("config", {}))
        self.db[Collections.CONNECTIONS].replace_one({"connectionId": connection.connection_id}, dict(doc))
        self.audit.record(
            action=AuditAction.UPDATE,
            entity_type="connection",
            entity_id=connection.connection_id,
            actor=actor,
            changes=diff_documents(current, doc),
        )
        return ConnectionDefinition.model_validate(doc)

    def get(self, connection_id: str) -> ConnectionDefinition:
        return ConnectionDefinition.model_validate(self.get_raw(connection_id))

    def get_raw(self, connection_id: str) -> dict[str, Any]:
        doc = self.db[Collections.CONNECTIONS].find_one({"connectionId": connection_id}, {"_id": False})
        if not doc:
            raise NotFoundError(f"Connection '{connection_id}' not found")
        return doc

    def find_optional(self, connection_id: str) -> ConnectionDefinition | None:
        doc = self.db[Collections.CONNECTIONS].find_one({"connectionId": connection_id}, {"_id": False})
        return ConnectionDefinition.model_validate(doc) if doc else None

    def list(
        self, *, conn_type: str | None = None, environment: str | None = None, enabled: bool | None = None
    ) -> list[ConnectionDefinition]:
        query: dict[str, Any] = {}
        if conn_type:
            query["type"] = conn_type
        if environment:
            query["environment"] = environment
        if enabled is not None:
            query["enabled"] = enabled
        return [
            ConnectionDefinition.model_validate(doc)
            for doc in self.db[Collections.CONNECTIONS].find(query, {"_id": False}).sort("connectionId", 1)
        ]

    def delete(self, connection_id: str, *, actor: str) -> None:
        in_use = self.db[Collections.DEFINITIONS].find_one(
            {
                "$or": [
                    {"legs.sources.connectionRef": connection_id},
                    {"legs.outputs.connectionRef": connection_id},
                ]
            },
            {"reconId": True},
        )
        if in_use:
            raise ConflictError(
                f"Connection '{connection_id}' is referenced by reconciliation '{in_use['reconId']}'"
            )
        result = self.db[Collections.CONNECTIONS].delete_one({"connectionId": connection_id})
        if result.deleted_count == 0:
            raise NotFoundError(f"Connection '{connection_id}' not found")
        self.audit.record(
            action=AuditAction.DELETE, entity_type="connection", entity_id=connection_id, actor=actor
        )

    def record_test_result(self, connection_id: str, *, success: bool, message: str, actor: str) -> None:
        self.db[Collections.CONNECTIONS].update_one(
            {"connectionId": connection_id},
            {
                "$set": {
                    "lastTestedAt": utcnow(),
                    "lastTestResult": ("SUCCESS: " if success else "FAILED: ") + message[:500],
                }
            },
        )
        self.audit.record(
            action=AuditAction.TEST,
            entity_type="connection",
            entity_id=connection_id,
            actor=actor,
            success=success,
            details={"message": message[:500]},
        )


class RunRepository:
    """Run lifecycle state - the source of truth for the control plane."""

    def __init__(self, database: Database) -> None:
        self.db = database

    def create(
        self,
        *,
        run_id: str,
        definition: ReconciliationDefinition,
        trigger_type: TriggerType,
        triggered_by: str,
        business_date: str,
        parameters: dict[str, Any] | None = None,
        node: str | None = None,
        idem_key: str | None = None,
        status: RunStatus = RunStatus.QUEUED,
    ) -> dict[str, Any]:
        key = idem_key or idempotency_key(
            definition.recon_id,
            definition.version,
            {
                dim: (parameters or {}).get(dim, business_date if dim == "business_date" else None)
                for dim in definition.idempotency_dimensions
            },
        )
        doc: dict[str, Any] = {
            "runId": run_id,
            "reconId": definition.recon_id,
            "reconName": definition.name,
            "version": definition.version,
            "product": definition.product,
            "customer": definition.customer,
            "environment": definition.environment,
            "status": status.value,
            "triggerType": trigger_type.value,
            "triggeredBy": triggered_by,
            "businessDate": business_date,
            "parameters": parameters or {},
            "idempotencyKey": key,
            "node": node,
            "createdAt": utcnow(),
            "startTime": None,
            "endTime": None,
            "durationMs": None,
            "sparkApplicationId": None,
            "metrics": {},
            "legs": [],
            "attempt": 1,
            "errorMessage": None,
        }
        try:
            self.db[Collections.RUNS].insert_one(dict(doc))
        except DuplicateKeyError as exc:
            existing = self.db[Collections.RUNS].find_one({"idempotencyKey": key}, {"_id": False})
            from reconx.common.errors import DuplicateRunError

            raise DuplicateRunError(
                f"A run for '{definition.recon_id}' with the same business dimensions already exists",
                details={"existingRunId": (existing or {}).get("runId"), "idempotencyKey": key},
            ) from exc
        return doc

    def get(self, run_id: str) -> dict[str, Any]:
        doc = self.db[Collections.RUNS].find_one({"runId": run_id}, {"_id": False})
        if not doc:
            raise NotFoundError(f"Run '{run_id}' not found")
        return doc

    def find_optional(self, run_id: str) -> dict[str, Any] | None:
        return self.db[Collections.RUNS].find_one({"runId": run_id}, {"_id": False})

    def update_status(
        self,
        run_id: str,
        status: RunStatus,
        *,
        error: str | None = None,
        spark_application_id: str | None = None,
        metrics: dict[str, Any] | None = None,
        extra: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        update: dict[str, Any] = {"status": status.value, "updatedAt": utcnow()}
        if status == RunStatus.RUNNING:
            update["startTime"] = utcnow()
        if status.is_terminal:
            update["endTime"] = utcnow()
        if error is not None:
            update["errorMessage"] = error[:4000]
        if spark_application_id:
            update["sparkApplicationId"] = spark_application_id
        if metrics:
            update["metrics"] = metrics
        if extra:
            update.update(extra)
        doc = _without_id(
            self.db[Collections.RUNS].find_one_and_update(
                {"runId": run_id}, {"$set": update}, return_document=ReturnDocument.AFTER
            )
        )
        if not doc:
            raise NotFoundError(f"Run '{run_id}' not found")
        if status.is_terminal and doc.get("startTime"):
            duration = int((doc["endTime"] - doc["startTime"]).total_seconds() * 1000)
            self.db[Collections.RUNS].update_one({"runId": run_id}, {"$set": {"durationMs": duration}})
            doc["durationMs"] = duration
        return doc

    def upsert_leg(self, run_id: str, leg: dict[str, Any]) -> None:
        self.db[Collections.LEG_RUNS].update_one(
            {"runId": run_id, "legId": leg["legId"]},
            {"$set": {**leg, "runId": run_id, "updatedAt": utcnow()}},
            upsert=True,
        )

    def list_legs(self, run_id: str) -> list[dict[str, Any]]:
        return list(self.db[Collections.LEG_RUNS].find({"runId": run_id}, {"_id": False}).sort("legId", 1))

    def list(
        self,
        *,
        recon_id: str | None = None,
        status: str | list[str] | None = None,
        product: str | None = None,
        customer: str | None = None,
        business_date: str | None = None,
        since: datetime | None = None,
        limit: int = 100,
        skip: int = 0,
    ) -> list[dict[str, Any]]:
        query: dict[str, Any] = {}
        if recon_id:
            query["reconId"] = recon_id
        if status:
            query["status"] = {"$in": status} if isinstance(status, list) else status
        if product:
            query["product"] = product
        if customer:
            query["customer"] = customer
        if business_date:
            query["businessDate"] = business_date
        if since:
            query["createdAt"] = {"$gte": since}
        cursor = (
            self.db[Collections.RUNS]
            .find(query, {"_id": False})
            .sort("createdAt", -1)
            .skip(skip)
            .limit(limit)
        )
        return list(cursor)

    def count_active(self, recon_id: str) -> int:
        return self.db[Collections.RUNS].count_documents(
            {
                "reconId": recon_id,
                "status": {
                    "$in": [
                        RunStatus.QUEUED.value,
                        RunStatus.STARTING.value,
                        RunStatus.RUNNING.value,
                        RunStatus.WAITING_FOR_DATA.value,
                    ]
                },
            }
        )

    def last_successful(self, recon_id: str) -> dict[str, Any] | None:
        return self.db[Collections.RUNS].find_one(
            {"reconId": recon_id, "status": {"$in": [RunStatus.SUCCESS.value, RunStatus.PARTIAL_SUCCESS.value]}},
            {"_id": False},
            sort=[("createdAt", -1)],
        )

    def last_run(self, recon_id: str) -> dict[str, Any] | None:
        return self.db[Collections.RUNS].find_one(
            {"reconId": recon_id}, {"_id": False}, sort=[("createdAt", -1)]
        )

    def claim_queued(self, node: str, limit: int = 5) -> list[dict[str, Any]]:
        """Atomically claim QUEUED runs for execution on this node."""
        claimed: list[dict[str, Any]] = []
        for _ in range(limit):
            doc = _without_id(
                self.db[Collections.RUNS].find_one_and_update(
                    {"status": RunStatus.QUEUED.value},
                    {"$set": {"status": RunStatus.STARTING.value, "node": node, "claimedAt": utcnow()}},
                    sort=[("createdAt", 1)],
                    return_document=ReturnDocument.AFTER,
                )
            )
            if not doc:
                break
            claimed.append(doc)
        return claimed

    def statistics(self, *, since: datetime | None = None, **filters: Any) -> dict[str, Any]:
        match: dict[str, Any] = {k: v for k, v in filters.items() if v is not None}
        if since:
            match["createdAt"] = {"$gte": since}
        pipeline: list[dict[str, Any]] = [
            {"$match": match},
            {
                "$group": {
                    "_id": "$status",
                    "count": {"$sum": 1},
                    "avgDuration": {"$avg": "$durationMs"},
                    "recordsRead": {"$sum": "$metrics.recordsRead"},
                    "matched": {"$sum": "$metrics.recordsMatched"},
                    "unmatched": {"$sum": "$metrics.recordsUnmatched"},
                    "exceptions": {"$sum": "$metrics.exceptions"},
                }
            },
        ]
        by_status = {row["_id"]: row for row in self.db[Collections.RUNS].aggregate(pipeline)}
        total = sum(row["count"] for row in by_status.values())
        matched = sum(row.get("matched") or 0 for row in by_status.values())
        read = sum(row.get("recordsRead") or 0 for row in by_status.values())
        durations = [row["avgDuration"] for row in by_status.values() if row.get("avgDuration")]
        return {
            "total": total,
            "byStatus": {k: v["count"] for k, v in by_status.items()},
            "recordsRead": read,
            "recordsMatched": matched,
            "recordsUnmatched": sum(row.get("unmatched") or 0 for row in by_status.values()),
            "exceptions": sum(row.get("exceptions") or 0 for row in by_status.values()),
            "matchPercentage": round(matched / read * 100, 4) if read else None,
            "avgDurationMs": int(sum(durations) / len(durations)) if durations else None,
        }


def validate_unique_source_ids(definition: ReconciliationDefinition) -> None:
    for leg in definition.legs:
        ids = [s.id for s in leg.sources]
        if len(set(ids)) != len(ids):
            raise ValidationError(f"Leg '{leg.id}' has duplicate source ids")
