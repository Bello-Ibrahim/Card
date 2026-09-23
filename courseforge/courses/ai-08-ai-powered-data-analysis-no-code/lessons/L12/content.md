# L12 Capstone: Explore Your Dataset

Course: AI-08 · Module: M3 · Objectives: O5, O6 · Video: 5 min

## Hook
So far you have practised on a small, clean, fictional dataset. Now you choose real business data, with real questions and real mess. This week you will produce something you could show to a manager: a five-slide insight report built on findings you have checked yourself.

## Explanation
**The capstone brief.** Analyse a real business dataset with AI tools and present a five-slide insight report with charts, a clear recommendation and the limits of the analysis. You build it in three steps:

- **Step 1 (this lesson):** choose and clean a dataset, write 3 business questions, and record at least 5 checked findings in a findings log.
- **Step 2 (L13):** choose your main finding and plan a five-slide storyline.
- **Step 3 (L14):** build the slides and check every number.

The rubric gives points for your questions and data preparation, your analysis, how you checked the AI, your charts, and your story and recommendation. Read the full rubric on the course page before you start.

**Choosing a dataset.** You have two options:

1. **Your own work data, anonymised.** Follow L02: remove names, contact details and IDs, and check that your employer allows you to use the data for training and to upload it to an AI tool. If you are unsure, use option 2.
2. **A public sample dataset.** Possible sources include the UCI Machine Learning Repository (for example its "Online Retail" dataset), World Bank Open Data, Our World in Data, Kaggle, and your country's government open-data portal. Licences differ between sources and even between datasets on the same site, so read the licence and note it in your report. [VERIFY] [REGION]

A good capstone dataset has a few hundred to a few thousand rows, a date column, at least one number to measure (sales, visits, costs) and at least one group column (product, region, channel). Check the current file size limit of your AI tool. [VERSION]

**The findings log.** This is a simple table in Google Sheets where you record every finding as you work:

| No. | Question | Finding | How found | How checked | Result |
|---|---|---|---|---|---|
| 1 | Q1 | ... | AI prompt / pivot table | Recalculated with SUMIFS | Confirmed |

The "How checked" column uses the 5-point routine from L11. A finding that fails the check stays in the log, marked "rejected" with the reason. That record shows your judgement.

**Analogy:** A findings log is like a scientist's lab notebook. Each entry records what was tried, what was seen and how it was checked, so anyone can follow the work later, including you.

## Worked Example
Rahel is a sales supervisor for a fictional chain of three electronics shops in Addis Ababa, Ethiopia. She exports one year of sales, removes customer names and phone numbers, and checks with her manager that she may use the anonymised data.

Her business question is "Where should we focus next quarter?" She breaks it into three data questions: revenue by shop per month compared with the previous month; revenue by product category, this year's second half compared with the first half; and average basket value by weekday.

She cleans the file (two date formats, a duplicated week, and category names in two languages) and logs each fix. Then she asks the AI her first question with the four-part prompt from L06.

Her log after one session has 6 findings. Five are confirmed with pivot tables. One is rejected: the AI said "Saturday sales are highest because of payday", but the file has no payday information, and the Saturday total includes one large business order. She writes "rejected: invented cause, one-order effect" in the Result column.

## Common Mistake
Many learners choose a very large or complex dataset because it looks impressive, then spend all week cleaning it. Choose a dataset you can understand in 15 minutes. A simple dataset analysed carefully earns more than a complex one explored quickly.

## Key Takeaways
1. Choose anonymised work data you are allowed to use, or a public dataset whose licence you have read.
2. Write 3 measurable business questions before you start the analysis.
3. Record every finding in a findings log, including how you checked it and any finding you rejected.

## Hands-on Exercise
**Task:** Capstone step 1: choose your dataset, clean it, write 3 business questions, and record at least 5 checked findings in a findings log.
**Tools:** Google Sheets (free); Claude or ChatGPT with file analysis [VERSION]; a public data source if you do not use your own data.
**Steps:**
1. Choose your dataset. Note its source and licence, or confirm that you anonymised your own data and have permission.
2. Keep an untouched original. Clean a copy and keep a cleaning log (L04).
3. Write one business question and break it into 3 measurable data questions (L03), naming the columns.
4. Ask the AI each question with the four-part prompt (L06). Build pivot tables to compare (L07).
5. Record each finding in your findings log, with how you found it and how you checked it (L11).
6. Continue until you have at least 5 confirmed findings.
**What good looks like:** A clean dataset with a cleaning log; 3 measurable questions with named columns; a findings log with at least 5 confirmed findings, each with a specific check such as "SUMIFS matched: 12,480" or "row count 1,206 in both", plus any rejected findings with reasons.
**Time:** about 60 minutes

## Review Flags
- [VERIFY] Public dataset sources (UCI Machine Learning Repository, including the "Online Retail" dataset, World Bank Open Data, Our World in Data, Kaggle) must be checked for availability and licence terms before scripting; licences differ between datasets.
- [REGION] Government open-data portals and rules on using work data differ by country and employer.
- [VERSION] File size limits and file-analysis features in Claude and ChatGPT must be checked against the live tools.
