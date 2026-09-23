# L12 Testing Data with dbt

Course: AI-17 · Module: M3 · Objectives: O5, O3 · Video: 5 min (screen demo)

## Hook
In L11 you found problems by looking. That works once. Tomorrow a new file arrives, and nobody will look. dbt tests turn every problem you found into a check that runs automatically, every time.

## Explanation
A dbt test is a query that looks for bad rows. If the query returns zero rows, the test passes. If it returns rows, the test fails and dbt shows how many. There are two kinds:

**Generic tests** are ready-made and configured in YAML, next to the column descriptions from L10. dbt Core includes four:

- `unique`: no value appears twice (uniqueness).
- `not_null`: no value is missing (completeness).
- `accepted_values`: every value is in a list you give (validity).
- `relationships`: every value exists in another model, like a foreign key (consistency).

**Singular tests** are your own SQL files in the `tests/` folder. Each one selects the rows that break a business rule, such as "a shipment cannot leave before it is packed".

You also decide what a failure means. By default a failing test is an **error**. With `dbt build`, which runs and tests models in order, an error stops the models that depend on the failed one, so bad data does not reach the feature table. For less serious problems, set `severity: warn`: dbt reports the problem but continues. A good rule: use error for anything that would make the AI dataset wrong (duplicates, broken keys, impossible values), and warn for things a person should review (a small number of missing optional values).

Add-on packages, such as `dbt_utils`, provide more generic tests. The course only needs the built-in four [VERSION].

**Analogy:** Tests are like the smoke alarms in a building. You install them once, in the places where fire is most likely. After that you do not check each room every night; the alarm tells you when something is wrong.

## Worked Example
Mateo is a data engineer at a hypothetical coffee exporter in Medellín, Colombia. His staging model `stg_shipments` must be reliable before it feeds a model that predicts shipping delays.

On-screen steps:

1. Open `models/staging/schema.yml` and add tests [VERSION]:

```yaml
version: 2
models:
  - name: stg_shipments
    columns:
      - name: shipment_id
        data_tests: [unique, not_null]
      - name: shipment_status
        data_tests:
          - accepted_values:
              values: ['packed', 'shipped', 'delivered']
      - name: exporter_id
        data_tests:
          - relationships:
              to: ref('stg_exporters')
              field: exporter_id
      - name: bags
        data_tests:
          - not_null:
              config:
                severity: warn
```

2. Create `tests/assert_bags_positive_and_ship_after_pack.sql`:

```sql
select shipment_id, bags, packed_date, ship_date
from {{ ref('stg_shipments') }}
where bags <= 0
   or cast(ship_date as date) < cast(packed_date as date)
```

3. Run `dbt test --select stg_shipments`.
4. Show the results. On Mateo's three invented rows, the singular test returns 2 rows: shipment 502, shipped two days before it was packed, and shipment 503, with -5 bags (checked in DuckDB). The `accepted_values` test also fails, because shipment 503 has the status `pending`.
5. Discuss each failure with the business team. `pending` is a real status that was missing from the list, so Mateo adds it. The other two are data-entry errors, so he asks the source team to correct them and leaves the tests as errors.
6. Run `dbt build` and show that the feature table is skipped while an error test fails.

## Common Mistake
Many learners add tests only to the final table. When a test fails there, it is hard to know which step caused the problem. Test at every layer: keys and accepted values in staging, relationships between models, and business rules on the marts. Another mistake is to make a failing test pass by deleting it or changing it to warn without asking why it failed. A test should only change when the rule really changes.

## Key Takeaways
1. A dbt test is a query that returns bad rows; zero rows means the test passes.
2. Generic tests (`unique`, `not_null`, `accepted_values`, `relationships`) are set in YAML, and singular tests are SQL files for business rules.
3. Decide on purpose which failures stop the pipeline (error) and which only report (warn), and test at every layer.

## Hands-on Exercise
**Task:** Add at least 6 tests to your project, including one custom test for a business rule. Break the data on purpose so that one test fails, then fix it.
**Tools:** Your dbt project with `stg_orders`, `fct_orders` and `fct_customer_features`; dbt Core; DuckDB or PostgreSQL.
**Steps:**
1. In `schema.yml`, add `unique` and `not_null` to `stg_orders.order_id`.
2. Add `accepted_values` for `order_status` with `delivered`, `cancelled` and `returned`.
3. Add `not_null` with `severity: warn` to `amount_usd`, and `unique` to `customer_id` in the feature table.
4. Write a singular test that finds orders with a negative amount or an order date in the future.
5. Run `dbt test`. The warning for the missing amount of order 1006 is expected.
6. Insert a raw order with the status `lost`, rebuild with `dbt build`, and show the failing test.
7. Fix it in the right place (remove the invented row, or add the status if the business confirms it), then run `dbt build` until all error tests pass.
**What good looks like:** At least 6 tests across 2 layers, one singular test, a screenshot of one deliberate failure and a clean final run, plus one sentence on why you chose error or warn for each test.
**Time:** about 35 minutes

## Review Flags
- [VERSION] dbt test syntax changes between releases: the `data_tests:` key (older releases use `tests:`), the placement of `values`, `to` and `field` (newer releases may expect them under an `arguments:` key), `severity` configuration and add-on packages such as `dbt_utils` must be checked against the current dbt Core release and adapter.
