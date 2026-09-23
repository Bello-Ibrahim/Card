# Capstone Rubric: Build an ELT Pipeline to an AI-Ready Dataset

## Task
Build a working ELT pipeline that loads a public raw dataset, transforms it with dbt Core, tests its quality, runs on a schedule in Apache Airflow, and delivers a documented, AI-ready dataset. You design and load the data in L16 (capstone step 1), build and test the dbt layers in L17 (step 2), and orchestrate, document and present the pipeline in L18 (step 3). Use a public dataset whose licence allows your use, or the extended course sample. Do not load personal data, and do not paste raw data, passwords or connection details into AI tools.

## Deliverables
- A one-page pipeline design: use case and label, sources, layers with their grain, tests, schedule and output, with a reason for each design choice.
- Raw tables loaded unchanged into PostgreSQL or DuckDB, with a profile of row counts and known issues.
- A dbt Core project with staging, intermediate and mart models, and at least 8 tests including one singular test and one leakage check.
- An Airflow DAG that runs load, `dbt build`, documentation and export on a daily schedule, with retries and idempotent tasks, plus a screenshot of a successful run.
- Exported train and test Parquet files with a time-based split, and a half-page datasheet.
- The generated dbt documentation with its lineage graph, and a 3-minute recorded walkthrough.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Pipeline design and choices | O6 | The design covers all six sections, states the grain of every layer and gives a clear reason linked to reliability, cost or the AI use case for each choice (storage, full or incremental, schedule, format, split). | All six sections present, with reasons for most choices. | Some sections missing, or choices listed without reasons. | No design, or a design that does not match the pipeline. | 15 |
| Raw loading and dbt layers | O3, O7 | Raw data is loaded unchanged and profiled with real counts; staging, intermediate and mart models each have one clear job, use `source()` and `ref()`, and build without errors. | Raw load and three layers work, with small naming or structure issues. | Layers are mixed (for example cleaning and features in one model) or raw data was changed before loading. | Models do not build, or no dbt project. | 20 |
| Data quality tests | O5 | At least 8 tests across layers, including a singular business-rule test and a leakage check; each has a justified error or warn severity, and every warning is explained. | At least 8 tests across layers, mostly with sensible severities. | Fewer than 8 tests, or tests only on the final table. | No working tests. | 20 |
| Orchestration | O4 | The DAG runs the full pipeline on a schedule with correct dependencies, retries with a delay and idempotent tasks; a successful run and a safe rerun are shown. | The DAG runs the full pipeline with correct dependencies and retries. | The DAG runs only part of the pipeline, or tasks are not idempotent. | No working DAG. | 15 |
| AI-ready dataset and datasheet | O5, O6, O7 | Features use only data before the feature date; the time-based split has no overlapping dates and a gap where labels look ahead; personal data is removed or protected; the datasheet is complete and matches the files. | Correct time-based split and a mostly complete datasheet, with personal data handled. | Random split, unclear feature dates, or datasheet missing key parts. | No exported dataset, or clear leakage. | 20 |
| Documentation, lineage and walkthrough | O7 | Every model has a useful description, the lineage connects every source to the mart, and the 3-minute walkthrough clearly shows lineage, tests, one caught problem and a green run. | Most models documented and a clear walkthrough within time. | Few descriptions, gaps in lineage, or a walkthrough that is unclear or much too long. | No documentation or no walkthrough. | 10 |

Total: 100

## Submission Checklist
- My design page states the use case, the label, the grain of each layer and a reason for each design choice.
- I recorded the dataset's source, licence and download date, and I loaded no personal data.
- My raw tables are unchanged, and I recorded their row counts and known issues.
- My dbt project has staging, intermediate and mart models that build without errors.
- I have at least 8 tests, including one singular test and one leakage check, and I explained every warning.
- My Airflow DAG runs load, `dbt build`, docs and export in order, with retries, and my tasks are idempotent.
- My train and test files are split by time with no overlapping dates, and the datasheet numbers match them.
- My dbt documentation site shows lineage from every source to the final mart.
- My walkthrough is about 3 minutes and shows no passwords or personal data.
