# Capstone Rubric: Clean and Explore a Real Public Dataset

## Task
Build a data-cleaning and exploration notebook in Google Colab (or Jupyter with VS Code) on a real public dataset. Choose a dataset with a clear licence, write a question, audit the data, clean it with a justified cleaning log, explore it with labelled charts, and finish with an ML-ready table. The notebook must run from top to bottom without errors after a restart. You start in L19 (choose, load and audit) and finish in L20 (clean, explore and document). Do not use datasets that contain personal information about identifiable people, and do not upload confidential data from your job.

## Deliverables
- A shared Colab link (view access) or a GitHub copy of the notebook.
- In the notebook, in this order: Question; Source (name, web address, download date, licence); Load; Audit with a problem list; Cleaning with a cleaning log table; Exploration with at least 3 labelled charts and one insight sentence each; ML-ready table; Limits.
- The ML-ready CSV file saved by the notebook (target column plus numeric features).

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Loading and working with the data | O4 | Data loads with clear code; selection, filtering, sorting and group summaries are used correctly and support the question. | Data loads and pandas operations are mostly correct and relevant. | Data loads, but pandas operations are few, incorrect in places or not linked to the question. | Data does not load or pandas is not used. | 15 |
| Data-quality audit | O5 | Reusable audit code checks missing values, duplicates, types, category spellings, impossible values and outliers; every problem is listed with the code that found it. | Most checks are done and problems are listed with code. | Some checks are done, but problems are missing or not backed by code. | No audit. | 20 |
| Cleaning decisions and log | O6 | Every problem has an action and a clear, specific justification, including costs such as lost rows; shapes are printed after each step and the audit is run again. | Most decisions are logged with reasonable justifications. | Cleaning is done, but the log is incomplete or reasons are vague. | No cleaning, or cleaning with no log. | 20 |
| Exploration with charts | O5 | At least 3 suitable chart types, each with title, axis labels and units, and an accurate insight sentence that does not claim a cause. | 3 charts with labels and mostly accurate insights. | Fewer than 3 charts, or charts are unlabelled or poorly matched to the question. | No charts. | 15 |
| ML-ready table | O6 | One row per example, one target, only numeric features, no missing values; identifiers and leaky columns removed with reasons; CSV saved. | Table is mostly ML-ready, with reasons for most removed columns. | Table still has text, missing values or unexplained removals. | No ML-ready table. | 15 |
| Reproducible, documented notebook | O7 | Runs from top to bottom after a restart without errors; includes assert checks; source, licence and limits are recorded; readable names and text cells throughout. | Runs after a restart with minor issues; source and licence recorded. | Needs manual steps to run, or source, licence or limits are missing. | Does not run, or cannot be opened from the shared link. | 15 |

Total: 100

## Submission Checklist
- My dataset is public, I recorded its source, web address, download date and licence, and the licence allows my use.
- My data contains no personal information about identifiable people and no confidential data from my job.
- My notebook has a clear question in the first text cell.
- My audit lists every problem with the code that found it.
- My cleaning log gives a reason for every decision, and I ran the audit again after cleaning.
- I made at least 3 labelled charts, each with one insight sentence.
- My ML-ready table has one target, only numeric features and no missing values, and I explained each removed column.
- I added a Limits section.
- I restarted the session and ran all cells without errors before sharing.
- I tested my shared link from another account or a private browser window, or I shared a GitHub copy.
