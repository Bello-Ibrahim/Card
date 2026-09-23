# L15 Exploring Data with Charts | Presenter Script

Course: AI-11 · Video: 5 min · Words: 664

## Hook
A table of one thousand seven hundred numbers hides its patterns. A chart can show a gap, a cluster or a strange point in a few seconds. Charts are not only for final reports. They are one of the fastest ways to explore and check data.

## Explain
Last time, we audited data with code. Today, we look at it. pandas can draw charts straight from a DataFrame with the plot method. It uses a library called matplotlib underneath, which Colab already has. Three chart types cover most exploration.

A histogram shows the distribution of one number column. Which values are common, which are rare, and where the gaps are. A bar chart compares a number across categories, such as countries. And a scatter plot shows the relationship between two number columns. Each dot is one row. If the dots rise from left to right, the two values tend to rise together.

When you read a chart, look for four things. The general pattern, clusters, gaps and outliers. Then ask whether a pattern could come from the way the data was collected. And remember, a chart shows that two things move together. It does not show that one causes the other.

Exploring a table without charts is like reading the heights of one thousand points on a map. The numbers are all there, but you will not see the mountain. A chart is the map drawn from those numbers. The shape appears at once, and you know where to look.

Every chart needs a title, axis labels with units, and a note of the data source. When values cover a very wide range, such as income, use a log scale. It spaces one thousand, ten thousand and one hundred thousand evenly, so small values are not squeezed into a corner.

## Demonstrate
Let's draw all three. Rafael is preparing a session for secondary school teachers in Lisbon, Portugal. He uses the invented practice sample.

First, a histogram of life expectancy. The bins setting asks for six bars, and we add a title and a label on the horizontal axis. It shows two groups. Several values between about fifty-five and sixty-four, several between about sixty-eight and seventy-nine, and few in between. With a different number of bars, the picture can change, so it is worth trying two or three.

Next, a bar chart. We keep only two thousand and seven, and plot income per person by country, with a title and a label on the vertical axis, in US dollars. Chile stands far above the other five countries.

Finally, a scatter plot of income against life expectancy, with a log scale for income. The dots generally rise from left to right. But three points sit high on the left. Vietnam has life expectancy above seventy with low income per person.

Rafael notes this as a question for further reading, not a conclusion. He also reminds the teachers that these are invented practice numbers. Real statements need the full dataset.

A common mistake is choosing a chart because it looks attractive. A line connecting countries in alphabetical order suggests a trend that does not exist. Pick the chart by the question. And don't leave the default labels with no units, which forces the reader to guess.

## Recap
Let's recap. First, use a histogram for a distribution, a bar chart for comparing categories, and a scatter plot for a relationship between two numbers. Second, read each chart for patterns, clusters, gaps and outliers, and remember that moving together does not prove cause. Third, give every chart a clear title, axis labels with units, and the data source.

## CTA
Now it is your turn. In the exercise below this video, you will make three labelled charts from the data, and write one sentence of insight under each one. It takes about twenty-five minutes. Next week, we start cleaning data, and your capstone project comes closer. In the next lesson, we handle missing values, duplicates and types. See you there.

## Thumbnail
Headline: See the Pattern
Image: Navy background, three mini charts side by side (histogram, bar chart, scatter plot) in teal, headline in teal Inter Bold.

## Production Notes
- [VERSION] pandas plotting options (kind, bins, logx, legend, title) and matplotlib behaviour differ between versions; check in the current Colab runtime. content.md code was tested with pandas 3.0.6 and matplotlib 3.11.2.
- [VERIFY] Gapminder data source, access method and licence (carried from L11). The practice sample values are invented; every chart title in the demo includes 'practice sample' or the screen shows the label 'Invented practice data'.
- Charts on screen must be the ones produced by the content.md code: a 6-bin life expectancy histogram with two groups (about 55 to 64 and about 68 to 79); a 2007 GDP-per-person bar chart with Chile far above the rest; a log-scale scatter with three Vietnam points high on the left.
- Rafael (Lisbon) is fictional.
