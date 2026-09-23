# L11 Meet pandas: Series and DataFrames | Presenter Script

Course: AI-11 · Video: 5 min · Words: 680

## Hook
A spreadsheet with fifty rows is easy to read by eye. A table with fifty thousand rows is not. pandas lets you ask questions of a large table in one line of code, and repeat the same steps on next month's data in seconds.

## Explain
Welcome to week three. Until now, we worked with single values, lists and files. Now we work with whole tables. pandas is the most widely used Python library for tables of data, and it has two main objects.

A DataFrame is a whole table, with rows and named columns. A Series is one column of that table, for example the life expectancy column. Each row also has an index label on the left, starting at zero.

A DataFrame is like a spreadsheet, but instead of clicking and scrolling, you give written instructions. The instructions are saved, so you can check them, share them, and run them again on new data. A Series is like one column cut out on its own.

You usually load data with read csv. Then you take a first look with four tools. Head shows the first five rows. Shape gives the number of rows and columns. Info lists each column, its data type, and how many values are not missing. And describe summarises every number column. Notice that shape has no brackets after it. It is a property of the table, not a function.

This week, we use Gapminder country data. It has life expectancy, population and income per person, for many countries over time. Check the data source and its licence before you publish any results. To start, we use a small practice sample in the same format. Its numbers are invented, so they are not real statistics.

## Demonstrate
Let's meet the data. Aroha is a data journalist in Wellington, New Zealand. Before she writes any story, she wants to understand the table.

We paste one cell into Colab. It imports pandas and holds the practice sample as text in CSV format. A small helper from the io module lets read csv treat that text as if it were a file, and the result is a DataFrame called df. With a real file, you would simply give read csv the file name. We use this same sample until lesson fifteen.

Now a first look. Shape tells us there are eighteen rows and six columns. Next we list the column names. And then the unique years. There are three, nineteen ninety-seven, two thousand and two, and two thousand and seven.

Next, describe, rounded to one decimal place. Look at the minimum and maximum rows. Life expectancy runs from fifty-four point eight to seventy-eight point five. Population runs from fifteen million to eighty-five million. That is a much wider range. Notice that country and continent are missing from this summary. We will see why in a moment.

Finally, info. Every column has eighteen values that are not missing, so nothing is missing. It also shows each column's data type. The text columns may show a different type name, depending on your pandas version.

A common mistake is to think describe covers every column. By default, it only summarises number columns. So if a number column is stored as text, it will not appear at all. That is often the first sign of a data problem. So always check the data types in info as well. We look for these problems in lesson fourteen.

## Recap
Let's recap. First, a DataFrame is a table, and a Series is one of its columns. You load CSV data with read csv. Second, start every dataset with head, shape, info and describe. Third, today's practice sample is invented. For real conclusions, use the full Gapminder data, with its source and licence checked.

## CTA
Now it is your turn. In the exercise below this video, you will load the data and answer four questions. How many rows, which columns, which years, and which column has the widest range. It takes about twenty minutes. In the next lesson, we select and filter rows and columns. See you there.

## Thumbnail
Headline: Meet pandas
Image: Navy background, a clean data table with one column highlighted in teal, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Gapminder data source, access method (CSV URL or the plotly library copy) and licence must be confirmed before recording and before learners publish results. The voiceover says only that learners must check the source and licence.
- [VERSION] px.data.gapminder() availability in the Colab runtime; dtype names in info() (str in pandas 3, object in older versions). content.md outputs were produced with Python 3.11 and pandas 3.0.6.
- The practice sample values are invented and must stay labelled on screen as 'Invented practice data, not real statistics' whenever the table is visible.
- Printed outputs on screen must match content.md: '(18, 6)', "['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap']", '[1997 2002 2007]'; describe() min/max: lifeExp 54.8 to 78.5, pop 15,000,000 to 85,000,000.
- Screen step for the sample cell: paste the full sample cell from content.md rather than typing it; zoom so the reader can see it is a CSV block.
- Aroha (Wellington) is fictional.
