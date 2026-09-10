"""Reconciliation Designer.

Builds a complete reconciliation definition step by step: sources (including
hand-written SQL in any dialect with ``${variable}`` substitution), keys and
normalisation, one or more matching logics combined with AND/OR, the columns
carried onto exception records, outputs, data-availability conditions, the
schedule and notifications.
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    empty_state,
    get_client,
    handle_api_error,
    has_permission,
    leg_flow_diagram,
    page_header,
)

COMPARISON_RULES = [
    "exact",
    "case_insensitive",
    "trimmed",
    "numeric_exact",
    "numeric_tolerance",
    "percentage_tolerance",
    "date_tolerance",
    "date_only",
    "expression",
    "contains",
    "always_match",
]
SOURCE_TYPES = ["jdbc", "s3", "storagegrid", "sftp", "filesystem", "excel", "kafka", "leg_output", "temp_view"]
FILE_FORMATS = ["csv", "json", "parquet", "excel", "orc", "avro"]
SQL_DIALECTS = ["generic", "mssql", "postgresql", "mysql", "oracle", "db2", "sqlite"]
OUTPUT_TYPES = ["none", "jdbc", "s3", "storagegrid", "filesystem", "kafka", "temp_view", "sftp"]
CONDITION_TYPES = [
    "file_exists",
    "s3_file_exists",
    "sftp_file_exists",
    "file_count",
    "file_size",
    "jdbc_query",
    "custom_sql",
    "kafka_available",
    "previous_run_successful",
    "reconciliation_succeeded",
]
MATCH_CATEGORIES = [
    "MATCHED",
    "MISMATCH",
    "LEFT_ONLY",
    "RIGHT_ONLY",
    "DUPLICATE_LEFT",
    "DUPLICATE_RIGHT",
    "DUPLICATE_BOTH",
]

def _to_yaml(payload: dict[str, Any]) -> str:
    """Serialise the working definition as YAML for export/version control."""
    import yaml

    return yaml.safe_dump({"reconciliation": payload}, sort_keys=False, allow_unicode=True, width=100)


page_header("Reconciliation Designer", "Configure a reconciliation end to end", "🛠️")
client = get_client()


# --------------------------------------------------------------------------- #
# Working definition
# --------------------------------------------------------------------------- #
def blank_definition() -> dict[str, Any]:
    return {
        "reconId": "",
        "name": "",
        "description": "",
        "product": "",
        "customer": "",
        "environment": "",
        "tags": [],
        "variables": [],
        "parameters": {},
        "legs": [],
        "schedule": {"type": "manual", "timezone": "UTC", "enabled": True, "timeoutMinutes": 180},
        "notifications": {"email": {"enabled": False, "recipients": [], "on": ["SUCCESS", "FAILURE"]}},
        "events": {"enabled": True, "onFailure": "WARN_ONLY"},
        "retention": {"runsDays": 365, "exceptionsDays": 90},
        "idempotencyDimensions": ["business_date"],
    }


def blank_leg(index: int) -> dict[str, Any]:
    return {
        "id": f"leg_{index + 1}",
        "name": f"Leg {index + 1}",
        "enabled": True,
        "sources": [],
        "keys": [],
        "matchLogic": {"operator": "AND", "rules": []},
        "exceptionColumns": [],
        "outputs": [],
        "matching": {"duplicateDetection": True, "nullEqualsNull": True, "trimKeys": True},
    }


if "designer_definition" not in st.session_state:
    st.session_state.designer_definition = blank_definition()

definition: dict[str, Any] = st.session_state.designer_definition


def connections_by_type() -> dict[str, list[str]]:
    try:
        items = client.list_connections(enabled=True)
    except ApiError:
        return {}
    grouped: dict[str, list[str]] = {}
    for item in items:
        grouped.setdefault(item["type"], []).append(item["connectionId"])
    return grouped


connection_map = connections_by_type()
all_connections = sorted({c for values in connection_map.values() for c in values})


def variable_values() -> dict[str, Any]:
    """Current variable values used for preview substitution."""
    values = {
        variable["name"]: variable.get("default", "")
        for variable in definition.get("variables", [])
        if variable.get("name")
    }
    values.update(definition.get("parameters") or {})
    return values


# --------------------------------------------------------------------------- #
# Load / new
# --------------------------------------------------------------------------- #
toolbar = st.columns([2.2, 1, 1, 1])
try:
    existing = client.list_reconciliations(limit=500).get("items", [])
except ApiError as exc:
    handle_api_error(exc)
    existing = []

options = ["<new reconciliation>"] + [f"{item['reconId']} — {item.get('name', '')}" for item in existing]
selected = toolbar[0].selectbox("Load an existing reconciliation", options, key="designer_load_select")

if toolbar[1].button("Load", use_container_width=True, disabled=selected == options[0]):
    recon_id = selected.split(" — ")[0]
    try:
        loaded = client.get_reconciliation(recon_id)["definition"]
        st.session_state.designer_definition = loaded
        st.session_state.designer_loaded_version = loaded.get("version")
        st.success(f"Loaded '{recon_id}' version {loaded.get('version')}")
        st.rerun()
    except ApiError as exc:
        handle_api_error(exc)

if toolbar[2].button("New", use_container_width=True):
    st.session_state.designer_definition = blank_definition()
    st.session_state.pop("designer_loaded_version", None)
    st.rerun()

if toolbar[3].button("Add leg", use_container_width=True, type="primary"):
    definition.setdefault("legs", []).append(blank_leg(len(definition.get("legs", []))))
    st.rerun()

tabs = st.tabs(
    [
        "1 · General",
        "2 · Variables",
        "3 · Legs, sources & matching",
        "4 · Conditions",
        "5 · Schedule & notifications",
        "6 · Review, validate & save",
    ]
)

# --------------------------------------------------------------------------- #
# 1. General
# --------------------------------------------------------------------------- #
with tabs[0]:
    columns = st.columns(2)
    definition["reconId"] = columns[0].text_input(
        "Reconciliation ID *",
        definition.get("reconId", ""),
        help="Stable identifier, e.g. payments_daily_recon. Letters, digits, '_', '-' and '.'",
    )
    definition["name"] = columns[1].text_input("Name *", definition.get("name", ""))
    definition["description"] = st.text_area("Description", definition.get("description", ""), height=80)

    columns = st.columns(3)
    definition["product"] = columns[0].text_input("Product", definition.get("product") or "")
    definition["customer"] = columns[1].text_input("Customer", definition.get("customer") or "")
    definition["environment"] = columns[2].text_input("Environment", definition.get("environment") or "")

    tags = st.text_input(
        "Tags (comma separated)", ", ".join(definition.get("tags", [])), key="designer_tags"
    )
    definition["tags"] = [t.strip() for t in tags.split(",") if t.strip()]

    st.markdown("##### Idempotency")
    st.caption(
        "A run is uniquely identified by `reconId + version + these dimensions`. "
        "Two scheduler nodes computing the same key can never start the same logical run twice."
    )
    dimensions = st.text_input(
        "Idempotency dimensions",
        ", ".join(definition.get("idempotencyDimensions", ["business_date"])),
        key="designer_idem",
    )
    definition["idempotencyDimensions"] = [d.strip() for d in dimensions.split(",") if d.strip()]

# --------------------------------------------------------------------------- #
# 2. Variables
# --------------------------------------------------------------------------- #
with tabs[1]:
    st.markdown("##### Variables")
    st.caption(
        "Declare `${variables}` you can use anywhere in the configuration - SQL queries, **table names**, "
        "file paths, filters and connection fields. They are substituted at run time."
    )
    with st.expander("Built-in variables (always available)", expanded=False):
        st.markdown(
            "| Variable | Example |\n|---|---|\n"
            "| `${business_date}` | 2026-09-10 |\n"
            "| `${business_date_compact}` | 20260910 |\n"
            "| `${business_date_yyyy}` / `${business_date_mm}` / `${business_date_dd}` | 2026 / 09 / 10 |\n"
            "| `${prev_business_date}` | 2026-09-09 |\n"
            "| `${next_business_date}` | 2026-09-11 |\n"
            "| `${run_timestamp}` | 20260910T020000Z |\n"
            "| `${recon_id}` / `${run_id}` | payments_daily_recon / uuid |\n\n"
            "Use `${name:default}` to supply an inline fallback."
        )

    variables: list[dict[str, Any]] = definition.setdefault("variables", [])
    for index, variable in enumerate(list(variables)):
        with st.container(border=True):
            columns = st.columns([1.2, 1.2, 1, 1.4, 0.5])
            variable["name"] = columns[0].text_input("Name", variable.get("name", ""), key=f"var_name_{index}")
            variable["label"] = columns[1].text_input(
                "Label", variable.get("label") or "", key=f"var_label_{index}"
            )
            variable["type"] = columns[2].selectbox(
                "Type",
                ["string", "number", "date", "boolean", "choice"],
                index=["string", "number", "date", "boolean", "choice"].index(
                    variable.get("type", "string")
                ),
                key=f"var_type_{index}",
            )
            variable["default"] = columns[3].text_input(
                "Default value", variable.get("default") or "", key=f"var_default_{index}"
            )
            if columns[4].button("🗑", key=f"var_del_{index}", help="Remove variable"):
                variables.pop(index)
                st.rerun()
            if variable["type"] == "choice":
                choices = st.text_input(
                    "Choices (comma separated)",
                    ", ".join(variable.get("choices", [])),
                    key=f"var_choices_{index}",
                )
                variable["choices"] = [c.strip() for c in choices.split(",") if c.strip()]
            variable["promptAtRun"] = st.checkbox(
                "Prompt the operator when starting a manual run",
                value=bool(variable.get("promptAtRun")),
                key=f"var_prompt_{index}",
            )

    if st.button("➕ Add variable"):
        variables.append({"name": "", "type": "string", "default": "", "required": True})
        st.rerun()

    if variables:
        st.markdown("##### Preview values")
        st.caption("These values are used when you preview a query on the Sources tab.")
        st.json(variable_values())

# --------------------------------------------------------------------------- #
# 3. Legs, sources and matching
# --------------------------------------------------------------------------- #
with tabs[2]:
    legs: list[dict[str, Any]] = definition.setdefault("legs", [])
    if not legs:
        empty_state("No legs yet", "Use 'Add leg' above to start.", icon="🧩")
    else:
        st.code(leg_flow_diagram(legs), language="text")

    for leg_index, leg in enumerate(list(legs)):
        with st.expander(
            f"Leg {leg_index + 1}: {leg.get('name') or leg.get('id')}", expanded=leg_index == 0
        ):
            head = st.columns([1.2, 1.6, 1, 0.6])
            leg["id"] = head[0].text_input("Leg ID", leg.get("id", ""), key=f"leg_id_{leg_index}")
            leg["name"] = head[1].text_input("Leg name", leg.get("name") or "", key=f"leg_name_{leg_index}")
            leg["enabled"] = head[2].checkbox(
                "Enabled", value=leg.get("enabled", True), key=f"leg_enabled_{leg_index}"
            )
            if head[3].button("🗑", key=f"leg_del_{leg_index}", help="Remove leg"):
                legs.pop(leg_index)
                st.rerun()

            leg_tabs = st.tabs(
                ["Sources", "Keys", "Matching logic", "Exception columns", "Outputs", "Advanced"]
            )

            # ---------------------------------------------------------- sources
            with leg_tabs[0]:
                sources: list[dict[str, Any]] = leg.setdefault("sources", [])
                for source_index, source in enumerate(list(sources)):
                    with st.container(border=True):
                        row = st.columns([1.1, 1.1, 1.6, 0.4])
                        source["id"] = row[0].text_input(
                            "Source ID", source.get("id", ""), key=f"src_id_{leg_index}_{source_index}"
                        )
                        source["type"] = row[1].selectbox(
                            "Type",
                            SOURCE_TYPES,
                            index=SOURCE_TYPES.index(source.get("type", "jdbc"))
                            if source.get("type") in SOURCE_TYPES
                            else 0,
                            key=f"src_type_{leg_index}_{source_index}",
                        )
                        source_type = source["type"]
                        eligible = connection_map.get(source_type, []) or all_connections
                        if source_type in ("jdbc", "s3", "storagegrid", "sftp", "kafka", "filesystem", "excel"):
                            current = source.get("connectionRef")
                            choices = ["<none>", *eligible]
                            source["connectionRef"] = row[2].selectbox(
                                "Connection",
                                choices,
                                index=choices.index(current) if current in choices else 0,
                                key=f"src_conn_{leg_index}_{source_index}",
                            )
                            if source["connectionRef"] == "<none>":
                                source["connectionRef"] = None
                        if row[3].button("🗑", key=f"src_del_{leg_index}_{source_index}"):
                            sources.pop(source_index)
                            st.rerun()

                        # ---- location, per type
                        if source_type == "jdbc":
                            mode = st.radio(
                                "Read from",
                                ["Table", "SQL query"],
                                horizontal=True,
                                index=1 if source.get("query") else 0,
                                key=f"src_mode_{leg_index}_{source_index}",
                            )
                            dialect_index = SQL_DIALECTS.index(source.get("dialect", "generic"))
                            source["dialect"] = st.selectbox(
                                "SQL dialect",
                                SQL_DIALECTS,
                                index=dialect_index,
                                key=f"src_dialect_{leg_index}_{source_index}",
                                help=(
                                    "Declarative: the statement is sent to the database verbatim. "
                                    "T-SQL (SELECT TOP (n) ... WITH (NOLOCK)), Oracle FETCH FIRST and "
                                    "PostgreSQL LIMIT all work."
                                ),
                            )
                            if mode == "Table":
                                source["table"] = st.text_input(
                                    "Table",
                                    source.get("table") or "",
                                    key=f"src_table_{leg_index}_{source_index}",
                                    help=(
                                        "Qualified names are supported, including SQL Server brackets: "
                                        "[dbo].[Transactions]. ${variables} are substituted."
                                    ),
                                )
                                source.pop("query", None)
                            else:
                                source["query"] = st.text_area(
                                    "SQL query",
                                    source.get("query") or "",
                                    height=190,
                                    key=f"src_query_{leg_index}_{source_index}",
                                    help=(
                                        "Read-only SELECT/WITH only. Use ${variables} anywhere, including "
                                        "in table names."
                                    ),
                                )
                                source.pop("table", None)
                                if source.get("dialect") == "mssql":
                                    st.caption(
                                        "T-SQL example: "
                                        "`SELECT TOP (1000) t.[TransactionId], t.[Amount] "
                                        "FROM ${ledger_table} AS t WITH (NOLOCK) "
                                        "WHERE t.[BusinessDate] = '${business_date}'`"
                                    )

                            preview_columns = st.columns([1, 1, 3])
                            if preview_columns[0].button(
                                "🔍 Preview", key=f"src_preview_{leg_index}_{source_index}"
                            ):
                                if not source.get("connectionRef"):
                                    st.warning("Select a connection first.")
                                else:
                                    try:
                                        preview = client.preview_query(
                                            source["connectionRef"],
                                            query=source.get("query"),
                                            table=source.get("table"),
                                            limit=100,
                                            variables=variable_values(),
                                            dialect=source.get("dialect", "generic"),
                                        )
                                        st.session_state[f"preview_{leg_index}_{source_index}"] = preview
                                    except ApiError as exc:
                                        handle_api_error(exc)
                            list_tables_clicked = preview_columns[1].button(
                                "📋 Tables", key=f"src_tables_{leg_index}_{source_index}"
                            )
                            if list_tables_clicked and source.get("connectionRef"):
                                try:
                                    tables = client.list_tables(source["connectionRef"])
                                    st.session_state[f"tables_{leg_index}_{source_index}"] = tables
                                except ApiError as exc:
                                    handle_api_error(exc)

                            tables = st.session_state.get(f"tables_{leg_index}_{source_index}")
                            if tables:
                                st.caption(f"{len(tables)} table(s)/view(s) visible to this connection")
                                st.dataframe(tables, use_container_width=True, hide_index=True, height=180)

                            preview = st.session_state.get(f"preview_{leg_index}_{source_index}")
                            if preview:
                                st.caption(
                                    f"Executed in {preview['elapsedMs']} ms · {preview['rowCount']} row(s)"
                                    + (" (truncated)" if preview.get("truncated") else "")
                                )
                                st.code(preview["statement"], language="sql")
                                st.dataframe(
                                    preview["rows"], use_container_width=True, hide_index=True, height=240
                                )
                                st.caption(f"Columns: {', '.join(preview['columns'])}")

                        elif source_type in ("s3", "storagegrid", "filesystem", "sftp", "excel"):
                            columns = st.columns([2.4, 1, 1])
                            source["path"] = columns[0].text_input(
                                "Path",
                                source.get("path") or "",
                                key=f"src_path_{leg_index}_{source_index}",
                                help="Supports ${variables}, e.g. s3://bucket/in/${business_date}/*.parquet",
                            )
                            fmt = source.get("format") or "csv"
                            source["format"] = columns[1].selectbox(
                                "Format",
                                FILE_FORMATS,
                                index=FILE_FORMATS.index(fmt) if fmt in FILE_FORMATS else 0,
                                key=f"src_fmt_{leg_index}_{source_index}",
                            )
                            source["filePattern"] = columns[2].text_input(
                                "File pattern",
                                source.get("filePattern") or "",
                                key=f"src_pattern_{leg_index}_{source_index}",
                            ) or None
                            list_files_clicked = st.button(
                                "📂 List files", key=f"src_ls_{leg_index}_{source_index}"
                            )
                            if list_files_clicked and source.get("connectionRef"):
                                try:
                                    files = client.list_files(
                                        source["connectionRef"],
                                        source.get("path", ""),
                                        source.get("filePattern"),
                                    )
                                    st.dataframe(files, use_container_width=True, hide_index=True)
                                except ApiError as exc:
                                    handle_api_error(exc)

                        elif source_type == "kafka":
                            columns = st.columns(3)
                            source["topic"] = columns[0].text_input(
                                "Topic", source.get("topic") or "", key=f"src_topic_{leg_index}_{source_index}"
                            )
                            options = source.setdefault("options", {})
                            options["startingOffsets"] = columns[1].text_input(
                                "Starting offsets",
                                options.get("startingOffsets", "earliest"),
                                key=f"src_start_{leg_index}_{source_index}",
                            )
                            options["messageFormat"] = columns[2].selectbox(
                                "Message format",
                                ["json", "csv", "avro", "string"],
                                index=["json", "csv", "avro", "string"].index(
                                    options.get("messageFormat", "json")
                                ),
                                key=f"src_msgfmt_{leg_index}_{source_index}",
                            )

                        elif source_type == "leg_output":
                            other_legs = [x.get("id") for x in legs if x.get("id") != leg.get("id")]
                            current = source.get("legRef")
                            source["legRef"] = st.selectbox(
                                "Producing leg",
                                other_legs or ["<no other leg>"],
                                index=other_legs.index(current) if current in other_legs else 0,
                                key=f"src_legref_{leg_index}_{source_index}",
                            )
                        elif source_type == "temp_view":
                            source["view"] = st.text_input(
                                "View name", source.get("view") or "", key=f"src_view_{leg_index}_{source_index}"
                            )

                        source["filter"] = st.text_input(
                            "Row filter (Spark SQL, optional)",
                            source.get("filter") or "",
                            key=f"src_filter_{leg_index}_{source_index}",
                            help="Applied after reading, e.g. status = 'SETTLED'",
                        ) or None

                if st.button("➕ Add source", key=f"add_src_{leg_index}"):
                    sources.append(
                        {"id": f"source_{len(sources) + 1}", "type": "jdbc", "dialect": "generic"}
                    )
                    st.rerun()

                if len(sources) >= 2:
                    ids = [s.get("id") for s in sources]
                    columns = st.columns(2)
                    leg["leftSource"] = columns[0].selectbox(
                        "Left source",
                        ids,
                        index=ids.index(leg.get("leftSource")) if leg.get("leftSource") in ids else 0,
                        key=f"leg_left_{leg_index}",
                    )
                    right_default = leg.get("rightSource") if leg.get("rightSource") in ids else ids[-1]
                    leg["rightSource"] = columns[1].selectbox(
                        "Right source",
                        ids,
                        index=ids.index(right_default),
                        key=f"leg_right_{leg_index}",
                    )

            # ------------------------------------------------------------- keys
            with leg_tabs[1]:
                st.caption(
                    "The reconciliation key identifies the same business record on both sides. "
                    "Normalisation is applied before matching."
                )
                keys: list[dict[str, Any]] = leg.setdefault("keys", [])
                for key_index, key in enumerate(list(keys)):
                    with st.container(border=True):
                        columns = st.columns([1.2, 1.2, 1, 0.4])
                        key["left"] = columns[0].text_input(
                            "Left column", key.get("left") or "", key=f"key_left_{leg_index}_{key_index}"
                        )
                        key["right"] = columns[1].text_input(
                            "Right column", key.get("right") or "", key=f"key_right_{leg_index}_{key_index}"
                        )
                        key["alias"] = columns[2].text_input(
                            "Alias", key.get("alias") or key.get("left") or "",
                            key=f"key_alias_{leg_index}_{key_index}",
                        )
                        if columns[3].button("🗑", key=f"key_del_{leg_index}_{key_index}"):
                            keys.pop(key_index)
                            st.rerun()
                        normalization = key.setdefault("normalization", {})
                        norm_columns = st.columns(4)
                        normalization["trim"] = norm_columns[0].checkbox(
                            "Trim", value=normalization.get("trim", True), key=f"key_trim_{leg_index}_{key_index}"
                        )
                        case_options = ["none", "upper", "lower"]
                        normalization["case"] = norm_columns[1].selectbox(
                            "Case",
                            case_options,
                            index=case_options.index(normalization.get("case", "none")),
                            key=f"key_case_{leg_index}_{key_index}",
                        )
                        normalization["stripLeadingZeros"] = norm_columns[2].checkbox(
                            "Strip leading zeros",
                            value=normalization.get("stripLeadingZeros", False),
                            key=f"key_zeros_{leg_index}_{key_index}",
                        )
                        normalization["padLeft"] = norm_columns[3].number_input(
                            "Pad left to",
                            min_value=0,
                            max_value=64,
                            value=int(normalization.get("padLeft") or 0),
                            key=f"key_pad_{leg_index}_{key_index}",
                        ) or None

                if st.button("➕ Add key component", key=f"add_key_{leg_index}"):
                    keys.append({"left": "", "right": "", "normalization": {"trim": True}})
                    st.rerun()

                if keys:
                    separator = leg.setdefault("matching", {}).get("keySeparator", "|")
                    preview = f" {separator} ".join(k.get("alias") or k.get("left") or "?" for k in keys)
                    st.info(f"Composite key: **{preview}**")

            # --------------------------------------------------- matching logic
            with leg_tabs[2]:
                st.caption(
                    "Add one or more **matching logics**. Comparisons inside a rule combine with the rule's "
                    "operator; the rules themselves combine with the group operator below."
                )
                match_logic: dict[str, Any] = leg.setdefault("matchLogic", {"operator": "AND", "rules": []})
                columns = st.columns([1, 3])
                match_logic["operator"] = columns[0].radio(
                    "Combine rules with",
                    ["AND", "OR"],
                    horizontal=True,
                    index=0 if match_logic.get("operator", "AND") == "AND" else 1,
                    key=f"ml_op_{leg_index}",
                    help=(
                        "AND: every rule must hold for a MATCH (stricter, more breaks). "
                        "OR: any single rule is enough (use it when there are alternative ways to "
                        "prove the same economic match)."
                    ),
                )
                match_logic["negate"] = columns[1].checkbox(
                    "Negate the whole group (NOT)",
                    value=bool(match_logic.get("negate")),
                    key=f"ml_negate_{leg_index}",
                )

                rules: list[dict[str, Any]] = match_logic.setdefault("rules", [])
                for rule_index, rule in enumerate(list(rules)):
                    with st.container(border=True):
                        head = st.columns([1.1, 1.6, 0.9, 0.8, 0.4])
                        rule["id"] = head[0].text_input(
                            "Rule ID", rule.get("id", f"rule_{rule_index + 1}"),
                            key=f"rule_id_{leg_index}_{rule_index}",
                        )
                        rule["name"] = head[1].text_input(
                            "Rule name", rule.get("name") or "", key=f"rule_name_{leg_index}_{rule_index}"
                        )
                        rule["operator"] = head[2].selectbox(
                            "Comparisons",
                            ["AND", "OR"],
                            index=0 if rule.get("operator", "AND") == "AND" else 1,
                            key=f"rule_op_{leg_index}_{rule_index}",
                        )
                        rule["negate"] = head[3].checkbox(
                            "NOT", value=bool(rule.get("negate")), key=f"rule_not_{leg_index}_{rule_index}"
                        )
                        if head[4].button("🗑", key=f"rule_del_{leg_index}_{rule_index}"):
                            rules.pop(rule_index)
                            st.rerun()

                        comparisons: list[dict[str, Any]] = rule.setdefault("comparisons", [])
                        for c_index, comparison in enumerate(list(comparisons)):
                            columns = st.columns([1.1, 1.1, 1.2, 0.9, 0.4])
                            comparison["left"] = columns[0].text_input(
                                "Left field",
                                comparison.get("left") or "",
                                key=f"cmp_l_{leg_index}_{rule_index}_{c_index}",
                            )
                            comparison["right"] = columns[1].text_input(
                                "Right field",
                                comparison.get("right") or "",
                                key=f"cmp_r_{leg_index}_{rule_index}_{c_index}",
                            )
                            comparison["rule"] = columns[2].selectbox(
                                "Comparison",
                                COMPARISON_RULES,
                                index=COMPARISON_RULES.index(comparison.get("rule", "exact"))
                                if comparison.get("rule") in COMPARISON_RULES
                                else 0,
                                key=f"cmp_rule_{leg_index}_{rule_index}_{c_index}",
                            )
                            if comparison["rule"] in (
                                "numeric_tolerance",
                                "percentage_tolerance",
                                "date_tolerance",
                            ):
                                comparison["tolerance"] = columns[3].number_input(
                                    "Tolerance",
                                    value=float(comparison.get("tolerance") or 0.01),
                                    step=0.01,
                                    format="%.4f",
                                    key=f"cmp_tol_{leg_index}_{rule_index}_{c_index}",
                                )
                                if comparison["rule"] == "date_tolerance":
                                    comparison["toleranceUnit"] = st.selectbox(
                                        "Tolerance unit",
                                        ["seconds", "minutes", "hours", "days"],
                                        index=["seconds", "minutes", "hours", "days"].index(
                                            comparison.get("toleranceUnit", "seconds")
                                        ),
                                        key=f"cmp_unit_{leg_index}_{rule_index}_{c_index}",
                                    )
                            if columns[4].button("🗑", key=f"cmp_del_{leg_index}_{rule_index}_{c_index}"):
                                comparisons.pop(c_index)
                                st.rerun()
                            if comparison["rule"] == "expression":
                                comparison["expression"] = st.text_input(
                                    "Boolean expression",
                                    comparison.get("expression") or "",
                                    key=f"cmp_expr_{leg_index}_{rule_index}_{c_index}",
                                    help="Use left.<column> and right.<column>, e.g. "
                                    "ABS(left.amount - right.amount) <= 0.01",
                                )

                        if st.button("➕ Add comparison", key=f"add_cmp_{leg_index}_{rule_index}"):
                            comparisons.append({"left": "", "right": "", "rule": "exact"})
                            st.rerun()

                        if comparisons:
                            joiner = f" {rule.get('operator', 'AND')} "
                            body = joiner.join(
                                f"{c.get('left')} {c.get('rule')} {c.get('right')}" for c in comparisons
                            )
                            st.caption(("NOT (" + body + ")") if rule.get("negate") else body)

                if st.button("➕ Add matching logic", key=f"add_rule_{leg_index}", type="primary"):
                    rules.append(
                        {
                            "id": f"rule_{len(rules) + 1}",
                            "name": f"Rule {len(rules) + 1}",
                            "operator": "AND",
                            "comparisons": [],
                        }
                    )
                    st.rerun()

                if rules:
                    labels = [
                        ("NOT " if r.get("negate") else "") + (r.get("name") or r.get("id"))
                        for r in rules
                    ]
                    expression = f" {match_logic.get('operator', 'AND')} ".join(labels)
                    if match_logic.get("negate"):
                        expression = f"NOT ({expression})"
                    st.success(f"**Match when:** {expression}")

                with st.expander("💡 Ask the advisor to draft the matching logic"):
                    st.caption(
                        "Uses profiled column statistics from a previous run to draft value/reference rules."
                    )
                    columns = st.columns([1, 1, 2])
                    operator = columns[0].selectbox("Combine with", ["AND", "OR"], key=f"sugg_op_{leg_index}")
                    if columns[1].button("Draft", key=f"sugg_btn_{leg_index}"):
                        try:
                            suggestion = client.suggest_match_logic(
                                recon_id=definition.get("reconId") or None, operator=operator
                            )
                            if suggestion.get("matchLogic"):
                                leg["matchLogic"] = suggestion["matchLogic"]
                                st.success("Matching logic drafted from profiled columns.")
                                st.rerun()
                            else:
                                st.info(suggestion.get("reason", "No suggestion available."))
                        except ApiError as exc:
                            handle_api_error(exc)

            # ------------------------------------------------- exception columns
            with leg_tabs[3]:
                st.caption(
                    "Choose the **source columns carried onto every exception record** for this leg. "
                    "Officers see them as columns in the Exceptions page and in the CSV export."
                )
                exception_columns: list[dict[str, Any]] = leg.setdefault("exceptionColumns", [])
                for ec_index, column_spec in enumerate(list(exception_columns)):
                    columns = st.columns([1.2, 1.2, 1.2, 1.1, 0.4])
                    column_spec["alias"] = columns[0].text_input(
                        "Column name (in the exceptions table)",
                        column_spec.get("alias", ""),
                        key=f"ec_alias_{leg_index}_{ec_index}",
                    )
                    column_spec["left"] = columns[1].text_input(
                        "Left source column",
                        column_spec.get("left") or "",
                        key=f"ec_left_{leg_index}_{ec_index}",
                    ) or None
                    column_spec["right"] = columns[2].text_input(
                        "Right source column",
                        column_spec.get("right") or "",
                        key=f"ec_right_{leg_index}_{ec_index}",
                    ) or None
                    source_options = ["coalesce", "left", "right", "both"]
                    column_spec["source"] = columns[3].selectbox(
                        "Take from",
                        source_options,
                        index=source_options.index(column_spec.get("source", "coalesce")),
                        key=f"ec_src_{leg_index}_{ec_index}",
                        help=(
                            "coalesce: left value, falling back to right (best for one-sided breaks) · "
                            "left/right: always that side · both: 'left | right' side by side"
                        ),
                    )
                    if columns[4].button("🗑", key=f"ec_del_{leg_index}_{ec_index}"):
                        exception_columns.pop(ec_index)
                        st.rerun()

                add_columns = st.columns([1, 1, 2])
                if add_columns[0].button("➕ Add exception column", key=f"add_ec_{leg_index}"):
                    exception_columns.append({"alias": "", "left": "", "right": "", "source": "coalesce"})
                    st.rerun()
                if add_columns[1].button("Add from key columns", key=f"add_ec_keys_{leg_index}"):
                    for key in leg.get("keys", []):
                        alias = key.get("alias") or key.get("left")
                        if alias and not any(c.get("alias") == alias for c in exception_columns):
                            exception_columns.append(
                                {
                                    "alias": alias,
                                    "left": key.get("left"),
                                    "right": key.get("right"),
                                    "source": "coalesce",
                                }
                            )
                    st.rerun()

                if exception_columns:
                    st.info(
                        "Exception records will carry: "
                        + ", ".join(f"`{c.get('alias')}`" for c in exception_columns if c.get("alias"))
                    )

            # ---------------------------------------------------------- outputs
            with leg_tabs[4]:
                outputs: list[dict[str, Any]] = leg.setdefault("outputs", [])
                for output_index, output in enumerate(list(outputs)):
                    with st.container(border=True):
                        columns = st.columns([1, 1, 1.6, 0.4])
                        output["id"] = columns[0].text_input(
                            "Output ID", output.get("id") or f"output_{output_index + 1}",
                            key=f"out_id_{leg_index}_{output_index}",
                        )
                        output["type"] = columns[1].selectbox(
                            "Type",
                            OUTPUT_TYPES,
                            index=OUTPUT_TYPES.index(output.get("type", "jdbc"))
                            if output.get("type") in OUTPUT_TYPES
                            else 0,
                            key=f"out_type_{leg_index}_{output_index}",
                        )
                        if output["type"] in ("jdbc", "s3", "storagegrid", "kafka", "sftp", "filesystem"):
                            choices = ["<none>", *all_connections]
                            current = output.get("connectionRef")
                            output["connectionRef"] = columns[2].selectbox(
                                "Connection",
                                choices,
                                index=choices.index(current) if current in choices else 0,
                                key=f"out_conn_{leg_index}_{output_index}",
                            )
                            if output["connectionRef"] == "<none>":
                                output["connectionRef"] = None
                        if columns[3].button("🗑", key=f"out_del_{leg_index}_{output_index}"):
                            outputs.pop(output_index)
                            st.rerun()

                        if output["type"] == "jdbc":
                            output["table"] = st.text_input(
                                "Target table", output.get("table") or "",
                                key=f"out_table_{leg_index}_{output_index}",
                            )
                        elif output["type"] in ("s3", "storagegrid", "filesystem", "sftp"):
                            columns = st.columns([2, 1, 1])
                            output["path"] = columns[0].text_input(
                                "Path", output.get("path") or "", key=f"out_path_{leg_index}_{output_index}"
                            )
                            output["format"] = columns[1].selectbox(
                                "Format",
                                FILE_FORMATS,
                                index=FILE_FORMATS.index(output.get("format", "parquet"))
                                if output.get("format") in FILE_FORMATS
                                else 2,
                                key=f"out_fmt_{leg_index}_{output_index}",
                            )
                            modes = ["append", "overwrite", "errorifexists", "ignore"]
                            output["mode"] = columns[2].selectbox(
                                "Mode",
                                modes,
                                index=modes.index(output.get("mode", "append")),
                                key=f"out_mode_{leg_index}_{output_index}",
                            )
                        elif output["type"] == "kafka":
                            output["topic"] = st.text_input(
                                "Topic", output.get("topic") or "", key=f"out_topic_{leg_index}_{output_index}"
                            )
                        elif output["type"] == "temp_view":
                            output["view"] = st.text_input(
                                "View name", output.get("view") or "", key=f"out_view_{leg_index}_{output_index}"
                            )

                        output["categories"] = st.multiselect(
                            "Categories to write (empty = all)",
                            MATCH_CATEGORIES,
                            default=output.get("categories", []),
                            key=f"out_cats_{leg_index}_{output_index}",
                        )

                if st.button("➕ Add output", key=f"add_out_{leg_index}"):
                    outputs.append({"id": f"output_{len(outputs) + 1}", "type": "jdbc", "mode": "append"})
                    st.rerun()

                st.markdown("##### Exception output")
                st.caption(
                    "Optional. Without one, exceptions are written to the platform metrics database, "
                    "where the Exceptions page reads them from."
                )
                use_exception_output = st.checkbox(
                    "Write exceptions to a dedicated output",
                    value=bool(leg.get("exceptionOutput")),
                    key=f"use_exc_out_{leg_index}",
                )
                if use_exception_output:
                    exception_output = leg.setdefault(
                        "exceptionOutput", {"type": "s3", "format": "parquet", "mode": "append"}
                    )
                    columns = st.columns([1, 1.6, 1.4])
                    exception_output["type"] = columns[0].selectbox(
                        "Type",
                        OUTPUT_TYPES,
                        index=OUTPUT_TYPES.index(exception_output.get("type", "s3")),
                        key=f"exc_out_type_{leg_index}",
                    )
                    choices = ["<none>", *all_connections]
                    current = exception_output.get("connectionRef")
                    exception_output["connectionRef"] = columns[1].selectbox(
                        "Connection",
                        choices,
                        index=choices.index(current) if current in choices else 0,
                        key=f"exc_out_conn_{leg_index}",
                    )
                    if exception_output["connectionRef"] == "<none>":
                        exception_output["connectionRef"] = None
                    if exception_output["type"] == "jdbc":
                        exception_output["table"] = columns[2].text_input(
                            "Table", exception_output.get("table") or "", key=f"exc_out_table_{leg_index}"
                        )
                    else:
                        exception_output["path"] = columns[2].text_input(
                            "Path", exception_output.get("path") or "", key=f"exc_out_path_{leg_index}"
                        )
                else:
                    leg.pop("exceptionOutput", None)

            # --------------------------------------------------------- advanced
            with leg_tabs[5]:
                matching = leg.setdefault("matching", {})
                columns = st.columns(3)
                matching["duplicateDetection"] = columns[0].checkbox(
                    "Detect duplicate keys",
                    value=matching.get("duplicateDetection", True),
                    key=f"m_dup_{leg_index}",
                )
                matching["nullEqualsNull"] = columns[1].checkbox(
                    "NULL equals NULL",
                    value=matching.get("nullEqualsNull", True),
                    key=f"m_null_{leg_index}",
                )
                matching["caseInsensitiveKeys"] = columns[2].checkbox(
                    "Case-insensitive keys",
                    value=matching.get("caseInsensitiveKeys", False),
                    key=f"m_case_{leg_index}",
                )
                columns = st.columns(3)
                matching["keySeparator"] = columns[0].text_input(
                    "Key separator", matching.get("keySeparator", "|"), key=f"m_sep_{leg_index}"
                )
                matching["exceptionThreshold"] = columns[1].number_input(
                    "Exception threshold (PARTIAL_SUCCESS above)",
                    min_value=0,
                    value=int(matching.get("exceptionThreshold") or 0),
                    key=f"m_thr_{leg_index}",
                ) or None
                matching["maxExceptionRecords"] = columns[2].number_input(
                    "Max exception records persisted",
                    min_value=1000,
                    max_value=10_000_000,
                    value=int(matching.get("maxExceptionRecords") or 1_000_000),
                    step=1000,
                    key=f"m_max_{leg_index}",
                )

                st.markdown("##### Aggregate reconciliation")
                aggregates: list[dict[str, Any]] = leg.setdefault("aggregates", [])
                for a_index, aggregate in enumerate(list(aggregates)):
                    columns = st.columns([1.2, 1, 1, 1, 0.9, 0.4])
                    aggregate["name"] = columns[0].text_input(
                        "Name", aggregate.get("name") or "", key=f"agg_name_{leg_index}_{a_index}"
                    )
                    functions = ["COUNT", "SUM", "MIN", "MAX", "AVG", "COUNT_DISTINCT"]
                    aggregate["function"] = columns[1].selectbox(
                        "Function",
                        functions,
                        index=functions.index(aggregate.get("function", "COUNT")),
                        key=f"agg_fn_{leg_index}_{a_index}",
                    )
                    aggregate["leftField"] = columns[2].text_input(
                        "Left field", aggregate.get("leftField") or "", key=f"agg_l_{leg_index}_{a_index}"
                    ) or None
                    aggregate["rightField"] = columns[3].text_input(
                        "Right field", aggregate.get("rightField") or "", key=f"agg_r_{leg_index}_{a_index}"
                    ) or None
                    aggregate["tolerance"] = columns[4].number_input(
                        "Tolerance",
                        value=float(aggregate.get("tolerance") or 0.0),
                        step=0.01,
                        key=f"agg_tol_{leg_index}_{a_index}",
                    )
                    if columns[5].button("🗑", key=f"agg_del_{leg_index}_{a_index}"):
                        aggregates.pop(a_index)
                        st.rerun()
                if st.button("➕ Add aggregate check", key=f"add_agg_{leg_index}"):
                    aggregates.append({"name": "", "function": "COUNT", "tolerance": 0.0})
                    st.rerun()

                leg["dependsOn"] = st.multiselect(
                    "Depends on legs",
                    [x.get("id") for x in legs if x.get("id") != leg.get("id")],
                    default=leg.get("dependsOn", []),
                    key=f"leg_deps_{leg_index}",
                    help="Implicit when a source reads another leg's output; set explicitly for ordering.",
                )
                leg["continueOnFailure"] = st.checkbox(
                    "Continue the run if this leg fails",
                    value=bool(leg.get("continueOnFailure")),
                    key=f"leg_cof_{leg_index}",
                )

# --------------------------------------------------------------------------- #
# 4. Conditions
# --------------------------------------------------------------------------- #
with tabs[3]:
    st.caption(
        "Data-availability conditions hold a scheduled run in **WAITING_FOR_DATA** until the inputs are "
        "actually there, instead of reporting every record as a break."
    )
    use_conditions = st.checkbox(
        "Enable data-availability conditions", value=bool(definition.get("conditions"))
    )
    if use_conditions:
        conditions = definition.setdefault("conditions", {"operator": "AND", "conditions": []})
        conditions["operator"] = st.radio(
            "Combine with", ["AND", "OR", "NOT"], horizontal=True,
            index=["AND", "OR", "NOT"].index(conditions.get("operator", "AND")),
        )
        children: list[dict[str, Any]] = conditions.setdefault("conditions", [])
        for index, condition in enumerate(list(children)):
            with st.container(border=True):
                columns = st.columns([1.3, 1.4, 0.4])
                condition["type"] = columns[0].selectbox(
                    "Condition",
                    CONDITION_TYPES,
                    index=CONDITION_TYPES.index(condition.get("type", "file_exists"))
                    if condition.get("type") in CONDITION_TYPES
                    else 0,
                    key=f"cond_type_{index}",
                )
                choices = ["<none>", *all_connections]
                current = condition.get("connectionRef")
                condition["connectionRef"] = columns[1].selectbox(
                    "Connection",
                    choices,
                    index=choices.index(current) if current in choices else 0,
                    key=f"cond_conn_{index}",
                )
                if condition["connectionRef"] == "<none>":
                    condition["connectionRef"] = None
                if columns[2].button("🗑", key=f"cond_del_{index}"):
                    children.pop(index)
                    st.rerun()

                kind = condition["type"]
                if kind in ("file_exists", "s3_file_exists", "sftp_file_exists", "file_count", "file_size"):
                    columns = st.columns([2.4, 1, 1])
                    condition["path"] = columns[0].text_input(
                        "Path", condition.get("path") or "", key=f"cond_path_{index}",
                        help="Supports ${variables}, e.g. s3://payments/in/${business_date}/*.parquet",
                    )
                    condition["filePattern"] = columns[1].text_input(
                        "Pattern", condition.get("filePattern") or "", key=f"cond_pattern_{index}"
                    ) or None
                    condition["minCount"] = columns[2].number_input(
                        "Min files", min_value=1, value=int(condition.get("minCount", 1)),
                        key=f"cond_min_{index}",
                    )
                elif kind in ("jdbc_query", "custom_sql"):
                    condition["query"] = st.text_area(
                        "Query (must return a single scalar)",
                        condition.get("query") or "",
                        height=110,
                        key=f"cond_query_{index}",
                        help="e.g. SELECT COUNT(*) FROM transactions WHERE business_date = '${business_date}'",
                    )
                    columns = st.columns(2)
                    comparators = ["gt", "gte", "lt", "lte", "eq", "ne"]
                    condition["comparator"] = columns[0].selectbox(
                        "Comparator",
                        comparators,
                        index=comparators.index(condition.get("comparator", "gt")),
                        key=f"cond_cmp_{index}",
                    )
                    condition["threshold"] = columns[1].number_input(
                        "Threshold", value=float(condition.get("threshold", 0)), key=f"cond_thr_{index}"
                    )
                elif kind == "kafka_available":
                    columns = st.columns(3)
                    condition["topic"] = columns[0].text_input(
                        "Topic", condition.get("topic") or "", key=f"cond_topic_{index}"
                    )
                    condition["minMessages"] = columns[1].number_input(
                        "Min messages", min_value=1, value=int(condition.get("minMessages", 1)),
                        key=f"cond_msgs_{index}",
                    )
                    condition["lookbackHours"] = columns[2].number_input(
                        "Lookback (hours)", min_value=1, value=int(condition.get("lookbackHours", 24)),
                        key=f"cond_look_{index}",
                    )
                elif kind in ("previous_run_successful", "reconciliation_succeeded"):
                    columns = st.columns(2)
                    condition["reconId"] = columns[0].text_input(
                        "Reconciliation ID", condition.get("reconId") or "", key=f"cond_recon_{index}"
                    ) or None
                    condition["lookbackHours"] = columns[1].number_input(
                        "Lookback (hours)", min_value=1, value=int(condition.get("lookbackHours", 24)),
                        key=f"cond_look2_{index}",
                    )

        if st.button("➕ Add condition"):
            children.append({"type": "file_exists", "minCount": 1})
            st.rerun()

        evaluate_clicked = st.button("🧪 Evaluate conditions now") if children else False
        if definition.get("reconId") and evaluate_clicked:
            try:
                result = client.evaluate_conditions(definition["reconId"])
                (st.success if result["satisfied"] else st.warning)(result["summary"])
                st.json(result["detail"])
            except ApiError as exc:
                handle_api_error(exc)
    else:
        definition.pop("conditions", None)

# --------------------------------------------------------------------------- #
# 5. Schedule and notifications
# --------------------------------------------------------------------------- #
with tabs[4]:
    schedule = definition.setdefault("schedule", {"type": "manual", "timezone": "UTC"})
    schedule_types = ["manual", "cron", "interval", "daily", "weekly", "monthly", "once", "event"]
    columns = st.columns([1, 1, 1])
    schedule["type"] = columns[0].selectbox(
        "Schedule type",
        schedule_types,
        index=schedule_types.index(schedule.get("type", "manual")),
    )
    schedule["timezone"] = columns[1].text_input("Timezone", schedule.get("timezone", "UTC"))
    schedule["enabled"] = columns[2].checkbox("Enabled", value=schedule.get("enabled", True))

    if schedule["type"] == "cron":
        schedule["expression"] = st.text_input(
            "Cron expression", schedule.get("expression", "0 2 * * *"), help="Standard 5-field cron"
        )
    elif schedule["type"] == "interval":
        schedule["intervalSeconds"] = st.number_input(
            "Interval (seconds)", min_value=30, value=int(schedule.get("intervalSeconds", 3600)), step=30
        )
    elif schedule["type"] in ("daily", "weekly", "monthly"):
        columns = st.columns(3)
        schedule["time"] = columns[0].text_input("Time (HH:MM)", schedule.get("time", "02:00"))
        if schedule["type"] == "weekly":
            day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            selected_days = columns[1].multiselect(
                "Days", day_names, default=[day_names[d] for d in schedule.get("daysOfWeek", [0])]
            )
            schedule["daysOfWeek"] = [day_names.index(d) for d in selected_days]
        if schedule["type"] == "monthly":
            schedule["dayOfMonth"] = columns[1].number_input(
                "Day of month", min_value=1, max_value=31, value=int(schedule.get("dayOfMonth", 1))
            )

    columns = st.columns(4)
    schedule["timeoutMinutes"] = columns[0].number_input(
        "Timeout (minutes)", min_value=1, value=int(schedule.get("timeoutMinutes", 180))
    )
    schedule["maxConcurrentRuns"] = columns[1].number_input(
        "Max concurrent runs", min_value=1, max_value=50, value=int(schedule.get("maxConcurrentRuns", 1))
    )
    schedule["waitForDataMinutes"] = columns[2].number_input(
        "Wait for data (minutes)", min_value=0, value=int(schedule.get("waitForDataMinutes", 120))
    )
    schedule["businessDateOffsetDays"] = columns[3].number_input(
        "Business date offset (days)", value=int(schedule.get("businessDateOffsetDays", 0))
    )

    retries = schedule.setdefault("retries", {})
    columns = st.columns(3)
    retries["maxAttempts"] = columns[0].number_input(
        "Retry attempts", min_value=1, max_value=20, value=int(retries.get("maxAttempts", 1))
    )
    retries["initialDelaySeconds"] = columns[1].number_input(
        "Initial retry delay (s)", min_value=0, value=int(retries.get("initialDelaySeconds", 60))
    )
    retries["multiplier"] = columns[2].number_input(
        "Backoff multiplier", min_value=1.0, value=float(retries.get("multiplier", 2.0)), step=0.5
    )

    st.divider()
    st.markdown("##### Email notifications")
    email = definition.setdefault("notifications", {}).setdefault("email", {})
    email["enabled"] = st.checkbox("Send email notifications", value=email.get("enabled", False))
    if email["enabled"]:
        recipients = st.text_input(
            "Recipients (comma separated)", ", ".join(email.get("recipients", []))
        )
        email["recipients"] = [r.strip() for r in recipients.split(",") if r.strip()]
        email["on"] = st.multiselect(
            "Notify on",
            ["SUCCESS", "FAILURE", "PARTIAL_SUCCESS", "DATA_UNAVAILABLE", "EXCEPTION_THRESHOLD", "CANCELLED"],
            default=email.get("on", ["SUCCESS", "FAILURE"]),
        )
        columns = st.columns(3)
        email["subjectPrefix"] = columns[0].text_input(
            "Subject prefix", email.get("subjectPrefix", "[RECON]")
        )
        email["includeExceptionSample"] = columns[1].checkbox(
            "Include exception sample", value=email.get("includeExceptionSample", True)
        )
        email["exceptionThreshold"] = columns[2].number_input(
            "Exception threshold", min_value=0, value=int(email.get("exceptionThreshold") or 0)
        ) or None

    st.markdown("##### Kafka events")
    events = definition.setdefault("events", {})
    columns = st.columns(3)
    events["enabled"] = columns[0].checkbox("Publish events", value=events.get("enabled", True))
    failure_modes = ["WARN_ONLY", "RETRY", "FAIL_RUN"]
    events["onFailure"] = columns[1].selectbox(
        "If publishing fails",
        failure_modes,
        index=failure_modes.index(events.get("onFailure", "WARN_ONLY")),
        help="WARN_ONLY logs and stores the event in the outbox; FAIL_RUN fails the reconciliation.",
    )
    events["emitStageEvents"] = columns[2].checkbox(
        "Emit per-leg events", value=events.get("emitStageEvents", True)
    )

# --------------------------------------------------------------------------- #
# 6. Review, validate and save
# --------------------------------------------------------------------------- #
with tabs[5]:
    st.markdown("##### Definition preview")
    cleaned = {k: v for k, v in definition.items() if v not in (None, "", [], {})}
    st.json(cleaned, expanded=False)

    columns = st.columns([1, 1, 1, 1])
    if columns[0].button("✅ Validate", use_container_width=True):
        try:
            report = client.validate_definition(cleaned)
            st.session_state.designer_validation = report
        except ApiError as exc:
            handle_api_error(exc)

    report = st.session_state.get("designer_validation")
    if report:
        if report.get("valid"):
            st.success(f"Valid · {report.get('warningCount', 0)} warning(s)")
        else:
            st.error(f"{report.get('errorCount', 0)} error(s) must be fixed before saving")
        for issue in report.get("issues", []):
            icon = {"ERROR": "❌", "WARNING": "⚠️", "INFO": "ℹ️"}.get(issue["severity"], "•")
            st.markdown(f"{icon} `{issue['path']}` — {issue['message']}")
            if issue.get("hint"):
                st.caption(f"   ↳ {issue['hint']}")
        if report.get("executionOrder"):
            st.info(
                "Execution plan: "
                + " → ".join(f"[{', '.join(stage)}]" for stage in report["executionOrder"])
            )

    is_update = any(item["reconId"] == definition.get("reconId") for item in existing)
    comment = st.text_input("Change comment", key="designer_comment")

    if columns[1].button(
        "💾 Save draft", use_container_width=True, disabled=not has_permission("recon:create")
    ):
        try:
            if is_update:
                result = client.update_reconciliation(
                    definition["reconId"],
                    cleaned,
                    comment=comment or None,
                    expected_version=st.session_state.get("designer_loaded_version"),
                )
                if result.get("saved"):
                    st.success(
                        f"Saved version {result['definition']['version']} "
                        f"(status {result['definition']['status']})"
                    )
                    st.session_state.designer_loaded_version = result["definition"]["version"]
                else:
                    st.error("Not saved — fix the validation errors below")
                    st.session_state.designer_validation = result.get("validation")
            else:
                result = client.create_reconciliation(cleaned)
                if result.get("created"):
                    st.success(f"Created '{result['definition']['reconId']}' as a draft")
                    st.session_state.designer_loaded_version = result["definition"]["version"]
                else:
                    st.error("Not created — fix the validation errors below")
                    st.session_state.designer_validation = result.get("validation")
        except ApiError as exc:
            handle_api_error(exc)

    if columns[2].button(
        "🚀 Save & activate", use_container_width=True, disabled=not has_permission("recon:activate")
    ):
        try:
            if is_update:
                result = client.update_reconciliation(
                    definition["reconId"],
                    cleaned,
                    comment=comment or None,
                    expected_version=st.session_state.get("designer_loaded_version"),
                    activate=True,
                )
            else:
                result = client.create_reconciliation(cleaned, activate=True)
            if result.get("saved") or result.get("created"):
                st.success("Saved and activated — the scheduler will pick it up on its next tick")
                st.session_state.designer_loaded_version = result["definition"]["version"]
            else:
                st.error("Not saved — fix the validation errors")
                st.session_state.designer_validation = result.get("validation")
        except ApiError as exc:
            handle_api_error(exc)

    columns[3].download_button(
        "⬇️ Export YAML",
        data=_to_yaml(cleaned),
        file_name=f"{definition.get('reconId') or 'reconciliation'}.yaml",
        mime="application/x-yaml",
        use_container_width=True,
    )

    with st.expander("Import from YAML/JSON"):
        uploaded = st.file_uploader("Configuration file", type=["yaml", "yml", "json"])
        import_clicked = st.button("Import")
        if uploaded is not None and import_clicked:
            import yaml

            try:
                data = yaml.safe_load(uploaded.getvalue().decode("utf-8"))
                if isinstance(data, dict) and "reconciliation" in data:
                    data = data["reconciliation"]
                if isinstance(data, dict) and "id" in data and "reconId" not in data:
                    data["reconId"] = data.pop("id")
                st.session_state.designer_definition = data
                st.success("Imported — review the tabs and validate before saving")
                st.rerun()
            except Exception as exc:
                st.error(f"Could not parse the file: {exc}")
