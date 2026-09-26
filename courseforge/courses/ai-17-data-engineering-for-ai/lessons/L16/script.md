# L16 Capstone Part 1: Design and Ingest | Presenter Script

Course: AI-17 · Video: 5 min · Words: 734

## Hook
For three weeks, you built each part of a pipeline on its own. Now you build the whole thing, for a use case you choose. And the first step is not code. It is one page that says what you will build, and why.

## Explain
Welcome to the capstone. You build a working pipeline that loads a public raw dataset, transforms it with dbt Core, tests its quality, runs on a schedule in Apache Airflow, and delivers a documented, AI-ready dataset.

You work in three steps. Today is design and ingest. Next is transform and test, and last is orchestrate, document and present. The rubric scores six areas, from your design choices to your walkthrough. Read it on the course page before you start.

First, choose a dataset and a use case. Pick a public dataset with at least a few thousand rows, a date column and a clear entity. Pair it with an AI use case that has a clear label, such as daily demand at bike stations, or late deliveries. Check the licence, and avoid personal data. If you cannot download one, extend the course sample file, so it works offline.

Then write a one-page design that answers six questions. What will the model predict, for whom and how often? Which sources? Which layers, and what is the grain of each? Which tests, and which must stop the pipeline? When does it run, and how does it recover? And what exactly is the output?

For each choice, write one sentence of reasoning, based on reliability, cost and fitness for the use case. For example: DuckDB or PostgreSQL? Full rebuild or incremental? Daily or hourly?

The design page is like an architect's plan for a small house. It does not show every nail. But it shows the rooms, the doors between them and what the house is for. Builders who skip the plan often knock down a wall later.

## Demonstrate
Ana is a backend developer at a city transport office in Lisbon, Portugal. She wants to predict bike rentals per station per day, so vans can move bikes to busy stations before the morning rush.

Her design, in short. The sources are a daily trips file and a station list. Staging cleans trips and stations. An intermediate model counts trips per station per day. The mart adds features, such as rentals on the same weekday last week, with a feature date of the day before.

Her tests check for unique trip IDs, no negative durations, and that every station exists. The pipeline runs daily at two in the morning, with two retries. The output is Parquet files with a time-based split. She chooses DuckDB, because one pipeline builds the dataset and no application writes to it.

Now the ingest. In Python, she connects to her DuckDB file. She creates a raw schema and loads the trips file without changes, with every column as text.

Then she profiles the load with one query. It counts the rows, the distinct trip IDs, the trips without an end time, and the trips with a negative duration.

On her six invented sample rows, DuckDB returns six, five, one and one. That means one duplicated trip, one trip without an end time, and one trip that ended before it started.

She records the counts and the three problems on her design page, under known issues. Then she adds a test for each one to her plan for the next step.

A common mistake is to choose a dataset first and look for a use case afterwards. Then the label is often not in the data. Start from the prediction. Write the label as a column name, such as rentals next day, and check that you can calculate it from the data.

## Recap
Let's recap. First, the capstone is a full pipeline to an AI-ready dataset, built in three steps and assessed with the course rubric. Second, a one-page design covers use case, sources, layers, tests, schedule and output, with a reason for each choice. Third, load raw data unchanged, and record row counts and problems before you write any transformation.

## CTA
Now it is your turn. This is capstone step one. Write your one-page design, load your raw data into PostgreSQL or DuckDB, and record the row counts and the problems you find. It takes about an hour. Next lesson: Capstone Part Two, Transform and Test.

## Thumbnail
Headline: Plan First, Then Load
Image: Navy background, a one-page design sheet with six ticked sections next to a database cylinder labelled raw, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Public bike-share trip datasets, or any other dataset named for the capstone: confirm the licence and current download location before recording. The voiceover names no specific dataset.
- [VERSION] DuckDB read_csv options (all_varchar) and the FILTER clause were tested with DuckDB 1.5.5; check against the current release.
- Screen output must match content.md exactly: the profile query returns 6 | 5 | 1 | 1 on Ana's six invented sample rows (one duplicated trip, one missing end time, one negative duration).
- Show the course page with the capstone rubric when the six scoring areas are mentioned.
- Ana and the city transport office in Lisbon, Portugal are fictional; the trip rows are invented.
