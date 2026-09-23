# L02 ETL, ELT, Batch and Streaming

Course: AI-17 · Module: M1 · Objectives: O1, O2 · Video: 5 min

## Hook
Two pipelines deliver the same sales data. One transforms it before it reaches the warehouse; the other loads it first and transforms it later. Both work. So why does most modern analytics work, including this course, choose the second one?

## Explanation
**ETL** means Extract, Transform, Load. Data is taken from a source, cleaned and reshaped on a separate server, and only the finished result is loaded into the warehouse. ETL was common when warehouse storage and computing were expensive, so teams stored only what they needed.

**ELT** means Extract, Load, Transform. Raw data is loaded into the warehouse first, exactly as it arrived, and then transformed there with SQL. ELT has three advantages for AI work:

- You keep the raw data, so you can rebuild any table when a rule changes or a bug is found.
- Transformations are SQL inside the warehouse, so analysts and engineers can read, review and test them.
- A new feature for a model can be built from raw data that is already loaded, without asking for a new extract.

This course uses ELT: load raw data into PostgreSQL or DuckDB (M1), then transform it with dbt Core (M2).

The second choice is timing. A **batch** pipeline processes a group of records on a schedule, for example every night at 02:00 or every hour. A **streaming** pipeline processes each event within seconds of its arrival, using a continuous flow of messages. Streaming is useful when a late answer has no value, such as blocking a fraudulent card payment. It also needs more infrastructure and is harder to test. Most AI training data is prepared in batches, because a model retrained every day or week does not need second-by-second updates. In this course all hands-on work is batch; streaming is a concept only.

Finally, where does the data live?

- A **data warehouse** stores structured tables and is designed for SQL analytics. PostgreSQL can act as a small warehouse, and DuckDB acts as one on your laptop.
- A **data lake** stores files of any type (CSV, Parquet, JSON, images, logs) in cheap storage. It holds more variety, but it needs extra tools to query and control it.

Many teams use both: raw files land in a lake, and cleaned tables live in a warehouse.

**Analogy:** ETL is like a restaurant that cooks every meal in a central kitchen and delivers only finished plates; if a customer wants a change, the kitchen must start again. ELT is like delivering fresh ingredients to a well-equipped kitchen in each restaurant, where cooks can prepare new dishes whenever they need them. Batch is the daily delivery truck; streaming is a conveyor belt that never stops.

## Worked Example
Aigerim is a data analyst at a hypothetical logistics company in Almaty, Kazakhstan. She reviews three data needs:

| Need | Choice | Reason |
|---|---|---|
| Weekly model that predicts parcel volume per depot | Batch, ELT | The model retrains once a week; raw scans are loaded nightly and transformed in the warehouse |
| Alert when a refrigerated truck goes above 8 °C | Streaming | A warning two hours late could mean spoiled goods |
| Monthly on-time delivery report for managers | Batch, ELT | A daily or monthly run is enough, and analysts want to change the definition of "on time" later |

For the parcel-volume model, Aigerim explains why ELT helps. Last month the team changed the rule for "delivered" to exclude parcels left with a neighbour. Because the raw scan data was already in the warehouse, she changed one SQL model and rebuilt two years of history in one run. With ETL she would have needed a new extract from the source system.

## Common Mistake
Many learners believe streaming is always better because "real time is faster". Speed has a cost: more components, harder testing and harder recovery after failures. Ask one question first: "If this answer arrives one hour later, does anyone lose value?" If the answer is no, choose batch. A reliable nightly batch is worth more than a fragile real-time system.

## Key Takeaways
1. ETL transforms data before loading it; ELT loads raw data first and transforms it inside the warehouse, which keeps raw data available for rebuilds.
2. Batch pipelines run on a schedule; streaming pipelines process events as they arrive, which is only worth the extra effort when minutes matter.
3. Warehouses hold structured tables for SQL analytics, while lakes hold raw files of any type; many teams use both.

## Hands-on Exercise
**Task:** Classify 6 scenarios as batch or streaming, and explain one choice in a sentence.
**Tools:** Pen and paper, or any notes app.
**Steps:**
1. Read the scenarios (all hypothetical): (a) nightly sales reports for a supermarket chain in Kenya; (b) card fraud alerts for a bank in Brazil; (c) a weekly demand forecast for a bakery in Poland; (d) live seat availability for a bus company in Mexico; (e) a monthly churn model for a gym chain in Australia; (f) a warning when a factory machine in Vietnam overheats.
2. Label each one "batch" or "streaming".
3. For each batch scenario, write how often it should run (hourly, daily, weekly).
4. Choose one scenario and write one sentence that explains your choice using the question "does an hour's delay lose value?"
5. Compare your labels with the answer key on the course page.
**What good looks like:** (b), (d) and (f) are labelled streaming; (a), (c) and (e) are labelled batch with a sensible schedule. Your sentence links the choice to the cost of a delay.
**Time:** about 15 minutes

## Review Flags
- None. Streaming is covered at concept level only, as agreed in the curriculum, and all examples are hypothetical.
