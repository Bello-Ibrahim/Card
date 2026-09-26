# L18 Capstone Part 3: Orchestrate, Document and Present | Presenter Script

Course: AI-17 · Video: 5 min · Words: 688

## Hook
A pipeline that only runs when you type commands is a prototype. A pipeline that runs every night, stops on bad data, explains itself and delivers a ready dataset is a product. Today, your capstone becomes a product.

## Explain
In step two, you built and tested your dbt layers. This last step has three pieces: orchestrate, document and present.

First, orchestrate. One Airflow DAG runs the whole pipeline in order. It loads the raw data for the logical date, runs the dbt build, generates the documentation and exports the dataset. Because the build stops on failed error tests, a bad load never reaches the export. Use retries with a delay, and keep every task idempotent, so a rerun is always safe.

Second, document. Generate the dbt documentation, and check that every model has a description, and that the lineage graph connects each source to the final mart. Then finish your datasheet with the real row counts, date range and split of your export. The numbers in the datasheet must match the files.

Third, present. Record a three-minute walkthrough for a colleague who did not build the pipeline. Spend half a minute on the use case and label, one minute on the lineage, forty-five seconds on the tests and a problem they caught, half a minute on the green Airflow run, and fifteen seconds on the files and the main limit.

The walkthrough is like handing over the keys of a house with its manual. You show where the water and electricity come in, which switch does what, and what to check when something stops working. The new owner should not need to call you.

## Demonstrate
Hana is a data engineer at a dairy cooperative near Addis Ababa, Ethiopia. Her capstone predicts tomorrow's milk collection at each collection centre, so the cooperative can send the right number of cooling trucks.

She opens her DAG file. It runs every day at two in the morning, with two retries, ten minutes apart. There are four bash tasks: load the raw data for the logical date, build with dbt, generate the docs, and export the split. The last line runs the load, then the build, and then the docs and the export side by side.

She triggers the DAG in the web interface. In the graph view, the load runs first, then the build, and then the docs and the export run in parallel.

In the build log, the summary line shows the passed tests and one expected warning. The output folder holds the training file, the test file and the datasheet. She checks the files with a count query, and the numbers match the datasheet.

Then she opens the dbt documentation site, and follows the lineage from the raw collections table to the centre features table.

Finally, she starts her screen recorder and gives the three-minute walkthrough, with the timing plan. She names one limit clearly. Two collection centres opened recently, so the model has little history for them, and their predictions need a human check.

A common mistake is to read code line by line and run out of time before showing the result. Show the lineage, the tests and a green run, and open code only to answer a specific question. The viewer needs to understand what the pipeline does, how it protects data quality, and how to check that it worked. Before recording, close any window with passwords or personal data.

## Recap
Let's recap. First, one Airflow DAG runs the full pipeline: load, build, documentation and export, with retries and idempotent tasks. Second, the build stops on failed error tests, so bad data never reaches your AI-ready dataset. Third, a short walkthrough of lineage, tests and a green run lets a colleague understand and trust your pipeline without you.

## CTA
Now it is your turn, for the last capstone step. Run your full pipeline from Airflow, export the dataset and the datasheet, and record your walkthrough. Then submit your project folder, your files, your design page and your recording, with the rubric's checklist. Congratulations on finishing Data Engineering for AI. You now build pipelines that AI can trust.

## Thumbnail
Headline: From Prototype to Product
Image: Navy background, an Airflow-style graph of four green task boxes, one branching into two, beside a play button for a walkthrough, headline in teal Inter Bold.

## Production Notes
- [VERSION] Airflow 3 imports (airflow.sdk, airflow.providers.standard) versus Airflow 2 imports, cron schedule strings, default_args, list dependencies and the graph view must be checked against the current Airflow release; dbt build and dbt docs generate behaviour must be checked against the current dbt Core release.
- [VERIFY] Screen recorder suggestion (OBS Studio) must be confirmed as still free and available for learners' operating systems; the voiceover only says a screen recorder.
- The DAG on screen is the exact milk_capstone.py from content.md, with the Airflow 2 import comments; it was checked to parse, not run.
- Before recording the demo, close any window that shows passwords, profiles or personal data.
- Hana and the dairy cooperative near Addis Ababa, Ethiopia are fictional.
