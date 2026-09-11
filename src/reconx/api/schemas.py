"""Request/response payloads for the control-plane API."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

from reconx.config.models import ReconciliationDefinition, _to_camel


class ApiModel(BaseModel):
    model_config = ConfigDict(alias_generator=_to_camel, populate_by_name=True, extra="forbid")


# ------------------------------------------------------------------ auth
class LoginRequest(ApiModel):
    username: str
    password: str


class TokenResponse(ApiModel):
    access_token: str
    token_type: str = "bearer"  # noqa: S105 - OAuth token type, not a secret
    expires_at: str
    expires_in: int
    user: dict[str, Any]


class UserCreateRequest(ApiModel):
    username: str = Field(min_length=2, max_length=64)
    password: str = Field(min_length=8, max_length=256)
    roles: list[str] = Field(min_length=1)
    email: str | None = None
    display_name: str | None = None


class UserUpdateRequest(ApiModel):
    roles: list[str] | None = None
    enabled: bool | None = None
    email: str | None = None
    display_name: str | None = None
    password: str | None = Field(default=None, min_length=8, max_length=256)


# --------------------------------------------------------- reconciliations
class ReconciliationCreateRequest(ApiModel):
    model_config = ConfigDict(alias_generator=_to_camel, populate_by_name=True, extra="allow")

    definition: dict[str, Any]
    comment: str | None = None
    activate: bool = False


class ReconciliationUpdateRequest(ApiModel):
    model_config = ConfigDict(alias_generator=_to_camel, populate_by_name=True, extra="allow")

    definition: dict[str, Any]
    comment: str | None = None
    expected_version: int | None = None
    activate: bool = False


class ValidationRequest(ApiModel):
    model_config = ConfigDict(alias_generator=_to_camel, populate_by_name=True, extra="allow")

    definition: dict[str, Any]


class CloneRequest(ApiModel):
    new_recon_id: str
    new_name: str | None = None


class RollbackRequest(ApiModel):
    version: int
    comment: str | None = None


class RunRequest(ApiModel):
    business_date: str | None = None
    parameters: dict[str, Any] = Field(default_factory=dict)
    skip_conditions: bool = False
    profile_sources: bool = False
    version: int | None = None


class DefinitionResponse(ApiModel):
    model_config = ConfigDict(extra="allow")

    definition: dict[str, Any]


# ------------------------------------------------------------- connections
class ConnectionRequest(ApiModel):
    model_config = ConfigDict(alias_generator=_to_camel, populate_by_name=True, extra="allow")

    connection: dict[str, Any]


class ConnectionTestRequest(ApiModel):
    model_config = ConfigDict(alias_generator=_to_camel, populate_by_name=True, extra="allow")

    connection: dict[str, Any] | None = Field(
        default=None, description="Test an unsaved connection; omit to test the stored one"
    )


class QueryPreviewRequest(ApiModel):
    """Preview a hand-written query (any dialect) before saving it."""

    query: str | None = None
    table: str | None = None
    limit: int = Field(default=100, ge=1, le=5000)
    variables: dict[str, Any] = Field(default_factory=dict)
    dialect: Literal["generic", "mssql", "postgresql", "mysql", "oracle", "db2", "sqlite"] = "generic"


class QueryPreviewResponse(ApiModel):
    columns: list[str]
    rows: list[dict[str, Any]]
    row_count: int
    truncated: bool
    elapsed_ms: int
    statement: str


# -------------------------------------------------------------------- runs
class CancelRequest(ApiModel):
    reason: str | None = None


# -------------------------------------------------------------- exceptions
class ExceptionStatusRequest(ApiModel):
    """Close out (or reassign) exceptions with a mandatory officer comment."""

    exception_ids: list[int] = Field(default_factory=list)
    status: Literal[
        "OPEN", "INVESTIGATING", "REOPENED", "RESOLVED", "CLOSED", "WONT_FIX", "FALSE_POSITIVE"
    ] = "CLOSED"
    comment: str = Field(min_length=3, max_length=8000)
    resolution_code: str | None = Field(
        default=None,
        description="Optional taxonomy code, e.g. TIMING / FX / SOURCE_ERROR / DUPLICATE_FEED",
    )
    assigned_to: str | None = None


class ExceptionBulkCloseRequest(ApiModel):
    """Close every open exception matching a filter."""

    comment: str = Field(min_length=3, max_length=8000)
    status: Literal["RESOLVED", "CLOSED", "WONT_FIX", "FALSE_POSITIVE"] = "CLOSED"
    resolution_code: str | None = None
    run_id: str | None = None
    recon_id: str | None = None
    leg_id: str | None = None
    exception_type: str | None = None
    business_date: str | None = None
    field: str | None = None
    limit: int = Field(default=5000, ge=1, le=100_000)


class ExceptionCommentRequest(ApiModel):
    comment: str = Field(min_length=1, max_length=8000)


# ---------------------------------------------------------------- advisor
class AdvisorChatRequest(ApiModel):
    question: str = Field(min_length=1, max_length=4000)
    recon_id: str | None = None
    run_id: str | None = None
    history: list[dict[str, str]] = Field(default_factory=list)
    allow_llm: bool = True


class AdvisorAnalyseRequest(ApiModel):
    recon_id: str | None = None
    run_id: str | None = None


class MatchLogicSuggestionRequest(ApiModel):
    recon_id: str | None = None
    run_id: str | None = None
    operator: Literal["AND", "OR"] = "AND"
    key_columns: list[str] = Field(default_factory=list)


# ---------------------------------------------------------------- generic
class MessageResponse(ApiModel):
    message: str
    details: dict[str, Any] = Field(default_factory=dict)


class ErrorResponse(ApiModel):
    code: str
    message: str
    details: dict[str, Any] = Field(default_factory=dict)


class PagedResponse(ApiModel):
    items: list[Any]
    total: int | None = None
    limit: int
    offset: int


def parse_definition(payload: dict[str, Any]) -> ReconciliationDefinition:
    """Accept both a bare definition and the ``{"definition": {...}}`` envelope."""
    data = payload.get("definition", payload) if isinstance(payload, dict) else payload
    if isinstance(data, dict) and "reconciliation" in data:
        data = data["reconciliation"]
    if isinstance(data, dict) and "id" in data and "reconId" not in data:
        data = {**data, "reconId": data.pop("id")}
    return ReconciliationDefinition.model_validate(data)


def isoformat(value: datetime | None) -> str | None:
    return value.isoformat() if isinstance(value, datetime) else value
