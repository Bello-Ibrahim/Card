"""Reporting and dashboard endpoints."""

from __future__ import annotations

from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query

from reconx.api.deps import DatabaseDep, MetricsDep, ReconRepoDep, RunRepoDep, requires
from reconx.common.logging import get_logger
from reconx.common.timeutils import utcnow
from reconx.config.enums import DefinitionStatus, Permission, RunStatus
from reconx.config.store import Collections

log = get_logger(__name__)
router = APIRouter(prefix="/api/reports", tags=["reports"])


@router.get("/dashboard", summary="Dashboard headline numbers")
def dashboard(
    runs: RunRepoDep,
    repository: ReconRepoDep,
    metrics: MetricsDep,
    db: DatabaseDep,
    principal: Annotated[Any, Depends(requires(Permission.REPORT_VIEW))],
    days: int = Query(default=30, ge=1, le=365),
    product: str | None = None,
    customer: str | None = None,
) -> dict[str, Any]:
    since = utcnow() - timedelta(days=days)
    statistics = runs.statistics(since=since, product=product, customer=customer)
    by_status = statistics.get("byStatus", {})
    definitions = {
        "total": repository.count(),
        "active": repository.count(status=DefinitionStatus.ACTIVE.value),
        "draft": repository.count(status=DefinitionStatus.DRAFT.value),
        "disabled": repository.count(status=DefinitionStatus.DISABLED.value),
    }
    warehouse: dict[str, Any] = {}
    try:
        warehouse = metrics.dashboard_summary(days=days, product=product, customer=customer)
    except Exception as exc:
        log.warning("api.dashboard_metrics_unavailable", error=str(exc)[:200])

    return {
        "days": days,
        "definitions": definitions,
        "runs": {
            "total": statistics.get("total", 0),
            "success": by_status.get(RunStatus.SUCCESS.value, 0),
            "partial": by_status.get(RunStatus.PARTIAL_SUCCESS.value, 0),
            "failed": by_status.get(RunStatus.FAILED.value, 0),
            "running": by_status.get(RunStatus.RUNNING.value, 0)
            + by_status.get(RunStatus.STARTING.value, 0)
            + by_status.get(RunStatus.QUEUED.value, 0),
            "waitingForData": by_status.get(RunStatus.WAITING_FOR_DATA.value, 0),
            "cancelled": by_status.get(RunStatus.CANCELLED.value, 0),
            "skipped": by_status.get(RunStatus.SKIPPED.value, 0),
            "byStatus": by_status,
        },
        "volumes": {
            "recordsRead": statistics.get("recordsRead", 0),
            "recordsMatched": statistics.get("recordsMatched", 0),
            "recordsUnmatched": statistics.get("recordsUnmatched", 0),
            "exceptions": statistics.get("exceptions", 0),
            "matchPercentage": statistics.get("matchPercentage"),
            "avgDurationMs": statistics.get("avgDurationMs"),
        },
        "warehouse": warehouse,
        "schedules": {
            "total": db[Collections.SCHEDULE_STATE].count_documents({}),
            "enabled": db[Collections.SCHEDULE_STATE].count_documents({"enabled": True, "paused": False}),
            "paused": db[Collections.SCHEDULE_STATE].count_documents({"paused": True}),
        },
    }


@router.get("/trend", summary="Run trend over time")
def trend(
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.REPORT_VIEW))],
    days: int = Query(default=30, ge=1, le=365),
    recon_id: str | None = None,
) -> dict[str, Any]:
    try:
        return {"items": metrics.run_trend(days=days, recon_id=recon_id)}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Metrics database unavailable: {exc}") from exc


@router.get("/runs", summary="Historical runs from the metrics warehouse")
def runs_report(
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.REPORT_VIEW))],
    recon_id: str | None = None,
    status: str | None = None,
    product: str | None = None,
    customer: str | None = None,
    business_date: str | None = None,
    days: int = Query(default=30, ge=1, le=3650),
    limit: int = Query(default=200, ge=1, le=5000),
) -> dict[str, Any]:
    try:
        items = metrics.list_runs(
            recon_id=recon_id,
            status=status,
            product=product,
            customer=customer,
            business_date=business_date,
            since=utcnow() - timedelta(days=days),
            limit=limit,
        )
        return {"items": items, "count": len(items)}
    except Exception as exc:
        raise HTTPException(status_code=503, detail=f"Metrics database unavailable: {exc}") from exc


@router.get("/field-metrics", summary="Field-level mismatch metrics for a run")
def field_metrics(
    run_id: str,
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.REPORT_VIEW))],
) -> dict[str, Any]:
    return {"items": metrics.list_field_metrics(run_id)}
