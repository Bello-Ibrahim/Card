# L09 Choosing and Building the Right Chart

Course: AI-08 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
A colourful 3D pie chart with nine slices looks impressive on a slide. Ask the audience which slice is the biggest, and half of them will guess wrong. A good chart is not the most attractive one. It is the one that makes the message obvious in five seconds.

## Explanation
Start with the message, then choose the chart. Ask: "What do I want the reader to see?"

- **Change over time** (revenue by month): use a **line chart**. Time goes on the horizontal axis, from left to right.
- **Comparison between groups** (revenue by region or product): use a **bar or column chart**. Sort the bars from largest to smallest so the order is easy to read.
- **Parts of a whole** (share of revenue by channel): a bar chart usually still works better. A **pie chart** is only readable with two or three slices of clearly different sizes.
- **Relationship between two numbers** (units and revenue): use a **scatter chart**.

Avoid **3D effects**. They distort the size of bars and slices, so the reader sees differences that are not in the data. Also avoid too many colours: use one colour, and a second colour only to highlight the point you want to make.

Start the value axis of a bar chart at **zero**. If it starts higher, small differences look huge.

**Write a title that states the finding**, not just the topic. "Revenue by region" is a topic. "South brought in most of the revenue" is a finding. The reader gets the message even if they only read the title.

AI can help you choose. Describe the question and the columns, and ask: "Which chart type best shows this, and why? Suggest a title that states the finding." Then build the chart yourself in Google Sheets, so it uses your checked data:

1. Select the columns you need (for a summary, select a pivot table from L07).
2. Choose **Insert > Chart**. [VERSION]
3. In the **Chart editor**, on the **Setup** tab, choose the chart type. [VERSION]
4. On the **Customise** tab, open **Chart and axis titles** and type your finding as the title. [VERSION]

**Analogy:** Choosing a chart is like choosing a way to give directions. For a route through a city, you draw a map. For "turn left at the bank", a single sentence is enough. The best format depends on what the other person needs to understand, not on which format looks most impressive.

## Worked Example
Mei Lin is a marketing analyst for a fictional online bookshop in Kuala Lumpur, Malaysia. Her report has a 3D pie chart of revenue by book category, with nine slices and the title "Q2 Revenue".

She describes the data to an AI tool and asks for a better chart. The AI suggests a sorted horizontal bar chart, because there are nine categories to compare and the labels are long. It suggests the title "Children's books brought in the most revenue in Q2".

Mei Lin builds it in Google Sheets from her pivot table. She sorts the categories from largest to smallest, removes the 3D effect, uses one colour for all bars and a stronger colour for the children's books bar. Before she uses the AI's title, she checks the pivot table: children's books really are first, so the title is correct.

She also has a line chart of monthly visitors. The AI suggested the title "Visitors grew strongly", but the chart shows two up months and one down month. She writes a more careful title: "Visitors rose in April and May, then fell in June."

## Common Mistake
Many learners choose the chart that looks most interesting, or accept the AI's first suggestion without checking it against the question. Another common mistake is a title that only names the topic. Choose the chart for the message, and make the title say the finding in one sentence that the data supports.

## Key Takeaways
1. Use line charts for change over time and bar charts for comparisons; avoid pie charts with many slices and all 3D effects.
2. Write a chart title that states the finding in one sentence, and check that the data supports it.
3. Ask AI to suggest a chart and title, then build it yourself in Google Sheets from your checked data.

## Hands-on Exercise
**Task:** Build 3 charts in Google Sheets for 3 different questions about the orders dataset. Give each a title that states the main finding in one sentence.
**Tools:** Google Sheets (free); Claude or ChatGPT (free tier) for suggestions. The data is fictional.
**Steps:**
1. Use your clean orders sheet (revenue in US dollars) and your pivot tables from L07:

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

2. Choose 3 questions: How did revenue change by month? Which region brought in most revenue? Which product brought in most revenue?
3. For each question, ask the AI which chart type fits and for a title that states the finding.
4. Build each chart with Insert > Chart. Remove 3D effects and sort bars from largest to smallest.
5. Check each title against your pivot tables before you keep it.
**What good looks like:** A line chart of monthly revenue (470, 820, 2,160) with a careful title such as "Revenue rose each month, but one large order made up most of March". A sorted bar chart by region with a title such as "South brought in 64% of revenue (2,220 of 3,450)". A sorted bar chart by product with a title such as "Office chairs brought in about 77% of revenue".
**Time:** about 30 minutes

## Review Flags
- [VERSION] Google Sheets chart steps (Insert > Chart, the Chart editor's Setup and Customise tabs, and Chart and axis titles) must be checked against the current interface.
