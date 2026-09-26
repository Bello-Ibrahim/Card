# L17 Capstone Part 2: Transform and Test | Presenter Script

Course: AI-17 · Video: 5 min · Words: 693

## Hook
Your raw data is loaded, and your problems are listed. This step turns that list into a pipeline. Every problem becomes either a cleaning rule or a test, and every layer has a clear job.

## Explain
In capstone step one, you designed your pipeline and loaded the raw data. Now you build the dbt project, in the three layers you already know.

Staging has one model per raw table. It renames, casts, removes exact duplicates and tests rows, with no joins. Intermediate models join and reshape staging models into useful building blocks, such as one row per delivered shipment with its label. Learners often skip this layer, but it keeps marts short and lets two marts share the same logic.

The mart is the final feature table, with one row per entity per feature date. Its features use only data from before that date.

Then add tests at each layer, with the checklist from week three. Would this problem make the AI dataset wrong? Then make it an error, so the build stops before the mart. Does a person need to review it, but the data is still usable? Make it a warning. Is it a business rule, not a column rule? Write a singular test.

Run the build command often. It builds and tests each model in dependency order, so you find each problem in the layer where it starts.

Layers with tests are like the checkpoints in a car factory. The engine is tested before it goes into the car, and the car is tested before it leaves the factory. A fault found at the engine check costs much less than a fault found by the customer.

## Demonstrate
Yusuf is a data analyst at a logistics company in Istanbul, Türkiye. His capstone predicts whether a shipment will arrive later than promised.

He shows his project tree: one staging model for shipments, one intermediate model that adds the label, and one mart for the shipment features.

He opens the intermediate model. It reads the staging model, calculates the promised hours between pick-up and the promised time, and marks a shipment as late when it was delivered after the promised time. It keeps only delivered shipments.

On four invented shipments, the compiled query in DuckDB returns three rows. S one has twenty-seven promised hours and is not late. S two has thirty-two hours and is late. S three has twenty-eight hours and is not late. S four has no delivery time yet, so it has no label and stays out of training.

The mart has one row per shipment at pick-up time. Its features include the promised hours, the vehicle type, and the late rate on the same route in the thirty days before pick-up.

In the schema file, he shows his test plan. Staging has unique and not null IDs, accepted vehicle types, and a warning for missing delivery times. Intermediate has a unique ID and a singular test for delivery before pick-up. The mart checks the label, and has a leakage test for route features.

He runs the build. One warning appears, for the missing delivery time of S four, as expected. Every error test passes.

A common mistake is to write all the logic in one large mart. When a test fails, nobody can see which part caused it. Keep each model short, with one job. And do not paste your raw data into an AI tool for test ideas. Describe the columns instead.

## Recap
Let's recap. First, build staging, intermediate and mart models, each with one clear job and one clear grain. Second, turn every known problem into a cleaning rule or a test, and choose error or warn with the week three checklist. Third, run the build often, so each problem is caught in the layer where it starts.

## CTA
Now it is your turn. This is capstone step two. Build staging, intermediate and mart models for your dataset, with at least eight tests, including one singular test and one leakage check. Make every test pass, and explain each warning. It takes about seventy-five minutes. Next lesson: Capstone Part Three, Orchestrate, Document and Present.

## Thumbnail
Headline: Every Problem Becomes a Test
Image: Navy background, three stacked layer bars labelled staging, intermediate and mart, each with a small test badge, headline in teal Inter Bold.

## Production Notes
- [VERSION] dbt build behaviour (skipping downstream models after a failed test), test severity settings and interval arithmetic with extract(epoch from ...) must be checked for the current dbt Core release and for both adapters (dbt-postgres, dbt-duckdb); the SQL was tested with DuckDB 1.5.5.
- Screen output must match content.md exactly: on four invented shipments the intermediate model returns three rows, S1 (27 promised hours, not late), S2 (32 hours, late), S3 (28 hours, not late); S4 has no delivery time and is left out.
- Show Yusuf's test plan table from content.md on screen; the final dbt build shows one expected warning for S4's missing delivery time and every error test passing.
- Yusuf and the logistics company in Istanbul, Türkiye are fictional; the shipments are invented.
