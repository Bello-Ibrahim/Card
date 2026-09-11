"""Typed HTTP client the Streamlit UI uses to talk to the control plane.

The UI never touches MongoDB, Spark or the metrics database directly - every
action goes through the API, so authorisation and audit are enforced in exactly
one place.
"""

from __future__ import annotations

import os
from typing import Any

import httpx

from reconx.common.logging import get_logger

log = get_logger(__name__)

DEFAULT_TIMEOUT = float(os.getenv("RECONX_UI_API_TIMEOUT", "120"))


class ApiError(Exception):
    """An error returned by the control plane, carrying its detail payload."""

    def __init__(self, message: str, *, status_code: int | None = None, details: Any = None) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details

    def __str__(self) -> str:  # pragma: no cover - display helper
        return self.message


class ReconXClient:
    """Thin wrapper over the REST API with bearer-token authentication."""

    def __init__(self, base_url: str | None = None, token: str | None = None) -> None:
        self.base_url = (base_url or os.getenv("RECONX_API_URL", "http://localhost:8000")).rstrip("/")
        self.token = token

    # ------------------------------------------------------------ transport
    def _headers(self) -> dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any = None,
        timeout: float | None = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        try:
            response = httpx.request(
                method,
                url,
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json,
                headers=self._headers(),
                timeout=timeout or DEFAULT_TIMEOUT,
            )
        except httpx.RequestError as exc:
            raise ApiError(
                f"Cannot reach the ReconX API at {self.base_url} ({exc.__class__.__name__}). "
                "Check RECONX_API_URL and that the API service is running."
            ) from exc

        if response.status_code >= 400:
            payload: Any
            try:
                payload = response.json()
            except ValueError:
                payload = {"message": response.text[:500]}
            message = (
                payload.get("message")
                or payload.get("detail")
                or f"HTTP {response.status_code}"
            )
            if isinstance(message, list):  # FastAPI validation errors
                message = "; ".join(
                    f"{'.'.join(str(p) for p in item.get('loc', []))}: {item.get('msg')}" for item in message
                )
            raise ApiError(str(message), status_code=response.status_code, details=payload)
        if not response.content:
            return None
        return response.json()

    def get(self, path: str, **kwargs: Any) -> Any:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> Any:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> Any:
        return self.request("PUT", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> Any:
        return self.request("DELETE", path, **kwargs)

    # ----------------------------------------------------------------- auth
    def login(self, username: str, password: str) -> dict[str, Any]:
        payload = self.post("/api/auth/login", json={"username": username, "password": password})
        self.token = payload["accessToken"]
        return payload

    def me(self) -> dict[str, Any]:
        return self.get("/api/auth/me")

    def roles(self) -> dict[str, Any]:
        return self.get("/api/auth/roles")

    def users(self) -> list[dict[str, Any]]:
        return self.get("/api/auth/users").get("items", [])

    def create_user(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.post("/api/auth/users", json=payload)

    def update_user(self, username: str, payload: dict[str, Any]) -> dict[str, Any]:
        return self.put(f"/api/auth/users/{username}", json=payload)

    def delete_user(self, username: str) -> Any:
        return self.delete(f"/api/auth/users/{username}")

    # ------------------------------------------------------- reconciliations
    def list_reconciliations(self, **params: Any) -> dict[str, Any]:
        return self.get("/api/reconciliations", params=params)

    def facets(self) -> dict[str, Any]:
        return self.get("/api/reconciliations/facets")

    def get_reconciliation(self, recon_id: str, version: int | None = None) -> dict[str, Any]:
        return self.get(f"/api/reconciliations/{recon_id}", params={"version": version})

    def create_reconciliation(self, definition: dict[str, Any], *, activate: bool = False) -> dict[str, Any]:
        return self.post(
            "/api/reconciliations", json={"definition": definition, "activate": activate}
        )

    def update_reconciliation(
        self,
        recon_id: str,
        definition: dict[str, Any],
        *,
        comment: str | None = None,
        expected_version: int | None = None,
        activate: bool = False,
    ) -> dict[str, Any]:
        return self.put(
            f"/api/reconciliations/{recon_id}",
            json={
                "definition": definition,
                "comment": comment,
                "expectedVersion": expected_version,
                "activate": activate,
            },
        )

    def validate_definition(self, definition: dict[str, Any]) -> dict[str, Any]:
        return self.post("/api/reconciliations/validate", json={"definition": definition})

    def activate(self, recon_id: str, version: int | None = None) -> dict[str, Any]:
        return self.post(f"/api/reconciliations/{recon_id}/activate", params={"version": version})

    def disable(self, recon_id: str) -> dict[str, Any]:
        return self.post(f"/api/reconciliations/{recon_id}/disable")

    def enable(self, recon_id: str) -> dict[str, Any]:
        return self.post(f"/api/reconciliations/{recon_id}/enable")

    def archive(self, recon_id: str) -> dict[str, Any]:
        return self.post(f"/api/reconciliations/{recon_id}/archive")

    def clone(self, recon_id: str, new_id: str, new_name: str | None = None) -> dict[str, Any]:
        return self.post(
            f"/api/reconciliations/{recon_id}/clone",
            json={"newReconId": new_id, "newName": new_name},
        )

    def versions(self, recon_id: str) -> list[dict[str, Any]]:
        return self.get(f"/api/reconciliations/{recon_id}/versions").get("items", [])

    def rollback(self, recon_id: str, version: int, comment: str | None = None) -> dict[str, Any]:
        return self.post(
            f"/api/reconciliations/{recon_id}/rollback", json={"version": version, "comment": comment}
        )

    def run_now(self, recon_id: str, **payload: Any) -> dict[str, Any]:
        return self.post(f"/api/reconciliations/{recon_id}/run", json=payload)

    def advice(self, recon_id: str, run_id: str | None = None) -> dict[str, Any]:
        return self.get(f"/api/reconciliations/{recon_id}/advice", params={"run_id": run_id})

    # ----------------------------------------------------------- connections
    def list_connections(self, **params: Any) -> list[dict[str, Any]]:
        return self.get("/api/connections", params=params).get("items", [])

    def connection_types(self) -> dict[str, Any]:
        return self.get("/api/connections/types")

    def get_connection(self, connection_id: str) -> dict[str, Any]:
        return self.get(f"/api/connections/{connection_id}").get("connection", {})

    def create_connection(self, connection: dict[str, Any]) -> dict[str, Any]:
        return self.post("/api/connections", json={"connection": connection})

    def update_connection(self, connection_id: str, connection: dict[str, Any]) -> dict[str, Any]:
        return self.put(f"/api/connections/{connection_id}", json={"connection": connection})

    def delete_connection(self, connection_id: str) -> Any:
        return self.delete(f"/api/connections/{connection_id}")

    def test_connection(self, connection_id: str) -> dict[str, Any]:
        return self.post(f"/api/connections/{connection_id}/test")

    def test_unsaved_connection(self, connection: dict[str, Any]) -> dict[str, Any]:
        return self.post("/api/connections/test", json={"connection": connection})

    def preview_query(
        self,
        connection_id: str,
        *,
        query: str | None = None,
        table: str | None = None,
        limit: int = 100,
        variables: dict[str, Any] | None = None,
        dialect: str = "generic",
    ) -> dict[str, Any]:
        return self.post(
            f"/api/connections/{connection_id}/preview",
            json={
                "query": query,
                "table": table,
                "limit": limit,
                "variables": variables or {},
                "dialect": dialect,
            },
        )

    def list_tables(self, connection_id: str, schema: str | None = None) -> list[dict[str, Any]]:
        return self.get(f"/api/connections/{connection_id}/tables", params={"schema": schema}).get(
            "items", []
        )

    def list_files(self, connection_id: str, path: str, pattern: str | None = None) -> list[dict[str, Any]]:
        return self.get(
            f"/api/connections/{connection_id}/files", params={"path": path, "pattern": pattern}
        ).get("items", [])

    # ------------------------------------------------------------------ runs
    def list_runs(self, **params: Any) -> list[dict[str, Any]]:
        return self.get("/api/runs", params=params).get("items", [])

    def get_run(self, run_id: str) -> dict[str, Any]:
        return self.get(f"/api/runs/{run_id}")

    def cancel_run(self, run_id: str, reason: str | None = None) -> dict[str, Any]:
        return self.post(f"/api/runs/{run_id}/cancel", json={"reason": reason})

    def retry_run(self, run_id: str) -> dict[str, Any]:
        return self.post(f"/api/runs/{run_id}/retry")

    def run_logs(self, run_id: str, lines: int = 200) -> dict[str, Any]:
        return self.get(f"/api/runs/{run_id}/logs", params={"lines": lines})

    def run_conditions(self, run_id: str) -> dict[str, Any]:
        return self.get(f"/api/runs/{run_id}/conditions")

    def run_statistics(self, **params: Any) -> dict[str, Any]:
        return self.get("/api/runs/statistics", params=params)

    # ------------------------------------------------------------ schedules
    def list_schedules(self, **params: Any) -> list[dict[str, Any]]:
        return self.get("/api/schedules", params=params).get("items", [])

    def get_schedule(self, recon_id: str) -> dict[str, Any]:
        return self.get(f"/api/schedules/{recon_id}")

    def pause_schedule(self, recon_id: str) -> dict[str, Any]:
        return self.post(f"/api/schedules/{recon_id}/pause")

    def resume_schedule(self, recon_id: str) -> dict[str, Any]:
        return self.post(f"/api/schedules/{recon_id}/resume")

    def evaluate_conditions(self, recon_id: str, business_date: str | None = None) -> dict[str, Any]:
        return self.post(
            f"/api/schedules/{recon_id}/evaluate-conditions", params={"business_date": business_date}
        )

    def schedule_history(self, recon_id: str, limit: int = 50) -> list[dict[str, Any]]:
        return self.get(f"/api/schedules/{recon_id}/history", params={"limit": limit}).get("items", [])

    # ----------------------------------------------------------- exceptions
    def list_exceptions(self, **params: Any) -> dict[str, Any]:
        return self.get("/api/exceptions", params=params)

    def get_exception(self, exception_id: int) -> dict[str, Any]:
        return self.get(f"/api/exceptions/{exception_id}")

    def update_exception_status(
        self,
        exception_ids: list[int],
        *,
        status: str,
        comment: str,
        resolution_code: str | None = None,
        assigned_to: str | None = None,
    ) -> dict[str, Any]:
        return self.post(
            "/api/exceptions/status",
            json={
                "exceptionIds": exception_ids,
                "status": status,
                "comment": comment,
                "resolutionCode": resolution_code,
                "assignedTo": assigned_to,
            },
        )

    def bulk_close_exceptions(self, **payload: Any) -> dict[str, Any]:
        return self.post("/api/exceptions/bulk-close", json=payload)

    def add_exception_comment(self, exception_id: int, comment: str) -> dict[str, Any]:
        return self.post(f"/api/exceptions/{exception_id}/comments", json={"comment": comment})

    def exception_comments(self, exception_id: int) -> list[dict[str, Any]]:
        return self.get(f"/api/exceptions/{exception_id}/comments").get("items", [])

    def exception_summary(self, **params: Any) -> dict[str, Any]:
        return self.get("/api/exceptions/summary", params=params)

    def export_exceptions_url(self, **params: Any) -> str:
        query = "&".join(f"{k}={v}" for k, v in params.items() if v is not None)
        return f"{self.base_url}/api/exceptions/export/csv?{query}"

    # --------------------------------------------------------------- reports
    def dashboard(self, **params: Any) -> dict[str, Any]:
        return self.get("/api/reports/dashboard", params=params)

    def trend(self, **params: Any) -> list[dict[str, Any]]:
        return self.get("/api/reports/trend", params=params).get("items", [])

    def runs_report(self, **params: Any) -> list[dict[str, Any]]:
        return self.get("/api/reports/runs", params=params).get("items", [])

    def field_metrics(self, run_id: str) -> list[dict[str, Any]]:
        return self.get("/api/reports/field-metrics", params={"run_id": run_id}).get("items", [])

    # --------------------------------------------------------------- advisor
    def ask_advisor(
        self,
        question: str,
        *,
        recon_id: str | None = None,
        run_id: str | None = None,
        history: list[dict[str, str]] | None = None,
        allow_llm: bool = True,
    ) -> dict[str, Any]:
        return self.post(
            "/api/advisor/chat",
            json={
                "question": question,
                "reconId": recon_id,
                "runId": run_id,
                "history": history or [],
                "allowLlm": allow_llm,
            },
        )

    def analyse(self, *, recon_id: str | None = None, run_id: str | None = None) -> dict[str, Any]:
        return self.post("/api/advisor/analyse", json={"reconId": recon_id, "runId": run_id})

    def profiles(self, *, recon_id: str | None = None, run_id: str | None = None) -> list[dict[str, Any]]:
        return self.get("/api/advisor/profiles", params={"recon_id": recon_id, "run_id": run_id}).get(
            "items", []
        )

    def suggest_match_logic(
        self,
        *,
        recon_id: str | None = None,
        run_id: str | None = None,
        operator: str = "AND",
        key_columns: list[str] | None = None,
    ) -> dict[str, Any]:
        return self.post(
            "/api/advisor/suggest-match-logic",
            json={
                "reconId": recon_id,
                "runId": run_id,
                "operator": operator,
                "keyColumns": key_columns or [],
            },
        )

    # ---------------------------------------------------------------- system
    def health(self) -> dict[str, Any]:
        return self.get("/health")

    def ready(self) -> dict[str, Any]:
        try:
            return self.get("/ready")
        except ApiError as exc:
            if exc.status_code == 503 and isinstance(exc.details, dict):
                return exc.details
            raise

    def system_info(self) -> dict[str, Any]:
        return self.get("/api/system/info")

    def system_status(self) -> dict[str, Any]:
        return self.get("/api/system/status")

    def locks(self) -> list[dict[str, Any]]:
        return self.get("/api/system/locks").get("items", [])

    def release_lock(self, lock_id: str) -> Any:
        return self.delete(f"/api/system/locks/{lock_id}")

    def initialise(self) -> dict[str, Any]:
        return self.post("/api/system/initialise")

    def audit(self, **params: Any) -> list[dict[str, Any]]:
        return self.get("/api/system/audit", params=params).get("items", [])
