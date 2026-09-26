# Screen Demo Pack: AI-17 L14 Retries, Backfills and Alerts

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L14_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Open load_sales.py
2. Show the script from content.md: ds = sys.argv[1], connect to pharmacy.duckdb
3. Highlight DELETE FROM raw.sales WHERE load_date = ? and the INSERT from read_csv of sales_{ds}.csv

**Narration over this clip (for pacing)**

> First, he makes the load script idempotent. It receives the logical date, deletes that date's rows from the raw sales table, and then inserts the rows from that day's file.

## Clip 2: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L14_screen_2.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Run: python load_sales.py 2026-09-01, then count rows in raw.sales: 3
2. Run the same command again and count again: still 3

**Narration over this clip (for pacing)**

> He runs it twice for the first of September, on a small sample file. The table holds three rows after each run, not six.

## Clip 3: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L14_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open the DAG file and add the default_args block from content.md: retries 3, retry_delay timedelta(minutes=10), on_failure_callback notify_failure
2. Show notify_failure printing the ALERT line
3. Pass default_args=default_args to the DAG

**Narration over this clip (for pacing)**

> Next, he adds default arguments to the DAG from the last lesson: three retries, ten minutes apart, and a failure function. Here it only prints an alert line. In real use, it would send a message to the team.

## Clip 4: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L14_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Rename the sales file for one date
2. Trigger the DAG and show the task in the up for retry state
3. Show the task failed after 3 retries and the ALERT line in the task log

**Narration over this clip (for pacing)**

> Now he breaks it on purpose. He renames the sales file for one date and triggers the DAG. The task waits and tries again. After three retries, it fails, and the alert line appears in the log.

## Clip 5: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L14_screen_5.mp4`
- **Target length:** about 6 seconds

**Steps**

1. Restore the file name
2. Clear the failed task and show it turning green

**Narration over this clip (for pacing)**

> He restores the file and clears the failed task. This time it succeeds.

## Clip 6: scene 14

- **Filename:** `ai-17-data-engineering-for-ai_L14_screen_6.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Run with docker compose exec: airflow backfill create --dag-id pharmacy_sales --from-date 2026-09-01 --to-date 2026-09-03 (show the Airflow 2 command as a caption)
2. Run: SELECT load_date, count(*) FROM raw.sales GROUP BY load_date ORDER BY load_date;
3. Highlight that each date appears once

**Narration over this clip (for pacing)**

> Then he backfills the three missed nights, from the first to the third of September, with the backfill command for his Airflow version, inside the container. Finally, he counts rows per load date. Each date appears once, with its own count. Running the backfill again would change nothing, because the load is idempotent.

## Production notes for this lesson

- [VERSION] Backfill commands differ between versions: Airflow 3 uses airflow backfill create --dag-id pharmacy_sales --from-date 2026-09-01 --to-date 2026-09-03; Airflow 2 uses airflow dags backfill -s 2026-09-01 -e 2026-09-03 pharmacy_sales. With Docker Compose, run it inside a container with docker compose exec; check the service names.
- [VERSION] default_args, on_failure_callback, the task context keys, the 'up for retry' state name and other interface labels must be checked against the current Airflow release.
- [VERSION] DuckDB prepared parameters inside read_csv(?) were tested with DuckDB 1.5.5; check against the current release.
- Screen output must match content.md: running load_sales.py twice for 2026-09-01 on the three-row sample file leaves 3 rows after each run, not 6.
- notify_failure only prints in the demo; the voiceover says a real one would send a chat message or email.
- Tariq and the pharmacy chain in Karachi, Pakistan are fictional; the sales rows are invented.
