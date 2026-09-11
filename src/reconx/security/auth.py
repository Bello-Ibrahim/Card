"""User management, password hashing and JWT issuance.

Local users live in MongoDB.  The :class:`AuthenticationBackend` seam is what
an LDAP / OIDC / SAML integration plugs into: implement ``authenticate`` and
register the backend - nothing else in the platform changes.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import timedelta
from typing import Any

import bcrypt
import jwt
from pymongo.collection import Collection
from pymongo.database import Database

from reconx.common.errors import AuthenticationError, ConflictError, NotFoundError
from reconx.common.logging import get_logger
from reconx.common.timeutils import utcnow
from reconx.config.enums import Permission, Role
from reconx.config.settings import Settings, get_settings
from reconx.security.rbac import permissions_for

log = get_logger(__name__)

BCRYPT_ROUNDS = int(os.getenv("RECONX_BCRYPT_ROUNDS", "12"))

USERS_COLLECTION = "users"


@dataclass
class Principal:
    """The authenticated caller."""

    username: str
    roles: list[str] = field(default_factory=list)
    display_name: str | None = None
    email: str | None = None
    source: str = "local"
    attributes: dict[str, Any] = field(default_factory=dict)

    @property
    def permissions(self) -> frozenset[Permission]:
        return permissions_for(self.roles)

    def has(self, permission: Permission) -> bool:
        return permission in self.permissions

    def to_dict(self) -> dict[str, Any]:
        return {
            "username": self.username,
            "roles": self.roles,
            "displayName": self.display_name,
            "email": self.email,
            "source": self.source,
            "permissions": sorted(p.value for p in self.permissions),
        }


SYSTEM_PRINCIPAL = Principal(username="system", roles=[Role.ADMIN.value], source="system")
ANONYMOUS_PRINCIPAL = Principal(username="anonymous", roles=[Role.VIEWER.value], source="anonymous")


def _prehash(password: str) -> bytes:
    """SHA-256 + base64 pre-hash.

    bcrypt silently truncates anything past 72 bytes; pre-hashing keeps the full
    entropy of long passphrases and avoids null-byte truncation issues.
    """
    return base64.b64encode(hashlib.sha256(password.encode("utf-8")).digest())


def hash_password(password: str) -> str:
    return bcrypt.hashpw(_prehash(password), bcrypt.gensalt(rounds=BCRYPT_ROUNDS)).decode("ascii")


def verify_password(password: str, password_hash: str) -> bool:
    if not password_hash:
        return False
    try:
        return bcrypt.checkpw(_prehash(password), password_hash.encode("ascii"))
    except (ValueError, TypeError):  # malformed stored hash
        return False


class AuthenticationBackend(ABC):
    """Seam for LDAP/OIDC/SSO integrations."""

    name: str = "abstract"

    @abstractmethod
    def authenticate(self, username: str, password: str) -> Principal | None: ...


class MongoUserStore(AuthenticationBackend):
    """Local user directory backed by MongoDB."""

    name = "local"

    def __init__(self, database: Database, settings: Settings | None = None) -> None:
        self.db = database
        self.settings = settings or get_settings()

    @property
    def collection(self) -> Collection:
        return self.db[USERS_COLLECTION]

    def ensure_indexes(self) -> None:
        self.collection.create_index("username", unique=True, name="uq_username")
        self.collection.create_index("email", sparse=True, name="ix_email")

    def create_user(
        self,
        username: str,
        password: str,
        roles: list[str],
        *,
        email: str | None = None,
        display_name: str | None = None,
        created_by: str = "system",
    ) -> dict[str, Any]:
        if self.collection.find_one({"username": username}):
            raise ConflictError(f"User '{username}' already exists")
        invalid = [r for r in roles if r not in {role.value for role in Role}]
        if invalid:
            raise AuthenticationError(f"Unknown role(s): {invalid}")
        doc = {
            "username": username,
            "passwordHash": hash_password(password),
            "roles": roles,
            "email": email,
            "displayName": display_name or username,
            "enabled": True,
            "source": "local",
            "createdAt": utcnow(),
            "createdBy": created_by,
            "updatedAt": utcnow(),
            "failedLoginAttempts": 0,
        }
        self.collection.insert_one(doc)
        log.info("auth.user_created", username=username, roles=roles, created_by=created_by)
        return _public_user(doc)

    def update_user(
        self,
        username: str,
        *,
        roles: list[str] | None = None,
        enabled: bool | None = None,
        email: str | None = None,
        display_name: str | None = None,
        password: str | None = None,
        updated_by: str = "system",
    ) -> dict[str, Any]:
        update: dict[str, Any] = {"updatedAt": utcnow(), "updatedBy": updated_by}
        if roles is not None:
            update["roles"] = roles
        if enabled is not None:
            update["enabled"] = enabled
        if email is not None:
            update["email"] = email
        if display_name is not None:
            update["displayName"] = display_name
        if password:
            update["passwordHash"] = hash_password(password)
        doc = self.collection.find_one_and_update(
            {"username": username}, {"$set": update}, return_document=True
        )
        if not doc:
            raise NotFoundError(f"User '{username}' not found")
        log.info("auth.user_updated", username=username, updated_by=updated_by)
        return _public_user(doc)

    def delete_user(self, username: str) -> None:
        result = self.collection.delete_one({"username": username})
        if result.deleted_count == 0:
            raise NotFoundError(f"User '{username}' not found")

    def list_users(self) -> list[dict[str, Any]]:
        return [_public_user(doc) for doc in self.collection.find().sort("username", 1)]

    def get_user(self, username: str) -> dict[str, Any] | None:
        doc = self.collection.find_one({"username": username})
        return _public_user(doc) if doc else None

    def authenticate(self, username: str, password: str) -> Principal | None:
        doc = self.collection.find_one({"username": username})
        if not doc or not doc.get("enabled", True):
            # constant-ish work to avoid trivial user enumeration by timing
            verify_password(password, _DUMMY_HASH)
            return None
        if not verify_password(password, doc.get("passwordHash", "")):
            self.collection.update_one(
                {"username": username},
                {"$inc": {"failedLoginAttempts": 1}, "$set": {"lastFailedLoginAt": utcnow()}},
            )
            return None
        self.collection.update_one(
            {"username": username},
            {"$set": {"lastLoginAt": utcnow(), "failedLoginAttempts": 0}},
        )
        return Principal(
            username=doc["username"],
            roles=list(doc.get("roles", [])),
            display_name=doc.get("displayName"),
            email=doc.get("email"),
            source="local",
        )

    def bootstrap_admin(self) -> str | None:
        """Create the initial ADMIN user if the directory is empty."""
        if self.collection.count_documents({}, limit=1):
            return None
        username = self.settings.security.bootstrap_admin_username
        password = self.settings.security.bootstrap_admin_password or _generated_password()
        self.create_user(username, password, [Role.ADMIN.value], display_name="Platform Administrator")
        log.warning(
            "auth.bootstrap_admin_created",
            username=username,
            generated=self.settings.security.bootstrap_admin_password is None,
        )
        return password if self.settings.security.bootstrap_admin_password is None else None


#: Pre-computed hash used to equalise timing for unknown users.
_DUMMY_HASH = hash_password("reconx-dummy-password")


def _generated_password() -> str:
    return hashlib.sha256(os.urandom(32)).hexdigest()[:20]


def _public_user(doc: dict[str, Any]) -> dict[str, Any]:
    out = {k: v for k, v in doc.items() if k not in {"passwordHash", "_id"}}
    out["permissions"] = sorted(p.value for p in permissions_for(doc.get("roles", [])))
    return out


class TokenService:
    """Issues and validates signed JWT session tokens."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    def issue(self, principal: Principal, *, expires_minutes: int | None = None) -> dict[str, Any]:
        expiry = utcnow() + timedelta(minutes=expires_minutes or self.settings.security.jwt_expiry_minutes)
        payload = {
            "sub": principal.username,
            "roles": principal.roles,
            "name": principal.display_name,
            "email": principal.email,
            "src": principal.source,
            "iat": int(utcnow().timestamp()),
            "exp": int(expiry.timestamp()),
            "iss": "reconx",
        }
        token = jwt.encode(
            payload, self.settings.security.jwt_secret, algorithm=self.settings.security.jwt_algorithm
        )
        return {
            "accessToken": token,
            "tokenType": "bearer",
            "expiresAt": expiry.isoformat(),
            "expiresIn": int((expiry - utcnow()).total_seconds()),
            "user": principal.to_dict(),
        }

    def verify(self, token: str) -> Principal:
        try:
            payload = jwt.decode(
                token,
                self.settings.security.jwt_secret,
                algorithms=[self.settings.security.jwt_algorithm],
                issuer="reconx",
            )
        except jwt.ExpiredSignatureError as exc:
            raise AuthenticationError("Session expired - please sign in again") from exc
        except jwt.InvalidTokenError as exc:
            raise AuthenticationError("Invalid authentication token") from exc
        return Principal(
            username=payload["sub"],
            roles=list(payload.get("roles", [])),
            display_name=payload.get("name"),
            email=payload.get("email"),
            source=payload.get("src", "local"),
        )


def constant_time_equals(a: str, b: str) -> bool:
    return hmac.compare_digest(a.encode(), b.encode())
