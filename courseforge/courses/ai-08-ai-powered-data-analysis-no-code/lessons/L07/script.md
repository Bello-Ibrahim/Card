# L07 Summaries and Pivot Tables | Presenter Script

Course: AI-08 · Video: 5 min · Words: 742

## Hook
Your manager asks, what is our average order in the South? You answer, seven hundred and forty dollars. It sounds healthy. But two of the three South orders were under two hundred and fifty dollars. The average was true, and still it told the wrong story.

## Explain
Today, we summarise data by group, with pivot tables in Google Sheets.

A summary by group takes many rows, and reduces them to a few numbers per group, such as per region or per month. The three most useful summaries are the total, which is how much in all. The count, which is how many rows. And the average, which is the total divided by the count.

The average is useful, but it can hide important differences. One very large value pulls the average up, so the typical order may be much smaller. When you see an average, also look at the count, and at the largest and smallest values.

A pivot table builds these summaries for you, without formulas. You choose which column goes in rows, which are the groups. And which column goes in values, which are the numbers, added up, counted or averaged.

A good habit is to compare the pivot table with the AI's own summary. If they differ, there is usually a simple cause. The AI skipped a row, used a different column, or grouped dates in a different way.

Think of a pile of receipts. You sort them into envelopes, first by month and then by shop, and you write the total on each envelope. The receipts do not change. You only arrange them, so the totals are easy to read.

## Demonstrate
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

## Recap
Let's recap. First, summaries by group use totals, counts and averages, and a pivot table builds them without formulas. Second, an average can hide large differences, so always check the count, and the largest and smallest values. Third, compare your pivot table with the AI's summary, and find the cause of any difference.

## CTA
Now it is your turn. In the exercise below this video, you will build two pivot tables in Google Sheets, sales by region and by month. Then ask the AI for the same summary, and explain any difference. It takes about thirty minutes. In the next lesson, we look at trends, outliers and correlation. See you there.

## Thumbnail
Headline: When Averages Mislead
Image: Navy background, three bars for South orders (240, 180, 1,800) with a dashed teal average line at 740 floating above two of them, headline in teal Inter Bold.

## Production Notes
- Screen demo lesson: record in Google Sheets and in Claude or ChatGPT with the fictional clean orders sheet from content.md, including the Month column (H) from L05.
- [VERSION] Google Sheets pivot table steps (Insert > Pivot table, New sheet, the Rows and Values Add buttons, and the 'Summarise by' options including COUNTA) must be checked against the current interface before recording.
- [VERSION] File-analysis features in Claude and ChatGPT must be checked against the live tools before recording.
- To reproduce the AI mismatch in scene 13, export a copy of the file in which order 1008's revenue is stored as the text "1,800" in quotation marks, as content.md describes. If the live AI reads it correctly anyway, show the mismatch from a prepared screenshot and label it 'example'.
- Tomasz and the Kraków setting are fictional. Spoken numbers match content.md: North 680 / 4 orders / average 170; South 2,220 / 3 / 740; West 550 / 3 / 183.33; total 3,450; months 470, 820, 2,160; AI table South 420 with 2 orders.
