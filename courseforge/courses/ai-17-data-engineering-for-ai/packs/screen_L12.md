# Screen Demo Pack: AI-17 L12 Testing Data with dbt

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L12_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open models/staging/schema.yml
2. Type the stg_shipments tests from content.md: unique and not_null on shipment_id
3. Add accepted_values ['packed', 'shipped', 'delivered'] on shipment_status
4. Add relationships to ref('stg_exporters') on exporter_id, and not_null with severity warn on bags

**Narration over this clip (for pacing)**

> He opens the staging schema file. The shipment ID must be unique and not null. The status must be packed, shipped or delivered. The exporter ID must exist in the exporters model. And a missing number of bags only gives a warning.

## Clip 2: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L12_screen_2.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Create tests/assert_bags_positive_and_ship_after_pack.sql
2. Type the select from content.md: where bags <= 0 or ship_date < packed_date

**Narration over this clip (for pacing)**

> Next, a singular test for a business rule. It selects any shipment with zero or fewer bags, or a ship date before the packed date.

## Clip 3: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L12_screen_3.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Run: dbt test --select stg_shipments
2. Show the singular test failing with 2 rows: shipment 502 and shipment 503
3. Show accepted_values failing on shipment 503 with status 'pending'

**Narration over this clip (for pacing)**

> He runs the tests for the shipments model. On his three invented rows, the singular test finds two bad rows. Shipment five o two was shipped two days before it was packed, and shipment five o three has minus five bags. The accepted values test also fails, because shipment five o three has the status pending.

## Clip 4: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L12_screen_4.mp4`
- **Target length:** about 20 seconds

**Steps**

1. In schema.yml, add 'pending' to the accepted_values list
2. Leave the singular test unchanged, severity error
3. Caption: 502 and 503 sent back to the source team

**Narration over this clip (for pacing)**

> Mateo discusses each failure with the business team. Pending is a real status that was missing from the list, so he adds it. The other two are data entry errors, so he asks the source team to correct them, and he leaves the tests as errors.

## Clip 5: scene 13

- **Filename:** `ai-17-data-engineering-for-ai_L12_screen_5.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Run: dbt build
2. Highlight the failing test and the downstream feature table marked as skipped

**Narration over this clip (for pacing)**

> Finally, he runs build. While the error test fails, the feature table is skipped. Bad rows never reach the model.

## Production notes for this lesson

- [VERSION] dbt test syntax changes between releases: the data_tests: key (older releases use tests:), the placement of values, to and field (newer releases may expect them under an arguments: key), severity configuration and add-on packages such as dbt_utils must be checked against the current dbt Core release and adapter before recording.
- Screen output must match content.md: the singular test returns 2 rows (shipment 502 shipped two days before packing, shipment 503 with -5 bags); accepted_values fails on shipment 503 with status 'pending'.
- Mateo and the coffee exporter in Medellín, Colombia are fictional; the three shipment rows are invented.
