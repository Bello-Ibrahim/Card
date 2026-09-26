# HeyGen Batch Pack: AI-11 M3 (Working with Data in pandas)

Course: Python for AI. Make one HeyGen video per lesson below, using these settings for every video.

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

## L11 Meet pandas: Series and DataFrames

- **Filename:** `ai-11-python-for-ai_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (678 words). The quality gate accepts ±10%.

```text
A spreadsheet with fifty rows is easy to read by eye. A table with fifty thousand rows is not. pandas lets you ask questions of a large table in one line of code, and repeat the same steps on next month's data in seconds.

We are now in week three. Until now, we worked with single values, lists and files. Now we work with whole tables. pandas is the most widely used Python library for tables of data, and it has two main objects.

A DataFrame is a whole table, with rows and named columns. A Series is one column of that table, for example the life expectancy column. Each row also has an index label on the left, starting at zero.

A DataFrame is like a spreadsheet, but instead of clicking and scrolling, you give written instructions. The instructions are saved, so you can check them, share them, and run them again on new data. A Series is like one column cut out on its own.

You usually load data with read csv. Then you take a first look with four tools. Head shows the first five rows. Shape gives the number of rows and columns. Info lists each column, its data type, and how many values are not missing. And describe summarises every number column. Notice that shape has no brackets after it. It is a property of the table, not a function.

This week, we use Gapminder country data. It has life expectancy, population and income per person, for many countries over time. Check the data source and its licence before you publish any results. To start, we use a small practice sample in the same format. Its numbers are invented, so they are not real statistics.

Let's meet the data. Aroha is a data journalist in Wellington, New Zealand. Before she writes any story, she wants to understand the table.

We paste one cell into Colab. It imports pandas and holds the practice sample as text in CSV format. A small helper from the io module lets read csv treat that text as if it were a file, and the result is a DataFrame called df. With a real file, you would simply give read csv the file name. We use this same sample until lesson fifteen.

Now a first look. Shape tells us there are eighteen rows and six columns. Next we list the column names. And then the unique years. There are three, nineteen ninety-seven, two thousand and two, and two thousand and seven.

Next, describe, rounded to one decimal place. Look at the minimum and maximum rows. Life expectancy runs from fifty-four point eight to seventy-eight point five. Population runs from fifteen million to eighty-five million. That is a much wider range. Notice that country and continent are missing from this summary. We will see why in a moment.

Finally, info. Every column has eighteen values that are not missing, so nothing is missing. It also shows each column's data type. The text columns may show a different type name, depending on your pandas version.

A common mistake is to think describe covers every column. By default, it only summarises number columns. So if a number column is stored as text, it will not appear at all. That is often the first sign of a data problem. So always check the data types in info as well. We look for these problems in lesson fourteen.

Let's recap. First, a DataFrame is a table, and a Series is one of its columns. You load CSV data with read csv. Second, start every dataset with head, shape, info and describe. Third, today's practice sample is invented. For real conclusions, use the full Gapminder data, with its source and licence checked.

Now it is your turn. In the exercise below this video, you will load the data and answer four questions. How many rows, which columns, which years, and which column has the widest range. It takes about twenty minutes. In the next lesson, we select and filter rows and columns. See you there.
```

## L12 Selecting and Filtering Rows and Columns

- **Filename:** `ai-11-python-for-ai_M3_L12_presenter.mp4`
- **Expected length:** about 4.8 minutes (672 words). The quality gate accepts ±10%.

```text
Most questions about data start with, which ones? Which countries? Which year? Which customers spent more than one hundred? Filtering is how you turn a big table into the few rows that answer your question.

Last time, we loaded a table and took a first look. Now we choose parts of it. One column name in square brackets gives a Series. A list of names gives a smaller DataFrame. That is why you see double brackets. The outer ones select, and the inner ones make the list.

Loc and iloc both select rows and columns. Loc uses labels, like index labels and column names. Iloc uses positions, counted from zero. And just like range, the end position is not included.

Now, filtering rows. A comparison on a column, such as year equals two thousand and seven, gives one True or False value for every row. This is called a mask. When you put the mask inside square brackets, pandas keeps only the rows marked True.

Think of a mask as a sieve with holes shaped by your question. You pour the whole table through it. Rows that match fall through into your result. Rows that don't match stay behind. Joining two conditions is like stacking two sieves. A row must pass through both.

To combine conditions, pandas uses symbols instead of words. The ampersand means and, the vertical bar means or, and the tilde means not. Put each condition in its own round brackets. And isin checks a column against a list of values. Finally, loc can filter rows and choose columns in one step. You give it the mask first, then the list of columns you want to keep.

Let's use it. Mateus is a public health student in Maputo, Mozambique. He wants the countries in Africa and the Americas with life expectancy above sixty, in the most recent year. He uses the invented practice sample from the last lesson.

First, we keep only the latest year. Instead of typing two thousand and seven, we ask for the maximum year, so the code still works when newer data is added.

Next, the mask. The continent must be in our list of two, and life expectancy must be above sixty. Then loc keeps the matching rows, and only three columns. We print the result and count its rows.

Run it. Ghana, Peru and Chile, and a count of three. The numbers on the left show which rows of the original table were kept. Kenya is not there, because its value, fifty-nine point six, is below sixty. Counting the rows is a quick check that the filter did what you meant.

One more. Asian countries in two thousand and seven, with the largest population first. We combine two conditions, each in its own brackets. Then we sort by population in descending order, and show two columns. Vietnam comes first, with eighty-five million people, then Nepal. Two rows, which is what we expected from the sample.

A common mistake is writing the word and instead of the ampersand, or forgetting the round brackets. Both give an error. The fix is always the same. Use the symbol, and wrap each condition in its own brackets. Also note that this data says Americas, not South America. Filter on the wrong name, and you get zero rows, with no error to warn you.

Let's recap. First, single brackets give one column, and double brackets give several. Loc uses labels, and iloc uses positions. Second, a condition creates a True or False mask, and the table keeps the True rows. Third, combine conditions with ampersand, bar and tilde, with each one in round brackets, and check every filter by counting rows.

Now it is your turn. In the exercise below this video, you will write five filters on the data, for example all Asian countries in two thousand and seven sorted by population, and check each result by counting rows. It takes about twenty-five minutes. In the next lesson, we learn sorting, grouping and summarising. See you there.
```

## L13 Sorting, Grouping and Summarising

- **Filename:** `ai-11-python-for-ai_M3_L13_presenter.mp4`
- **Expected length:** about 4.8 minutes (668 words). The quality gate accepts ±10%.

```text
Which continent had the biggest change? You cannot answer that by looking at single rows. You need to put rows into groups, and summarise each group. In pandas, this takes one line.

Last time, we filtered rows. Now we sort and summarise them. Sort values puts rows in order, from smallest to largest. Add ascending equals False to put the largest first. You can also sort by several columns, for example by continent and then by year. And value counts counts how many rows have each value. It is the quickest way to spot rare or misspelled categories.

Group by works in three steps, often called split, apply, combine. First, split the rows into groups, for example by continent. Then apply a summary to each group, such as the mean, the median or a count. Finally, combine the results into a new, smaller table.

Think of a shoebox of receipts. You sort them into piles by month, and then add up each pile. You don't change the receipts. You only organise them, and write one total on a note on top of each pile. The notes together are your summary table.

In code, you group by continent, take the life expectancy column, and calculate the mean. To get several summaries at once, use agg, and give each result a name. Here, n unique counts different values, so each country counts once, even though it appears in three years.

You can also add a calculated column, such as total income from population times income per person. pandas calculates it for every row at once, with no loop. And one choice to make carefully. The mean is pulled by a few very large or small values. The median is the middle value, so it is more stable when a group has extreme values, as income data often does.

Let's try it. Soo-ah is an analyst at a development charity in Seoul, South Korea. She wants the median income per person for each continent, in each year. She uses the invented practice sample.

We group by two columns, continent and year, take the income column, and calculate the median. Then unstack turns the years into columns, so the table is easy to read across. Grouping by two columns gives one value for each pair of continent and year.

Run it. We get one row per continent, and one column per year. In this sample, the Americas have much higher values than the other two groups. And all three groups increase from two thousand and two to two thousand and seven.

But with only two countries per continent, these are practice numbers only. Real conclusions need the full dataset. So which rows drive the high Americas values? A quick sort, largest first, showing the top three rows. All three are Chile. So one country pulls the Americas group up. This is a good habit. When a summary surprises you, look at the rows behind it.

A common mistake is averaging values that should not be averaged directly. The mean of country values gives each country the same weight, so a small country counts as much as a very large one. That can be the right choice, but say clearly what your summary means. Also, group by leaves out rows where the group column is missing, so check for missing values first.

Let's recap. First, sort values orders rows, and value counts counts the rows for each category. Second, group by splits rows into groups, applies a summary such as mean, median or count, and combines the results. Agg names several summaries at once. Third, add calculated columns without a loop, and prefer the median when groups contain extreme values.

Now it is your turn. In the exercise below this video, you will make a table of average life expectancy by continent for three different years, and write two sentences on what changed. It takes about twenty-five minutes. In the next lesson, we learn how to find data quality problems. See you there.
```

## L14 Finding Data Quality Problems

- **Filename:** `ai-11-python-for-ai_M3_L14_presenter.mp4`
- **Expected length:** about 4.8 minutes (670 words). The quality gate accepts ±10%.

```text
A machine learning model learns whatever is in its data, including the mistakes. If a quantity of minus two, or a copied row, goes into training, the model treats it as truth. So before you clean anything, you need to find the problems.

Last time, we summarised clean practice data. Real data is rarely clean. A data audit is a systematic check of a dataset for problems, done before cleaning. You don't fix anything yet. You make a list.

Think of a mechanic's inspection before a repair. The mechanic walks around the car with a checklist. Tyres, lights, brakes, oil. They write down every problem first, and only then decide what to fix, and in what order. If you start repairs too early, you fix the first thing you notice, and miss the dangerous one.

Five checks find most problems. First, missing values. Is na, followed by sum, counts the empty cells in each column. Second, duplicates, which are rows that copy an earlier row exactly. Third, wrong types. A price column stored as text means at least one value could not be read as a number.

Fourth, inconsistent categories. Unique lists every different spelling, and to a computer, Lima in capitals is a different value. Fifth, impossible values and outliers. An impossible value cannot be true, like a negative quantity. An outlier is possible but unusual. Outliers need a human decision, not automatic deletion.

For each problem, write down what you found, where, and the code that found it. This list becomes your cleaning plan in lesson sixteen.

Let's audit a real-looking file. Oluwaseun is an operations analyst for an online marketplace with shops in Lagos, Hanoi and Lima. He receives an export of recent orders. The data is synthetic, made up for this course.

We paste one cell that holds eleven orders as CSV text, and read it into a DataFrame called orders. We use this same file for the next three lessons.

Now three checks. First, missing values. A short extra step keeps only the columns that have at least one. One order date and one payment method are missing. Second, duplicates. There is one copied row. Third, the city spellings. Six different spellings, for only three cities.

Dtypes shows that the price and the date are both stored as text. To find the bad price, we try to convert the column to numbers. Any value that fails becomes missing, and we show those rows. It is order ten oh five, with the price unknown.

Finally, the quantity. The minimum is minus two, which is impossible. The median is two. And the maximum is five hundred. That is possible, but very unusual.

Here is Oluwaseun's audit list. One duplicate row. A missing date and a missing payment method. A price stored as text. Dates stored as text. Six spellings for three cities. An impossible quantity of minus two. And a possible outlier of five hundred units, to confirm with the Lima shop. Each item has the order number and the code that found it.

A common mistake is fixing the first problem you see, like deleting the five hundred unit order. It may be a real bulk order from a genuine customer. Complete the audit first. And look at the minimum, median and maximum, not only the mean. Here, one outlier pulls the mean quantity up to forty-seven, which describes no real order.

Let's recap. First, audit before you clean. List every problem, and the code that found it. Second, use five checks for missing values, copies, wrong types, spellings and extreme values. Third, impossible values are errors, but outliers are questions that need a human decision.

Now it is your turn. In the exercise below this video, you will audit the messy order file, and list every problem you find, with the code that found it. Mark each one as an error, or as a question for a person. It takes about twenty-five minutes. In the next lesson, we explore data with charts. See you there.
```

## L15 Exploring Data with Charts

- **Filename:** `ai-11-python-for-ai_M3_L15_presenter.mp4`
- **Expected length:** about 4.7 minutes (659 words). The quality gate accepts ±10%.

```text
A table of one thousand seven hundred numbers hides its patterns. A chart can show a gap, a cluster or a strange point in a few seconds. Charts are not only for final reports. They are one of the fastest ways to explore and check data.

Last time, we audited data with code. Today, we look at it. pandas can draw charts straight from a DataFrame with the plot method. It uses a library called matplotlib underneath, which Colab already has. Three chart types cover most exploration.

A histogram shows the distribution of one number column. Which values are common, which are rare, and where the gaps are. A bar chart compares a number across categories, such as countries. And a scatter plot shows the relationship between two number columns. Each dot is one row. If the dots rise from left to right, the two values tend to rise together.

When you read a chart, look for four things. The general pattern, clusters, gaps and outliers. Then ask whether a pattern could come from the way the data was collected. And remember, a chart shows that two things move together. It does not show that one causes the other.

Exploring a table without charts is like reading the heights of one thousand points on a map. The numbers are all there, but you will not see the mountain. A chart is the map drawn from those numbers. The shape appears at once, and you know where to look.

Every chart needs a title, axis labels with units, and a note of the data source. When values cover a very wide range, such as income, use a log scale. It spaces one thousand, ten thousand and one hundred thousand evenly, so small values are not squeezed into a corner.

Let's draw all three. Rafael is preparing a session for secondary school teachers in Lisbon, Portugal. He uses the invented practice sample.

First, a histogram of life expectancy. The bins setting asks for six bars, and we add a title and a label on the horizontal axis. It shows two groups. Several values between about fifty-five and sixty-four, several between about sixty-eight and seventy-nine, and few in between. With a different number of bars, the picture can change, so it is worth trying two or three.

Next, a bar chart. We keep only two thousand and seven, and plot income per person by country, with a title and a label on the vertical axis, in US dollars. Chile stands far above the other five countries.

Finally, a scatter plot of income against life expectancy, with a log scale for income. The dots generally rise from left to right. But three points sit high on the left. Vietnam has life expectancy above seventy with low income per person.

Rafael notes this as a question for further reading, not a conclusion. He also reminds the teachers that these are invented practice numbers. Real statements need the full dataset.

A common mistake is choosing a chart because it looks attractive. A line connecting countries in alphabetical order suggests a trend that does not exist. Pick the chart by the question. And don't leave the default labels with no units, which forces the reader to guess.

Let's recap. First, use a histogram for a distribution, a bar chart for comparing categories, and a scatter plot for a relationship between two numbers. Second, read each chart for patterns, clusters, gaps and outliers, and remember that moving together does not prove cause. Third, give every chart a clear title, axis labels with units, and the data source.

Now it is your turn. In the exercise below this video, you will make three labelled charts from the data, and write one sentence of insight under each one. It takes about twenty-five minutes. Next week, we start cleaning data, and your capstone project comes closer. In the next lesson, we handle missing values, duplicates and types. See you there.
```
