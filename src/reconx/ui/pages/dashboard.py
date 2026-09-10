"""Dashboard: headline numbers, trends and what needs attention."""

from __future__ import annotations

from typing import Any

import pandas as pd
import plotly.express as px
import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    duration,
    empty_state,
    get_client,
    handle_api_error,
    metric_row,
    number,
    page_header,
    percentage,
    timestamp,
    to_dataframe,
)

STATUS_COLOUR_MAP = {
    "SUCCESS": "#1a7f37",
    "PARTIAL_SUCCESS": "#9a6700",
    "FAILED": "#cf222e",
    "RUNNING": "#0969da",
    "QUEUED": "#6e7781",
    "WAITING_FOR_DATA": "#8250df",
    "CANCELLED": "#57606a",
    "SKIPPED": "#8c959f",
    "STARTING": "#54aeff",
}

page_header("Dashboard", "Reconciliation health across the platform", "📊")
client = get_client()

filters = st.columns([1, 1.4, 1.4, 1])
days = filters[0].selectbox("Period", [1, 7, 14, 30, 90, 365], index=3, format_func=lambda d: f"Last {d}d")

try:
    facets = client.facets()
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

product = filters[1].selectbox("Product", ["All", *facets.get("products", [])])
customer = filters[2].selectbox("Customer", ["All", *facets.get("customers", [])])
if filters[3].button("Refresh", use_container_width=True):
    st.rerun()

try:
    summary: dict[str, Any] = client.dashboard(
        days=days,
        product=None if product == "All" else product,
        customer=None if customer == "All" else customer,
    )
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

definitions = summary.get("definitions", {})
runs = summary.get("runs", {})
volumes = summary.get("volumes", {})
schedules = summary.get("schedules", {})

metric_row(
    [
        ("Reconciliations", number(definitions.get("total")), f"{definitions.get('active', 0)} active"),
        ("Runs", number(runs.get("total")), f"{runs.get('running', 0)} in flight"),
        ("Successful", number(runs.get("success")), None),
        ("Failed", number(runs.get("failed")), None),
        ("Waiting for data", number(runs.get("waitingForData")), None),
    ]
)
metric_row(
    [
        ("Records processed", number(volumes.get("recordsRead")), None),
        ("Matched", number(volumes.get("recordsMatched")), None),
        ("Unmatched", number(volumes.get("recordsUnmatched")), None),
        ("Match rate", percentage(volumes.get("matchPercentage")), None),
        ("Avg duration", duration(volumes.get("avgDurationMs")), None),
    ]
)

st.divider()
left, right = st.columns([1.35, 1])

with left:
    st.markdown("#### Run trend")
    try:
        trend = client.trend(days=days)
    except ApiError:
        trend = []
    if trend:
        frame = pd.DataFrame(trend)
        frame["day"] = pd.to_datetime(frame["day"], errors="coerce")
        chart = px.bar(
            frame,
            x="day",
            y="runs",
            color="status",
            color_discrete_map=STATUS_COLOUR_MAP,
            labels={"day": "", "runs": "Runs", "status": "Status"},
        )
        chart.update_layout(
            height=320, margin=dict(l=0, r=0, t=10, b=0), legend=dict(orientation="h", y=-0.2)
        )
        st.plotly_chart(chart, use_container_width=True)

        matched = frame.dropna(subset=["avg_match_percentage"])
        if not matched.empty:
            match_chart = px.line(
                matched.groupby("day", as_index=False)["avg_match_percentage"].mean(),
                x="day",
                y="avg_match_percentage",
                markers=True,
                labels={"day": "", "avg_match_percentage": "Match %"},
            )
            match_chart.update_traces(line_color="#1a7f37")
            match_chart.update_layout(height=220, margin=dict(l=0, r=0, t=24, b=0), title="Match rate")
            st.plotly_chart(match_chart, use_container_width=True)
    else:
        empty_state(
            "No trend data yet",
            "Trends are read from the metrics database once runs have completed.",
            icon="📈",
        )

with right:
    st.markdown("#### Run outcomes")
    by_status = {k: v for k, v in (runs.get("byStatus") or {}).items() if v}
    if by_status:
        pie = px.pie(
            names=list(by_status.keys()),
            values=list(by_status.values()),
            hole=0.55,
            color=list(by_status.keys()),
            color_discrete_map=STATUS_COLOUR_MAP,
        )
        pie.update_layout(height=300, margin=dict(l=0, r=0, t=10, b=0), showlegend=True)
        st.plotly_chart(pie, use_container_width=True)
    else:
        empty_state("No runs in this period", icon="🕳️")

    st.markdown("#### Schedules")
    metric_row(
        [
            ("Total", number(schedules.get("total")), None),
            ("Active", number(schedules.get("enabled")), None),
            ("Paused", number(schedules.get("paused")), None),
        ]
    )

st.divider()
columns = st.columns([1.4, 1])

with columns[0]:
    st.markdown("#### Recent runs")
    try:
        recent = client.list_runs(limit=12, days=days)
    except ApiError as exc:
        handle_api_error(exc)
        recent = []
    if recent:
        frame = to_dataframe(
            [
                {
                    "Run": row.get("runId", "")[:8],
                    "Reconciliation": row.get("reconName") or row.get("reconId"),
                    "Business date": row.get("businessDate"),
                    "Status": row.get("status"),
                    "Matched": row.get("metrics", {}).get("recordsMatched"),
                    "Exceptions": row.get("metrics", {}).get("exceptions"),
                    "Duration": duration(row.get("durationMs")),
                    "Started": timestamp(row.get("startTime") or row.get("createdAt"), with_seconds=False),
                }
                for row in recent
            ]
        )
        st.dataframe(frame, use_container_width=True, hide_index=True)
    else:
        empty_state("No runs yet", "Trigger a reconciliation from the Reconciliations page.", icon="▶️")

with columns[1]:
    st.markdown("#### Needs attention")
    attention: list[dict[str, Any]] = []
    try:
        attention += client.list_runs(status="FAILED", limit=5, days=days)
        attention += client.list_runs(status="WAITING_FOR_DATA", limit=5)
    except ApiError:
        pass
    if attention:
        for row in attention[:8]:
            icon = "❌" if row.get("status") == "FAILED" else "🕒"
            with st.container(border=True):
                st.markdown(f"{icon} **{row.get('reconName') or row.get('reconId')}**")
                st.caption(
                    f"{row.get('status')} · {row.get('businessDate') or ''} · run `{row.get('runId', '')[:8]}`"
                )
                message = row.get("errorMessage") or row.get("conditionSummary")
                if message:
                    st.markdown(
                        f"<span style='font-size:0.82rem;color:#57606a'>{str(message)[:200]}</span>",
                        unsafe_allow_html=True,
                    )
    else:
        empty_state("Nothing needs attention", "No failed or waiting runs in this period.", icon="✅")
