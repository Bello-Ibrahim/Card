# Screen Demo Pack: AI-17 L16 Capstone Part 1: Design and Ingest

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L16_screen_1.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Open Python and connect to bikes.duckdb
2. Run CREATE SCHEMA IF NOT EXISTS raw;
3. Run CREATE TABLE raw.trips AS SELECT * FROM read_csv('trips.csv', all_varchar = true);

**Narration over this clip (for pacing)**

> Now the ingest. In Python, she connects to her DuckDB file. She creates a raw schema and loads the trips file without changes, with every column as text.

## Clip 2: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L16_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Type the profile query from content.md: count(*), count(DISTINCT trip_id), count(*) - count(ended_at), count(*) FILTER (WHERE CAST(duration_s AS INTEGER) < 0)
2. Run it against raw.trips

**Narration over this clip (for pacing)**

> Then she profiles the load with one query. It counts the rows, the distinct trip IDs, the trips without an end time, and the trips with a negative duration.

## Clip 3: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L16_screen_3.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Show the output: 6 | 5 | 1 | 1
2. Label each value: rows, distinct_trips, missing_end, negative_duration

**Narration over this clip (for pacing)**

> On her six invented sample rows, DuckDB returns six, five, one and one. That means one duplicated trip, one trip without an end time, and one trip that ended before it started.

## Clip 4: scene 14

- **Filename:** `ai-17-data-engineering-for-ai_L16_screen_4.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Open the design page and add a Known issues section with the real counts
2. Add one planned test per problem for L17

**Narration over this clip (for pacing)**

> She records the counts and the three problems on her design page, under known issues. Then she adds a test for each one to her plan for the next step.

## Production notes for this lesson

- [VERIFY] Public bike-share trip datasets, or any other dataset named for the capstone: confirm the licence and current download location before recording. The voiceover names no specific dataset.
- [VERSION] DuckDB read_csv options (all_varchar) and the FILTER clause were tested with DuckDB 1.5.5; check against the current release.
- Screen output must match content.md exactly: the profile query returns 6 | 5 | 1 | 1 on Ana's six invented sample rows (one duplicated trip, one missing end time, one negative duration).
- Show the course page with the capstone rubric when the six scoring areas are mentioned.
- Ana and the city transport office in Lisbon, Portugal are fictional; the trip rows are invented.
