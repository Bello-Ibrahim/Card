"""Run management endpoints."""

from __future__ import annotations

from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, Query, Request

from reconx.api.deps import (
    AuditDep,
    MetricsDep,
    ReconRepoDep,
    RunRepoDep,
    SchedulerDep,
    audit_context,
    requires,
)
from reconx.api.schemas import CancelRequest
from reconx.common.logging import get_logger
from reconx.common.timeutils import utcnow
from reconx.config.enums import Permission, RunStatus
from reconx.security.audit import AuditAction

log = get_logger(__name__)
router = APIRouter(prefix="/api/runs", tags=["runs"])

ACTIVE_STATUSES = [
    RunStatus.QUEUED.value,
    RunStatus.STARTING.value,
    RunStatus.RUNNING.value,
    RunStatus.WAITING_FOR_DATA.value,
]


@router.get("", summary="List runs")
def list_runs(
    runs: RunRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
    recon_id: str | None = None,
    status: str | None = None,
    product: str | None = None,
    customer: str | None = None,
    business_date: str | None = None,
    active_only: bool = False,
    days: int | None = Query(default=None, ge=1, le=3650),
    limit: int = Query(default=100, ge=1, le=1000),
    offset: int = Query(default=0, ge=0),
) -> dict[str, Any]:
    status_filter: Any = status
    if active_only:
        status_filter = ACTIVE_STATUSES
    items = runs.list(
        recon_id=recon_id,
        status=status_filter,
        product=product,
        customer=customer,
        business_date=business_date,
        since=utcnow() - timedelta(days=days) if days else None,
        limit=limit,
        skip=offset,
    )
    return {"items": items, "limit": limit, "offset": offset, "count": len(items)}


@router.get("/statistics", summary="Aggregate run statistics")
def statistics(
    runs: RunRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
    days: int = Query(default=30, ge=1, le=3650),
    recon_id: str | None = None,
    product: str | None = None,
    customer: str | None = None,
) -> dict[str, Any]:
    return runs.statistics(
        since=utcnow() - timedelta(days=days),
        reconId=recon_id,
        product=product,
        customer=customer,
    )


@router.get("/{run_id}", summary="Run detail")
def get_run(
    run_id: str,
    runs: RunRepoDep,
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
) -> dict[str, Any]:
    run = runs.get(run_id)
    legs = runs.list_legs(run_id)
    detail: dict[str, Any] = {"run": run, "legs": legs}
    try:
        detail["metricsRun"] = metrics.get_run(run_id)
        detail["metricsLegs"] = metrics.list_leg_runs(run_id)
        detail["fieldMetrics"] = metrics.list_field_metrics(run_id)
        detail["sourceMetrics"] = metrics.list_source_metrics(run_id)
        detail["exceptionSummary"] = metrics.exception_summary(run_id)
        detail["exceptionStatus"] = metrics.exception_status_summary(run_id=run_id)
    except Exception as exc:
        log.warning("api.run_metrics_unavailable", run_id=run_id, error=str(exc)[:200])
        detail["metricsError"] = str(exc)[:400]
    return detail


@router.get("/{run_id}/legs", summary="Leg results for a run")
def run_legs(
    run_id: str,
    metrics: MetricsDep,
    runs: RunRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
) -> dict[str, Any]:
    try:
        items = metrics.list_leg_runs(run_id)
    except Exception:
        items = runs.list_legs(run_id)
    return {"items": items}


@router.post("/{run_id}/cancel", summary="Cancel a run")
def cancel_run(
    run_id: str,
    payload: CancelRequest,
    scheduler: SchedulerDep,
    audit: AuditDep,
    request: Request,
    principal: Annotated[Any, Depends(requires(Permission.RUN_CANCEL))],
) -> dict[str, Any]:
    result = scheduler.cancel_run(run_id, actor=principal.username)
    audit.record(
        action=AuditAction.CANCEL,
        entity_type="run",
        entity_id=run_id,
        actor=principal.username,
        details={"reason": payload.reason},
        **audit_context(request),
    )
    return result


@router.get("/{run_id}/logs", summary="Tail the driver log of a run submitted by this node")
def run_logs(
    run_id: str,
    scheduler: SchedulerDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
    lines: int = Query(default=200, ge=1, le=5000),
) -> dict[str, Any]:
    content = scheduler.orchestrator.tail_log(run_id, lines)
    return {
        "runId": run_id,
        "lines": content.splitlines()[-lines:],
        "available": bool(content),
        "note": (
            "Logs are local to the node that submitted the run. In Kubernetes, use "
            "`kubectl logs` on the driver pod, or your log aggregator, for a cluster-wide view."
        ),
    }


@router.get("/{run_id}/conditions", summary="Condition evaluation detail for a waiting run")
def run_conditions(
    run_id: str,
    runs: RunRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RUN_VIEW))],
) -> dict[str, Any]:
    run = runs.get(run_id)
    return {
        "runId": run_id,
        "status": run.get("status"),
        "conditionSummary": run.get("conditionSummary"),
        "conditionResult": run.get("conditionResult"),
        "waitingSince": run.get("waitingSince"),
        "lastCheckedAt": run.get("lastConditionCheckAt"),
    }


@router.post("/{run_id}/retry", status_code=202, summary="Retry a failed run")
def retry_run(
    run_id: str,
    runs: RunRepoDep,
    repository: ReconRepoDep,
    scheduler: SchedulerDep,
    audit: AuditDep,
    request: Request,
    principal: Annotated[Any, Depends(requires(Permission.RECON_EXECUTE))],
) -> dict[str, Any]:
    original = runs.get(run_id)
    parameters = dict(original.get("parameters") or {})
    # A retry is a new logical run: give it a distinct idempotency dimension so
    # the unique key does not reject it, while keeping the lineage visible.
    parameters["retry_of"] = run_id
    new_run = scheduler.trigger_now(
        original["reconId"],
        triggered_by=principal.username,
        business_date=original.get("businessDate"),
        parameters=parameters,
        skip_conditions=False,
        version=original.get("version"),
    )
    audit.record(
        action=AuditAction.EXECUTE,
        entity_type="run",
        entity_id=new_run.get("runId", ""),
        actor=principal.username,
        details={"retryOf": run_id},
        **audit_context(request),
    )
    return {"run": new_run, "retryOf": run_id}
