# L07 Summaries and Pivot Tables

Course: AI-08 · Module: M2 · Objectives: O4, O2 · Video: 5 min (screen demo)

## Hook
Your manager asks, "What is our average order in the South?" You answer 740 dollars. It sounds healthy. But two of the three South orders were under 250 dollars. The average was true, and still it told the wrong story.

## Explanation
A **summary by group** takes many rows and reduces them to a few numbers per group, such as per region or per month. The three most useful summaries are:

- **Total (sum):** how much in all. Total revenue per region.
- **Count:** how many rows. Number of orders per region.
- **Average (mean):** the total divided by the count. Average revenue per order.

The average is useful but can **hide important differences**. One very large value pulls the average up, so the "typical" order may be much smaller than the average. When you see an average, also look at the count and at the largest and smallest values. In Google Sheets, `=MEDIAN(G2:G11)` gives the middle value, which one large order affects much less.

A **pivot table** builds these summaries for you without formulas. In Google Sheets you choose which column goes in **Rows** (the groups), and which column goes in **Values** (the numbers, with SUM, COUNT or AVERAGE).

A good habit is to **compare the pivot table with the AI's own summary.** If they agree, you have more confidence. If they differ, the difference usually has a simple cause: the AI skipped a row, used a different column, or grouped dates in a different way. Finding that cause is part of the analysis.

**Analogy:** A pivot table is like sorting a pile of receipts into envelopes, first by month and then by shop, and writing the total on each envelope. The receipts do not change; you only arrange them so the totals are easy to read.

## Worked Example
Tomasz, a sales coordinator in Kraków, Poland, uses the fictional clean orders sheet (revenue in US dollars), plus the Month column from L05 in column H (not shown):

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

Presenter steps on screen:

1. Click any cell in the data. Choose **Insert > Pivot table**, select **New sheet** and click **Create**. [VERSION]
2. In the pivot table editor, next to **Rows**, click **Add** and choose **Region**.
3. Next to **Values**, click **Add** and choose **Revenue**. Check that it says **Summarise by: SUM**. [VERSION]
4. Read the result: North 680, South 2,220, West 550, Grand total 3,450.
5. Add **Revenue** to Values a second time and change it to **COUNTA** (the number of orders) and a third time to **AVERAGE**. North: 4 orders, average 170. South: 3 orders, average 740. West: 3 orders, average 183.33.
6. Create a second pivot table with **Month** in Rows and SUM of Revenue: 2026-01 470, 2026-02 820, 2026-03 2,160.
7. Upload the same sheet to the AI tool and ask: "Show total, count and average Revenue per Region in a table, and tell me how many rows you used."

In Tomasz's case, the AI's table shows South with a total of 420 and 2 orders. The pivot table shows 2,220 and 3 orders. He asks the AI which rows it used. It had read the Revenue value of order 1008 as text, because his exported file still had "1,800" in quotation marks, so it left that row out. He fixes the source file and the numbers match.

The South average of 740 comes mostly from one order of 1,800. The other two South orders were 240 and 180. The average alone hides this.

## Common Mistake
Many learners report only the average. An average without the count and the range can mislead, especially with a small number of rows or one very large value. Always show the count next to the average, and look at the individual rows when one group looks unusual.

## Key Takeaways
1. Summaries by group use totals, counts and averages, and a pivot table builds them without formulas.
2. An average can hide large differences; always check the count and the largest and smallest values.
3. Compare your pivot table with the AI's summary, and find the cause of any difference.

## Hands-on Exercise
**Task:** Build 2 pivot tables in Google Sheets (sales by region and by month), ask the AI for the same summary, compare the numbers and explain any difference.
**Tools:** Google Sheets (free); Claude or ChatGPT with file analysis. [VERSION] The data is fictional.
**Steps:**
1. Open your clean orders sheet with the Month column from L05.
2. Build a pivot table with Region in Rows and SUM, COUNTA and AVERAGE of Revenue in Values.
3. Build a second pivot table with Month in Rows and SUM of Revenue.
4. Upload the sheet to the AI tool and ask for the same two summaries as tables, with the number of rows used.
5. Put the two sets of numbers side by side. Mark each one "match" or "different".
6. For any difference, ask the AI which rows and columns it used, and write one sentence explaining the cause.
**What good looks like:** Region: North 680 (4 orders, average 170), South 2,220 (3 orders, average 740), West 550 (3 orders, average 183.33). Month: 470, 820 and 2,160, total 3,450. Every difference has a written cause, and you note that the South average depends on one large order.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Google Sheets pivot table steps (Insert > Pivot table, New sheet, the Rows and Values Add buttons, and the "Summarise by" options including COUNTA) must be checked against the current interface.
- [VERSION] File-analysis features in Claude and ChatGPT must be checked against the live tools before scripting.
