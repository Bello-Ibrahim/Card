# L10 A Simple Dashboard in Looker Studio | Presenter Script

Course: AI-08 · Video: 5 min · Words: 705

## Hook
Every Monday, your manager asks for the latest numbers, and you copy charts into an email. A dashboard is one page, connected to your sheet, that people can open whenever they need it. Today, you build one.

## Explain
Last time, we built clear charts in Google Sheets. Now we bring them together on one page.

Looker Studio is a free Google tool for building dashboards and reports. It connects to a data source, such as a Google Sheet, and shows the data as charts, scorecards and tables on a page. When the sheet changes, the dashboard shows the new data.

A simple one-page dashboard has four parts. Scorecards, which are single large numbers, like total revenue. Charts, a line chart for change over time and a bar chart for comparisons. A filter control, like a date range, so viewers can choose the period. And a clear title with short labels, so the page makes sense without you.

A calculated field is a new field that Looker Studio calculates from existing ones, for example average order value. AI can help you write the formula. AI can also suggest a layout, such as scorecards across the top and charts below.

Share safely. Give view-only access to named people, not edit access. Check the data source settings before you share, and only connect anonymised or approved data, as you learned in lesson two.

A dashboard is like the instrument panel of a car. The driver does not need to see the engine. Only a few clear numbers, such as speed and fuel, always in the same place.

## Demonstrate
Omar is a small business adviser in Amman, Jordan. He builds a dashboard for the fictional orders sheet, so the shop owner can check sales without opening the spreadsheet. The sheet has one header row, no merged cells, and real dates.

He opens Looker Studio and creates a new report. He chooses the Google Sheets connector, selects the spreadsheet and the worksheet, keeps the first row as headers, and adds it.

He checks the fields. Order date must be a date, and revenue must be a number. Then he adds two scorecards. Revenue shows three thousand four hundred and fifty, and the record count shows ten orders.

Next, he asks the AI for a Looker Studio calculated field for average revenue per order. It suggests the sum of revenue divided by the count of order IDs. He adds it as a third scorecard, which shows three hundred and forty-five. He checks by hand. Three thousand four hundred and fifty divided by ten is three hundred and forty-five.

Now the charts. First, a time series chart, with order date set to month, and revenue as the metric. It shows four hundred and seventy, eight hundred and twenty, and two thousand one hundred and sixty.

Then a bar chart with region and revenue, sorted from largest. South is two thousand two hundred and twenty, North six hundred and eighty, and West five hundred and fifty.

He adds a date range control in the top right, and tests it. He chooses February twenty twenty-six only, and total revenue changes to eight hundred and twenty.

Finally, he types the title, orders dashboard, January to March twenty twenty-six. He clicks share, adds the owner's email address, and chooses viewer.

A common mistake is to fill the page with every chart you can make. Twelve charts show nothing clearly. Choose the three to five numbers people really need, check each one against your pivot tables, and share with view-only access.

## Recap
Let's recap. First, Looker Studio connects to a Google Sheet, and shows scorecards, charts and filters on a page that updates with the data. Second, keep it simple, and check every number against your sheet. Third, ask AI for layout ideas and calculated fields, and share with view-only access and only safe data.

## CTA
Now it is your turn. In the exercise below this video, you will build a one-page Looker Studio dashboard from the orders sheet, with at least two charts, two scorecards and one filter. It takes about thirty-five minutes. In the next lesson, we start week three by checking AI insights for errors. See you there.

## Thumbnail
Headline: One Page, Live Numbers
Image: Navy background, a clean one-page dashboard mock-up with three teal scorecards across the top and a line chart and bar chart below, headline in teal Inter Bold.

## Production Notes
- Screen demo lesson: record in Looker Studio with a free Google account, connected to the fictional clean orders sheet from content.md (headers in row 1, no merged cells, real dates in Order Date).
- [VERSION] Looker Studio interface, connectors and sharing settings must be checked against the live tool before recording: Create > Report, the Google Sheets connector options ('Use first row as headers'), field types, scorecard and chart names, Record Count, calculated field syntax (SUM(Revenue) / COUNT(Order ID)), the date range control, and the Share and Viewer options.
- [VERIFY] How data source credentials (owner's or viewer's) affect what viewers can see, and the current default. The narration says only 'check the data source settings before you share'; it does not state the credential behaviour as fact.
- Omar and the Amman setting are fictional. Spoken numbers match content.md: scorecards 3,450 and 10; calculated field 345 (3,450 ÷ 10); months 470, 820, 2,160; regions South 2,220, North 680, West 550; February filter 820.
- Scene 15: use a placeholder email address such as owner@example.com, never a real one.
