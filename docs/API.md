# REST API

The control plane is a FastAPI application. **OpenAPI is served live** at
`/docs` (Swagger UI), `/redoc` and `/openapi.json` — that is the
authoritative reference, generated from the same Pydantic models the platform
validates with. This page is the map.

Base URL: `http://<api-host>:8000`.

---

## Authentication

```bash
TOKEN=$(curl -s -X POST http://localhost:8000/api/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"reconx-admin"}' | jq -r .accessToken)

curl -H "Authorization: Bearer $TOKEN" http://localhost:8000/api/reconciliations
```

A token may also be sent as `X-API-Key`. Every response carries
`X-Correlation-Id`; send your own to thread a request through the logs.

Bodies and responses are **camelCase**. Errors are uniform:

```json
{"code": "VALIDATION_ERROR", "message": "…", "details": {"field": "legs[0].keys"}}
```

| Status | Meaning |
|---|---|
| `400` | Validation or configuration error |
| `401` | Missing or invalid token |
| `403` | Authenticated but lacking the permission |
| `404` | Not found |
| `409` | Conflict — version mismatch, duplicate idempotency key, lock held |
| `422` | Request body failed schema validation |
| `500` | Unhandled error (correlation id in the response) |

---

## Auth and users

| Method | Path | Permission |
|---|---|---|
| `POST` | `/api/auth/login` | — |
| `GET` | `/api/auth/me` | authenticated |
| `GET` | `/api/auth/roles` | authenticated |
| `GET` | `/api/auth/users` | `user:manage` |
| `POST` | `/api/auth/users` | `user:manage` |
| `PUT` | `/api/auth/users/{username}` | `user:manage` |
| `DELETE` | `/api/auth/users/{username}` | `user:manage` |

## Reconciliations

| Method | Path | Permission |
|---|---|---|
| `GET` | `/api/reconciliations` | `recon:view` |
| `GET` | `/api/reconciliations/facets` | `recon:view` |
| `POST` | `/api/reconciliations` | `recon:create` |
| `GET` | `/api/reconciliations/{reconId}` | `recon:view` |
| `PUT` | `/api/reconciliations/{reconId}` | `recon:edit` |
| `POST` | `/api/reconciliations/validate` | `recon:view` |
| `POST` | `/api/reconciliations/{reconId}/validate` | `recon:view` |
| `POST` | `/api/reconciliations/{reconId}/activate` | `recon:activate` |
| `POST` | `/api/reconciliations/{reconId}/disable` | `recon:disable` |
| `POST` | `/api/reconciliations/{reconId}/enable` | `recon:disable` |
| `POST` | `/api/reconciliations/{reconId}/archive` | `recon:delete` |
| `POST` | `/api/reconciliations/{reconId}/clone` | `recon:create` |
| `GET` | `/api/reconciliations/{reconId}/versions` | `recon:view` |
| `POST` | `/api/reconciliations/{reconId}/rollback` | `recon:edit` |
| `POST` | `/api/reconciliations/{reconId}/run` | `recon:execute` |
| `GET` | `/api/reconciliations/{reconId}/advice` | `recon:view` |
| `DELETE` | `/api/reconciliations/{reconId}` | `recon:delete` |

`PUT` accepts `expectedVersion` for optimistic concurrency — a mismatch
returns `409` instead of silently overwriting a colleague's edit.

```bash
# run now, for a past date, with variables
curl -X POST .../api/reconciliations/eod-cash/run -H "Authorization: Bearer $TOKEN" \
  -d '{"businessDate":"2026-09-01","parameters":{"business_unit":"EMEA"},"profileSources":true}'
```

## Connections

| Method | Path | Permission |
|---|---|---|
| `GET` | `/api/connections` | `connection:view` |
| `GET` | `/api/connections/types` | `connection:view` |
| `POST` | `/api/connections` | `connection:manage` |
| `GET` | `/api/connections/{connectionId}` | `connection:view` |
| `PUT` | `/api/connections/{connectionId}` | `connection:manage` |
| `DELETE` | `/api/connections/{connectionId}` | `connection:manage` |
| `POST` | `/api/connections/{connectionId}/test` | `connection:test` |
| `POST` | `/api/connections/test` | `connection:test` |
| `POST` | `/api/connections/{connectionId}/preview-query` | `connection:test` |
| `GET` | `/api/connections/{connectionId}/tables` | `connection:view` |
| `GET` | `/api/connections/{connectionId}/files` | `connection:view` |

Responses **never contain secrets** — secret fields come back masked.

```bash
# preview a hand-written query with variables applied
curl -X POST .../api/connections/ledger_mssql/preview-query -H "Authorization: Bearer $TOKEN" \
  -d '{"dialect":"mssql","limit":50,
       "variables":{"ledger_table":"dbo.LedgerEntries","business_date":"2026-09-01"},
       "query":"SELECT TOP 100 * FROM ${ledger_table} WHERE BusinessDate = '\''${business_date}'\''"}'
```

Only read-only statements are accepted; see [SECURITY.md](SECURITY.md#4-sql-safety).

## Runs

| Method | Path | Permission |
|---|---|---|
| `GET` | `/api/runs` | `run:view` |
| `GET` | `/api/runs/statistics` | `run:view` |
| `GET` | `/api/runs/{runId}` | `run:view` |
| `GET` | `/api/runs/{runId}/legs` | `run:view` |
| `GET` | `/api/runs/{runId}/conditions` | `run:view` |
| `GET` | `/api/runs/{runId}/logs` | `run:view` |
| `POST` | `/api/runs/{runId}/cancel` | `run:cancel` |
| `POST` | `/api/runs/{runId}/retry` | `recon:execute` |

`/logs` tails the driver log of a run **submitted by the node serving the
request**; in a multi-node deployment use your log aggregator for the general
case.

## Schedules

| Method | Path | Permission |
|---|---|---|
| `GET` | `/api/schedules` | `schedule:view` |
| `GET` | `/api/schedules/{reconId}` | `schedule:view` |
| `POST` | `/api/schedules/{reconId}/pause` | `schedule:manage` |
| `POST` | `/api/schedules/{reconId}/resume` | `schedule:manage` |
| `POST` | `/api/schedules/{reconId}/evaluate-conditions` | `schedule:view` |
| `GET` | `/api/schedules/{reconId}/history` | `schedule:view` |
| `DELETE` | `/api/schedules/{reconId}` | `schedule:manage` |

`evaluate-conditions` runs the availability tree **now** and returns a
per-leaf result — the fastest way to answer "why is this waiting?".

## Exceptions

| Method | Path | Permission |
|---|---|---|
| `GET` | `/api/exceptions` | `exception:view` |
| `GET` | `/api/exceptions/summary` | `exception:view` |
| `GET` | `/api/exceptions/{exceptionId}` | `exception:view` |
| `POST` | `/api/exceptions/status` | `exception:view` |
| `POST` | `/api/exceptions/bulk-close` | `exception:view` |
| `POST` | `/api/exceptions/{exceptionId}/comments` | `exception:view` |
| `GET` | `/api/exceptions/{exceptionId}/comments` | `exception:view` |
| `GET` | `/api/exceptions/export/csv` | `exception:view` |

```bash
# close out with a mandatory officer comment
curl -X POST .../api/exceptions/status -H "Authorization: Bearer $TOKEN" -d '{
  "exceptionIds": [1201, 1202, 1203],
  "status": "RESOLVED",
  "resolutionCode": "TIMING",
  "comment": "Settlement leg booked T+1; confirmed against SWIFT MT940 for 2026-09-01."
}'
```

`comment` is required (min 3 characters) on every status change. Note that `exception:view` gates the whole exception router,
close-out included: exception triage is the reconciliation officer's job, so
every role that can see a break can work it, and the audit trail (not a
permission) records who did. Statuses:
`OPEN`, `INVESTIGATING`, `REOPENED`, `RESOLVED`, `CLOSED`, `WONT_FIX`,
`FALSE_POSITIVE`. Reopening is counted, and every transition writes an
immutable comment row plus an audit entry.

`bulk-close` takes a filter (`runId`, `reconId`, `legId`, `exceptionType`,
`businessDate`, `field`) plus the same mandatory comment, with a `limit`.

The CSV export includes the configured exception context columns.

## Reports

| Method | Path | Permission |
|---|---|---|
| `GET` | `/api/reports/dashboard` | `report:view` |
| `GET` | `/api/reports/trend` | `report:view` |
| `GET` | `/api/reports/runs` | `report:view` |
| `GET` | `/api/reports/field-metrics` | `report:view` |

## Advisor

| Method | Path | Permission |
|---|---|---|
| `POST` | `/api/advisor/chat` | `run:view` |
| `POST` | `/api/advisor/analyse` | `run:view` |
| `GET` | `/api/advisor/profiles` | `run:view` |
| `POST` | `/api/advisor/suggest-match-logic` | `recon:view` |

## System

| Method | Path | Permission |
|---|---|---|
| `GET` | `/health` | — (liveness) |
| `GET` | `/ready` | — (readiness; checks MongoDB and the metrics DB) |
| `GET` | `/metrics` | — (Prometheus) |
| `GET` | `/api/system/info` | `system:manage` |
| `GET` | `/api/system/status` | `run:view` |
| `GET` | `/api/system/locks` | `system:manage` |
| `DELETE` | `/api/system/locks/{lockId}` | `system:manage` |
| `POST` | `/api/system/initialise` | `system:manage` |
| `GET` | `/api/system/audit` | `audit:view` |

`/health`, `/ready` and `/metrics` are unauthenticated so probes and scrapers
work without credentials; restrict them at the network layer if that matters
to you. They expose no configuration values.

---

## Generating a client

```bash
curl -s http://localhost:8000/openapi.json > openapi.json
openapi-generator-cli generate -i openapi.json -g python -o ./client
```

The schema is generated from the runtime models, so a client generated this
way is always in step with the deployed version.
