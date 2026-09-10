# Known limitations

What the platform does not do, what is thinner than it looks, and what was not
exercised in the environment this was built in. Nothing here is a surprise
waiting for you in production if you read it first.

For what *was* verified and how, see [TEST_RESULTS.md](TEST_RESULTS.md).

---

## 1. Configured but not implemented

| Field | Status |
|---|---|
| `retention.archiveTo` | Accepted and stored, but **archiving is not performed**. `reconx-admin maintenance --purge` deletes according to `runsDays` and `exceptionsDays`; it does not write the rows to the configured output first. Archive outside the platform if you need it. |
| `retention.resultsDays`, `retention.eventsDays` | Accepted and stored, not enforced. Written results live in your object store / warehouse under their own lifecycle rules; event retention is Kafka's. |
| `RECONX_SECURITY_SECRETS_BACKEND` | Reported by `/api/system/info` but does not gate resolution. Which backend is used is decided by the *scheme* on each reference (`env:`, `file:`, `k8s:`, `enc:`, `vault:`). Setting it documents intent; it does not enforce it. |

---

## 2. Deliberately out of scope

* **Streaming reconciliation.** A reconciliation is a bounded computation over
  two datasets. The Kafka connector reads an *offset range*, not a continuous
  stream. Continuous reconciliation would need a different consistency model
  (windowing, late arrival, retraction) and is not what this platform is.
* **Column-level lineage.** The platform records which sources and which
  transformations produced a result, not a column-by-column lineage graph.
* **Machine-learned or fuzzy matching.** Matching is deterministic and
  explainable, by design: an officer must be able to say exactly why two rows
  matched. The advisor recommends deterministic rules; it does not introduce
  probabilistic matching.
* **Multi-tenancy isolation.** `environment`, `product` and `customer` are
  organisational metadata and filters, not a security boundary. One
  deployment is one trust domain; separate tenants get separate deployments.
* **Workflow beyond exception close-out.** There is status, assignment,
  comments, resolution codes and an audit trail — not a case-management
  system with SLAs, escalation chains or approval routing. The Kafka
  `exception` event is the integration point for a real workflow tool.

---

## 3. Thin or single-implementation areas

| Area | What ships | What it means |
|---|---|---|
| **Authentication backends** | `MongoUserStore` only | LDAP/OIDC/SAML is a clean extension point (`AuthenticationBackend` has one method, and every call site depends on `Principal`), but no such backend is written. You would write one. |
| **Vault provider** | HTTP KV v2, token auth | `VAULT_ADDR` + `VAULT_TOKEN` only. No AppRole, Kubernetes auth, or lease renewal. Inert unless both variables are set. Other managers (AWS/GCP/Azure) are a `SecretProvider` subclass away, not shipped. |
| **`/api/runs/{runId}/logs`** | Node-local | Tails the driver log of a run submitted by *the node serving the request*. In a multi-node deployment use your log aggregator; the `run_id` is in every log line. |
| **Excel** | Driver-side, row-capped | Read with `openpyxl` on the driver, so it is single-threaded and bounded by `maxRows`. Convert large workbooks to CSV/Parquet upstream. |
| **Streamlit horizontal scaling** | Sticky sessions required | Streamlit holds session state in the process. The chart sets cookie affinity on the ingress; without it a second replica breaks the UI, not the platform. |
| **Reporting exports** | CSV | Runs and exceptions export as CSV. No PDF or XLSX generation; the metrics tables are the interface for your BI tool. |
| **Prometheus metrics** | Gauges, computed per scrape | `/metrics` counts from MongoDB on each scrape. It is honest and cheap at normal scrape intervals, but they are gauges (`reconx_runs{status=…}` over 7 days), not monotonic counters — write alerts accordingly. Exception-volume alerting belongs in SQL against the metrics database. |
| **`spark-submit` / `kubernetes` submit modes** | Implemented, not exercised here | `inprocess` is what the tests and the demo use. The other two build and invoke a real `spark-submit`; see §5. |

---

## 4. Operational sharp edges

* **The encryption key is not recoverable.** Lose
  `RECONX_SECURITY_ENCRYPTION_KEY` and every `enc:` connection secret must be
  re-entered. Back it up.
* **The staging directory must be shared.** SFTP and Excel sources stage
  files that executors then read. A `ReadWriteOnce` volume will work on a
  single node and fail the moment executors land elsewhere.
* **JDBC driver jars are not vendored.** Licences differ. Without the jar,
  exception persistence falls back to a bounded (100 000 row) driver-side
  insert and logs that it did — degraded, not silent, but fix the classpath.
  Oracle's `ojdbc` must be fetched by hand.
* **MongoDB must be a replica set.** Version-and-pointer writes use
  transactions. A standalone `mongod` will fail those writes.
* **Schedules with `catchUp: false` (the default) do not back-fill.** A
  paused or missed window is not silently made up; re-run explicitly.
* **`SCHEDULER_LOCK_TTL_SECONDS` must exceed a tick's duration.** If a tick
  takes longer than the TTL, another node can pick up the same reconciliation
  — the unique idempotency key still prevents a duplicate run, but you will
  see rejected inserts in the log rather than clean scheduling.

---

## 5. What was not verified in this build environment

The platform was developed and tested in a sandbox with restricted egress.
This is an honest account of the boundary:

**Verified against real services**

* **PostgreSQL 16** — installed and used for real, including distributed
  Spark JDBC writes of exceptions with configured context columns, the full
  metrics schema and the officer close-out workflow.
* **Apache Spark 3.5.3** — real `SparkSession` in `local[*]`; the engine,
  transformations, data quality, profiling and the whole reconciliation
  algorithm run on it in the test suite.
* **SMTP** — a real in-process `aiosmtpd` server receives the notification
  e-mail in the end-to-end test.
* **Kubernetes manifests** — all 23 documents validated against the real
  Kubernetes OpenAPI models.

**Substituted**

* **MongoDB** — `mongomock`. Repository semantics (versioning, rollback,
  unique idempotency index, lock TTL) are tested against it. Index *creation*
  is asserted; TTL *expiry* is enforced by a real `mongod`, not by mongomock,
  so lock expiry timing should be confirmed on your cluster.
* **Kafka** — the publisher, envelopes, topic routing, failure modes and the
  MongoDB outbox are unit-tested with a stub producer. No broker was
  reachable; delivery against a real broker is exercised by the compose stack.
* **S3 / StorageGRID / SFTP** — configuration, URL and option construction,
  and listing logic are unit-tested. No object store or SFTP server was
  reachable from the build environment; the compose stack (MinIO + an SFTP
  container) is what exercises them.
* **Helm** — `get.helm.sh` was unreachable, so `helm lint`/`helm template`
  could not run. `scripts/validate_helm_chart.py` was written to statically
  check the chart (templates parse, referenced values exist, required keys
  present) and passes. Run `make helm-lint` where you have the binary before
  installing.
* **Spark cluster modes** — `spark-submit` and Spark-on-Kubernetes build and
  invoke a real `spark-submit` with the conf shown in the logs, but no
  standalone or Kubernetes Spark cluster was available to run against.
  Validate on a staging cluster before production.

**Not attempted**

* Load and scale testing at production volumes. The design decisions that
  matter for scale (single-pass aggregation, no driver-side collection,
  distributed exception writes, AQE/skew handling) are in place and the
  reasoning is in [ARCHITECTURE.md](ARCHITECTURE.md#7-scaling-and-large-data),
  but no benchmark was run — do not treat any throughput number as measured,
  because none is.
* A penetration test. The SQL guard, secret handling and RBAC are tested for
  the cases they were designed against; that is not the same as an adversarial
  review.

---

## 6. Upgrade and compatibility notes

* Definition documents are forward-compatible: every field added since v1 has
  a default, so an older stored definition validates against a newer model.
  There is no down-conversion — a definition saved by a newer version may use
  fields an older deployment does not understand.
* The metrics schema has one migration (`V1__initial_schema.sql`). There is no
  migration *runner*: apply DDL with your own tooling (Flyway, Liquibase,
  psql). `RESULT_AUTO_CREATE_SCHEMA=true` is a development convenience.
* Kafka event envelopes carry `schemaVersion` (currently `1.0`). Consumers
  should ignore unknown fields rather than pin to an exact shape.
