"""Exception management: review, comment and close out.

Exceptions are the officer's work queue.  Every state change carries a
mandatory comment and is written to an immutable comment trail plus the audit
log, so "why was this break closed?" always has an answer.
"""

from __future__ import annotations

import contextlib
import csv
import io
import json
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import StreamingResponse

from reconx.api.deps import AuditDep, MetricsDep, audit_context, requires
from reconx.api.schemas import (
    ExceptionBulkCloseRequest,
    ExceptionCommentRequest,
    ExceptionStatusRequest,
)
from reconx.common.errors import ReconXError
from reconx.common.logging import get_logger
from reconx.config.enums import Permission

log = get_logger(__name__)
router = APIRouter(prefix="/api/exceptions", tags=["exceptions"])

#: Suggested taxonomy shown in the UI; free text is still accepted.
RESOLUTION_CODES = [
    "TIMING",
    "FX_RATE",
    "ROUNDING",
    "SOURCE_ERROR",
    "TARGET_ERROR",
    "DUPLICATE_FEED",
    "KEY_MISMATCH",
    "MANUAL_ADJUSTMENT",
    "FALSE_POSITIVE",
    "ACCEPTED_DIFFERENCE",
    "OTHER",
]


def _expand(row: dict[str, Any]) -> dict[str, Any]:
    """Parse the JSON context/key columns so the UI can render them as columns."""
    out = dict(row)
    for column in ("key_components", "context_columns"):
        value = out.get(column)
        if isinstance(value, str) and value.strip().startswith("{"):
            with contextlib.suppress(json.JSONDecodeError):
                out[column] = json.loads(value)
    return out


@router.get("", summary="List exceptions")
def list_exceptions(
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.EXCEPTION_VIEW))],
    run_id: str | None = None,
    recon_id: str | None = None,
    leg_id: str | None = None,
    exception_type: str | None = None,
    business_date: str | None = None,
    field: str | None = None,
    status: str | None = Query(default=None, description="Status, or OPEN_ONLY for every open state"),
    search: str | None = Query(default=None, description="Substring match on the reconciliation key"),
    limit: int = Query(default=200, ge=1, le=5000),
    offset: int = Query(default=0, ge=0),
) -> dict[str, Any]:
    items = metrics.list_exceptions(
        run_id=run_id,
        recon_id=recon_id,
        leg_id=leg_id,
        exception_type=exception_type,
        business_date=business_date,
        field=field,
        status=status,
        search=search,
        limit=limit,
        offset=offset,
    )
    context_columns: list[str] = []
    for row in items[:200]:
        parsed = _expand(row).get("context_columns")
        if isinstance(parsed, dict):
            for key in parsed:
                if key not in context_columns:
                    context_columns.append(key)
    return {
        "items": [_expand(row) for row in items],
        "limit": limit,
        "offset": offset,
        "count": len(items),
        "contextColumns": context_columns,
        "statusSummary": metrics.exception_status_summary(recon_id=recon_id, run_id=run_id),
        "resolutionCodes": RESOLUTION_CODES,
    }


@router.get("/summary", summary="Exception counts by type and field")
def summary(
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.EXCEPTION_VIEW))],
    run_id: str | None = None,
    recon_id: str | None = None,
) -> dict[str, Any]:
    return {
        "byType": metrics.exception_summary(run_id) if run_id else [],
        "byStatus": metrics.exception_status_summary(recon_id=recon_id, run_id=run_id),
        "resolutionCodes": RESOLUTION_CODES,
    }


@router.get("/{exception_id}", summary="Exception detail with its comment trail")
def get_exception(
    exception_id: int,
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.EXCEPTION_VIEW))],
) -> dict[str, Any]:
    record = metrics.get_exception(exception_id)
    if not record:
        raise HTTPException(status_code=404, detail=f"Exception {exception_id} not found")
    return {
        "exception": _expand(record),
        "comments": metrics.list_exception_comments(exception_id),
    }


@router.post("/status", summary="Close out or update exceptions (comment required)")
def update_status(
    payload: ExceptionStatusRequest,
    metrics: MetricsDep,
    audit: AuditDep,
    request: Request,
    principal: Annotated[Any, Depends(requires(Permission.EXCEPTION_VIEW))],
) -> dict[str, Any]:
    if not payload.exception_ids:
        raise HTTPException(status_code=400, detail="At least one exception id is required")
    try:
        result = metrics.update_exception_status(
            payload.exception_ids,
            status=payload.status,
            comment=payload.comment,
            actor=principal.username,
            resolution_code=payload.resolution_code,
            assigned_to=payload.assigned_to,
        )
    except ReconXError as exc:
        raise HTTPException(status_code=400, detail=exc.message) from exc
    audit.record(
        action="EXCEPTION_STATUS_CHANGE",
        entity_type="exception",
        entity_id=",".join(str(i) for i in payload.exception_ids[:20]),
        actor=principal.username,
        details={
            "status": payload.status,
            "count": len(payload.exception_ids),
            "resolutionCode": payload.resolution_code,
            "comment": payload.comment[:500],
        },
        **audit_context(request),
    )
    return result


@router.post("/bulk-close", summary="Close every open exception matching a filter")
def bulk_close(
    payload: ExceptionBulkCloseRequest,
    metrics: MetricsDep,
    audit: AuditDep,
    request: Request,
    principal: Annotated[Any, Depends(requires(Permission.EXCEPTION_VIEW))],
) -> dict[str, Any]:
    if not any([payload.run_id, payload.recon_id, payload.leg_id, payload.exception_type]):
        raise HTTPException(
            status_code=400,
            detail="Provide at least one filter (runId, reconId, legId or exceptionType) for a bulk close",
        )
    try:
        result = metrics.close_exceptions_by_filter(
            comment=payload.comment,
            actor=principal.username,
            status=payload.status,
            resolution_code=payload.resolution_code,
            run_id=payload.run_id,
            recon_id=payload.recon_id,
            leg_id=payload.leg_id,
            exception_type=payload.exception_type,
            business_date=payload.business_date,
            field=payload.field,
            limit=payload.limit,
        )
    except ReconXError as exc:
        raise HTTPException(status_code=400, detail=exc.message) from exc
    audit.record(
        action="EXCEPTION_BULK_CLOSE",
        entity_type="exception",
        entity_id=payload.run_id or payload.recon_id or "filter",
        actor=principal.username,
        details={**payload.model_dump(by_alias=True), "updated": result.get("updated")},
        **audit_context(request),
    )
    return result


@router.post("/{exception_id}/comments", status_code=201, summary="Add a comment")
def add_comment(
    exception_id: int,
    payload: ExceptionCommentRequest,
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.EXCEPTION_VIEW))],
) -> dict[str, Any]:
    try:
        return metrics.add_exception_comment(
            exception_id, comment=payload.comment, actor=principal.username
        )
    except ReconXError as exc:
        raise HTTPException(status_code=400, detail=exc.message) from exc


@router.get("/{exception_id}/comments", summary="Comment trail")
def list_comments(
    exception_id: int,
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.EXCEPTION_VIEW))],
) -> dict[str, Any]:
    return {"items": metrics.list_exception_comments(exception_id)}


@router.get("/export/csv", summary="Download exceptions as CSV")
def export_csv(
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.EXCEPTION_VIEW))],
    run_id: str | None = None,
    recon_id: str | None = None,
    exception_type: str | None = None,
    status: str | None = None,
    limit: int = Query(default=50_000, ge=1, le=500_000),
) -> StreamingResponse:
    rows = [
        _expand(row)
        for row in metrics.list_exceptions(
            run_id=run_id,
            recon_id=recon_id,
            exception_type=exception_type,
            status=status,
            limit=limit,
        )
    ]
    context_keys: list[str] = []
    for row in rows:
        if isinstance(row.get("context_columns"), dict):
            for key in row["context_columns"]:
                if key not in context_keys:
                    context_keys.append(key)

    base_columns = [
        "id",
        "run_id",
        "recon_id",
        "leg_id",
        "business_date",
        "reconciliation_key",
        "exception_type",
        "source",
        "field",
        "rule",
        "expected_value",
        "actual_value",
        "left_occurrences",
        "right_occurrences",
        "status",
        "resolution_code",
        "resolution_note",
        "resolved_by",
        "resolved_at",
        "created_at",
    ]

    def _generate() -> Any:
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        writer.writerow([*base_columns, *context_keys])
        yield buffer.getvalue()
        buffer.seek(0)
        buffer.truncate(0)
        for row in rows:
            context = row.get("context_columns") if isinstance(row.get("context_columns"), dict) else {}
            writer.writerow(
                [row.get(column) for column in base_columns]
                + [context.get(key) for key in context_keys]
            )
            yield buffer.getvalue()
            buffer.seek(0)
            buffer.truncate(0)

    filename = f"exceptions_{run_id or recon_id or 'all'}.csv"
    return StreamingResponse(
        _generate(),
        media_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )
