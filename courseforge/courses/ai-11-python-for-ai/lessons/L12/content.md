# L12 Selecting and Filtering Rows and Columns

Course: AI-11 · Module: M3 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
Most questions about data start with "which ones?" Which countries? Which year? Which customers spent more than 100? Filtering is how you turn a big table into the few rows that answer your question.

## Explanation
**Choosing columns.** One column name in square brackets gives a Series: `df["country"]`. A **list** of names gives a smaller DataFrame: `df[["country", "lifeExp"]]`. Note the double brackets: the outer ones select, the inner ones make the list.

**loc and iloc.** Both select rows and columns in the form `[rows, columns]`:

- `df.loc[...]` uses **labels**: index labels and column names. `df.loc[0, "country"]` gives `Kenya`.
- `df.iloc[...]` uses **positions**, counted from 0. `df.iloc[0:2, 0:3]` gives the first 2 rows and first 3 columns. As with `range()`, the end number is not included.

**Filtering rows with conditions.** A comparison on a column, such as `df["year"] == 2007`, gives a Series of True and False values, one per row. This is called a **mask**. Putting the mask inside `df[...]` keeps only the rows marked True.

To combine conditions, pandas uses symbols instead of words:

- `&` for "and", `|` for "or", `~` for "not".
- **Put each condition in its own round brackets:** `(df["year"] == 2007) & (df["lifeExp"] > 60)`.

`isin()` checks against a list of values: `df["continent"].isin(["Africa", "Americas"])`.

You can filter and choose columns in one step with `loc`: `df.loc[mask, ["country", "lifeExp"]]`.

**Analogy:** A mask is like a sieve with holes shaped by your question. You pour the whole table through it. Rows that match (True) fall through into your result, and rows that do not match (False) stay behind. Joining two conditions with `&` is like stacking two sieves: a row must pass through both.

## Worked Example
Mateus is a public-health student in Maputo, Mozambique. He wants the countries in Africa and the Americas with life expectancy above 60 in the most recent year. He uses the practice sample from L11, so the numbers are invented. Note that Gapminder uses the continent name "Americas", not "South America"; filtering on "South America" returns 0 rows.

The presenter first runs the L11 sample cell, then builds the filter in steps:

```python
latest = df[df["year"] == df["year"].max()]
mask = latest["continent"].isin(["Africa", "Americas"]) & (latest["lifeExp"] > 60)
result = latest.loc[mask, ["country", "continent", "lifeExp"]]
print(result)
print(len(result))
```

```
   country continent  lifeExp
5    Ghana    Africa     60.1
8     Peru  Americas     71.6
11   Chile  Americas     78.5
3
```

`df["year"].max()` finds the most recent year instead of typing 2007, so the code still works if newer data is added. The index labels (5, 8, 11) show which rows of the original table were kept. Kenya is not in the result because its value, 59.6, is below 60.

Mateus checks the result by counting: `len(result)` is 3, which matches what he sees. Next, a filter with sorting: Asian countries in 2007, largest population first.

```python
asia07 = df[(df["continent"] == "Asia") & (df["year"] == 2007)]
print(asia07.sort_values("pop", ascending=False)[["country", "pop"]])
```

```
    country       pop
14  Vietnam  85000000
17    Nepal  28000000
```

## Common Mistake
Beginners write `and` instead of `&`, or forget the round brackets. `df[df["year"] == 2007 and df["lifeExp"] > 60]` raises `ValueError: The truth value of a Series is ambiguous`. Without brackets, `df["year"] == 2007 & df["lifeExp"] > 60` is evaluated in the wrong order and raises a different error. The fix is always the same: use `&` or `|`, and wrap each condition in its own brackets.

## Key Takeaways
1. `df["col"]` gives one column; `df[["a", "b"]]` gives several; `loc` uses labels and `iloc` uses positions.
2. A condition creates a True/False mask, and `df[mask]` keeps the True rows.
3. Combine conditions with `&`, `|` and `~`, with each condition in round brackets, and check every filter by counting rows.

## Hands-on Exercise
**Task:** Write 5 filters on the Gapminder data, for example all Asian countries in 2007 sorted by population, and check each result by counting rows.
**Tools:** Google Colab (free) with pandas; the practice sample from L11 or the full Gapminder data.
**Steps:**
1. Run the L11 sample cell (or load the full data).
2. Write filter 1: all rows for one country of your choice.
3. Write filter 2: all Asian countries in 2007, sorted by population from largest to smallest.
4. Write filter 3: rows where life expectancy is above 70 **or** GDP per person is below 1,200.
5. Write filter 4: rows from 1997 that are **not** in Africa, using `~`.
6. Write filter 5: your own question, using `loc` to show only 3 columns.
7. For each filter, print `len(result)` and write in a text cell whether the count matches what you expected by looking at the data.
**What good looks like:** Five filters that run without errors, each with a row count and a one-line check. With the sample data, filter 2 returns 2 rows and filter 4 returns 4 rows.
**Time:** about 25 minutes

## Review Flags
- [VERIFY] Gapminder data source, access method and licence (carried from L11). The practice sample values are invented.
- [VERSION] Outputs and error messages were produced with Python 3.11 and pandas 3.0.6; the second error message (without brackets) may be worded differently in other pandas versions.
