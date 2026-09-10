"""Metrics repository - persistence and historical reporting over JDBC.

The control plane and the Spark driver both write here.  Every write is
best-effort-with-retry and never silently swallows an error: failures are
logged with context and re-raised as
:class:`~reconx.common.errors.MetricsPersistenceError` so the caller decides
whether the run fails.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping
from datetime import datetime, timedelta
from typing import Any

from sqlalchemy import Engine, create_engine, delete, func, select, text
from sqlalchemy.exc import SQLAlchemyError

from reconx.common.errors import MetricsPersistenceError, NotFoundError
from reconx.common.logging import get_logger
from reconx.common.retry import RetryPolicy, call_with_retry
from reconx.common.timeutils import utcnow
from reconx.config.settings import Settings, get_settings
from reconx.metrics.models import (
    ALL_TABLES,
    audit_log,
    metadata,
    reconciliation_definition,
    reconciliation_exception_comment,
    reconciliation_exceptions,
    reconciliation_field_metrics,
    reconciliation_leg_run,
    reconciliation_metrics,
    reconciliation_run,
    reconciliation_source_metrics,
    scheduler_execution,
)

log = get_logger(__name__)


class MetricsRepository:
    """Reads and writes the reconciliation metrics database."""

    def __init__(self, engine: Engine | None = None, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self._engine = engine
        self.retry_policy = RetryPolicy(max_attempts=3, initial_delay_seconds=1.0)

    @property
    def engine(self) -> Engine:
        if self._engine is None:
            url = self.settings.result_db.resolved_sqlalchemy_url()
            self._engine = create_engine(
                url,
                pool_pre_ping=True,
                pool_size=self.settings.result_db.pool_size,
                max_overflow=self.settings.result_db.pool_size,
                future=True,
            )
        return self._engine

    # ------------------------------------------------------------- lifecycle
    def create_schema(self) -> list[str]:
        """Create every table if absent.  Idempotent."""
        try:
            metadata.create_all(self.engine, checkfirst=True)
        except SQLAlchemyError as exc:
            raise MetricsPersistenceError(f"Could not create the metrics schema: {exc}") from exc
        log.info("metrics.schema_created", tables=len(ALL_TABLES))
        return [table.name for table in ALL_TABLES]

    def ping(self) -> dict[str, Any]:
        with self.engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"ok": True, "dialect": self.engine.dialect.name}

    def close(self) -> None:
        if self._engine is not None:
            self._engine.dispose()
            self._engine = None

    # ----------------------------------------------------------------- write
    def _execute(self, statement: Any, operation: str, params: Any = None) -> Any:
        def _run() -> Any:
            with self.engine.begin() as connection:
                return connection.execute(statement, params) if params else connection.execute(statement)

        try:
            return call_with_retry(_run, policy=self.retry_policy, operation=operation)
        except SQLAlchemyError as exc:
            log.error("metrics.write_failed", operation=operation, error=str(exc)[:600])
            raise MetricsPersistenceError(f"{operation} failed: {exc}") from exc

    def upsert_definition(self, definition: Mapping[str, Any]) -> None:
        recon_id = definition.get("reconId")
        version = int(definition.get("version", 1))
        row = {
            "recon_id": recon_id,
            "version": version,
            "name": definition.get("name"),
            "description": definition.get("description"),
            "product": definition.get("product"),
            "customer": definition.get("customer"),
            "environment": definition.get("environment"),
            "status": definition.get("status", "DRAFT"),
            "enabled": bool(definition.get("enabled", True)),
            "owner": definition.get("owner"),
            "leg_count": len(definition.get("legs", []) or []),
            "schedule_type": (definition.get("schedule") or {}).get("type"),
            "schedule_expression": (definition.get("schedule") or {}).get("expression"),
            "definition_json": json.dumps(definition, default=str)[:1_000_000],
            "created_by": definition.get("createdBy"),
            "created_at": _as_datetime(definition.get("createdAt")),
            "updated_by": definition.get("updatedBy"),
            "updated_at": _as_datetime(definition.get("updatedAt")) or utcnow(),
        }
        self._execute(
            delete(reconciliation_definition).where(
                (reconciliation_definition.c.recon_id == recon_id)
                & (reconciliation_definition.c.version == version)
            ),
            "definition.delete_existing",
        )
        self._execute(reconciliation_definition.insert().values(**row), "definition.insert")

    def record_run_start(self, run: Mapping[str, Any]) -> None:
        row = {
            "run_id": run["runId"],
            "recon_id": run["reconId"],
            "recon_name": run.get("reconName"),
            "version": int(run.get("version", 1)),
            "product": run.get("product"),
            "customer": run.get("customer"),
            "environment": run.get("environment"),
            "business_date": run.get("businessDate"),
            "status": run.get("status", "RUNNING"),
            "trigger_type": run.get("triggerType"),
            "triggered_by": run.get("triggeredBy"),
            "node": run.get("node"),
            "spark_application_id": run.get("sparkApplicationId"),
            "idempotency_key": run.get("idempotencyKey"),
            "attempt": int(run.get("attempt", 1)),
            "start_time": _as_datetime(run.get("startTime")) or utcnow(),
            "created_at": utcnow(),
        }
        existing = self._execute(
            select(reconciliation_run.c.run_id).where(reconciliation_run.c.run_id == row["run_id"]),
            "run.exists",
        ).first()
        if existing:
            self.update_run(row["run_id"], row)
            return
        self._execute(reconciliation_run.insert().values(**row), "run.insert")

    def update_run(self, run_id: str, values: Mapping[str, Any]) -> None:
        payload = {k: v for k, v in values.items() if k != "run_id" and k in reconciliation_run.c}
        if not payload:
            return
        self._execute(
            reconciliation_run.update().where(reconciliation_run.c.run_id == run_id).values(**payload),
            "run.update",
        )

    def record_run_completion(
        self,
        run_id: str,
        *,
        status: str,
        metrics: Mapping[str, Any] | None = None,
        error: str | None = None,
        spark_application_id: str | None = None,
        end_time: datetime | None = None,
    ) -> None:
        metrics = metrics or {}
        end = end_time or utcnow()
        values: dict[str, Any] = {
            "status": status,
            "end_time": end,
            "error_message": (error or "")[:4000] or None,
            "records_read": int(metrics.get("recordsRead", 0) or 0),
            "records_written": int(metrics.get("recordsWritten", 0) or 0),
            "records_matched": int(metrics.get("recordsMatched", 0) or 0),
            "records_unmatched": int(metrics.get("recordsUnmatched", 0) or 0),
            "duplicates": int(metrics.get("duplicates", 0) or 0),
            "exceptions": int(metrics.get("exceptions", 0) or 0),
            "field_mismatches": int(metrics.get("fieldMismatches", 0) or 0),
            "match_percentage": metrics.get("matchPercentage"),
            "read_time_ms": int(metrics.get("readTimeMs", 0) or 0),
            "process_time_ms": int(metrics.get("processTimeMs", 0) or 0),
            "write_time_ms": int(metrics.get("writeTimeMs", 0) or 0),
            "spark_time_ms": int(metrics.get("sparkTimeMs", 0) or 0),
        }
        if spark_application_id:
            values["spark_application_id"] = spark_application_id
        row = self._execute(
            select(reconciliation_run.c.start_time).where(reconciliation_run.c.run_id == run_id),
            "run.start_time",
        ).first()
        if row and row[0]:
            start = row[0]
            if start.tzinfo is None:
                start = start.replace(tzinfo=end.tzinfo)
            values["duration_ms"] = int((end - start).total_seconds() * 1000)
        self.update_run(run_id, values)

    def record_leg_run(self, leg: Mapping[str, Any]) -> None:
        payload = {k: v for k, v in leg.items() if k in reconciliation_leg_run.c}
        self._execute(
            delete(reconciliation_leg_run).where(
                (reconciliation_leg_run.c.run_id == leg["run_id"])
                & (reconciliation_leg_run.c.leg_id == leg["leg_id"])
            ),
            "leg_run.delete_existing",
        )
        self._execute(reconciliation_leg_run.insert().values(**payload), "leg_run.insert")

    def record_metrics(self, rows: Iterable[Mapping[str, Any]]) -> int:
        payload = [
            {
                "run_id": row["run_id"],
                "recon_id": row["recon_id"],
                "leg_id": row.get("leg_id"),
                "metric_name": row["metric_name"],
                "metric_value": row.get("metric_value"),
                "metric_text": (str(row["metric_text"])[:1024] if row.get("metric_text") else None),
                "metric_type": row.get("metric_type", "COUNTER"),
                "business_date": row.get("business_date"),
                "recorded_at": utcnow(),
            }
            for row in rows
        ]
        if not payload:
            return 0
        self._execute(reconciliation_metrics.insert(), "metrics.insert", payload)
        return len(payload)

    def record_field_metrics(self, rows: Iterable[Mapping[str, Any]]) -> int:
        payload = []
        for row in rows:
            compared = int(row.get("comparedCount", 0) or 0)
            mismatch = int(row.get("mismatchCount", 0) or 0)
            payload.append(
                {
                    "run_id": row["runId"],
                    "recon_id": row["reconId"],
                    "leg_id": row["legId"],
                    "rule_id": row.get("ruleId"),
                    "rule_name": row.get("ruleName"),
                    "field_name": row.get("fieldName"),
                    "compared_count": compared,
                    "mismatch_count": mismatch,
                    "mismatch_percentage": round(mismatch / compared * 100, 4) if compared else None,
                    "created_at": utcnow(),
                }
            )
        if not payload:
            return 0
        self._execute(reconciliation_field_metrics.insert(), "field_metrics.insert", payload)
        return len(payload)

    def record_source_metrics(self, rows: Iterable[Mapping[str, Any]]) -> int:
        payload = [
            {
                "run_id": row["runId"],
                "recon_id": row["reconId"],
                "leg_id": row["legId"],
                "source_id": row["sourceId"],
                "source_type": row.get("sourceType"),
                "connection_ref": row.get("connectionRef"),
                "records_read": row.get("recordsRead"),
                "column_count": row.get("columnCount"),
                "read_time_ms": row.get("readTimeMs"),
                "data_quality_passed": row.get("dataQualityPassed"),
                "data_quality_details": json.dumps(row.get("dataQualityDetails"), default=str)[:200_000]
                if row.get("dataQualityDetails")
                else None,
                "schema_json": json.dumps(row.get("schema"), default=str)[:200_000]
                if row.get("schema")
                else None,
                "created_at": utcnow(),
            }
            for row in rows
        ]
        if not payload:
            return 0
        self._execute(reconciliation_source_metrics.insert(), "source_metrics.insert", payload)
        return len(payload)

    def record_exceptions(self, rows: Iterable[Mapping[str, Any]]) -> int:
        payload = [
            {
                "run_id": row["run_id"],
                "recon_id": row["recon_id"],
                "leg_id": row["leg_id"],
                "business_date": row.get("business_date"),
                "reconciliation_key": _truncate(row.get("reconciliation_key"), 1024),
                "exception_type": row.get("exception_type", "UNKNOWN"),
                "source": _truncate(row.get("source"), 128),
                "field": _truncate(row.get("field"), 256),
                "rule": _truncate(row.get("rule"), 256),
                "expected_value": _truncate(row.get("expected_value"), 2048),
                "actual_value": _truncate(row.get("actual_value"), 2048),
                "key_components": (
                    json.dumps(row.get("key_components"), default=str)
                    if isinstance(row.get("key_components"), (dict, list))
                    else _truncate(row.get("key_components"), 2048)
                ),
                "context_columns": (
                    json.dumps(row.get("context_columns"), default=str)
                    if isinstance(row.get("context_columns"), (dict, list))
                    else _truncate(row.get("context_columns"), 8000)
                ),
                "left_occurrences": row.get("left_occurrences"),
                "right_occurrences": row.get("right_occurrences"),
                "status": "OPEN",
                "created_at": utcnow(),
                "updated_at": utcnow(),
                "reopened_count": 0,
                "comment_count": 0,
            }
            for row in rows
        ]
        if not payload:
            return 0
        self._execute(reconciliation_exceptions.insert(), "exceptions.insert", payload)
        return len(payload)

    def record_audit(self, record: Mapping[str, Any]) -> None:
        self._execute(
            audit_log.insert().values(
                event_time=_as_datetime(record.get("timestamp")) or utcnow(),
                action=record.get("action", "UNKNOWN"),
                entity_type=record.get("entityType", "unknown"),
                entity_id=str(record.get("entityId", ""))[:256],
                actor=str(record.get("actor", "system"))[:128],
                success=bool(record.get("success", True)),
                old_version=record.get("oldVersion"),
                new_version=record.get("newVersion"),
                changes=json.dumps(record.get("changes"), default=str)[:200_000]
                if record.get("changes")
                else None,
                details=json.dumps(record.get("details"), default=str)[:200_000]
                if record.get("details")
                else None,
                source_ip=record.get("sourceIp"),
            ),
            "audit.insert",
        )

    def record_scheduler_execution(self, record: Mapping[str, Any]) -> None:
        self._execute(
            scheduler_execution.insert().values(
                recon_id=record["reconId"],
                node=record.get("node", "unknown"),
                scheduled_time=_as_datetime(record.get("scheduledTime")),
                fired_at=_as_datetime(record.get("firedAt")) or utcnow(),
                status=record.get("status", "UNKNOWN"),
                run_id=record.get("runId"),
                business_date=record.get("businessDate"),
                conditions_met=record.get("conditionsMet"),
                condition_detail=json.dumps(record.get("conditionDetail"), default=str)[:200_000]
                if record.get("conditionDetail")
                else None,
                message=_truncate(record.get("message"), 4000),
            ),
            "scheduler_execution.insert",
        )


    # --------------------------------------------------- exception workflow
    #: Statuses an exception can be in.  RESOLVED/CLOSED/WONT_FIX are terminal
    #: for reporting purposes; an officer can still reopen an exception.
    OPEN_STATUSES = ("OPEN", "INVESTIGATING", "REOPENED")
    CLOSED_STATUSES = ("RESOLVED", "CLOSED", "WONT_FIX", "FALSE_POSITIVE")

    def get_exception(self, exception_id: int) -> dict[str, Any] | None:
        with self.engine.connect() as connection:
            row = connection.execute(
                select(reconciliation_exceptions).where(reconciliation_exceptions.c.id == exception_id)
            ).first()
            return dict(row._mapping) if row else None

    def update_exception_status(
        self,
        exception_ids: Iterable[int],
        *,
        status: str,
        comment: str,
        actor: str,
        resolution_code: str | None = None,
        assigned_to: str | None = None,
    ) -> dict[str, Any]:
        """Close out (or reassign) one or more exceptions with an officer comment.

        The comment is mandatory: an exception that changes state without a
        reason is not auditable.  Every transition is recorded both on the
        exception row and as an immutable comment record.
        """
        ids = [int(i) for i in exception_ids]
        if not ids:
            return {"updated": 0, "ids": []}
        if not comment or not comment.strip():
            raise MetricsPersistenceError("A comment is required when changing an exception's status")
        status = status.upper()
        allowed = (*self.OPEN_STATUSES, *self.CLOSED_STATUSES)
        if status not in allowed:
            raise MetricsPersistenceError(
                f"Unknown exception status '{status}' (allowed: {', '.join(allowed)})"
            )

        with self.engine.connect() as connection:
            existing = {
                int(row._mapping["id"]): dict(row._mapping)
                for row in connection.execute(
                    select(
                        reconciliation_exceptions.c.id,
                        reconciliation_exceptions.c.status,
                        reconciliation_exceptions.c.run_id,
                        reconciliation_exceptions.c.recon_id,
                        reconciliation_exceptions.c.reopened_count,
                    ).where(reconciliation_exceptions.c.id.in_(ids))
                )
            }
        missing = sorted(set(ids) - set(existing))
        if missing:
            raise NotFoundError(f"Exception(s) not found: {missing[:10]}")

        now = utcnow()
        is_closing = status in self.CLOSED_STATUSES
        values: dict[str, Any] = {
            "status": status,
            "resolution_note": _truncate(comment, 8000),
            "updated_at": now,
        }
        if resolution_code:
            values["resolution_code"] = resolution_code[:64]
        if assigned_to is not None:
            values["assigned_to"] = assigned_to[:128]
        if is_closing:
            values.update({"resolved_by": actor[:128], "resolved_at": now})
        else:
            values.update({"resolved_by": None, "resolved_at": None})

        self._execute(
            reconciliation_exceptions.update()
            .where(reconciliation_exceptions.c.id.in_(ids))
            .values(**values),
            "exceptions.update_status",
        )

        reopened = [
            i
            for i in ids
            if str(existing[i].get("status")) in self.CLOSED_STATUSES and status in self.OPEN_STATUSES
        ]
        if reopened:
            self._execute(
                reconciliation_exceptions.update()
                .where(reconciliation_exceptions.c.id.in_(reopened))
                .values(reopened_count=reconciliation_exceptions.c.reopened_count + 1),
                "exceptions.increment_reopened",
            )

        comments = [
            {
                "exception_id": i,
                "run_id": existing[i].get("run_id"),
                "recon_id": existing[i].get("recon_id"),
                "author": actor[:128],
                "comment": _truncate(comment, 8000),
                "status_before": existing[i].get("status"),
                "status_after": status,
                "created_at": now,
            }
            for i in ids
        ]
        self._execute(reconciliation_exception_comment.insert(), "exception_comment.insert", comments)
        self._execute(
            reconciliation_exceptions.update()
            .where(reconciliation_exceptions.c.id.in_(ids))
            .values(comment_count=reconciliation_exceptions.c.comment_count + 1),
            "exceptions.increment_comments",
        )
        self.record_audit(
            {
                "timestamp": now,
                "action": "EXCEPTION_" + ("CLOSE" if is_closing else "UPDATE"),
                "entityType": "exception",
                "entityId": ",".join(str(i) for i in ids[:20]),
                "actor": actor,
                "success": True,
                "details": {
                    "status": status,
                    "count": len(ids),
                    "resolutionCode": resolution_code,
                    "comment": comment[:500],
                },
            }
        )
        log.info(
            "exceptions.status_changed",
            count=len(ids),
            status=status,
            actor=actor,
            reopened=len(reopened),
        )
        return {"updated": len(ids), "ids": ids, "status": status, "reopened": len(reopened)}

    def add_exception_comment(self, exception_id: int, *, comment: str, actor: str) -> dict[str, Any]:
        """Add a comment without changing the exception's status."""
        if not comment or not comment.strip():
            raise MetricsPersistenceError("Comment text is required")
        record = self.get_exception(exception_id)
        if not record:
            raise NotFoundError(f"Exception {exception_id} not found")
        now = utcnow()
        self._execute(
            reconciliation_exception_comment.insert().values(
                exception_id=exception_id,
                run_id=record.get("run_id"),
                recon_id=record.get("recon_id"),
                author=actor[:128],
                comment=_truncate(comment, 8000),
                status_before=record.get("status"),
                status_after=record.get("status"),
                created_at=now,
            ),
            "exception_comment.insert_single",
        )
        self._execute(
            reconciliation_exceptions.update()
            .where(reconciliation_exceptions.c.id == exception_id)
            .values(comment_count=reconciliation_exceptions.c.comment_count + 1, updated_at=now),
            "exceptions.increment_comment",
        )
        return {"exceptionId": exception_id, "author": actor, "createdAt": now.isoformat()}

    def list_exception_comments(self, exception_id: int, *, limit: int = 100) -> list[dict[str, Any]]:
        with self.engine.connect() as connection:
            return [
                dict(row._mapping)
                for row in connection.execute(
                    select(reconciliation_exception_comment)
                    .where(reconciliation_exception_comment.c.exception_id == exception_id)
                    .order_by(reconciliation_exception_comment.c.created_at.desc())
                    .limit(limit)
                )
            ]

    def close_exceptions_by_filter(
        self,
        *,
        comment: str,
        actor: str,
        status: str = "CLOSED",
        resolution_code: str | None = None,
        run_id: str | None = None,
        recon_id: str | None = None,
        leg_id: str | None = None,
        exception_type: str | None = None,
        business_date: str | None = None,
        field: str | None = None,
        limit: int = 5000,
    ) -> dict[str, Any]:
        """Bulk close-out - e.g. "close every LEFT_ONLY break for this feed"."""
        query = select(reconciliation_exceptions.c.id)
        if run_id:
            query = query.where(reconciliation_exceptions.c.run_id == run_id)
        if recon_id:
            query = query.where(reconciliation_exceptions.c.recon_id == recon_id)
        if leg_id:
            query = query.where(reconciliation_exceptions.c.leg_id == leg_id)
        if exception_type:
            query = query.where(reconciliation_exceptions.c.exception_type == exception_type)
        if business_date:
            query = query.where(reconciliation_exceptions.c.business_date == business_date)
        if field:
            query = query.where(reconciliation_exceptions.c.field == field)
        query = query.where(reconciliation_exceptions.c.status.in_(self.OPEN_STATUSES)).limit(limit)
        with self.engine.connect() as connection:
            ids = [int(row[0]) for row in connection.execute(query)]
        if not ids:
            return {"updated": 0, "ids": []}
        return self.update_exception_status(
            ids, status=status, comment=comment, actor=actor, resolution_code=resolution_code
        )

    def exception_status_summary(
        self, *, recon_id: str | None = None, run_id: str | None = None
    ) -> dict[str, int]:
        query = select(reconciliation_exceptions.c.status, func.count().label("count"))
        if recon_id:
            query = query.where(reconciliation_exceptions.c.recon_id == recon_id)
        if run_id:
            query = query.where(reconciliation_exceptions.c.run_id == run_id)
        query = query.group_by(reconciliation_exceptions.c.status)
        with self.engine.connect() as connection:
            return {str(row[0] or "OPEN"): int(row[1]) for row in connection.execute(query)}

    # ------------------------------------------------------------------ read
    def list_runs(
        self,
        *,
        recon_id: str | None = None,
        status: str | None = None,
        product: str | None = None,
        customer: str | None = None,
        business_date: str | None = None,
        since: datetime | None = None,
        limit: int = 100,
    ) -> list[dict[str, Any]]:
        query = select(reconciliation_run)
        if recon_id:
            query = query.where(reconciliation_run.c.recon_id == recon_id)
        if status:
            query = query.where(reconciliation_run.c.status == status)
        if product:
            query = query.where(reconciliation_run.c.product == product)
        if customer:
            query = query.where(reconciliation_run.c.customer == customer)
        if business_date:
            query = query.where(reconciliation_run.c.business_date == business_date)
        if since:
            query = query.where(reconciliation_run.c.start_time >= since)
        query = query.order_by(reconciliation_run.c.start_time.desc()).limit(limit)
        with self.engine.connect() as connection:
            return [dict(row._mapping) for row in connection.execute(query)]

    def get_run(self, run_id: str) -> dict[str, Any] | None:
        with self.engine.connect() as connection:
            row = connection.execute(
                select(reconciliation_run).where(reconciliation_run.c.run_id == run_id)
            ).first()
            return dict(row._mapping) if row else None

    def list_leg_runs(self, run_id: str) -> list[dict[str, Any]]:
        with self.engine.connect() as connection:
            return [
                dict(row._mapping)
                for row in connection.execute(
                    select(reconciliation_leg_run)
                    .where(reconciliation_leg_run.c.run_id == run_id)
                    .order_by(reconciliation_leg_run.c.stage, reconciliation_leg_run.c.leg_id)
                )
            ]

    def list_exceptions(
        self,
        *,
        run_id: str | None = None,
        recon_id: str | None = None,
        exception_type: str | None = None,
        business_date: str | None = None,
        leg_id: str | None = None,
        status: str | list[str] | None = None,
        field: str | None = None,
        search: str | None = None,
        limit: int = 500,
        offset: int = 0,
    ) -> list[dict[str, Any]]:
        query = select(reconciliation_exceptions)
        if run_id:
            query = query.where(reconciliation_exceptions.c.run_id == run_id)
        if recon_id:
            query = query.where(reconciliation_exceptions.c.recon_id == recon_id)
        if exception_type:
            query = query.where(reconciliation_exceptions.c.exception_type == exception_type)
        if business_date:
            query = query.where(reconciliation_exceptions.c.business_date == business_date)
        if leg_id:
            query = query.where(reconciliation_exceptions.c.leg_id == leg_id)
        if status:
            statuses = [status] if isinstance(status, str) else list(status)
            if "OPEN_ONLY" in statuses:
                query = query.where(reconciliation_exceptions.c.status.in_(self.OPEN_STATUSES))
            else:
                query = query.where(reconciliation_exceptions.c.status.in_(statuses))
        if field:
            query = query.where(reconciliation_exceptions.c.field == field)
        if search:
            like = f"%{search}%"
            query = query.where(reconciliation_exceptions.c.reconciliation_key.like(like))
        query = query.order_by(reconciliation_exceptions.c.id.desc()).limit(limit).offset(offset)
        with self.engine.connect() as connection:
            return [dict(row._mapping) for row in connection.execute(query)]

    def exception_summary(self, run_id: str) -> list[dict[str, Any]]:
        query = (
            select(
                reconciliation_exceptions.c.leg_id,
                reconciliation_exceptions.c.exception_type,
                reconciliation_exceptions.c.field,
                func.count().label("count"),
            )
            .where(reconciliation_exceptions.c.run_id == run_id)
            .group_by(
                reconciliation_exceptions.c.leg_id,
                reconciliation_exceptions.c.exception_type,
                reconciliation_exceptions.c.field,
            )
            .order_by(func.count().desc())
        )
        with self.engine.connect() as connection:
            return [dict(row._mapping) for row in connection.execute(query)]

    def list_field_metrics(self, run_id: str) -> list[dict[str, Any]]:
        with self.engine.connect() as connection:
            return [
                dict(row._mapping)
                for row in connection.execute(
                    select(reconciliation_field_metrics)
                    .where(reconciliation_field_metrics.c.run_id == run_id)
                    .order_by(reconciliation_field_metrics.c.mismatch_count.desc())
                )
            ]

    def list_source_metrics(self, run_id: str) -> list[dict[str, Any]]:
        with self.engine.connect() as connection:
            return [
                dict(row._mapping)
                for row in connection.execute(
                    select(reconciliation_source_metrics).where(
                        reconciliation_source_metrics.c.run_id == run_id
                    )
                )
            ]

    def dashboard_summary(
        self, *, days: int = 30, product: str | None = None, customer: str | None = None
    ) -> dict[str, Any]:
        since = utcnow() - timedelta(days=days)
        query = select(
            reconciliation_run.c.status,
            func.count().label("runs"),
            func.avg(reconciliation_run.c.duration_ms).label("avg_duration"),
            func.sum(reconciliation_run.c.records_read).label("records_read"),
            func.sum(reconciliation_run.c.records_matched).label("matched"),
            func.sum(reconciliation_run.c.records_unmatched).label("unmatched"),
            func.sum(reconciliation_run.c.exceptions).label("exceptions"),
        ).where(reconciliation_run.c.start_time >= since)
        if product:
            query = query.where(reconciliation_run.c.product == product)
        if customer:
            query = query.where(reconciliation_run.c.customer == customer)
        query = query.group_by(reconciliation_run.c.status)
        with self.engine.connect() as connection:
            rows = [dict(row._mapping) for row in connection.execute(query)]
        total = sum(int(r["runs"]) for r in rows)
        matched = sum(int(r["matched"] or 0) for r in rows)
        read = sum(int(r["records_read"] or 0) for r in rows)
        durations = [float(r["avg_duration"]) for r in rows if r["avg_duration"]]
        return {
            "days": days,
            "totalRuns": total,
            "byStatus": {r["status"]: int(r["runs"]) for r in rows},
            "recordsRead": read,
            "recordsMatched": matched,
            "recordsUnmatched": sum(int(r["unmatched"] or 0) for r in rows),
            "exceptions": sum(int(r["exceptions"] or 0) for r in rows),
            "matchPercentage": round(matched / read * 100, 4) if read else None,
            "avgDurationMs": int(sum(durations) / len(durations)) if durations else None,
        }

    def run_trend(self, *, days: int = 30, recon_id: str | None = None) -> list[dict[str, Any]]:
        since = utcnow() - timedelta(days=days)
        day = func.date(reconciliation_run.c.start_time).label("day")
        query = (
            select(
                day,
                reconciliation_run.c.status,
                func.count().label("runs"),
                func.sum(reconciliation_run.c.records_read).label("records_read"),
                func.sum(reconciliation_run.c.exceptions).label("exceptions"),
                func.avg(reconciliation_run.c.duration_ms).label("avg_duration"),
                func.avg(reconciliation_run.c.match_percentage).label("avg_match_percentage"),
            )
            .where(reconciliation_run.c.start_time >= since)
            .group_by(day, reconciliation_run.c.status)
            .order_by(day)
        )
        if recon_id:
            query = query.where(reconciliation_run.c.recon_id == recon_id)
        with self.engine.connect() as connection:
            return [dict(row._mapping) for row in connection.execute(query)]

    def purge_old_data(self, *, runs_days: int, exceptions_days: int, recon_id: str | None = None) -> dict[str, int]:
        """Retention enforcement (invoked by the scheduler's maintenance task)."""
        deleted: dict[str, int] = {}
        exception_cutoff = utcnow() - timedelta(days=exceptions_days)
        run_cutoff = utcnow() - timedelta(days=runs_days)
        statements = [
            ("exceptions", delete(reconciliation_exceptions).where(reconciliation_exceptions.c.created_at < exception_cutoff)),
            ("runs", delete(reconciliation_run).where(reconciliation_run.c.start_time < run_cutoff)),
            ("leg_runs", delete(reconciliation_leg_run).where(reconciliation_leg_run.c.start_time < run_cutoff)),
            ("metrics", delete(reconciliation_metrics).where(reconciliation_metrics.c.recorded_at < run_cutoff)),
        ]
        for name, statement in statements:
            if recon_id:
                statement = statement.where(text("recon_id = :rid")).params(rid=recon_id)
            result = self._execute(statement, f"purge.{name}")
            deleted[name] = int(result.rowcount or 0)
        log.info("metrics.purged", **deleted)
        return deleted


def _as_datetime(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def _truncate(value: Any, length: int) -> str | None:
    if value is None:
        return None
    text_value = str(value)
    return text_value[:length]
