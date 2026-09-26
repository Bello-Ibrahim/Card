# Screen Demo Pack: AI-17 L06 dbt Core: Project Setup and First Model

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-17-data-engineering-for-ai_L06_screen_1.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Run: python -m venv .venv
2. Run: source .venv/bin/activate  (on Windows: .venv\Scripts\activate)
3. Run: pip install dbt-core dbt-duckdb
4. Caption: for PostgreSQL, install dbt-postgres instead

**Narration over this clip (for pacing)**

> First, she creates and activates a virtual environment. Then she installs dbt Core with the DuckDB adapter. If you use PostgreSQL, you install the PostgreSQL adapter instead.

## Clip 2: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L06_screen_2.mp4`
- **Target length:** about 8 seconds

**Steps**

1. Run: dbt init riad_bookings
2. Choose duckdb at the adapter prompt
3. Open the new riad_bookings folder and show dbt_project.yml and models/

**Narration over this clip (for pacing)**

> Next, she creates a project called riad bookings, and chooses DuckDB when the tool asks for the adapter.

## Clip 3: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L06_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open ~/.dbt/profiles.yml
2. Show the riad_bookings profile from content.md: target dev, type duckdb, path /home/leila/data/riad.duckdb, threads 1
3. Caption: PostgreSQL password via env_var('PG_PASSWORD')

**Narration over this clip (for pacing)**

> Now the profile. She opens the profiles file in her home folder, and points the development target to her DuckDB file, with one thread. A PostgreSQL profile would list the host, port, user and database, and read the password from an environment variable.

## Clip 4: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L06_screen_4.mp4`
- **Target length:** about 3 seconds

**Steps**

1. Run: dbt debug
2. Highlight the passing connection test line

**Narration over this clip (for pacing)**

> She runs debug, and the connection test passes.

## Clip 5: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L06_screen_5.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Delete the example models folder created by dbt init
2. Create models/bookings_first.sql
3. Type the select of booking_id, guest_country, check_in_date from raw.bookings, as in content.md

**Narration over this clip (for pacing)**

> Then she deletes the example models, and writes her first model. It simply selects the booking ID, guest country and check-in date from the raw bookings table.

## Clip 6: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L06_screen_6.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run: dbt run
2. Highlight the log line for one view model and the success summary
3. In DuckDB run: SELECT count(*) FROM main.bookings_first;
4. Show that the count matches SELECT count(*) FROM raw.bookings;

**Narration over this clip (for pacing)**

> She runs dbt. The log shows one view model created, and a summary line that reports success. Finally, she counts the rows in the new view, and the count matches the raw table.

## Production notes for this lesson

- [VERIFY] dbt Core's open-source licence terms: the voiceover calls dbt Core a command-line tool and does not describe its licence; confirm before adding 'free and open source' on screen.
- [VERSION] dbt Core package and adapter names (dbt-core, dbt-duckdb, dbt-postgres), the dbt init prompts, the profile keys, the default schema for dbt-duckdb (main) and the run log wording must be checked against the current releases before recording.
- The profile path /home/leila/data/riad.duckdb is an example; make sure no real password or connection string appears on screen. The PostgreSQL profile reads the password from an environment variable.
- Leila and the guesthouses in Marrakesh, Morocco are fictional; the bookings data is invented.
