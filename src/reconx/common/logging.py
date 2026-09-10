"""Structured JSON logging with run-scoped correlation context.

Any log record emitted anywhere in the platform can automatically carry
``recon_id`` / ``run_id`` / ``leg_id`` / ``spark_application_id`` /
``correlation_id`` because they live in :mod:`contextvars` bound once at the
start of a unit of work.  Secrets are scrubbed before serialisation.
"""

from __future__ import annotations

import contextvars
import logging
import os
import socket
import sys
import uuid
from collections.abc import Iterator, MutableMapping
from contextlib import contextmanager
from typing import Any

import structlog

_HOSTNAME = socket.gethostname()

# A ContextVar default must be immutable: a shared dict would leak fields between
# contexts. None means "empty" and every reader normalises it.
_log_context: contextvars.ContextVar[dict[str, Any] | None] = contextvars.ContextVar(
    "reconx_log_context", default=None
)

SENSITIVE_KEYS = frozenset(
    {
        "password",
        "passwd",
        "secret",
        "secret_key",
        "secretkey",
        "access_key",
        "accesskey",
        "token",
        "authorization",
        "api_key",
        "apikey",
        "private_key",
        "privatekey",
        "passphrase",
        "credentials",
        "sasl_password",
        "ssl_key_password",
        "jdbc_password",
        "smtp_password",
        "client_secret",
    }
)

REDACTED = "***REDACTED***"

#: Separator-insensitive form so snake_case, camelCase and kebab-case all match
#: (``sasl_password``, ``saslPassword`` and ``sasl-password`` are one key).
_NORMALISED_SENSITIVE = frozenset(key.replace("_", "") for key in SENSITIVE_KEYS)


def is_sensitive_key(key: str) -> bool:
    return key.lower().replace("-", "").replace("_", "") in _NORMALISED_SENSITIVE


def scrub(value: Any, _depth: int = 0) -> Any:
    """Recursively redact values whose key looks like a credential."""
    if _depth > 8:
        return value
    if isinstance(value, MutableMapping):
        out: dict[str, Any] = {}
        for k, v in value.items():
            if isinstance(k, str) and is_sensitive_key(k):
                out[k] = REDACTED
            else:
                out[k] = scrub(v, _depth + 1)
        return out
    if isinstance(value, (list, tuple)):
        return type(value)(scrub(v, _depth + 1) for v in value)
    return value


def _add_context(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    event_dict.update(_log_context.get() or {})
    event_dict.setdefault("hostname", _HOSTNAME)
    event_dict.setdefault("service", os.getenv("RECONX_SERVICE", "reconx"))
    event_dict.setdefault("pid", os.getpid())
    return event_dict


def _scrub_processor(_logger: Any, _name: str, event_dict: dict[str, Any]) -> dict[str, Any]:
    return scrub(event_dict)


_CONFIGURED = False


def configure_logging(level: str | None = None, json_output: bool | None = None) -> None:
    """Idempotently configure structlog + stdlib logging."""
    global _CONFIGURED
    level = (level or os.getenv("LOG_LEVEL", "INFO")).upper()
    if json_output is None:
        json_output = os.getenv("LOG_FORMAT", "json").lower() == "json"

    renderer: Any = (
        structlog.processors.JSONRenderer() if json_output else structlog.dev.ConsoleRenderer(colors=False)
    )

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, level, logging.INFO),
        force=True,
    )
    for noisy in ("py4j", "botocore", "boto3", "urllib3", "paramiko", "kafka", "pymongo"):
        logging.getLogger(noisy).setLevel(logging.WARNING)

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_log_level,
            _add_context,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            _scrub_processor,
            renderer,
        ],
        wrapper_class=structlog.make_filtering_bound_logger(getattr(logging, level, logging.INFO)),
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
    _CONFIGURED = True


def get_logger(name: str | None = None) -> Any:
    if not _CONFIGURED:
        configure_logging()
    return structlog.get_logger(name or "reconx")


def bind_context(**kwargs: Any) -> None:
    """Permanently bind fields to the current execution context."""
    ctx = dict(_log_context.get() or {})
    ctx.update({k: v for k, v in kwargs.items() if v is not None})
    _log_context.set(ctx)


def clear_context() -> None:
    _log_context.set(None)


def current_context() -> dict[str, Any]:
    return dict(_log_context.get() or {})


@contextmanager
def log_context(**kwargs: Any) -> Iterator[None]:
    """Temporarily bind fields for the duration of the ``with`` block."""
    token = _log_context.set(
        {**(_log_context.get() or {}), **{k: v for k, v in kwargs.items() if v is not None}}
    )
    try:
        yield
    finally:
        _log_context.reset(token)


def new_correlation_id() -> str:
    return uuid.uuid4().hex
