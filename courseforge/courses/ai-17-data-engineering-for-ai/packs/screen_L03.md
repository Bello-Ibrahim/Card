# Screen Demo Pack: AI-17 L03 Setting Up PostgreSQL and Loading Raw Data

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L03_screen_1.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Open a terminal in the folder that holds indicators.csv
2. Run: docker run --name pg-course -e POSTGRES_PASSWORD=course_pw -p 5432:5432 -d postgres:17
3. Run docker ps to show the pg-course container is up

**Narration over this clip (for pacing)**

> First, in a terminal, she starts PostgreSQL in Docker with one command. It gives the container a name, sets a password and opens the usual port.

## Clip 2: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L03_screen_2.mp4`
- **Target length:** about 6 seconds

**Steps**

1. Run: docker cp indicators.csv pg-course:/tmp/indicators.csv
2. Run: docker exec -it pg-course psql -U postgres
3. Show the postgres=# prompt

**Narration over this clip (for pacing)**

> Next, she copies the file into the container, and opens the SQL shell.

## Clip 3: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L03_screen_3.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Type: CREATE SCHEMA IF NOT EXISTS raw;
2. Type: CREATE TABLE raw.indicators (country_code TEXT, indicator TEXT, year TEXT, value TEXT);
3. Type: \copy raw.indicators FROM '/tmp/indicators.csv' WITH (FORMAT csv, HEADER true)
4. Show the COPY 5 confirmation

**Narration over this clip (for pacing)**

> Now she creates the raw schema, and a raw table with four columns. Every column is text, even the year and the value. That is on purpose. A numeric column would reject the two dots, and the whole load would stop. Then she loads the file with the copy command, telling it that the file is CSV with a header row.

## Clip 4: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L03_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run: SELECT count(*) FROM raw.indicators;  (result: 5)
2. Run: SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = 'raw' AND table_name = 'indicators';
3. Show four rows, each with data_type text

**Narration over this clip (for pacing)**

> After every load, check two things. She counts the rows, and gets five, the same number as in the file. Then she asks the information schema for each column's data type. Every column shows text.

## Clip 5: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L03_screen_5.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Run: SELECT * FROM raw.indicators;
2. Highlight the empty value (shown as null) for PER 2023 and the '..' for BOL 2023
3. Cut to a notes file listing: 1. empty value PER 2023, 2. '..' placeholder BOL 2023

**Narration over this clip (for pacing)**

> Mariana writes both problems in her notes: the empty value, which PostgreSQL stores as null, and the two dots. She does not change them in the raw table. A staging model will convert the dots to null later.

## Production notes for this lesson

- [VERSION] PostgreSQL installation steps (Docker image tag postgres:17, native installers) and default settings differ by operating system and release; check the docker run, docker cp and psql commands against the current release before recording.
- [VERIFY] World Bank development indicators: the voiceover does not name the dataset; confirm licence and download location before showing it on screen.
- Screen output must match content.md: count 5 in PostgreSQL, every column type text. The note that DuckDB shows VARCHAR stays in the lesson page, not in the voiceover.
- Mariana and the charity in Cusco, Peru are fictional; the indicator values in indicators.csv are invented for teaching.
- The password course_pw is for a local teaching container only; show it on screen as in content.md.
