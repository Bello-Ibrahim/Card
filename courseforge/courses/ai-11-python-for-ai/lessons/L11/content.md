# L11 Meet pandas: Series and DataFrames

Course: AI-11 · Module: M3 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
A spreadsheet with 50 rows is easy to read by eye. A table with 50,000 rows is not. pandas lets you ask questions of a large table in one line of code, and repeat the same steps on next month's data in seconds.

## Explanation
**pandas** is the most widely used Python library for tables of data. It has two main objects:

- A **DataFrame** is a whole table: rows and named columns, like a spreadsheet you control with code.
- A **Series** is one column of a DataFrame. `df["lifeExp"]` gives the life expectancy column as a Series.

Each row has an **index** label on the left (0, 1, 2 and so on by default).

You usually load data with `pd.read_csv()`, which reads a CSV file from your computer, from Colab's file panel or from a web address (URL). Then you take a first look:

- `df.head()` shows the first 5 rows (`head(3)` shows 3).
- `df.shape` gives (rows, columns). It has no brackets, because it is a property, not a function.
- `df.info()` lists each column, its **dtype** (data type) and how many values are not missing.
- `df.describe()` gives count, mean, standard deviation, minimum, quartiles and maximum for each number column.

**Analogy:** A DataFrame is like a spreadsheet, but instead of clicking and scrolling you give written instructions. The instructions are saved, so you can check them, share them and run them again on new data. A Series is like one column of that spreadsheet cut out on its own.

This week uses **Gapminder** country indicators: life expectancy (`lifeExp`), population (`pop`) and GDP per person (`gdpPercap`) for many countries over time. A full copy is included in the plotly library, which Colab usually has installed: `import plotly.express as px` then `df = px.data.gapminder()`. [VERSION] Check the data source and licence before you publish any results. [VERIFY]

So that the lesson works offline, we start with a **small practice sample in the same format**. Its numbers are invented for practice. They are not real statistics.

## Worked Example
Aroha is a data journalist in Wellington, New Zealand. She wants to understand the table before writing any story.

The presenter pastes this cell into Colab and runs it. It creates the practice sample that L12 to L15 also use:

```python
import io
import pandas as pd

sample = """country,continent,year,lifeExp,pop,gdpPercap
Kenya,Africa,1997,55.1,29000000,1350
Kenya,Africa,2002,54.8,32000000,1290
Kenya,Africa,2007,59.6,36000000,1480
Ghana,Africa,1997,58.3,18000000,1110
Ghana,Africa,2002,58.6,20000000,1180
Ghana,Africa,2007,60.1,23000000,1330
Peru,Americas,1997,68.4,25000000,5840
Peru,Americas,2002,69.9,27000000,5910
Peru,Americas,2007,71.6,29000000,7410
Chile,Americas,1997,75.6,15000000,10120
Chile,Americas,2002,77.7,16000000,10780
Chile,Americas,2007,78.5,16500000,13170
Vietnam,Asia,1997,70.6,76000000,1390
Vietnam,Asia,2002,72.9,80000000,1760
Vietnam,Asia,2007,74.2,85000000,2440
Nepal,Asia,1997,59.4,23000000,1010
Nepal,Asia,2002,61.3,25000000,1060
Nepal,Asia,2007,63.8,28000000,1090
"""
df = pd.read_csv(io.StringIO(sample))
```

`io.StringIO` lets `read_csv` read text as if it were a file. With a real file you would write `pd.read_csv("gapminder.csv")`.

Then a first look, one line per cell:

```python
print(df.shape)
print(df.columns.tolist())
print(df["year"].unique())
```

```
(18, 6)
['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap']
[1997 2002 2007]
```

```python
df.describe().round(1)
```

The presenter points to the `min` and `max` rows: `lifeExp` runs from 54.8 to 78.5, while `pop` runs from 15,000,000 to 85,000,000. `df.info()` shows 18 non-null values in every column, so nothing is missing. The text columns show the dtype `str` in pandas 3 and `object` in older versions. [VERSION]

## Common Mistake
Beginners often read `describe()` and assume it covers every column. By default it only summarises number columns, so `country` and `continent` are left out. Also check the dtypes in `info()`: a number column that shows as text (`object` or `str`) will not appear in `describe()` at all, which is often the first sign of a data problem. You will look for these problems in L14.

## Key Takeaways
1. A DataFrame is a table and a Series is one of its columns; load CSV data with `pd.read_csv()`.
2. Start every dataset with `head()`, `shape`, `info()` and `describe()`.
3. The practice sample here is invented; use the full Gapminder data, with its source and licence checked, for real conclusions.

## Hands-on Exercise
**Task:** Load the Gapminder data into a DataFrame and answer 4 questions: how many rows, which columns, which years, and which column has the widest range.
**Tools:** Google Colab (free) with pandas (pre-installed). Use the practice sample, or the full data with `px.data.gapminder()`.
**Steps:**
1. Run the sample cell above, or load the full data into `df`.
2. Use `df.shape` to find the number of rows and columns.
3. Use `df.columns.tolist()` to list the columns.
4. Use `df["year"].unique()` to list the years.
5. Use `df.describe()` and calculate max minus min for each number column. Which is widest?
6. Write the 4 answers in a text cell, with the code that found each one.
**What good looks like:** Four correct answers, each backed by code. For the sample: 18 rows, 6 columns, the years 1997, 2002 and 2007, and `pop` has the widest range. For the full data, your numbers will be larger.
**Time:** about 20 minutes

## Review Flags
- [VERIFY] Gapminder data source, access method (CSV URL or the plotly library copy) and licence must be confirmed before recording and before learners publish results. The practice sample values are invented and must stay labelled as such.
- [VERSION] px.data.gapminder() availability in the Colab runtime, and dtype names shown by info() (str in pandas 3, object in earlier versions). Outputs were produced with Python 3.11 and pandas 3.0.6.
