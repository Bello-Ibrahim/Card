# Screen Demo Pack: AI-17 L15 Preparing Datasets for Machine Learning

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L15_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open a Python session and connect to DuckDB
2. Run the CREATE TABLE ml_ready AS SELECT md5(borrower_id || 'course-salt-2026') AS borrower_key ... query from content.md
3. Caption: in real use the salt is a secret stored outside the code

**Narration over this clip (for pacing)**

> In Python, she connects to DuckDB and creates a protected table. It hashes the borrower ID with a salt, and keeps only the feature date, two features and the label. The name and phone columns are gone. In real use, the salt is a secret stored outside the code.

## Clip 2: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L15_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run COPY (SELECT * FROM ml_ready WHERE feature_date < DATE '2026-04-01') TO 'train.parquet' (FORMAT parquet)
2. Run COPY (SELECT * FROM ml_ready WHERE feature_date >= DATE '2026-04-01') TO 'test.parquet' (FORMAT parquet)

**Narration over this clip (for pacing)**

> Next, she exports a time-based split as Parquet files. Everything before the first of April goes to the training file, and everything from the first of April goes to the test file.

## Clip 3: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L15_screen_3.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Run the check query from content.md with UNION ALL over 'train.parquet' and 'test.parquet'
2. Show the output: train | 3 | 2026-01-01 | 2026-03-01 and test | 3 | 2026-04-01 | 2026-05-01

**Narration over this clip (for pacing)**

> Then she checks both files with one query. On six invented rows, the training file has three rows, from January to March. The test file has three rows, from April to May. No date appears in both files.

## Clip 4: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L15_screen_4.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Highlight the 2026-03-01 train row and the 90-day label window overlapping April
2. Add a note: real dataset needs a gap

**Narration over this clip (for pacing)**

> She also notes one limit. The March labels look ninety days ahead, into the test period. So for the real dataset, she will leave a gap.

## Clip 5: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L15_screen_5.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Open a new datasheet file in the editor
2. Fill in: source (loan system, nightly), grain (one borrower per month), date range, split rule, personal data removed
3. Add known issues (few borrowers from rural branches) and intended use (payment reminder ranking, not rejecting loans)

**Narration over this clip (for pacing)**

> Last, she writes a short datasheet. It gives the source, what one row means, the date range, the split rule and the personal data removed. It lists known issues, such as few borrowers from rural branches. And it states the intended use: ranking borrowers for a friendly payment reminder, not rejecting loans.

## Production notes for this lesson

- [REGION] Rules on personal data in training datasets differ by country; the lesson gives general guidance, not legal advice. Review the pseudonymisation versus anonymisation wording for each target market.
- [VERSION] DuckDB's md5 function, COPY ... (FORMAT parquet) and direct Parquet queries were tested with DuckDB 1.5.5; check against the current release.
- Screen output must match content.md exactly: train | 3 | 2026-01-01 | 2026-03-01 and test | 3 | 2026-04-01 | 2026-05-01, on six invented rows.
- The salt 'course-salt-2026' is written in the SQL for the demo only; show the caption that in real use the salt is a secret stored outside the code.
- Mei Lin and the consumer lender in Penang, Malaysia are fictional; all loan rows are invented. Do not show real personal data on screen.
