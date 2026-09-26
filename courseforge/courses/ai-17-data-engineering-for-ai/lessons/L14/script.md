# L14 Retries, Backfills and Alerts | Presenter Script

Course: AI-17 · Video: 5 min · Words: 682

## Hook
Your pipeline will fail. A server restarts, a file arrives late, a password expires. The question is not whether it fails, but what happens next. Does it recover by itself? And does it leave clean data behind?

## Explain
In the last lesson, you built a DAG that runs every night. Today, you make it safe to fail. Four design choices help: retries, idempotent tasks, backfills and alerts.

First, retries. Many failures are temporary, such as a network timeout. Airflow can try a task again automatically. You set how many times, and how long to wait between tries. The wait gives the other system time to recover.

Second, idempotent tasks. A task is idempotent when running it twice for the same date gives the same result as running it once. A load that only adds rows is not idempotent, because a retry doubles the data. A load that first deletes that date's rows, and then inserts them again, is idempotent. Retries are only safe when tasks are idempotent.

Third, backfills. When a pipeline was down, or a rule changed, you rerun it for past dates. Each run receives its logical date, so the task loads the right day. Again, this is only safe with idempotent tasks.

Fourth, alerts. When a task still fails after all its retries, a person must know. Airflow can call a Python function on failure, and that function can send an email or a chat message.

A good pipeline is like a postal service. If nobody is home, the courier tries again tomorrow, not twice at the same door today. Every parcel has a tracking number, so a second attempt never creates a second parcel. And if delivery fails three times, the sender is told.

## Demonstrate
Tariq is a data engineer at a pharmacy chain in Karachi, Pakistan. Every night, each store's sales file arrives with the date in its name. Last week, the file server was down for three nights.

First, he makes the load script idempotent. It receives the logical date, deletes that date's rows from the raw sales table, and then inserts the rows from that day's file.

He runs it twice for the first of September, on a small sample file. The table holds three rows after each run, not six.

Next, he adds default arguments to the DAG from the last lesson: three retries, ten minutes apart, and a failure function. Here it only prints an alert line. In real use, it would send a message to the team.

Now he breaks it on purpose. He renames the sales file for one date and triggers the DAG. The task waits and tries again. After three retries, it fails, and the alert line appears in the log.

He restores the file and clears the failed task. This time it succeeds.

Then he backfills the three missed nights, from the first to the third of September, with the backfill command for his Airflow version, inside the container. Finally, he counts rows per load date. Each date appears once, with its own count. Running the backfill again would change nothing, because the load is idempotent.

A common mistake is to set many retries and think the pipeline is now reliable. If a task adds data, a retry can leave doubled rows. And if the error is permanent, retries only delay the alert. Make tasks idempotent first, and use a few retries with a delay.

## Recap
Let's recap. First, retries with a delay handle temporary failures, but they are only safe when tasks are idempotent. Second, an idempotent task gives the same result when you run it twice, for example by deleting and reloading one date's rows. Third, backfills rerun past dates using the logical date, and alerts make sure a person knows when retries are not enough.

## CTA
Now it is your turn. In the exercise, you make one task fail on purpose and watch the retries. Then you fix it, run a backfill for three past dates, and run it again to check that no rows are doubled. It takes about forty minutes. Next lesson: Preparing Datasets for Machine Learning.

## Thumbnail
Headline: Safe to Fail
Image: Navy background, a task box with a circular retry arrow, a small bell and a calendar showing three dates filled in, headline in teal Inter Bold.

## Production Notes
- [VERSION] Backfill commands differ between versions: Airflow 3 uses airflow backfill create --dag-id pharmacy_sales --from-date 2026-09-01 --to-date 2026-09-03; Airflow 2 uses airflow dags backfill -s 2026-09-01 -e 2026-09-03 pharmacy_sales. With Docker Compose, run it inside a container with docker compose exec; check the service names.
- [VERSION] default_args, on_failure_callback, the task context keys, the 'up for retry' state name and other interface labels must be checked against the current Airflow release.
- [VERSION] DuckDB prepared parameters inside read_csv(?) were tested with DuckDB 1.5.5; check against the current release.
- Screen output must match content.md: running load_sales.py twice for 2026-09-01 on the three-row sample file leaves 3 rows after each run, not 6.
- notify_failure only prints in the demo; the voiceover says a real one would send a chat message or email.
- Tariq and the pharmacy chain in Karachi, Pakistan are fictional; the sales rows are invented.
