# L17 Capstone Part 2: Transform and Test

Course: AI-17 · Module: M4 · Objectives: O3, O5, O7 · Video: 5 min (screen demo)

## Hook
Your raw data is loaded and your problems are listed. This step turns that list into a pipeline: every problem becomes either a cleaning rule or a test, and every layer has a clear job.

## Explanation
Build the dbt project in the three layers you know:

- **Staging** (`stg_`): one model per raw table. Rename, cast, remove exact duplicates and test rows. No joins.
- **Intermediate** (`int_`): join and reshape staging models into useful building blocks, such as "one row per delivered shipment with its label". Learners often skip this layer, but it keeps marts short and lets two marts share the same logic.
- **Mart** (`fct_` or `mart_`): the final feature table, one row per entity per feature date, with features built only from data before that date (L08).

Then add tests at each layer, using the week 3 checklist:

1. **Would this problem make the AI dataset wrong?** Duplicated IDs, broken keys, impossible values, rows after the feature date. Make it an **error**, so `dbt build` stops before the mart.
2. **Does a person need to review it, but the dataset is still usable?** A few missing optional values, an unusual but possible value. Make it a **warning**.
3. **Is it a business rule, not a column rule?** Such as "delivered after pick-up". Write a **singular test**.

Run `dbt build` often. It builds and tests each model in dependency order, so you find a problem in the layer where it starts.

**Analogy:** Layers with tests are like the checkpoints in a car factory. The engine is tested before it goes into the car, and the car is tested before it leaves the factory. A fault found at the engine check costs much less than a fault found by the customer.

## Worked Example
Yusuf is a data analyst at a hypothetical logistics company in Istanbul, Türkiye. His capstone predicts whether a shipment will arrive later than promised.

On-screen steps:

1. Show the project tree: `models/staging/stg_shipments.sql`, `models/intermediate/int_shipments_labelled.sql`, `models/marts/fct_shipment_features.sql`.
2. Open the intermediate model:

```sql
select
    shipment_id,
    origin,
    destination,
    vehicle_type,
    picked_up_at,
    extract(epoch from (promised_at - picked_up_at)) / 3600 as promised_hours,
    delivered_at > promised_at                               as is_late
from {{ ref('stg_shipments') }}
where delivered_at is not null
```

On four invented shipments, the compiled SQL in DuckDB returned three rows: S1 (27 promised hours, not late), S2 (32 hours, late) and S3 (28 hours, not late). Shipment S4 had no delivery time yet, so it has no label and is left out of training.

3. Explain the mart in words: one row per shipment at pick-up time, with features such as promised hours, vehicle type, and the late rate on the same route in the 30 days before pick-up. The label is `is_late`.
4. Open `schema.yml` and show his test plan:

| Layer | Test | Severity |
|---|---|---|
| staging | `unique`, `not_null` on `shipment_id` | error |
| staging | `accepted_values` on `vehicle_type` | error |
| staging | `not_null` on `delivered_at` | warn |
| intermediate | `unique` on `shipment_id` | error |
| intermediate | singular: `delivered_at` before `picked_up_at` | error |
| mart | `not_null` on `is_late` | error |
| mart | singular: no route feature uses shipments after pick-up | error |

5. Run `dbt build`. One warning appears for S4's missing delivery time, as expected; every error test passes.

## Common Mistake
Many learners write all the logic in one large mart, with joins, cleaning and features in 200 lines of SQL. When a test fails, nobody can see which part caused it, and the same cleaning is copied into the next mart. Keep each model short with one job, and put tests on the layer where a problem first appears. Also, do not paste your raw data into an AI tool to ask for test ideas; describe the columns instead.

## Key Takeaways
1. Build staging, intermediate and mart models, each with one clear job and one clear grain.
2. Turn every known problem into a cleaning rule or a test, and choose error or warn with the week 3 checklist.
3. Run `dbt build` often, so each problem is caught in the layer where it starts.

## Hands-on Exercise
**Task:** Capstone step 2: build staging, intermediate and mart models for your dataset, with at least 8 tests, and make every test pass.
**Tools:** dbt Core with dbt-duckdb or dbt-postgres, your raw tables from L16, a code editor.
**Steps:**
1. Declare every raw table as a source.
2. Build one staging model per source, following L07.
3. Build at least one intermediate model that creates the label or joins sources.
4. Build the mart: one row per entity per feature date, with at least 4 features and the label.
5. Write a test plan table like Yusuf's, then add at least 8 tests, including one singular test and one leakage check.
6. Run `dbt build` and fix each failure at its source; change a test only when the rule itself was wrong.
7. Record the final `dbt build` summary and explain each remaining warning in one sentence.
**What good looks like:** Three layers with clear names and grains, at least 8 tests across the layers, a final `dbt build` with no errors, and a short note for every warning.
**Time:** about 75 minutes

## Review Flags
- [VERSION] `dbt build` behaviour (skipping downstream models after a failed test), test severity settings and interval arithmetic with `extract(epoch from ...)` must be checked for the current dbt Core release and for both adapters (dbt-postgres, dbt-duckdb); the SQL was tested with DuckDB 1.5.5.
