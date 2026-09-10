"""FastAPI dependencies: settings, repositories, authentication and RBAC."""

from __future__ import annotations

import functools
from collections.abc import Callable
from typing import Annotated, Any

from fastapi import Depends, Header, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pymongo.database import Database

from reconx.advisor.chat import ReconAdvisor
from reconx.common.errors import AuthenticationError
from reconx.common.logging import get_logger
from reconx.config.enums import Permission
from reconx.config.repository import (
    ConnectionRepository,
    ReconciliationRepository,
    RunRepository,
)
from reconx.config.settings import Settings, get_settings
from reconx.config.store import get_database
from reconx.metrics.repository import MetricsRepository
from reconx.scheduler.service import SchedulerService
from reconx.security.audit import AuditLogger
from reconx.security.auth import ANONYMOUS_PRINCIPAL, MongoUserStore, Principal, TokenService
from reconx.security.rbac import require_permission

log = get_logger(__name__)

bearer_scheme = HTTPBearer(auto_error=False)


def settings_dependency() -> Settings:
    return get_settings()


SettingsDep = Annotated[Settings, Depends(settings_dependency)]


def database_dependency(settings: SettingsDep) -> Database:
    return get_database(settings)


DatabaseDep = Annotated[Database, Depends(database_dependency)]


@functools.lru_cache(maxsize=1)
def _metrics_repository() -> MetricsRepository:
    return MetricsRepository()


def metrics_dependency() -> MetricsRepository:
    return _metrics_repository()


MetricsDep = Annotated[MetricsRepository, Depends(metrics_dependency)]


def audit_dependency(db: DatabaseDep, metrics: MetricsDep) -> AuditLogger:
    return AuditLogger(db, metrics)


AuditDep = Annotated[AuditLogger, Depends(audit_dependency)]


def recon_repository(db: DatabaseDep, audit: AuditDep) -> ReconciliationRepository:
    return ReconciliationRepository(db, audit)


ReconRepoDep = Annotated[ReconciliationRepository, Depends(recon_repository)]


def connection_repository(db: DatabaseDep, audit: AuditDep) -> ConnectionRepository:
    return ConnectionRepository(db, audit)


ConnectionRepoDep = Annotated[ConnectionRepository, Depends(connection_repository)]


def run_repository(db: DatabaseDep) -> RunRepository:
    return RunRepository(db)


RunRepoDep = Annotated[RunRepository, Depends(run_repository)]


def user_store(db: DatabaseDep, settings: SettingsDep) -> MongoUserStore:
    return MongoUserStore(db, settings)


UserStoreDep = Annotated[MongoUserStore, Depends(user_store)]


def token_service(settings: SettingsDep) -> TokenService:
    return TokenService(settings)


TokenServiceDep = Annotated[TokenService, Depends(token_service)]

_scheduler_singleton: SchedulerService | None = None


def scheduler_service(db: DatabaseDep, settings: SettingsDep, metrics: MetricsDep) -> SchedulerService:
    """The API embeds a scheduler *client* - it submits and cancels runs.

    The scheduling loop itself runs in the dedicated scheduler deployment; this
    instance never calls ``start()``.
    """
    global _scheduler_singleton
    if _scheduler_singleton is None:
        _scheduler_singleton = SchedulerService(db, settings, metrics=metrics)
    return _scheduler_singleton


SchedulerDep = Annotated[SchedulerService, Depends(scheduler_service)]


def advisor_service(
    db: DatabaseDep, metrics: MetricsDep, recon_repo: ReconRepoDep, runs: RunRepoDep, settings: SettingsDep
) -> ReconAdvisor:
    return ReconAdvisor(
        metrics_repository=metrics,
        recon_repository=recon_repo,
        run_repository=runs,
        mongo_db=db,
        settings=settings,
    )


AdvisorDep = Annotated[ReconAdvisor, Depends(advisor_service)]


# --------------------------------------------------------------------------- #
# Authentication
# --------------------------------------------------------------------------- #
async def current_principal(
    request: Request,
    settings: SettingsDep,
    tokens: TokenServiceDep,
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)] = None,
    x_api_key: Annotated[str | None, Header(alias="X-API-Key")] = None,
) -> Principal:
    """Resolve the caller from a bearer token (or allow anonymous read)."""
    if not settings.security.auth_enabled:
        from reconx.security.auth import SYSTEM_PRINCIPAL

        return SYSTEM_PRINCIPAL

    token = credentials.credentials if credentials else None
    if not token and x_api_key:
        token = x_api_key
    if not token:
        if settings.security.allow_anonymous_read and request.method in ("GET", "HEAD", "OPTIONS"):
            return ANONYMOUS_PRINCIPAL
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        return tokens.verify(token)
    except AuthenticationError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=exc.message,
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


PrincipalDep = Annotated[Principal, Depends(current_principal)]


def requires(permission: Permission) -> Callable[..., Principal]:
    """Dependency factory enforcing a single permission."""

    def _dependency(principal: PrincipalDep, request: Request, audit: AuditDep) -> Principal:
        try:
            require_permission(principal.roles, permission)
        except Exception as exc:
            audit.record(
                action="PERMISSION_DENIED",
                entity_type="api",
                entity_id=request.url.path,
                actor=principal.username,
                success=False,
                details={"permission": permission.value, "method": request.method},
            )
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
        return principal

    return _dependency


def client_ip(request: Request) -> str | None:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else None


def audit_context(request: Request) -> dict[str, Any]:
    return {"source_ip": client_ip(request), "user_agent": request.headers.get("user-agent")}
