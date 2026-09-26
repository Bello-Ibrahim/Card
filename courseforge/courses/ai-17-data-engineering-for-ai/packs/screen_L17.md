# Screen Demo Pack: AI-17 L17 Capstone Part 2: Transform and Test

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L17_screen_1.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Show the project tree: models/staging/stg_shipments.sql
2. models/intermediate/int_shipments_labelled.sql
3. models/marts/fct_shipment_features.sql

**Narration over this clip (for pacing)**

> He shows his project tree: one staging model for shipments, one intermediate model that adds the label, and one mart for the shipment features.

## Clip 2: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L17_screen_2.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open int_shipments_labelled.sql and show the model from content.md
2. Highlight promised_hours, is_late and where delivered_at is not null

**Narration over this clip (for pacing)**

> He opens the intermediate model. It reads the staging model, calculates the promised hours between pick-up and the promised time, and marks a shipment as late when it was delivered after the promised time. It keeps only delivered shipments.

## Clip 3: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L17_screen_3.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Run the compiled SQL in DuckDB
2. Show three rows: S1 27 false, S2 32 true, S3 28 false
3. Caption: S4 has no delivery time, so no label

**Narration over this clip (for pacing)**

> On four invented shipments, the compiled query in DuckDB returns three rows. S one has twenty-seven promised hours and is not late. S two has thirty-two hours and is late. S three has twenty-eight hours and is not late. S four has no delivery time yet, so it has no label and stays out of training.

## Clip 4: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L17_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open fct_shipment_features.sql
2. Highlight features: promised_hours, vehicle_type, 30-day route late rate before pick-up, label is_late

**Narration over this clip (for pacing)**

> The mart has one row per shipment at pick-up time. Its features include the promised hours, the vehicle type, and the late rate on the same route in the thirty days before pick-up.

## Clip 5: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L17_screen_5.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Open schema.yml
2. Show the test plan table from content.md: staging, intermediate and mart tests with their severity
3. Highlight the warn on delivered_at and the leakage singular test in the mart

**Narration over this clip (for pacing)**

> In the schema file, he shows his test plan. Staging has unique and not null IDs, accepted vehicle types, and a warning for missing delivery times. Intermediate has a unique ID and a singular test for delivery before pick-up. The mart checks the label, and has a leakage test for route features.

## Clip 6: scene 14

- **Filename:** `ai-17-data-engineering-for-ai_L17_screen_6.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Run: dbt build
2. Show one warning for S4's missing delivered_at and all error tests passing

**Narration over this clip (for pacing)**

> He runs the build. One warning appears, for the missing delivery time of S four, as expected. Every error test passes.

## Production notes for this lesson

- [VERSION] dbt build behaviour (skipping downstream models after a failed test), test severity settings and interval arithmetic with extract(epoch from ...) must be checked for the current dbt Core release and for both adapters (dbt-postgres, dbt-duckdb); the SQL was tested with DuckDB 1.5.5.
- Screen output must match content.md exactly: on four invented shipments the intermediate model returns three rows, S1 (27 promised hours, not late), S2 (32 hours, late), S3 (28 hours, not late); S4 has no delivery time and is left out.
- Show Yusuf's test plan table from content.md on screen; the final dbt build shows one expected warning for S4's missing delivery time and every error test passing.
- Yusuf and the logistics company in Istanbul, Türkiye are fictional; the shipments are invented.
