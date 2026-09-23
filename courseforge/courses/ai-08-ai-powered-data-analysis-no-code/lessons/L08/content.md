# L08 Trends, Outliers and Correlation

Course: AI-08 · Module: M2 · Objectives: O2, O5 · Video: 5 min

## Hook
Revenue in March was more than four times revenue in January. Is the business growing fast? Or did one customer place one very large order? The same number can tell two very different stories.

## Explanation
Three ideas help you find patterns, and each one has a trap.

**Trend.** A trend is the general direction of a number over time: up, down or flat. To read a trend, look at many periods, not two. Three months of data can show a direction, but it is weak evidence. Also check whether one period is unusual: a single large value can create a "trend" that disappears when you look closer.

**Outlier.** An outlier is a value far from the others, such as one order ten times larger than usual. Outliers have three common causes:

- **A data error:** 45 was typed instead of 450.
- **A real but rare event:** a bulk order, a festival, a system outage.
- **A sign of change:** the first of many large orders from a new type of customer.

Never delete an outlier just because it is unusual. **Ask why it exists first.** Fix it if it is an error. If it is real, keep it, and report results with and without it so readers see its effect.

**Correlation versus causation.** Two numbers are **correlated** when they tend to move together. That does not mean one **causes** the other. Here is a hypothetical case: in a coastal town, ice-cream sales and sunburn cases rise and fall together over the year. Ice cream does not cause sunburn. Both follow a third factor: hot, sunny weather. When AI says "X leads to Y", ask: could a third factor explain both? Could it be a coincidence in a small dataset? Could the direction be reversed?

AI tools find outliers and correlations quickly but explain them less carefully. They may call a normal value an outlier, or describe a correlation as a cause. Your job is to ask "why?" and "how could I check?"

**Analogy:** Reading data is like reading footprints in sand. A long line of steps shows a direction: a trend. One very deep print is an outlier; ask what made it. Two lines of prints side by side do not mean one person followed the other. Both may have walked to the same café.

## Worked Example
Fatou runs three ice-cream kiosks in Dakar, Senegal. She asks an AI tool to analyse her fictional weekly sales sheet for 12 weeks.

The AI reports:

1. **A rising trend:** weekly sales grew from about 300 cups in week 1 to about 450 in week 12. Fatou checks with a line chart. The rise is steady over many weeks, not caused by one value, so she accepts it as a trend.
2. **Two outliers:** 900 cups in week 7 and 45 cups in week 10. She does not delete them. She asks why. Week 7 was the week of a local festival next to one kiosk: a real event, so she keeps it and notes it. Week 10 does not match her till records, which show 450. It was a typing error, so she corrects it.
3. **A correlation:** the AI notes that her sales rise in the same weeks as sunburn cases reported by a nearby clinic (also fictional), and says "higher sales are linked to sunburn". Fatou recognises the third factor: hot weather drives both. The useful finding for her business is the link between temperature and sales, which she can check against weather records.

## Common Mistake
Many learners remove every outlier to make the chart look tidy. This can remove the most important finding. The opposite mistake is to build a whole conclusion on one outlier. Investigate first, then report with and without the unusual value.

## Key Takeaways
1. A trend needs many periods; check whether one unusual value creates or hides it.
2. Ask why an outlier exists before you remove it: fix errors, keep real events, and report their effect.
3. Correlation does not prove causation; look for a third factor, coincidence or reversed direction.

## Hands-on Exercise
**Task:** Use AI to find the 3 largest outliers and one trend in the orders dataset. For each, write a possible cause and how you could check it.
**Tools:** Google Sheets (free); Claude or ChatGPT with file analysis. [VERSION] The data is fictional.
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

2. Upload it and ask: "Which 3 orders are the most unusual, and why? Show the values you compared." Then ask: "What is the trend in total Revenue by month? Show the monthly totals."
3. For each outlier, write: is it really unusual, a possible cause, and one way to check the cause.
4. Calculate the monthly totals with and without order 1008 using `=SUMIFS(G2:G11, H2:H11, "2026-03")` and a hand subtraction.
5. Write one sentence about the trend that you would be comfortable sharing with a manager.
**What good looks like:** Order 1008 (15 chairs, 1,800) is the clear outlier, perhaps a bulk order for a new office; check with the sales team. Orders 1005 (40 units) and 1010 (30 units) are large by units but small by revenue, so they are not real revenue outliers. Monthly revenue is 470, 820 and 2,160, but March without 1008 is only 360, and three months is too little data. A good trend sentence: "Revenue rose from January to March, but most of March came from one large order."
**Time:** about 25 minutes

## Review Flags
- [VERSION] File-analysis features in Claude and ChatGPT must be checked against the live tools before scripting.
