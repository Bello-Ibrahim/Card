# HeyGen Batch Pack: AI-08 M2 (Analysing and Visualising Data)

Course: AI-Powered Data Analysis (No Code). Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L06 Asking Good Questions of Your Data

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M2_L06_presenter.mp4`
- **Expected length:** about 5.1 minutes (711 words). The quality gate accepts ±10%.

```text
Two people upload the same file to one AI tool. One gets a vague paragraph that could fit any business. The other gets a clear table with exact numbers and a note on how they were calculated. The difference is not the tool. It is the prompt.

Last week, you prepared clean, safe data. This week, we analyse it, and that starts with the prompt.

In lesson three, you turned a business question into a measurable data question. Now you put that question into a prompt. A strong analysis prompt has four parts. First, describe the dataset. For example, this file has ten orders from January to March twenty twenty-six, one row per order. Second, name the columns. Revenue is in column G, in US dollars.

Third, state the question, with the measure, group, period and comparison. What was total revenue per region for January to March? Fourth, ask for the method. Show the table first. Then tell me how many rows and which columns you used, and how you calculated each number.

Asking for a table first, and conclusions second, is important. A table is easy to check against your own data. A paragraph of conclusions is easy to believe, and hard to check.

Asking for the method helps you spot problems early. If the AI says it used nine rows, and your sheet has ten, you know something is wrong before you read any conclusion. And keep one question per prompt when you start. Long prompts with five questions often skip or mix up one part.

And remember the safety rule from lesson two. Upload only anonymised or fictional data, or data your organisation has approved for the tool.

Asking AI about your data is like ordering at a busy counter. Something to eat, please, gets you whatever is easiest to serve. One vegetable soup, small, no bread, and the receipt, gets you exactly what you wanted, plus proof of what you paid for.

Sofia is an operations analyst for a courier company in Mexico City. She uploads a fictional, anonymised file of deliveries. The columns are delivery ID, date, zone, promised minutes and actual minutes.

Her first prompt is short. Are our deliveries late? The AI answers with a general paragraph. Some deliveries appear to be delayed, especially at busy times. It suggests that she monitor performance. There are no numbers she can use.

So she writes a second prompt. This file has one row per delivery for March twenty twenty-six. A delivery is late when actual minutes minus promised minutes is more than ten. For each zone, count the deliveries and the late deliveries, and give the percentage late.

Show the table first. Then tell me how many rows you used, and how you calculated each column. Conclusion in two sentences maximum.

This time, the AI gives a table with one row per zone, and the three numbers she asked for. It notes that it used all the rows in the file, and it shows the formula it used for late. The conclusion names the zone with the highest percentage late.

Sofia still checks. She counts the rows in her own sheet with a COUNTA formula, and she recalculates the percentage for one zone. Both match, so she can use the table in her weekly report.

A common mistake is to ask for insights or interesting patterns, and accept whatever comes back. The AI then chooses the measure, the group and the period for you, often without saying so. Ask your own measurable question, and ask for the table and the method before the conclusion.

Let's recap. First, a strong analysis prompt describes the dataset, names the columns, states a measurable question, and asks for the method. Second, ask for a table first and conclusions second, because tables are easier to check than sentences. Third, check the row count and columns the AI reports against your own sheet, before you trust the conclusion.

Now it is your turn. In the exercise below this video, you will upload the clean orders sheet and ask three questions, using the four-part prompt. For each answer, note whether the AI showed its method. It takes about twenty-five minutes. In the next lesson, we build summaries and pivot tables. See you there.
```

## L07 Summaries and Pivot Tables

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M2_L07_presenter.mp4`
- **Expected length:** about 5.3 minutes (741 words). The quality gate accepts ±10%.

```text
Your manager asks, what is our average order in the South? You answer, seven hundred and forty dollars. It sounds healthy. But two of the three South orders were under two hundred and fifty dollars. The average was true, and still it told the wrong story.

Today, we summarise data by group, with pivot tables in Google Sheets.

A summary by group takes many rows, and reduces them to a few numbers per group, such as per region or per month. The three most useful summaries are the total, which is how much in all. The count, which is how many rows. And the average, which is the total divided by the count.

The average is useful, but it can hide important differences. One very large value pulls the average up, so the typical order may be much smaller. When you see an average, also look at the count, and at the largest and smallest values.

A pivot table builds these summaries for you, without formulas. You choose which column goes in rows, which are the groups. And which column goes in values, which are the numbers, added up, counted or averaged.

A good habit is to compare the pivot table with the AI's own summary. If they differ, there is usually a simple cause. The AI skipped a row, used a different column, or grouped dates in a different way.

Think of a pile of receipts. You sort them into envelopes, first by month and then by shop, and you write the total on each envelope. The receipts do not change. You only arrange them, so the totals are easy to read.

Tomasz is a sales coordinator in Kraków, Poland. He uses the same clean, fictional orders sheet, with revenue in US dollars, and the month column from lesson five.

He clicks any cell in the data, and chooses insert, pivot table. He selects a new sheet, and clicks create.

In the editor, he adds region to rows. Then he adds revenue to values, and checks that it is summarised by sum. The result is North six hundred and eighty, South two thousand two hundred and twenty, and West five hundred and fifty. The grand total is three thousand four hundred and fifty.

Next, he adds revenue to values two more times, once as a count of orders, and once as an average. North has four orders, with an average of one hundred and seventy. South has three orders, with an average of seven hundred and forty. West has three orders, with an average of one hundred and eighty-three point three three.

Then he builds a second pivot table, with month in rows and the sum of revenue. January is four hundred and seventy, February eight hundred and twenty, and March two thousand one hundred and sixty.

He uploads the same sheet to the AI tool. He asks for total, count and average revenue per region in a table, and the number of rows it used.

The AI's table shows South with a total of four hundred and twenty, and only two orders. The pivot table shows two thousand two hundred and twenty, and three orders. So he asks the AI which rows it used.

It had read the revenue of order ten oh eight as text, because his exported file still had one thousand eight hundred in quotation marks. So it left that row out. He fixes the source file, and the numbers match.

Look again at the South average of seven hundred and forty. Most of it comes from one order of one thousand eight hundred. The average alone hides this.

A common mistake is to report only the average. Always show the count next to it, and look at the individual rows when one group looks unusual.

Let's recap. First, summaries by group use totals, counts and averages, and a pivot table builds them without formulas. Second, an average can hide large differences, so always check the count, and the largest and smallest values. Third, compare your pivot table with the AI's summary, and find the cause of any difference.

Now it is your turn. In the exercise below this video, you will build two pivot tables in Google Sheets, sales by region and by month. Then ask the AI for the same summary, and explain any difference. It takes about thirty minutes. In the next lesson, we look at trends, outliers and correlation. See you there.
```

## L08 Trends, Outliers and Correlation

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M2_L08_presenter.mp4`
- **Expected length:** about 5.2 minutes (730 words). The quality gate accepts ±10%.

```text
Revenue in March was more than four times revenue in January. Is the business growing fast? Or did one customer place one very large order? The same number can tell two very different stories.

Last time, we built summaries and pivot tables. Now we look for patterns. Three ideas help, and each one has a trap.

The first idea is a trend. A trend is the general direction of a number over time, up, down or flat. To read a trend, look at many periods, not two. Three months can show a direction, but it is weak evidence. And check whether one unusual period creates a trend that disappears when you look closer.

The second idea is an outlier. That is a value far from the others. Outliers have three common causes. A data error, like forty-five typed instead of four hundred and fifty. A real but rare event, like a bulk order or a festival. Or a sign of change, like the first of many large orders from a new type of customer.

So never delete an outlier just because it is unusual. Ask why it exists first. Fix it if it is an error. If it is real, keep it, and report results with and without it.

The third idea is correlation. Two numbers are correlated when they tend to move together. That does not mean one causes the other. Here is a hypothetical case. In a coastal town, ice-cream sales and sunburn cases rise and fall together over the year. Ice cream does not cause sunburn. Both follow a third factor, hot, sunny weather.

So when AI says X leads to Y, ask three questions. Could a third factor explain both? Could it be a coincidence in a small dataset? Could the direction be reversed? AI finds outliers and correlations quickly, but it explains them less carefully.

Think of footprints in sand. A long line of steps shows a direction. That is a trend. One very deep print is an outlier, so ask what made it. And two lines of prints side by side do not mean one person followed the other. Both may have walked to the same café.

Fatou runs three ice-cream kiosks in Dakar, Senegal. She asks an AI tool to analyse her fictional weekly sales sheet for twelve weeks.

First, the AI reports a rising trend. Weekly sales grew from about three hundred cups in week one, to about four hundred and fifty in week twelve. Fatou checks with a line chart. The rise is steady over many weeks, not caused by one value. So she accepts it as a trend.

Second, the AI finds two outliers. Nine hundred cups in week seven, and forty-five cups in week ten. She does not delete them. She asks why.

Week seven was the week of a local festival next to one kiosk. That is a real event, so she keeps it and notes it. Week ten does not match her till records, which show four hundred and fifty. It was a typing error, so she corrects it.

Third, the AI notes that her sales rise in the same weeks as sunburn cases at a nearby clinic, which is also fictional. It says, higher sales are linked to sunburn.

Fatou sees the third factor. Hot weather drives both. The useful finding for her business is the link between temperature and sales, and she can check it against weather records.

A common mistake is to remove every outlier to make the chart look tidy. That can remove the most important finding. The opposite mistake is to build a whole conclusion on one outlier. Investigate first, then report with and without the unusual value.

Let's recap. First, a trend needs many periods, so check whether one unusual value creates or hides it. Second, ask why an outlier exists before you remove it. Fix errors, keep real events, and report their effect. Third, correlation does not prove causation. Look for a third factor, a coincidence, or a reversed direction.

Now it is your turn. In the exercise below this video, you will use AI to find the three largest outliers and one trend in the orders sheet. For each one, write a possible cause and how you could check it. It takes about twenty-five minutes. In the next lesson, we choose and build the right chart. See you there.
```

## L09 Choosing and Building the Right Chart

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M2_L09_presenter.mp4`
- **Expected length:** about 5.1 minutes (708 words). The quality gate accepts ±10%.

```text
A colourful 3D pie chart with nine slices looks impressive. Ask the audience which slice is the biggest, and half of them will guess wrong. A good chart is not the most attractive one. It is the one that makes the message obvious in five seconds.

Last time, we found trends and outliers. Now we show them clearly. Start with the message, then choose the chart. Ask yourself, what do I want the reader to see?

For change over time, like revenue by month, use a line chart, with time from left to right. For comparisons between groups, like revenue by region, use a bar chart. Sort the bars from largest to smallest, so the order is easy to read.

For parts of a whole, a bar chart usually still works better. A pie chart is only readable with two or three slices of clearly different sizes. And for the relationship between two numbers, like units and revenue, use a scatter chart.

Avoid 3D effects. They distort the size of bars and slices, so the reader sees differences that are not in the data. Use one colour, and a second colour only to highlight your point. And start the value axis of a bar chart at zero. If it starts higher, small differences look huge.

Next, write a title that states the finding, not just the topic. Revenue by region is a topic. South brought in most of the revenue is a finding. The reader gets the message, even if they only read the title.

AI can help you choose. Describe the question and the columns, and ask which chart type fits best, and why. Ask it to suggest a title that states the finding. Then build the chart yourself in Google Sheets, from your checked data. Select the data, insert a chart, choose the type, and type your title.

Choosing a chart is like giving directions. For a route across a city, you draw a map. For turn left at the bank, one sentence is enough. The format depends on what the other person needs to understand.

Mei Lin is a marketing analyst for a fictional online bookshop in Kuala Lumpur, Malaysia. Her report has a 3D pie chart of revenue by book category, with nine slices and the title, Q two revenue.

She describes the data to an AI tool, and asks for a better chart. The AI suggests a sorted horizontal bar chart, because there are nine categories to compare, and the labels are long. It suggests the title, children's books brought in the most revenue in Q two.

Mei Lin builds it in Google Sheets from her pivot table. She sorts the categories from largest to smallest, and removes the 3D effect. She uses one colour for all bars, and a stronger colour for children's books.

Before she uses the AI's title, she checks the pivot table. Children's books really are first, so the title is correct.

She also has a line chart of monthly visitors. The AI suggests the title, visitors grew strongly. But the chart shows two months up and one month down. So she writes a more careful title. Visitors rose in April and May, then fell in June.

A common mistake is to choose the chart that looks most interesting, or to accept the AI's first suggestion without checking it. Another is a title that only names the topic. Choose the chart for the message, and make the title state a finding the data supports.

Let's recap. First, use line charts for change over time and bar charts for comparisons. Avoid pie charts with many slices, and all 3D effects. Second, write a chart title that states the finding in one sentence, and check that the data supports it. Third, ask AI to suggest a chart and a title, then build it yourself in Google Sheets from your checked data.

Now it is your turn. In the exercise below this video, you will build three charts in Google Sheets, for three different questions about the orders sheet. Give each chart a title that states the main finding in one sentence. It takes about thirty minutes. In the next lesson, we build a simple dashboard in Looker Studio. See you there.
```

## L10 A Simple Dashboard in Looker Studio

- **Filename:** `ai-08-ai-powered-data-analysis-no-code_M2_L10_presenter.mp4`
- **Expected length:** about 5.0 minutes (695 words). The quality gate accepts ±10%.

```text
Every Monday, your manager asks for the latest numbers, and you copy charts into an email. A dashboard is one page, connected to your sheet, that people can open whenever they need it. Today, you build one.

Last time, we built clear charts in Google Sheets. Now we bring them together on one page.

Looker Studio is a free Google tool for building dashboards and reports. It connects to a data source, such as a Google Sheet, and shows the data as charts, scorecards and tables on a page. When the sheet changes, the dashboard shows the new data.

A simple one-page dashboard has four parts. Scorecards, which are single large numbers, like total revenue. Charts, a line chart for change over time and a bar chart for comparisons. A filter control, like a date range, so viewers can choose the period. And a clear title with short labels, so the page makes sense without you.

A calculated field is a new field that Looker Studio calculates from existing ones, for example average order value. AI can help you write the formula. AI can also suggest a layout, such as scorecards across the top and charts below.

Share safely. Give view-only access to named people, not edit access. Check the data source settings before you share, and only connect anonymised or approved data, as you learned in lesson two.

A dashboard is like the instrument panel of a car. The driver does not need to see the engine. Only a few clear numbers, such as speed and fuel, always in the same place.

Omar is a small business adviser in Amman, Jordan. He builds a dashboard for the fictional orders sheet, so the shop owner can check sales without opening the spreadsheet. The sheet has one header row, no merged cells, and real dates.

He opens Looker Studio and creates a new report. He chooses the Google Sheets connector, selects the spreadsheet and the worksheet, keeps the first row as headers, and adds it.

He checks the fields. Order date must be a date, and revenue must be a number. Then he adds two scorecards. Revenue shows three thousand four hundred and fifty, and the record count shows ten orders.

Next, he asks the AI for a Looker Studio calculated field for average revenue per order. It suggests the sum of revenue divided by the count of order IDs. He adds it as a third scorecard, which shows three hundred and forty-five. He checks by hand. Three thousand four hundred and fifty divided by ten is three hundred and forty-five.

Now the charts. First, a time series chart, with order date set to month, and revenue as the metric. It shows four hundred and seventy, eight hundred and twenty, and two thousand one hundred and sixty.

Then a bar chart with region and revenue, sorted from largest. South is two thousand two hundred and twenty, North six hundred and eighty, and West five hundred and fifty.

He adds a date range control in the top right, and tests it. He chooses February twenty twenty-six only, and total revenue changes to eight hundred and twenty.

Finally, he types the title, orders dashboard, January to March twenty twenty-six. He clicks share, adds the owner's email address, and chooses viewer.

A common mistake is to fill the page with every chart you can make. Twelve charts show nothing clearly. Choose the three to five numbers people really need, check each one against your pivot tables, and share with view-only access.

Let's recap. First, Looker Studio connects to a Google Sheet, and shows scorecards, charts and filters on a page that updates with the data. Second, keep it simple, and check every number against your sheet. Third, ask AI for layout ideas and calculated fields, and share with view-only access and only safe data.

Now it is your turn. In the exercise below this video, you will build a one-page Looker Studio dashboard from the orders sheet, with at least two charts, two scorecards and one filter. It takes about thirty-five minutes. In the next lesson, we start week three by checking AI insights for errors. See you there.
```
