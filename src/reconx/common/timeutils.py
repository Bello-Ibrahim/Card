"""Timezone-aware time helpers.  All persisted timestamps are UTC."""

from __future__ import annotations

from datetime import UTC, date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from reconx.common.errors import ConfigurationError

UTC = UTC


def utcnow() -> datetime:
    return datetime.now(tz=UTC)


def to_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


def get_timezone(name: str | None) -> ZoneInfo | timezone:
    if not name or name.upper() == "UTC":
        return UTC
    try:
        return ZoneInfo(name)
    except (ZoneInfoNotFoundError, ValueError) as exc:  # pragma: no cover - env dependent
        raise ConfigurationError(f"Unknown timezone '{name}'") from exc


def business_date(
    reference: datetime | None = None, *, tz: str | None = None, offset_days: int = 0
) -> date:
    """Business date for a run: local calendar date in ``tz`` shifted by ``offset_days``."""
    ref = reference or utcnow()
    local = ref.astimezone(get_timezone(tz))
    return (local + timedelta(days=offset_days)).date()


def format_duration(millis: int | float | None) -> str:
    """Human readable duration, e.g. ``15m 32s``."""
    if millis is None:
        return "-"
    total_seconds = int(millis // 1000)
    hours, rem = divmod(total_seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    if hours:
        return f"{hours}h {minutes}m {seconds}s"
    if minutes:
        return f"{minutes}m {seconds}s"
    return f"{seconds}s"


def isoformat(value: datetime | None) -> str | None:
    return to_utc(value).isoformat().replace("+00:00", "Z") if value else None
