# L09 Choosing and Building the Right Chart | Presenter Script

Course: AI-08 · Video: 5 min · Words: 708

## Hook
A colourful 3D pie chart with nine slices looks impressive. Ask the audience which slice is the biggest, and half of them will guess wrong. A good chart is not the most attractive one. It is the one that makes the message obvious in five seconds.

## Explain
Last time, we found trends and outliers. Now we show them clearly. Start with the message, then choose the chart. Ask yourself, what do I want the reader to see?

For change over time, like revenue by month, use a line chart, with time from left to right. For comparisons between groups, like revenue by region, use a bar chart. Sort the bars from largest to smallest, so the order is easy to read.

For parts of a whole, a bar chart usually still works better. A pie chart is only readable with two or three slices of clearly different sizes. And for the relationship between two numbers, like units and revenue, use a scatter chart.

Avoid 3D effects. They distort the size of bars and slices, so the reader sees differences that are not in the data. Use one colour, and a second colour only to highlight your point. And start the value axis of a bar chart at zero. If it starts higher, small differences look huge.

Next, write a title that states the finding, not just the topic. Revenue by region is a topic. South brought in most of the revenue is a finding. The reader gets the message, even if they only read the title.

AI can help you choose. Describe the question and the columns, and ask which chart type fits best, and why. Ask it to suggest a title that states the finding. Then build the chart yourself in Google Sheets, from your checked data. Select the data, insert a chart, choose the type, and type your title.

Choosing a chart is like giving directions. For a route across a city, you draw a map. For turn left at the bank, one sentence is enough. The format depends on what the other person needs to understand.

## Demonstrate
Mei Lin is a marketing analyst for a fictional online bookshop in Kuala Lumpur, Malaysia. Her report has a 3D pie chart of revenue by book category, with nine slices and the title, Q two revenue.

She describes the data to an AI tool, and asks for a better chart. The AI suggests a sorted horizontal bar chart, because there are nine categories to compare, and the labels are long. It suggests the title, children's books brought in the most revenue in Q two.

Mei Lin builds it in Google Sheets from her pivot table. She sorts the categories from largest to smallest, and removes the 3D effect. She uses one colour for all bars, and a stronger colour for children's books.

Before she uses the AI's title, she checks the pivot table. Children's books really are first, so the title is correct.

She also has a line chart of monthly visitors. The AI suggests the title, visitors grew strongly. But the chart shows two months up and one month down. So she writes a more careful title. Visitors rose in April and May, then fell in June.

A common mistake is to choose the chart that looks most interesting, or to accept the AI's first suggestion without checking it. Another is a title that only names the topic. Choose the chart for the message, and make the title state a finding the data supports.

## Recap
Let's recap. First, use line charts for change over time and bar charts for comparisons. Avoid pie charts with many slices, and all 3D effects. Second, write a chart title that states the finding in one sentence, and check that the data supports it. Third, ask AI to suggest a chart and a title, then build it yourself in Google Sheets from your checked data.

## CTA
Now it is your turn. In the exercise below this video, you will build three charts in Google Sheets, for three different questions about the orders sheet. Give each chart a title that states the main finding in one sentence. It takes about thirty minutes. In the next lesson, we build a simple dashboard in Looker Studio. See you there.

## Thumbnail
Headline: Charts That Make Sense
Image: Navy background, a crossed-out 3D pie chart on the left and a clean sorted teal bar chart with one highlighted bar on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Sheets chart steps (Insert > Chart, the Chart editor's Setup and Customise tabs, and Chart and axis titles) must be checked against the current interface. The narration describes the steps in general words; the slide in scene 7 may show the menu names once checked.
- Mei Lin and the Kuala Lumpur bookshop are fictional. content.md gives no category values, so the bar chart in scenes 10–11 uses unlabelled bar lengths with only 'Children's books' named and first; do not invent figures or other category names that look like real data.
- 'Q2' is spoken as 'Q two'.
- Stock footage must show no real bookshop names or logos.
