"""Reporting: trends, volumes and historical analysis."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    duration,
    empty_state,
    get_client,
    handle_api_error,
    number,
    page_header,
    percentage,
    timestamp,
    to_dataframe,
)

STATUS_COLOURS = {
    "SUCCESS": "#1a7f37",
    "PARTIAL_SUCCESS": "#9a6700",
    "FAILED": "#cf222e",
    "CANCELLED": "#57606a",
    "SKIPPED": "#8c959f",
    "RUNNING": "#0969da",
    "WAITING_FOR_DATA": "#8250df",
}

page_header("Reports", "Historical reconciliation performance", "📈")
client = get_client()

try:
    facets = client.facets()
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

filters = st.columns([1, 1.4, 1.2, 1.2, 1.2])
days = filters[0].selectbox("Period", [7, 14, 30, 90, 180, 365], index=2, format_func=lambda d: f"Last {d}d")
recon_id = filters[1].selectbox("Reconciliation", ["All", *[]] + [
    item["reconId"] for item in client.list_reconciliations(limit=500).get("items", [])
])
product = filters[2].selectbox("Product", ["All", *facets.get("products", [])])
customer = filters[3].selectbox("Customer", ["All", *facets.get("customers", [])])
status = filters[4].selectbox("Status", ["All", "SUCCESS", "PARTIAL_SUCCESS", "FAILED", "SKIPPED"])

try:
    rows = client.runs_report(
        recon_id=None if recon_id == "All" else recon_id,
        product=None if product == "All" else product,
        customer=None if customer == "All" else customer,
        status=None if status == "All" else status,
        days=days,
        limit=2000,
    )
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

if not rows:
    empty_state(
        "No runs in this period",
        "Reports read from the metrics database, which is populated as runs complete.",
        icon="📈",
    )
    st.stop()

frame = pd.DataFrame(rows)
total_read = int(frame["records_read"].fillna(0).sum())
total_matched = int(frame["records_matched"].fillna(0).sum())
metrics = st.columns(6)
metrics[0].metric("Runs", number(len(frame)))
metrics[1].metric("Records read", number(total_read))
metrics[2].metric("Matched", number(total_matched))
metrics[3].metric(
    "Match rate", percentage(total_matched / total_read * 100 if total_read else None)
)
metrics[4].metric("Exceptions", number(int(frame["exceptions"].fillna(0).sum())))
metrics[5].metric("Avg duration", duration(frame["duration_ms"].dropna().mean() if not frame.empty else None))

tabs = st.tabs(["Trend", "Volumes", "Duration", "Exceptions by reconciliation", "Run history"])

with tabs[0]:
    try:
        trend = client.trend(days=days, recon_id=None if recon_id == "All" else recon_id)
    except ApiError:
        trend = []
    if trend:
        trend_frame = pd.DataFrame(trend)
        trend_frame["day"] = pd.to_datetime(trend_frame["day"], errors="coerce")
        chart = px.bar(
            trend_frame,
            x="day",
            y="runs",
            color="status",
            color_discrete_map=STATUS_COLOURS,
            labels={"day": "", "runs": "Runs"},
            title="Runs per day by outcome",
        )
        chart.update_layout(height=380, margin=dict(l=0, r=0, t=40, b=0))
        st.plotly_chart(chart, use_container_width=True)

        match_frame = trend_frame.dropna(subset=["avg_match_percentage"])
        if not match_frame.empty:
            match_chart = px.line(
                match_frame.groupby("day", as_index=False)["avg_match_percentage"].mean(),
                x="day",
                y="avg_match_percentage",
                markers=True,
                title="Average match rate",
                labels={"day": "", "avg_match_percentage": "Match %"},
            )
            match_chart.update_traces(line_color="#1a7f37")
            match_chart.update_layout(height=300, margin=dict(l=0, r=0, t=40, b=0))
            st.plotly_chart(match_chart, use_container_width=True)
    else:
        empty_state("No trend data", icon="📈")

with tabs[1]:
    volume_frame = frame.copy()
    volume_frame["start_time"] = pd.to_datetime(volume_frame["start_time"], errors="coerce")
    chart = px.area(
        volume_frame.sort_values("start_time"),
        x="start_time",
        y=["records_matched", "records_unmatched"],
        labels={"start_time": "", "value": "Records", "variable": ""},
        color_discrete_map={"records_matched": "#1a7f37", "records_unmatched": "#cf222e"},
        title="Matched vs unmatched over time",
    )
    chart.update_layout(height=380, margin=dict(l=0, r=0, t=40, b=0))
    st.plotly_chart(chart, use_container_width=True)

with tabs[2]:
    duration_frame = frame.dropna(subset=["duration_ms"]).copy()
    if not duration_frame.empty:
        duration_frame["minutes"] = duration_frame["duration_ms"] / 60000
        chart = px.box(
            duration_frame,
            x="recon_id",
            y="minutes",
            points="outliers",
            labels={"recon_id": "", "minutes": "Minutes"},
            title="Execution duration by reconciliation",
        )
        chart.update_layout(height=400, margin=dict(l=0, r=0, t=40, b=0))
        st.plotly_chart(chart, use_container_width=True)
    else:
        empty_state("No completed runs with a duration", icon="⏱️")

with tabs[3]:
    grouped = (
        frame.groupby("recon_id", as_index=False)[["exceptions", "records_unmatched", "records_read"]]
        .sum()
        .sort_values("exceptions", ascending=False)
    )
    chart = px.bar(
        grouped.head(20),
        x="recon_id",
        y="exceptions",
        labels={"recon_id": "", "exceptions": "Exceptions"},
        title="Exceptions by reconciliation",
    )
    chart.update_traces(marker_color="#cf222e")
    chart.update_layout(height=400, margin=dict(l=0, r=0, t=40, b=0))
    st.plotly_chart(chart, use_container_width=True)
    st.dataframe(grouped, use_container_width=True, hide_index=True)

with tabs[4]:
    st.dataframe(
        to_dataframe(
            [
                {
                    "Run": row.get("run_id", "")[:8],
                    "Reconciliation": row.get("recon_id"),
                    "Status": row.get("status"),
                    "Business date": row.get("business_date"),
                    "Read": row.get("records_read"),
                    "Matched": row.get("records_matched"),
                    "Unmatched": row.get("records_unmatched"),
                    "Exceptions": row.get("exceptions"),
                    "Match %": percentage(row.get("match_percentage")),
                    "Duration": duration(row.get("duration_ms")),
                    "Started": timestamp(row.get("start_time")),
                    "Node": row.get("node"),
                }
                for row in rows
            ]
        ),
        use_container_width=True,
        hide_index=True,
        height=460,
    )
    st.download_button(
        "⬇️ Download as CSV",
        data=frame.to_csv(index=False).encode("utf-8"),
        file_name=f"reconx_runs_{days}d.csv",
        mime="text/csv",
    )
