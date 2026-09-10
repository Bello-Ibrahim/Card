"""Administration: users, roles, audit trail and platform maintenance."""

from __future__ import annotations

import streamlit as st

from reconx.ui.api_client import ApiError
from reconx.ui.components import (
    current_user,
    empty_state,
    get_client,
    handle_api_error,
    has_permission,
    page_header,
    timestamp,
    to_dataframe,
)

page_header("Administration", "Users, roles, audit trail and maintenance", "⚙️")
client = get_client()

tabs = st.tabs(["👥 Users", "🔐 Roles & permissions", "📜 Audit trail", "🧰 Maintenance"])

with tabs[0]:
    if not has_permission("user:manage"):
        st.info("You need the `user:manage` permission to administer users.")
    else:
        try:
            users = client.users()
            roles_payload = client.roles()
        except ApiError as exc:
            handle_api_error(exc)
            st.stop()

        role_names = [role["role"] for role in roles_payload.get("roles", [])]
        st.dataframe(
            to_dataframe(
                [
                    {
                        "Username": user.get("username"),
                        "Display name": user.get("displayName"),
                        "Roles": ", ".join(user.get("roles", [])),
                        "Email": user.get("email"),
                        "Enabled": user.get("enabled"),
                        "Source": user.get("source"),
                        "Last login": timestamp(user.get("lastLoginAt")),
                        "Failed logins": user.get("failedLoginAttempts", 0),
                    }
                    for user in users
                ]
            ),
            use_container_width=True,
            hide_index=True,
        )

        columns = st.columns(2)
        with columns[0]:
            st.markdown("##### Create a user")
            with st.form("create_user"):
                username = st.text_input("Username")
                password = st.text_input("Password", type="password", help="At least 8 characters")
                display_name = st.text_input("Display name")
                email = st.text_input("Email")
                selected_roles = st.multiselect("Roles", role_names, default=["VIEWER"])
                if st.form_submit_button("Create user", type="primary"):
                    try:
                        client.create_user(
                            {
                                "username": username,
                                "password": password,
                                "roles": selected_roles,
                                "displayName": display_name or None,
                                "email": email or None,
                            }
                        )
                        st.success(f"User '{username}' created")
                        st.rerun()
                    except ApiError as exc:
                        handle_api_error(exc)

        with columns[1]:
            st.markdown("##### Update a user")
            if users:
                with st.form("update_user"):
                    target = st.selectbox("User", [u["username"] for u in users])
                    existing = next(u for u in users if u["username"] == target)
                    new_roles = st.multiselect("Roles", role_names, default=existing.get("roles", []))
                    enabled = st.checkbox("Enabled", value=existing.get("enabled", True))
                    new_password = st.text_input("New password (blank = unchanged)", type="password")
                    if st.form_submit_button("Update user"):
                        try:
                            client.update_user(
                                target,
                                {
                                    "roles": new_roles,
                                    "enabled": enabled,
                                    "password": new_password or None,
                                },
                            )
                            st.success(f"User '{target}' updated")
                            st.rerun()
                        except ApiError as exc:
                            handle_api_error(exc)

                if st.button("🗑 Delete selected user", type="secondary"):
                    st.session_state.confirm_delete_user = True
                if st.session_state.get("confirm_delete_user"):
                    st.warning("This cannot be undone.")
                    if st.button("Confirm delete", type="primary"):
                        try:
                            client.delete_user(target)
                            st.session_state.confirm_delete_user = False
                            st.success("User deleted")
                            st.rerun()
                        except ApiError as exc:
                            handle_api_error(exc)

with tabs[1]:
    try:
        roles_payload = client.roles()
    except ApiError as exc:
        handle_api_error(exc)
        roles_payload = {"roles": []}

    st.caption(
        "Permissions are checked in the API on every request; the UI only hides what the signed-in user "
        "cannot do."
    )
    for role in roles_payload.get("roles", []):
        with st.expander(f"**{role['role']}** — {role['count']} permission(s)"):
            st.markdown("\n".join(f"- `{permission}`" for permission in role["permissions"]))

    st.markdown("##### Your effective permissions")
    st.json(sorted(current_user().get("permissions", [])))

with tabs[2]:
    if not has_permission("audit:view"):
        st.info("You need the `audit:view` permission (ADMIN or AUDITOR role).")
    else:
        filters = st.columns(4)
        entity_type = filters[0].selectbox(
            "Entity", ["All", "reconciliation", "connection", "run", "schedule", "exception", "user", "api"]
        )
        action = filters[1].text_input("Action", "")
        actor = filters[2].text_input("Actor", "")
        limit = filters[3].selectbox("Rows", [100, 250, 500], index=0)
        try:
            entries = client.audit(
                entity_type=None if entity_type == "All" else entity_type,
                action=action or None,
                actor=actor or None,
                limit=limit,
            )
        except ApiError as exc:
            handle_api_error(exc)
            entries = []
        if entries:
            st.dataframe(
                to_dataframe(
                    [
                        {
                            "Time": timestamp(entry.get("timestamp")),
                            "Action": entry.get("action"),
                            "Entity": f"{entry.get('entityType')}/{entry.get('entityId')}",
                            "Actor": entry.get("actor"),
                            "Success": entry.get("success"),
                            "Versions": f"{entry.get('oldVersion') or '—'} → {entry.get('newVersion') or '—'}",
                            "Source IP": entry.get("sourceIp"),
                        }
                        for entry in entries
                    ]
                ),
                use_container_width=True,
                hide_index=True,
                height=420,
            )
            selected_index = st.number_input(
                "Inspect entry #", min_value=0, max_value=max(0, len(entries) - 1), value=0
            )
            st.json(entries[int(selected_index)])
        else:
            empty_state("No audit entries match", icon="📜")

with tabs[3]:
    if not has_permission("system:manage"):
        st.info("You need the `system:manage` permission for maintenance actions.")
    else:
        st.markdown("##### Initialise storage")
        st.caption(
            "Creates the MongoDB indexes and the metrics tables. Safe to run repeatedly — it only creates "
            "what is missing."
        )
        if st.button("🧱 Create indexes and tables", type="primary"):
            try:
                result = client.initialise()
                st.success(
                    f"{len(result.get('indexes', []))} index(es) and "
                    f"{len(result.get('tables', []))} table(s) ensured"
                )
                st.json(result)
            except ApiError as exc:
                handle_api_error(exc)

        st.divider()
        st.markdown("##### Platform information")
        try:
            st.json(client.system_info())
        except ApiError as exc:
            handle_api_error(exc)
