"""Shared Streamlit helpers: session state, formatting and reusable widgets."""

from __future__ import annotations

import os
from datetime import datetime
from typing import Any

import pandas as pd
import streamlit as st

from reconx.common.timeutils import format_duration
from reconx.ui.api_client import ApiError, ReconXClient

STATUS_COLOURS: dict[str, str] = {
    "SUCCESS": "#1a7f37",
    "PARTIAL_SUCCESS": "#9a6700",
    "FAILED": "#cf222e",
    "RUNNING": "#0969da",
    "STARTING": "#0969da",
    "QUEUED": "#6e7781",
    "WAITING_FOR_DATA": "#8250df",
    "CANCELLED": "#6e7781",
    "SKIPPED": "#6e7781",
    "ACTIVE": "#1a7f37",
    "DRAFT": "#6e7781",
    "DISABLED": "#9a6700",
    "ARCHIVED": "#57606a",
    "OPEN": "#cf222e",
    "INVESTIGATING": "#9a6700",
    "REOPENED": "#bc4c00",
    "RESOLVED": "#1a7f37",
    "CLOSED": "#57606a",
    "WONT_FIX": "#6e7781",
    "FALSE_POSITIVE": "#6e7781",
}

STATUS_ICONS: dict[str, str] = {
    "SUCCESS": "✅",
    "PARTIAL_SUCCESS": "⚠️",
    "FAILED": "❌",
    "RUNNING": "🔄",
    "STARTING": "🚀",
    "QUEUED": "⏳",
    "WAITING_FOR_DATA": "🕒",
    "CANCELLED": "🚫",
    "SKIPPED": "⏭️",
}

SEVERITY_ICONS = {"CRITICAL": "🔴", "WARNING": "🟠", "SUGGESTION": "🔵", "INFO": "⚪"}


# --------------------------------------------------------------------------- #
# Session / client
# --------------------------------------------------------------------------- #
def get_client() -> ReconXClient:
    """The API client for the signed-in user (or an anonymous one)."""
    if "client" not in st.session_state:
        st.session_state.client = ReconXClient(os.getenv("RECONX_API_URL", "http://localhost:8000"))
    client: ReconXClient = st.session_state.client
    client.token = st.session_state.get("token")
    return client


def current_user() -> dict[str, Any]:
    return st.session_state.get("user") or {}


def has_permission(permission: str) -> bool:
    return permission in set(current_user().get("permissions", []))


def require_permission(permission: str, *, message: str | None = None) -> bool:
    """Render a notice and return False when the user lacks a permission."""
    if has_permission(permission):
        return True
    st.info(message or f"You need the `{permission}` permission for this action.")
    return False


def logout() -> None:
    for key in ("token", "user", "client"):
        st.session_state.pop(key, None)


def handle_api_error(exc: ApiError) -> None:
    """Consistent, actionable error surface for API failures."""
    if exc.status_code == 401:
        st.error("Your session has expired. Please sign in again.")
        logout()
    elif exc.status_code == 403:
        st.error(f"Not permitted: {exc.message}")
    else:
        st.error(f"{exc.message}")
        if isinstance(exc.details, dict) and exc.details.get("details"):
            with st.expander("Error detail"):
                st.json(exc.details["details"])


# --------------------------------------------------------------------------- #
# Formatting
# --------------------------------------------------------------------------- #
def status_badge(status: str | None) -> str:
    if not status:
        return "—"
    icon = STATUS_ICONS.get(status, "")
    return f"{icon} {status.replace('_', ' ').title()}".strip()


def coloured_status(status: str | None) -> str:
    colour = STATUS_COLOURS.get(str(status), "#6e7781")
    return (
        f"<span style='background:{colour}1a;color:{colour};padding:2px 8px;border-radius:10px;"
        f"font-size:0.78rem;font-weight:600;white-space:nowrap'>{status}</span>"
    )


def number(value: Any, default: str = "—") -> str:
    if value is None:
        return default
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return str(value)


def percentage(value: Any, default: str = "—") -> str:
    if value is None:
        return default
    try:
        return f"{float(value):.2f}%"
    except (TypeError, ValueError):
        return str(value)


def duration(value: Any) -> str:
    return format_duration(value) if value is not None else "—"


def timestamp(value: Any, *, with_seconds: bool = True) -> str:
    if not value:
        return "—"
    if isinstance(value, str):
        try:
            value = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return value
    fmt = "%Y-%m-%d %H:%M:%S" if with_seconds else "%Y-%m-%d %H:%M"
    return value.strftime(fmt)


def to_dataframe(rows: list[dict[str, Any]], columns: list[str] | None = None) -> pd.DataFrame:
    frame = pd.DataFrame(rows or [])
    if columns:
        present = [c for c in columns if c in frame.columns]
        frame = frame[present] if present else frame
    return frame


# --------------------------------------------------------------------------- #
# Layout helpers
# --------------------------------------------------------------------------- #
def page_header(title: str, subtitle: str | None = None, icon: str = "") -> None:
    st.markdown(f"## {icon} {title}".strip())
    if subtitle:
        st.caption(subtitle)


def metric_row(metrics: list[tuple[str, Any, str | None]]) -> None:
    """Render a row of metrics: ``(label, value, delta)``."""
    columns = st.columns(len(metrics))
    for column, (label, value, delta) in zip(columns, metrics, strict=False):
        column.metric(label, value, delta)


def empty_state(message: str, hint: str | None = None, icon: str = "📭") -> None:
    st.markdown(
        f"<div style='text-align:center;padding:36px 12px;color:#57606a'>"
        f"<div style='font-size:2rem'>{icon}</div>"
        f"<div style='font-weight:600;margin-top:8px'>{message}</div>"
        + (f"<div style='font-size:0.86rem;margin-top:4px'>{hint}</div>" if hint else "")
        + "</div>",
        unsafe_allow_html=True,
    )


def advice_card(advice: dict[str, Any]) -> None:
    """Render one advisor finding with its evidence and applicable config."""
    icon = SEVERITY_ICONS.get(advice.get("severity", "INFO"), "⚪")
    confidence = advice.get("confidence")
    with st.container(border=True):
        header = f"{icon} **{advice.get('title')}**"
        if advice.get("legId"):
            header += f" &nbsp;·&nbsp; `{advice['legId']}`"
        st.markdown(header)
        st.markdown(
            f"<div style='color:#57606a;font-size:0.86rem'>{advice.get('category', '')}"
            + (f" · confidence {float(confidence):.0%}" if confidence is not None else "")
            + "</div>",
            unsafe_allow_html=True,
        )
        st.write(advice.get("detail", ""))
        columns = st.columns(2)
        if advice.get("evidence"):
            with columns[0].expander("Evidence"):
                st.json(advice["evidence"])
        if advice.get("suggestedConfig"):
            with columns[1].expander("Suggested configuration"):
                st.json(advice["suggestedConfig"])


def render_condition_tree(result: dict[str, Any], depth: int = 0) -> None:
    """Recursively render a condition evaluation result."""
    icon = "✅" if result.get("satisfied") else "⏳"
    indent = "&nbsp;" * (depth * 4)
    st.markdown(
        f"{indent}{icon} **{result.get('type')}** — {result.get('description')}",
        unsafe_allow_html=True,
    )
    if result.get("error"):
        st.markdown(f"{indent}&nbsp;&nbsp;⚠️ `{result['error']}`", unsafe_allow_html=True)
    for child in result.get("children", []):
        render_condition_tree(child, depth + 1)


def leg_flow_diagram(legs: list[dict[str, Any]]) -> str:
    """ASCII diagram of the leg DAG, shown in the designer and detail pages."""
    if not legs:
        return "(no legs configured)"
    lines: list[str] = []
    for index, leg in enumerate(legs):
        sources = leg.get("sources", [])
        leg_id = leg.get("id", f"leg{index}")
        left = leg.get("leftSource") or (sources[0].get("id") if sources else "?")
        right = leg.get("rightSource") or (sources[1].get("id") if len(sources) > 1 else "?")
        depends = leg.get("dependsOn") or []
        lines.append(f"  [{left}] ──┐")
        lines.append(f"            ├── ({leg_id}) ──> {leg_id}__result")
        lines.append(f"  [{right}] ──┘")
        if depends:
            lines.append(f"            ↑ depends on: {', '.join(depends)}")
        if index < len(legs) - 1:
            lines.append("")
    return "\n".join(lines)


def json_editor(label: str, value: Any, *, height: int = 300, key: str | None = None) -> Any:
    """Edit a JSON fragment with validation feedback."""
    import json

    text = st.text_area(label, value=json.dumps(value, indent=2, default=str), height=height, key=key)
    try:
        return json.loads(text) if text.strip() else None
    except json.JSONDecodeError as exc:
        st.error(f"Invalid JSON: {exc}")
        return None


def confirm_button(label: str, *, key: str, danger: bool = False, help_text: str | None = None) -> bool:
    """Two-step confirmation for destructive actions."""
    state_key = f"__confirm_{key}"
    if st.session_state.get(state_key):
        st.warning(f"Confirm: {label}?")
        columns = st.columns(2)
        if columns[0].button("Yes, proceed", key=f"{key}_yes", type="primary"):
            st.session_state[state_key] = False
            return True
        if columns[1].button("Cancel", key=f"{key}_no"):
            st.session_state[state_key] = False
        return False
    if st.button(label, key=key, type="secondary" if not danger else "primary", help=help_text):
        st.session_state[state_key] = True
        st.rerun()
    return False
