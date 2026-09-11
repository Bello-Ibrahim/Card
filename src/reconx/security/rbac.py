"""Role-based access control.

Roles map to a fixed permission set.  Everything in the API and UI checks
permissions (never role names) so new roles can be introduced without touching
call sites.
"""

from __future__ import annotations

from collections.abc import Iterable

from reconx.common.errors import AuthorizationError
from reconx.config.enums import Permission, Role

P = Permission

ROLE_PERMISSIONS: dict[Role, frozenset[Permission]] = {
    Role.ADMIN: frozenset(Permission),
    Role.OPERATOR: frozenset(
        {
            P.RECON_VIEW,
            P.RECON_EXECUTE,
            P.RECON_ACTIVATE,
            P.RECON_DISABLE,
            P.RUN_VIEW,
            P.RUN_CANCEL,
            P.CONNECTION_VIEW,
            P.CONNECTION_TEST,
            P.SCHEDULE_VIEW,
            P.SCHEDULE_MANAGE,
            P.REPORT_VIEW,
            P.EXCEPTION_VIEW,
        }
    ),
    Role.DEVELOPER: frozenset(
        {
            P.RECON_VIEW,
            P.RECON_CREATE,
            P.RECON_EDIT,
            P.RECON_EXECUTE,
            P.RUN_VIEW,
            P.CONNECTION_VIEW,
            P.CONNECTION_MANAGE,
            P.CONNECTION_TEST,
            P.SCHEDULE_VIEW,
            P.SCHEDULE_MANAGE,
            P.REPORT_VIEW,
            P.EXCEPTION_VIEW,
        }
    ),
    Role.VIEWER: frozenset(
        {P.RECON_VIEW, P.RUN_VIEW, P.CONNECTION_VIEW, P.SCHEDULE_VIEW, P.REPORT_VIEW, P.EXCEPTION_VIEW}
    ),
    Role.AUDITOR: frozenset(
        {
            P.RECON_VIEW,
            P.RUN_VIEW,
            P.CONNECTION_VIEW,
            P.SCHEDULE_VIEW,
            P.REPORT_VIEW,
            P.EXCEPTION_VIEW,
            P.AUDIT_VIEW,
        }
    ),
}


def permissions_for(roles: Iterable[str | Role]) -> frozenset[Permission]:
    granted: set[Permission] = set()
    for role in roles:
        try:
            role_enum = Role(role) if not isinstance(role, Role) else role
        except ValueError:
            continue
        granted |= ROLE_PERMISSIONS.get(role_enum, frozenset())
    return frozenset(granted)


def has_permission(roles: Iterable[str | Role], permission: Permission) -> bool:
    return permission in permissions_for(roles)


def require_permission(roles: Iterable[str | Role], permission: Permission, *, subject: str = "") -> None:
    if not has_permission(roles, permission):
        raise AuthorizationError(
            f"Permission '{permission.value}' is required"
            + (f" to access {subject}" if subject else ""),
            details={"required": permission.value, "roles": [str(r) for r in roles]},
        )


def describe_role(role: Role) -> list[str]:
    return sorted(p.value for p in ROLE_PERMISSIONS.get(role, frozenset()))
