# L09 Incremental Models and Changing Data

Course: AI-17 · Module: M2 · Objectives: O3, O6 · Video: 5 min (screen demo)

## Hook
Your events table grows every day. On the first day the model builds in seconds; a year later it rebuilds the whole history every night, even though only yesterday's rows are new. Incremental models let dbt process only what changed.

## Explanation
So far every model was rebuilt completely on each run. That is simple and safe, and it is the right default. For large tables that only grow, it becomes slow and, on cloud warehouses, expensive.

An **incremental model** is built in full the first time. On later runs, dbt selects only new or changed rows and adds them to the existing table. You control this with two pieces of Jinja:

- `is_incremental()` is true when the table already exists and the run is not a full refresh.
- `{{ this }}` refers to the existing table, so you can ask "what is the latest timestamp I already have?"

A `unique_key` tells dbt which column identifies a row. If a row with the same key arrives again, dbt replaces it instead of adding a duplicate. How dbt does this (merge, or delete and insert) depends on the adapter [VERSION].

A different problem is data that **changes**. A customer moves to a new city; the source table simply overwrites the old address. If a model needs to know "where did this customer live in January?", the history is gone. A dbt **snapshot** solves this: on every run it compares the source with the last version and keeps old versions with `dbt_valid_from` and `dbt_valid_to` columns. This is often called a slowly changing dimension.

The trade-off: incremental models and snapshots add complexity and new ways to fail. Late-arriving rows can be missed, a wrong filter can create duplicates, and a change in logic only applies to new rows until you run `dbt run --full-refresh`.

**Analogy:** A full rebuild is like reprinting the whole phone book every day. An incremental model prints only the new pages and adds them to the binder. A snapshot is like keeping the old pages when a number changes, stamped with the dates they were valid.

## Worked Example
An is an analytics engineer at a hypothetical language-learning app in Hanoi, Vietnam. The raw table `raw.events` receives app events every day.

On-screen steps:

1. Create `models/marts/fct_events.sql`:

```sql
{{ config(materialized='incremental', unique_key='event_id') }}

select
    event_id,
    user_id,
    event_type,
    cast(event_ts as timestamp) as event_ts,
    current_timestamp           as dbt_loaded_at
from {{ source('raw', 'events') }}
{% if is_incremental() %}
where cast(event_ts as timestamp) > (select max(event_ts) from {{ this }})
{% endif %}
```

2. Run `dbt run --select fct_events`. The first run builds the full table: 3 events.
3. Insert 2 new events for the next day into `raw.events`.
4. Run the same command again. Only the 2 new rows are selected.
5. Run it a third time without new data. No rows are selected.
6. Check for duplicates:

```sql
select event_id, count(*)
from main.fct_events
group by event_id
having count(*) > 1;
```

We simulated the compiled SQL in DuckDB. The second run selected 2 rows, the third selected 0, and the table ended with 5 rows and 5 distinct `event_id` values; the duplicate check returned no rows. The `dbt_loaded_at` column shows that the first 3 rows kept their original load time.

An also tracks changes in user profiles with a snapshot. In recent dbt releases it can be defined in YAML [VERSION]:

```yaml
snapshots:
  - name: users_snapshot
    relation: source('raw', 'users')
    config:
      unique_key: user_id
      strategy: check
      check_cols: ['country', 'plan']
```

She runs `dbt snapshot` every day, before the models.

## Common Mistake
Many learners make every model incremental "for speed" from the first day. On small tables this saves nothing and adds risk: a filter on `>` misses events that arrive late with an older timestamp. Start with full rebuilds. Switch a model to incremental only when it is large and slow, and then add a small look-back window, for example reprocessing the last 3 days, with a `unique_key` to prevent duplicates.

## Key Takeaways
1. Incremental models build the full table once, then process only new or changed rows, using `is_incremental()` and `{{ this }}`.
2. A `unique_key` prevents duplicates when rows arrive again, and snapshots keep the history of records that change.
3. Incremental logic adds complexity and new failure modes, so use it only for large, slow tables and test it for duplicates.

## Hands-on Exercise
**Task:** Convert one model to incremental, add new rows to the raw table, and run it twice. Check that only the new rows were processed and that no rows are duplicated.
**Tools:** Your dbt project from L07 and L08, DuckDB or PostgreSQL.
**Steps:**
1. Create `models/marts/fct_orders.sql` that selects from `{{ ref('stg_orders') }}`, with `materialized='incremental'`, `unique_key='order_id'` and a `dbt_loaded_at` column.
2. Filter new rows with `order_date > (select max(order_date) from {{ this }})` inside `is_incremental()`.
3. Run `dbt run --select stg_orders fct_orders` and count the rows (expected: 7).
4. Insert two new orders into `raw.orders`, for example `1009, C05, 2026-02-10, 18.00, delivered, MX` and `1010, C01, 2026-02-11, 22.50, delivered, KE`.
5. Run the same command twice. Count the rows after each run (expected: 9, then 9).
6. Run the duplicate check query and compare the `dbt_loaded_at` values.
**What good looks like:** The table has 9 rows after both runs, the duplicate check returns nothing, and only the two new orders have the newer `dbt_loaded_at` time. You can explain one way the filter could miss a late order.
**Time:** about 35 minutes

## Review Flags
- [VERSION] Incremental strategies and `unique_key` behaviour differ between adapters (dbt-postgres, dbt-duckdb) and releases; the YAML snapshot syntax (`relation`, `config`, `strategy: check`) is only available in recent dbt Core releases, and older releases use a Jinja `{% snapshot %}` block.
