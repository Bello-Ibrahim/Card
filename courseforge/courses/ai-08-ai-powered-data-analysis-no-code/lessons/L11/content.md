# L11 Checking AI Insights for Errors

Course: AI-08 · Module: M3 · Objectives: O6 · Video: 5 min

## Hook
The AI's answer is well written, uses exact numbers and sounds certain. Three of its four sentences are wrong or misleading. Would you notice before your manager did?

## Explanation
AI analysis errors follow a few common patterns:

- **Wrong column:** it reports units when you asked about revenue.
- **Ignored rows:** it skips blank or badly formatted rows, so counts and averages change.
- **Totals and averages mixed up:** it calls a total an average, or divides by the wrong count.
- **Invented cause:** it explains *why* something happened with information that is not in the data.
- **Trend from too little data:** it sees "strong growth" in three months, or in one large value.

A short **5-point checking routine** catches most of these:

1. **Recalculate one number** yourself with a formula or pivot table.
2. **Check row counts:** ask how many rows the AI used and compare with `=COUNTA()` on your sheet.
3. **Look at the chart:** plot the data and see whether one value drives the pattern.
4. **Ask "compared with what?":** is there a fair comparison, such as a previous period or another group?
5. **Look for other explanations:** is the cause in the data, or did the AI add it? Could a third factor or one unusual event explain it?

You do not need to check every sentence to the last decimal. But every number and claim you pass on to others should survive this routine.

**Analogy:** Checking AI insights is like checking a restaurant bill before you pay. You do not redo every sum, but you check the total, count the dishes, and ask about any item you did not order.

## Worked Example
Ingrid works in revenue management at a hotel in Bergen, Norway. She uploads a fictional, anonymised file of 200 bookings. The AI says: "The average stay is 3.5 nights. Guests from Germany stay longest, so the hotel should advertise in Germany."

She applies the routine. Row count: the AI used 188 rows. Twelve bookings, all long stays for a company contract, had a blank Nationality cell, and the AI dropped them. Her own `=AVERAGE()` over all 200 rows gives 3.8 nights. "Compared with what?": the German result is based on only 4 bookings, too few to support an advertising decision. Other explanations: the data has no information about advertising, so the recommendation is the AI's idea, not a finding. Ingrid reports the corrected average and marks the Germany point "needs more data".

## Common Mistake
Many learners check only whether the numbers are correct. But a sentence can use correct numbers and still mislead, through a missing comparison, a trend built on one value, or an invented cause. Check the reasoning as well as the arithmetic.

## Key Takeaways
1. Common AI errors are the wrong column, ignored rows, totals mixed with averages, invented causes and trends from too little data.
2. Use the 5-point routine: recalculate one number, check row counts, look at the chart, ask "compared with what?" and look for other explanations.
3. Correct numbers can still support a misleading conclusion, so check the reasoning too.

## Hands-on Exercise
**Task:** Review 4 AI-generated insights about the orders dataset, some with planted errors. Use the 5-point routine to find and correct the errors.
**Tools:** Google Sheets (free) with your pivot tables from L07. No AI tool is needed.
**Steps:**
1. Use your clean orders sheet (revenue in US dollars):

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

2. Read this fictional AI answer:

> 1. Total revenue for January to March 2026 was 3,450 dollars, and the average order was worth 383 dollars.
> 2. North is the strongest region, with total sales of 57.
> 3. Revenue grew strongly every month (470, 820 and 2,160 dollars). Demand is rising because more businesses are returning to their offices, so April will be even higher.
> 4. Office chairs brought in 2,640 dollars, about 77% of total revenue.

3. For each insight, apply the 5-point routine and write "correct", "wrong" or "misleading".
4. For each error, write the type of error and a corrected sentence.
**What good looks like:** Answer key. Insight 1: the total is correct, but the average is wrong (ignored row): 3,450 ÷ 9 = 383, but there are 10 orders, so the average is 345. Insight 2: wrong column: 57 is North's units. By revenue, South is strongest with 2,220 (North 680). Insight 3: numbers correct but misleading: order 1008 alone is 1,800 of March's 2,160; without it March is 360, lower than February. Three months is too little for a forecast, and "returning to offices" is an invented cause, because no column supports it. Insight 4: correct (2,640 ÷ 3,450 = 76.5%), though it also depends on order 1008. A good corrected summary: "Revenue was 3,450 from 10 orders (average 345). South led with 2,220, mostly from one order of 1,800."
**Time:** about 25 minutes

## Review Flags
- None. The hotel case, the orders dataset and the AI answer are fictional, and the planted errors are deliberate teaching material; all derived numbers were recalculated.
