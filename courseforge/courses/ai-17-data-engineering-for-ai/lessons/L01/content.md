# L01 What Data Engineers Do for AI

Course: AI-17 · Module: M1 · Objectives: O1, O2 · Video: 5 min

## Hook
A team spends two days training a model and two months getting the data ready for it. That is not bad planning. In most AI projects, collecting, cleaning, joining and delivering data is the largest part of the work, and it is the part that data engineers own.

## Explanation
Data engineering is the work of moving data from the places where it is created to the places where it is used, in a form that people and systems can trust. Four roles appear in every data system:

- **Sources** are where data is created: an app database, a payment service, a sensor, a CSV export from a partner or a public dataset.
- **Pipelines** are the automated steps that copy, clean, join and reshape the data. A pipeline runs again and again, not once.
- **Storage** is where the data lives between steps. It can be a **data warehouse**, a database built for analytical queries on structured tables, or a **data lake**, cheap file storage that holds raw files of any shape. You will compare them in L02.
- **Consumers** are the people and systems that use the result: a dashboard, a finance report, a data scientist, or a machine learning model that retrains every week.

For AI, the consumer has special needs. A model learns whatever patterns the data contains, including mistakes. If a pipeline sends duplicated rows, the model learns that some events happen twice as often as they do. If it mixes future information into training data, the model looks excellent in testing and fails in real use. So the data engineer's job is not only "move the data". It is "move the data so that the model learns the right thing".

A good pipeline for AI has four qualities:

1. **Reliable:** it runs on time, and when it fails, someone knows.
2. **Repeatable:** running it again gives the same result, so a dataset can be rebuilt.
3. **Tested:** automatic checks catch missing, duplicated or invalid values before a consumer sees them.
4. **Documented:** anyone can see where each column comes from and what it means.

This course builds all four with free tools: PostgreSQL and DuckDB for storage, dbt Core for transformations and tests, and Apache Airflow for scheduling.

**Analogy:** A data pipeline is like a water treatment plant. River water (raw data) arrives full of mud and leaves. The plant filters it, treats it and tests it in fixed stages, then sends safe water to every tap (the consumers), every day. When the plant works well, nobody notices it. When it fails, everybody downstream notices at once.

## Worked Example
Tomás is a backend developer at a hypothetical crop insurance start-up in Córdoba, Argentina. The data science team wants a model that predicts which farms will make a drought claim next season. They ask Tomás for "a table of farms with their history".

Tomás maps the flow before writing any code:

| Stage | What he finds |
|---|---|
| Sources | The policy database (farms, crops, dates), the claims system, daily rainfall files from a weather provider, and field-visit notes typed by agents |
| Pipeline | A nightly job that copies the four sources, cleans them and joins them by farm and date |
| Storage | Raw copies kept unchanged; cleaned tables and a final "one row per farm per season" table in a warehouse |
| Consumers | The data science team (model training), the finance team (claims report) and a dashboard for regional managers |

The map shows two risks early. First, the rainfall files use station codes, not farm IDs, so Tomás needs a lookup table that links each farm to its nearest station. Second, the field-visit notes are sometimes written after a claim is paid. If those notes enter the training data, the model will "see" the answer. He writes both risks next to the map and agrees with the data scientists which date each column is based on.

## Common Mistake
Many people think data engineering is a one-time job: "load the data once, then the model team takes over". In practice the model is retrained, new rows arrive every day, and sources change their format without warning. A one-off script that worked once becomes a problem the next week. Treat every data flow as a system that runs repeatedly: plan for schedules, failures, tests and documentation from the first day.

## Key Takeaways
1. Every data system has sources, pipelines, storage and consumers; mapping them is the first step of any data engineering task.
2. AI models learn from whatever the data contains, so duplicated, missing or future information quietly produces a worse model.
3. A good pipeline for AI is reliable, repeatable, tested and documented, not only fast.

## Hands-on Exercise
**Task:** Map the data flow of a hypothetical ride-hailing app in Jakarta, Indonesia: list 4 data sources, where the data is stored, and 3 teams or systems that use it.
**Tools:** Pen and paper, or a free diagram tool such as draw.io (diagrams.net).
**Steps:**
1. Draw four boxes in a row: Sources, Pipeline, Storage, Consumers.
2. List 4 sources, for example driver GPS pings, trip bookings, payments and in-app ratings.
3. For each source, write how often new data arrives (every second, every trip, once a day).
4. Under Storage, decide what stays as raw data and what becomes clean tables.
5. List 3 consumers, for example a pricing model, a driver payments team and a safety team.
6. Mark one risk for an AI consumer, such as a column that is only known after the event you want to predict.
7. Do not use real personal data about drivers or riders; invent all examples.
**What good looks like:** A one-page diagram with 4 named sources, a clear split between raw and clean storage, 3 consumers with what each one needs, and at least one written data risk.
**Time:** about 20 minutes

## Review Flags
- None. The examples are hypothetical and the lesson states no statistics, dates or product facts that need checking.
