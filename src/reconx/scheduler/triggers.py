"""Schedule evaluation: when does a reconciliation fire next?

All arithmetic happens in the schedule's own timezone and is returned in UTC,
so a "02:00 Europe/London" schedule stays at 02:00 local across DST changes.
"""

from __future__ import annotations

import calendar
from datetime import datetime, time, timedelta
from typing import Any

from croniter import croniter

from reconx.common.errors import ConfigurationError
from reconx.common.logging import get_logger
from reconx.common.timeutils import UTC, get_timezone, to_utc, utcnow
from reconx.config.enums import ScheduleType
from reconx.config.models import ScheduleSpec

log = get_logger(__name__)


def next_fire_time(
    schedule: ScheduleSpec, *, after: datetime | None = None, last_run: datetime | None = None
) -> datetime | None:
    """Next UTC firing time, or ``None`` for manual/expired schedules."""
    if not schedule.enabled or schedule.paused or schedule.type == ScheduleType.MANUAL:
        return None

    tz = get_timezone(schedule.timezone)
    reference = to_utc(after or utcnow()).astimezone(tz)

    if schedule.start_date and reference < to_utc(schedule.start_date).astimezone(tz):
        reference = to_utc(schedule.start_date).astimezone(tz)

    candidate: datetime | None
    if schedule.type == ScheduleType.CRON:
        candidate = croniter(schedule.expression or "", reference).get_next(datetime)
    elif schedule.type == ScheduleType.INTERVAL:
        interval = timedelta(seconds=int(schedule.interval_seconds or 3600))
        base = to_utc(last_run).astimezone(tz) if last_run else reference
        candidate = base + interval
        if candidate <= reference:
            # Skip whole intervals rather than firing a burst of catch-ups.
            missed = int((reference - candidate).total_seconds() // interval.total_seconds()) + 1
            candidate = candidate + interval * missed
    elif schedule.type == ScheduleType.DAILY:
        candidate = _next_daily(reference, schedule.time or "00:00")
    elif schedule.type == ScheduleType.WEEKLY:
        candidate = _next_weekly(reference, schedule.time or "00:00", schedule.days_of_week)
    elif schedule.type == ScheduleType.MONTHLY:
        candidate = _next_monthly(reference, schedule.time or "00:00", schedule.day_of_month or 1)
    elif schedule.type == ScheduleType.ONCE:
        run_at = to_utc(schedule.run_at) if schedule.run_at else None
        if run_at is None or (last_run and last_run >= run_at):
            return None
        candidate = run_at.astimezone(tz)
    elif schedule.type == ScheduleType.EVENT:
        return None  # fired by conditions/dependencies, not by the clock
    else:  # pragma: no cover - enum is exhaustive
        raise ConfigurationError(f"Unsupported schedule type '{schedule.type}'")

    if candidate is None:
        return None
    result = to_utc(candidate)
    if schedule.end_date and result > to_utc(schedule.end_date):
        return None
    return result


def _parse_time(value: str) -> time:
    hour, _, minute = value.partition(":")
    return time(hour=int(hour), minute=int(minute or 0))


def _next_daily(reference: datetime, at: str) -> datetime:
    target_time = _parse_time(at)
    candidate = reference.replace(
        hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0
    )
    if candidate <= reference:
        candidate += timedelta(days=1)
    return candidate


def _next_weekly(reference: datetime, at: str, days_of_week: list[int]) -> datetime:
    target_time = _parse_time(at)
    days = sorted({d % 7 for d in (days_of_week or [0])})
    for offset in range(0, 8):
        candidate = (reference + timedelta(days=offset)).replace(
            hour=target_time.hour, minute=target_time.minute, second=0, microsecond=0
        )
        if candidate > reference and candidate.weekday() in days:
            return candidate
    return reference + timedelta(days=7)


def _next_monthly(reference: datetime, at: str, day_of_month: int) -> datetime:
    target_time = _parse_time(at)
    year, month = reference.year, reference.month
    for _ in range(14):
        last_day = calendar.monthrange(year, month)[1]
        # Day 31 in a 30-day month means "the last day of the month".
        day = min(day_of_month, last_day)
        candidate = reference.replace(
            year=year, month=month, day=day, hour=target_time.hour, minute=target_time.minute,
            second=0, microsecond=0,
        )
        if candidate > reference:
            return candidate
        month += 1
        if month > 12:
            month, year = 1, year + 1
    raise ConfigurationError("Could not compute the next monthly firing time")


def is_due(
    schedule: ScheduleSpec,
    *,
    next_run_at: datetime | None,
    now: datetime | None = None,
) -> bool:
    """Is the stored next-run time reached (within the misfire grace window)?"""
    if next_run_at is None or not schedule.enabled or schedule.paused:
        return False
    now = now or utcnow()
    if to_utc(next_run_at) > now:
        return False
    overdue = (now - to_utc(next_run_at)).total_seconds()
    if schedule.misfire_grace_seconds and overdue > schedule.misfire_grace_seconds and not schedule.catch_up:
        log.warning(
            "schedule.misfire_skipped",
            overdue_seconds=int(overdue),
            grace_seconds=schedule.misfire_grace_seconds,
        )
        return False
    return True


def describe(schedule: ScheduleSpec) -> str:
    """Human-readable schedule description for the UI."""
    if schedule.type == ScheduleType.MANUAL:
        return "Manual only"
    if schedule.type == ScheduleType.CRON:
        return f"Cron '{schedule.expression}' ({schedule.timezone})"
    if schedule.type == ScheduleType.INTERVAL:
        seconds = int(schedule.interval_seconds or 0)
        if seconds % 3600 == 0:
            return f"Every {seconds // 3600}h"
        if seconds % 60 == 0:
            return f"Every {seconds // 60}m"
        return f"Every {seconds}s"
    if schedule.type == ScheduleType.DAILY:
        return f"Daily at {schedule.time} ({schedule.timezone})"
    if schedule.type == ScheduleType.WEEKLY:
        names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        days = ", ".join(names[d % 7] for d in sorted(schedule.days_of_week))
        return f"Weekly on {days} at {schedule.time} ({schedule.timezone})"
    if schedule.type == ScheduleType.MONTHLY:
        return f"Monthly on day {schedule.day_of_month} at {schedule.time} ({schedule.timezone})"
    if schedule.type == ScheduleType.ONCE:
        return f"Once at {schedule.run_at.isoformat() if schedule.run_at else '?'}"
    if schedule.type == ScheduleType.EVENT:
        return "Event / condition driven"
    return schedule.type.value


def upcoming_fire_times(schedule: ScheduleSpec, count: int = 5) -> list[datetime]:
    """Preview the next N firings (shown in the UI's schedule editor)."""
    times: list[datetime] = []
    cursor = utcnow()
    for _ in range(count):
        nxt = next_fire_time(schedule, after=cursor, last_run=cursor if schedule.type == ScheduleType.INTERVAL else None)
        if nxt is None:
            break
        times.append(nxt)
        cursor = nxt + timedelta(seconds=1)
    return times


def schedule_state_document(recon_id: str, schedule: ScheduleSpec, **extra: Any) -> dict[str, Any]:
    """Document persisted in ``schedule_state`` for the scheduler loop."""
    return {
        "reconId": recon_id,
        "type": schedule.type.value,
        "description": describe(schedule),
        "enabled": schedule.enabled,
        "paused": schedule.paused,
        "timezone": schedule.timezone,
        "nextRunAt": next_fire_time(schedule),
        "updatedAt": utcnow(),
        **extra,
    }


__all__ = [
    "UTC",
    "describe",
    "is_due",
    "next_fire_time",
    "schedule_state_document",
    "upcoming_fire_times",
]
