# L13 Orchestrating with Apache Airflow

Course: AI-17 · Module: M3 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
Your pipeline works when you type three commands in the right order. But who types them at 03:00 every night, and who notices when the second one fails? An orchestrator does both.

## Explanation
Apache Airflow is a free, open-source orchestrator [VERIFY]. It runs pipelines written as Python files and shows every run in a web interface. Four ideas explain it:

- A **DAG** (directed acyclic graph) is one pipeline: a set of tasks and the arrows between them. "Acyclic" means the arrows never loop back.
- A **task** is one step, such as "load raw data" or "run dbt". An **operator** is the type of task; `BashOperator` runs a shell command.
- **Dependencies** set the order: `load_raw >> dbt_run >> dbt_test` means each task starts only after the one before it succeeds.
- A **schedule** says when the DAG runs, for example `"@daily"`. Each run has a **logical date**, available in commands as `{{ ds }}`, which tells the task which day of data to process.

Airflow has several parts that run together: a scheduler, a web server or API server, a database for its own records and workers that run tasks. The simplest local setup is the official Docker Compose file [VERSION]. It needs Docker and enough free memory; the Airflow documentation gives a minimum of about 4 GB, with 8 GB recommended [VERIFY]. On Windows, Airflow usually runs through Docker Desktop or WSL [VERSION].

Airflow 2 and Airflow 3 differ in imports, some command names and the web interface [VERSION]. The code below targets Airflow 3 and shows the Airflow 2 imports as comments. In this course Airflow calls dbt with simple shell commands, so you install one extra tool, not an integration package.

**Analogy:** Airflow is like a train timetable with a station manager. The timetable (schedule) says when each train leaves; the rail lines (dependencies) say which train must arrive before another departs; the manager (scheduler) watches every train and reports delays on the station board (web interface).

## Worked Example
Katarzyna is a data engineer at a hypothetical bakery chain in Kraków, Poland. Her dbt project is in a folder `dbt/shop`, and a Python script loads each day's orders.

On-screen steps:

1. Download the official `docker-compose.yaml` for your Airflow version from the Airflow documentation [VERSION]. In the same folder, create `dags`, `logs`, `plugins` and `config` folders.
2. On Linux, create a `.env` file with `AIRFLOW_UID=` followed by the output of `id -u`.
3. Mount the dbt project and scripts into the containers by adding volumes such as `./dbt:/opt/airflow/dbt` in the compose file, and make dbt available in the image, for example with `_PIP_ADDITIONAL_REQUIREMENTS` for local testing only [VERSION].
4. Run `docker compose up airflow-init`, then `docker compose up -d`.
5. Save this file as `dags/shop_elt.py`:

```python
from datetime import datetime

from airflow.sdk import DAG  # Airflow 2: from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
# Airflow 2: from airflow.operators.bash import BashOperator

DBT = "cd /opt/airflow/dbt/shop && dbt"

with DAG(
    dag_id="shop_elt",
    start_date=datetime(2026, 9, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    load_raw = BashOperator(
        task_id="load_raw",
        bash_command="python /opt/airflow/scripts/load_orders.py {{ ds }}",
    )
    dbt_run = BashOperator(task_id="dbt_run", bash_command=f"{DBT} run --profiles-dir .")
    dbt_test = BashOperator(task_id="dbt_test", bash_command=f"{DBT} test --profiles-dir .")

    load_raw >> dbt_run >> dbt_test
```

6. Open `http://localhost:8080` and sign in with the default local account from the documentation [VERSION].
7. Find `shop_elt`, switch it on, and trigger it manually.
8. Open the graph view and show the three tasks turning green in order. Open the log of `dbt_run` and show the dbt output.

We checked that this Python parses without errors; it cannot run without an Airflow installation. The `profiles.yml` here sits in the project folder for the container, so its password must come from an environment variable, not from the file.

## Common Mistake
Many learners put heavy work at the top level of the DAG file, such as reading a database or a large file outside any task. Airflow reads DAG files often to find changes, so that code runs again and again and slows the scheduler. Keep the DAG file light: define tasks and dependencies only, and put the real work inside the tasks.

## Key Takeaways
1. An Airflow DAG is a pipeline written in Python: tasks, dependencies between them and a schedule.
2. `BashOperator` can run your load script and dbt commands, and `>>` sets the order in which they run.
3. The local Docker Compose setup needs Docker and enough memory, and Airflow 2 and 3 differ in imports and interface, so follow the documentation for your version.

## Hands-on Exercise
**Task:** Write a DAG with 3 tasks (load raw data, run dbt models, run dbt tests) that runs daily, trigger it manually, and check that the tasks run in the right order.
**Tools:** Apache Airflow with Docker Compose (free), Docker Desktop, your dbt project, a code editor.
**Steps:**
1. Set up Airflow with the official Docker Compose file for your version.
2. Write a small `load_orders.py` that loads `orders.csv` into `raw.orders`.
3. Create the DAG with `schedule="@daily"`, `catchup=False` and the three tasks.
4. Check the file for errors with `python -c "import ast; ast.parse(open('dags/your_dag.py').read())"`.
5. Trigger the DAG in the web interface and watch the graph view.
6. Take a screenshot of the successful run and of one task log.
**What good looks like:** The DAG appears without import errors, all three tasks finish green in the order load, run, test, and the `dbt_test` log shows the test results from L12.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Airflow's local installation method (Docker Compose file, `airflow-init`, `.env`, `_PIP_ADDITIONAL_REQUIREMENTS`), the Airflow 3 imports (`airflow.sdk`, `airflow.providers.standard`) versus Airflow 2 imports, the default local login, the web interface views and Windows support (Docker Desktop or WSL) must be checked against the current release.
- [VERIFY] Minimum and recommended memory for Airflow's Docker Compose setup (stated here as about 4 GB minimum, 8 GB recommended) must be confirmed in the current documentation.
- [VERIFY] Apache Airflow's open-source licence must be confirmed before describing it as free and open source on screen.
