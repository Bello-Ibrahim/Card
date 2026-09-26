# L13 Orchestrating with Apache Airflow | Presenter Script

Course: AI-17 · Video: 5 min · Words: 719

## Hook
Your pipeline works when you type three commands in the right order. But who types them at three in the morning, every night? And who notices when the second one fails? An orchestrator does both.

## Explain
In the last lesson, you added tests to your dbt project. Today, you make the whole pipeline run by itself. The tool is Apache Airflow, an orchestrator. It runs pipelines written as Python files, and it shows every run in a web interface.

Four ideas explain Airflow. The first is the DAG, short for directed acyclic graph. A DAG is one pipeline: a set of tasks and the arrows between them. Acyclic means the arrows never loop back.

The second idea is the task, one step, such as load raw data or run dbt. An operator is the type of task. The bash operator, for example, runs a shell command.

The third idea is dependencies. They set the order. Each task starts only after the one before it succeeds. The fourth is the schedule, which says when the DAG runs, for example daily. Each run also has a logical date, which tells the task which day of data to process.

Behind the scenes, several parts run together: a scheduler, a web server, a database for Airflow's own records, and workers that run the tasks. The simplest local setup is the official Docker Compose file. It needs Docker and enough free memory, so check the documentation for your version.

Airflow two and Airflow three differ in imports, some command names and the web interface. Our code targets Airflow three, and shows the Airflow two imports as comments.

Think of Airflow as a train timetable with a station manager. The timetable says when each train leaves. The rail lines say which train must arrive before another departs. And the manager watches every train and reports delays on the station board.

## Demonstrate
Let's build it. Katarzyna is a data engineer at a bakery chain in Kraków, Poland. Her dbt project is in a folder called dbt slash shop, and a Python script loads each day's orders.

First, she downloads the official Docker Compose file for her Airflow version, and creates four folders next to it. On Linux, she also writes her user ID into a small environment file.

She mounts her dbt project and scripts into the containers, and makes dbt available inside them, for local testing only. Then she starts Airflow with two commands.

Now the DAG file. It creates a DAG called shop E L T that starts on the first of September, runs daily, and does not catch up on old dates. Inside are three bash tasks. The first runs the load script and passes it the logical date. The second runs dbt, and the third runs the dbt tests.

The last line sets the order: load, then run, then test. The file only defines tasks and dependencies. No real work happens outside a task.

She opens the web interface on port eight thousand and eighty, and signs in with the default local account. She finds shop E L T, switches it on and triggers it manually.

In the graph view, the three tasks turn green, one after another. She opens the log of the dbt run task, and there is the familiar dbt output.

A common mistake is to put heavy work at the top of the DAG file, such as reading a database outside any task. Airflow reads DAG files often to find changes, so that code runs again and again and slows the scheduler. Keep the file light, and put the real work inside the tasks.

## Recap
Let's recap. First, an Airflow DAG is a pipeline written in Python: tasks, the dependencies between them, and a schedule. Second, the bash operator can run your load script and your dbt commands, and one short line sets their order. Third, the local Docker setup needs enough memory, and Airflow two and three differ, so follow the documentation for your version.

## CTA
Now it is your turn. In the exercise, you write a DAG with three tasks that load raw data, run your dbt models and run your dbt tests, every day. You trigger it manually, and check that the tasks run in the right order. It takes about forty minutes. Next lesson: Retries, Backfills and Alerts.

## Thumbnail
Headline: Pipelines That Run Themselves
Image: Navy background, three connected task boxes turning green in order under a small moon icon, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Apache Airflow's open-source licence must be confirmed before describing it as free and open source; the voiceover only calls it an orchestrator.
- [VERIFY] Memory for the Docker Compose setup (about 4 GB minimum, 8 GB recommended) must be confirmed in the current documentation; the voiceover only says Docker needs enough free memory.
- [VERSION] The local installation method (official docker-compose.yaml, airflow-init, .env with AIRFLOW_UID, _PIP_ADDITIONAL_REQUIREMENTS for local testing only), the Airflow 3 imports (airflow.sdk, airflow.providers.standard) versus Airflow 2 imports, the default local login, the web interface views and Windows support (Docker Desktop or WSL) must be checked against the current release before recording.
- The DAG code on screen is the exact shop_elt.py from content.md; it was checked to parse, not run. Show the Airflow 2 import comments on screen.
- profiles.yml sits in the project folder for the container, so its password must come from an environment variable; do not show a real password on screen.
- Katarzyna and the bakery chain in Kraków, Poland are fictional.
