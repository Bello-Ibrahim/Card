# Screen Demo Pack: AI-17 L18 Capstone Part 3: Orchestrate, Document and Present

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-17-data-engineering-for-ai_L18_screen_1.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Open dags/milk_capstone.py and show the code from content.md, with the Airflow 2 import comments
2. Highlight schedule="0 2 * * *" (every day at 02:00) and default_args retries 2, retry_delay 10 minutes
3. Highlight the four BashOperator tasks and load_raw >> dbt_build >> [dbt_docs, export]

**Narration over this clip (for pacing)**

> She opens her DAG file. It runs every day at two in the morning, with two retries, ten minutes apart. There are four bash tasks: load the raw data for the logical date, build with dbt, generate the docs, and export the split. The last line runs the load, then the build, and then the docs and the export side by side.

## Clip 2: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L18_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Trigger milk_capstone in the web interface
2. Open the graph view: load_raw, then dbt_build, then dbt_docs and export_dataset side by side, all green

**Narration over this clip (for pacing)**

> She triggers the DAG in the web interface. In the graph view, the load runs first, then the build, and then the docs and the export run in parallel.

## Clip 3: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L18_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open the dbt_build task log and highlight the summary line: passed tests and one expected warning
2. Show the output folder: train.parquet, test.parquet, datasheet.md
3. Run a count query on train.parquet and test.parquet and compare with the datasheet numbers

**Narration over this clip (for pacing)**

> In the build log, the summary line shows the passed tests and one expected warning. The output folder holds the training file, the test file and the datasheet. She checks the files with a count query, and the numbers match the datasheet.

## Clip 4: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L18_screen_4.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Open the dbt documentation site
2. Follow the lineage graph from raw.collections to fct_centre_features

**Narration over this clip (for pacing)**

> Then she opens the dbt documentation site, and follows the lineage from the raw collections table to the centre features table.

## Clip 5: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L18_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Start the screen recording
2. Walk through use case, lineage, tests, green run and output files, following the timing plan
3. Caption: limit, two new centres need a human check

**Narration over this clip (for pacing)**

> Finally, she starts her screen recorder and gives the three-minute walkthrough, with the timing plan. She names one limit clearly. Two collection centres opened recently, so the model has little history for them, and their predictions need a human check.

## Production notes for this lesson

- [VERSION] Airflow 3 imports (airflow.sdk, airflow.providers.standard) versus Airflow 2 imports, cron schedule strings, default_args, list dependencies and the graph view must be checked against the current Airflow release; dbt build and dbt docs generate behaviour must be checked against the current dbt Core release.
- [VERIFY] Screen recorder suggestion (OBS Studio) must be confirmed as still free and available for learners' operating systems; the voiceover only says a screen recorder.
- The DAG on screen is the exact milk_capstone.py from content.md, with the Airflow 2 import comments; it was checked to parse, not run.
- Before recording the demo, close any window that shows passwords, profiles or personal data.
- Hana and the dairy cooperative near Addis Ababa, Ethiopia are fictional.
