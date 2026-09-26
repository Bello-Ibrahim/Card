# L15 Preparing Datasets for Machine Learning | Presenter Script

Course: AI-17 · Video: 5 min · Words: 727

## Hook
You have a clean, tested feature table. It is still not ready for a model. How you split it, what personal data it still contains, and what you tell people about it decide whether the model's test results can be trusted.

## Explain
Your pipeline now runs, retries and backfills by itself. In this lesson, you prepare its output for machine learning. An AI-ready dataset has four properties.

It is clean and tested, so your quality checks pass. It is split correctly into training data, which teaches the model, and test data, which checks it on rows it has never seen. It is protected, so personal data is removed or reduced. And it is documented and versioned.

Let's start with splitting. A random split mixes rows from all dates. That is fine when time does not matter. But when the model predicts the future, such as next month's loan defaults, split by time. Train on earlier dates, and test on later ones. This copies real use. A random split lets the model learn from future rows, so the test results look better than they will be.

If the label looks ahead, for example default in the next ninety days, leave a gap between the last training date and the first test date. Then training labels do not overlap the test period.

Next, personal data. Remove columns the model does not need, such as names and phone numbers. Replace IDs with a key made from a hash and a secret value, called a salt. Rows can still be joined, but the original ID is hidden. This is pseudonymisation, not anonymisation, because with the salt, the ID can be matched again. Rules differ by country, so check your organisation's rules.

A time-based split is like a weather forecaster who tests a new method on last month's weather, using only data from before last month. Testing it on days mixed from the whole year would let the method remember the answers.

## Demonstrate
Mei Lin is a data engineer at a consumer lender in Penang, Malaysia. Her feature table has one row per borrower per month, with the full name, the phone number, some features, and the label: default in the next ninety days.

In Python, she connects to DuckDB and creates a protected table. It hashes the borrower ID with a salt, and keeps only the feature date, two features and the label. The name and phone columns are gone. In real use, the salt is a secret stored outside the code.

Next, she exports a time-based split as Parquet files. Everything before the first of April goes to the training file, and everything from the first of April goes to the test file.

Then she checks both files with one query. On six invented rows, the training file has three rows, from January to March. The test file has three rows, from April to May. No date appears in both files.

She also notes one limit. The March labels look ninety days ahead, into the test period. So for the real dataset, she will leave a gap.

Last, she writes a short datasheet. It gives the source, what one row means, the date range, the split rule and the personal data removed. It lists known issues, such as few borrowers from rural branches. And it states the intended use: ranking borrowers for a friendly payment reminder, not rejecting loans.

Two common mistakes. The first is a random split for a model that predicts the future, which gives a test score that is too optimistic. The second is thinking that dropping the name makes data anonymous. IDs, exact dates and rare combinations can still identify people. And never paste real personal records into AI chat tools.

## Recap
Let's recap. First, an AI-ready dataset is clean, split correctly, protected and documented with a datasheet. Second, when a model predicts the future, split by time, and leave a gap when labels look ahead. Third, remove personal data the model does not need, and remember that hashing IDs is pseudonymisation.

## CTA
Now it is your turn. In the exercise, you create a time-based train and test split of your feature table in DuckDB, export both as Parquet files, and write a half-page datasheet. It takes about thirty-five minutes. After this, the capstone begins. Next lesson: Capstone Part One, Design and Ingest.

## Thumbnail
Headline: Ready for the Model?
Image: Navy background, a timeline split into a teal train block and an orange test block with a gap between them, headline in teal Inter Bold.

## Production Notes
- [REGION] Rules on personal data in training datasets differ by country; the lesson gives general guidance, not legal advice. Review the pseudonymisation versus anonymisation wording for each target market.
- [VERSION] DuckDB's md5 function, COPY ... (FORMAT parquet) and direct Parquet queries were tested with DuckDB 1.5.5; check against the current release.
- Screen output must match content.md exactly: train | 3 | 2026-01-01 | 2026-03-01 and test | 3 | 2026-04-01 | 2026-05-01, on six invented rows.
- The salt 'course-salt-2026' is written in the SQL for the demo only; show the caption that in real use the salt is a secret stored outside the code.
- Mei Lin and the consumer lender in Penang, Malaysia are fictional; all loan rows are invented. Do not show real personal data on screen.
