# L06 Asking Good Questions of Your Data

Course: AI-08 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
Two people upload the same file to the same AI tool. One gets a vague paragraph that could describe any business. The other gets a clear table with exact numbers and a note on how they were calculated. The difference is not the tool. It is the prompt.

## Explanation
In L03 you learned to turn a business question into a measurable data question. Now you will put that data question into a prompt that an AI file-analysis tool can answer well. A strong analysis prompt has four parts:

1. **Describe the dataset.** What is it, how many rows, what period? "This file has 10 orders from January to March 2026, one row per order."
2. **Name the columns.** Say which columns to use and what they mean. "Revenue is in column G, in US dollars. Region is in column C."
3. **State the question.** Use the measure, group, period and comparison. "What was total Revenue per Region for January to March 2026?"
4. **Ask for the method.** "Show the table first. Then tell me how many rows you used, which columns you used, and how you calculated each number. Give your conclusion in no more than two sentences."

Asking for a **table first and conclusions second** is important. A table is easy to check against your own data. A paragraph of conclusions is easy to believe and hard to check.

Asking the AI to **show its method** helps you spot problems early. If it says it used 9 rows and your sheet has 10, you know something is wrong before you read any conclusion.

Keep one question per prompt when you start. Long prompts with five questions often produce answers where one part is skipped or mixed up.

Remember the safety rule from L02: upload only anonymised or fictional data, or data your organisation has approved for the tool.

**Analogy:** Asking AI about your data is like ordering at a busy counter. "Something to eat, please" gets you whatever is easiest to serve. "One vegetable soup, small, no bread, and the receipt" gets you exactly what you wanted, plus proof of what you paid for.

## Worked Example
Sofia is an operations analyst for a courier company in Mexico City. She uploads a fictional, anonymised file of deliveries with the columns Delivery ID, Date, Zone, Promised minutes and Actual minutes.

**First prompt:** "Are our deliveries late?"
**AI answer:** a general paragraph saying that "some deliveries appear to be delayed, especially at busy times" and suggesting that she "monitor performance". There are no numbers she can use.

**Second prompt:** "This file has one row per delivery for March 2026. A delivery is late when Actual minutes minus Promised minutes is more than 10. For each Zone, count the deliveries and the late deliveries, and give the percentage late. Show the table first. Then tell me how many rows you used and how you calculated each column. Conclusion in two sentences maximum."

**AI answer:** a table with one row per zone and the three numbers she asked for, a note that it used all rows in the file, and the formula it used for "late". The conclusion names the zone with the highest percentage late.

Sofia then checks the total row count against her sheet with `=COUNTA(A2:A5000)` and recalculates the percentage for one zone with a formula. Both match, so she can use the table in her weekly report.

## Common Mistake
Many learners ask for "insights" or "interesting patterns" and accept whatever comes back. The AI then chooses the measure, the group and the period for you, often without saying so, and its most confident sentence may be the least supported. Ask your own measurable question, and ask for the table and method before the conclusion.

## Key Takeaways
1. A strong analysis prompt describes the dataset, names the columns, states a measurable question and asks for the method.
2. Ask for a table first and conclusions second, because tables are easier to check than sentences.
3. Check the row count and columns the AI reports against your own sheet before you trust the conclusion.

## Hands-on Exercise
**Task:** Upload the cleaned orders dataset and ask 3 analysis questions using the four-part prompt structure. For each answer, note whether the AI showed its method.
**Tools:** Google Sheets (free); Claude or ChatGPT with file analysis. [VERSION] The data is fictional.
**Steps:**
1. Use your clean orders sheet from L04, which should match this table (revenue in US dollars):

| Order ID | Order Date | Region | Product | Units | Unit Price | Revenue |
|---|---|---|---|---|---|---|
| 1001 | 2026-01-08 | North | Notebook pack | 20 | 4 | 80 |
| 1002 | 2026-01-15 | South | Office chair | 2 | 120 | 240 |
| 1003 | 2026-01-22 | West | Desk lamp | 5 | 30 | 150 |
| 1004 | 2026-02-03 | North | Office chair | 3 | 120 | 360 |
| 1005 | 2026-02-11 | West | Notebook pack | 40 | 4 | 160 |
| 1006 | 2026-02-19 | South | Desk lamp | 6 | 30 | 180 |
| 1007 | 2026-02-26 | North | Desk lamp | 4 | 30 | 120 |
| 1008 | 2026-03-04 | South | Office chair | 15 | 120 | 1800 |
| 1009 | 2026-03-18 | West | Office chair | 2 | 120 | 240 |
| 1010 | 2026-03-25 | North | Notebook pack | 30 | 4 | 120 |

2. Download it as a .csv file and upload it to the AI tool.
3. Ask 3 questions, each as a separate four-part prompt: revenue by month, units by region, and average revenue per order by product.
4. For each answer, record: the numbers, the row count the AI reports, the columns it used, and whether it showed its method (yes, partly or no).
5. If it did not show its method, ask: "Which rows and columns did you use, and how did you calculate this?"
**What good looks like:** Revenue by month: January 470, February 820, March 2,160. Units by region: North 57, South 23, West 47. Average revenue per order: Notebook pack 120, Office chair 660, Desk lamp 150. Each answer uses 10 rows, and your notes show which answers included the method.
**Time:** about 25 minutes

## Review Flags
- [VERSION] File upload and analysis features in Claude and ChatGPT, including free plan limits, must be checked against the live tools before scripting.
