# L18 Capstone Part 3: Orchestrate, Document and Present

Course: AI-17 · Module: M4 · Objectives: O4, O7 · Video: 5 min (screen demo)

## Hook
A pipeline that only runs when you type commands is a prototype. A pipeline that runs every night, stops on bad data, explains itself and delivers a ready dataset is a product. This last step turns your capstone into the second one.

## Explanation
Three pieces finish the capstone.

**1. Orchestrate.** One Airflow DAG runs the whole pipeline in order: load the raw data for the logical date, run `dbt build` (models and tests together), generate the documentation, and export the AI-ready dataset. Because `dbt build` stops on failed error tests, a bad load never reaches the export. Use retries with a delay, and keep every task idempotent (L14), so a rerun or a backfill is always safe. A task list in square brackets, such as `[dbt_docs, export]`, means both tasks can run after the build, in parallel.

**2. Document.** Run `dbt docs generate` and check that every model you built has a description and that the lineage graph connects each source to the final mart. Finish the datasheet from L15 with the real row counts, date range and split of your export.

**3. Present.** Record a 3-minute walkthrough for a colleague who did not build the pipeline. Show, do not only tell:

- 30 seconds: the use case and the label.
- 60 seconds: the lineage graph, from raw source to feature table.
- 45 seconds: the tests, and one problem they caught.
- 30 seconds: the Airflow run, all tasks green.
- 15 seconds: the exported files and the datasheet's main limit.

**Analogy:** The walkthrough is like handing over the keys of a house with its manual. You show where the water and electricity come in, which switch does what and what to check when something stops working. The new owner should not need to call you.

## Worked Example
Hana is a data engineer at a hypothetical dairy cooperative near Addis Ababa, Ethiopia. Her capstone predicts tomorrow's milk collection at each collection centre, so the cooperative can send the right number of cooling trucks.

On-screen steps:

1. Open `dags/milk_capstone.py`:

```python
from datetime import datetime, timedelta

from airflow.sdk import DAG  # Airflow 2: from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
# Airflow 2: from airflow.operators.bash import BashOperator

DBT = "cd /opt/airflow/dbt/milk && dbt"

with DAG(
    dag_id="milk_capstone",
    start_date=datetime(2026, 9, 1),
    schedule="0 2 * * *",
    catchup=False,
    default_args={"retries": 2, "retry_delay": timedelta(minutes=10)},
) as dag:
    load_raw = BashOperator(task_id="load_raw",
        bash_command="python /opt/airflow/scripts/load_collections.py {{ ds }}")
    dbt_build = BashOperator(task_id="dbt_build",
        bash_command=f"{DBT} build --profiles-dir .")
    dbt_docs = BashOperator(task_id="dbt_docs",
        bash_command=f"{DBT} docs generate --profiles-dir .")
    export = BashOperator(task_id="export_dataset",
        bash_command="python /opt/airflow/scripts/export_split.py {{ ds }}")

    load_raw >> dbt_build >> [dbt_docs, export]
```

   The schedule `0 2 * * *` means every day at 02:00. We checked that the file parses; it needs an Airflow installation to run [VERSION].
2. Trigger the DAG in the web interface and show the graph view: `load_raw`, then `dbt_build`, then `dbt_docs` and `export_dataset` side by side.
3. Open the `dbt_build` log and show the summary line with passed tests and one expected warning.
4. Show the output folder: `train.parquet`, `test.parquet` and `datasheet.md`.
5. Open the dbt documentation site and follow the lineage from `raw.collections` to `fct_centre_features`.
6. Start the screen recording and give the 3-minute walkthrough, using the timing plan above.

In her walkthrough Hana names one limit clearly: two collection centres opened recently, so the model has little history for them, and their predictions need a human check.

## Common Mistake
Many learners spend the whole walkthrough reading SQL line by line and run out of time before showing the result. The viewer needs to understand what the pipeline does, how it protects data quality and how to check that it worked. Show the lineage, the tests and a green run, and open code only to answer a specific question. Before recording, close any window that shows passwords, profiles or personal data.

## Key Takeaways
1. One Airflow DAG runs the full pipeline: load, `dbt build`, documentation and export, with retries and idempotent tasks.
2. `dbt build` stops on failed error tests, so bad data never reaches the exported AI-ready dataset.
3. A short walkthrough of lineage, tests and a successful run lets a colleague understand and trust the pipeline without you.

## Hands-on Exercise
**Task:** Capstone step 3: run the full pipeline from an Airflow DAG, export the final dataset and datasheet, and record a 3-minute walkthrough of the lineage and the tests.
**Tools:** Apache Airflow with Docker Compose, dbt Core, DuckDB or PostgreSQL, a free screen recorder such as OBS Studio.
**Steps:**
1. Write the capstone DAG with load, `dbt build`, docs and export tasks, retries and a daily schedule.
2. Make sure the load and export scripts use `{{ ds }}` and are idempotent.
3. Trigger the DAG and wait for all tasks to succeed; fix and rerun any failure.
4. Check the exported Parquet files with a count query and update the datasheet with the real numbers.
5. Generate the dbt documentation and check the lineage from every source to the mart.
6. Plan your 3 minutes with the timing plan above, then record the walkthrough.
7. Submit the project folder, the exported files, the datasheet, the design page from L16 and the recording, using the rubric's checklist.
**What good looks like:** A green Airflow run of the full pipeline, exported train and test files that match the datasheet, a complete lineage graph and a clear 3-minute recording that shows the lineage, the tests and one problem they caught.
**Time:** about 90 minutes

## Review Flags
- [VERSION] Airflow 3 imports (`airflow.sdk`, `airflow.providers.standard`) versus Airflow 2 imports, cron schedule strings, `default_args`, list dependencies and the graph view must be checked against the current Airflow release; `dbt build` and `dbt docs generate` behaviour must be checked against the current dbt Core release.
- [VERIFY] Screen recorder suggestion (OBS Studio): confirm it is still free and available for the learners' operating systems.
