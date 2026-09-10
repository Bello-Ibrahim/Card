# Operations

Day-two runbook: what to watch, what the states mean, how to fix the things
that actually go wrong, and how to recover.

---

## 1. Daily checks

| Check | Where |
|---|---|
| Any run in `FAILED` since yesterday | UI → Runs, or `GET /api/runs?status=FAILED` |
| Runs stuck in `WAITING_FOR_DATA` | UI → Runs (the condition detail shows the failing leaf) |
| Exception backlog by age | UI → Exceptions, filter `status=OPEN` |
| Scheduler nodes alive | `GET /api/system/status` |
| Locks older than their TTL | `GET /api/system/locks` |
| Outbox depth (undelivered Kafka events) | `GET /api/system/info` |

---

## 2. Run states

| Status | Meaning | Action |
|---|---|---|
| `QUEUED` | Created, not yet submitted | None |
| `STARTING` | Spark submission in flight | None |
| `RUNNING` | Executing | Watch `/api/runs/{id}` |
| `WAITING_FOR_DATA` | Conditions unsatisfied; re-checking | Check the source feed |
| `SKIPPED` | Waited past `waitForDataMinutes` | Investigate the upstream feed; re-run when it lands |
| `SUCCESS` | All legs completed, thresholds respected | None |
| `PARTIAL_SUCCESS` | Completed, but a non-fatal leg failed or a threshold was breached | Read the leg detail |
| `FAILED` | A fatal error | See §4 |
| `CANCELLED` | Cancelled by an operator | Audit says who and why |

`SKIPPED` is not a failure. Missing data is an operational state, and the
platform deliberately distinguishes "the feed never arrived" from "the
reconciliation broke".

---

## 3. Common tasks

### Re-run a reconciliation for a past date

```bash
curl -X POST /api/reconciliations/eod-cash/run \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"businessDate": "2026-09-01", "parameters": {"business_unit": "EMEA"}}'
```

The idempotency key includes the business date, so a second identical request
is rejected rather than producing a duplicate run. To genuinely re-run, cancel
or let the existing run reach a terminal state first, then use
`POST /api/runs/{runId}/retry`, which creates a new run linked to the original.

### Pause a schedule

```bash
curl -X POST /api/schedules/eod-cash/pause -d '{"reason": "upstream migration"}'
```

Pausing writes an audit entry. Resume with `/resume`; the scheduler does not
back-fill the missed firings unless `catchUp` is set on the schedule.

### Force-release a stuck lock

Locks expire by TTL, so this is rarely needed — only when a node died holding
one and you cannot wait out the TTL:

```bash
curl -X DELETE "/api/system/locks/recon:eod-cash"      # requires system:manage
```

### Close a wave of exceptions with one cause

UI → Exceptions → filter (run, field, type) → **Bulk close**, with a mandatory
comment and a resolution code. Every closed record still gets its own
immutable comment row and audit entry, so bulk action is not a shortcut around
the trail.

### Roll back a bad definition

UI → Reconciliation → Versions → **Roll back to v N**. This publishes v N's
content as a *new* version; the history stays linear. Activation still
requires `recon:activate`.

---

## 4. Troubleshooting

### A run failed with a connector error

Look at the run detail's error and the leg it failed on, then test the
connection: UI → Connections → **Test**, or
`POST /api/connections/{id}/test`. The test resolves secrets exactly as the
job does, so a failure here is the same failure the job hit.

| Symptom | Usual cause |
|---|---|
| `SecretResolutionError: Environment variable 'X' is not set` | The Secret key is missing from the pod, or `secretsBackend` disagrees with the reference scheme |
| `No suitable driver` on a JDBC source | The driver jar is not on the Spark classpath — see §5 |
| SFTP host-key rejection | `knownHosts` not populated for a new host |
| S3 `403` with valid keys | Bucket policy, or a path-style/endpoint mismatch on StorageGRID |
| `Table or view not found` for a leg source | An upstream leg did not register its result view — check the DAG order |

### A run failed with `${variable} is not resolved`

A source query references a variable that was neither declared on the
definition (with a default) nor supplied at run time. The error names the
variable. Declare it under `variables:` with a default, or pass it in
`parameters` on the run request.

### Everything reconciles as LEFT_ONLY and RIGHT_ONLY

The key does not line up. This is the single most common configuration
mistake, and the advisor detects it: open the run in the UI and ask the
**Advisor** — it compares one-sided counts on both sides, measures raw versus
normalised value overlap for each shared column, and tells you whether the key
is wrong or the feed is genuinely incomplete.

### Mismatches that "look identical"

Whitespace, case, leading zeros, trailing precision or a date format. The
advisor classifies the actual differences in the exception sample and
recommends the comparison rule and tolerance. Fixing it is usually a
`normalization` block on the key or a `numeric_tolerance` on the comparison.

### The job is slow

| Observation | Fix |
|---|---|
| One task runs far longer than the rest | Key skew — check for a dominant key value; AQE skew handling is on, but a degenerate key needs a better key |
| Huge shuffle spill | Raise `shufflePartitions` (2-3x total executor cores) |
| Small side re-read repeatedly | Set `broadcast: true` on it |
| Long read stage on JDBC | Add a partition column / bounds in the source options; push the filter into the query |
| Long write of exceptions | Expected if break counts are large; check `maxExceptionRecords` is set sanely |

`GET /api/reports/field-metrics?runId=…` shows which comparison is producing
the breaks, which is usually the fastest route to the cause.

### Kafka is down

Runs continue. Events go to the MongoDB outbox and behaviour follows the
definition's `events.onFailure`:

* `WARN_ONLY` (default) — log, carry on
* `RETRY` — retry with exponential backoff, then outbox
* `FAIL_RUN` — the run fails, for reconciliations where downstream
  notification is contractual

Drain the outbox once the broker is back; the maintenance job does this on its
schedule.

### The scheduler is not firing

1. `GET /api/system/status` — is a node reporting recent ticks?
2. Is the definition `ACTIVE` and `enabled`, and its schedule not `paused`?
3. Is `nextFireTime` in the past? (`GET /api/schedules/{reconId}`)
4. Is a stale lock held? (`GET /api/system/locks`)
5. Is `maxConcurrentRuns` already reached by an active run?

---

## 5. Spark classpath and drivers

The Spark image copies `deployment/docker/jars/*.jar` onto the classpath.
If a driver is missing:

* the job logs `jdbc.driver_missing` with the class name;
* exception persistence falls back to a **bounded, streamed driver-side
  insert** (capped at 100 000 rows) and says so in the log — data is not
  silently dropped, but this is a degraded mode. Fix the classpath.

Add drivers with `./scripts/fetch-jdbc-drivers.sh`, or point
`SPARK_EXTRA_JARS` at a location the executors can read.

---

## 6. Monitoring

Scrape `/metrics`. The signals worth alerting on:

| Series | Meaning |
|---|---|
| `reconx_uptime_seconds` | API uptime |
| `reconx_definitions{status=...}` | Definition counts by DRAFT/ACTIVE/DISABLED/ARCHIVED |
| `reconx_runs{status=...}` | Runs by status over the last 7 days |
| `reconx_runs_active` | Runs currently QUEUED/STARTING/RUNNING/WAITING_FOR_DATA |
| `reconx_schedules_enabled` | Enabled, unpaused schedules |
| `reconx_locks_held` | Distributed locks currently held |
| `reconx_local_jobs_running` | Jobs running on this node |

Alerts worth wiring from those:

| Alert | Condition |
|---|---|
| Reconciliation failed | `increase(reconx_runs{status="FAILED"}[1h]) > 0` |
| Data never arrived | `reconx_runs{status="WAITING_FOR_DATA"}` stays non-zero longer than the definition's `waitForDataMinutes` |
| Scheduler stalled | `reconx_local_jobs_running` and `reconx_runs_active` both flat while schedules are due, or `/ready` failing |
| Locks leaking | `reconx_locks_held` above the number of active reconciliations for longer than `SCHEDULER_LOCK_TTL_SECONDS` |
| Readiness flapping | `/ready` failing means MongoDB or the metrics DB is unreachable |

Exception-volume alerting is a warehouse query rather than a gauge — the
exception table carries `recon_id`, `business_date` and `status`, so a spike
against the trailing average is a SQL alert in your BI/monitoring stack.

Logs are JSON with `correlation_id`, `run_id`, `recon_id` and `leg_id`.
One run is one `run_id` grep away; one API request is one `correlation_id`
away, including the Spark job it triggered.

---

## 7. Retention and maintenance

The maintenance CronJob (`deployment/kubernetes/10-maintenance-cronjob.yaml`,
`maintenance.schedule` in the chart) runs `reconx-admin maintenance` nightly.
It is a plain CLI command, so you can run any of it by hand:

```bash
reconx-admin maintenance --purge            # apply each definition's retention block
reconx-admin maintenance --replay-events    # drain the Kafka outbox
reconx-admin maintenance --reclaim-orphans  # fail runs abandoned by dead nodes
```

The shipped CronJob runs `--purge --replay-events`. Add `--reclaim-orphans`
if you want reclamation on a fixed schedule as well as on the scheduler's own
tick. Expired locks need no job: the TTL index removes them.

`--purge` honours `retention.runsDays` and `retention.exceptionsDays` per
definition. Archiving to `retention.archiveTo` before deletion is configured
on the definition but is **not** performed by this command — see
[LIMITATIONS.md](LIMITATIONS.md).

---

## 8. Disaster recovery

| Store | Loses | RPO driver | Restore |
|---|---|---|---|
| MongoDB | Definitions, versions, runs, schedule state, users, audit | Your snapshot/oplog cadence | `mongorestore`, then `reconx-admin init-db` to re-assert indexes |
| Metrics DB | Results, exceptions, field metrics, warehouse audit | Vendor backup cadence | Vendor restore; re-run reconciliations to regenerate results if needed |
| Kafka | Undelivered events | Broker replication | Re-drain the outbox; consumers re-read from their offsets |
| Object storage | Written outputs | Bucket versioning | Re-run the reconciliation — results are reproducible from the sources |

**The platform's outputs are reproducible.** Given the sources and a version
of the definition, re-running produces the same result. That makes MongoDB
(the definitions and the audit trail) the critical restore target; everything
downstream can be rebuilt.

### Restore drill

1. Restore MongoDB into a replica set; run `reconx-admin init-db`.
2. Restore or recreate the metrics schema
   (`src/reconx/metrics/migrations/V1__initial_schema.sql`).
3. Bring up the API with the **same** `RECONX_SECURITY_ENCRYPTION_KEY` — stored
   `enc:` connection secrets cannot be read without it.
4. `GET /api/system/ready` must be green before starting schedulers.
5. Start one scheduler, confirm it ticks and takes locks, then scale up.
6. Re-run one known reconciliation for a past date and compare against the
   pre-incident metrics.

### Regional failover

Control-plane services are stateless, so failover is a data-store question:
run MongoDB with cross-site replica-set members, use your database's own
replication for the metrics store, and deploy the ReconX Deployments in the
standby cluster with the same ConfigMap/Secret. Because run creation is
guarded by the unique idempotency key, a standby fleet that starts while the
primary is still draining cannot double-run a reconciliation.
