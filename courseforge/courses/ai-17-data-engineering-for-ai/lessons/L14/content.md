# L14 Retries, Backfills and Alerts

Course: AI-17 · Module: M3 · Objectives: O4, O6 · Video: 5 min (screen demo)

## Hook
Your pipeline will fail. A source server restarts, a file arrives late, a password expires. The question is not whether it fails, but what happens next: does it recover by itself, and does it leave clean data behind?

## Explanation
Four design choices make a pipeline safe to fail:

- **Retries.** Many failures are temporary, such as a network timeout. Airflow can try a task again automatically: `retries` sets how many times, and `retry_delay` sets how long to wait. A delay gives the other system time to recover.
- **Idempotent tasks.** A task is idempotent when running it twice for the same date gives the same result as running it once. A load that only appends rows is not idempotent: a retry doubles the data. A load that first deletes that date's rows and then inserts them is idempotent. Retries are only safe when tasks are idempotent.
- **Backfills.** When a pipeline was down, or a rule changed, you rerun it for past dates. Each run receives its logical date as `{{ ds }}`, so the task loads the right day. Backfills are only safe when tasks are idempotent too.
- **Alerts.** When a task still fails after all retries, a person must know. Airflow can call a Python function on failure (`on_failure_callback`), which can send an email or a chat message [VERSION].

**Analogy:** A good pipeline is like a postal service. If nobody is home, the courier tries again tomorrow, not twice at the same door today. Every parcel has a tracking number, so a second attempt never creates a second parcel. If delivery fails three times, the sender is informed.

## Worked Example
Tariq is a data engineer at a hypothetical pharmacy chain in Karachi, Pakistan. Each store's sales file arrives every night as `sales_YYYY-MM-DD.csv`. Last week the file server was down for three nights.

On-screen steps:

1. Make the load script idempotent. `load_sales.py` receives the logical date and replaces that date's rows:

```python
import sys
import duckdb

ds = sys.argv[1]                      # logical date from {{ ds }}
con = duckdb.connect("pharmacy.duckdb")
con.execute("DELETE FROM raw.sales WHERE load_date = ?", [ds])
con.execute(
    "INSERT INTO raw.sales SELECT *, CAST(? AS DATE) FROM read_csv(?, all_varchar = true)",
    [ds, f"sales_{ds}.csv"],
)
```

We ran it twice for `2026-09-01` on a three-row sample file: the table held 3 rows after each run, not 6.

2. Add retries and an alert to the DAG from L13 and pass `default_args=default_args` to the `DAG`:

```python
from datetime import timedelta

def notify_failure(context):
    ti = context["task_instance"]
    print(f"ALERT: {ti.dag_id}.{ti.task_id} failed for {context['ds']}")

default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=10),
    "on_failure_callback": notify_failure,
}
```

   In real use, `notify_failure` would send a message to the team's chat or email instead of printing.
3. Rename the sales file for one date so the load fails. Trigger the DAG and show the task in the "up for retry" state, then failed after 3 retries, with the alert line in the log [VERSION].
4. Restore the file and clear the failed task; it succeeds.
5. Backfill the three missed nights. In Airflow 3: `airflow backfill create --dag-id pharmacy_sales --from-date 2026-09-01 --to-date 2026-09-03`. In Airflow 2: `airflow dags backfill -s 2026-09-01 -e 2026-09-03 pharmacy_sales` [VERSION]. With Docker Compose, run the command inside a container with `docker compose exec` [VERSION].
6. Check the result: `SELECT load_date, count(*) FROM raw.sales GROUP BY load_date ORDER BY load_date;` Each date appears once, with its own row count.

## Common Mistake
Many learners set a high number of retries and think the pipeline is now reliable. If the task appends data, every retry that failed halfway can leave partial or doubled rows. And if the error is permanent, such as a wrong column name, retries only delay the alert. Make tasks idempotent first, use a small number of retries with a delay, and make sure a person hears about the final failure.

## Key Takeaways
1. Retries with a delay handle temporary failures, but they are only safe when tasks are idempotent.
2. An idempotent task gives the same result when run twice, for example by deleting and reloading one date's rows.
3. Backfills rerun past dates using the logical date, and failure alerts make sure a person knows when retries are not enough.

## Hands-on Exercise
**Task:** Make one task fail on purpose, watch the retries in Airflow, then fix it and run a backfill for 3 past dates. Check that no rows are duplicated.
**Tools:** Your Airflow setup and DAG from L13, DuckDB or PostgreSQL, a terminal.
**Steps:**
1. Change your load script so it deletes and reloads the rows for the logical date `{{ ds }}`.
2. Add `retries`, `retry_delay` (use 1 minute for the exercise) and `on_failure_callback` to the DAG.
3. Break the load on purpose, for example by pointing it to a missing file name.
4. Trigger the DAG and record each retry attempt from the task log.
5. Fix the problem and clear the task so it succeeds.
6. Run a backfill for 3 past dates with the command for your Airflow version.
7. Run a duplicate check on the raw table, then run the backfill again and check that the counts do not change.
**What good looks like:** Screenshots of the retries and of the alert message, a successful backfill for 3 dates, and a count query that returns the same numbers before and after the second backfill.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Airflow backfill commands differ between versions (`airflow backfill create` in Airflow 3, `airflow dags backfill` in Airflow 2); `default_args`, `on_failure_callback`, the task context keys, task state names in the interface and the `docker compose exec` service names must be checked against the current release.
- [VERSION] DuckDB prepared parameters inside `read_csv(?)` were tested with DuckDB 1.5.5; check them against the current release.
