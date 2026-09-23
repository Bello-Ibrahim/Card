# L07 Sources, Staging Models and ref()

Course: AI-17 · Module: M2 · Objectives: O2, O3 · Video: 5 min (screen demo)

## Hook
A column called `amt` in one table, `Amount` in another and `order_value_usd` in a third. Dates stored as text. A test row someone forgot to delete. Every raw table has problems like these, and the staging layer is where you fix them once, for everyone.

## Explanation
A dbt project is built in **layers**. Each layer has one job, which makes the project easier to read and to change:

- **Sources** are the raw tables, declared in a YAML file. dbt does not build them; it only reads them.
- **Staging models** (`stg_`) are one model per source table. They rename columns to one consistent style, cast types, trim spaces and remove rows that are clearly not real data. They do not join, aggregate or change what the data means.
- **Intermediate and mart models** (L08) join and aggregate staging models to answer questions.

Two Jinja functions connect the layers:

- `{{ source('raw', 'orders') }}` points to a declared raw table.
- `{{ ref('stg_orders') }}` points to another model.

When you use these instead of writing table names directly, dbt builds a dependency graph. It knows that `stg_orders` must be built before any model that refers to it, and it can draw the lineage graph (L10). If the raw schema moves, you change one line in the YAML file, not every model.

**Analogy:** Staging is like preparing ingredients before cooking. You wash the vegetables, peel them and cut them to the same size, but you do not yet decide on the dish. Because every ingredient is prepared the same way, any cook can use it for any recipe.

## Worked Example
Sipho is a backend developer at a hypothetical online craft marketplace in Durban, South Africa. The course sample `orders.csv` (L03) is his raw export, loaded into `raw.orders`. It has a duplicated order, a test row, a missing amount and one status written as `Delivered`.

On-screen steps:

1. Create the folder `models/staging/`.
2. Create `models/staging/_sources.yml`:

```yaml
version: 2
sources:
  - name: raw
    schema: raw
    tables:
      - name: orders
```

3. Create `models/staging/stg_orders.sql`:

```sql
with source as (
    select distinct * from {{ source('raw', 'orders') }}
)
select
    cast(order_id as integer)                  as order_id,
    customer_id,
    cast(order_date as date)                   as order_date,
    cast(nullif(amount, '') as decimal(10, 2)) as amount_usd,
    lower(trim(status))                        as order_status,
    upper(country)                             as country_code
from source
where customer_id <> 'TEST'
```

4. Delete `orders_first.sql` from L06, because the staging model replaces it.
5. Run `dbt run --select stg_orders` and show the success line in the log.
6. Query the result: `select * from main.stg_orders order by order_id;` (use your own schema name with PostgreSQL).

We ran the compiled SQL in DuckDB on the course sample. It returned 7 rows from the 9 raw rows: the exact duplicate of order 1007 and the `TEST` row were removed. `order_id` became INTEGER, `order_date` became DATE and `amount_usd` became DECIMAL(10,2). Order 1005 now has the status `delivered`, and order 1006 has a NULL amount. Sipho keeps that NULL: a missing amount is a fact about the data, and a test will report it (L12).

Sipho also names each column in a consistent style: lowercase with underscores, the unit in the name (`amount_usd`) and a clear prefix for codes (`country_code`).

Later models never read `raw.orders` directly. A mart would start with `from {{ ref('stg_orders') }}`, so dbt always builds staging first.

## Common Mistake
Many learners put business logic into staging: they join customers, filter to "delivered only" or calculate totals. Then a second team that needs cancelled orders cannot use the staging model and writes its own copy of the cleaning rules. Keep staging close to the source: clean and rename, but keep every real row and every real column. Business decisions belong in marts.

## Key Takeaways
1. Declare raw tables as sources in YAML and read them with `source()`; read other models with `ref()` so dbt knows the build order.
2. Build one staging model per source that renames, casts and cleans columns without changing their meaning.
3. Remove only rows that are clearly not real data, such as exact duplicates and test rows, and leave business rules for later layers.

## Hands-on Exercise
**Task:** Declare your raw table as a source and build a staging model that renames columns to a consistent style, fixes data types and removes obvious test rows.
**Tools:** Your dbt project from L06 (dbt Core with dbt-duckdb or dbt-postgres), a code editor.
**Steps:**
1. Create `models/staging/_sources.yml` and declare `raw.orders` as a source.
2. Create `stg_orders.sql` using `source()`, not a written table name.
3. Rename every column to lowercase with underscores, and add units or clear suffixes where they help.
4. Cast the ID, date and amount columns to the right types.
5. Remove exact duplicates and the `TEST` row, and standardise the status text.
6. Run `dbt run --select stg_orders` and query the result.
7. Write down the row count before and after, and the reason for each removed row.
**What good looks like:** The model builds without errors, returns 7 rows from the course sample, has correct types for every column, and keeps the order with a missing amount. Your note explains the 2 removed rows.
**Time:** about 30 minutes

## Review Flags
- [VERSION] dbt YAML source syntax, the `source()` and `ref()` functions and the default schema name for query results must be checked against the current dbt Core release and adapter (dbt-postgres, dbt-duckdb).
