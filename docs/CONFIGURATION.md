# Configuration reference

Two things are configured: the **platform** (environment variables, one set
for every service) and **reconciliations** (documents in MongoDB, authored in
the UI or imported from YAML/JSON).

---

# Part 1 — Platform settings

Every service reads the same settings object, so one ConfigMap plus one Secret
drives the whole deployment. `.env.example` is the annotated master list.

## Core

| Variable | Default | Meaning |
|---|---|---|
| `RECONX_ENVIRONMENT` | `local` | `local`/`dev`/`test` relax literal-secret and auth checks; anything else is treated as production |
| `RECONX_SERVICE` | `reconx` | Service name in logs |
| `LOG_LEVEL` | `INFO` | |
| `LOG_FORMAT` | `json` | `json` or `console` |
| `RECONX_STAGING_DIR` | `/tmp/reconx-staging` | Shared staging for SFTP/Excel — must be visible to executors |

## MongoDB (`MONGODB_`)

| Variable | Default |
|---|---|
| `MONGODB_URI` | `mongodb://localhost:27017/?replicaSet=&directConnection=true` |
| `MONGODB_DATABASE` | `reconx` |
| `MONGODB_TLS` | `false` |
| `MONGODB_SERVER_SELECTION_TIMEOUT_MS` | `10000` |
| `MONGODB_MAX_POOL_SIZE` | `50` |

## Metrics database (`RESULT_`)

| Variable | Default | Meaning |
|---|---|---|
| `RESULT_JDBC_URL` | `jdbc:postgresql://localhost:5432/reconx_results` | What Spark uses |
| `RESULT_JDBC_DRIVER` | `org.postgresql.Driver` | |
| `RESULT_JDBC_USER` / `RESULT_JDBC_PASSWORD` | `reconx` | |
| `RESULT_SQLALCHEMY_URL` | derived | What the control plane uses; derived from the JDBC URL when omitted |
| `RESULT_SCHEMA_NAME` | `public` | |
| `RESULT_POOL_SIZE` | `5` | |
| `RESULT_AUTO_CREATE_SCHEMA` | `true` | **Set `false` in production**; apply the migration instead |

## Kafka (`KAFKA_`)

| Variable | Default |
|---|---|
| `KAFKA_ENABLED` | `true` |
| `KAFKA_BOOTSTRAP_SERVERS` | `localhost:9092` |
| `KAFKA_SECURITY_PROTOCOL` | `PLAINTEXT` |
| `KAFKA_SASL_MECHANISM` / `KAFKA_SASL_USERNAME` / `KAFKA_SASL_PASSWORD` | unset |
| `KAFKA_SSL_CA_LOCATION` | unset |
| `KAFKA_TOPIC_PREFIX` | `reconciliation` |
| `KAFKA_CLIENT_ID` | `reconx` |
| `KAFKA_DELIVERY_TIMEOUT_MS` | `30000` |

## Spark (`SPARK_`)

| Variable | Default | Meaning |
|---|---|---|
| `SPARK_MASTER` | `local[*]` | `local[*]`, `spark://…`, `k8s://…` |
| `SPARK_SUBMIT_MODE` | `inprocess` | `inprocess`, `spark-submit`, `kubernetes` |
| `SPARK_IMAGE` | `reconx/spark:1.0.0` | For Spark-on-K8s |
| `SPARK_SERVICE_ACCOUNT` | `reconx-spark` | |
| `SPARK_DRIVER_CORES` / `SPARK_DRIVER_MEMORY` | `1` / `2g` | |
| `SPARK_EXECUTOR_CORES` / `SPARK_EXECUTOR_MEMORY` / `SPARK_EXECUTOR_INSTANCES` | `2` / `4g` / `2` | |
| `SPARK_DYNAMIC_ALLOCATION` (+ `_MIN_EXECUTORS`, `_MAX_EXECUTORS`) | `false` / `1` / `10` | |
| `SPARK_SHUFFLE_PARTITIONS` | `200` | Aim for 2-3x total executor cores |
| `SPARK_ADAPTIVE_ENABLED` | `true` | AQE and skew-join handling |
| `SPARK_BROADCAST_THRESHOLD_MB` | `10` | `-1` disables broadcast joins |
| `SPARK_EXTRA_JARS` / `SPARK_EXTRA_PACKAGES` | unset | JDBC drivers, format libraries |
| `SPARK_EVENT_LOG_DIR`, `SPARK_LOCAL_DIR`, `SPARK_WAREHOUSE_DIR` | unset | |
| `SPARK_JOB_TIMEOUT_SECONDS` | `7200` | |

## Scheduler (`SCHEDULER_`)

| Variable | Default | Meaning |
|---|---|---|
| `SCHEDULER_ENABLED` | `true` | |
| `SCHEDULER_POLL_INTERVAL_SECONDS` | `30` | |
| `SCHEDULER_LOCK_TTL_SECONDS` | `120` | Must exceed a tick's duration |
| `SCHEDULER_NODE_ID` | hostname | Stamped on locks and runs |
| `SCHEDULER_MAX_CONCURRENT_RUNS` | `10` | Per node |
| `SCHEDULER_DATA_WAIT_TIMEOUT_MINUTES` | `240` | Default cap on `WAITING_FOR_DATA` |
| `SCHEDULER_CONDITION_RECHECK_SECONDS` | `300` | |
| `SCHEDULER_ORPHAN_RUN_TIMEOUT_MINUTES` | `720` | Reclaim runs from dead nodes after this |

## Security (`RECONX_SECURITY_`)

| Variable | Default | Meaning |
|---|---|---|
| `RECONX_SECURITY_JWT_SECRET` | `change-me-in-production` | **Change it** |
| `RECONX_SECURITY_JWT_ALGORITHM` | `HS256` | |
| `RECONX_SECURITY_JWT_EXPIRY_MINUTES` | `480` | |
| `RECONX_SECURITY_ENCRYPTION_KEY` | unset | Fernet key for `enc:` secrets — `reconx-admin gen-key` |
| `RECONX_SECURITY_SECRETS_BACKEND` | `auto` | `env`, `file`, `encrypted`, `auto` |
| `RECONX_SECURITY_SECRETS_FILE_DIR` | `/var/run/secrets/reconx` | Where `k8s:` references resolve |
| `RECONX_SECURITY_BOOTSTRAP_ADMIN_USERNAME` | `admin` | |
| `RECONX_SECURITY_BOOTSTRAP_ADMIN_PASSWORD` | unset | Generated and logged once if unset |
| `RECONX_SECURITY_AUTH_ENABLED` | `true` | Development only when false |
| `RECONX_SECURITY_ALLOW_ANONYMOUS_READ` | `false` | |

## API (`API_`) and SMTP (`SMTP_`)

| Variable | Default |
|---|---|
| `API_HOST` / `API_PORT` | `0.0.0.0` / `8000` |
| `API_ROOT_PATH` | `""` (set when behind a path-prefixed ingress) |
| `API_CORS_ORIGINS` | `*` — **restrict in production** |
| `API_WORKERS` | `1` |
| `API_BASE_URL` | `http://localhost:8000` (used by the UI and e-mail links) |
| `API_REQUEST_TIMEOUT_SECONDS` | `120` |
| `SMTP_ENABLED` | `true` |
| `SMTP_HOST` / `SMTP_PORT` | `localhost` / `1025` |
| `SMTP_USERNAME` / `SMTP_PASSWORD` | unset |
| `SMTP_USE_TLS` / `SMTP_USE_SSL` | `false` / `false` |
| `SMTP_FROM_ADDRESS` / `SMTP_FROM_NAME` | `reconx@example.com` / `ReconX Platform` |

## Advisor

| Variable | Default | Meaning |
|---|---|---|
| `ADVISOR_LLM_ENABLED` | `false` | Enrich deterministic findings with a narrative |
| `ANTHROPIC_API_KEY` | unset | Required when the above is true |
| `ADVISOR_LLM_MODEL` | `claude-sonnet-5` | |

---

# Part 2 — Reconciliation definition

```yaml
reconId: eod-cash-recon          # unique, immutable identity
name: End-of-day cash reconciliation
description: Payments file vs core ledger
product: PAYMENTS
customer: EMEA
owner: recon-team@bank.internal
tags: [daily, cash]

variables: [...]                 # declared run parameters
legs: [...]                      # the DAG
conditions: {...}                # data availability
schedule: {...}
notifications: {...}
events: {...}
retention: {...}
spark: {...}                     # per-reconciliation Spark overrides
dataQuality: [...]
idempotencyDimensions: [businessDate]
```

`version`, `status`, `createdBy/At`, `updatedBy/At`, `activatedBy/At` and
`changeComment` are maintained by the platform, not by the author.

## `variables[]`

```yaml
variables:
  - name: business_unit
    label: Business unit
    type: choice                 # string | number | date | boolean | choice
    choices: [EMEA, APAC, AMER]
    default: EMEA
    required: true
    promptAtRun: true            # ask on a manual run
  - name: ledger_table
    default: dbo.LedgerEntries
```

Referenced as `${name}` in queries, table names, paths, topics and file
patterns. `${name:fallback}` supplies an inline default.

**Built-ins, always available:** `${business_date}`,
`${business_date_compact}` (`YYYYMMDD`), `${business_date_yyyy}`,
`${business_date_mm}`, `${business_date_dd}`, `${prev_business_date}`,
`${prev_business_date_compact}`, `${next_business_date}`,
`${run_timestamp}`, `${run_date}`, `${recon_id}`, `${run_id}`.

## `legs[]`

```yaml
legs:
  - id: payments_vs_ledger
    name: Payments vs ledger
    enabled: true
    dependsOn: []                # explicit DAG edges
    sources: [...]               # at least one; two for a two-sided leg
    leftSource: payments
    rightSource: ledger
    keys: [...]
    comparisons: [...]           # simple form (implicit AND)
    matchLogic: {...}            # or the multi-rule form
    aggregates: [...]
    matching: {...}
    exceptionColumns: [...]
    preTransformations: [...]
    postTransformations: [...]
    outputs: [...]
    exceptionOutput: {...}
    dataQuality: [...]
    registerResultView: leg1_result
    continueOnFailure: false
```

### `sources[]`

| Field | Applies to | Notes |
|---|---|---|
| `id`, `name`, `type` | all | `s3`, `storagegrid`, `sftp`, `jdbc`, `filesystem`, `kafka`, `excel`, `temp_view`, `leg_output`, `inline` |
| `connectionRef` | all except temp/leg/inline | Connection id |
| `path`, `bucket`, `filePattern`, `recursive` | file-like | Globs allowed |
| `table`, `query`, `dialect` | jdbc | `dialect`: `generic`, `mssql`, `postgresql`, `mysql`, `oracle`, `db2`, `sqlite` |
| `topic` | kafka | |
| `view` | temp_view | |
| `legRef`, `legOutputRef` | leg_output | |
| `inlineRows` | inline | |
| `format`, `options` | all | Format options are passed to the reader |
| `schema` | all | `mode`: `infer`, `explicit`, `validate`, `evolve` |
| `transformations`, `filter` | all | Applied at read time |
| `dataQuality` | all | Per-source checks |
| `registerTempView`, `repartition`, `cache`, `broadcast` | all | Execution hints |

### `keys[]`

```yaml
keys:
  - left: customer_id
    right: cust_id
    alias: customer
    normalization:
      trim: true
      case: upper
      stripLeadingZeros: true
      padLeft: 10
      padCharacter: "0"
      removeCharacters: "[-/ ]"
      numericScale: 2
      dateFormat: yyyy-MM-dd
      parseDateFormats: [dd/MM/yyyy, yyyyMMdd]
      nullAs: ""
```

Multiple entries make a composite key. Normalisation defaults come from
`matching` (`trimKeys`, `caseInsensitiveKeys`, `nullEqualsNull`) unless the
key overrides them. A NULL component becomes a distinct sentinel unless
`nullAs` maps it to a value.

### `comparisons[]`

```yaml
comparisons:
  - left: amount
    right: amount
    rule: numeric_tolerance
    tolerance: 0.01
    toleranceUnit: absolute      # absolute | percent | seconds | minutes | hours | days
    critical: true               # non-critical mismatches are reported, not fatal
    nullEqualsNull: true
```

| Rule | Behaviour |
|---|---|
| `exact` | Byte equality |
| `case_insensitive` | Equality after upper-casing |
| `trimmed` | Equality after trimming |
| `numeric_exact` | Numeric equality after casting |
| `numeric_tolerance` | `abs(l - r) <= tolerance` |
| `percentage_tolerance` | `abs(l - r) / abs(r) * 100 <= tolerance` |
| `date_tolerance` | Difference within `tolerance` `toleranceUnit` |
| `date_only` | Compare the date part, ignore time |
| `contains` | One side contains the other (case-insensitive) |
| `always_match` | Carry the field into output without comparing |
| `expression` | Custom Spark SQL predicate |

```yaml
  - name: fx_within_book_tolerance
    rule: expression
    expression: "ABS(left.amount - right.amount) <= right.tolerance_limit"
```

`left.x` / `right.x` (also `source_a.x` / `source_b.x`) address the two sides.
Expressions are validated against the SQL guard before execution.

### `matchLogic`

The multi-rule form. Rules group the comparisons that belong together; the
operator says how rules combine; groups nest; any node can be negated.

```yaml
matchLogic:
  operator: OR
  rules:
    - id: value_rule
      name: Amount and currency agree
      operator: AND
      comparisons:
        - {left: amount, right: amount, rule: numeric_tolerance, tolerance: 0.01}
        - {left: currency, right: currency, rule: case_insensitive}
    - id: reference_rule
      comparisons:
        - {left: ext_ref, right: ext_ref, rule: trimmed}
  groups:
    - operator: AND
      negate: true
      rules: [...]
```

Each rule's pass/fail is recorded per row and aggregated into metrics, so the
UI and the advisor can tell you a rule never fires.

### `aggregates[]`

```yaml
aggregates:
  - name: total_by_currency
    function: SUM            # COUNT | COUNT_DISTINCT | SUM | MIN | MAX | AVG
    leftField: amount
    rightField: amount
    groupBy: [{left: currency, right: ccy, alias: currency}]
    tolerance: 0.5
    toleranceUnit: absolute
```

Control totals: they catch a feed that is individually reconciled but
collectively wrong.

### `matching`

| Field | Default | Meaning |
|---|---|---|
| `nullEqualsNull` | `true` | Two NULLs compare equal |
| `caseInsensitiveKeys` | `false` | Default key case handling |
| `trimKeys` | `true` | |
| `keySeparator` | `\|` | |
| `duplicateDetection` | `true` | |
| `failOnDuplicates` | `false` | |
| `treatDuplicatesAsExceptions` | `true` | |
| `broadcastSmallerSide` | `true` | |
| `exceptionThreshold` / `exceptionThresholdPercent` | unset | Above this the run is `PARTIAL_SUCCESS` |
| `maxExceptionRecords` | (capped) | Bound on persisted exceptions |
| `includeMatchedInOutput` | `true` | |
| `comparisonColumnsInExceptions` | `true` | |

### `exceptionColumns[]`

The business columns an officer needs to work a break without opening the
source data:

```yaml
exceptionColumns:
  - trade_date                                          # shorthand: same name both sides
  - {alias: country, left: country, right: country}
  - {alias: ledger_amount, right: amount, source: right}
  - {alias: currency_pair, left: currency, right: currency, source: both}
```

`source`: `coalesce` (default — left, falling back to right), `left`,
`right`, or `both` (both values, joined). These columns are written to the
exception table, shown in the UI grid and included in the CSV export.

### `outputs[]` and `exceptionOutput`

```yaml
outputs:
  - id: breaks
    type: s3                    # jdbc | s3 | storagegrid | filesystem | kafka | sftp | temp_view | none
    connectionRef: results_s3
    path: "s3a://recon-results/${recon_id}/${business_date}/"
    format: parquet
    mode: append                # append | overwrite | errorifexists | ignore
    partitionBy: [business_date]
    categories: [MISMATCH, LEFT_ONLY, RIGHT_ONLY]
    columns: []                 # empty = all
    maxRecordsPerFile: 1000000
    compression: snappy
```

## `conditions`

```yaml
conditions:
  operator: AND                 # AND | OR | NOT
  conditions:
    - type: s3_file_exists
      connectionRef: payments_s3
      path: "s3://payments/in/${business_date}/*.parquet"
      minCount: 1
      minSizeBytes: 1024
    - type: jdbc_query
      connectionRef: ledger
      query: "SELECT COUNT(*) FROM ledger WHERE BusinessDate = '${business_date}'"
      comparator: gt            # gt | gte | lt | lte | eq | ne
      threshold: 0
    - operator: OR
      conditions:
        - {type: sftp_file_exists, connectionRef: sftp, path: /out, filePattern: "*.csv"}
        - {type: previous_run_successful, lookbackHours: 48}
```

Types: `always`, `file_exists`, `s3_file_exists`, `sftp_file_exists`,
`file_count`, `file_size`, `jdbc_query`, `custom_sql`, `kafka_available`,
`previous_run_successful`, `reconciliation_succeeded`. Any node accepts
`negate: true`.

## `schedule`

```yaml
schedule:
  enabled: true
  type: cron                    # cron | interval | daily | weekly | monthly | once | event | manual
  expression: "0 2 * * MON-FRI"
  timezone: Europe/London
  businessDateOffsetDays: -1
  waitForDataMinutes: 120
  timeoutMinutes: 180
  maxConcurrentRuns: 1
  catchUp: false
  misfireGraceSeconds: 900
  retries:
    maxAttempts: 3
    initialDelaySeconds: 60
    maxDelaySeconds: 1800
    multiplier: 2.0
    jitter: true
    retryOnDataUnavailable: false
```

Timezones are real: schedules are evaluated in the named zone, including
across DST transitions.

## `notifications`, `events`, `retention`, `spark`

```yaml
notifications:
  email:
    enabled: true
    recipients: [recon-team@bank.internal]
    cc: []
    on: [SUCCESS, FAILURE, PARTIAL_SUCCESS, DATA_UNAVAILABLE, EXCEPTION_THRESHOLD, CANCELLED]
    subjectPrefix: "[RECON]"
    includeMetrics: true
    includeExceptionSample: true
    exceptionSampleSize: 20

events:
  enabled: true
  topicPrefix: reconciliation
  onFailure: WARN_ONLY          # WARN_ONLY | RETRY | FAIL_RUN
  emitStageEvents: true
  emitExceptionEvents: false
  exceptionEventLimit: 1000

retention:
  runsDays: 365
  exceptionsDays: 90

spark:
  executorInstances: 8
  executorMemory: 8g
  shufflePartitions: 800
  extraConf: {spark.sql.files.maxPartitionBytes: "268435456"}
```

> YAML 1.1 parses a bare `on:` as the boolean `true`. The model accepts that
> (and `notifyOn:`) so hand-written YAML behaves as intended; quoting it as
> `"on":` also works.

## `idempotencyDimensions`

Which fields make a run unique. Default `[businessDate]`, so one
reconciliation runs once per business date per version. Add `business_unit`
and the same definition can run once per unit per date without the duplicate
guard rejecting the second.

---

## Validating a definition

```bash
reconx-admin validate examples/sample-reconciliation.yaml
reconx-admin import examples/sample-reconciliation.yaml --activate
```

or `POST /api/reconciliations/validate`. Validation checks structure,
cross-references (connections, sources, legs), key/comparison column
presence, SQL safety, DAG acyclicity and schedule sanity — before anything
touches a cluster.
