# L16 Cleaning Data: Missing Values, Duplicates and Types

Course: AI-11 · Module: M4 · Objectives: O5, O6 · Video: 5 min (screen demo)

## Hook
In L14 you found the problems. Now you must decide what to do about each one. There is rarely a single correct answer, and every choice changes what a future model will learn. That is why a good analyst writes down each decision and the reason for it.

## Explanation
The main cleaning tools in pandas:

- `df.drop_duplicates()` removes rows that are exact copies of an earlier row.
- `df.dropna(subset=["col"])` removes rows where that column is missing. Without `subset`, it removes rows with **any** missing value, which can remove far more than you expect.
- `df["col"].fillna(value)` fills missing values. Common choices are the **mean** (for number columns without extreme values), the **median** (for number columns with extreme values), the **most common value** (for categories: `df["col"].mode()[0]`), or a label such as `"unknown"`.
- `pd.to_numeric(col, errors="coerce")` converts text to numbers and turns values that cannot be converted into `NaN`.
- `pd.to_datetime(col)` converts text to real dates. `astype()` converts to other types, such as `astype(int)`.
- A filter such as `df[df["quantity"] > 0]` removes impossible values.

**Every choice has a cost.** Dropping rows loses information and can make the data less representative: if most missing values come from one city, dropping them removes that city's customers. Filling values keeps the rows but invents numbers, and can hide the fact that the data was missing. A filled value is a guess.

Keep a **cleaning log**: a short table with the problem, the action, the number of rows affected and a one-line justification. It lets another person check your work and repeat it.

Work on a copy, and never overwrite the raw file. Cleaning steps should be code, so they can run again on new data.

**Analogy:** Cleaning data is like restoring an old building. A restorer decides, room by room, whether to repair, replace or remove. Each decision is photographed and written in a record, so future owners know which walls are original and which are new. A cleaning log is that record for your data.

## Worked Example
Linh is a junior data analyst at the same marketplace as in L14 (shops in Lagos, Hanoi and Lima). She uses the synthetic order data from L14 and cleans it step by step.

The presenter runs the L14 data cell first, then:

```python
clean = orders.drop_duplicates()
clean = clean[clean["quantity"] > 0]
clean = clean.dropna(subset=["order_date"]).copy()
clean["unit_price"] = pd.to_numeric(clean["unit_price"], errors="coerce")
clean["unit_price"] = clean["unit_price"].fillna(clean["unit_price"].median())
clean["order_date"] = pd.to_datetime(clean["order_date"])
print(clean.shape, clean.isna().sum().sum())
```

```
(8, 8) 0
```

`.copy()` tells pandas that `clean` is a new table, so later changes do not affect `orders` and do not cause a warning. The table went from 11 rows to 8, and no missing values remain. `unit_price` is now a number column (`float64`) and `order_date` is a date column (`datetime64`). [VERSION]

Linh's cleaning log, in a text cell:

| Problem | Action | Rows | Justification |
|---|---|---|---|
| Duplicate order 1003 | Drop copy | 1 | Same order ID and values; counted twice by mistake. |
| Quantity -2 (1004) | Drop row | 1 | Impossible value; this also removes the missing payment. |
| Missing date (1007) | Drop row | 1 | A date cannot be guessed; the row cannot be placed in time. |
| Price "unknown" (1005) | Fill with median (4.50) | 1 | Keeps the order; median because prices vary widely. |
| Dates stored as text | `to_datetime` | all | Needed to extract weekday and month in L17. |
| Quantity 500 (1006) | Keep, flag | 0 | Possible bulk order; waiting for the Lima shop to confirm. |

Linh notes one cost: order 1007 was one of only two returned orders, so dropping it removes half of the returns. She adds this to the log as a risk.

## Common Mistake
Beginners often run `df.dropna()` with no `subset` "to be safe". In a real dataset with many columns, almost every row has at least one empty cell, so this can delete most of the data without any message. Always check the shape before and after each step, and use `subset` to target the column that matters. A second mistake is filling missing values without recording it, so nobody knows later which values are real.

## Key Takeaways
1. Use `drop_duplicates`, `dropna(subset=...)`, `fillna`, `to_numeric`, `to_datetime` and filters to fix the problems found in the audit.
2. Dropping loses information and filling invents values; choose based on the column and the cost.
3. Record every decision in a cleaning log, and check the shape after each step.

## Hands-on Exercise
**Task:** Clean the messy order file and write a one-line justification for each decision in a cleaning log.
**Tools:** Google Colab (free) with pandas; the synthetic order data from L14 and your audit list.
**Steps:**
1. Run the L14 data cell and print `orders.shape`.
2. For each problem in your L14 audit, choose an action: drop, fill, convert, or keep and flag.
3. Write the code for each action in its own cell, and print the shape after each one.
4. Try one alternative: fill the unknown price with the mean instead of the median, compare the two values, and decide which you prefer.
5. Write your cleaning log as a table in a text cell, with a one-line justification per row.
6. Finish with `clean.info()` to confirm the types and that no values are missing.
**What good looks like:** A cleaned table with no duplicates, no missing values, a numeric price column and a date column, plus a log in which every action has a reason. Your choices may differ from Linh's if your reasons are clear.
**Time:** about 30 minutes

## Review Flags
- [VERSION] The date dtype shows as datetime64[us] in pandas 3 and datetime64[ns] in pandas 2. The code was tested without warnings in pandas 3.0.6 and 2.2.3 with Python 3.11.
- The order data is synthetic and was created for this course.
