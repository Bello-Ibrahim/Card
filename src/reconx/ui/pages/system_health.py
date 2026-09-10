"""System health: dependencies, nodes, locks and event topics."""

from __future__ import annotations

import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    empty_state,
    get_client,
    handle_api_error,
    has_permission,
    page_header,
    timestamp,
    to_dataframe,
)

page_header("System Health", "Platform dependencies and cluster state", "❤️")
client = get_client()

if st.button("🔄 Refresh"):
    st.rerun()

columns = st.columns([1, 1, 2])
try:
    health = client.health()
    columns[0].metric("API", health.get("status", "?"))
    columns[1].metric("Uptime", f"{health.get('uptimeSeconds', 0) // 60} min")
    columns[2].caption(
        f"Host `{health.get('hostname')}` · version {health.get('version')} · {health.get('time')}"
    )
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

st.markdown("#### Dependencies")
try:
    readiness = client.ready()
except ApiError as exc:
    handle_api_error(exc)
    readiness = {"checks": {}}

checks = readiness.get("checks", {})
check_columns = st.columns(max(1, len(checks)))
for index, (name, payload) in enumerate(checks.items()):
    status = payload.get("status", "UNKNOWN")
    icon = {"UP": "✅", "DOWN": "❌", "DEGRADED": "⚠️", "DISABLED": "⏸️"}.get(status, "❓")
    with check_columns[index % len(check_columns)]:
        st.metric(name, f"{icon} {status}")
        if payload.get("error"):
            st.caption(payload["error"][:180])
        elif payload.get("version"):
            st.caption(f"v{payload['version']}")
        elif payload.get("brokers") is not None:
            st.caption(f"{payload['brokers']} broker(s)")

overall = readiness.get("status")
if overall == "READY":
    st.success("All required dependencies are reachable")
else:
    st.error("The platform is NOT ready — see the failing dependency above")

st.divider()
tabs = st.tabs(["Scheduler", "Distributed locks", "Configuration", "Event topics"])

with tabs[0]:
    try:
        status = client.system_status()
        columns = st.columns(5)
        columns[0].metric("Node", status.get("node", "—"))
        columns[1].metric("Scheduler ticks", status.get("ticks", 0))
        columns[2].metric("Jobs on this node", status.get("runningJobs", 0))
        columns[3].metric("Max concurrent", status.get("maxConcurrent", 0))
        columns[4].metric("Active schedules", status.get("schedules", 0))
        st.caption(
            f"Poll interval: {status.get('pollIntervalSeconds')}s. Every node runs the same loop and "
            "coordinates through MongoDB locks plus the unique run idempotency key."
        )
    except ApiError as exc:
        handle_api_error(exc)

with tabs[1]:
    if not has_permission("system:manage"):
        st.info("You need the `system:manage` permission to view locks.")
    else:
        try:
            locks = client.locks()
        except ApiError as exc:
            handle_api_error(exc)
            locks = []
        if locks:
            st.dataframe(
                to_dataframe(
                    [
                        {
                            "Lock": row.get("lockId"),
                            "Owner": row.get("owner"),
                            "Acquired": timestamp(row.get("acquiredAt")),
                            "Expires": timestamp(row.get("expiresAt")),
                            "Renewals": row.get("renewals"),
                        }
                        for row in locks
                    ]
                ),
                use_container_width=True,
                hide_index=True,
            )
            target = st.selectbox("Lock to release", [row["lockId"] for row in locks])
            st.caption(
                "Locks expire automatically (TTL). Force-release only when a node has died and you need "
                "the schedule to fire before the TTL lapses."
            )
            if st.button("🔓 Force release", type="primary"):
                try:
                    result = client.release_lock(target)
                    st.success(result.get("message", "Released"))
                    st.rerun()
                except ApiError as exc:
                    handle_api_error(exc)
        else:
            empty_state("No locks held", "Nothing is being scheduled right now.", icon="🔓")

with tabs[2]:
    if not has_permission("system:manage"):
        st.info("You need the `system:manage` permission to view the configuration.")
    else:
        try:
            info = client.system_info()
            st.json(info)
            st.caption("Secrets are never included in this payload.")
        except ApiError as exc:
            handle_api_error(exc)

with tabs[3]:
    try:
        info = client.system_info()
        kafka = info.get("kafka", {})
        st.markdown(
            f"**Kafka:** {'enabled' if kafka.get('enabled') else 'disabled'} · "
            f"`{kafka.get('bootstrapServers')}` · protocol `{kafka.get('securityProtocol')}`"
        )
        for topic in kafka.get("topics", []):
            st.markdown(f"- `{topic}`")
        st.caption(
            "Events are published asynchronously. If the broker is unavailable, events are written to the "
            "MongoDB outbox and replayed — reconciliation results are never affected."
        )
    except ApiError:
        st.caption("Configuration is only visible to administrators.")
