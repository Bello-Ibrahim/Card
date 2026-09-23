# L13 Sorting, Grouping and Summarising | Presenter Script

Course: AI-11 · Video: 5 min · Words: 670

## Hook
Which continent had the biggest change? You cannot answer that by looking at single rows. You need to put rows into groups, and summarise each group. In pandas, this takes one line.

## Explain
Last time, we filtered rows. Now we sort and summarise them. Sort values puts rows in order, from smallest to largest. Add ascending equals False to put the largest first. You can also sort by several columns, for example by continent and then by year. And value counts counts how many rows have each value. It is the quickest way to spot rare or misspelled categories.

Group by works in three steps, often called split, apply, combine. First, split the rows into groups, for example by continent. Then apply a summary to each group, such as the mean, the median or a count. Finally, combine the results into a new, smaller table.

Think of a shoebox of receipts. You sort them into piles by month, and then add up each pile. You don't change the receipts. You only organise them, and write one total on a note on top of each pile. The notes together are your summary table.

In code, you group by continent, take the life expectancy column, and calculate the mean. To get several summaries at once, use agg, and give each result a name. Here, n unique counts different values, so each country counts once, even though it appears in three years.

You can also add a calculated column, such as total income from population times income per person. pandas calculates it for every row at once, with no loop. And one choice to make carefully. The mean is pulled by a few very large or small values. The median is the middle value, so it is more stable when a group has extreme values, as income data often does.

## Demonstrate
Let's try it. Soo-ah is an analyst at a development charity in Seoul, South Korea. She wants the median income per person for each continent, in each year. She uses the invented practice sample.

We group by two columns, continent and year, take the income column, and calculate the median. Then unstack turns the years into columns, so the table is easy to read across. Grouping by two columns gives one value for each pair of continent and year.

Run it. We get one row per continent, and one column per year. In this sample, the Americas have much higher values than the other two groups. And all three groups increase from two thousand and two to two thousand and seven.

But with only two countries per continent, these are practice numbers only. Real conclusions need the full dataset. So which rows drive the high Americas values? A quick sort, largest first, showing the top three rows. All three are Chile. So one country pulls the Americas group up. This is a good habit. When a summary surprises you, look at the rows behind it.

A common mistake is averaging values that should not be averaged directly. The mean of country values gives each country the same weight, so a small country counts as much as a very large one. That can be the right choice, but say clearly what your summary means. Also, group by leaves out rows where the group column is missing, so check for missing values first.

## Recap
Let's recap. First, sort values orders rows, and value counts counts the rows for each category. Second, group by splits rows into groups, applies a summary such as mean, median or count, and combines the results. Agg names several summaries at once. Third, add calculated columns without a loop, and prefer the median when groups contain extreme values.

## CTA
Now it is your turn. In the exercise below this video, you will make a table of average life expectancy by continent for three different years, and write two sentences on what changed. It takes about twenty-five minutes. In the next lesson, we learn how to find data quality problems. See you there.

## Thumbnail
Headline: Split, Apply, Combine
Image: Navy background, rows splitting into three coloured piles, each with a summary note on top, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Gapminder data source, access method and licence (carried from L11). The practice sample values are invented; label the table on screen as 'Invented practice data'.
- [VERSION] Printed output formats (for example the 'Name: count' line under value_counts()) differ between pandas versions. Outputs were produced with Python 3.11 and pandas 3.0.6.
- Printed outputs on screen must match content.md: the unstacked median table (Africa 1230.0 / 1235.0 / 1405.0; Americas 7980.0 / 8345.0 / 10290.0; Asia 1200.0 / 1410.0 / 1765.0) and the Chile 2007 13170 / 2002 10780 / 1997 10120 sort.
- Soo-ah (Seoul) is fictional. Stock footage of receipts must show no readable shop names or logos.
