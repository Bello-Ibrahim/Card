# Screen Demo Pack: AI-17 L09 Incremental Models and Changing Data

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L09_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Create models/marts/fct_events.sql
2. Type the config line: materialized='incremental', unique_key='event_id'
3. Type the select of event_id, user_id, event_type, event_ts and current_timestamp as dbt_loaded_at from the raw events source, as in content.md

**Narration over this clip (for pacing)**

> She creates an events model, and its first line sets the materialisation to incremental, with the event ID as the unique key. The model selects the event columns, casts the timestamp, and adds a column that records when dbt loaded each row.

## Clip 2: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L09_screen_2.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Type the if is_incremental() block with: where event_ts > (select max(event_ts) from {{ this }})
2. Highlight the whole block

**Narration over this clip (for pacing)**

> Then the key part. Only on incremental runs, a filter keeps events newer than the latest timestamp already in the table.

## Clip 3: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L09_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run: dbt run --select fct_events  (full build: 3 events)
2. Insert 2 new events for the next day into raw.events
3. Run the same command again: 2 rows selected
4. Run it a third time: 0 rows selected

**Narration over this clip (for pacing)**

> The first run builds the full table, with three events. She inserts two new events for the next day, and runs the same command again. This time, only the two new rows are selected. A third run, with no new data, selects nothing.

## Clip 4: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L09_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Run the duplicate check from content.md: select event_id, count(*) from main.fct_events group by event_id having count(*) > 1;
2. Show: no rows returned
3. Run select * from main.fct_events; show 5 rows and highlight dbt_loaded_at on the first 3

**Narration over this clip (for pacing)**

> Now she checks for duplicates, grouping by event ID and keeping any ID that appears more than once. The check returns no rows. The table has five rows and five distinct IDs, and the loaded at column shows that the first three rows kept their original load time.

## Production notes for this lesson

- [VERSION] Incremental strategies and unique_key behaviour (merge, or delete and insert) differ between adapters (dbt-postgres, dbt-duckdb) and releases; the voiceover does not name a strategy.
- [VERSION] The YAML snapshot syntax (relation, config, strategy: check) is only available in recent dbt Core releases; older releases use a Jinja snapshot block. Check before recording the snapshot slide.
- Screen output must match content.md: first run 3 events, second run selects 2 rows, third run selects 0, final table 5 rows and 5 distinct event_id values, duplicate check returns no rows, first 3 rows keep their original dbt_loaded_at.
- An and the language-learning app in Hanoi, Vietnam are fictional; the events are invented.
