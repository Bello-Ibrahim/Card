# L10 A Simple Dashboard in Looker Studio

Course: AI-08 · Module: M2 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
Every Monday, your manager asks for "the latest numbers", and you copy charts into an email. A dashboard is one page, connected to your sheet, that people can open whenever they need it.

## Explanation
**Looker Studio** is a free Google tool for building dashboards and reports. It connects to a data source, such as a Google Sheet, and shows the data as charts, scorecards and tables on a page. When the sheet changes, the dashboard shows the new data. The interface, connectors and sharing settings change often, so check the live tool. [VERSION]

A simple one-page dashboard has four parts:

- **Scorecards:** single large numbers, such as total revenue or number of orders.
- **Charts:** a time series or line chart for change over time, and a bar chart for comparisons (L09).
- **A filter control:** for example a date range control, so viewers can choose the period.
- **A clear title** and short labels, so the page makes sense without you.

A **calculated field** is a new column that Looker Studio calculates from existing fields, for example average order value. AI can help you write the formula: describe your fields and ask for "a Looker Studio calculated field formula".

AI can also suggest a **layout**, such as scorecards across the top and charts below them.

**Share safely.** Give **view-only** access to named people, not edit access. Check whose credentials the data source uses: if it uses yours, viewers may see all the data in the dashboard even without access to the sheet. [VERSION] [VERIFY] Only connect anonymised or approved data, following L02.

**Analogy:** A dashboard is like the instrument panel of a car. The driver does not need to see the engine, only a few clear numbers, such as speed and fuel, always in the same place.

## Worked Example
Omar is a small business adviser in Amman, Jordan. He builds a dashboard for the fictional orders sheet, so the shop owner can check sales without opening the spreadsheet. The sheet must have one header row, no merged cells, and a real date in Order Date.

Presenter steps on screen: [VERSION]

1. Open Looker Studio and choose **Create > Report**.
2. In **Add data to report**, choose the **Google Sheets** connector. Select the spreadsheet and the worksheet, keep "Use first row as headers" ticked, and click **Add**.
3. Check the fields: Order Date must be a **Date** type and Revenue a **Number**. Change the type if needed.
4. Add two **scorecards**: Revenue (SUM) shows 3,450, and Record Count shows 10 orders.
5. Omar asks the AI: "Write a Looker Studio calculated field for average revenue per order, from fields Revenue and Order ID." It suggests `SUM(Revenue) / COUNT(Order ID)`. He adds it as a field and a third scorecard: 345. He checks it by hand: 3,450 ÷ 10 = 345.
6. Add a **time series chart** with Order Date as the dimension (set to month) and Revenue as the metric: 470, 820, 2,160.
7. Add a **bar chart** with Region as the dimension and Revenue as the metric, sorted from largest: South 2,220, North 680, West 550.
8. Add a **date range control** in the top right. Test it: choose February 2026 only; total revenue changes to 820.
9. Type a title: "Orders dashboard, January to March 2026".
10. Click **Share**, add the owner's email address, and choose **Viewer**.

## Common Mistake
Many learners fill the page with every chart they can make. Twelve charts show nothing clearly. Choose the 3 to 5 numbers people really need, check that each one matches your pivot tables, and share with view-only access.

## Key Takeaways
1. Looker Studio connects to a Google Sheet and shows scorecards, charts and filters on a page that updates with the data.
2. Keep it simple: a few scorecards, one chart for change over time, one for comparison, and a filter, and check every number against your sheet.
3. Ask AI for layout ideas and calculated fields, and share the dashboard with view-only access and only safe data.

## Hands-on Exercise
**Task:** Build a one-page Looker Studio dashboard from the orders dataset with at least 2 charts, 2 scorecards and one filter.
**Tools:** Looker Studio (free, with a Google account); Google Sheets (free); Claude or ChatGPT (free tier) for layout ideas. The data is fictional.
**Steps:**
1. Make sure your clean orders sheet matches this table, with headers in row 1:

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

2. Ask an AI tool for a simple layout for a sales dashboard with 2 scorecards, 2 charts and a date filter.
3. Follow the presenter steps above to connect the sheet, and add the scorecards, charts and date range control.
4. Check every number against your pivot tables from L07.
5. Share the dashboard with one person as Viewer, or keep it private if you have no one to share with.
**What good looks like:** Scorecards show 3,450 revenue and 10 orders (and 345 average if you add the calculated field). A monthly chart shows 470, 820 and 2,160, and a region bar chart shows South 2,220, North 680 and West 550. The date filter changes the numbers correctly, and sharing is view-only.
**Time:** about 35 minutes

## Review Flags
- [VERSION] Looker Studio interface, connectors and sharing settings must be checked against the live tool before scripting: Create > Report, the Google Sheets connector options, field types, scorecard and chart names, Record Count, calculated field syntax, the date range control, and the Share and Viewer options.
- [VERIFY] Confirm how data source credentials (owner's or viewer's) affect what viewers can see, and the current default setting.
