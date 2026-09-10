"""Identifier and idempotency-key generation."""

from __future__ import annotations

import hashlib
import re
import uuid
from collections.abc import Mapping
from typing import Any

_SLUG_RE = re.compile(r"[^a-zA-Z0-9_.-]+")


def new_run_id() -> str:
    """Globally unique run identifier (UUID4, hex-with-dashes)."""
    return str(uuid.uuid4())


def slug(value: str) -> str:
    return _SLUG_RE.sub("-", value.strip()).strip("-").lower()


def idempotency_key(recon_id: str, version: int, dimensions: Mapping[str, Any] | None = None) -> str:
    """Deterministic key preventing two nodes from starting the same logical run.

    The key is built from ``recon_id`` + ``version`` + the configured business
    dimensions (typically ``business_date``).  Two scheduler nodes computing the
    same key will collide on the unique index and only one wins.
    """
    parts = [recon_id, str(version)]
    for key in sorted((dimensions or {}).keys()):
        parts.append(f"{key}={dimensions[key]}")  # type: ignore[index]
    raw = "|".join(parts)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]
    return f"{slug(recon_id)}:{version}:{digest}"


def deterministic_id(*parts: Any) -> str:
    raw = "|".join(str(p) for p in parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()
