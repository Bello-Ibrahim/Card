"""Recon Advisor - a chatbot that explains reconciliation results.

The advisor reads the run's metrics, field-level comparison results, exception
samples and column profiles, and answers questions about them: why records did
not match, which columns to match on, which comparison rule fits the observed
differences, and how to combine several matching logics.

Answers are generated from that evidence, so they cite real numbers.
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    advice_card,
    empty_state,
    get_client,
    handle_api_error,
    number,
    page_header,
    percentage,
)

SUGGESTED_QUESTIONS = [
    "Summarise this run",
    "Why did records not match?",
    "Which columns should I match on?",
    "What tolerance should I set?",
    "Should I combine my rules with AND or OR?",
    "What do the duplicates mean?",
    "What are the top exceptions?",
    "How can I make this run faster?",
]

page_header("Recon Advisor", "Ask about a run and get evidence-backed recommendations", "💬")
client = get_client()

# --------------------------------------------------------------------------- #
# Scope selection
# --------------------------------------------------------------------------- #
scope = st.columns([1.5, 1.8, 1, 0.9])
try:
    reconciliations = client.list_reconciliations(limit=500).get("items", [])
except ApiError as exc:
    handle_api_error(exc)
    reconciliations = []

recon_options = ["<none>", *[item["reconId"] for item in reconciliations]]
recon_id = scope[0].selectbox("Reconciliation", recon_options, key="advisor_recon")

runs: list[dict[str, Any]] = []
run_id: str | None = None
if recon_id != "<none>":
    try:
        runs = client.list_runs(recon_id=recon_id, limit=30)
    except ApiError:
        runs = []
    run_labels = ["Latest run", *[
        f"{row['runId'][:8]} · {row.get('businessDate') or ''} · {row.get('status')}" for row in runs
    ]]
    choice = scope[1].selectbox("Run", run_labels, key="advisor_run")
    if choice != "Latest run":
        prefix = choice.split(" · ")[0]
        run_id = next((row["runId"] for row in runs if row["runId"].startswith(prefix)), None)

allow_llm = scope[2].toggle(
    "Narrative mode",
    value=False,
    help=(
        "When the platform is configured with an LLM (ADVISOR_LLM_ENABLED + ANTHROPIC_API_KEY), the same "
        "evidence is used to phrase a richer narrative answer. Off by default: the built-in answers are "
        "deterministic and work without any external call."
    ),
)
if scope[3].button("Clear chat", use_container_width=True):
    st.session_state.advisor_history = []
    st.rerun()

if recon_id == "<none>":
    empty_state(
        "Select a reconciliation to begin",
        "The advisor analyses a completed run: its metrics, field comparisons, exception samples "
        "and column profiles.",
        icon="💬",
    )
    st.stop()

# --------------------------------------------------------------------------- #
# Findings panel
# --------------------------------------------------------------------------- #
left, right = st.columns([1.55, 1])

with right:
    st.markdown("#### Findings")
    try:
        analysis = client.analyse(recon_id=recon_id, run_id=run_id)
    except ApiError as exc:
        handle_api_error(exc)
        analysis = {"advice": [], "counts": {}}

    counts = analysis.get("counts", {})
    metric_columns = st.columns(4)
    metric_columns[0].metric("Critical", number(counts.get("CRITICAL", 0)))
    metric_columns[1].metric("Warnings", number(counts.get("WARNING", 0)))
    metric_columns[2].metric("Suggestions", number(counts.get("SUGGESTION", 0)))
    metric_columns[3].metric("Info", number(counts.get("INFO", 0)))

    advice_items = analysis.get("advice", [])
    if advice_items:
        for item in advice_items[:12]:
            advice_card(item)
    else:
        empty_state(
            "No findings yet",
            "Run the reconciliation (ideally with source profiling enabled) and come back.",
            icon="🔍",
        )

    with st.expander("Column profiles"):
        try:
            profiles = client.profiles(recon_id=recon_id, run_id=run_id)
        except ApiError:
            profiles = []
        if not profiles:
            st.caption(
                "No profiles stored. Start a run with **Profile sources** enabled to collect column "
                "statistics (uniqueness, nulls, case/whitespace anomalies, cross-source value overlap)."
            )
        for profile in profiles:
            st.markdown(f"**Leg `{profile.get('legId')}`**")
            candidates = profile.get("keyCandidates", [])[:8]
            if candidates:
                st.dataframe(
                    [
                        {
                            "Column": c["leftColumn"],
                            "Score": round(c["score"], 3),
                            "Uniqueness": percentage((c["leftUniqueness"] or 0) * 100),
                            "Nulls": percentage((c["leftNullRatio"] or 0) * 100),
                            "Overlap": percentage((c["overlapRatio"] or 0) * 100)
                            if c.get("overlapRatio") is not None
                            else "—",
                            "Normalisation": c.get("normalizationHint") or "—",
                        }
                        for c in candidates
                    ],
                    use_container_width=True,
                    hide_index=True,
                )
            comparison_candidates = profile.get("comparisonCandidates", [])[:10]
            if comparison_candidates:
                st.caption("Suggested comparison rules")
                st.dataframe(
                    [
                        {
                            "Column": c["leftColumn"],
                            "Rule": c["suggestedRule"],
                            "Tolerance": c.get("tolerance"),
                            "Why": c["reason"][:90],
                        }
                        for c in comparison_candidates
                    ],
                    use_container_width=True,
                    hide_index=True,
                )

# --------------------------------------------------------------------------- #
# Chat
# --------------------------------------------------------------------------- #
with left:
    st.markdown("#### Ask the advisor")
    if "advisor_history" not in st.session_state:
        st.session_state.advisor_history = []

    chips = st.columns(4)
    for index, question in enumerate(SUGGESTED_QUESTIONS[:8]):
        if chips[index % 4].button(question, key=f"chip_{index}", use_container_width=True):
            st.session_state.advisor_pending = question

    container = st.container(height=430)
    for message in st.session_state.advisor_history:
        with container.chat_message(message["role"]):
            st.markdown(message["content"])
            if message.get("suggestedConfig"):
                with st.expander("Suggested configuration (copy into the designer)"):
                    st.json(message["suggestedConfig"])

    question = st.chat_input("Ask about this run - e.g. why did 40% of records not match?")
    pending = st.session_state.pop("advisor_pending", None)
    question = question or pending

    if question:
        st.session_state.advisor_history.append({"role": "user", "content": question})
        with container.chat_message("user"):
            st.markdown(question)
        with container.chat_message("assistant"):
            with st.spinner("Analysing the run..."):
                try:
                    reply = client.ask_advisor(
                        question,
                        recon_id=recon_id,
                        run_id=run_id,
                        history=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.advisor_history[-6:]
                        ],
                        allow_llm=allow_llm,
                    )
                except ApiError as exc:
                    handle_api_error(exc)
                    st.stop()
            st.markdown(reply["text"])
            if reply.get("suggestedConfig"):
                with st.expander("Suggested configuration (copy into the designer)"):
                    st.json(reply["suggestedConfig"])
            context = reply.get("context", {})
            st.caption(
                f"Intent: `{reply.get('intent')}` · source: `{reply.get('source')}` · "
                f"evidence: {context.get('legCount', 0)} leg(s), "
                f"{context.get('exceptionSample', 0)} sampled exception(s)"
                + (", column profiles available" if context.get("hasProfiles") else "")
            )
        st.session_state.advisor_history.append(
            {
                "role": "assistant",
                "content": reply["text"],
                "suggestedConfig": reply.get("suggestedConfig"),
            }
        )
        st.rerun()

    st.caption(
        "The advisor answers from the platform's own data — run metrics, per-field comparison results, "
        "exception samples and column profiles. It never invents numbers; when the evidence is missing it "
        "says what to run to collect it."
    )
