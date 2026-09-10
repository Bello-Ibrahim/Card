"""Control-plane API: authentication, RBAC, CRUD and the exception workflow."""

from __future__ import annotations

from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from reconx.config.enums import Role

pytestmark = pytest.mark.integration


@pytest.fixture
def client(mongo_db, metrics_repository, monkeypatch) -> Iterator[TestClient]:
    """API wired to the in-memory MongoDB and the test metrics database."""
    from reconx.api import deps
    from reconx.api.main import create_app
    from reconx.config.settings import get_settings
    from reconx.config.store import ensure_indexes
    from reconx.security.auth import MongoUserStore

    ensure_indexes(mongo_db)
    settings = get_settings()

    app = create_app(settings)
    app.dependency_overrides[deps.database_dependency] = lambda: mongo_db
    app.dependency_overrides[deps.metrics_dependency] = lambda: metrics_repository
    deps._scheduler_singleton = None

    store = MongoUserStore(mongo_db, settings)
    store.ensure_indexes()
    store.create_user("admin_user", "admin-password", [Role.ADMIN.value])
    store.create_user("viewer_user", "viewer-password", [Role.VIEWER.value])
    store.create_user("operator_user", "operator-password", [Role.OPERATOR.value])

    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def _token(client: TestClient, username: str, password: str) -> str:
    response = client.post("/api/auth/login", json={"username": username, "password": password})
    assert response.status_code == 200, response.text
    return response.json()["accessToken"]


@pytest.fixture
def admin_headers(client) -> dict[str, str]:
    return {"Authorization": f"Bearer {_token(client, 'admin_user', 'admin-password')}"}


@pytest.fixture
def viewer_headers(client) -> dict[str, str]:
    return {"Authorization": f"Bearer {_token(client, 'viewer_user', 'viewer-password')}"}


class TestHealth:
    def test_health_needs_no_authentication(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "UP"

    def test_readiness_reports_each_dependency(self, client):
        payload = client.get("/ready").json()
        assert "mongodb" in payload["checks"]
        assert "metricsDatabase" in payload["checks"]

    def test_prometheus_metrics_are_exposed(self, client):
        response = client.get("/metrics")
        assert response.status_code == 200
        assert "reconx_definitions" in response.text

    def test_openapi_document_is_generated(self, client):
        document = client.get("/openapi.json").json()
        assert document["info"]["title"] == "ReconX Control Plane"
        assert "/api/reconciliations" in document["paths"]

    def test_correlation_id_is_returned(self, client):
        response = client.get("/health", headers={"X-Correlation-Id": "abc-123"})
        assert response.headers["X-Correlation-Id"] == "abc-123"

    def test_security_headers_are_set(self, client):
        response = client.get("/health")
        assert response.headers["X-Content-Type-Options"] == "nosniff"
        assert response.headers["X-Frame-Options"] == "DENY"


class TestAuthentication:
    def test_bad_credentials_are_rejected(self, client):
        assert client.post(
            "/api/auth/login", json={"username": "admin_user", "password": "wrong"}
        ).status_code == 401

    def test_unauthenticated_requests_are_rejected(self, client):
        assert client.get("/api/reconciliations").status_code == 401

    def test_invalid_token_is_rejected(self, client):
        assert client.get(
            "/api/reconciliations", headers={"Authorization": "Bearer nonsense"}
        ).status_code == 401

    def test_me_returns_effective_permissions(self, client, admin_headers):
        payload = client.get("/api/auth/me", headers=admin_headers).json()
        assert payload["username"] == "admin_user"
        assert "recon:create" in payload["permissions"]

    def test_roles_endpoint_lists_every_role(self, client, admin_headers):
        payload = client.get("/api/auth/roles", headers=admin_headers).json()
        assert {role["role"] for role in payload["roles"]} == {r.value for r in Role}


class TestRbac:
    def test_viewer_cannot_create(self, client, viewer_headers, sample_definition):
        response = client.post(
            "/api/reconciliations", json={"definition": sample_definition}, headers=viewer_headers
        )
        assert response.status_code == 403

    def test_viewer_can_read(self, client, viewer_headers):
        assert client.get("/api/reconciliations", headers=viewer_headers).status_code == 200

    def test_viewer_cannot_manage_users(self, client, viewer_headers):
        assert client.get("/api/auth/users", headers=viewer_headers).status_code == 403

    def test_permission_denials_are_audited(self, client, viewer_headers, admin_headers, sample_definition):
        client.post(
            "/api/reconciliations", json={"definition": sample_definition}, headers=viewer_headers
        )
        entries = client.get(
            "/api/system/audit", params={"action": "PERMISSION_DENIED"}, headers=admin_headers
        ).json()["items"]
        assert entries and entries[0]["actor"] == "viewer_user"


class TestReconciliationEndpoints:
    def _create_connection(self, client, headers):
        return client.post(
            "/api/connections",
            json={
                "connection": {
                    "connectionId": "local_files",
                    "name": "Local files",
                    "type": "filesystem",
                    "config": {"basePath": "/"},
                }
            },
            headers=headers,
        )

    def test_full_lifecycle(self, client, admin_headers, sample_definition):
        assert self._create_connection(client, admin_headers).status_code == 201

        created = client.post(
            "/api/reconciliations", json={"definition": sample_definition}, headers=admin_headers
        )
        assert created.status_code == 201, created.text
        assert created.json()["created"] is True
        assert created.json()["definition"]["version"] == 1

        detail = client.get(
            f"/api/reconciliations/{sample_definition['reconId']}", headers=admin_headers
        ).json()
        assert detail["definition"]["name"] == sample_definition["name"]
        assert detail["schedule"]["description"].startswith("Cron")

        activated = client.post(
            f"/api/reconciliations/{sample_definition['reconId']}/activate", headers=admin_headers
        )
        assert activated.json()["definition"]["status"] == "ACTIVE"

        updated = dict(sample_definition, description="v2")
        saved = client.put(
            f"/api/reconciliations/{sample_definition['reconId']}",
            json={"definition": updated, "comment": "second version"},
            headers=admin_headers,
        )
        assert saved.json()["saved"] is True
        assert saved.json()["definition"]["version"] == 2

        versions = client.get(
            f"/api/reconciliations/{sample_definition['reconId']}/versions", headers=admin_headers
        ).json()["items"]
        assert len(versions) == 2

        disabled = client.post(
            f"/api/reconciliations/{sample_definition['reconId']}/disable", headers=admin_headers
        )
        assert disabled.json()["definition"]["status"] == "DISABLED"

    def test_validation_endpoint_reports_issues(self, client, admin_headers):
        broken = {
            "reconId": "broken_recon",
            "name": "Broken",
            "legs": [
                {
                    "id": "leg",
                    "sources": [
                        {"id": "a", "type": "jdbc", "connectionRef": "nope", "query": "DROP TABLE x"},
                        {"id": "b", "type": "jdbc", "connectionRef": "nope", "table": "t"},
                    ],
                    "keys": [{"left": "id", "right": "id"}],
                }
            ],
        }
        report = client.post(
            "/api/reconciliations/validate", json={"definition": broken}, headers=admin_headers
        ).json()
        assert report["valid"] is False
        assert report["errorCount"] >= 1

    def test_validation_endpoint_reports_schema_errors_gracefully(self, client, admin_headers):
        report = client.post(
            "/api/reconciliations/validate",
            json={"definition": {"name": "missing id"}},
            headers=admin_headers,
        ).json()
        assert report["valid"] is False

    def test_clone_and_rollback(self, client, admin_headers, sample_definition):
        self._create_connection(client, admin_headers)
        client.post("/api/reconciliations", json={"definition": sample_definition}, headers=admin_headers)
        client.put(
            f"/api/reconciliations/{sample_definition['reconId']}",
            json={"definition": dict(sample_definition, description="v2")},
            headers=admin_headers,
        )
        rolled_back = client.post(
            f"/api/reconciliations/{sample_definition['reconId']}/rollback",
            json={"version": 1, "comment": "revert"},
            headers=admin_headers,
        ).json()
        assert rolled_back["definition"]["version"] == 3

        cloned = client.post(
            f"/api/reconciliations/{sample_definition['reconId']}/clone",
            json={"newReconId": "payments_copy", "newName": "Copy"},
            headers=admin_headers,
        )
        assert cloned.status_code == 201
        assert cloned.json()["definition"]["reconId"] == "payments_copy"

    def test_facets(self, client, admin_headers, sample_definition):
        self._create_connection(client, admin_headers)
        client.post("/api/reconciliations", json={"definition": sample_definition}, headers=admin_headers)
        facets = client.get("/api/reconciliations/facets", headers=admin_headers).json()
        assert "PAYMENTS" in facets["products"]


class TestConnectionEndpoints:
    def test_secrets_are_masked_in_responses(self, client, admin_headers):
        client.post(
            "/api/connections",
            json={
                "connection": {
                    "connectionId": "pg1",
                    "name": "PG",
                    "type": "jdbc",
                    "config": {
                        "databaseType": "postgresql",
                        "host": "db",
                        "database": "x",
                        "username": "u",
                        "password": "s3cret",
                    },
                }
            },
            headers=admin_headers,
        )
        payload = client.get("/api/connections/pg1", headers=admin_headers).json()
        assert payload["connection"]["config"]["password"] == "********"
        listing = client.get("/api/connections", headers=admin_headers).json()
        assert listing["items"][0]["config"]["password"] == "********"

    def test_connection_test_reports_failure_without_raising(self, client, admin_headers):
        client.post(
            "/api/connections",
            json={
                "connection": {
                    "connectionId": "sftp1",
                    "name": "SFTP",
                    "type": "sftp",
                    "config": {"host": "nonexistent.invalid", "username": "u", "password": "p"},
                }
            },
            headers=admin_headers,
        )
        result = client.post("/api/connections/sftp1/test", headers=admin_headers).json()
        assert result["success"] is False
        assert "failed" in result["message"].lower()

    def test_filesystem_connection_test_succeeds(self, client, admin_headers, tmp_path):
        client.post(
            "/api/connections",
            json={
                "connection": {
                    "connectionId": "files1",
                    "name": "Files",
                    "type": "filesystem",
                    "config": {"basePath": str(tmp_path)},
                }
            },
            headers=admin_headers,
        )
        result = client.post("/api/connections/files1/test", headers=admin_headers).json()
        assert result["success"] is True

    def test_query_preview_requires_a_jdbc_connection(self, client, admin_headers, tmp_path):
        client.post(
            "/api/connections",
            json={
                "connection": {
                    "connectionId": "files2",
                    "name": "Files",
                    "type": "filesystem",
                    "config": {"basePath": str(tmp_path)},
                }
            },
            headers=admin_headers,
        )
        response = client.post(
            "/api/connections/files2/preview", json={"query": "SELECT 1"}, headers=admin_headers
        )
        assert response.status_code == 400
        assert "only available for JDBC" in response.json()["detail"]

    def test_query_preview_substitutes_variables(self, client, admin_headers, tmp_path):
        import sqlite3

        database = tmp_path / "preview.db"
        connection = sqlite3.connect(database)
        connection.execute("CREATE TABLE ledger (id INTEGER, unit TEXT, business_date TEXT)")
        connection.executemany(
            "INSERT INTO ledger VALUES (?,?,?)",
            [(1, "CORP", "2026-09-10"), (2, "RETAIL", "2026-09-10")],
        )
        connection.commit()
        connection.close()

        client.post(
            "/api/connections",
            json={
                "connection": {
                    "connectionId": "sqlite1",
                    "name": "SQLite",
                    "type": "jdbc",
                    "config": {
                        "databaseType": "sqlite",
                        "jdbcUrl": f"jdbc:sqlite:{database}",
                        "database": str(database),
                    },
                }
            },
            headers=admin_headers,
        )
        preview = client.post(
            "/api/connections/sqlite1/preview",
            json={
                "query": "SELECT * FROM ${tbl} WHERE unit = '${unit}' AND business_date = '${business_date}'",
                "variables": {"tbl": "ledger", "unit": "CORP", "business_date": "2026-09-10"},
                "limit": 10,
            },
            headers=admin_headers,
        )
        assert preview.status_code == 200, preview.text
        payload = preview.json()
        assert payload["rowCount"] == 1
        assert "ledger" in payload["statement"]
        assert payload["columns"] == ["id", "unit", "business_date"]

    def test_query_preview_blocks_writes(self, client, admin_headers, tmp_path):
        import sqlite3

        database = tmp_path / "guard.db"
        sqlite3.connect(database).execute("CREATE TABLE t (a INT)")
        client.post(
            "/api/connections",
            json={
                "connection": {
                    "connectionId": "sqlite2",
                    "name": "SQLite",
                    "type": "jdbc",
                    "config": {"databaseType": "sqlite", "jdbcUrl": f"jdbc:sqlite:{database}"},
                }
            },
            headers=admin_headers,
        )
        response = client.post(
            "/api/connections/sqlite2/preview", json={"query": "DROP TABLE t"}, headers=admin_headers
        )
        assert response.status_code == 400


class TestExceptionWorkflow:
    def _seed(self, metrics_repository) -> list[int]:
        metrics_repository.record_exceptions(
            [
                {
                    "run_id": "run-x",
                    "recon_id": "payments_daily_recon",
                    "leg_id": "leg1",
                    "business_date": "2026-09-10",
                    "reconciliation_key": f"K{index}",
                    "exception_type": "MISMATCH" if index % 2 else "LEFT_ONLY",
                    "field": "amount" if index % 2 else None,
                    "expected_value": "100.00" if index % 2 else None,
                    "actual_value": "100.05" if index % 2 else None,
                    "context_columns": {"trade_date": "2026-09-10", "country": "UK"},
                }
                for index in range(6)
            ]
        )
        return [row["id"] for row in metrics_repository.list_exceptions(run_id="run-x")]

    def test_listing_exposes_context_columns(self, client, admin_headers, metrics_repository):
        self._seed(metrics_repository)
        payload = client.get(
            "/api/exceptions", params={"run_id": "run-x"}, headers=admin_headers
        ).json()
        assert payload["count"] == 6
        assert set(payload["contextColumns"]) == {"trade_date", "country"}
        assert payload["items"][0]["context_columns"]["country"] == "UK"

    def test_close_out_requires_a_comment(self, client, admin_headers, metrics_repository):
        ids = self._seed(metrics_repository)
        response = client.post(
            "/api/exceptions/status",
            json={"exceptionIds": ids[:1], "status": "CLOSED", "comment": "x"},
            headers=admin_headers,
        )
        assert response.status_code == 422  # min_length on the comment

    def test_close_out_records_the_officer_and_comment(self, client, admin_headers, metrics_repository):
        ids = self._seed(metrics_repository)
        response = client.post(
            "/api/exceptions/status",
            json={
                "exceptionIds": ids[:2],
                "status": "RESOLVED",
                "comment": "Timing difference confirmed with the settlements team (OPS-4412).",
                "resolutionCode": "TIMING",
            },
            headers=admin_headers,
        )
        assert response.status_code == 200
        assert response.json()["updated"] == 2

        detail = client.get(f"/api/exceptions/{ids[0]}", headers=admin_headers).json()
        assert detail["exception"]["status"] == "RESOLVED"
        assert detail["exception"]["resolved_by"] == "admin_user"
        assert detail["exception"]["resolution_code"] == "TIMING"
        assert detail["comments"][0]["author"] == "admin_user"
        assert "OPS-4412" in detail["comments"][0]["comment"]

    def test_open_only_filter_excludes_closed_exceptions(self, client, admin_headers, metrics_repository):
        ids = self._seed(metrics_repository)
        client.post(
            "/api/exceptions/status",
            json={"exceptionIds": ids[:3], "status": "CLOSED", "comment": "Known feed cut-off."},
            headers=admin_headers,
        )
        payload = client.get(
            "/api/exceptions", params={"run_id": "run-x", "status": "OPEN_ONLY"}, headers=admin_headers
        ).json()
        assert payload["count"] == 3

    def test_bulk_close_by_type(self, client, admin_headers, metrics_repository):
        self._seed(metrics_repository)
        response = client.post(
            "/api/exceptions/bulk-close",
            json={
                "comment": "All left-only breaks are the known T+1 cut-off.",
                "status": "WONT_FIX",
                "reconId": "payments_daily_recon",
                "exceptionType": "LEFT_ONLY",
            },
            headers=admin_headers,
        )
        assert response.status_code == 200
        assert response.json()["updated"] == 3

    def test_bulk_close_requires_a_scope(self, client, admin_headers, metrics_repository):
        self._seed(metrics_repository)
        response = client.post(
            "/api/exceptions/bulk-close",
            json={"comment": "everything", "status": "CLOSED"},
            headers=admin_headers,
        )
        assert response.status_code == 400

    def test_comment_without_status_change(self, client, admin_headers, metrics_repository):
        ids = self._seed(metrics_repository)
        client.post(
            f"/api/exceptions/{ids[0]}/comments",
            json={"comment": "Chased the source team."},
            headers=admin_headers,
        )
        comments = client.get(f"/api/exceptions/{ids[0]}/comments", headers=admin_headers).json()
        assert comments["items"][0]["comment"] == "Chased the source team."

    def test_reopening_is_tracked(self, client, admin_headers, metrics_repository):
        ids = self._seed(metrics_repository)
        client.post(
            "/api/exceptions/status",
            json={"exceptionIds": ids[:1], "status": "CLOSED", "comment": "Closed in error."},
            headers=admin_headers,
        )
        client.post(
            "/api/exceptions/status",
            json={"exceptionIds": ids[:1], "status": "REOPENED", "comment": "New evidence received."},
            headers=admin_headers,
        )
        detail = client.get(f"/api/exceptions/{ids[0]}", headers=admin_headers).json()
        assert detail["exception"]["status"] == "REOPENED"
        assert detail["exception"]["reopened_count"] == 1
        assert len(detail["comments"]) == 2

    def test_csv_export_includes_context_columns(self, client, admin_headers, metrics_repository):
        self._seed(metrics_repository)
        response = client.get(
            "/api/exceptions/export/csv", params={"run_id": "run-x"}, headers=admin_headers
        )
        assert response.status_code == 200
        header = response.text.splitlines()[0]
        assert "trade_date" in header and "country" in header
        assert "resolution_note" in header


class TestAdvisorEndpoints:
    def test_chat_without_a_run_still_answers(self, client, admin_headers):
        response = client.post(
            "/api/advisor/chat",
            json={"question": "Which columns should I match on?", "allowLlm": False},
            headers=admin_headers,
        )
        assert response.status_code == 200
        assert response.json()["intent"] == "key_selection"

    def test_analyse_returns_counts(self, client, admin_headers):
        payload = client.post("/api/advisor/analyse", json={}, headers=admin_headers).json()
        assert set(payload["counts"]) == {"CRITICAL", "WARNING", "SUGGESTION", "INFO"}

    def test_match_logic_suggestion_without_profiles_explains_why(self, client, admin_headers):
        payload = client.post(
            "/api/advisor/suggest-match-logic", json={"operator": "AND"}, headers=admin_headers
        ).json()
        assert payload["matchLogic"] is None
        assert "profiling" in payload["reason"]
