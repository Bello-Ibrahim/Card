# Screen Demo Pack: AI-17 L08 Building Marts and Feature Tables for AI

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L08_screen_1.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Open dbt_project.yml
2. Add: vars: feature_date: '2026-03-01'

**Narration over this clip (for pacing)**

> First, she adds a variable to the project file. The feature date is the first of March, twenty twenty-six.

## Clip 2: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L08_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Create models/marts/fct_customer_features.sql
2. Type the select list from content.md: customer_id, feature_date, recharges_90d, spend_90d_brl, last_recharge_date, days_since_last
3. Show from {{ ref('stg_recharges') }} and group by customer_id

**Narration over this clip (for pacing)**

> Next, she creates the feature model in the marts folder. For each customer, it counts recharges, adds up the spend, finds the last recharge date, and works out the days since that recharge.

## Clip 3: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L08_screen_3.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Highlight the where clause: recharge_date < feature_date and recharge_date >= feature_date - interval '90 days'
2. Highlight each {{ var("feature_date") }} reference

**Narration over this clip (for pacing)**

> The most important part is the filter. It keeps only recharges before the feature date, and within the ninety days before it. Both limits come from the same variable.

## Clip 4: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L08_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Run: dbt run --select fct_customer_features
2. Query the table and show the three rows exactly as in content.md
3. Highlight the M01 row: 3 | 70.0 | 2026-02-20 | 9

**Narration over this clip (for pacing)**

> She runs the model and queries the table. On eight invented recharges, it returns three rows, one per customer. Customer M one recharged three times, spent seventy reais, and last recharged nine days before the feature date.

## Clip 5: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L08_screen_5.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Show the stg_recharges rows for M01 on 2026-03-05 and M03 on 2026-03-10, greyed out and marked 'after feature date'
2. Cut to her notes: feature, formula, 90-day window, based on 2026-03-01

**Narration over this clip (for pacing)**

> But M one also recharged on the fifth of March, and M three on the tenth. Without the date filter, those recharges would enter the features, and recharged recently would perfectly predict did not churn. That is leakage. Juliana writes the feature date and window next to each column, so the data scientists know what each value means.

## Production notes for this lesson

- [VERSION] dbt vars syntax in dbt_project.yml and date arithmetic (date - date, interval '90 days') must be checked for the chosen adapter; the SQL was tested in DuckDB 1.5.5.
- Screen output must match content.md exactly: three rows, M01 | 2026-03-01 | 3 | 70.0 | 2026-02-20 | 9; M02 | 2026-03-01 | 1 | 10.0 | 2026-01-02 | 58; M03 | 2026-03-01 | 1 | 50.0 | 2026-02-27 | 2.
- Juliana and the prepaid mobile network in Recife, Brazil are fictional; the eight recharges are invented.
