# Screen Demo Pack: AI-17 L10 Documentation and Lineage

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L10_screen_1.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open models/marts/schema.yml (create it if needed)
2. Type the fct_borrower_features model description from content.md
3. Highlight: 'One row per borrower per feature_date'

**Narration over this clip (for pacing)**

> She opens the schema file in the marts folder. For the model, she writes the grain, one row per borrower per feature date, the rule that it uses only repayments before that date, and what it is used for.

## Clip 2: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L10_screen_2.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Type the borrower_id column description: internal ID from stg_borrowers, not a national ID
2. Type the late_payments_180d description from content.md
3. Add short descriptions for stg_repayments and stg_borrowers in models/staging/schema.yml

**Narration over this clip (for pacing)**

> Then she describes two columns. The borrower ID is an internal ID, not a national ID. And late payments in one hundred and eighty days counts instalments paid more than seven days late, in the hundred and eighty days before the feature date.

## Clip 3: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L10_screen_3.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Run: dbt docs generate
2. Run: dbt docs serve
3. In the browser, open fct_borrower_features and show the descriptions and column types

**Narration over this clip (for pacing)**

> She runs generate, then serve, and the site opens in her browser. She opens the feature table, and shows the descriptions and column types.

## Clip 4: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L10_screen_4.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Open the lineage graph view
2. Show raw.repayments → stg_repayments → fct_borrower_features and raw.borrowers → stg_borrowers → fct_borrower_features
3. Click stg_repayments and show its downstream models

**Narration over this clip (for pacing)**

> Now the lineage graph. Two paths lead into the feature table: raw repayments through staging repayments, and raw borrowers through staging borrowers. She clicks staging repayments to show every model downstream of it.

## Production notes for this lesson

- [VERSION] dbt docs generate and dbt docs serve behaviour (default port, browser opening) and the layout of the documentation site and lineage graph view must be checked against the current dbt Core release before recording.
- Priya and the microfinance lender in Pune, India are fictional; borrower data is invented. The borrower_id description stresses that it is not a national ID; keep that visible on screen.
- Screen lineage must show exactly: raw.repayments → stg_repayments → fct_borrower_features and raw.borrowers → stg_borrowers → fct_borrower_features.
