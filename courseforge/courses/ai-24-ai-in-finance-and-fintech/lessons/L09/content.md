# L09 AI for Financial Analysis and Reporting

Course: AI-24 · Module: M2 · Objectives: O3 · Video: 5 min

## Hook
It is the last day of the quarter-end close. You have a profit-and-loss sheet, a budget and two hours to write the management commentary. An AI assistant can write a first draft in thirty seconds. Can you trust the numbers in it?

## Explanation
AI assistants are useful in finance teams for tasks built around text and structure:

- **Summarising** long documents, such as board packs, audit reports or credit memos.
- **Explaining variances** between actual results and budget, or between two periods, in clear sentences.
- **Drafting commentary** for management reports, in a set format and tone.
- **Checking consistency**, for example whether the commentary and the tables tell the same story.

The main risk is that language models are built to produce fluent text, not to calculate. They can:

- **Invent numbers** that are not in the source.
- **Misread numbers**, for example swapping two lines or reading thousands as millions.
- **Calculate wrongly**, especially percentages and differences.
- **Give a wrong reason** for a variance that sounds convincing.

So the rule in this course is simple: **every figure in AI-drafted commentary is checked against the source before it leaves the team.** Where possible, calculate the variances yourself in the spreadsheet first and give the AI the calculated table. Then its job is only to write the words, which is what it does best.

Two more rules apply. First, do not paste confidential company data, unpublished results or customer data into a public AI tool. Use synthetic or approved data, or a tool your institution has approved for that data. Second, commentary describes what happened. It must not turn into investment advice or a forecast presented as fact.

**Analogy:** An AI assistant is like a fast, eager junior analyst. The junior can produce a well-written draft in minutes, and the draft is often useful. But no experienced manager sends a junior's work to the board without checking every number, because a single wrong figure can damage trust in the whole report.

## Worked Example
Arjun Mehta is a finance analyst at Kaveri Home Appliances, a synthetic company in India. He gives an AI assistant the quarterly profit-and-loss summary (in thousands of rupees) and asks for variance commentary against budget.

| Line | Budget | Actual | Variance |
|---|---|---|---|
| Revenue | 12,000 | 11,400 | −600 (−5.0%) |
| Cost of goods sold | 7,200 | 7,068 | −132 (−1.8%) |
| Gross profit | 4,800 | 4,332 | −468 (−9.75%) |
| Operating expenses | 3,000 | 3,150 | +150 (+5.0%) |
| Operating profit | 1,800 | 1,182 | −618 (−34.3%) |

The AI's draft says: "Revenue fell 6% below budget. Gross margin improved thanks to lower cost of goods sold. Operating profit was 618 below budget, mainly because of higher operating expenses."

Arjun checks each figure.

- **"Revenue fell 6%"** is wrong. The shortfall is 600 on 12,000, which is 5.0%.
- **"Gross margin improved"** is wrong. Gross margin was 40.0% in the budget (4,800 ÷ 12,000) and 38.0% in the actual results (4,332 ÷ 11,400). Cost of goods sold fell less than revenue.
- **"618 below budget"** is correct, but the reason is wrong. Lower gross profit explains 468 of the 618. Higher operating expenses explain only 150.

His corrected commentary reads: "Revenue was 5.0% below budget. Gross margin fell from 40.0% to 38.0%, so gross profit was 468 below budget. Operating expenses were 150 above budget. Together, operating profit was 618 (34.3%) below budget."

## Common Mistake
Many analysts check only the numbers they expect to be wrong, or only the first paragraph. Errors in AI drafts often appear in the reasons and comparisons, not only in the raw figures. Check every number and every "because" against the source.

## Key Takeaways
1. AI assistants are good at summarising, explaining variances and drafting commentary in a set format.
2. Language models can invent, misread or miscalculate numbers and give convincing but wrong reasons, so every figure and every stated reason must be checked against the source.
3. Calculate variances in the spreadsheet first, use only synthetic or approved data, and keep commentary factual, with no investment advice.

## Hands-on Exercise
**Task:** Ask a free AI assistant for variance commentary on a synthetic quarterly profit-and-loss sheet, then check and correct every number.
**Tools:** Google Sheets (free); Claude or ChatGPT (free plan) [VERSION]; the course's synthetic quarterly profit-and-loss sheet.
**Steps:**
1. Open the synthetic profit-and-loss sheet in Google Sheets.
2. Add columns for variance (actual − budget) and variance percentage ((actual − budget) ÷ budget).
3. Copy the table without your variance columns into the AI assistant and ask: "Write five sentences of management commentary on the variances against budget."
4. Highlight every number and every reason in the AI's answer.
5. Check each one against your sheet and mark it "correct" or "wrong".
6. Rewrite the commentary with all errors corrected.
**What good looks like:** Every number in the draft is checked, each error is marked with the correct value, the stated reasons match the arithmetic, and the final commentary contains no forecasts or investment advice.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
