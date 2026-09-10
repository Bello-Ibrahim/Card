# ReconX — Enterprise Distributed Data Reconciliation Platform

A configuration-driven reconciliation platform for multi-node Linux clusters:
**Apache Spark** does the distributed processing, **MongoDB** holds versioned
configuration, a **JDBC database** holds metrics, results and exceptions,
**Kafka** carries lifecycle events, and a **Streamlit** UI (on a **FastAPI**
control plane) is where reconciliation officers design, schedule, run and
investigate reconciliations.

Nothing about a reconciliation is written in code. Sources, keys, matching
rules, tolerances, outputs, conditions, schedules and notifications are all
configuration — versioned, validated, auditable and rollback-able.

```text
                         ┌───────────────────────────┐
                         │       Streamlit UI        │
                         │  Designer · Runs · Recon  │
                         │  Advisor · Exceptions     │
                         └─────────────┬─────────────┘
                                       │ REST (JWT, RBAC)
                         ┌─────────────▼─────────────┐
                         │   FastAPI control plane   │
                         │  config · runs · reports  │
                         └───────┬─────────┬─────────┘
                   ┌─────────────┘         └─────────────┐
                   ▼                                     ▼
          ┌──────────────────┐                  ┌──────────────────┐
          │ MongoDB          │                  │ Kafka            │
          │ definitions      │                  │ lifecycle events │
          │ versions · runs  │                  │ exceptions       │
          │ locks · users    │                  │ alerts           │
          └────────┬─────────┘                  └──────────────────┘
                   │
                   ▼
          ┌────────────────────────┐
          │ Scheduler (N nodes)    │  distributed locks + idempotency keys
          │ conditions · triggers  │
          └────────────┬───────────┘
                       ▼
          ┌────────────────────────┐
          │ Apache Spark cluster   │  read → transform → reconcile → write
          └───────┬────────┬───────┘
                  ▼        ▼
      ┌──────────────┐  ┌─────────────────────────────────┐
      │ Data sources │  │ JDBC metrics database           │
      │ S3 · SFTP    │  │ runs · legs · field metrics     │
      │ StorageGRID  │  │ exceptions (+ officer workflow) │
      │ JDBC · Kafka │  │ audit · scheduler history       │
      │ Files · Excel│  └─────────────────────────────────┘
      └──────────────┘
```

---

## Quick start

### 1. Run the demo — no external services needed

```bash
make install          # creates .venv and installs everything
make jars             # downloads the JDBC drivers Spark needs
make demo             # runs a two-leg reconciliation on the bundled CSVs
```

The demo exercises composite normalised keys, two matching logics combined with
`OR`, duplicate detection, exception context columns, aggregate reconciliation
and a second leg that consumes the first leg's output.

### 2. Run the full stack

```bash
./scripts/fetch-jdbc-drivers.sh deployment/docker/jars
docker compose up -d
```

| Service | URL | Credentials |
|---|---|---|
| **Streamlit UI** | http://localhost:8501 | `admin` / `reconx-admin` |
| API + OpenAPI docs | http://localhost:8000/docs | bearer token from `/api/auth/login` |
| Kafka UI | http://localhost:8080 | — |
| MinIO console | http://localhost:9001 | `reconx` / `reconx-secret` |
| Mailpit (captured e-mail) | http://localhost:8025 | — |
| Spark master | http://localhost:8090 | — |

The stack runs **two scheduler replicas** on purpose: it demonstrates that
distributed locking prevents the same reconciliation from firing twice.

### 3. Import the example reconciliation

```bash
reconx-admin import examples/sample-reconciliation.yaml --activate
```

---

## What it does

### Configuration-driven, versioned, auditable

* Every save creates a **new immutable version**. An `ACTIVE` definition is
  never mutated in place — a new version stays `DRAFT` until someone with the
  `recon:activate` permission promotes it.
* **Rollback** republishes a historical version as a new one, so history stays
  linear and the audit trail never lies.
* Every change records **who, what, when, old version → new version** and a
  field-level diff, in MongoDB and in the JDBC `audit_log`.

### Multi-leg DAG execution

A reconciliation is a DAG of legs. A leg's result is registered as a Spark
temporary view that later legs consume directly — no round trip through
storage:

```text
Source A ─┐
          ├─ leg 1 ── result 1 ─┐
Source B ─┘                     │
                                ├─ leg 2 ── final result
Source C ───────────────────────┘
```

Cycles are detected at validation time, and legs that can run in parallel are
grouped into stages.

### Multiple matching logics, combined with AND / OR

The feature that makes real-world reconciliation tractable: a leg can carry
several *matching logics*, each grouping the comparisons that belong together,
and you choose how they combine.

```yaml
matchLogic:
  operator: OR              # AND = every rule must hold · OR = any rule is enough
  rules:
    - id: value_rule
      name: Amount and currency agree
      operator: AND         # how the comparisons inside this rule combine
      comparisons:
        - {left: amount, right: amount, rule: numeric_tolerance, tolerance: 0.01}
        - {left: currency, right: currency, rule: case_insensitive}
    - id: reference_rule
      name: External reference agrees
      comparisons:
        - {left: ext_ref, right: ext_ref, rule: trimmed}
```

Groups nest and can be negated, so arbitrary boolean expressions are
expressible from the UI. Every result row records which rules **matched** and
which **failed**, and per-rule pass/fail metrics are persisted — so you can see
whether a rule is doing any work.

Comparison rules: `exact`, `case_insensitive`, `trimmed`, `numeric_exact`,
`numeric_tolerance`, `percentage_tolerance`, `date_tolerance`, `date_only`,
`contains`, `always_match`, and `expression` for a custom Spark SQL predicate
(`ABS(left.amount - right.amount) <= 0.01`).

### Hand-written SQL in any dialect, with variables

Write the query in your database's own dialect — it is sent verbatim:

```yaml
- id: ledger
  type: jdbc
  connectionRef: ledger_mssql
  dialect: mssql
  query: |
    SELECT l.[CustomerId] AS customer_id, l.[Amount] AS amount
    FROM ${ledger_table} AS l WITH (NOLOCK)
    WHERE l.[BusinessDate] = '${business_date}'
      AND l.[BusinessUnit] = '${business_unit}'
```

`${variables}` are substituted in the query **and in table names**, so the same
definition serves every business unit and every date. Variables are declared on
the reconciliation (with defaults, types and choices), the UI prompts for them
on a manual run, and the built-ins (`${business_date}`,
`${business_date_compact}`, `${prev_business_date}`, …) are always available.

Only read-only `SELECT`/`WITH` statements are accepted — see
[Security](docs/SECURITY.md). The designer has a **Preview query** button that
runs the statement with the variables applied and shows the rows and columns
before you save.

### Exceptions as first-class records — with your business columns

Exceptions carry the key, the failing field, the rule that failed, and the
expected/actual values. They also carry **whatever business columns you
configure**, so an officer can work a break without opening the source data:

```yaml
exceptionColumns:
  - trade_date                                        # from either side
  - {alias: country, left: country, right: country}
  - {alias: ledger_amount, right: amount, source: right}
  - {alias: currency_pair, left: currency, right: currency, source: both}
```

Officers **close exceptions out from the UI** with a mandatory comment:

* statuses `OPEN → INVESTIGATING → RESOLVED / CLOSED / WONT_FIX / FALSE_POSITIVE`,
  and reopening is tracked
* an optional resolution code (`TIMING`, `FX_RATE`, `ROUNDING`, …)
* every transition writes an immutable comment record **and** an audit entry
* bulk close by filter for a known, feed-wide cause
* CSV export including the configured business columns

### The Recon Advisor

A chatbot that explains a run and recommends configuration. It is
**evidence-first**: every answer is derived from the run's metrics, per-field
comparison results, exception samples and column profiles that the platform
already stored. It works offline and never invents a number.

It can tell you:

* **why records did not match** — it distinguishes a key that does not line up
  (similar counts of one-sided records on both sides) from a feed that is
  genuinely incomplete
* **which columns to match on** — shared columns ranked by uniqueness, null
  density and *measured cross-source value overlap*, including whether
  normalising (trim / case / leading zeros) materially improves that overlap
* **which comparison rule fits** — it classifies the actual differences in the
  exception sample (case-only, whitespace, leading zeros, small rounding,
  date-format, timezone offset, truncation) and recommends the matching rule,
  with a tolerance derived from the observed spread
* **whether your matching logic is pulling its weight** — a rule that never
  matches, or always matches, is flagged
* duplicates, data quality, performance and scheduling advice

Findings come with the evidence behind them and a ready-to-paste configuration
fragment. Set `ADVISOR_LLM_ENABLED=true` with an `ANTHROPIC_API_KEY` to have
the same evidence phrased as a richer narrative; the deterministic findings are
still shown, and an unreachable model degrades silently.

### Data availability conditions

A schedule can say *run at 02:00, but only if the data is there*:

```yaml
conditions:
  operator: AND
  conditions:
    - {type: s3_file_exists, connectionRef: payments_s3,
       path: "s3://payments/in/${business_date}/*.parquet", minCount: 1}
    - {type: jdbc_query, connectionRef: ledger_mssql, comparator: gt, threshold: 0,
       query: "SELECT COUNT(*) FROM ledger WHERE BusinessDate = '${business_date}'"}
    - operator: OR
      conditions:
        - {type: sftp_file_exists, connectionRef: settlements_sftp, path: /out, filePattern: "*.csv"}
        - {type: previous_run_successful, lookbackHours: 48}
```

Unsatisfied conditions hold the run in `WAITING_FOR_DATA` and re-check until
`waitForDataMinutes` elapses, at which point it becomes `SKIPPED` — missing data
is an operational state, not a failure. The UI shows exactly which leaf is
holding the run back.

Condition types: `file_exists`, `s3_file_exists`, `sftp_file_exists`,
`file_count`, `file_size`, `jdbc_query`, `custom_sql`, `kafka_available`,
`previous_run_successful`, `reconciliation_succeeded` — nested with
`AND` / `OR` / `NOT`.

### Distributed by design

* The scheduler runs on **every node**. Each tick takes a MongoDB lock per
  reconciliation, and the runs collection has a **unique idempotency key**
  (`recon_id + version + business dimensions`) as the second line of defence.
  Two nodes can never start the same logical run.
* Control-plane services are **stateless** — every piece of state lives in
  MongoDB, the metrics database, Kafka or object storage.
* A crashed node's lock expires by TTL, and its abandoned runs are reclaimed
  and marked `FAILED` so they can be retried without creating duplicates.

### Built for large data

* Full outer join, single-pass metric aggregation, no `collect()` of business
  data. The only rows that reach the driver are counters and small samples.
* Adaptive query execution, skew-join handling, configurable shuffle
  partitions, broadcast hints, predicate pushdown and column pruning.
* Exceptions are written to the metrics database with a **distributed JDBC
  write**; if the driver jar is missing the platform falls back to a bounded,
  streamed driver-side insert and says so in the log.

---

## Connectors

| Type | Read | Write | Notes |
|---|---|---|---|
| **S3** | ✅ | ✅ | `s3a://` — AWS or any S3-compatible endpoint; IAM/IRSA or keys |
| **StorageGRID** | ✅ | ✅ | NetApp S3 API — explicit endpoint, path-style, tenant region |
| **SFTP** | ✅ | ✅ | Password or SSH key, known-hosts, gzip, file patterns |
| **JDBC** | ✅ | ✅ | PostgreSQL, MySQL/MariaDB, SQL Server, Oracle, DB2, SQLite, H2 |
| **Filesystem** | ✅ | ✅ | CSV, JSON, Parquet, ORC, Avro |
| **Kafka** | ✅ | ✅ | Batch by offset range; JSON/CSV/Avro payloads; SASL/SSL |
| **Excel** | ✅ | ✅ | XLSX/XLSM via openpyxl, with an explicit row cap |
| **Temp view / leg output** | ✅ | ✅ | How multi-leg DAGs pass data between legs |

Adding a connector means dropping a module in `src/reconx/connectors/` that
subclasses `DataSourceConnector` and is decorated with `@register_connector`.
The reconciliation engine is never modified.

---

## Repository layout

```text
src/reconx/
  common/        logging (JSON + correlation), retry, ids, templating, errors
  config/        pydantic models, MongoDB repositories, validation, settings
  security/      secrets, encryption, auth, RBAC, audit, SQL guard
  connectors/    s3, storagegrid, sftp, jdbc, kafka, filesystem, excel, temp_view
  spark/         session, schema, transforms, keys, data quality, profiler, job
    reconciliation/  the engine: comparisons, matching logic, classification
  advisor/       recommendation engine and the chatbot
  events/        Kafka publisher with outbox fallback
  notifications/ SMTP notifier (pluggable channels)
  metrics/       SQLAlchemy schema, repository, SQL migrations
  scheduler/     conditions, distributed locks, triggers, service, Spark runner
  api/           FastAPI control plane (routers, deps, schemas)
  ui/            Streamlit application and pages
deployment/      docker/ · kubernetes/ · helm/
docs/            architecture, deployment, operations, security, connectors...
examples/        sample reconciliation, connections, env, runnable demo
tests/           unit · integration · e2e
```

> The task specification suggested top-level `api/`, `spark/`, `ui/` … folders.
> They are the same modules, kept inside one installable `reconx` package so
> the services share one dependency graph and one import root. The mapping is
> one-to-one.

---

## Documentation

| Document | Contents |
|---|---|
| [Architecture](docs/ARCHITECTURE.md) | Components, data flow, the reconciliation algorithm, scaling |
| [Deployment](docs/DEPLOYMENT.md) | Kubernetes, Helm, Spark, MongoDB, Kafka, TLS, backup, upgrades |
| [Local development](docs/DEVELOPMENT.md) | Toolchain, running the services, the test suite |
| [Configuration reference](docs/CONFIGURATION.md) | Every field of a reconciliation definition |
| [Connectors](docs/CONNECTORS.md) | Per-connector configuration and operational notes |
| [Advisor](docs/ADVISOR.md) | What the advisor knows and how it reaches its conclusions |
| [Operations](docs/OPERATIONS.md) | Runbook, disaster recovery, troubleshooting |
| [Security](docs/SECURITY.md) | Secrets, authentication, RBAC, SQL safety, hardening checklist |
| [API](docs/API.md) | REST endpoints (OpenAPI is served at `/docs`) |
| [Known limitations](docs/LIMITATIONS.md) | What is not implemented, and why |

---

## Testing

```bash
make test              # the whole suite
make test-unit         # fast, no Spark
make test-spark        # engine tests on a local SparkSession
make test-integration  # repositories + API
make test-e2e          # the full pipeline
make check             # lint + typecheck + tests + config validation
```

**301 tests** covering key generation and normalisation, every comparison rule,
multi-rule matching logic, duplicate detection, aggregate reconciliation,
transformations, schema evolution, data quality, condition evaluation,
distributed locking, schedule arithmetic across timezones and DST, versioning
and rollback, secret handling, RBAC, the exception workflow, the advisor, and a
full end-to-end pipeline (CSV + JDBC → reconcile → metrics → events → e-mail →
advisor).

See [docs/TEST_RESULTS.md](docs/TEST_RESULTS.md) for what was verified in which
environment.

---

## Licence

Apache-2.0.
