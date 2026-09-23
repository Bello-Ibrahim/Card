# L17 Shaping Features: Text, Categories and Dates

Course: AI-11 · Module: M4 · Objectives: O4, O6 · Video: 5 min (screen demo)

## Hook
To a person, "Lima", "LIMA" and "lima " are the same city. To a computer they are three different values. And a machine learning model cannot use the word "Lima" at all: it needs numbers. This lesson turns text, categories and dates into clean, numeric **features**.

## Explanation
A **feature** is a column that a model uses to make a prediction. Most machine learning models only work with numbers, so text and dates must be converted. The steps are usually done in this order.

**1. Clean text** with the `.str` methods, which work on a whole column at once:

- `.str.strip()` removes spaces at the start and end.
- `.str.lower()` makes all letters lowercase.
- `.str.replace("old", "new")` replaces one spelling with another.

You can chain them: `df["city"].str.strip().str.lower()`.

**2. Group rare categories.** A category that appears only once or twice gives a model very little to learn from. Replace rare values with a shared label such as `"other"`. Choose the threshold (for example "fewer than 2 rows") and record it in your cleaning log.

**3. One-hot encode categories** with `pd.get_dummies`. It creates one new column per category, with 1 where the row has that category and 0 elsewhere. A city column with three cities becomes three columns: `city_hanoi`, `city_lagos` and `city_lima`. Why not just number the cities 1, 2 and 3? Because a model would read "Lima = 3" as "more than Lagos = 2", which has no meaning.

The default output type of `get_dummies` depends on the pandas version: True/False in recent versions, 0/1 in older ones. [VERSION] Add `dtype=int` to always get 0 and 1.

**4. Extract date parts.** A full date is hard for a model to use, but its parts often matter. With the `.dt` accessor on a date column: `.dt.year`, `.dt.month`, `.dt.dayofweek` (0 is Monday, 6 is Sunday) and `.dt.day_name()` for readable names.

**Analogy:** One-hot encoding is like a form with tick boxes instead of a blank line. A blank line ("City: ____") invites many spellings. Tick boxes ("Lagos ☐ Hanoi ☐ Lima ☐") give every answer the same shape, and a computer can count ticks easily. Each box becomes one column, with 1 for ticked and 0 for empty.

## Worked Example
Hamza is a data analyst in Rabat, Morocco, helping the same marketplace prepare its synthetic order data. He starts from the `clean` table from L16.

The presenter runs the L14 and L16 cells first, then:

```python
df = clean.copy()
df["city"] = df["city"].str.strip().str.lower().str.replace("ha noi", "hanoi")
print(df["city"].value_counts())
```

```
city
lagos    3
lima     3
hanoi    2
Name: count, dtype: int64
```

Six spellings became three cities. Next, the date parts:

```python
df["month"] = df["order_date"].dt.month
df["weekday"] = df["order_date"].dt.dayofweek
print(df[["order_date", "month", "weekday"]].head(3))
```

```
  order_date  month  weekday
0 2026-03-02      3        0
1 2026-03-02      3        0
2 2026-03-03      3        1
```

2 March 2026 is a Monday, so `weekday` is 0. Then Hamza groups rare payment methods and one-hot encodes:

```python
counts = df["payment"].value_counts()
rare = counts[counts < 2].index
df["payment"] = df["payment"].replace(list(rare), "other")
encoded = pd.get_dummies(df, columns=["city", "payment"], dtype=int)
print(encoded.filter(like="city_").head(3))
```

```
   city_hanoi  city_lagos  city_lima
0           0           1          0
1           0           1          0
2           1           0          0
```

"mobile" appeared only once after cleaning, so it became "other". `filter(like="city_")` shows only the new city columns. The table now also has `payment_card`, `payment_cash` and `payment_other`.

## Common Mistake
Beginners often one-hot encode before cleaning the text. Then "Lima" and "LIMA" become two separate columns, and the model treats them as two different cities, each with fewer examples. Always standardise text first, check it with `value_counts()`, and only then encode. A second mistake is encoding a column with hundreds of different values, such as customer names or order IDs, which creates hundreds of useless columns. Group rare values or leave such columns out.

## Key Takeaways
1. Clean text with `.str.strip()`, `.str.lower()` and `.str.replace()`, and check the result with `value_counts()`.
2. Group rare categories, then one-hot encode with `pd.get_dummies(..., dtype=int)` so each category becomes a 0/1 column.
3. Extract useful parts of dates, such as month and weekday, with the `.dt` accessor.

## Hands-on Exercise
**Task:** Standardise a city column with inconsistent spellings, one-hot encode it, and add weekday and month columns from an order date.
**Tools:** Google Colab (free) with pandas; your cleaned order table from L16.
**Steps:**
1. Print `clean["city"].unique()` and list the different spellings.
2. Standardise the column with `.str.strip()`, `.str.lower()` and `.str.replace()`. Check that `value_counts()` shows exactly 3 cities.
3. Add `month` and `weekday` columns with `.dt.month` and `.dt.dayofweek`. Add `.dt.day_name()` in a separate column to check a few rows.
4. Group any payment method with fewer than 2 rows into "other", and record the threshold in your cleaning log.
5. One-hot encode `city` and `payment` with `pd.get_dummies(..., dtype=int)`.
6. Run `get_dummies` once without `dtype=int` and note the output type your pandas version gives.
**What good looks like:** 3 city columns and 3 payment columns containing only 0 and 1, correct month and weekday values (2 March 2026 gives month 3 and weekday 0), and a log entry for the rare-category rule.
**Time:** about 25 minutes

## Review Flags
- [VERSION] pd.get_dummies default output type: True/False (bool) in pandas 2.0 and later, 0/1 integers (uint8) in earlier versions. The lesson uses dtype=int so results match across versions. Outputs were produced with Python 3.11 and pandas 3.0.6, and the code was also tested with pandas 2.2.3.
- The order data is synthetic and was created for this course.
