"""Authentication and user administration."""

from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Request, status

from reconx.api.deps import AuditDep, PrincipalDep, TokenServiceDep, UserStoreDep, audit_context, requires
from reconx.api.schemas import (
    LoginRequest,
    MessageResponse,
    TokenResponse,
    UserCreateRequest,
    UserUpdateRequest,
)
from reconx.common.logging import get_logger
from reconx.config.enums import Permission, Role
from reconx.security.audit import AuditAction
from reconx.security.rbac import ROLE_PERMISSIONS, describe_role

log = get_logger(__name__)
router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login", response_model=TokenResponse, summary="Sign in and obtain a token")
def login(
    payload: LoginRequest,
    users: UserStoreDep,
    tokens: TokenServiceDep,
    audit: AuditDep,
    request: Request,
) -> Any:
    principal = users.authenticate(payload.username, payload.password)
    if principal is None:
        audit.record(
            action=AuditAction.LOGIN_FAILED,
            entity_type="user",
            entity_id=payload.username,
            actor=payload.username,
            success=False,
            **audit_context(request),
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    audit.record(
        action=AuditAction.LOGIN,
        entity_type="user",
        entity_id=principal.username,
        actor=principal.username,
        **audit_context(request),
    )
    return tokens.issue(principal)


@router.get("/me", summary="Current principal and effective permissions")
def me(principal: PrincipalDep) -> dict[str, Any]:
    return principal.to_dict()


@router.get("/roles", summary="Roles and the permissions they grant")
def roles(principal: PrincipalDep) -> dict[str, Any]:
    return {
        "roles": [
            {"role": role.value, "permissions": describe_role(role), "count": len(ROLE_PERMISSIONS[role])}
            for role in Role
        ],
        "permissions": [p.value for p in Permission],
    }


@router.get("/users", summary="List users")
def list_users(
    users: UserStoreDep,
    principal: Annotated[Any, Depends(requires(Permission.USER_MANAGE))],
) -> dict[str, Any]:
    return {"items": users.list_users()}


@router.post("/users", status_code=201, summary="Create a user")
def create_user(
    payload: UserCreateRequest,
    users: UserStoreDep,
    principal: Annotated[Any, Depends(requires(Permission.USER_MANAGE))],
) -> dict[str, Any]:
    return users.create_user(
        payload.username,
        payload.password,
        payload.roles,
        email=payload.email,
        display_name=payload.display_name,
        created_by=principal.username,
    )


@router.put("/users/{username}", summary="Update a user")
def update_user(
    username: str,
    payload: UserUpdateRequest,
    users: UserStoreDep,
    principal: Annotated[Any, Depends(requires(Permission.USER_MANAGE))],
) -> dict[str, Any]:
    return users.update_user(
        username,
        roles=payload.roles,
        enabled=payload.enabled,
        email=payload.email,
        display_name=payload.display_name,
        password=payload.password,
        updated_by=principal.username,
    )


@router.delete("/users/{username}", summary="Delete a user")
def delete_user(
    username: str,
    users: UserStoreDep,
    principal: Annotated[Any, Depends(requires(Permission.USER_MANAGE))],
) -> MessageResponse:
    if username == principal.username:
        raise HTTPException(status_code=400, detail="You cannot delete your own account")
    users.delete_user(username)
    return MessageResponse(message=f"User '{username}' deleted")
