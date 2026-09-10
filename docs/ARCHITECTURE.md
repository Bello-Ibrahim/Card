# Architecture

ReconX separates four concerns that most reconciliation systems tangle
together: **what to reconcile** (configuration, in MongoDB), **when to
reconcile it** (the scheduler, on every node), **how to reconcile it** (the
Spark engine), and **what happened** (the metrics database, Kafka and the UI).

No reconciliation logic is compiled. A definition is data; the engine is a
generic interpreter of that data.

---

## 1. Components

| Component | Process | State it owns | Scales by |
|---|---|---|---|
| Streamlit UI | `reconx-ui` | Session only | Replicas behind sticky sessions |
| Control-plane API | `reconx-api` (uvicorn/FastAPI) | None | Replicas + HPA |
| Scheduler | `reconx-scheduler` | None (locks in MongoDB) | Replicas — safe by design |
| Spark job | driver + executors | None | Executors / dynamic allocation |
| MongoDB | external | Definitions, versions, runs, locks, users, audit, outbox | Replica set |
| Metrics DB (JDBC) | external | Runs, legs, field metrics, exceptions, audit, scheduler history | Vendor HA |
| Kafka | external | Lifecycle events | Partitions |
| SMTP | external | — | — |

Every control-plane process is **stateless**. Restarting or losing one loses
nothing: schedule state, locks and run records live in MongoDB, results and
exceptions in the metrics database.

### Why the UI never talks to MongoDB

The Streamlit app is a pure API client (`src/reconx/ui/api_client.py`). That
keeps one authorisation boundary (the API's RBAC dependencies), one audit
point, and one validation path. It also means the UI can be run outside the
cluster against a remote API without opening the databases.

---

## 2. Configuration data flow

```text
  Designer (Streamlit)
        │  definition JSON
        ▼
  POST /api/reconciliations           ── validate (structure + semantics + DAG)
        │
        ▼
  MongoDB  reconciliation_definitions   ← current pointer document
           reconciliation_versions      ← append-only, immutable
           audit_log                    ← who/what/when + field diff
        │
        ▼
  POST /api/reconciliations/{id}/activate   (permission: recon:activate)
        │
        ▼
  Scheduler reads only ACTIVE definitions
```

A save never mutates a stored version. `ReconciliationRepository.save()`
writes a new version document and moves the pointer; activation flips the
pointer's `status` to `ACTIVE` and stamps `activatedBy`/`activatedAt`.
Rollback re-publishes an old version *as a new version*, so the version
sequence is always monotonic and the audit trail never has to be interpreted
backwards.

---

## 3. Execution data flow

```text
scheduler tick (every node, every SCHEDULER_POLL_INTERVAL_SECONDS)
  │
  ├─ for each ACTIVE definition with a due schedule
  │    ├─ acquire MongoDB lock  recon:<reconId>          (TTL, node-stamped)
  │    ├─ evaluate data-availability conditions
  │    │     satisfied ──────────────► create run (unique idempotency key)
  │    │     not satisfied ──────────► run status WAITING_FOR_DATA
  │    └─ release lock
  │
  ├─ process WAITING_FOR_DATA runs (re-check, promote or SKIP on timeout)
  └─ reclaim orphaned runs from dead nodes  ──────────► FAILED (retryable)
        │
        ▼
   submit  ──►  in-process | spark-submit | Kubernetes spark-submit
        │
        ▼
   ReconciliationJob.run()
     1. validate definition
     2. start SparkSession (with the definition's Spark overrides)
     3. record run start in the metrics DB, publish RECONCILIATION_STARTED
     4. execute leg stages (topological order; legs in a stage run in sequence
        on one driver but each leg's work is fully distributed)
     5. write outputs, exceptions, metrics
     6. determine final status, publish COMPLETED/FAILED, send e-mail
```

### Leg execution

```text
for each source in leg:
    read (connector)  →  schema handling  →  data-quality checks
                      →  transformations  →  optional temp view / cache
left, right = the leg's two sides
    → pre-transformations
    → add __reconx_key (normalised, composite)
    → duplicate counting (window over the key)
    → prefix columns  l__* / r__*
    → FULL OUTER JOIN on __reconx_key
    → comparison columns (one boolean per FieldComparison)
    → matching logic evaluation (rules/groups, AND/OR/NOT)
    → classify: MATCHED / MISMATCH / LEFT_ONLY / RIGHT_ONLY / DUPLICATE_* 
    → annotate (matched rules, failed rules, failed fields)
    → single-pass metric aggregation
    → build exceptions (explode field detail, attach configured context columns)
    → aggregate comparisons (SUM/COUNT/AVG… with tolerance)
    → post-transformations, outputs, result temp view for downstream legs
```

The DAG is built from `dependsOn` plus implicit dependencies inferred from
`type: leg_output` sources. `reconx.config.validation` detects cycles and
missing references before anything runs, and groups independent legs into
stages.

---

## 4. The reconciliation algorithm

### Keys

A key is a normalised concatenation of one or more columns
(`src/reconx/spark/keys.py`). Normalisation is what makes real data
reconcile — `'  001 '` and `'1'` are the same account once trim and
leading-zero handling apply. Each component is written to a reserved
`__reconx_key_<n>` column and the parts are joined with the configured
separator into `__reconx_key`.

NULL is not the empty string. Unless `nullAsMissing`/`null_as` says otherwise,
a NULL component becomes the sentinel `<NULL>` so that two rows with missing
account numbers do not silently match each other.

### Join and classification

One `FULL OUTER JOIN` on `__reconx_key` produces every category in a single
shuffle:

| Category | Condition |
|---|---|
| `MATCHED` | Both sides present and the matching logic evaluates true |
| `MISMATCH` | Both sides present and the matching logic evaluates false |
| `LEFT_ONLY` | Right side absent |
| `RIGHT_ONLY` | Left side absent |
| `DUPLICATE_LEFT` / `DUPLICATE_RIGHT` / `DUPLICATE_BOTH` | Key occurs more than once on that side |
| `MISSING` | A required column was absent on a present row |

Duplicate counts come from a window aggregation taken *before* the join, so a
duplicated key that is also one-sided is counted correctly on both axes.

### Matching logic

A leg carries either a flat list of `comparisons` (implicitly ANDed) or a
`matchLogic` tree:

```text
MatchLogic(operator=OR)
 ├── MatchRule "value_rule"     (operator=AND)
 │     ├── amount   numeric_tolerance 0.01
 │     └── currency case_insensitive
 └── MatchRule "reference_rule" (operator=AND)
       └── ext_ref  trimmed
```

`evaluate_match_logic()` compiles the tree into one Spark `Column` expression —
there is no per-row Python. Groups nest arbitrarily and any node can be
negated, so the builder in the UI can express any boolean combination. Each
rule's outcome is also materialised as its own boolean column, which is what
makes per-rule pass/fail metrics (and the advisor's "this rule never fires"
finding) possible.

### Metrics in one pass

`_compute_metrics()` issues a single `agg()` with conditional counters, so
total, matched, mismatched, left-only, right-only, duplicate and per-field
counts all come from one scan of the joined DataFrame. The only data that
reaches the driver is that row of counters plus a bounded exception sample.

---

## 5. Storage model

### MongoDB (configuration and coordination)

| Collection | Purpose |
|---|---|
| `reconciliation_definitions` | Current pointer document per `reconId` |
| `reconciliation_versions` | Append-only immutable versions |
| `connections` | Connection definitions (secrets stored as references or Fernet ciphertext) |
| `runs` | Run lifecycle records; **unique index on the idempotency key** |
| `schedule_state` | Last fire, next fire, pause state, misfire tracking |
| `locks` | Distributed locks; **TTL index** so a dead node's lock expires |
| `users` | Users, bcrypt password hashes, roles |
| `audit_log` | Configuration and workflow audit trail |
| `event_outbox` | Kafka messages that could not be delivered |
| `column_profiles` | Source profiles used by the advisor |

### JDBC metrics database (results and reporting)

| Table | Contents |
|---|---|
| `reconciliation_definition` | Denormalised definition snapshot per version |
| `reconciliation_run` | One row per run: status, timings, totals |
| `reconciliation_leg_run` | Per-leg counts and durations |
| `reconciliation_metrics` | Named metrics (including per-rule pass/fail) |
| `reconciliation_source_metrics` | Rows read, bytes, DQ outcomes per source |
| `reconciliation_field_metrics` | Per-field compared/matched/mismatched counts |
| `reconciliation_exceptions` | First-class exception records + officer workflow columns + configured business columns |
| `reconciliation_exception_comment` | Immutable comment trail |
| `audit_log` | Mirror of configuration/workflow audit for warehouse reporting |
| `scheduler_execution` | Every scheduler firing decision |

DDL is generated from the SQLAlchemy models
(`src/reconx/metrics/models.py`) and shipped as
`src/reconx/metrics/migrations/V1__initial_schema.sql` for DBAs who apply
migrations themselves (`RESULT_AUTO_CREATE_SCHEMA=false`).

---

## 6. Distribution and safety

Three independent mechanisms stop the same logical run happening twice:

1. **Distributed lock.** Each scheduler tick takes `recon:<reconId>` in
   MongoDB with a TTL and the node id. `ensure_lock_index()` guarantees the
   unique index exists before the first acquire, so the lock is enforced by
   the database, not by convention.
2. **Idempotency key.** `recon_id + version + business dimensions`
   (`idempotencyDimensions`, default business date) has a **unique index** on
   the runs collection. Even if two nodes somehow passed the lock, the second
   insert fails.
3. **Concurrency guard.** `maxConcurrentRuns` per definition, and
   `SCHEDULER_MAX_CONCURRENT_RUNS` per node.

Node failure is handled by expiry, not by heartbeat consensus: the lock's TTL
releases it, and runs stuck in a non-terminal state past
`SCHEDULER_ORPHAN_RUN_TIMEOUT_MINUTES` are reclaimed and marked `FAILED` so
retry logic (not a duplicate schedule firing) decides what happens next.

---

## 7. Scaling and large data

* **Never `collect()`.** Business data stays in the cluster. The driver sees
  aggregate counters and a configurable exception sample only. The one bounded
  fallback (`_insert_exceptions_via_driver`, capped at 100 000 rows) exists
  for environments without a JDBC driver jar and logs loudly when used.
* **Adaptive query execution** and skew-join handling are on by default;
  `shufflePartitions` and `broadcastThresholdMb` are per-definition overrides.
* **Broadcast hints** — `broadcast: true` on a source marks the small side.
* **Column pruning and predicate pushdown** happen naturally because sources
  declare `select`/`filter` transformations before the join.
* **Exception writes are distributed** — Spark writes them to the metrics
  database over JDBC with `numPartitions`/`batchsize` tuning.
* **Inter-leg data passing uses temp views**, not object storage round trips.

Rough capacity guidance: a leg is bounded by one shuffle of both sides. With
`SPARK_EXECUTOR_INSTANCES x SPARK_EXECUTOR_CORES` slots and
`shufflePartitions` at roughly 2-3x that number, 100M x 100M row legs are a
tuning exercise, not an architectural one.

---

## 8. Observability

* **Structured JSON logs** (`structlog`) with `run_id`, `recon_id`, `leg_id`
  and a correlation id bound into contextvars, so every line of a request or
  a run is greppable by one id. A scrubber removes anything matching a
  sensitive key name, separator-insensitively (`password`, `secretKey`,
  `sasl_password`, …).
* **`/health`** — liveness, no dependencies touched.
* **`/ready`** — readiness; checks MongoDB and the metrics database.
* **`/metrics`** — Prometheus exposition: run counts by status, durations,
  exception counts, scheduler ticks, condition evaluations.
* **Kafka events** are the integration-grade signal: `started`,
  `stage.completed`, `completed`, `failed`, `exception`, `data-unavailable`,
  `alert` under the configured topic prefix.

---

## 9. Extension points

| To add… | Do this | Engine changes |
|---|---|---|
| A connector | Subclass `DataSourceConnector`, decorate `@register_connector` | None |
| A comparison rule | Add to `ComparisonRule` and `comparisons.py` | None |
| A condition type | Add to `ConditionType` and `scheduler/conditions.py` | None |
| A transformation | Add to `TransformType` and `spark/transforms.py` | None |
| A notification channel | Implement the notifier protocol in `notifications/` | None |
| A secret backend | Subclass `SecretProvider`, register on the resolver | None |

See [Extensibility notes in CONNECTORS.md](CONNECTORS.md#adding-a-connector).
