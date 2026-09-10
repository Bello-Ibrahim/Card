"""Schedule overview and control."""

from __future__ import annotations

import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    empty_state,
    get_client,
    handle_api_error,
    has_permission,
    page_header,
    render_condition_tree,
    timestamp,
    to_dataframe,
)

page_header("Schedules", "When each reconciliation fires, and what it waits for", "🗓️")
client = get_client()

columns = st.columns([1, 1, 4])
show = columns[0].selectbox("Show", ["All", "Enabled", "Paused"])
if columns[1].button("🔄 Refresh", use_container_width=True):
    st.rerun()

try:
    schedules = client.list_schedules(
        enabled=True if show == "Enabled" else (False if show == "Paused" else None)
    )
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

if show == "Paused":
    schedules = [s for s in schedules if s.get("paused")]

if not schedules:
    empty_state(
        "No schedules registered",
        "Schedules appear once a reconciliation is ACTIVE and the scheduler has ticked.",
        icon="🗓️",
    )
    st.stop()

st.dataframe(
    to_dataframe(
        [
            {
                "Reconciliation": s.get("reconId"),
                "Name": s.get("reconName"),
                "Schedule": s.get("description"),
                "Enabled": s.get("enabled"),
                "Paused": s.get("paused", False),
                "Next run": timestamp(s.get("nextRunAt")),
                "Last run": timestamp(s.get("lastRunAt")),
                "Timezone": s.get("timezone"),
            }
            for s in schedules
        ]
    ),
    use_container_width=True,
    hide_index=True,
)

st.divider()
selected = st.selectbox("Schedule", [s["reconId"] for s in schedules])
try:
    detail = client.get_schedule(selected)
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

state = detail.get("state", {})
columns = st.columns([2, 1, 1, 1])
columns[0].markdown(f"### {selected}\n{detail.get('description')}")
columns[1].metric("Next run", timestamp(state.get("nextRunAt"), with_seconds=False))
columns[2].metric("Last run", timestamp(state.get("lastRunAt"), with_seconds=False))
columns[3].metric("Paused", "Yes" if state.get("paused") else "No")

actions = st.columns(4)
manage = has_permission("schedule:manage")
if actions[0].button("⏸ Pause", use_container_width=True, disabled=not manage or state.get("paused")):
    try:
        client.pause_schedule(selected)
        st.success("Schedule paused")
        st.rerun()
    except ApiError as exc:
        handle_api_error(exc)
if actions[1].button("▶️ Resume", use_container_width=True, disabled=not manage or not state.get("paused")):
    try:
        result = client.resume_schedule(selected)
        st.success(f"Resumed — next run {timestamp(result.get('nextRunAt'))}")
        st.rerun()
    except ApiError as exc:
        handle_api_error(exc)
if actions[2].button("🧪 Evaluate conditions", use_container_width=True):
    try:
        result = client.evaluate_conditions(selected)
        (st.success if result["satisfied"] else st.warning)(result["summary"])
        st.session_state.condition_detail = result["detail"]
    except ApiError as exc:
        handle_api_error(exc)
if actions[3].button("▶️ Run now", use_container_width=True, disabled=not has_permission("recon:execute")):
    try:
        run = client.run_now(selected)
        st.success(f"Run started: `{run.get('runId')}`")
    except ApiError as exc:
        handle_api_error(exc)

tabs = st.tabs(["Upcoming firings", "Conditions", "Firing history"])

with tabs[0]:
    upcoming = detail.get("upcoming", [])
    if upcoming:
        for fire_time in upcoming:
            st.markdown(f"- {timestamp(fire_time)}")
    else:
        st.caption("This schedule has no future firings (manual, event-driven, paused or expired).")

with tabs[1]:
    if detail.get("conditions"):
        st.json(detail["conditions"])
        if st.session_state.get("condition_detail"):
            st.markdown("##### Last evaluation")
            render_condition_tree(st.session_state.condition_detail)
    else:
        st.caption(
            "No data-availability conditions. The run will start on schedule whether or not the data has "
            "landed — add conditions in the designer to hold it in WAITING_FOR_DATA instead."
        )

with tabs[2]:
    try:
        history = client.schedule_history(selected, limit=50)
    except ApiError as exc:
        handle_api_error(exc)
        history = []
    if history:
        st.dataframe(
            to_dataframe(
                [
                    {
                        "Fired at": timestamp(row.get("fired_at")),
                        "Scheduled": timestamp(row.get("scheduled_time")),
                        "Status": row.get("status"),
                        "Node": row.get("node"),
                        "Business date": row.get("business_date"),
                        "Conditions met": row.get("conditions_met"),
                        "Run": (row.get("run_id") or "")[:8],
                        "Message": (row.get("message") or "")[:80],
                    }
                    for row in history
                ]
            ),
            use_container_width=True,
            hide_index=True,
        )
    else:
        empty_state("No firing history yet", icon="🗓️")
