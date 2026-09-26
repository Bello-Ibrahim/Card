# Screen Demo Pack: AI-17 L13 Orchestrating with Apache Airflow

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L13_screen_1.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Download the official docker-compose.yaml for the Airflow version from the Airflow documentation
2. In the same folder, create dags, logs, plugins and config folders
3. On Linux, create .env with AIRFLOW_UID= followed by the output of id -u

**Narration over this clip (for pacing)**

> First, she downloads the official Docker Compose file for her Airflow version, and creates four folders next to it. On Linux, she also writes her user ID into a small environment file.

## Clip 2: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L13_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. In docker-compose.yaml, add volumes such as ./dbt:/opt/airflow/dbt and the scripts folder
2. Add dbt through _PIP_ADDITIONAL_REQUIREMENTS, with a 'local testing only' caption
3. Run: docker compose up airflow-init
4. Run: docker compose up -d

**Narration over this clip (for pacing)**

> She mounts her dbt project and scripts into the containers, and makes dbt available inside them, for local testing only. Then she starts Airflow with two commands.

## Clip 3: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L13_screen_3.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Create dags/shop_elt.py
2. Paste the DAG code from content.md, with the Airflow 2 import comments visible
3. Highlight dag_id, start_date, schedule="@daily" and catchup=False
4. Highlight the three BashOperator tasks and {{ ds }} in load_raw

**Narration over this clip (for pacing)**

> Now the DAG file. It creates a DAG called shop E L T that starts on the first of September, runs daily, and does not catch up on old dates. Inside are three bash tasks. The first runs the load script and passes it the logical date. The second runs dbt, and the third runs the dbt tests.

## Clip 4: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L13_screen_4.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Highlight the last line: load_raw >> dbt_run >> dbt_test

**Narration over this clip (for pacing)**

> The last line sets the order: load, then run, then test. The file only defines tasks and dependencies. No real work happens outside a task.

## Clip 5: scene 14

- **Filename:** `ai-17-data-engineering-for-ai_L13_screen_5.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Open http://localhost:8080 and sign in with the default local account from the documentation
2. Find shop_elt in the DAG list
3. Switch it on and trigger it manually

**Narration over this clip (for pacing)**

> She opens the web interface on port eight thousand and eighty, and signs in with the default local account. She finds shop E L T, switches it on and triggers it manually.

## Clip 6: scene 15

- **Filename:** `ai-17-data-engineering-for-ai_L13_screen_6.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Open the graph view and show load_raw, dbt_run and dbt_test turning green in order
2. Open the dbt_run task log and show the dbt output

**Narration over this clip (for pacing)**

> In the graph view, the three tasks turn green, one after another. She opens the log of the dbt run task, and there is the familiar dbt output.

## Production notes for this lesson

- [VERIFY] Apache Airflow's open-source licence must be confirmed before describing it as free and open source; the voiceover only calls it an orchestrator.
- [VERIFY] Memory for the Docker Compose setup (about 4 GB minimum, 8 GB recommended) must be confirmed in the current documentation; the voiceover only says Docker needs enough free memory.
- [VERSION] The local installation method (official docker-compose.yaml, airflow-init, .env with AIRFLOW_UID, _PIP_ADDITIONAL_REQUIREMENTS for local testing only), the Airflow 3 imports (airflow.sdk, airflow.providers.standard) versus Airflow 2 imports, the default local login, the web interface views and Windows support (Docker Desktop or WSL) must be checked against the current release before recording.
- The DAG code on screen is the exact shop_elt.py from content.md; it was checked to parse, not run. Show the Airflow 2 import comments on screen.
- profiles.yml sits in the project folder for the container, so its password must come from an environment variable; do not show a real password on screen.
- Katarzyna and the bakery chain in Kraków, Poland are fictional.
