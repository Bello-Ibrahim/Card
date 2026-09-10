"""ReconX Streamlit UI - entry point.

Navigation is built programmatically so pages can be hidden from users whose
role does not grant the underlying permission; the API enforces the same rules
again server-side.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import streamlit as st

# Allow `streamlit run src/reconx/ui/streamlit_app.py` from a source checkout.
_SRC = Path(__file__).resolve().parents[2]
if str(_SRC) not in sys.path:  # pragma: no cover - import bootstrap
    sys.path.insert(0, str(_SRC))

from reconx import __version__
from reconx.ui.api_client import ApiError
from reconx.ui.components import current_user, get_client, logout

st.set_page_config(
    page_title="ReconX - Reconciliation Platform",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": f"ReconX Enterprise Data Reconciliation Platform v{__version__}",
        "Report a Bug": None,
        "Get Help": None,
    },
)

st.markdown(
    """
    <style>
      .block-container {padding-top: 2.2rem; padding-bottom: 3rem; max-width: 1500px;}
      [data-testid="stMetricValue"] {font-size: 1.55rem;}
      [data-testid="stMetricLabel"] {font-size: 0.82rem; color: #57606a;}
      div[data-testid="stExpander"] details summary p {font-weight: 600;}
      .stTabs [data-baseweb="tab-list"] {gap: 4px;}
      .stTabs [data-baseweb="tab"] {padding: 6px 14px;}
      code {font-size: 0.85em;}
    </style>
    """,
    unsafe_allow_html=True,
)


def _login_view() -> None:
    _, middle, _ = st.columns([1, 1.2, 1])
    with middle:
        st.markdown("<div style='height:6vh'></div>", unsafe_allow_html=True)
        st.markdown("# 🔗 ReconX")
        st.caption("Enterprise Distributed Data Reconciliation Platform")
        with st.container(border=True):
            st.markdown("#### Sign in")
            with st.form("login_form"):
                username = st.text_input("Username", autocomplete="username")
                password = st.text_input("Password", type="password", autocomplete="current-password")
                submitted = st.form_submit_button("Sign in", type="primary", use_container_width=True)
            if submitted:
                client = get_client()
                try:
                    payload = client.login(username, password)
                    st.session_state.token = payload["accessToken"]
                    st.session_state.user = payload["user"]
                    st.rerun()
                except ApiError as exc:
                    st.error(exc.message)
        api_url = os.getenv("RECONX_API_URL", "http://localhost:8000")
        st.caption(f"Control plane: `{api_url}`")
        with st.expander("First time here?"):
            st.markdown(
                "The API creates an initial **ADMIN** user on first start.\n\n"
                "- Username: `RECONX_SECURITY_BOOTSTRAP_ADMIN_USERNAME` (default `admin`)\n"
                "- Password: `RECONX_SECURITY_BOOTSTRAP_ADMIN_PASSWORD`, or a generated one printed "
                "**once** in the API logs (`api.bootstrap_admin_password_generated`)\n\n"
                "Change it immediately after signing in, under **Administration → Users**."
            )


def _sidebar(user: dict) -> None:
    with st.sidebar:
        st.markdown("### 🔗 ReconX")
        st.caption(f"v{__version__}")
        st.markdown(
            f"**{user.get('displayName') or user.get('username')}**  \n"
            f"<span style='color:#57606a;font-size:0.82rem'>{', '.join(user.get('roles', []))}</span>",
            unsafe_allow_html=True,
        )
        if st.button("Sign out", use_container_width=True):
            logout()
            st.rerun()
        st.divider()
        try:
            health = get_client().health()
            st.caption(f"API {health.get('status', '?')} · {health.get('hostname', '')}")
        except ApiError:
            st.error("API unreachable")


def main() -> None:
    if not st.session_state.get("token"):
        _login_view()
        return

    user = current_user()
    if not user:
        try:
            st.session_state.user = get_client().me()
            user = st.session_state.user
        except ApiError:
            logout()
            st.rerun()

    permissions = set(user.get("permissions", []))
    _sidebar(user)

    pages_dir = Path(__file__).parent / "pages"

    def page(filename: str, title: str, icon: str, permission: str | None = None) -> object | None:
        if permission and permission not in permissions:
            return None
        return st.Page(str(pages_dir / filename), title=title, icon=icon)

    sections: dict[str, list[object]] = {
        "Overview": [
            page("dashboard.py", "Dashboard", "📊", "report:view"),
            page("reports.py", "Reports", "📈", "report:view"),
        ],
        "Configure": [
            page("reconciliations.py", "Reconciliations", "🧾", "recon:view"),
            page("designer.py", "Reconciliation Designer", "🛠️", "recon:view"),
            page("connections.py", "Connections", "🔌", "connection:view"),
            page("schedules.py", "Schedules", "🗓️", "schedule:view"),
        ],
        "Operate": [
            page("runs.py", "Runs", "▶️", "run:view"),
            page("exceptions.py", "Exceptions", "🚨", "exception:view"),
            page("advisor.py", "Recon Advisor", "💬", "run:view"),
        ],
        "Administer": [
            page("system_health.py", "System Health", "❤️", "run:view"),
            page("administration.py", "Administration", "⚙️", "recon:view"),
        ],
    }
    navigation = {
        section: [p for p in pages if p is not None]
        for section, pages in sections.items()
        if any(p is not None for p in pages)
    }
    if not navigation:
        st.error("Your account has no permissions assigned. Contact your platform administrator.")
        return
    st.navigation(navigation).run()


main()
