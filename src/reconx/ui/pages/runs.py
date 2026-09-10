"""Run monitoring and detail."""

from __future__ import annotations

import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    coloured_status,
    duration,
    empty_state,
    get_client,
    handle_api_error,
    has_permission,
    number,
    page_header,
    percentage,
    render_condition_tree,
    timestamp,
    to_dataframe,
)

page_header("Runs", "Monitor reconciliation executions", "▶️")
client = get_client()

filters = st.columns([1.4, 1.2, 1, 1, 0.9])
try:
    reconciliations = client.list_reconciliations(limit=500).get("items", [])
except ApiError as exc:
    handle_api_error(exc)
    reconciliations = []

recon_id = filters[0].selectbox("Reconciliation", ["All", *[r["reconId"] for r in reconciliations]])
status = filters[1].selectbox(
    "Status",
    ["All", "RUNNING", "QUEUED", "STARTING", "WAITING_FOR_DATA", "SUCCESS", "PARTIAL_SUCCESS",
     "FAILED", "CANCELLED", "SKIPPED"],
)
days = filters[2].selectbox("Period", [1, 7, 30, 90], index=1, format_func=lambda d: f"Last {d}d")
limit = filters[3].selectbox("Rows", [50, 100, 250, 500], index=1)
if filters[4].button("🔄 Refresh", use_container_width=True):
    st.rerun()

try:
    runs = client.list_runs(
        recon_id=None if recon_id == "All" else recon_id,
        status=None if status == "All" else status,
        days=days,
        limit=limit,
    )
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

active = [r for r in runs if r.get("status") in ("QUEUED", "STARTING", "RUNNING", "WAITING_FOR_DATA")]
if active:
    st.info(f"🔄 {len(active)} run(s) currently in flight")

if not runs:
    empty_state("No runs match these filters", icon="▶️")
    st.stop()

st.dataframe(
    to_dataframe(
        [
            {
                "Run": row.get("runId", "")[:8],
                "Reconciliation": row.get("reconName") or row.get("reconId"),
                "Status": row.get("status"),
                "Business date": row.get("businessDate"),
                "Trigger": row.get("triggerType"),
                "Node": row.get("node"),
                "Read": (row.get("metrics") or {}).get("recordsRead"),
                "Matched": (row.get("metrics") or {}).get("recordsMatched"),
                "Exceptions": (row.get("metrics") or {}).get("exceptions"),
                "Duration": duration(row.get("durationMs")),
                "Started": timestamp(row.get("startTime") or row.get("createdAt")),
            }
            for row in runs
        ]
    ),
    use_container_width=True,
    hide_index=True,
    height=330,
)

st.divider()
selected_run = st.selectbox(
    "Open a run",
    [row["runId"] for row in runs],
    format_func=lambda r: (
        f"{r[:8]} · "
        + next(
            (f"{x.get('reconId')} · {x.get('status')} · {x.get('businessDate') or ''}" for x in runs if x["runId"] == r),
            "",
        )
    ),
)

try:
    detail = client.get_run(selected_run)
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

run = detail.get("run", {})
metrics = run.get("metrics") or {}
legs = detail.get("metricsLegs") or detail.get("legs") or []

header = st.columns([2.4, 1, 1, 1])
header[0].markdown(
    f"### {run.get('reconName') or run.get('reconId')}\n"
    f"`{run.get('runId')}` · {coloured_status(run.get('status'))}",
    unsafe_allow_html=True,
)
header[1].metric("Duration", duration(run.get("durationMs")))
header[2].metric("Match rate", percentage(metrics.get("matchPercentage")))
header[3].metric("Exceptions", number(metrics.get("exceptions")))

actions = st.columns(5)
if actions[0].button("🛑 Cancel", use_container_width=True, disabled=not has_permission("run:cancel")):
    try:
        result = client.cancel_run(selected_run, "Cancelled from the UI")
        st.success(result.get("reason") or "Run cancelled")
        st.rerun()
    except ApiError as exc:
        handle_api_error(exc)
if actions[1].button("🔁 Retry", use_container_width=True, disabled=not has_permission("recon:execute")):
    try:
        result = client.retry_run(selected_run)
        st.success(f"Retry started: `{result['run'].get('runId')}`")
    except ApiError as exc:
        handle_api_error(exc)
if actions[2].button("🚨 Exceptions", use_container_width=True):
    st.session_state.exc_run = selected_run
    st.info("Open the **Exceptions** page — the run filter is pre-selected.")
if actions[3].button("💬 Ask the advisor", use_container_width=True):
    st.session_state.advisor_recon = run.get("reconId")
    st.info("Open the **Recon Advisor** page to discuss this run.")

tabs = st.tabs(["Overview", "Legs", "Sources & data quality", "Field metrics", "Conditions", "Logs", "Raw"])

with tabs[0]:
    columns = st.columns(3)
    with columns[0]:
        st.markdown("**Execution**")
        st.markdown(
            f"- Status: {run.get('status')}\n"
            f"- Trigger: {run.get('triggerType')} by {run.get('triggeredBy')}\n"
            f"- Business date: {run.get('businessDate')}\n"
            f"- Node: `{run.get('node')}`\n"
            f"- Spark app: `{run.get('sparkApplicationId') or '—'}`\n"
            f"- Version: {run.get('version')}\n"
            f"- Attempt: {run.get('attempt', 1)}"
        )
    with columns[1]:
        st.markdown("**Timing**")
        st.markdown(
            f"- Created: {timestamp(run.get('createdAt'))}\n"
            f"- Started: {timestamp(run.get('startTime'))}\n"
            f"- Ended: {timestamp(run.get('endTime'))}\n"
            f"- Duration: {duration(run.get('durationMs'))}\n"
            f"- Read: {duration(metrics.get('readTimeMs'))}\n"
            f"- Process: {duration(metrics.get('processTimeMs'))}\n"
            f"- Write: {duration(metrics.get('writeTimeMs'))}"
        )
    with columns[2]:
        st.markdown("**Volumes**")
        st.markdown(
            f"- Records read: {number(metrics.get('recordsRead'))}\n"
            f"- Matched: {number(metrics.get('recordsMatched'))}\n"
            f"- Unmatched: {number(metrics.get('recordsUnmatched'))}\n"
            f"- Duplicates: {number(metrics.get('duplicates'))}\n"
            f"- Field mismatches: {number(metrics.get('fieldMismatches'))}\n"
            f"- Exceptions: {number(metrics.get('exceptions'))}"
        )
    if run.get("errorMessage"):
        st.error(run["errorMessage"])
    if detail.get("exceptionStatus"):
        st.markdown("**Exception workflow status**")
        st.json(detail["exceptionStatus"])

with tabs[1]:
    if legs:
        st.dataframe(
            to_dataframe(
                [
                    {
                        "Leg": leg.get("leg_id") or leg.get("legId"),
                        "Status": leg.get("status"),
                        "Key": leg.get("recon_key") or leg.get("reconKey"),
                        "Matching": leg.get("match_logic") or leg.get("matchLogic"),
                        "Left": leg.get("left_records") or leg.get("leftRecords"),
                        "Right": leg.get("right_records") or leg.get("rightRecords"),
                        "Matched": leg.get("matched"),
                        "Mismatch": leg.get("mismatched"),
                        "Left only": leg.get("left_only") or leg.get("leftOnly"),
                        "Right only": leg.get("right_only") or leg.get("rightOnly"),
                        "Dup L/R": f"{leg.get('duplicates_left', 0)}/{leg.get('duplicates_right', 0)}",
                        "Match %": percentage(leg.get("match_percentage") or leg.get("matchPercentage")),
                        "Duration": duration(leg.get("duration_ms") or leg.get("durationMs")),
                    }
                    for leg in legs
                ]
            ),
            use_container_width=True,
            hide_index=True,
        )
        for leg in legs:
            if leg.get("error_message"):
                st.error(f"{leg.get('leg_id')}: {leg['error_message']}")
    else:
        empty_state("No leg results recorded", icon="🧩")

with tabs[2]:
    source_metrics = detail.get("sourceMetrics", [])
    if source_metrics:
        st.dataframe(
            to_dataframe(
                [
                    {
                        "Leg": row.get("leg_id"),
                        "Source": row.get("source_id"),
                        "Type": row.get("source_type"),
                        "Connection": row.get("connection_ref"),
                        "Records": row.get("records_read"),
                        "Columns": row.get("column_count"),
                        "Read time": duration(row.get("read_time_ms")),
                        "DQ passed": row.get("data_quality_passed"),
                    }
                    for row in source_metrics
                ]
            ),
            use_container_width=True,
            hide_index=True,
        )
        for row in source_metrics:
            if row.get("data_quality_details"):
                with st.expander(f"Data quality — {row.get('source_id')}"):
                    st.json(row["data_quality_details"])
    else:
        empty_state("No source metrics recorded", icon="📥")

with tabs[3]:
    field_metrics = detail.get("fieldMetrics", [])
    if field_metrics:
        st.dataframe(
            to_dataframe(
                [
                    {
                        "Leg": row.get("leg_id"),
                        "Rule": row.get("rule_name") or row.get("rule_id"),
                        "Field": row.get("field_name"),
                        "Compared": row.get("compared_count"),
                        "Mismatches": row.get("mismatch_count"),
                        "Mismatch %": percentage(row.get("mismatch_percentage")),
                    }
                    for row in field_metrics
                ]
            ),
            use_container_width=True,
            hide_index=True,
        )
        st.caption(
            "A field with a high mismatch rate is where the advisor looks first when recommending a "
            "different comparison rule or tolerance."
        )
    else:
        empty_state("No field-level metrics", "They are produced when a leg has field comparisons.", icon="📐")

with tabs[4]:
    try:
        conditions = client.run_conditions(selected_run)
    except ApiError as exc:
        handle_api_error(exc)
        conditions = {}
    if conditions.get("conditionResult"):
        st.markdown(f"**{conditions.get('conditionSummary')}**")
        st.caption(
            f"Waiting since {timestamp(conditions.get('waitingSince'))} · "
            f"last checked {timestamp(conditions.get('lastCheckedAt'))}"
        )
        render_condition_tree(conditions["conditionResult"])
    else:
        st.caption("This run had no data-availability conditions, or they were skipped.")

with tabs[5]:
    try:
        logs = client.run_logs(selected_run, lines=400)
    except ApiError as exc:
        handle_api_error(exc)
        logs = {}
    if logs.get("available"):
        st.code("\n".join(logs.get("lines", [])), language="log")
    else:
        st.caption(logs.get("note", "No local log available for this run."))

with tabs[6]:
    st.json(detail)
