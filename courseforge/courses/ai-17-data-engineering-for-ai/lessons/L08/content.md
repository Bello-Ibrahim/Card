# L08 Building Marts and Feature Tables for AI

Course: AI-17 · Module: M2 · Objectives: O3, O6 · Video: 5 min (screen demo)

## Hook
A churn model gets an excellent score in testing and fails in its first month of real use. The data was clean and the code had no bugs. The problem was one column: it quietly used information from after the date the model was supposed to predict.

## Explanation
**Marts** are the final layer of a dbt project. They join and aggregate staging models into tables that answer a business question, such as "revenue per store per month". A mart has a clear grain (L04) and a name that says what it holds, for example `fct_orders` or `dim_customers`.

A **feature table** is a special mart for machine learning. It has:

- **One row per entity** at a given date, such as one row per customer on 1 March.
- **Feature columns** that describe the entity, such as number of purchases in the last 90 days or days since the last login.
- A **feature date** (also called a cut-off or snapshot date): the moment the prediction would be made.
- Often a **label** column, the thing to predict, calculated from events *after* the feature date.

The golden rule is: **features may only use data from before the feature date.** If a feature uses events after that date, the model learns from the future. This is **data leakage**. It makes test results look excellent and real results poor, because in real use the future is not available.

Keep the feature date in one place, not repeated in every model. dbt **variables** do this: define `feature_date` in `dbt_project.yml` and read it with `{{ var('feature_date') }}`.

**Analogy:** Building features is like preparing a student for an exam using only lessons taught before the exam date. If the practice test includes the real exam answers, the student's practice score is perfect, but it tells you nothing about how they will really do.

## Worked Example
Juliana is a data engineer at a hypothetical prepaid mobile network in Recife, Brazil. The data science team wants to predict which customers will stop recharging in March 2026. Her staging model `stg_recharges` has one row per recharge: `customer_id`, `recharge_date` and `amount_brl`.

On-screen steps:

1. In `dbt_project.yml`, add:

```yaml
vars:
  feature_date: '2026-03-01'
```

2. Create `models/marts/fct_customer_features.sql`:

```sql
select
    customer_id,
    date '{{ var("feature_date") }}'                        as feature_date,
    count(*)                                                as recharges_90d,
    sum(amount_brl)                                         as spend_90d_brl,
    max(recharge_date)                                      as last_recharge_date,
    date '{{ var("feature_date") }}' - max(recharge_date)   as days_since_last
from {{ ref('stg_recharges') }}
where recharge_date <  date '{{ var("feature_date") }}'
  and recharge_date >= date '{{ var("feature_date") }}' - interval '90 days'
group by customer_id
```

3. Run `dbt run --select fct_customer_features`.
4. Query the table and show one row per customer.

We ran the compiled SQL in DuckDB on eight invented recharges. It returned three rows:

```text
M01 | 2026-03-01 | 3 | 70.0 | 2026-02-20 |  9
M02 | 2026-03-01 | 1 | 10.0 | 2026-01-02 | 58
M03 | 2026-03-01 | 1 | 50.0 | 2026-02-27 |  2
```

Customer M01 also recharged on 5 March, and M03 on 10 March. Without the line `recharge_date < feature_date`, those recharges would enter the features, and "recharged recently" would perfectly predict "did not churn". Juliana writes the feature date and the 90-day window next to each column in her notes, so the data scientists know exactly what each value means.

## Common Mistake
Many learners build features from the whole table "because more data is better", or they compute a customer's total spend over all time and join it to a training row dated months earlier. Both mix future information into the past. For every feature, ask: "Would I know this value on the feature date?" If the answer is no, filter the source rows by date first.

## Key Takeaways
1. Marts join and aggregate staging models into tables that answer questions; a feature table is a mart with one row per entity at a feature date.
2. Features may only use data from before the feature date; using later data is leakage and makes test results falsely good.
3. Store the feature date once, for example as a dbt variable, and document which date and window each feature is based on.

## Hands-on Exercise
**Task:** Build a mart that aggregates your data to one row per entity with at least 4 useful feature columns, and write down the date each feature is based on.
**Tools:** Your dbt project with `stg_orders` from L07, dbt Core, DuckDB or PostgreSQL.
**Steps:**
1. Choose the entity (for the course sample: one row per customer) and a feature date, for example `2026-02-01`.
2. Add `feature_date` to `vars` in `dbt_project.yml`.
3. Create `models/marts/fct_customer_features.sql` that selects from `{{ ref('stg_orders') }}` and filters to orders before the feature date.
4. Add at least 4 features, such as order count, total amount, number of cancelled orders and days since the last order.
5. Run the model and check that each customer appears once.
6. Write a small table: feature name, formula, time window, date it is based on.
**What good looks like:** One row per customer, at least 4 features, no order on or after the feature date used, and a feature table that explains each column's time window.
**Time:** about 35 minutes

## Review Flags
- [VERSION] dbt `vars` syntax in `dbt_project.yml` and date arithmetic (`date - date`, `interval '90 days'`) must be checked for the chosen adapter; the SQL was tested in DuckDB 1.5.5, and PostgreSQL also returns an integer number of days for `date - date`.
