"""Health, readiness, metrics and administrative endpoints."""

from __future__ import annotations

import platform
import socket
import time
from typing import Annotated, Any

from fastapi import APIRouter, Depends, Response

from reconx import __version__
from reconx.api.deps import (
    DatabaseDep,
    MetricsDep,
    SchedulerDep,
    SettingsDep,
    requires,
)
from reconx.api.schemas import MessageResponse
from reconx.common.logging import get_logger
from reconx.common.timeutils import utcnow
from reconx.config.enums import Permission
from reconx.config.store import ensure_indexes
from reconx.config.store import ping as mongo_ping
from reconx.connectors import available_connectors
from reconx.events.schemas import topics_for

log = get_logger(__name__)
router = APIRouter(tags=["system"])
START_TIME = time.time()


@router.get("/health", summary="Liveness probe")
def health() -> dict[str, Any]:
    """Cheap check: the process is up.  Never touches a dependency."""
    return {
        "status": "UP",
        "service": "reconx-api",
        "version": __version__,
        "hostname": socket.gethostname(),
        "uptimeSeconds": int(time.time() - START_TIME),
        "time": utcnow().isoformat(),
    }


@router.get("/ready", summary="Readiness probe")
def ready(settings: SettingsDep, metrics: MetricsDep, response: Response) -> dict[str, Any]:
    """Deep check: can we reach the state stores we cannot work without?"""
    checks: dict[str, Any] = {}
    ready_state = True

    try:
        checks["mongodb"] = {"status": "UP", **mongo_ping(settings)}
    except Exception as exc:
        checks["mongodb"] = {"status": "DOWN", "error": str(exc)[:300]}
        ready_state = False

    try:
        checks["metricsDatabase"] = {"status": "UP", **metrics.ping()}
    except Exception as exc:
        checks["metricsDatabase"] = {"status": "DOWN", "error": str(exc)[:300]}
        ready_state = False

    if settings.kafka.enabled:
        try:
            from confluent_kafka.admin import AdminClient

            admin = AdminClient(
                {"bootstrap.servers": settings.kafka.bootstrap_servers, "socket.timeout.ms": 5000}
            )
            metadata = admin.list_topics(timeout=5)
            checks["kafka"] = {"status": "UP", "brokers": len(metadata.brokers)}
        except Exception as exc:
            checks["kafka"] = {"status": "DEGRADED", "error": str(exc)[:200]}
    else:
        checks["kafka"] = {"status": "DISABLED"}

    if not ready_state:
        response.status_code = 503
    return {"status": "READY" if ready_state else "NOT_READY", "checks": checks}


@router.get("/metrics", summary="Prometheus metrics", response_class=Response)
def prometheus_metrics(db: DatabaseDep, scheduler: SchedulerDep) -> Response:
    from prometheus_client import CONTENT_TYPE_LATEST, CollectorRegistry, Gauge, generate_latest

    from reconx.config.enums import DefinitionStatus, RunStatus
    from reconx.config.store import Collections

    registry = CollectorRegistry()
    uptime = Gauge("reconx_uptime_seconds", "API uptime in seconds", registry=registry)
    uptime.set(time.time() - START_TIME)

    definitions = Gauge(
        "reconx_definitions", "Reconciliation definitions", ["status"], registry=registry
    )
    for status_value in DefinitionStatus:
        definitions.labels(status=status_value.value).set(
            db[Collections.DEFINITIONS].count_documents({"status": status_value.value})
        )

    runs = Gauge("reconx_runs", "Runs by status (last 7 days)", ["status"], registry=registry)
    from datetime import timedelta

    since = utcnow() - timedelta(days=7)
    for status_value in RunStatus:
        runs.labels(status=status_value.value).set(
            db[Collections.RUNS].count_documents({"status": status_value.value, "createdAt": {"$gte": since}})
        )

    active = Gauge("reconx_runs_active", "Currently active runs", registry=registry)
    active.set(
        db[Collections.RUNS].count_documents(
            {
                "status": {
                    "$in": [
                        RunStatus.QUEUED.value,
                        RunStatus.STARTING.value,
                        RunStatus.RUNNING.value,
                        RunStatus.WAITING_FOR_DATA.value,
                    ]
                }
            }
        )
    )
    schedules = Gauge("reconx_schedules_enabled", "Enabled schedules", registry=registry)
    schedules.set(db[Collections.SCHEDULE_STATE].count_documents({"enabled": True, "paused": False}))

    locks = Gauge("reconx_locks_held", "Distributed locks currently held", registry=registry)
    locks.set(db[Collections.LOCKS].count_documents({}))

    jobs = Gauge("reconx_local_jobs_running", "Jobs running on this node", registry=registry)
    jobs.set(scheduler.orchestrator.running_count())

    return Response(content=generate_latest(registry), media_type=CONTENT_TYPE_LATEST)


@router.get("/api/system/info", summary="Platform configuration overview")
def system_info(
    settings: SettingsDep,
    principal: Annotated[Any, Depends(requires(Permission.SYSTEM_MANAGE))],
) -> dict[str, Any]:
    """Effective configuration with every secret redacted."""
    return {
        "version": __version__,
        "environment": settings.environment,
        "python": platform.python_version(),
        "hostname": socket.gethostname(),
        "mongodb": {"database": settings.mongo.database, "tls": settings.mongo.tls},
        "kafka": {
            "enabled": settings.kafka.enabled,
            "bootstrapServers": settings.kafka.bootstrap_servers,
            "topicPrefix": settings.kafka.topic_prefix,
            "securityProtocol": settings.kafka.security_protocol,
            "topics": topics_for(settings.kafka.topic_prefix),
        },
        "resultDatabase": {
            "jdbcUrl": settings.result_db.jdbc_url,
            "driver": settings.result_db.jdbc_driver,
            "autoCreateSchema": settings.result_db.auto_create_schema,
        },
        "spark": {
            "master": settings.spark.master,
            "submitMode": settings.spark.submit_mode,
            "namespace": settings.spark.namespace,
            "image": settings.spark.image,
            "executorInstances": settings.spark.executor_instances,
            "executorMemory": settings.spark.executor_memory,
            "shufflePartitions": settings.spark.shuffle_partitions,
            "dynamicAllocation": settings.spark.dynamic_allocation,
        },
        "scheduler": {
            "enabled": settings.scheduler.enabled,
            "pollIntervalSeconds": settings.scheduler.poll_interval_seconds,
            "maxConcurrentRuns": settings.scheduler.max_concurrent_runs,
            "lockTtlSeconds": settings.scheduler.lock_ttl_seconds,
        },
        "smtp": {
            "enabled": settings.smtp.enabled,
            "host": settings.smtp.host,
            "port": settings.smtp.port,
            "useTls": settings.smtp.use_tls,
            "fromAddress": settings.smtp.from_address,
        },
        "security": {
            "authEnabled": settings.security.auth_enabled,
            "secretsBackend": settings.security.secrets_backend,
            "jwtAlgorithm": settings.security.jwt_algorithm,
            "encryptionConfigured": bool(settings.security.encryption_key),
        },
        "connectors": available_connectors(),
    }


@router.get("/api/system/status", summary="Scheduler and node status")
def system_status(
    scheduler: SchedulerDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
) -> dict[str, Any]:
    return scheduler.status()


@router.get("/api/system/locks", summary="Distributed locks currently held")
def locks(
    db: DatabaseDep,
    principal: Annotated[Any, Depends(requires(Permission.SYSTEM_MANAGE))],
) -> dict[str, Any]:
    from reconx.scheduler.locks import list_locks

    return {"items": list_locks(db)}


@router.delete("/api/system/locks/{lock_id:path}", summary="Force-release a stuck lock")
def release_lock(
    lock_id: str,
    db: DatabaseDep,
    principal: Annotated[Any, Depends(requires(Permission.SYSTEM_MANAGE))],
) -> MessageResponse:
    from reconx.scheduler.locks import force_release

    released = force_release(db, lock_id)
    return MessageResponse(
        message=f"Lock '{lock_id}' released" if released else f"No lock '{lock_id}' was held"
    )


@router.post("/api/system/initialise", summary="Create MongoDB indexes and metrics tables")
def initialise(
    db: DatabaseDep,
    metrics: MetricsDep,
    settings: SettingsDep,
    principal: Annotated[Any, Depends(requires(Permission.SYSTEM_MANAGE))],
) -> dict[str, Any]:
    indexes = ensure_indexes(db, settings)
    tables = metrics.create_schema()
    return {"indexes": indexes, "tables": tables}


@router.get("/api/system/audit", summary="Audit trail")
def audit_trail(
    db: DatabaseDep,
    principal: Annotated[Any, Depends(requires(Permission.AUDIT_VIEW))],
    entity_type: str | None = None,
    entity_id: str | None = None,
    actor: str | None = None,
    action: str | None = None,
    limit: int = 200,
    offset: int = 0,
) -> dict[str, Any]:
    from reconx.security.audit import AuditLogger

    return {
        "items": AuditLogger(db).query(
            entity_type=entity_type,
            entity_id=entity_id,
            actor=actor,
            action=action,
            limit=limit,
            skip=offset,
        )
    }
