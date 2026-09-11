"""Exponential-backoff retry helpers.

Non-retryable :class:`~reconx.common.errors.ReconXError` subclasses are raised
immediately - the platform never loops forever on a permanent failure.
"""

from __future__ import annotations

import functools
import random
import time
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import Any, TypeVar

from reconx.common.errors import ReconXError
from reconx.common.logging import get_logger

T = TypeVar("T")
log = get_logger(__name__)

#: Java/py4j stack traces are enormous; keep logs readable and let the raised
#: exception carry the full detail.
MAX_LOGGED_ERROR_CHARS = 600


def _short(exc: BaseException) -> str:
    text = str(exc).strip().replace("\n", " | ")
    return text if len(text) <= MAX_LOGGED_ERROR_CHARS else text[:MAX_LOGGED_ERROR_CHARS] + " ...[truncated]"


@dataclass(frozen=True)
class RetryPolicy:
    """Configurable exponential backoff with optional jitter."""

    max_attempts: int = 3
    initial_delay_seconds: float = 2.0
    max_delay_seconds: float = 60.0
    multiplier: float = 2.0
    jitter: bool = True

    def delay_for(self, attempt: int) -> float:
        """Delay *before* attempt number ``attempt`` (1-based, first has no delay)."""
        if attempt <= 1:
            return 0.0
        raw = self.initial_delay_seconds * (self.multiplier ** (attempt - 2))
        raw = min(raw, self.max_delay_seconds)
        if self.jitter:
            raw = raw * (0.5 + random.random() / 2)  # noqa: S311 - jitter, not crypto
        return round(raw, 3)

    @classmethod
    def from_config(cls, cfg: dict[str, Any] | None) -> RetryPolicy:
        cfg = cfg or {}
        return cls(
            max_attempts=int(cfg.get("maxAttempts", cfg.get("max_attempts", 3))),
            initial_delay_seconds=float(
                cfg.get("initialDelaySeconds", cfg.get("initial_delay_seconds", 2.0))
            ),
            max_delay_seconds=float(cfg.get("maxDelaySeconds", cfg.get("max_delay_seconds", 60.0))),
            multiplier=float(cfg.get("multiplier", 2.0)),
            jitter=bool(cfg.get("jitter", True)),
        )


DEFAULT_POLICY = RetryPolicy()


def is_retryable(exc: BaseException) -> bool:
    if isinstance(exc, ReconXError):
        return exc.retryable
    # Unknown/infra errors (socket, driver, IO) are assumed transient.
    return isinstance(exc, (OSError, TimeoutError, ConnectionError))


def call_with_retry(
    fn: Callable[[], T],
    *,
    policy: RetryPolicy = DEFAULT_POLICY,
    operation: str = "operation",
    retry_on: Iterable[type[BaseException]] | None = None,
    sleep: Callable[[float], None] = time.sleep,
) -> T:
    """Invoke ``fn`` with exponential backoff, honouring retryability."""
    retry_types = tuple(retry_on) if retry_on else ()
    last: BaseException | None = None
    for attempt in range(1, max(1, policy.max_attempts) + 1):
        delay = policy.delay_for(attempt)
        if delay:
            log.warning("retry.backoff", operation=operation, attempt=attempt, delay_seconds=delay)
            sleep(delay)
        try:
            return fn()
        except BaseException as exc:
            last = exc
            retryable = is_retryable(exc) or (retry_types and isinstance(exc, retry_types))
            if not retryable or attempt >= policy.max_attempts:
                log.error(
                    "retry.giving_up",
                    operation=operation,
                    attempt=attempt,
                    retryable=bool(retryable),
                    error=_short(exc),
                )
                raise
            log.warning("retry.failed_attempt", operation=operation, attempt=attempt, error=_short(exc))
    assert last is not None
    raise last


def retry(
    policy: RetryPolicy = DEFAULT_POLICY,
    *,
    operation: str | None = None,
    retry_on: Iterable[type[BaseException]] | None = None,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator form of :func:`call_with_retry`."""

    def decorator(fn: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            return call_with_retry(
                lambda: fn(*args, **kwargs),
                policy=policy,
                operation=operation or fn.__qualname__,
                retry_on=retry_on,
            )

        return wrapper

    return decorator
