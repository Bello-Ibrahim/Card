# L03 From Business Question to Data Question

Course: AI-08 · Module: M1 · Objectives: O5 · Video: 5 min

## Hook
"How is the shop doing?" is a question every owner asks. But if you type it into an AI tool with your sales sheet, you will get a long, general answer that does not help you decide anything. The problem is not the AI. The problem is the question.

## Explanation
Good analysis starts with a clear question. A **business question** is what you or your manager want to know, in everyday words: "Are we losing money?" or "Is the new menu working?" A **data question** is a question your spreadsheet can answer with a number.

To turn a business question into data questions, make each one measurable with four parts:

- **What to measure:** which number? Revenue, units, profit, number of customers, average order?
- **Which group:** all products, or one product? All shops, or one region?
- **Which time period:** last month, this quarter, January to April?
- **Compared with what:** the previous month, the same month last year, another product, a target?

The last part is the one people forget most often. "Revenue was 5,000 in March" means little alone. "Revenue was 5,000 in March, against 6,000 in February" tells you something.

Then check that your data can answer it. For each data question, name the **columns** you need. If a column does not exist, you either need more data or a different question. This step saves time: you find missing data before you start the analysis, not after.

A useful habit is to write the data questions before you open any AI tool. Then you can give the AI a precise question, and you can judge whether its answer is complete.

**Analogy:** A business question is like telling a taxi driver "Take me somewhere nice." A data question is like giving the exact address. Both start the journey, but only one gets you to a place you can check you have reached.

## Worked Example
Kwame runs a bakery in Accra, Ghana. He is worried: "My profits are falling." His fictional sales sheet has these columns: Month, Product, Units sold, Revenue (GHS) and Ingredient cost (GHS).

"Profits are falling" is a feeling, not yet a question. Kwame breaks it into three data questions:

1. **Is profit really falling, and since when?** Profit per month (Revenue minus Ingredient cost) for January to June, compared month by month. Columns: Month, Revenue, Ingredient cost.
2. **Is it all products or only some?** Profit per product per month, comparing each product's January with its June. Columns: Product, Month, Revenue, Ingredient cost.
3. **Is it fewer sales or higher costs?** Units sold per month compared with ingredient cost per unit (Ingredient cost divided by Units sold). Columns: Month, Units sold, Ingredient cost.

When he looks at the answers, he finds that total units are stable, but the ingredient cost per loaf of one bread type has risen since April. The worry "profits are falling" is now a specific finding he can act on: review the price or the recipe of one product.

Notice what Kwame did not ask: "Why are customers unhappy?" His sheet has no column about customer opinions, so that question needs different data.

## Common Mistake
Beginners often write data questions that are still vague, such as "Look at sales trends." Ask yourself: could two people answer this question and get the same number? If not, it is not yet measurable. Add the measure, the group, the time period and the comparison.

## Key Takeaways
1. A business question is what you want to know in everyday words; a data question can be answered with a number from your data.
2. Make each data question measurable: what to measure, which group, which time period, and compared with what.
3. Name the columns each data question needs, so you discover missing data before you start.

## Hands-on Exercise
**Task:** Write one business question and break it into 3 measurable data questions, naming the columns each one needs.
**Tools:** Pen and paper or Google Sheets (free). Optional: Claude or ChatGPT to comment on your questions.
**Steps:**
1. Use a question from your own work, or use this fictional café dataset and the question "Is the café making less money than before?"

| Month | Item | Units sold | Revenue | Ingredient cost |
|---|---|---|---|---|
| Jan | Coffee | 400 | 1200 | 400 |
| Jan | Pastry | 300 | 1200 | 600 |
| Feb | Coffee | 420 | 1260 | 420 |
| Feb | Pastry | 310 | 1240 | 620 |
| Mar | Coffee | 410 | 1230 | 410 |
| Mar | Pastry | 320 | 1280 | 960 |
| Apr | Coffee | 430 | 1290 | 430 |
| Apr | Pastry | 300 | 1200 | 900 |

2. Write 3 data questions. Each must include what to measure, which group, which time period and a comparison.
3. Next to each question, list the columns needed.
4. Optional: answer one question in Google Sheets with a simple formula, such as `=D9-E9` for pastry profit in April.
5. Optional: ask an AI tool, "Is each of these questions measurable? Suggest one improvement." Do not paste confidential business data into it.
**What good looks like:** Three specific questions, such as "What was profit (Revenue minus Ingredient cost) per item per month, January compared with April?" with columns Month, Item, Revenue and Ingredient cost. With the café data, this shows that coffee profit rose from 800 to 860, while pastry profit fell from 600 to 300 because ingredient cost per pastry went from 2 to 3 in March.
**Time:** about 20 minutes

## Review Flags
- None. The bakery and café cases and all figures are fictional, and no external facts need checking.
