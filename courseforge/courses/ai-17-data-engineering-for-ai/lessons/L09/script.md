# L09 Incremental Models and Changing Data | Presenter Script

Course: AI-17 · Video: 5 min · Words: 689

## Hook
Your events table grows every day. On the first day, the model builds in seconds. A year later, it rebuilds the whole history every night, even though only yesterday's rows are new. Incremental models let dbt process only what changed.

## Explain
Last time, you built a feature table. So far, every model was rebuilt completely on each run. That is simple and safe, and it is the right default. But for large tables that only grow, it becomes slow, and on cloud warehouses, expensive.

An incremental model is built in full the first time. On later runs, dbt selects only new or changed rows, and adds them to the existing table. Two pieces of Jinja control this. The first is true when the table already exists and this is not a full refresh. The second refers to the existing table, so you can ask: what is my latest timestamp?

A unique key tells dbt which column identifies a row. If a row with the same key arrives again, dbt replaces it, instead of adding a duplicate.

A different problem is data that changes. A customer moves to a new city, and the source simply overwrites the old address. If a model needs to know where the customer lived in January, the history is gone. A dbt snapshot solves this. On every run, it compares the source with the last version, and keeps old versions with valid from and valid to dates.

The trade-off is complexity. Late rows can be missed, a wrong filter can create duplicates, and a change in logic only applies to new rows, until you run a full refresh.

Think of a phone book. A full rebuild reprints the whole book every day. An incremental model prints only the new pages and adds them to the binder. And a snapshot keeps the old pages when a number changes, stamped with the dates they were valid.

## Demonstrate
Let's try it. An is an analytics engineer at a language-learning app in Hanoi, Vietnam. The raw events table receives app events every day.

She creates an events model, and its first line sets the materialisation to incremental, with the event ID as the unique key. The model selects the event columns, casts the timestamp, and adds a column that records when dbt loaded each row.

Then the key part. Only on incremental runs, a filter keeps events newer than the latest timestamp already in the table.

The first run builds the full table, with three events. She inserts two new events for the next day, and runs the same command again. This time, only the two new rows are selected. A third run, with no new data, selects nothing.

Now she checks for duplicates, grouping by event ID and keeping any ID that appears more than once. The check returns no rows. The table has five rows and five distinct IDs, and the loaded at column shows that the first three rows kept their original load time.

An also tracks changes in user profiles with a snapshot. In recent dbt releases, it can be defined in YAML. It watches the country and plan columns, and she runs the snapshot command every day, before the models.

A common mistake is to make every model incremental from day one. On small tables, it saves nothing and adds risk. Start with full rebuilds. Switch only large, slow models, and add a small look-back window, such as the last three days, with a unique key.

## Recap
Let's recap. First, incremental models build the full table once, then process only new or changed rows. Second, a unique key prevents duplicates when rows arrive again, and snapshots keep the history of records that change. Third, incremental logic adds new ways to fail, so use it only for large, slow tables, and always test for duplicates.

## CTA
Now it is your turn. In the exercise, you will turn your orders mart into an incremental model, add two new orders, and run it twice. You should see seven rows, then nine, then nine again, with no duplicates. It takes about thirty-five minutes. Next lesson: Documentation and Lineage.

## Thumbnail
Headline: Only Process What Changed
Image: Navy background, a tall grey stack of existing rows with two new teal rows being added on top, headline in teal Inter Bold.

## Production Notes
- [VERSION] Incremental strategies and unique_key behaviour (merge, or delete and insert) differ between adapters (dbt-postgres, dbt-duckdb) and releases; the voiceover does not name a strategy.
- [VERSION] The YAML snapshot syntax (relation, config, strategy: check) is only available in recent dbt Core releases; older releases use a Jinja snapshot block. Check before recording the snapshot slide.
- Screen output must match content.md: first run 3 events, second run selects 2 rows, third run selects 0, final table 5 rows and 5 distinct event_id values, duplicate check returns no rows, first 3 rows keep their original dbt_loaded_at.
- An and the language-learning app in Hanoi, Vietnam are fictional; the events are invented.
