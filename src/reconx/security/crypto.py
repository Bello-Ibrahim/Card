"""Symmetric encryption for secrets stored in MongoDB.

Uses Fernet (AES-128-CBC + HMAC-SHA256).  The key comes from
``RECONX_SECURITY_ENCRYPTION_KEY`` which in production is mounted from a
Kubernetes Secret / external secret manager - never from source control.
"""

from __future__ import annotations

import base64
import functools
import hashlib
import os

from cryptography.fernet import Fernet, InvalidToken

from reconx.common.errors import ConfigurationError, SecretResolutionError

ENC_PREFIX = "enc:"


def generate_key() -> str:
    """Generate a fresh base64 Fernet key (used by ``reconx-admin gen-key``)."""
    return Fernet.generate_key().decode()


def _coerce_key(raw: str) -> bytes:
    """Accept a real Fernet key, or derive one from an arbitrary passphrase."""
    candidate = raw.strip()
    try:
        decoded = base64.urlsafe_b64decode(candidate.encode())
        if len(decoded) == 32:
            return candidate.encode()
    except Exception:  # noqa: S110 - not base64/not 32 bytes: derive a key below
        pass
    digest = hashlib.sha256(candidate.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest)


@functools.lru_cache(maxsize=4)
def _fernet(key: str) -> Fernet:
    return Fernet(_coerce_key(key))


def get_encryption_key(explicit: str | None = None) -> str:
    key = explicit or os.getenv("RECONX_SECURITY_ENCRYPTION_KEY")
    if not key:
        raise ConfigurationError(
            "No encryption key configured. Set RECONX_SECURITY_ENCRYPTION_KEY "
            "(generate one with `reconx-admin gen-key`)."
        )
    return key


def encrypt(plaintext: str, key: str | None = None) -> str:
    """Encrypt and return an ``enc:``-prefixed secret reference."""
    if plaintext.startswith(ENC_PREFIX):
        return plaintext
    token = _fernet(get_encryption_key(key)).encrypt(plaintext.encode("utf-8")).decode()
    return f"{ENC_PREFIX}{token}"


def decrypt(reference: str, key: str | None = None) -> str:
    if not reference.startswith(ENC_PREFIX):
        return reference
    token = reference[len(ENC_PREFIX) :]
    try:
        return _fernet(get_encryption_key(key)).decrypt(token.encode()).decode("utf-8")
    except InvalidToken as exc:
        raise SecretResolutionError(
            "Failed to decrypt secret - the encryption key does not match the stored ciphertext"
        ) from exc


def is_encrypted(value: str | None) -> bool:
    return bool(value) and str(value).startswith(ENC_PREFIX)
