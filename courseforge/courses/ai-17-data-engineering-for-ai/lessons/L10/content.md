# L10 Documentation and Lineage

Course: AI-17 · Module: M2 · Objectives: O2 · Video: 5 min (screen demo)

## Hook
A data scientist asks: "Where does `days_since_last` come from, and does it include cancelled orders?" If the answer is only in your memory, every question interrupts you, and when you leave the team the answer leaves with you.

## Explanation
Documentation in dbt lives next to the code. You add a `description` to each model and to its important columns in a YAML file, usually the same `schema.yml` file where tests will go (L12). Because descriptions sit in the project, they are reviewed and versioned with the SQL, and they change when the SQL changes.

dbt then generates a **documentation site** with two commands:

- `dbt docs generate` reads the project and the database and writes a catalogue of every model, column, type and description.
- `dbt docs serve` starts a small local web server and opens the site in your browser [VERSION].

The site includes the **lineage graph**, also called the DAG (directed acyclic graph). It shows every source and model as a box, with arrows that follow the `source()` and `ref()` calls. You did not draw this graph; dbt built it from your code. That is why using `ref()` instead of written table names matters.

Lineage helps in two directions:

- **Upstream:** a number in a feature table looks wrong. Follow the arrows back to see which staging model and which source it came from.
- **Downstream:** a source is about to change a column. Follow the arrows forward to see every model, and every consumer, that will be affected.

Good descriptions are short and specific. Say what one row means (the grain), the unit of each number, the time window of each feature and anything a reader might misunderstand, such as "excludes cancelled orders".

**Analogy:** Lineage is like the family tree printed at the front of a long novel. When a character appears in chapter 20, you check the tree to see who their parents are. You do not need to reread the whole book.

## Worked Example
Priya is an analytics engineer at a hypothetical microfinance lender in Pune, India. Loan officers ask many questions about her feature table, so she documents it.

On-screen steps:

1. Open `models/marts/schema.yml` (create it if it does not exist) and add:

```yaml
version: 2
models:
  - name: fct_borrower_features
    description: >
      One row per borrower per feature_date. Built only from
      repayments before feature_date. Used to train the
      late-repayment model.
    columns:
      - name: borrower_id
        description: Internal borrower ID from stg_borrowers. Not a national ID.
      - name: late_payments_180d
        description: >
          Number of instalments paid more than 7 days late in the
          180 days before feature_date. Source: stg_repayments.
```

2. Add short descriptions for `stg_repayments` and `stg_borrowers` in `models/staging/schema.yml`.
3. Run `dbt docs generate`, then `dbt docs serve`.
4. In the browser, open `fct_borrower_features` and show the descriptions and column types.
5. Open the lineage graph view [VERSION]. Show the arrows: `raw.repayments` → `stg_repayments` → `fct_borrower_features`, and `raw.borrowers` → `stg_borrowers` → `fct_borrower_features`.
6. Click `stg_repayments` and show its downstream models.

Priya then answers the loan officers' question in three sentences: "`late_payments_180d` comes from `raw.repayments`, which we receive every night from the loan system. `stg_repayments` converts the due and paid dates to DATE and removes test loans. The feature table counts instalments paid more than 7 days late in the 180 days before the feature date."

## Common Mistake
Many learners write descriptions that repeat the column name, such as "late_payments_180d: late payments in 180 days". That adds nothing. A useful description answers the questions a new reader would ask: what counts as late, which dates are included, what the unit is and where the value comes from. Another mistake is to document once and forget: update descriptions in the same change as the SQL.

## Key Takeaways
1. dbt descriptions live in YAML next to the models, so documentation is versioned and reviewed with the code.
2. `dbt docs generate` and `dbt docs serve` build a documentation site with a lineage graph created from `source()` and `ref()`.
3. Lineage lets you trace a value upstream to its source and see which models downstream a change will affect.

## Hands-on Exercise
**Task:** Document 3 models and their key columns, generate the documentation site, and use the lineage graph to explain in 3 sentences where one feature column comes from.
**Tools:** Your dbt project with `stg_orders`, `fct_customer_features` and `fct_orders`; dbt Core; a web browser.
**Steps:**
1. Add a `schema.yml` file for your staging and mart folders.
2. Write a description for each of the 3 models, including its grain.
3. Describe at least 3 key columns per model, with units and time windows.
4. Run `dbt docs generate` and `dbt docs serve`.
5. Open the lineage graph and take a screenshot.
6. Choose one feature column and write 3 sentences: its source, the staging step and the calculation.
**What good looks like:** Every described model shows its description on the site, the lineage graph connects `raw.orders` to your marts, and your 3 sentences trace one feature from source to mart without gaps.
**Time:** about 30 minutes

## Review Flags
- [VERSION] `dbt docs generate` and `dbt docs serve` behaviour (default port, browser opening) and the layout of the documentation site and lineage graph view must be checked against the current dbt Core release.
