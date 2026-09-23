# L15 Preparing Datasets for Machine Learning

Course: AI-17 · Module: M4 · Objectives: O5, O6 · Video: 5 min (screen demo)

## Hook
You have a clean, tested feature table. It is still not ready for a model. How you split it, what personal data it still contains and what you tell people about it decide whether the model's test results can be trusted.

## Explanation
An **AI-ready dataset** has four properties:

1. **Clean and tested:** the quality checks from M3 pass.
2. **Split correctly:** the training data teaches the model; the test data checks it on rows it has never seen.
3. **Protected:** personal data is removed or reduced to what the use case needs.
4. **Documented and versioned:** a short datasheet describes it, and each exported version has a date or number.

**Splitting.** A random split mixes rows from all dates. That is acceptable when time does not matter. When the model predicts the future, such as next month's loan defaults, split **by time**: train on earlier feature dates, test on later ones. This copies real use, where the model is trained on the past and applied to the future. A random split lets the model learn from "future" rows and makes test results look better than they will be. If the label looks ahead, for example "default in the next 90 days", leave a gap between the last training date and the first test date so that training labels do not overlap the test period.

**Personal data.** Remove columns the model does not need, such as names and phone numbers. Replace IDs with a key made from a hash and a secret value (a "salt"), so rows can be joined without showing the original ID. This is pseudonymisation, not anonymisation: with the salt, the ID can be matched again. Rules on personal data in training datasets differ by country [REGION]. This lesson gives general guidance, not legal advice; check your organisation's rules.

**Datasheet.** A half-page document that answers: where the data comes from, what one row means, the time range, how it was split, known problems and limits, what it may and may not be used for, and who to contact.

**Analogy:** A time-based split is like a weather forecaster who tests a new method on last month's weather using only data from before last month. Testing it on days mixed from the whole year would let the method "remember" the answers.

## Worked Example
Mei Lin is a data engineer at a hypothetical consumer lender in Penang, Malaysia. Her feature table `loan_features` has one row per borrower per month, with `full_name`, `phone`, features and the label `defaulted_next_90d`.

On-screen steps:

1. In Python, connect to DuckDB and create a protected table:

```sql
CREATE TABLE ml_ready AS
SELECT md5(borrower_id || 'course-salt-2026') AS borrower_key,
       feature_date, loans_12m, late_payments_12m, defaulted_next_90d
FROM loan_features;
```

   In real use, the salt is a secret stored outside the code, not a value written in the SQL.
2. Export a time-based split as Parquet:

```sql
COPY (SELECT * FROM ml_ready WHERE feature_date <  DATE '2026-04-01')
  TO 'train.parquet' (FORMAT parquet);
COPY (SELECT * FROM ml_ready WHERE feature_date >= DATE '2026-04-01')
  TO 'test.parquet' (FORMAT parquet);
```

3. Check both files:

```sql
SELECT 'train' AS split, count(*), min(feature_date), max(feature_date) FROM 'train.parquet'
UNION ALL
SELECT 'test', count(*), min(feature_date), max(feature_date) FROM 'test.parquet';
```

On six invented rows, DuckDB returned `train | 3 | 2026-01-01 | 2026-03-01` and `test | 3 | 2026-04-01 | 2026-05-01`. No date appears in both files, and the name and phone columns are gone. Mei Lin notes one limit: training labels from March look 90 days ahead into the test period, so for the real dataset she will leave a gap.

4. She writes a datasheet: source (loan system, nightly), grain (one borrower per month), date range, split rule, personal data removed, known issues (few borrowers from rural branches), intended use (ranking borrowers for a friendly payment reminder, not for rejecting loans).

## Common Mistake
Many learners split randomly because it is the default in many machine learning tutorials. For a model that predicts the future, a random split puts later rows in training and earlier rows in testing, so the test score is too optimistic. Another mistake is to think that dropping the name column makes data anonymous. IDs, exact dates and rare combinations can still identify people. Never paste real personal records into AI chat tools to ask for help with a split.

## Key Takeaways
1. An AI-ready dataset is clean, split correctly, protected and documented with a datasheet.
2. When a model predicts the future, split by time, and leave a gap when labels look ahead.
3. Remove personal data the model does not need; hashing IDs is pseudonymisation, and rules differ by country.

## Hands-on Exercise
**Task:** Create a time-based train and test split of your feature table in DuckDB, export both as Parquet files, and write a half-page datasheet for the dataset.
**Tools:** Python 3 with DuckDB, your dbt project output, a text editor.
**Steps:**
1. Choose a date column for the split. If your feature table has only one feature date, split the order-level table `fct_orders` by `order_date` (for example before and after `2026-02-01`).
2. Remove or hash any column that could identify a person.
3. Export `train.parquet` and `test.parquet` with `COPY ... (FORMAT parquet)`.
4. Run the check query and confirm no date appears in both files.
5. Write a datasheet with: source, grain, date range, split rule, personal data handling, known issues, intended use and uses to avoid.
**What good looks like:** Two Parquet files with no overlapping dates, a check query with its real output, no direct identifiers, and a clear half-page datasheet that another person could use to decide whether the data fits their model.
**Time:** about 35 minutes

## Review Flags
- [REGION] Rules on personal data in training datasets differ by country; the lesson gives general guidance, not legal advice, and the pseudonymisation versus anonymisation wording should be reviewed for each target market.
- [VERSION] DuckDB's `md5` function, `COPY ... (FORMAT parquet)` and direct Parquet queries were tested with DuckDB 1.5.5; check them against the current release.
