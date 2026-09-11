"""Schedule management endpoints."""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query

from reconx.api.deps import (
    AuditDep,
    DatabaseDep,
    ReconRepoDep,
    SchedulerDep,
    requires,
)
from reconx.api.schemas import MessageResponse
from reconx.common.logging import get_logger
from reconx.common.timeutils import utcnow
from reconx.config.enums import Permission
from reconx.config.store import Collections
from reconx.scheduler.triggers import describe, next_fire_time, upcoming_fire_times
from reconx.security.audit import AuditAction

log = get_logger(__name__)
router = APIRouter(prefix="/api/schedules", tags=["schedules"])


@router.get("", summary="List schedules and their next firing time")
def list_schedules(
    db: DatabaseDep,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.SCHEDULE_VIEW))],
    enabled: bool | None = None,
) -> dict[str, Any]:
    query: dict[str, Any] = {}
    if enabled is not None:
        query["enabled"] = enabled
    states = list(db[Collections.SCHEDULE_STATE].find(query, {"_id": False}).sort("nextRunAt", 1))
    return {"items": states, "total": len(states), "serverTime": utcnow().isoformat()}


@router.get("/{recon_id}", summary="Schedule detail with upcoming firings")
def get_schedule(
    recon_id: str,
    db: DatabaseDep,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.SCHEDULE_VIEW))],
    count: int = Query(default=10, ge=1, le=50),
) -> dict[str, Any]:
    definition = repository.get(recon_id)
    state = db[Collections.SCHEDULE_STATE].find_one({"reconId": recon_id}, {"_id": False}) or {}
    return {
        "reconId": recon_id,
        "schedule": definition.schedule.dump(),
        "description": describe(definition.schedule),
        "state": state,
        "upcoming": [t.isoformat() for t in upcoming_fire_times(definition.schedule, count)],
        "conditions": definition.conditions.dump() if definition.conditions else None,
    }


@router.post("/{recon_id}/pause", summary="Pause a schedule")
def pause(
    recon_id: str,
    db: DatabaseDep,
    audit: AuditDep,
    principal: Annotated[Any, Depends(requires(Permission.SCHEDULE_MANAGE))],
) -> dict[str, Any]:
    db[Collections.SCHEDULE_STATE].update_one(
        {"reconId": recon_id},
        {"$set": {"paused": True, "pausedBy": principal.username, "pausedAt": utcnow(), "nextRunAt": None}},
        upsert=True,
    )
    audit.record(
        action=AuditAction.SCHEDULE_PAUSE,
        entity_type="schedule",
        entity_id=recon_id,
        actor=principal.username,
    )
    return {"reconId": recon_id, "paused": True}


@router.post("/{recon_id}/resume", summary="Resume a paused schedule")
def resume(
    recon_id: str,
    db: DatabaseDep,
    repository: ReconRepoDep,
    audit: AuditDep,
    principal: Annotated[Any, Depends(requires(Permission.SCHEDULE_MANAGE))],
) -> dict[str, Any]:
    definition = repository.get(recon_id)
    upcoming = next_fire_time(definition.schedule)
    db[Collections.SCHEDULE_STATE].update_one(
        {"reconId": recon_id},
        {
            "$set": {
                "paused": False,
                "resumedBy": principal.username,
                "resumedAt": utcnow(),
                "nextRunAt": upcoming,
            }
        },
        upsert=True,
    )
    audit.record(
        action=AuditAction.SCHEDULE_RESUME,
        entity_type="schedule",
        entity_id=recon_id,
        actor=principal.username,
    )
    return {"reconId": recon_id, "paused": False, "nextRunAt": upcoming.isoformat() if upcoming else None}


@router.post("/{recon_id}/evaluate-conditions", summary="Evaluate data-availability conditions now")
def evaluate_conditions(
    recon_id: str,
    repository: ReconRepoDep,
    scheduler: SchedulerDep,
    principal: Annotated[Any, Depends(requires(Permission.SCHEDULE_VIEW))],
    business_date: str | None = None,
) -> dict[str, Any]:
    from reconx.common.templating import build_run_variables
    from reconx.common.timeutils import business_date as compute_business_date
    from reconx.config.models import declared_variable_defaults

    definition = repository.get(recon_id)
    resolved = (
        __import__("datetime").date.fromisoformat(business_date)
        if business_date
        else compute_business_date(tz=definition.schedule.timezone)
    )
    variables = build_run_variables(
        recon_id=recon_id,
        biz_date=resolved,
        timezone_name=definition.schedule.timezone,
        extra=declared_variable_defaults(definition),
    )
    result = scheduler._evaluate_conditions(definition, variables)
    return {
        "reconId": recon_id,
        "businessDate": resolved.isoformat(),
        "satisfied": result.satisfied,
        "summary": result.summary(),
        "detail": result.to_dict(),
    }


@router.get("/{recon_id}/history", summary="Scheduler firing history")
def history(
    recon_id: str,
    scheduler: SchedulerDep,
    principal: Annotated[Any, Depends(requires(Permission.SCHEDULE_VIEW))],
    limit: int = Query(default=50, ge=1, le=500),
) -> dict[str, Any]:
    from sqlalchemy import select

    from reconx.metrics.models import scheduler_execution

    try:
        with scheduler.metrics.engine.connect() as connection:
            rows = [
                dict(row._mapping)
                for row in connection.execute(
                    select(scheduler_execution)
                    .where(scheduler_execution.c.recon_id == recon_id)
                    .order_by(scheduler_execution.c.fired_at.desc())
                    .limit(limit)
                )
            ]
        return {"items": rows}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Metrics database unavailable: {exc}") from exc


@router.delete("/{recon_id}", summary="Clear stored schedule state")
def clear_state(
    recon_id: str,
    db: DatabaseDep,
    principal: Annotated[Any, Depends(requires(Permission.SCHEDULE_MANAGE))],
) -> MessageResponse:
    db[Collections.SCHEDULE_STATE].delete_one({"reconId": recon_id})
    return MessageResponse(
        message=f"Schedule state for '{recon_id}' cleared; it will be recomputed on the next scheduler tick"
    )
