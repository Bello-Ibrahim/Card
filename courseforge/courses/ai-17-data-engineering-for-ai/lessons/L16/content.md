# L16 Capstone Part 1: Design and Ingest

Course: AI-17 · Module: M4 · Objectives: O6, O7 · Video: 5 min (screen demo)

## Hook
For three weeks you built each part of a pipeline on its own. Now you build the whole thing, for a use case you choose. The first step is not code. It is one page that says what you will build and why.

## Explanation
**The capstone brief.** Build a working ELT pipeline that loads a public raw dataset, transforms it with dbt Core, tests its quality, runs on a schedule in Apache Airflow and delivers a documented, AI-ready dataset. You work in three steps: design and ingest (this lesson), transform and test (L17), and orchestrate, document and present (L18). The rubric scores six areas: design choices, raw loading and dbt layers, quality tests, orchestration, the final dataset with its datasheet, and documentation with the walkthrough. Read the rubric on the course page before you start.

**Choosing a dataset and use case.** Pick a public dataset with at least a few thousand rows, a date column and a clear entity, and an AI use case with a clear label. Examples: predicting daily demand at bike-sharing stations, or predicting late deliveries for a logistics company. Check the licence, and avoid datasets with personal data. If you cannot download a dataset, extend the course sample `orders.csv` so the pipeline still works offline.

**The one-page design.** Your design answers six questions:

1. **Use case:** what will the model predict, for whom, and how often?
2. **Sources:** which files or tables, their format and how often they update.
3. **Layers:** the raw tables, staging models, intermediate models and the final mart, with the grain of each.
4. **Tests:** the quality problems you expect, and which ones must stop the pipeline.
5. **Schedule:** when the pipeline runs, and how it recovers from failure.
6. **Output:** the feature table, its feature date, its split rule and its storage format.

Design choices are judged on reliability, cost and fitness for the use case. For example: DuckDB or PostgreSQL? Full rebuild or incremental? Daily or hourly? Write one sentence of reasoning for each choice.

**Analogy:** The design page is like an architect's plan for a small house. It does not show every nail, but it shows the rooms, the doors between them and what the house is for. Builders who skip the plan often have to knock down a wall later.

## Worked Example
Ana is a backend developer at a hypothetical city transport office in Lisbon, Portugal. Her use case: predict the number of bike rentals per station per day, so vans can move bikes to busy stations before the morning rush.

Her design, in short: sources are a daily trips CSV and a station list; staging cleans trips and stations; an intermediate model counts trips per station per day; the mart adds features such as rentals on the same weekday last week, with a feature date of the day before. Tests: unique `trip_id`, no negative durations, every station exists. Schedule: daily at 02:00 with 2 retries. Output: Parquet files with a time-based split. Storage: DuckDB, because one pipeline builds the dataset and no application writes to it.

On-screen steps for the ingest:

1. Open Python and connect to `bikes.duckdb`.
2. Load the raw trips without changes:

```sql
CREATE SCHEMA IF NOT EXISTS raw;
CREATE TABLE raw.trips AS
SELECT * FROM read_csv('trips.csv', all_varchar = true);
```

3. Profile the load:

```sql
SELECT count(*)                          AS rows,
       count(DISTINCT trip_id)           AS distinct_trips,
       count(*) - count(ended_at)        AS missing_end,
       count(*) FILTER (WHERE CAST(duration_s AS INTEGER) < 0) AS negative_duration
FROM raw.trips;
```

On Ana's six invented sample rows, DuckDB returned `6 | 5 | 1 | 1`: one duplicated trip, one trip without an end time and one trip that ended before it started.

4. She records the counts and the three problems in her design page under "Known issues", and adds a test for each one to her plan for L17.

## Common Mistake
Many learners choose a dataset first and look for a use case afterwards, or choose a use case whose label is not in the data. Then the final table cannot be used to train anything. Start from the prediction: write the label as a column name, such as `rentals_next_day`, and confirm that the dataset lets you calculate it from events after the feature date.

## Key Takeaways
1. The capstone is a full ELT pipeline to an AI-ready dataset, built in three steps and assessed with the course rubric.
2. A one-page design covers use case, sources, layers, tests, schedule and output, with a reason for each design choice.
3. Load raw data unchanged, then record row counts and problems before you write any transformation.

## Hands-on Exercise
**Task:** Capstone step 1: write your pipeline design and load the raw data into PostgreSQL or DuckDB, recording the row counts and any problems you found.
**Tools:** PostgreSQL or DuckDB, Python 3, a text editor; a public dataset such as city bike-share trip data [VERIFY], or the extended course sample.
**Steps:**
1. Choose the use case and write the label as a column name.
2. Choose a dataset and record its source, licence and download date.
3. Write the one-page design with the six sections above.
4. Load every source into the `raw` schema with all columns as text.
5. Run a profile query for rows, distinct IDs, missing values and invalid values.
6. Add a "Known issues" list to your design with the real query outputs.
7. Do not load personal data; if a column could identify a person, leave it out and note why.
**What good looks like:** A one-page design with a clear label, grain and reason for each choice; raw tables loaded unchanged; and a profile with real counts and at least three recorded issues or a note that explains why none were found.
**Time:** about 60 minutes

## Review Flags
- [VERIFY] Public bike-share trip datasets or any other dataset named for the capstone: confirm the licence and current download location before recording.
- [VERSION] DuckDB `read_csv` options (`all_varchar`) and the `FILTER` clause were tested with DuckDB 1.5.5; check them against the current release.
