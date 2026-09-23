# L02 ETL, ELT, Batch and Streaming | Presenter Script

Course: AI-17 · Video: 5 min · Words: 715

## Hook
Two pipelines deliver the same sales data. One transforms it before it reaches the warehouse. The other loads it first and transforms it later. Both work. So why does most modern analytics work, including this course, choose the second one?

## Explain
In the last lesson, we mapped sources, pipelines, storage and consumers. Today we look at two choices every pipeline makes: when to transform the data, and how often to move it.

ETL means extract, transform, load. Data is taken from a source, cleaned and reshaped on a separate server, and only the finished result is loaded into the warehouse. ETL was common when warehouse storage and computing were expensive, so teams stored only what they needed.

ELT means extract, load, transform. Raw data is loaded into the warehouse first, exactly as it arrived, and then transformed there with SQL.

ELT has three advantages for AI work. You keep the raw data, so you can rebuild any table when a rule changes. Transformations are SQL that people can read, review and test. And a new feature for a model can be built from data that is already loaded. This course uses ELT, with PostgreSQL or DuckDB for loading, and dbt Core for transforming.

The second choice is timing. A batch pipeline processes a group of records on a schedule, for example every night at two in the morning. A streaming pipeline processes each event within seconds of its arrival.

Streaming is useful when a late answer has no value, such as blocking a fraudulent card payment. But it needs more infrastructure and is harder to test. Most AI training data is prepared in batches, because a model retrained every day or week does not need second by second updates. In this course, all hands-on work is batch, and streaming is a concept only.

Finally, where does the data live? A data warehouse stores structured tables for SQL analytics. A data lake stores files of any type, such as CSV, Parquet, JSON, images or logs, in cheap storage. Many teams use both: raw files land in a lake, and cleaned tables live in a warehouse.

Here is a picture to remember. ETL is a central kitchen that delivers only finished plates. If a customer wants a change, the kitchen starts again. ELT delivers fresh ingredients to a kitchen in each restaurant, where cooks can prepare new dishes whenever they need them.

And batch is the daily delivery truck, while streaming is a conveyor belt that never stops.

## Demonstrate
Let's apply this. Aigerim is a data analyst at a logistics company in Almaty, Kazakhstan. She reviews three data needs.

First, a weekly model that predicts parcel volume per depot. The model retrains once a week, so she chooses batch and ELT. Second, an alert when a refrigerated truck goes above eight degrees. A warning two hours late could mean spoiled goods, so that one is streaming. Third, a monthly on-time delivery report. Batch and ELT are enough.

For the parcel volume model, ELT really helps. Last month, the team changed the rule for delivered, to exclude parcels left with a neighbour. Because the raw scan data was already in the warehouse, Aigerim changed one SQL model and rebuilt two years of history in one run. With ETL, she would have needed a new extract from the source system.

A common mistake is to believe streaming is always better, because real time sounds faster. Speed has a cost: more parts, harder testing and harder recovery. Ask one question first. If this answer arrives one hour later, does anyone lose value? If not, choose batch.

## Recap
Let's recap. First, ETL transforms data before loading it, while ELT loads raw data first and transforms it inside the warehouse, which keeps raw data for rebuilds. Second, batch runs on a schedule, and streaming processes events as they arrive, which is only worth it when minutes matter. Third, warehouses hold structured tables, lakes hold raw files, and many teams use both.

## CTA
Now try it yourself. In the exercise below this video, you will label six scenarios as batch or streaming, from nightly sales reports in Kenya to card fraud alerts in Brazil, and explain one choice. It takes about fifteen minutes. Next, we get hands-on: Setting Up PostgreSQL and Loading Raw Data.

## Thumbnail
Headline: Transform First or Later?
Image: Navy background, two pipeline arrows: one with a gear before the warehouse, one with the gear inside it, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags are None and all examples are hypothetical.
- Streaming is a concept only in this course, as agreed in the curriculum: do not show streaming tools or code on screen.
- Aigerim and the logistics company in Almaty, Kazakhstan are fictional; stock footage must show no real company names or logos.
