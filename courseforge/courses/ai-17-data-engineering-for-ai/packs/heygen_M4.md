# HeyGen Batch Pack: AI-17 M4 (From Pipeline to AI-Ready Dataset: Capstone)

Course: Data Engineering for AI. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L15 Preparing Datasets for Machine Learning

- **Filename:** `ai-17-data-engineering-for-ai_M4_L15_presenter.mp4`
- **Expected length:** about 5.2 minutes (720 words). The quality gate accepts ±10%.

```text
You have a clean, tested feature table. It is still not ready for a model. How you split it, what personal data it still contains, and what you tell people about it decide whether the model's test results can be trusted.

Your pipeline now runs, retries and backfills by itself. In this lesson, you prepare its output for machine learning. An AI-ready dataset has four properties.

It is clean and tested, so your quality checks pass. It is split correctly into training data, which teaches the model, and test data, which checks it on rows it has never seen. It is protected, so personal data is removed or reduced. And it is documented and versioned.

Let's start with splitting. A random split mixes rows from all dates. That is fine when time does not matter. But when the model predicts the future, such as next month's loan defaults, split by time. Train on earlier dates, and test on later ones. This copies real use. A random split lets the model learn from future rows, so the test results look better than they will be.

If the label looks ahead, for example default in the next ninety days, leave a gap between the last training date and the first test date. Then training labels do not overlap the test period.

Next, personal data. Remove columns the model does not need, such as names and phone numbers. Replace IDs with a key made from a hash and a secret value, called a salt. Rows can still be joined, but the original ID is hidden. This is pseudonymisation, not anonymisation, because with the salt, the ID can be matched again. Rules differ by country, so check your organisation's rules.

A time-based split is like a weather forecaster who tests a new method on last month's weather, using only data from before last month. Testing it on days mixed from the whole year would let the method remember the answers.

Mei Lin is a data engineer at a consumer lender in Penang, Malaysia. Her feature table has one row per borrower per month, with the full name, the phone number, some features, and the label: default in the next ninety days.

In Python, she connects to DuckDB and creates a protected table. It hashes the borrower ID with a salt, and keeps only the feature date, two features and the label. The name and phone columns are gone. In real use, the salt is a secret stored outside the code.

Next, she exports a time-based split as Parquet files. Everything before the first of April goes to the training file, and everything from the first of April goes to the test file.

Then she checks both files with one query. On six invented rows, the training file has three rows, from January to March. The test file has three rows, from April to May. No date appears in both files.

She also notes one limit. The March labels look ninety days ahead, into the test period. So for the real dataset, she will leave a gap.

Last, she writes a short datasheet. It gives the source, what one row means, the date range, the split rule and the personal data removed. It lists known issues, such as few borrowers from rural branches. And it states the intended use: ranking borrowers for a friendly payment reminder, not rejecting loans.

Two common mistakes. The first is a random split for a model that predicts the future, which gives a test score that is too optimistic. The second is thinking that dropping the name makes data anonymous. IDs, exact dates and rare combinations can still identify people. And never paste real personal records into AI chat tools.

Let's recap. First, an AI-ready dataset is clean, split correctly, protected and documented with a datasheet. Second, when a model predicts the future, split by time, and leave a gap when labels look ahead. Third, remove personal data the model does not need, and remember that hashing IDs is pseudonymisation.

Now it is your turn. In the exercise, you create a time-based train and test split of your feature table in DuckDB, export both as Parquet files, and write a half-page datasheet. It takes about thirty-five minutes. After this, the capstone begins. Next lesson: Capstone Part One, Design and Ingest.
```

## L16 Capstone Part 1: Design and Ingest

- **Filename:** `ai-17-data-engineering-for-ai_M4_L16_presenter.mp4`
- **Expected length:** about 5.2 minutes (728 words). The quality gate accepts ±10%.

```text
For three weeks, you built each part of a pipeline on its own. Now you build the whole thing, for a use case you choose. And the first step is not code. It is one page that says what you will build, and why.

Welcome to the capstone. You build a working pipeline that loads a public raw dataset, transforms it with dbt Core, tests its quality, runs on a schedule in Apache Airflow, and delivers a documented, AI-ready dataset.

You work in three steps. Today is design and ingest. Next is transform and test, and last is orchestrate, document and present. The rubric scores six areas, from your design choices to your walkthrough. Read it on the course page before you start.

First, choose a dataset and a use case. Pick a public dataset with at least a few thousand rows, a date column and a clear entity. Pair it with an AI use case that has a clear label, such as daily demand at bike stations, or late deliveries. Check the licence, and avoid personal data. If you cannot download one, extend the course sample file, so it works offline.

Then write a one-page design that answers six questions. What will the model predict, for whom and how often? Which sources? Which layers, and what is the grain of each? Which tests, and which must stop the pipeline? When does it run, and how does it recover? And what exactly is the output?

For each choice, write one sentence of reasoning, based on reliability, cost and fitness for the use case. For example: DuckDB or PostgreSQL? Full rebuild or incremental? Daily or hourly?

The design page is like an architect's plan for a small house. It does not show every nail. But it shows the rooms, the doors between them and what the house is for. Builders who skip the plan often knock down a wall later.

Ana is a backend developer at a city transport office in Lisbon, Portugal. She wants to predict bike rentals per station per day, so vans can move bikes to busy stations before the morning rush.

Her design, in short. The sources are a daily trips file and a station list. Staging cleans trips and stations. An intermediate model counts trips per station per day. The mart adds features, such as rentals on the same weekday last week, with a feature date of the day before.

Her tests check for unique trip IDs, no negative durations, and that every station exists. The pipeline runs daily at two in the morning, with two retries. The output is Parquet files with a time-based split. She chooses DuckDB, because one pipeline builds the dataset and no application writes to it.

Now the ingest. In Python, she connects to her DuckDB file. She creates a raw schema and loads the trips file without changes, with every column as text.

Then she profiles the load with one query. It counts the rows, the distinct trip IDs, the trips without an end time, and the trips with a negative duration.

On her six invented sample rows, DuckDB returns six, five, one and one. That means one duplicated trip, one trip without an end time, and one trip that ended before it started.

She records the counts and the three problems on her design page, under known issues. Then she adds a test for each one to her plan for the next step.

A common mistake is to choose a dataset first and look for a use case afterwards. Then the label is often not in the data. Start from the prediction. Write the label as a column name, such as rentals next day, and check that you can calculate it from the data.

Let's recap. First, the capstone is a full pipeline to an AI-ready dataset, built in three steps and assessed with the course rubric. Second, a one-page design covers use case, sources, layers, tests, schedule and output, with a reason for each choice. Third, load raw data unchanged, and record row counts and problems before you write any transformation.

Now it is your turn. This is capstone step one. Write your one-page design, load your raw data into PostgreSQL or DuckDB, and record the row counts and the problems you find. It takes about an hour. Next lesson: Capstone Part Two, Transform and Test.
```

## L17 Capstone Part 2: Transform and Test

- **Filename:** `ai-17-data-engineering-for-ai_M4_L17_presenter.mp4`
- **Expected length:** about 5.0 minutes (685 words). The quality gate accepts ±10%.

```text
Your raw data is loaded, and your problems are listed. This step turns that list into a pipeline. Every problem becomes either a cleaning rule or a test, and every layer has a clear job.

In capstone step one, you designed your pipeline and loaded the raw data. Now you build the dbt project, in the three layers you already know.

Staging has one model per raw table. It renames, casts, removes exact duplicates and tests rows, with no joins. Intermediate models join and reshape staging models into useful building blocks, such as one row per delivered shipment with its label. Learners often skip this layer, but it keeps marts short and lets two marts share the same logic.

The mart is the final feature table, with one row per entity per feature date. Its features use only data from before that date.

Then add tests at each layer, with the checklist from week three. Would this problem make the AI dataset wrong? Then make it an error, so the build stops before the mart. Does a person need to review it, but the data is still usable? Make it a warning. Is it a business rule, not a column rule? Write a singular test.

Run the build command often. It builds and tests each model in dependency order, so you find each problem in the layer where it starts.

Layers with tests are like the checkpoints in a car factory. The engine is tested before it goes into the car, and the car is tested before it leaves the factory. A fault found at the engine check costs much less than a fault found by the customer.

Yusuf is a data analyst at a logistics company in Istanbul, Türkiye. His capstone predicts whether a shipment will arrive later than promised.

He shows his project tree: one staging model for shipments, one intermediate model that adds the label, and one mart for the shipment features.

He opens the intermediate model. It reads the staging model, calculates the promised hours between pick-up and the promised time, and marks a shipment as late when it was delivered after the promised time. It keeps only delivered shipments.

On four invented shipments, the compiled query in DuckDB returns three rows. S one has twenty-seven promised hours and is not late. S two has thirty-two hours and is late. S three has twenty-eight hours and is not late. S four has no delivery time yet, so it has no label and stays out of training.

The mart has one row per shipment at pick-up time. Its features include the promised hours, the vehicle type, and the late rate on the same route in the thirty days before pick-up.

In the schema file, he shows his test plan. Staging has unique and not null IDs, accepted vehicle types, and a warning for missing delivery times. Intermediate has a unique ID and a singular test for delivery before pick-up. The mart checks the label, and has a leakage test for route features.

He runs the build. One warning appears, for the missing delivery time of S four, as expected. Every error test passes.

A common mistake is to write all the logic in one large mart. When a test fails, nobody can see which part caused it. Keep each model short, with one job. And do not paste your raw data into an AI tool for test ideas. Describe the columns instead.

Let's recap. First, build staging, intermediate and mart models, each with one clear job and one clear grain. Second, turn every known problem into a cleaning rule or a test, and choose error or warn with the week three checklist. Third, run the build often, so each problem is caught in the layer where it starts.

Now it is your turn. This is capstone step two. Build staging, intermediate and mart models for your dataset, with at least eight tests, including one singular test and one leakage check. Make every test pass, and explain each warning. It takes about seventy-five minutes. Next lesson: Capstone Part Three, Orchestrate, Document and Present.
```

## L18 Capstone Part 3: Orchestrate, Document and Present

- **Filename:** `ai-17-data-engineering-for-ai_M4_L18_presenter.mp4`
- **Expected length:** about 4.9 minutes (684 words). The quality gate accepts ±10%.

```text
A pipeline that only runs when you type commands is a prototype. A pipeline that runs every night, stops on bad data, explains itself and delivers a ready dataset is a product. Today, your capstone becomes a product.

In step two, you built and tested your dbt layers. This last step has three pieces: orchestrate, document and present.

First, orchestrate. One Airflow DAG runs the whole pipeline in order. It loads the raw data for the logical date, runs the dbt build, generates the documentation and exports the dataset. Because the build stops on failed error tests, a bad load never reaches the export. Use retries with a delay, and keep every task idempotent, so a rerun is always safe.

Second, document. Generate the dbt documentation, and check that every model has a description, and that the lineage graph connects each source to the final mart. Then finish your datasheet with the real row counts, date range and split of your export. The numbers in the datasheet must match the files.

Third, present. Record a three-minute walkthrough for a colleague who did not build the pipeline. Spend half a minute on the use case and label, one minute on the lineage, forty-five seconds on the tests and a problem they caught, half a minute on the green Airflow run, and fifteen seconds on the files and the main limit.

The walkthrough is like handing over the keys of a house with its manual. You show where the water and electricity come in, which switch does what, and what to check when something stops working. The new owner should not need to call you.

Hana is a data engineer at a dairy cooperative near Addis Ababa, Ethiopia. Her capstone predicts tomorrow's milk collection at each collection centre, so the cooperative can send the right number of cooling trucks.

She opens her DAG file. It runs every day at two in the morning, with two retries, ten minutes apart. There are four bash tasks: load the raw data for the logical date, build with dbt, generate the docs, and export the split. The last line runs the load, then the build, and then the docs and the export side by side.

She triggers the DAG in the web interface. In the graph view, the load runs first, then the build, and then the docs and the export run in parallel.

In the build log, the summary line shows the passed tests and one expected warning. The output folder holds the training file, the test file and the datasheet. She checks the files with a count query, and the numbers match the datasheet.

Then she opens the dbt documentation site, and follows the lineage from the raw collections table to the centre features table.

Finally, she starts her screen recorder and gives the three-minute walkthrough, with the timing plan. She names one limit clearly. Two collection centres opened recently, so the model has little history for them, and their predictions need a human check.

A common mistake is to read code line by line and run out of time before showing the result. Show the lineage, the tests and a green run, and open code only to answer a specific question. The viewer needs to understand what the pipeline does, how it protects data quality, and how to check that it worked. Before recording, close any window with passwords or personal data.

Let's recap. First, one Airflow DAG runs the full pipeline: load, build, documentation and export, with retries and idempotent tasks. Second, the build stops on failed error tests, so bad data never reaches your AI-ready dataset. Third, a short walkthrough of lineage, tests and a green run lets a colleague understand and trust your pipeline without you.

Now it is your turn, for the last capstone step. Run your full pipeline from Airflow, export the dataset and the datasheet, and record your walkthrough. Then submit your project folder, your files, your design page and your recording, with the rubric's checklist. Congratulations on finishing Data Engineering for AI. You now build pipelines that AI can trust.
```
