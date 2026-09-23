# L03 Setting Up PostgreSQL and Loading Raw Data

Course: AI-17 · Module: M1 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
The first rule of an ELT pipeline sounds strange: when data arrives, do not fix it. Load it exactly as it came, errors included. Today you will set up PostgreSQL and learn why that rule saves you later.

## Explanation
PostgreSQL is a free, open-source relational database. In this course it plays the role of a small warehouse. You can run it in two ways [VERSION]:

- **Docker:** one command starts PostgreSQL in a container. This is the same on Windows, macOS and Linux and is easy to delete later.
- **Native installer:** a normal installation for your operating system. It needs no Docker, but the steps and default settings differ by system and release.

Inside the database, a **schema** is a named folder for tables. We create a schema called `raw` and put every source table there, unchanged. Later layers (staging, marts) go in other schemas.

Why keep raw data exactly as it arrived?

- **Rebuilds:** if a cleaning rule is wrong, you fix the rule and run it again. You never need a new copy from the source.
- **Evidence:** when a number looks wrong, you can prove whether the problem was in the source or in your pipeline.
- **Safety:** loading every column as text means a strange value, such as `..` for "no data", never makes the load fail. You deal with it in the staging layer (L07).

**Analogy:** Raw data is like the original receipts an accountant keeps in a box. The accountant makes clean spreadsheets from them, but never writes on the receipts. If a spreadsheet total is wrong, the receipts show what really happened.

## Worked Example
Mariana is a data analyst at a hypothetical rural development charity in Cusco, Peru. She wants development indicators for Andean countries in PostgreSQL. Her file `indicators.csv` has these rows (values are invented for teaching):

```text
country_code,indicator,year,value
PER,access_electricity_pct,2022,95.1
PER,access_electricity_pct,2023,
BOL,access_electricity_pct,2022,93.4
BOL,access_electricity_pct,2023,..
ECU,access_electricity_pct,2022,98.7
```

On-screen steps:

1. In a terminal, start PostgreSQL in Docker (image tag and options may change [VERSION]):
   `docker run --name pg-course -e POSTGRES_PASSWORD=course_pw -p 5432:5432 -d postgres:17`
2. Copy the file into the container: `docker cp indicators.csv pg-course:/tmp/indicators.csv`
3. Open the SQL shell: `docker exec -it pg-course psql -U postgres`
4. Create the schema and a raw table with every column as text, then load the file:

```sql
CREATE SCHEMA IF NOT EXISTS raw;
CREATE TABLE raw.indicators (
    country_code TEXT, indicator TEXT, year TEXT, value TEXT
);
\copy raw.indicators FROM '/tmp/indicators.csv' WITH (FORMAT csv, HEADER true)
```

5. Check the load:

```sql
SELECT count(*) FROM raw.indicators;
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'raw' AND table_name = 'indicators';
```

The count is 5, and every column shows the type `text`. Mariana notices two problems: one empty value, which PostgreSQL stores as NULL, and one `..`, a placeholder for "no data". She writes both in her notes. She does not change them in the raw table; the staging model will convert `..` to NULL. (We tested these queries in DuckDB, which gives the same count of 5 and shows the type as `VARCHAR`.)

## Common Mistake
Many learners define strict types in the raw table, for example `value NUMERIC`, or "clean" the CSV in a spreadsheet before loading. Then the load fails on `..`, or the spreadsheet silently changes dates and leading zeros. Keep the raw table as text and unchanged. Type conversion is a transformation, so it belongs in the staging layer, where it is visible, tested and repeatable.

## Key Takeaways
1. PostgreSQL can run in Docker or from a native installer; a `raw` schema holds source data exactly as it arrived.
2. Loading every raw column as text means unexpected values never stop the load, and type fixes happen later in staging.
3. After every load, check the row count and the column types, and write down any problems you see.

## Hands-on Exercise
**Task:** Load a CSV dataset into a raw table in PostgreSQL, then count the rows and check each column's data type.
**Tools:** PostgreSQL (free) with Docker Desktop or a native installer; psql or the free DBeaver client.
**Steps:**
1. Save this course sample as `orders.csv`. It comes from a hypothetical online shop and is used in later lessons:

```text
order_id,customer_id,order_date,amount,status,country
1001,C01,2026-01-03,25.50,delivered,KE
1002,C02,2026-01-04,40.00,delivered,BR
1003,C01,2026-01-10,12.75,cancelled,KE
1004,C03,2026-01-12,99.90,delivered,IN
1005,C02,2026-02-01,15.00,Delivered,BR
1006,C04,2026-02-03,,delivered,VN
1007,C03,2026-02-05,60.00,returned,IN
1007,C03,2026-02-05,60.00,returned,IN
1008,TEST,2026-02-06,0.00,delivered,XX
```

2. Start PostgreSQL and open psql, as in the worked example.
3. Create `raw.orders` with six TEXT columns and load the file with `\copy`.
4. Run `SELECT count(*)` (expected: 9) and the `information_schema` query.
5. Write down every problem you can see without changing the data.
6. Optional: load a public dataset instead, such as World Bank development indicators [VERIFY]. Check its licence first, and do not load files that contain personal data.
**What good looks like:** `raw.orders` has 9 rows and 6 text columns, and your notes list at least four problems: the empty amount, the duplicated order 1007, the `TEST` row and the capital letter in `Delivered`.
**Time:** about 30 minutes

## Review Flags
- [VERSION] PostgreSQL installation steps (Docker image tag `postgres:17`, native installers) and default settings differ by operating system and release; check the `docker run`, `docker cp` and `psql` commands against the current release before recording.
- [VERIFY] World Bank development indicators: confirm the licence and current download location before naming the dataset on screen.
