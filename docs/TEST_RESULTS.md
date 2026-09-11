# Test results

What was run, what it proved, and — just as importantly — what it did not
cover. Read alongside [LIMITATIONS.md](LIMITATIONS.md).

---

## 1. Summary

```
$ pytest tests -q
301 passed
```

| | |
|---|---|
| Tests | **301 passed, 0 failed, 0 skipped** (exit code 0) |
| Wall time | ~6.5 minutes on one container (Spark session startup dominates) |
| Lint | `ruff check src tests` — **All checks passed** |
| Driver-materialisation guard | `scripts/check_no_unbounded_collect.sh` — pass |
| Definition validation | `examples/sample-reconciliation.yaml`, `examples/local-demo.yaml` — valid |
| Helm chart | `scripts/validate_helm_chart.py` — pass |
| Kubernetes manifests | 23/23 documents validated against the Kubernetes OpenAPI models |

### Environment

| | |
|---|---|
| Python | 3.11.15 |
| PySpark | 3.5.3 (real `SparkSession`, `local[*]`) |
| PostgreSQL | 16.13 |
| Platform | Linux x86_64 |

---

## 2. Coverage by area

| Test module | Tests | What it establishes |
|---|--:|---|
| `tests/unit/test_common.py` | 35 | JSON logging with correlation ids, secret scrubbing (separator-insensitive), retry with exponential backoff and jitter, id generation, `${variable}` templating including defaults and strict mode, business-date and timezone/DST arithmetic |
| `tests/unit/test_config_models.py` | 20 | Every configuration model: camelCase aliases both directions, validators, shorthand forms (`exceptionColumns` as a bare string), the YAML 1.1 `on: → True` case, `MatchLogic.describe()` |
| `tests/unit/test_validation.py` | 39 | Cross-reference checks (connections, sources, legs), DAG cycle detection and stage grouping, key/comparison column presence, schedule sanity, and the SQL guard: read-only enforcement, dangerous-function deny-list, qualified identifier forms |
| `tests/unit/test_reconciliation_engine.py` | 35 | Composite normalised keys and NULL sentinel semantics; **all 11 comparison rules** including numeric/percentage/date tolerance and custom expressions; multi-rule matching logic with AND/OR, nesting and negation; per-rule pass/fail metrics; every match category; duplicate detection (including a duplicated key that is also one-sided); aggregate reconciliation; exception building with configured context columns |
| `tests/unit/test_transforms_and_dq.py` | 29 | All transformation types, schema modes (`infer`/`explicit`/`validate`/`evolve`), and every data-quality check with `STOP` vs `CONTINUE_WITH_WARNING` |
| `tests/unit/test_scheduler.py` | 36 | Condition evaluation with AND/OR/NOT nesting and per-leaf reporting; distributed lock acquire/expire/contend; schedule arithmetic across timezones and DST transitions; idempotency-key construction; orphan-run reclamation |
| `tests/unit/test_advisor.py` | 41 | Difference classification (all ten classes), tolerance derivation, key ranking from profiles including normalisation gain, match-logic suggestion, dead/always-true rule detection, intent routing, and that the advisor degrades cleanly when evidence is missing |
| `tests/integration/test_repositories.py` | 26 | Append-only versioning, activation, rollback as a new version, optimistic concurrency, unique idempotency index, lock TTL index creation, user store and bcrypt hashing, the metrics repository including the exception officer workflow |
| `tests/integration/test_api.py` | 38 | Every router, RBAC enforcement per permission, secret masking in responses, error mapping, query preview, and the exception close-out/bulk-close/comment endpoints |
| `tests/e2e/test_end_to_end.py` | 2 | The whole pipeline: CSV + JDBC sources → Spark reconciliation → metrics and exceptions persisted → Kafka events captured → e-mail delivered to a real SMTP server → advisor findings derived from the stored run |
| **Total** | **301** | |

66 of these (Spark engine, transforms/DQ, e2e) are marked `spark` and run on a
real `SparkSession`.

---

## 3. Verified against real services

### Apache Spark 3.5.3

Not mocked. The engine tests, transformation tests, data-quality tests,
profiler tests and both end-to-end tests execute on a real `SparkSession` in
`local[*]`, with the JDBC driver jars on the classpath. The reconciliation
algorithm — key construction, the full outer join, comparison columns,
matching-logic evaluation, classification, single-pass aggregation and
exception construction — is exercised as it runs in production, differing only
in cluster topology.

### PostgreSQL 16.13

The integration and end-to-end suites were re-run against a real PostgreSQL
instance:

```bash
export RECONX_TEST_POSTGRES_URL="postgresql+psycopg://reconx:reconx@localhost:5432/reconx_results"
pytest tests/integration tests/e2e -q      # 66 passed
```

All ten metrics tables were created and written by the platform:

```
audit_log                          reconciliation_leg_run
reconciliation_definition          reconciliation_metrics
reconciliation_exception_comment   reconciliation_run
reconciliation_exceptions          reconciliation_source_metrics
reconciliation_field_metrics       scheduler_execution
```

A persisted exception, read back from PostgreSQL after the run, showing the
**distributed Spark JDBC write**, the **configured context columns** and the
**officer close-out**:

```
run_id          | e2e-run-2
recon_id        | payments_e2e_recon
leg_id          | transaction_leg
exception_type  | MISMATCH
field           | currency
expected_value  | GBP
actual_value    | EUR
context_columns | {"trade_date": "2026-09-10", "country": "UK"}
status          | RESOLVED
comment_count   | 1
```

That single row is the evidence for four separate requirements at once:
exceptions are first-class records, they carry the business columns configured
on the leg, they are written over JDBC by Spark, and an officer closed one out
with a comment that is counted and retained.

The default test run (no `RECONX_TEST_POSTGRES_URL`) uses SQLite, which is why
the schema is written with `BigInteger().with_variant(Integer, "sqlite")` and
`server_default=func.now()` — both suites pass on both engines.

### SMTP

The end-to-end test starts a real in-process `aiosmtpd` server on a free port,
runs a reconciliation configured to notify on completion, and asserts on the
delivered message: recipients, subject prefix, the metrics block and the
exception sample. Mail is genuinely sent and received, not stubbed.

### Kubernetes manifests

All 23 documents in `deployment/kubernetes/` were validated against the real
Kubernetes OpenAPI models — not a YAML syntax check: field names, types and
required properties for every Deployment, Service, HPA, PDB, NetworkPolicy,
CronJob, RBAC and Ingress object.

---

## 4. Substituted, and why

| Dependency | Substitute | What is still proven | What is not |
|---|---|---|---|
| **MongoDB** | `mongomock` | Repository semantics: versioning, rollback, optimistic concurrency, unique idempotency index, lock acquire/release, user store | TTL-driven lock *expiry* timing, transaction behaviour, and replica-set failover — these need a real `mongod` |
| **Kafka** | Stub producer | Envelope shape and `schemaVersion`, topic routing per event type, `WARN_ONLY`/`RETRY`/`FAIL_RUN` handling, MongoDB outbox write and replay, payload scrubbing | Broker delivery semantics, partitioning, SASL/SSL handshakes |
| **S3 / StorageGRID** | Unit tests over config | Hadoop `s3a` property construction, endpoint/path-style/region handling, credential resolution, listing logic | Actual reads/writes against an object store |
| **SFTP** | Unit tests over config | Host-key policy, key vs password selection, staging path handling, glob matching | A real SSH transfer |
| **Helm** | `scripts/validate_helm_chart.py` | Templates parse, every referenced value exists, required keys present | `helm lint` / `helm template` / `helm install` |
| **Spark cluster modes** | `inprocess` | The `spark-submit` command and conf are constructed and logged | Execution on a standalone or Kubernetes Spark cluster |

The substitutions are a property of this build environment's egress policy,
not of the code: `docker compose up` brings up real MongoDB, Kafka, MinIO and
an SFTP server, and the same suites run against them.

---

## 5. The demo as an end-to-end check

`make demo` runs a two-leg reconciliation over the bundled CSVs with no
external services. It is the fastest way to confirm an installation works:

```
matched=4  mismatch=1  leftOnly=3  rightOnly=1  dup=2
```

It exercises composite normalised keys, two matching logics combined with
`OR`, duplicate detection, exception context columns, aggregate
reconciliation, and a second leg consuming the first leg's output through a
temp view.

---

## 6. Not measured

* **No performance benchmark was run.** No throughput, latency or scale number
  in this repository is measured, and none is claimed. The design choices that
  matter at scale are documented and reviewable
  ([ARCHITECTURE.md](ARCHITECTURE.md#7-scaling-and-large-data)); validating
  them at your volumes is a staging-cluster exercise.
* **No security assessment.** The SQL guard, secret handling and RBAC have
  tests for the cases they were designed against. That is not an adversarial
  review.
* **No coverage percentage is quoted.** `make coverage` produces one; a number
  quoted here without the run behind it would be decoration.

---

## 7. Reproducing

```bash
make install
make jars
make test                 # 301 tests
make lint typecheck
make validate-config

# against real PostgreSQL
export RECONX_TEST_POSTGRES_URL="postgresql+psycopg://user:pass@host:5432/db"
make test-integration test-e2e

# against real MongoDB, Kafka, MinIO and SFTP
docker compose up -d
```
