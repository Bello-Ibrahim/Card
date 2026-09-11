# Local development

---

## 1. Toolchain

| Requirement | Version |
|---|---|
| Python | 3.11 |
| Java (for Spark) | 11 or 17 |
| Docker + Compose | for the full stack |
| Make | |

```bash
make install       # creates .venv and installs the project with all extras + dev tools
make jars          # downloads the JDBC drivers into .jars/ for local Spark
make help          # every target, with descriptions
```

`PYTHONPATH=src` is exported by the Makefile; the project is also installed in
editable mode, so `import reconx` works either way.

---

## 2. The demo — no external services

```bash
make demo
```

Runs a two-leg reconciliation over the CSVs in `examples/data/`, with the
metrics database on SQLite, Kafka disabled and Spark in `local[*]`. It
exercises composite normalised keys, two matching logics combined with `OR`,
duplicate detection, exception context columns, aggregate reconciliation, and
a second leg that consumes the first leg's output.

Expected result: `matched=4 mismatch=1 leftOnly=3 rightOnly=1 dup=2`.

Outputs land in `.data/demo-output/`; the metrics database is
`.data/demo-metrics.db` — open it with `sqlite3` and look at
`reconciliation_exceptions` to see the configured context columns.

---

## 3. Running the services

Against the compose stack (recommended — real MongoDB, PostgreSQL, Kafka,
MinIO, SFTP and a mail catcher):

```bash
./scripts/fetch-jdbc-drivers.sh deployment/docker/jars
docker compose up -d mongodb mongodb-init postgres kafka minio minio-init sftp mailpit
cp .env.example .env          # the defaults already point at the compose services
make run-api                  # http://localhost:8000/docs
make run-ui                   # http://localhost:8501
make run-scheduler
```

Or run everything in containers with `make docker-up` (see
[DEPLOYMENT.md](DEPLOYMENT.md#2-local-stack-docker-compose)).

Sign in as `admin` / `reconx-admin`.

---

## 4. Tests

```bash
make test              # everything
make test-unit         # fast: no Spark, no external services
make test-spark        # engine tests on a local SparkSession
make test-integration  # repositories (mongomock) + API (TestClient)
make test-e2e          # the full pipeline
make coverage          # + HTML report in htmlcov/
```

| Directory | What it covers |
|---|---|
| `tests/unit/test_common.py` | Logging and scrubbing, retry/backoff, ids, templating, time/DST |
| `tests/unit/test_config_models.py` | Every model, aliases, validators, the YAML `on:` case |
| `tests/unit/test_validation.py` | Cross-reference checks, DAG cycles, SQL guard |
| `tests/unit/test_reconciliation_engine.py` | Keys, all comparison rules, matching logic, duplicates, aggregates, exception building |
| `tests/unit/test_transforms_and_dq.py` | Transformations, schema modes, data-quality checks |
| `tests/unit/test_scheduler.py` | Conditions, locks, schedule arithmetic across timezones and DST, idempotency |
| `tests/unit/test_advisor.py` | Difference classification, recommendations, chat routing |
| `tests/integration/test_repositories.py` | Versioning, rollback, runs, locks, users, metrics repository |
| `tests/integration/test_api.py` | Routes, RBAC, secret masking, exception workflow |
| `tests/e2e/test_end_to_end.py` | CSV + JDBC → reconcile → metrics → events → e-mail → advisor |

Spark tests are marked `spark` and share one session-scoped `SparkSession`
(`tests/conftest.py`), with the JDBC jars from `.jars/` on the classpath.

MongoDB is faked with `mongomock`. The metrics database defaults to SQLite;
to run the same tests against **real PostgreSQL**:

```bash
export RECONX_TEST_POSTGRES_URL="postgresql+psycopg://reconx:reconx@localhost:5432/reconx_test"
make test-integration test-e2e
```

Kafka, SMTP, S3 and SFTP are covered by unit tests plus an in-process SMTP
server (`aiosmtpd`) in the e2e test; the compose stack is what exercises the
real brokers and servers.

---

## 5. Code quality

```bash
make lint          # ruff
make format        # ruff format + fix
make typecheck     # mypy over src/reconx
make validate-config
make check         # lint + typecheck + test + validate-config — what CI runs
```

```bash
make hooks         # .venv/bin/pre-commit install
.venv/bin/pre-commit run --all-files
```

`.pre-commit-config.yaml` runs ruff (check + format), mypy over `src/reconx`,
the standard hygiene hooks (including `detect-private-key`), validation of the
example definitions and the Helm chart, and
`scripts/check_no_unbounded_collect.sh` — a guard that rejects a `.collect()`
in `src/reconx/spark/` unless the same line shows its bound (`agg(...)`,
`limit(...)`, or an explicit `# bounded: <why>` marker), and rejects
`toPandas()` outright. `make lint` runs that guard too.

Ruff configuration (including the small set of documented per-rule ignores and
why each exists) lives in `pyproject.toml`.

`make validate-config` validates the two shipped example definitions and
statically checks the Helm chart with `scripts/validate_helm_chart.py`.

---

## 6. Project conventions

* **Configuration is data.** If you find yourself adding a branch to the
  engine for a specific reconciliation, add a configuration field instead.
* **camelCase on the wire, snake_case in Python.** Models use
  `alias_generator=_to_camel` with `populate_by_name=True`, so both work when
  parsing and the JSON is always camelCase.
* **Never collect business data to the driver.** Aggregate in Spark; the
  driver sees counters and bounded samples. If you need a fallback that
  touches rows, bound it and log that it happened.
* **Secrets are references.** Nothing resolves a secret except
  `SecretResolver`, and nothing logs a resolved value.
* **Check permissions, never role names.**
* **Errors carry structure.** Raise the typed errors in
  `reconx.common.errors` with `details`; the API maps them to codes.

---

## 7. Adding things

| To add… | Start at |
|---|---|
| A connector | `src/reconx/connectors/base.py`, then [CONNECTORS.md](CONNECTORS.md#adding-a-connector) |
| A comparison rule | `config/enums.py` (`ComparisonRule`) + `spark/reconciliation/comparisons.py` |
| A condition type | `config/enums.py` (`ConditionType`) + `scheduler/conditions.py` |
| A transformation | `config/enums.py` (`TransformType`) + `spark/transforms.py` |
| An API route | `api/routers/`, with a `requires(Permission)` dependency |
| A UI page | `ui/pages/`, registered in `ui/streamlit_app.py` |
| A metrics table | `metrics/models.py`, then `make db-ddl` |

Every one of these comes with a test in the matching `tests/` module. A
change to the engine without an engine test is not finished.

---

## 8. Useful CLI

```bash
reconx-admin gen-key                                    # Fernet key
reconx-admin init-db                                    # MongoDB indexes + metrics tables
reconx-admin check                                      # is every dependency reachable?
reconx-admin create-user jo "s3cret-password" --roles OPERATOR
reconx-admin validate examples/sample-reconciliation.yaml
reconx-admin import examples/sample-reconciliation.yaml --activate
reconx-admin export eod-cash-recon --output eod.yaml
reconx-admin run eod-cash-recon --business-date 2026-09-01 --param business_unit=EMEA
reconx-admin maintenance --purge --replay-events --reclaim-orphans
```
