"""Connection management: create, test and preview data sources."""

from __future__ import annotations

from typing import Any

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

CONNECTION_TYPES = ["jdbc", "s3", "storagegrid", "sftp", "kafka", "filesystem"]
DATABASE_TYPES = ["postgresql", "mysql", "mariadb", "sqlserver", "oracle", "db2", "sqlite", "h2"]

page_header("Connections", "How ReconX reaches your data - secrets are never stored in clear", "🔌")
client = get_client()

tabs = st.tabs(["📋 All connections", "➕ New connection", "🔍 Explore & preview"])

# --------------------------------------------------------------------------- #
# List
# --------------------------------------------------------------------------- #
with tabs[0]:
    try:
        connections = client.list_connections()
    except ApiError as exc:
        handle_api_error(exc)
        connections = []

    if not connections:
        empty_state("No connections yet", "Create one on the next tab.", icon="🔌")
    else:
        st.dataframe(
            to_dataframe(
                [
                    {
                        "ID": c["connectionId"],
                        "Name": c.get("name"),
                        "Type": c.get("type"),
                        "Environment": c.get("environment"),
                        "Enabled": c.get("enabled"),
                        "Last tested": timestamp(c.get("lastTestedAt"), with_seconds=False),
                        "Result": (c.get("lastTestResult") or "")[:70],
                    }
                    for c in connections
                ]
            ),
            use_container_width=True,
            hide_index=True,
        )

        selected = st.selectbox("Connection", [c["connectionId"] for c in connections])
        connection = next(c for c in connections if c["connectionId"] == selected)

        columns = st.columns([1, 1, 1, 3])
        if columns[0].button("🧪 Test", use_container_width=True, disabled=not has_permission("connection:test")):
            with st.spinner("Testing..."):
                try:
                    result = client.test_connection(selected)
                    if result["success"]:
                        st.success(f"{result['message']} ({result.get('latencyMs')} ms)")
                    else:
                        st.error(result["message"])
                    if result.get("details"):
                        st.json(result["details"])
                    if result.get("validationWarnings"):
                        for warning in result["validationWarnings"]:
                            st.warning(warning)
                except ApiError as exc:
                    handle_api_error(exc)
        if columns[1].button("🗑 Delete", use_container_width=True, disabled=not has_permission("connection:manage")):
            try:
                client.delete_connection(selected)
                st.success("Deleted")
                st.rerun()
            except ApiError as exc:
                handle_api_error(exc)

        st.markdown("##### Configuration")
        st.caption("Secret fields are shown masked; leave them as `********` to keep the stored value.")
        edited = st.data_editor(
            [{"Field": k, "Value": str(v)} for k, v in (connection.get("config") or {}).items()],
            use_container_width=True,
            hide_index=True,
            num_rows="dynamic",
            disabled=not has_permission("connection:manage"),
            key=f"conn_editor_{selected}",
        )
        if st.button("💾 Save changes", disabled=not has_permission("connection:manage")):
            config: dict[str, Any] = {}
            for row in edited:
                if not row.get("Field"):
                    continue
                value = row.get("Value")
                if isinstance(value, str):
                    if value.lower() in ("true", "false"):
                        value = value.lower() == "true"
                    elif value.isdigit():
                        value = int(value)
                config[row["Field"]] = value
            try:
                client.update_connection(
                    selected,
                    {
                        "connectionId": selected,
                        "name": connection.get("name"),
                        "type": connection.get("type"),
                        "environment": connection.get("environment", "default"),
                        "enabled": connection.get("enabled", True),
                        "description": connection.get("description"),
                        "config": config,
                    },
                )
                st.success("Connection updated")
                st.rerun()
            except ApiError as exc:
                handle_api_error(exc)

# --------------------------------------------------------------------------- #
# Create
# --------------------------------------------------------------------------- #
with tabs[1]:
    if not has_permission("connection:manage"):
        st.info("You need the `connection:manage` permission to create connections.")
    else:
        connection_type = st.selectbox("Connection type", CONNECTION_TYPES, key="new_conn_type")
        with st.form("new_connection"):
            columns = st.columns(3)
            connection_id = columns[0].text_input("Connection ID *", placeholder="mssql_payments")
            name = columns[1].text_input("Name *", placeholder="Payments SQL Server")
            environment = columns[2].text_input("Environment", "default")
            description = st.text_input("Description", "")

            config: dict[str, Any] = {}
            if connection_type == "jdbc":
                columns = st.columns(3)
                config["databaseType"] = columns[0].selectbox("Database", DATABASE_TYPES)
                config["host"] = columns[1].text_input("Host", placeholder="sql1.corp.example.com")
                config["port"] = columns[2].number_input("Port", min_value=0, max_value=65535, value=1433)
                columns = st.columns(3)
                config["database"] = columns[0].text_input("Database")
                config["schema"] = columns[1].text_input("Schema", placeholder="dbo")
                config["ssl"] = columns[2].checkbox("Use SSL/TLS", value=False)
                columns = st.columns(2)
                config["username"] = columns[0].text_input("Username")
                config["password"] = columns[1].text_input("Password", type="password")
                config["jdbcUrl"] = st.text_input(
                    "JDBC URL (optional - overrides the fields above)",
                    placeholder="jdbc:sqlserver://sql1:1433;databaseName=Payments;encrypt=true",
                )
                columns = st.columns(3)
                config["fetchSize"] = columns[0].number_input("Fetch size", min_value=100, value=10000, step=100)
                config["numPartitions"] = columns[1].number_input(
                    "Read partitions (0 = single)", min_value=0, value=0
                ) or None
                config["partitionColumn"] = columns[2].text_input("Partition column") or None
            elif connection_type in ("s3", "storagegrid"):
                columns = st.columns(2)
                config["endpoint"] = columns[0].text_input(
                    "Endpoint" + (" *" if connection_type == "storagegrid" else " (blank for AWS)"),
                    placeholder="https://sg.corp.example.com:8082",
                )
                config["region"] = columns[1].text_input("Region", "us-east-1")
                columns = st.columns(2)
                config["bucket"] = columns[0].text_input("Bucket")
                config["basePath"] = columns[1].text_input("Base path (optional)")
                config["useInstanceProfile"] = st.checkbox(
                    "Use IAM instance profile / IRSA (no keys)", value=False
                )
                columns = st.columns(2)
                config["accessKey"] = columns[0].text_input("Access key", type="password")
                config["secretKey"] = columns[1].text_input("Secret key", type="password")
                columns = st.columns(3)
                config["pathStyleAccess"] = columns[0].checkbox(
                    "Path-style access", value=connection_type == "storagegrid"
                )
                config["sslEnabled"] = columns[1].checkbox("SSL enabled", value=True)
                config["sslVerify"] = columns[2].checkbox("Verify certificates", value=True)
            elif connection_type == "sftp":
                columns = st.columns(3)
                config["host"] = columns[0].text_input("Host")
                config["port"] = columns[1].number_input("Port", min_value=1, max_value=65535, value=22)
                config["basePath"] = columns[2].text_input("Base path", "/")
                columns = st.columns(2)
                config["username"] = columns[0].text_input("Username")
                config["password"] = columns[1].text_input("Password", type="password")
                config["privateKey"] = st.text_area(
                    "Private key (PEM) or a secret reference such as k8s:sftp_key", height=90
                )
                columns = st.columns(2)
                config["knownHosts"] = columns[0].text_input("Known hosts file", "/etc/ssh/ssh_known_hosts")
                config["strictHostKeyChecking"] = columns[1].checkbox(
                    "Strict host key checking", value=True
                )
            elif connection_type == "kafka":
                config["bootstrapServers"] = st.text_input("Bootstrap servers", "kafka:9092")
                columns = st.columns(2)
                config["securityProtocol"] = columns[0].selectbox(
                    "Security protocol", ["PLAINTEXT", "SSL", "SASL_PLAINTEXT", "SASL_SSL"]
                )
                config["saslMechanism"] = columns[1].selectbox(
                    "SASL mechanism", ["", "PLAIN", "SCRAM-SHA-256", "SCRAM-SHA-512"]
                ) or None
                columns = st.columns(2)
                config["saslUsername"] = columns[0].text_input("SASL username") or None
                config["saslPassword"] = columns[1].text_input("SASL password", type="password") or None
            elif connection_type == "filesystem":
                config["basePath"] = st.text_input("Base path", "/data")
                columns = st.columns(2)
                config["writable"] = columns[0].checkbox("Writable", value=True)
                config["createMissingDirectories"] = columns[1].checkbox(
                    "Create missing directories", value=True
                )
                st.caption(
                    "In a multi-node cluster every node must see this path — use an NFS mount or a "
                    "ReadWriteMany PersistentVolumeClaim."
                )

            columns = st.columns(2)
            test_first = columns[0].form_submit_button("🧪 Test without saving")
            create = columns[1].form_submit_button("💾 Create connection", type="primary")

        payload = {
            "connectionId": connection_id,
            "name": name,
            "type": connection_type,
            "environment": environment,
            "description": description or None,
            "enabled": True,
            "config": {k: v for k, v in config.items() if v not in (None, "", 0)},
        }
        if test_first:
            try:
                result = client.test_unsaved_connection(payload)
                (st.success if result["success"] else st.error)(result["message"])
                if result.get("details"):
                    st.json(result["details"])
            except ApiError as exc:
                handle_api_error(exc)
        if create:
            if not connection_id or not name:
                st.error("Connection ID and name are required.")
            else:
                try:
                    client.create_connection(payload)
                    st.success(f"Connection '{connection_id}' created")
                    st.rerun()
                except ApiError as exc:
                    handle_api_error(exc)

        st.caption(
            "Secrets you type here are encrypted before they reach MongoDB. You can also store a "
            "**reference** instead: `env:VAR`, `file:/path`, `k8s:key` or `vault:path#key`."
        )

# --------------------------------------------------------------------------- #
# Explore
# --------------------------------------------------------------------------- #
with tabs[2]:
    try:
        connections = client.list_connections(enabled=True)
    except ApiError as exc:
        handle_api_error(exc)
        connections = []
    if not connections:
        empty_state("No connections to explore", icon="🔍")
    else:
        selected = st.selectbox(
            "Connection", [c["connectionId"] for c in connections], key="explore_conn"
        )
        connection = next(c for c in connections if c["connectionId"] == selected)

        if connection["type"] == "jdbc":
            st.markdown("##### Query preview")
            st.caption(
                "Write the query in your database's own dialect — SQL Server `SELECT TOP (n) ... WITH "
                "(NOLOCK)`, Oracle `FETCH FIRST`, PostgreSQL `LIMIT`. `${variables}` are substituted in the "
                "query **and** in table names. Only read-only statements are permitted."
            )
            mode = st.radio("Preview", ["SQL query", "Table"], horizontal=True, key="explore_mode")
            variables_text = st.text_area(
                "Variables (one per line, name=value)",
                "business_date=2026-09-10",
                height=80,
                key="explore_vars",
            )
            variables = {}
            for line in variables_text.splitlines():
                if "=" in line:
                    key, _, value = line.partition("=")
                    variables[key.strip()] = value.strip()

            if mode == "SQL query":
                query = st.text_area(
                    "SQL",
                    "SELECT TOP (100) *\nFROM ${table_name}\nWHERE [BusinessDate] = '${business_date}'",
                    height=150,
                    key="explore_query",
                )
                table = None
            else:
                table = st.text_input("Table", "[dbo].[Transactions]", key="explore_table")
                query = None

            columns = st.columns([1, 1, 3])
            limit = columns[0].number_input("Row limit", min_value=1, max_value=5000, value=100)
            if columns[1].button("🔍 Run preview", type="primary"):
                try:
                    preview = client.preview_query(
                        selected, query=query, table=table, limit=int(limit), variables=variables
                    )
                    st.success(
                        f"{preview['rowCount']} row(s) in {preview['elapsedMs']} ms"
                        + (" (truncated)" if preview.get("truncated") else "")
                    )
                    st.code(preview["statement"], language="sql")
                    st.dataframe(preview["rows"], use_container_width=True, hide_index=True)
                    st.caption("Columns: " + ", ".join(preview["columns"]))
                except ApiError as exc:
                    handle_api_error(exc)

            if st.button("📋 List tables and views"):
                try:
                    st.dataframe(client.list_tables(selected), use_container_width=True, hide_index=True)
                except ApiError as exc:
                    handle_api_error(exc)
        else:
            st.markdown("##### Browse files")
            columns = st.columns([2.5, 1, 1])
            path = columns[0].text_input("Path", "", key="explore_path")
            pattern = columns[1].text_input("Pattern", "", key="explore_pattern")
            if columns[2].button("📂 List", type="primary"):
                try:
                    files = client.list_files(selected, path, pattern or None)
                    if files:
                        st.dataframe(files, use_container_width=True, hide_index=True)
                    else:
                        st.info("No files matched.")
                except ApiError as exc:
                    handle_api_error(exc)
