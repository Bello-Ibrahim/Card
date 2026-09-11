"""Exceptions: the reconciliation officer's work queue.

Review breaks with their business context columns, add comments, and close them
out with a mandatory reason.  Every state change is recorded in an immutable
comment trail and the audit log.
"""

from __future__ import annotations

import contextlib
from typing import Any

import pandas as pd
import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    coloured_status,
    empty_state,
    get_client,
    handle_api_error,
    has_permission,
    number,
    page_header,
    timestamp,
)

EXCEPTION_TYPES = [
    "MISMATCH",
    "LEFT_ONLY",
    "RIGHT_ONLY",
    "DUPLICATE_LEFT",
    "DUPLICATE_RIGHT",
    "DUPLICATE_BOTH",
    "MISSING",
]
OPEN_STATUSES = ["OPEN", "INVESTIGATING", "REOPENED"]
CLOSED_STATUSES = ["RESOLVED", "CLOSED", "WONT_FIX", "FALSE_POSITIVE"]
ALL_STATUSES = [*OPEN_STATUSES, *CLOSED_STATUSES]

page_header("Exceptions", "Review, comment on and close out reconciliation breaks", "🚨")
client = get_client()

# --------------------------------------------------------------------------- #
# Filters
# --------------------------------------------------------------------------- #
filters = st.columns([1.4, 1.4, 1.2, 1.2, 1, 0.8])
try:
    reconciliations = client.list_reconciliations(limit=500).get("items", [])
except ApiError as exc:
    handle_api_error(exc)
    reconciliations = []

recon_options = ["All", *[item["reconId"] for item in reconciliations]]
recon_id = filters[0].selectbox("Reconciliation", recon_options, key="exc_recon")

run_options = ["All"]
if recon_id != "All":
    with contextlib.suppress(ApiError):
        run_options += [
            f"{row['runId'][:8]} · {row.get('businessDate') or ''} · {row.get('status')}"
            for row in client.list_runs(recon_id=recon_id, limit=40)
        ]
run_choice = filters[1].selectbox("Run", run_options, key="exc_run")
run_id: str | None = None
if run_choice != "All":
    prefix = run_choice.split(" · ")[0]
    try:
        run_id = next(
            row["runId"] for row in client.list_runs(recon_id=recon_id, limit=40) if row["runId"].startswith(prefix)
        )
    except (ApiError, StopIteration):
        run_id = None

exception_type = filters[2].selectbox("Type", ["All", *EXCEPTION_TYPES], key="exc_type")
status_filter = filters[3].selectbox(
    "Status", ["Open only", "All", *ALL_STATUSES], key="exc_status"
)
business_date = filters[4].text_input("Business date", "", key="exc_date", placeholder="YYYY-MM-DD")
limit = filters[5].selectbox("Rows", [100, 250, 500, 1000], index=1, key="exc_limit")

search = st.text_input(
    "Search by reconciliation key", "", key="exc_search", placeholder="e.g. UK|4|T1004"
)

status_parameter: str | None
if status_filter == "Open only":
    status_parameter = "OPEN_ONLY"
elif status_filter == "All":
    status_parameter = None
else:
    status_parameter = status_filter

try:
    payload = client.list_exceptions(
        recon_id=None if recon_id == "All" else recon_id,
        run_id=run_id,
        exception_type=None if exception_type == "All" else exception_type,
        business_date=business_date or None,
        status=status_parameter,
        search=search or None,
        limit=limit,
    )
except ApiError as exc:
    handle_api_error(exc)
    st.stop()

items: list[dict[str, Any]] = payload.get("items", [])
context_columns: list[str] = payload.get("contextColumns", [])
status_summary: dict[str, int] = payload.get("statusSummary", {})
resolution_codes: list[str] = payload.get("resolutionCodes", [])

summary_columns = st.columns(len(status_summary) + 1 if status_summary else 1)
summary_columns[0].metric("Shown", number(len(items)))
for index, (status, count) in enumerate(sorted(status_summary.items()), start=1):
    if index < len(summary_columns):
        summary_columns[index].metric(status.replace("_", " ").title(), number(count))

if not items:
    empty_state(
        "No exceptions match these filters",
        "Either everything reconciled, or the filters are too narrow.",
        icon="✅",
    )
    st.stop()

# --------------------------------------------------------------------------- #
# Table
# --------------------------------------------------------------------------- #
rows: list[dict[str, Any]] = []
for item in items:
    context = item.get("context_columns") if isinstance(item.get("context_columns"), dict) else {}
    row = {
        "Select": False,
        "ID": item.get("id"),
        "Status": item.get("status"),
        "Type": item.get("exception_type"),
        "Key": item.get("reconciliation_key"),
        "Leg": item.get("leg_id"),
        "Field": item.get("field"),
        "Expected": item.get("expected_value"),
        "Actual": item.get("actual_value"),
        "Rule": item.get("rule"),
        "Business date": item.get("business_date"),
    }
    for column in context_columns:
        row[column] = context.get(column)
    row["Comments"] = item.get("comment_count") or 0
    row["Resolved by"] = item.get("resolved_by")
    rows.append(row)

frame = pd.DataFrame(rows)
edited = st.data_editor(
    frame,
    use_container_width=True,
    hide_index=True,
    height=430,
    disabled=[c for c in frame.columns if c != "Select"],
    column_config={
        "Select": st.column_config.CheckboxColumn("", width="small"),
        "ID": st.column_config.NumberColumn("ID", width="small", format="%d"),
        "Key": st.column_config.TextColumn("Reconciliation key", width="medium"),
    },
    key="exception_editor",
)
selected_ids = [int(row["ID"]) for _, row in edited.iterrows() if row["Select"]]

if context_columns:
    st.caption(
        "Context columns shown from the source data: "
        + ", ".join(f"`{c}`" for c in context_columns)
        + " — configure these per leg in the designer (**Exception columns**)."
    )

# --------------------------------------------------------------------------- #
# Actions
# --------------------------------------------------------------------------- #
action_tabs = st.tabs(["✍️ Close out selected", "📚 Bulk close by filter", "🔎 Detail & history", "⬇️ Export"])

with action_tabs[0]:
    if not has_permission("exception:view"):
        st.info("You do not have permission to update exceptions.")
    elif not selected_ids:
        st.info("Tick the **Select** box on one or more rows above to close them out.")
    else:
        st.markdown(f"**{len(selected_ids)} exception(s) selected:** {selected_ids[:20]}")
        with st.form("close_out_form"):
            columns = st.columns([1.1, 1.3, 1.3])
            new_status = columns[0].selectbox("New status", CLOSED_STATUSES + OPEN_STATUSES, index=1)
            resolution_code = columns[1].selectbox("Resolution code", ["<none>", *resolution_codes])
            assigned_to = columns[2].text_input("Assign to (optional)", "")
            comment = st.text_area(
                "Officer comment *",
                height=110,
                placeholder=(
                    "Why is this being closed? e.g. 'Confirmed with the settlements team: the fee posts "
                    "one day later in the ledger. Accepted as a timing difference (ticket OPS-4412).'"
                ),
            )
            submitted = st.form_submit_button("Apply", type="primary")
        if submitted:
            if len(comment.strip()) < 3:
                st.error("A comment is required — it is what makes the close-out auditable.")
            else:
                try:
                    result = client.update_exception_status(
                        selected_ids,
                        status=new_status,
                        comment=comment.strip(),
                        resolution_code=None if resolution_code == "<none>" else resolution_code,
                        assigned_to=assigned_to or None,
                    )
                    st.success(
                        f"{result['updated']} exception(s) set to **{result['status']}**"
                        + (f" · {result['reopened']} reopened" if result.get("reopened") else "")
                    )
                    st.rerun()
                except ApiError as exc:
                    handle_api_error(exc)

with action_tabs[1]:
    st.caption(
        "Close every **open** exception matching a filter — useful for a known, feed-wide cause such as a "
        "timing cut-off. The same comment is recorded against each one."
    )
    with st.form("bulk_close_form"):
        columns = st.columns(3)
        bulk_recon = columns[0].selectbox("Reconciliation", recon_options, key="bulk_recon")
        bulk_type = columns[1].selectbox("Exception type", ["All", *EXCEPTION_TYPES], key="bulk_type")
        bulk_status = columns[2].selectbox("Close as", CLOSED_STATUSES, key="bulk_status")
        columns = st.columns(3)
        bulk_date = columns[0].text_input("Business date", business_date or "", key="bulk_date")
        bulk_leg = columns[1].text_input("Leg ID (optional)", "", key="bulk_leg")
        bulk_code = columns[2].selectbox("Resolution code", ["<none>", *resolution_codes], key="bulk_code")
        bulk_comment = st.text_area("Officer comment *", height=90, key="bulk_comment")
        bulk_limit = st.number_input("Maximum to close", min_value=1, max_value=100_000, value=1000)
        bulk_submitted = st.form_submit_button("Close matching exceptions", type="primary")
    if bulk_submitted:
        if len(bulk_comment.strip()) < 3:
            st.error("A comment is required.")
        elif bulk_recon == "All" and not run_id:
            st.error("Select a reconciliation (or a run) — a bulk close needs a scope.")
        else:
            try:
                result = client.bulk_close_exceptions(
                    comment=bulk_comment.strip(),
                    status=bulk_status,
                    resolutionCode=None if bulk_code == "<none>" else bulk_code,
                    reconId=None if bulk_recon == "All" else bulk_recon,
                    runId=run_id,
                    legId=bulk_leg or None,
                    exceptionType=None if bulk_type == "All" else bulk_type,
                    businessDate=bulk_date or None,
                    limit=int(bulk_limit),
                )
                st.success(f"{result['updated']} exception(s) closed as {result.get('status')}")
                st.rerun()
            except ApiError as exc:
                handle_api_error(exc)

with action_tabs[2]:
    detail_id = st.selectbox(
        "Exception",
        [item["id"] for item in items],
        format_func=lambda i: f"#{i} · "
        + next(
            (
                f"{x.get('exception_type')} {x.get('reconciliation_key')}"
                for x in items
                if x["id"] == i
            ),
            "",
        ),
        key="exc_detail_select",
    )
    if detail_id:
        try:
            detail = client.get_exception(int(detail_id))
        except ApiError as exc:
            handle_api_error(exc)
            detail = {}
        record = detail.get("exception", {})
        if record:
            columns = st.columns([1.4, 1])
            with columns[0]:
                st.markdown(f"**Key:** `{record.get('reconciliation_key')}`")
                st.markdown(
                    f"**Type:** {record.get('exception_type')} &nbsp;·&nbsp; "
                    f"**Status:** {coloured_status(record.get('status'))}",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f"**Leg:** `{record.get('leg_id')}` &nbsp;·&nbsp; "
                    f"**Source:** {record.get('source') or '—'} &nbsp;·&nbsp; "
                    f"**Business date:** {record.get('business_date') or '—'}"
                )
                if record.get("field"):
                    st.markdown(
                        f"**Field:** `{record.get('field')}` · rule *{record.get('rule') or '—'}*  \n"
                        f"**Expected:** `{record.get('expected_value')}`  \n"
                        f"**Actual:** `{record.get('actual_value')}`"
                    )
                if isinstance(record.get("context_columns"), dict) and record["context_columns"]:
                    st.markdown("**Business context**")
                    st.json(record["context_columns"])
                if isinstance(record.get("key_components"), dict):
                    st.markdown("**Key components**")
                    st.json(record["key_components"])
            with columns[1]:
                st.markdown("**Workflow**")
                st.markdown(
                    f"- Occurrences: {record.get('left_occurrences')} left / "
                    f"{record.get('right_occurrences')} right\n"
                    f"- Resolution code: `{record.get('resolution_code') or '—'}`\n"
                    f"- Resolved by: {record.get('resolved_by') or '—'}\n"
                    f"- Resolved at: {timestamp(record.get('resolved_at'))}\n"
                    f"- Reopened: {record.get('reopened_count') or 0} time(s)\n"
                    f"- Created: {timestamp(record.get('created_at'))}"
                )
                if record.get("resolution_note"):
                    st.info(record["resolution_note"])

            st.markdown("##### Comment trail")
            comments = detail.get("comments", [])
            if comments:
                for entry in comments:
                    with st.container(border=True):
                        transition = (
                            f" · {entry.get('status_before')} → {entry.get('status_after')}"
                            if entry.get("status_before") != entry.get("status_after")
                            else ""
                        )
                        st.markdown(
                            f"**{entry.get('author')}** · {timestamp(entry.get('created_at'))}{transition}"
                        )
                        st.write(entry.get("comment"))
            else:
                st.caption("No comments yet.")

            with st.form(f"comment_form_{detail_id}"):
                new_comment = st.text_area("Add a comment", height=90)
                if st.form_submit_button("Add comment") and new_comment.strip():
                    try:
                        client.add_exception_comment(int(detail_id), new_comment.strip())
                        st.success("Comment added")
                        st.rerun()
                    except ApiError as exc:
                        handle_api_error(exc)

with action_tabs[3]:
    st.caption("The CSV export includes the configured business context columns as real columns.")
    url = client.export_exceptions_url(
        run_id=run_id,
        recon_id=None if recon_id == "All" else recon_id,
        exception_type=None if exception_type == "All" else exception_type,
        status=status_parameter,
    )
    st.markdown(f"[⬇️ Download CSV]({url})")
    st.code(url, language="text")
    st.caption(
        "The link requires an authenticated session; if your browser is not signed in to the API, use "
        "`curl -H 'Authorization: Bearer <token>' '<url>' -o exceptions.csv`."
    )
