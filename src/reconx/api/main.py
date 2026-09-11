"""The ReconX control-plane API.

A stateless FastAPI service: every piece of state lives in MongoDB, the metrics
database or Kafka, so any number of replicas can run behind a load balancer.
"""

from __future__ import annotations

import time
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from reconx import __version__
from reconx.api.routers import (
    advisor,
    auth,
    connections,
    exceptions,
    reconciliations,
    reports,
    runs,
    schedules,
    system,
)
from reconx.common.errors import (
    AuthenticationError,
    AuthorizationError,
    ConflictError,
    NotFoundError,
    ReconXError,
    ValidationError,
)
from reconx.common.logging import (
    bind_context,
    clear_context,
    configure_logging,
    get_logger,
    new_correlation_id,
)
from reconx.config.settings import Settings, get_settings

log = get_logger(__name__)

DESCRIPTION = """
Control plane for the **ReconX** enterprise data reconciliation platform.

* **Reconciliations** - versioned, configuration-driven definitions with multi-leg DAG execution
* **Connections** - S3, StorageGRID, SFTP, JDBC, Kafka and filesystem, with secrets never stored in clear
* **Runs** - submit, monitor and cancel distributed Spark jobs
* **Exceptions** - review, comment on and close out breaks with a full audit trail
* **Advisor** - evidence-based recommendations on keys, matching logic and tolerances
"""


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    settings: Settings = get_settings()
    configure_logging(settings.log_level, json_output=settings.log_format == "json")
    log.info("api.starting", version=__version__, environment=settings.environment)

    _warn_on_insecure_defaults(settings)

    try:
        from reconx.config.store import ensure_indexes, get_database
        from reconx.security.auth import MongoUserStore

        database = get_database(settings)
        ensure_indexes(database, settings)
        generated = MongoUserStore(database, settings).bootstrap_admin()
        if generated:
            log.warning(
                "api.bootstrap_admin_password_generated",
                username=settings.security.bootstrap_admin_username,
                password=generated,
                hint="Sign in and change this password immediately; it is shown only once.",
            )
    except Exception as exc:
        log.error("api.mongo_initialisation_failed", error=str(exc)[:400])

    if settings.result_db.auto_create_schema:
        try:
            from reconx.metrics.repository import MetricsRepository

            MetricsRepository(settings=settings).create_schema()
        except Exception as exc:
            log.error("api.metrics_schema_failed", error=str(exc)[:400])

    yield
    log.info("api.stopping")


def create_app(settings: Settings | None = None) -> FastAPI:
    settings = settings or get_settings()
    app = FastAPI(
        title="ReconX Control Plane",
        description=DESCRIPTION,
        version=__version__,
        lifespan=lifespan,
        root_path=settings.api.root_path,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        contact={"name": "ReconX Platform Team"},
        license_info={"name": "Apache-2.0"},
    )

    origins = [o.strip() for o in settings.api.cors_origins.split(",") if o.strip()]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Correlation-Id"],
    )

    @app.middleware("http")
    async def correlation_middleware(request: Request, call_next: Any) -> Any:
        """Attach a correlation id to every request, response and log line."""
        correlation_id = request.headers.get("X-Correlation-Id") or new_correlation_id()
        bind_context(correlation_id=correlation_id, service="reconx-api")
        started = time.perf_counter()
        try:
            response = await call_next(request)
        finally:
            duration_ms = int((time.perf_counter() - started) * 1000)
            clear_context()
        response.headers["X-Correlation-Id"] = correlation_id
        if not request.url.path.startswith(("/health", "/ready", "/metrics")):
            log.info(
                "api.request",
                method=request.method,
                path=request.url.path,
                status=response.status_code,
                duration_ms=duration_ms,
                correlation_id=correlation_id,
            )
        return response

    @app.middleware("http")
    async def security_headers(request: Request, call_next: Any) -> Any:
        response = await call_next(request)
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "no-referrer")
        response.headers.setdefault("Cache-Control", "no-store")
        return response

    _register_exception_handlers(app)

    app.include_router(system.router)
    app.include_router(auth.router)
    app.include_router(reconciliations.router)
    app.include_router(connections.router)
    app.include_router(runs.router)
    app.include_router(schedules.router)
    app.include_router(exceptions.router)
    app.include_router(reports.router)
    app.include_router(advisor.router)

    @app.get("/", include_in_schema=False)
    def root() -> dict[str, Any]:
        return {
            "name": "ReconX Control Plane",
            "version": __version__,
            "documentation": "/docs",
            "openapi": "/openapi.json",
            "health": "/health",
        }

    return app


def _register_exception_handlers(app: FastAPI) -> None:
    status_for: dict[type[ReconXError], int] = {
        NotFoundError: 404,
        ConflictError: 409,
        ValidationError: 422,
        AuthenticationError: 401,
        AuthorizationError: 403,
    }

    @app.exception_handler(ReconXError)
    async def reconx_error_handler(request: Request, exc: ReconXError) -> JSONResponse:
        status_code = next(
            (code for error_type, code in status_for.items() if isinstance(exc, error_type)), 400
        )
        log.warning(
            "api.error",
            code=exc.code,
            status=status_code,
            path=request.url.path,
            message=exc.message[:300],
        )
        return JSONResponse(status_code=status_code, content=exc.to_dict())

    @app.exception_handler(Exception)
    async def unhandled_handler(request: Request, exc: Exception) -> JSONResponse:
        log.exception("api.unhandled_error", path=request.url.path, error=str(exc)[:400])
        return JSONResponse(
            status_code=500,
            content={
                "code": "INTERNAL_ERROR",
                "message": "An unexpected error occurred. Check the API logs with the correlation id.",
                "details": {},
            },
        )


def _warn_on_insecure_defaults(settings: Settings) -> None:
    """Fail loudly (in logs) when production is running with development defaults."""
    if settings.environment.lower() in {"local", "dev", "development", "test"}:
        return
    problems: list[str] = []
    if settings.security.jwt_secret == "change-me-in-production":  # noqa: S105 - the default marker
        problems.append("RECONX_SECURITY_JWT_SECRET is still the default value")
    if not settings.security.encryption_key:
        problems.append("RECONX_SECURITY_ENCRYPTION_KEY is not set - connection secrets cannot be encrypted")
    if not settings.security.auth_enabled:
        problems.append("Authentication is disabled (RECONX_SECURITY_AUTH_ENABLED=false)")
    if settings.api.cors_origins == "*":
        problems.append("API_CORS_ORIGINS is '*' - restrict it to your UI origin")
    for problem in problems:
        log.error("api.insecure_configuration", problem=problem, environment=settings.environment)


app = create_app()


def run() -> None:
    """Console-script entry point (``reconx-api``)."""
    import uvicorn

    settings = get_settings()
    uvicorn.run(
        "reconx.api.main:app",
        host=settings.api.host,
        port=settings.api.port,
        workers=settings.api.workers,
        log_config=None,
        access_log=False,
        proxy_headers=True,
        forwarded_allow_ips="*",
    )


if __name__ == "__main__":  # pragma: no cover
    run()
