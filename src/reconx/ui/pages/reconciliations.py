"""Reconciliation catalogue and detail view."""

from __future__ import annotations

from typing import Any

import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    coloured_status,
    duration,
    empty_state,
    get_client,
    handle_api_error,
    has_permission,
    leg_flow_diagram,
    number,
    page_header,
    percentage,
    timestamp,
    to_dataframe,
)

page_header("Reconciliations", "Every reconciliation definition on the platform", "🧾")
client = get_client()

try:
    facets = client.facets()
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

filters = st.columns([1, 1, 1, 1, 1.6])
status = filters[0].selectbox("Status", ["All", *facets.get("statuses", [])])
product = filters[1].selectbox("Product", ["All", *facets.get("products", [])])
customer = filters[2].selectbox("Customer", ["All", *facets.get("customers", [])])
environment = filters[3].selectbox("Environment", ["All", *facets.get("environments", [])])
search = filters[4].text_input("Search", placeholder="id, name or description")

try:
    payload = client.list_reconciliations(
        status=None if status == "All" else status,
        product=None if product == "All" else product,
        customer=None if customer == "All" else customer,
        environment=None if environment == "All" else environment,
        search=search or None,
        limit=500,
    )
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

items: list[dict[str, Any]] = payload.get("items", [])
if not items:
    empty_state(
        "No reconciliations found",
        "Create one in the Reconciliation Designer.",
        icon="🧾",
    )
    st.stop()

st.caption(f"{len(items)} reconciliation(s)")
frame = to_dataframe(
    [
        {
            "ID": item.get("reconId"),
            "Name": item.get("name"),
            "Status": item.get("status"),
            "Version": item.get("version"),
            "Product": item.get("product"),
            "Customer": item.get("customer"),
            "Legs": len(item.get("legs", [])),
            "Schedule": (item.get("schedule") or {}).get("type"),
            "Updated": timestamp(item.get("updatedAt"), with_seconds=False),
            "Updated by": item.get("updatedBy"),
        }
        for item in items
    ]
)
st.dataframe(frame, use_container_width=True, hide_index=True, height=280)

st.divider()
selected_id = st.selectbox(
    "Open a reconciliation",
    [item["reconId"] for item in items],
    format_func=lambda i: f"{i} — {next((x.get('name') for x in items if x['reconId'] == i), '')}",
)

try:
    detail = client.get_reconciliation(selected_id)
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

definition = detail["definition"]
schedule_info = detail.get("schedule", {})
recent_runs = detail.get("recentRuns", [])

header = st.columns([2.6, 1, 1, 1])
header[0].markdown(
    f"### {definition.get('name')}\n"
    f"`{definition.get('reconId')}` · version {definition.get('version')} · "
    f"{coloured_status(definition.get('status'))}",
    unsafe_allow_html=True,
)
header[1].metric("Legs", number(len(definition.get("legs", []))))
header[2].metric("Schedule", (definition.get("schedule") or {}).get("type", "manual"))
last_run = detail.get("lastRun") or {}
header[3].metric("Last run", last_run.get("status", "—"))

actions = st.columns(6)
if actions[0].button("▶️ Run now", use_container_width=True, disabled=not has_permission("recon:execute")):
    st.session_state.show_run_dialog = True
if actions[1].button("✅ Activate", use_container_width=True, disabled=not has_permission("recon:activate")):
    try:
        client.activate(selected_id)
        st.success("Activated")
        st.rerun()
    except ApiError as exc:
        handle_api_error(exc)
if actions[2].button("⏸ Disable", use_container_width=True, disabled=not has_permission("recon:disable")):
    try:
        client.disable(selected_id)
        st.success("Disabled")
        st.rerun()
    except ApiError as exc:
        handle_api_error(exc)
if actions[3].button("📋 Clone", use_container_width=True, disabled=not has_permission("recon:create")):
    st.session_state.show_clone_dialog = True
if actions[4].button("🛠️ Edit", use_container_width=True):
    st.session_state.designer_definition = definition
    st.session_state.designer_loaded_version = definition.get("version")
    st.success("Loaded into the designer — switch to **Reconciliation Designer**.")
if actions[5].button("🗄 Archive", use_container_width=True, disabled=not has_permission("recon:delete")):
    try:
        client.archive(selected_id)
        st.success("Archived")
        st.rerun()
    except ApiError as exc:
        handle_api_error(exc)

if st.session_state.get("show_run_dialog"):
    with st.form("run_now_form"):
        st.markdown("##### Run now")
        columns = st.columns(3)
        business_date = columns[0].text_input("Business date", "", placeholder="YYYY-MM-DD (default: today)")
        skip_conditions = columns[1].checkbox("Skip data-availability conditions")
        profile_sources = columns[2].checkbox(
            "Profile sources", help="Collects column statistics for the advisor (adds a Spark pass)"
        )
        parameters: dict[str, str] = {}
        for variable in definition.get("variables", []):
            parameters[variable["name"]] = st.text_input(
                f"{variable.get('label') or variable['name']}",
                variable.get("default") or "",
                key=f"runvar_{variable['name']}",
            )
        if st.form_submit_button("Start run", type="primary"):
            try:
                run = client.run_now(
                    selected_id,
                    businessDate=business_date or None,
                    parameters={k: v for k, v in parameters.items() if v},
                    skipConditions=skip_conditions,
                    profileSources=profile_sources,
                )
                st.session_state.show_run_dialog = False
                if run.get("status") == "WAITING_FOR_DATA":
                    st.warning(f"Run queued but waiting for data: {run.get('conditionSummary')}")
                else:
                    st.success(f"Run started: `{run.get('runId')}`")
            except ApiError as exc:
                handle_api_error(exc)

if st.session_state.get("show_clone_dialog"):
    with st.form("clone_form"):
        st.markdown("##### Clone reconciliation")
        new_id = st.text_input("New reconciliation ID", f"{selected_id}_copy")
        new_name = st.text_input("New name", f"{definition.get('name')} (copy)")
        if st.form_submit_button("Clone", type="primary"):
            try:
                client.clone(selected_id, new_id, new_name)
                st.session_state.show_clone_dialog = False
                st.success(f"Cloned to '{new_id}' as a draft")
                st.rerun()
            except ApiError as exc:
                handle_api_error(exc)

tabs = st.tabs(["Overview", "Legs", "Schedule & conditions", "Runs", "Versions", "Advisor", "Raw"])

with tabs[0]:
    columns = st.columns(2)
    with columns[0]:
        st.markdown("**Definition**")
        st.markdown(
            f"- Description: {definition.get('description') or '—'}\n"
            f"- Product / customer: {definition.get('product') or '—'} / {definition.get('customer') or '—'}\n"
            f"- Environment: {definition.get('environment') or '—'}\n"
            f"- Tags: {', '.join(definition.get('tags', [])) or '—'}\n"
            f"- Owner: {definition.get('owner') or '—'}\n"
            f"- Created: {timestamp(definition.get('createdAt'))} by {definition.get('createdBy') or '—'}\n"
            f"- Updated: {timestamp(definition.get('updatedAt'))} by {definition.get('updatedBy') or '—'}"
        )
    with columns[1]:
        st.markdown("**Variables**")
        if definition.get("variables"):
            st.dataframe(
                [
                    {
                        "Name": v["name"],
                        "Label": v.get("label"),
                        "Type": v.get("type"),
                        "Default": v.get("default"),
                    }
                    for v in definition["variables"]
                ],
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.caption("No declared variables (built-ins such as ${business_date} are always available).")

with tabs[1]:
    st.code(leg_flow_diagram(definition.get("legs", [])), language="text")
    for leg in definition.get("legs", []):
        with st.expander(f"Leg `{leg.get('id')}` — {leg.get('name') or ''}", expanded=False):
            columns = st.columns(2)
            with columns[0]:
                st.markdown("**Sources**")
                for source in leg.get("sources", []):
                    location = (
                        source.get("table")
                        or source.get("path")
                        or source.get("topic")
                        or source.get("view")
                        or source.get("legRef")
                        or ("query" if source.get("query") else "—")
                    )
                    st.markdown(
                        f"- `{source.get('id')}` — **{source.get('type')}** → {location}"
                        + (f" (`{source.get('connectionRef')}`)" if source.get("connectionRef") else "")
                    )
                    if source.get("query"):
                        st.code(source["query"], language="sql")
                st.markdown("**Keys**")
                for key in leg.get("keys", []):
                    st.markdown(f"- `{key.get('left')}` ↔ `{key.get('right')}`")
            with columns[1]:
                st.markdown("**Matching logic**")
                logic = leg.get("matchLogic")
                if logic:
                    labels = [
                        ("NOT " if r.get("negate") else "") + (r.get("name") or r.get("id"))
                        for r in logic.get("rules", [])
                    ]
                    operator = logic.get("operator", "AND")
                    expression = f" {operator} ".join(labels)
                    st.info(f"Match when: **{expression}**")
                    for rule in logic.get("rules", []):
                        st.markdown(f"**{rule.get('name') or rule.get('id')}** ({rule.get('operator')})")
                        for comparison in rule.get("comparisons", []):
                            tolerance = (
                                f" ± {comparison['tolerance']}" if comparison.get("tolerance") else ""
                            )
                            st.markdown(
                                f"   - `{comparison.get('left')}` vs `{comparison.get('right')}` "
                                f"— {comparison.get('rule')}{tolerance}"
                            )
                elif leg.get("comparisons"):
                    for comparison in leg["comparisons"]:
                        st.markdown(
                            f"- `{comparison.get('left')}` vs `{comparison.get('right')}` "
                            f"— {comparison.get('rule', 'exact')}"
                        )
                else:
                    st.caption("Presence only (no value comparison configured)")

                if leg.get("exceptionColumns"):
                    st.markdown("**Exception context columns**")
                    st.markdown(
                        ", ".join(f"`{c.get('alias')}`" for c in leg["exceptionColumns"])
                    )
                if leg.get("outputs"):
                    st.markdown("**Outputs**")
                    for output in leg["outputs"]:
                        st.markdown(
                            f"- {output.get('type')} → "
                            f"{output.get('table') or output.get('path') or output.get('topic') or output.get('view')}"
                        )

with tabs[2]:
    columns = st.columns(2)
    with columns[0]:
        st.markdown("**Schedule**")
        st.markdown(f"- {schedule_info.get('description', '—')}")
        upcoming = schedule_info.get("upcoming", [])
        if upcoming:
            st.markdown("**Next firings**")
            for fire_time in upcoming:
                st.markdown(f"- {timestamp(fire_time)}")
    with columns[1]:
        st.markdown("**Data-availability conditions**")
        if definition.get("conditions"):
            st.json(definition["conditions"])
            if st.button("🧪 Evaluate now"):
                try:
                    result = client.evaluate_conditions(selected_id)
                    (st.success if result["satisfied"] else st.warning)(result["summary"])
                    st.json(result["detail"])
                except ApiError as exc:
                    handle_api_error(exc)
        else:
            st.caption("None configured — runs start regardless of whether the data has landed.")

with tabs[3]:
    if recent_runs:
        st.dataframe(
            to_dataframe(
                [
                    {
                        "Run": row.get("runId", "")[:8],
                        "Status": row.get("status"),
                        "Business date": row.get("businessDate"),
                        "Trigger": row.get("triggerType"),
                        "Matched": (row.get("metrics") or {}).get("recordsMatched"),
                        "Unmatched": (row.get("metrics") or {}).get("recordsUnmatched"),
                        "Exceptions": (row.get("metrics") or {}).get("exceptions"),
                        "Match %": percentage((row.get("metrics") or {}).get("matchPercentage")),
                        "Duration": duration(row.get("durationMs")),
                        "Started": timestamp(row.get("startTime") or row.get("createdAt")),
                    }
                    for row in recent_runs
                ]
            ),
            use_container_width=True,
            hide_index=True,
        )
    else:
        empty_state("No runs yet", icon="▶️")

with tabs[4]:
    versions = detail.get("versions", [])
    if versions:
        st.dataframe(
            to_dataframe(
                [
                    {
                        "Version": v.get("version"),
                        "Status": v.get("status"),
                        "Updated": timestamp(v.get("updatedAt")),
                        "By": v.get("updatedBy"),
                        "Comment": v.get("comment"),
                    }
                    for v in versions
                ]
            ),
            use_container_width=True,
            hide_index=True,
        )
        columns = st.columns([1, 1, 2])
        target = columns[0].number_input(
            "Version", min_value=1, value=int(versions[-1].get("version", 1)), step=1
        )
        comment = columns[1].text_input("Rollback comment", "")
        if columns[2].button("↩️ Roll back", disabled=not has_permission("recon:edit")):
            try:
                result = client.rollback(selected_id, int(target), comment or None)
                st.success(
                    f"Rolled back to version {target} — published as version "
                    f"{result['definition']['version']}"
                )
                st.rerun()
            except ApiError as exc:
                handle_api_error(exc)
        st.caption(
            "A rollback republishes the historical content as a **new** version, so history stays linear "
            "and auditable."
        )

with tabs[5]:
    try:
        advice = client.advice(selected_id).get("advice", [])
    except ApiError as exc:
        handle_api_error(exc)
        advice = []
    if advice:
        from reconx.ui.components import advice_card

        for item in advice[:10]:
            advice_card(item)
    else:
        empty_state("No advisor findings yet", "Run the reconciliation first.", icon="💬")

with tabs[6]:
    st.json(definition)
