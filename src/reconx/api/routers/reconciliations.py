"""Reconciliation definition endpoints."""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Depends, Query, Request

from reconx.api.deps import (
    AdvisorDep,
    AuditDep,
    ConnectionRepoDep,
    MetricsDep,
    ReconRepoDep,
    RunRepoDep,
    SchedulerDep,
    audit_context,
    requires,
)
from reconx.api.schemas import (
    CloneRequest,
    MessageResponse,
    ReconciliationCreateRequest,
    ReconciliationUpdateRequest,
    RollbackRequest,
    RunRequest,
    ValidationRequest,
    parse_definition,
)
from reconx.common.logging import get_logger
from reconx.config.enums import DefinitionStatus, Permission
from reconx.config.validation import validate_definition
from reconx.scheduler.triggers import describe, upcoming_fire_times
from reconx.security.audit import AuditAction

log = get_logger(__name__)
router = APIRouter(prefix="/api/reconciliations", tags=["reconciliations"])


@router.get("", summary="List reconciliation definitions")
def list_reconciliations(
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_VIEW))],
    status: str | None = None,
    product: str | None = None,
    customer: str | None = None,
    environment: str | None = None,
    enabled: bool | None = None,
    tag: str | None = None,
    search: str | None = None,
    limit: int = Query(default=200, ge=1, le=1000),
    offset: int = Query(default=0, ge=0),
) -> dict[str, Any]:
    items = repository.list(
        status=status,
        product=product,
        customer=customer,
        environment=environment,
        enabled=enabled,
        tag=tag,
        search=search,
        limit=limit,
        skip=offset,
    )
    return {
        "items": items,
        "total": repository.count(status=status, product=product, customer=customer),
        "limit": limit,
        "offset": offset,
    }


@router.get("/facets", summary="Distinct products, customers and tags (for UI filters)")
def facets(
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_VIEW))],
) -> dict[str, Any]:
    return {
        "products": repository.distinct("product"),
        "customers": repository.distinct("customer"),
        "environments": repository.distinct("environment"),
        "tags": repository.distinct("tags"),
        "statuses": [s.value for s in DefinitionStatus],
    }


@router.post("", status_code=201, summary="Create a reconciliation")
def create_reconciliation(
    payload: ReconciliationCreateRequest,
    repository: ReconRepoDep,
    connections: ConnectionRepoDep,
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_CREATE))],
) -> dict[str, Any]:
    definition = parse_definition(payload.model_dump(by_alias=True))
    report = validate_definition(
        definition, available_connections={c.connection_id: str(c.type) for c in connections.list()}
    )
    if not report.valid:
        return {"created": False, "validation": report.to_dict()}
    created = repository.create(definition, actor=principal.username)
    if payload.activate:
        created = repository.activate_version(created.recon_id, actor=principal.username)
    try:
        metrics.upsert_definition(created.dump())
    except Exception as exc:
        log.warning("api.definition_metrics_failed", error=str(exc)[:200])
    return {"created": True, "definition": created.dump(), "validation": report.to_dict()}


@router.get("/{recon_id}", summary="Get a reconciliation definition")
def get_reconciliation(
    recon_id: str,
    repository: ReconRepoDep,
    runs: RunRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_VIEW))],
    version: int | None = None,
) -> dict[str, Any]:
    definition = repository.get(recon_id, version=version)
    recent = runs.list(recon_id=recon_id, limit=10)
    return {
        "definition": definition.dump(),
        "schedule": {
            "description": describe(definition.schedule),
            "upcoming": [t.isoformat() for t in upcoming_fire_times(definition.schedule, 5)],
        },
        "recentRuns": recent,
        "lastRun": recent[0] if recent else None,
        "versions": [
            {
                "version": v.get("version"),
                "status": v.get("status"),
                "updatedAt": v.get("updatedAt"),
                "updatedBy": v.get("updatedBy"),
                "comment": v.get("changeComment"),
            }
            for v in repository.list_versions(recon_id, limit=25)
        ],
    }


@router.put("/{recon_id}", summary="Save a new version of a reconciliation")
def update_reconciliation(
    recon_id: str,
    payload: ReconciliationUpdateRequest,
    repository: ReconRepoDep,
    connections: ConnectionRepoDep,
    metrics: MetricsDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_EDIT))],
) -> dict[str, Any]:
    definition = parse_definition(payload.model_dump(by_alias=True))
    if definition.recon_id != recon_id:
        return {"saved": False, "error": "reconId in the payload does not match the URL"}
    report = validate_definition(
        definition, available_connections={c.connection_id: str(c.type) for c in connections.list()}
    )
    if not report.valid:
        return {"saved": False, "validation": report.to_dict()}
    saved = repository.save_new_version(
        definition,
        actor=principal.username,
        comment=payload.comment,
        expected_version=payload.expected_version,
        activate=payload.activate,
    )
    try:
        metrics.upsert_definition(saved.dump())
    except Exception as exc:
        log.warning("api.definition_metrics_failed", error=str(exc)[:200])
    return {"saved": True, "definition": saved.dump(), "validation": report.to_dict()}


@router.post("/validate", summary="Validate a definition without saving it")
def validate_payload(
    payload: ValidationRequest,
    connections: ConnectionRepoDep,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_VIEW))],
) -> dict[str, Any]:
    try:
        definition = parse_definition(payload.model_dump(by_alias=True))
    except Exception as exc:
        return {
            "valid": False,
            "errorCount": 1,
            "warningCount": 0,
            "issues": [{"severity": "ERROR", "path": "definition", "message": str(exc)[:2000]}],
        }
    known = {c.connection_id: str(c.type) for c in connections.list()}
    report = validate_definition(
        definition,
        available_connections=known,
        known_recon_ids={d["reconId"] for d in repository.list(limit=1000)},
    )
    return report.to_dict()


@router.post("/{recon_id}/validate", summary="Validate the stored definition")
def validate_stored(
    recon_id: str,
    repository: ReconRepoDep,
    connections: ConnectionRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_VIEW))],
    version: int | None = None,
) -> dict[str, Any]:
    definition = repository.get(recon_id, version=version)
    report = validate_definition(
        definition, available_connections={c.connection_id: str(c.type) for c in connections.list()}
    )
    return report.to_dict()


@router.post("/{recon_id}/activate", summary="Activate a version")
def activate(
    recon_id: str,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_ACTIVATE))],
    version: int | None = None,
) -> dict[str, Any]:
    definition = repository.activate_version(recon_id, version, actor=principal.username)
    return {"definition": definition.dump()}


@router.post("/{recon_id}/disable", summary="Disable a reconciliation")
def disable(
    recon_id: str,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_DISABLE))],
) -> dict[str, Any]:
    definition = repository.set_status(recon_id, DefinitionStatus.DISABLED, actor=principal.username)
    return {"definition": definition.dump()}


@router.post("/{recon_id}/enable", summary="Re-enable a disabled reconciliation")
def enable(
    recon_id: str,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_ACTIVATE))],
) -> dict[str, Any]:
    definition = repository.set_status(recon_id, DefinitionStatus.ACTIVE, actor=principal.username)
    return {"definition": definition.dump()}


@router.post("/{recon_id}/archive", summary="Archive a reconciliation")
def archive(
    recon_id: str,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_DELETE))],
) -> dict[str, Any]:
    definition = repository.archive(recon_id, actor=principal.username)
    return {"definition": definition.dump()}


@router.post("/{recon_id}/clone", status_code=201, summary="Clone a reconciliation")
def clone(
    recon_id: str,
    payload: CloneRequest,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_CREATE))],
) -> dict[str, Any]:
    definition = repository.clone(
        recon_id, payload.new_recon_id, actor=principal.username, new_name=payload.new_name
    )
    return {"definition": definition.dump()}


@router.get("/{recon_id}/versions", summary="List versions")
def versions(
    recon_id: str,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_VIEW))],
    limit: int = Query(default=50, ge=1, le=500),
) -> dict[str, Any]:
    return {"items": repository.list_versions(recon_id, limit=limit)}


@router.post("/{recon_id}/rollback", summary="Roll back to a previous version")
def rollback(
    recon_id: str,
    payload: RollbackRequest,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_EDIT))],
) -> dict[str, Any]:
    definition = repository.rollback(
        recon_id, payload.version, actor=principal.username, comment=payload.comment
    )
    return {"definition": definition.dump(), "rolledBackTo": payload.version}


@router.post("/{recon_id}/run", status_code=202, summary="Run now")
def run_now(
    recon_id: str,
    payload: RunRequest,
    scheduler: SchedulerDep,
    audit: AuditDep,
    request: Request,
    principal: Annotated[Any, Depends(requires(Permission.RECON_EXECUTE))],
) -> dict[str, Any]:
    run = scheduler.trigger_now(
        recon_id,
        triggered_by=principal.username,
        business_date=payload.business_date,
        parameters=payload.parameters,
        skip_conditions=payload.skip_conditions,
        profile_sources=payload.profile_sources,
        version=payload.version,
    )
    audit.record(
        action=AuditAction.EXECUTE,
        entity_type="reconciliation",
        entity_id=recon_id,
        actor=principal.username,
        details={
            "runId": run.get("runId"),
            "businessDate": run.get("businessDate"),
            "skipConditions": payload.skip_conditions,
        },
        **audit_context(request),
    )
    return run


@router.get("/{recon_id}/advice", summary="Advisor findings for the latest run")
def advice(
    recon_id: str,
    advisor: AdvisorDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_VIEW))],
    run_id: str | None = None,
) -> dict[str, Any]:
    context = advisor.build_context(recon_id=recon_id, run_id=run_id)
    return {
        "reconId": recon_id,
        "runId": context.run_id,
        "advice": [item.to_dict() for item in advisor.advise(context)],
    }


@router.delete("/{recon_id}", summary="Archive (soft delete) a reconciliation")
def delete_reconciliation(
    recon_id: str,
    repository: ReconRepoDep,
    principal: Annotated[Any, Depends(requires(Permission.RECON_DELETE))],
) -> MessageResponse:
    repository.archive(recon_id, actor=principal.username)
    return MessageResponse(
        message=f"Reconciliation '{recon_id}' archived",
        details={"hint": "Archived definitions are retained for audit and can be cloned"},
    )
