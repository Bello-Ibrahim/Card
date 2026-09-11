"""Safe ``${variable}`` substitution for configuration values.

Only whitelisted variables are resolved.  This deliberately does **not** use
``eval``/``exec``/Jinja code execution: configuration comes from the UI and must
never be able to run arbitrary Python.
"""

from __future__ import annotations

import re
from collections.abc import Callable, Mapping
from datetime import date, datetime, timedelta
from typing import Any

from reconx.common.errors import ConfigurationError
from reconx.common.timeutils import business_date, utcnow

_VAR_RE = re.compile(r"\$\{([a-zA-Z_][a-zA-Z0-9_]*)(?::([^}]*))?\}")
_MAX_DEPTH = 5


def build_run_variables(
    *,
    recon_id: str | None = None,
    run_id: str | None = None,
    biz_date: date | None = None,
    timezone_name: str | None = None,
    extra: Mapping[str, Any] | None = None,
) -> dict[str, str]:
    """Standard variable set exposed to configuration templates."""
    bdate = biz_date or business_date(tz=timezone_name)
    now = utcnow()
    variables: dict[str, str] = {
        "business_date": bdate.isoformat(),
        "business_date_compact": bdate.strftime("%Y%m%d"),
        "business_date_yyyy": bdate.strftime("%Y"),
        "business_date_mm": bdate.strftime("%m"),
        "business_date_dd": bdate.strftime("%d"),
        "prev_business_date": (bdate - timedelta(days=1)).isoformat(),
        "prev_business_date_compact": (bdate - timedelta(days=1)).strftime("%Y%m%d"),
        "next_business_date": (bdate + timedelta(days=1)).isoformat(),
        "run_timestamp": now.strftime("%Y%m%dT%H%M%SZ"),
        "run_date": now.date().isoformat(),
    }
    if recon_id:
        variables["recon_id"] = recon_id
    if run_id:
        variables["run_id"] = run_id
    for key, value in (extra or {}).items():
        if value is None:
            continue
        variables[str(key)] = value.isoformat() if isinstance(value, (date, datetime)) else str(value)
    return variables


def render(value: str, variables: Mapping[str, Any], *, strict: bool = True) -> str:
    """Substitute ``${var}`` / ``${var:default}`` tokens in ``value``."""
    if "${" not in value:
        return value
    current = value
    for _ in range(_MAX_DEPTH):
        missing: list[str] = []
        rendered = _VAR_RE.sub(_make_replacer(variables, missing), current)
        if missing and strict:
            raise ConfigurationError(
                f"Unresolved template variable(s): {', '.join(sorted(set(missing)))}",
                details={"value": value, "available": sorted(variables.keys())},
            )
        if rendered == current:
            return rendered
        current = rendered
    return current


def _make_replacer(
    variables: Mapping[str, Any], missing: list[str]
) -> Callable[[re.Match[str]], str]:
    """Substitution callback that records the names it could not resolve."""

    def _replace(match: re.Match[str]) -> str:
        name, default = match.group(1), match.group(2)
        if name in variables and variables[name] is not None:
            return str(variables[name])
        if default is not None:
            return default
        missing.append(name)
        return match.group(0)

    return _replace


def render_deep(obj: Any, variables: Mapping[str, Any], *, strict: bool = True) -> Any:
    """Recursively render every string inside dicts/lists/tuples."""
    if isinstance(obj, str):
        return render(obj, variables, strict=strict)
    if isinstance(obj, Mapping):
        return {k: render_deep(v, variables, strict=strict) for k, v in obj.items()}
    if isinstance(obj, list):
        return [render_deep(v, variables, strict=strict) for v in obj]
    if isinstance(obj, tuple):
        return tuple(render_deep(v, variables, strict=strict) for v in obj)
    return obj
