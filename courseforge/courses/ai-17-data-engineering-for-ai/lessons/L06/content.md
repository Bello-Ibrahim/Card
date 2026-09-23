# L06 dbt Core: Project Setup and First Model

Course: AI-17 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Imagine 40 SQL scripts that must run in a certain order, and only one person knows the order. dbt Core replaces that person's memory with a project: every transformation is a file, and the tool works out what to run and when.

## Explanation
dbt Core is a free, open-source command-line tool for the "T" in ELT [VERIFY]. You write each transformation as a **model**: a `.sql` file that contains one `SELECT` statement. dbt wraps the SELECT in the right `CREATE VIEW` or `CREATE TABLE` command, runs the models in the right order and reports the result. Because models are plain text files, you can keep them in Git, review them and test them.

dbt Core needs three things:

- **An adapter** for your database. dbt talks to each database through a separate package: `dbt-postgres` for PostgreSQL and `dbt-duckdb` for DuckDB [VERSION].
- **A profile**, usually in `~/.dbt/profiles.yml`, that says how to connect: host, user, database file or schema. Keep passwords out of the project folder.
- **A project**, a folder with `dbt_project.yml` and a `models/` folder.

The main commands are `dbt debug` (check the connection), `dbt run` (build models), `dbt test` (run tests, L12) and `dbt build` (run and test in order). By default a model becomes a **view**; you can change it to a **table** with a configuration line.

**Analogy:** dbt is like a recipe book with a smart kitchen assistant. You write each recipe (model) on its own card and say which other recipes it needs. The assistant reads all the cards, decides the cooking order and tells you if a dish failed.

## Worked Example
Leila is a data analyst for a hypothetical group of guesthouses in Marrakesh, Morocco. Her raw bookings are already in a DuckDB file, `riad.duckdb`, in a table `raw.bookings`. She sets up dbt on screen.

On-screen steps:

1. Create and activate a virtual environment: `python -m venv .venv`, then `source .venv/bin/activate` (on Windows: `.venv\Scripts\activate`).
2. Install dbt with the DuckDB adapter: `pip install dbt-core dbt-duckdb` [VERSION]. For PostgreSQL, install `dbt-postgres` instead.
3. Create a project: `dbt init riad_bookings` and choose `duckdb` when asked for the adapter [VERSION]. Open the new folder.
4. Open `~/.dbt/profiles.yml` and make the DuckDB profile point to her file:

```yaml
riad_bookings:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: /home/leila/data/riad.duckdb
      threads: 1
```

   A PostgreSQL profile uses `type: postgres` with `host`, `port`, `user`, `password`, `dbname` and `schema` keys [VERSION]. Read the password from an environment variable, for example `password: "{{ env_var('PG_PASSWORD') }}"`.
5. Run `dbt debug` and show that the connection test passes.
6. Delete the example models that `dbt init` created, then create `models/bookings_first.sql`:

```sql
select
    booking_id,
    guest_country,
    check_in_date
from raw.bookings
```

7. Run `dbt run`. The log shows one view model created and a summary line that reports success [VERSION].
8. Open DuckDB and check the result: `SELECT count(*) FROM main.bookings_first;` The count matches `raw.bookings` (with dbt-duckdb, models go to the `main` schema unless the profile sets another one [VERSION]).

The model name `raw.bookings` is written directly into the SQL here. In L07 Leila replaces it with a declared source, so dbt knows where the data comes from.

## Common Mistake
Many learners put `profiles.yml` with a real database password inside the project folder and then push it to a public Git repository. Keep the profile in your home folder, read secrets from environment variables, and add any local credential files to `.gitignore`. Also, do not paste passwords or connection strings into AI chat tools when you ask for help with an error.

## Key Takeaways
1. A dbt model is one SELECT statement in a `.sql` file; dbt turns it into a view or table and runs models in the right order.
2. dbt Core needs an adapter for your database (such as dbt-postgres or dbt-duckdb), a profile for the connection and a project folder.
3. Use `dbt debug` to test the connection and `dbt run` to build models; keep credentials out of the project.

## Hands-on Exercise
**Task:** Install dbt Core with a PostgreSQL or DuckDB adapter, create a new project, write one model that selects from your raw table, and run it successfully.
**Tools:** Python 3, dbt Core with `dbt-duckdb` or `dbt-postgres` (free), a code editor such as VS Code (free), your `raw.orders` table from L03.
**Steps:**
1. Create a virtual environment and install dbt Core with one adapter.
2. If you use DuckDB, load `orders.csv` into a DuckDB file: in Python, run `duckdb.connect("shop.duckdb").sql("CREATE SCHEMA raw; CREATE TABLE raw.orders AS SELECT * FROM read_csv('orders.csv', all_varchar = true)")`.
3. Run `dbt init shop` and set up the profile for your database.
4. Run `dbt debug` until the connection test passes.
5. Create `models/orders_first.sql` that selects `order_id`, `customer_id` and `order_date` from `raw.orders`.
6. Run `dbt run`, then count the rows of the new view (expected: 9).
7. Take a screenshot of the successful run log.
**What good looks like:** `dbt debug` passes, `dbt run` builds one model without errors, the view has 9 rows, and no password is stored inside the project folder.
**Time:** about 35 minutes

## Review Flags
- [VERSION] dbt Core package and adapter names (`dbt-core`, `dbt-duckdb`, `dbt-postgres`), the `dbt init` prompts, the profile keys, the default schema for dbt-duckdb and the run log wording must be checked against the current releases.
- [VERIFY] dbt Core's open-source licence terms: confirm the current licence before describing it as free and open source on screen.
