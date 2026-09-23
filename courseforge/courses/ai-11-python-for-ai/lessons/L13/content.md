# L13 Sorting, Grouping and Summarising

Course: AI-11 · Module: M3 · Objectives: O4, O5 · Video: 5 min (screen demo)

## Hook
"Which continent had the biggest change?" You cannot answer that by looking at single rows. You need to put rows into groups and summarise each group. In pandas this takes one line.

## Explanation
**Sorting.** `df.sort_values("gdpPercap")` sorts rows from smallest to largest. Add `ascending=False` for largest first. You can sort by several columns: `sort_values(["continent", "year"])`.

**Counting.** `df["continent"].value_counts()` counts how many rows have each value. It is the quickest way to see the categories in a column and whether any are rare or misspelled.

**Grouping.** `groupby` works in three steps, often called **split, apply, combine**:

1. **Split** the rows into groups by the values of one or more columns, such as `continent`.
2. **Apply** a summary to each group, such as `mean()`, `median()` or `count()`.
3. **Combine** the results into a new, smaller table.

```python
df.groupby("continent")["lifeExp"].mean()
```

Read this as: "group by continent, take the lifeExp column, and calculate the mean for each group". To calculate several summaries at once, use `agg`, which lets you name each result column:

```python
df.groupby("continent").agg(mean_life=("lifeExp", "mean"),
                            countries=("country", "nunique"))
```

`nunique` counts **different** values, so each country is counted once even though it appears in three years.

**Calculated columns.** You can add a new column from existing ones, and pandas calculates it for every row at once, with no loop: `df["gdp_total_bn"] = df["pop"] * df["gdpPercap"] / 1e9` gives total GDP in billions.

**Mean or median?** The mean is pulled up or down by a few very large or small values. The median is the middle value, so it is more stable when a group contains extreme values, as income data often does.

**Analogy:** `groupby` is like sorting a shoebox of receipts into piles by month, and then adding up each pile. You do not change the receipts. You only organise them and write one total on a note on top of each pile. The notes together are your summary table.

## Worked Example
Soo-ah is an analyst at a development charity in Seoul, South Korea. She wants the median GDP per person for each continent in each year, using the invented practice sample from L11.

The presenter runs the L11 sample cell first, then:

```python
summary = df.groupby(["continent", "year"])["gdpPercap"].median()
print(summary.unstack())
```

```
year         1997    2002     2007
continent                         
Africa     1230.0  1235.0   1405.0
Americas   7980.0  8345.0  10290.0
Asia       1200.0  1410.0   1765.0
```

Grouping by two columns gives one value per continent and year. `unstack()` turns the years into columns, so the table is easy to read across. In this sample, the Americas group has much higher values than the other two, and all three groups increase from 2002 to 2007. With only 2 countries per continent, these are practice numbers only; real conclusions need the full dataset.

A quick sort shows which rows drive the high Americas values:

```python
print(df.sort_values("gdpPercap", ascending=False).head(3)[["country", "year", "gdpPercap"]])
```

```
   country  year  gdpPercap
11   Chile  2007      13170
10   Chile  2002      10780
9    Chile  1997      10120
```

## Common Mistake
Beginners often average values that should not be averaged directly. The mean of country life expectancies gives each country the same weight: a small country counts as much as a very large one. That can be the right choice, but it is not the average for all people on the continent. Say clearly what your summary means, for example "the median of country values". Also remember that `groupby` leaves out rows where the group column is missing by default, so check `isna()` first.

## Key Takeaways
1. `sort_values` orders rows, and `value_counts` counts the rows for each category.
2. `groupby` splits rows into groups, applies a summary such as `mean`, `median` or `count`, and combines the results; `agg` names several summaries at once.
3. Add calculated columns without a loop, and prefer the median when groups contain extreme values.

## Hands-on Exercise
**Task:** Produce a table of average life expectancy by continent for 3 different years, and write 2 sentences on what changed.
**Tools:** Google Colab (free) with pandas; the practice sample or the full Gapminder data.
**Steps:**
1. Filter the data to 3 years with `df["year"].isin([...])`. The sample has 1997, 2002 and 2007; with the full data you can choose any 3.
2. Group by `continent` and `year`, take `lifeExp` and calculate the mean.
3. Use `unstack()` and `round(1)` to make a readable table with years as columns.
4. Add a column showing the change from the first year to the last year.
5. Write 2 sentences: which continent changed most, and one limit of this summary.
**What good looks like:** A table with one row per continent and one column per year. With the sample, Africa shows 56.7, 56.7 and 59.8. The sentences describe the change correctly and mention a limit, such as "each country has equal weight" or "only 2 countries per continent".
**Time:** about 25 minutes

## Review Flags
- [VERIFY] Gapminder data source, access method and licence (carried from L11). The practice sample values are invented.
- [VERSION] Printed output formats, such as the "Name: count" line under value_counts(), differ between pandas versions. Outputs were produced with Python 3.11 and pandas 3.0.6.
