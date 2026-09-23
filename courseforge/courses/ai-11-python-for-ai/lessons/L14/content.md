# L14 Finding Data Quality Problems

Course: AI-11 · Module: M3 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
A machine learning model learns whatever is in its data, including the mistakes. If a quantity of -2 or a copied row goes into training, the model treats it as truth. Before you clean anything, you need to find the problems. This is called a data audit.

## Explanation
A **data audit** is a systematic check of a dataset for problems, done before cleaning. You do not fix anything yet. You make a list. Five checks find most problems:

1. **Missing values:** `df.isna().sum()` counts empty cells in each column. pandas shows missing values as `NaN` (or `NaT` for dates).
2. **Duplicates:** `df.duplicated().sum()` counts rows that are exact copies of an earlier row. `df[df.duplicated(keep=False)]` shows every copy, including the first.
3. **Wrong types:** `df.dtypes` shows each column's type. A price column with a text dtype means at least one value could not be read as a number. `pd.to_numeric(col, errors="coerce")` turns values that are not numbers into `NaN`, so you can find them.
4. **Inconsistent categories:** `df["city"].unique()` lists every different spelling. "Lima" and "LIMA" are different values to a computer.
5. **Impossible values and outliers:** `describe()` shows min and max. An **impossible value** cannot be true, such as a negative quantity. An **outlier** is possible but unusual, such as one order that is 100 times larger than the rest. Outliers need a human decision, not automatic deletion.

For each problem, record what you found, where, and the code that found it. This list becomes the plan for cleaning in L16.

**Analogy:** A data audit is like a mechanic's inspection before a repair. The mechanic walks around the car with a checklist: tyres, lights, brakes, oil. They write down every problem first and only then decide what to fix and in what order. Starting repairs before the inspection means you fix the first thing you notice and miss the dangerous one.

## Worked Example
Oluwaseun is an operations analyst for an online marketplace with shops in Lagos, Hanoi and Lima. He receives an export of recent orders. The data is **synthetic** (made up for this course), and prices are in US dollars. L16 to L18 use the same file.

The presenter pastes and runs this cell:

```python
import io
import pandas as pd

raw = """order_id,city,order_date,quantity,unit_price,payment,returned,refund
1001,Lagos,2026-03-02,2,4.50,card,no,0
1002,lagos ,2026-03-02,1,12.00,cash,yes,12.00
1003,Hanoi,2026-03-03,3,2.75,card,no,0
1004,Hanoi,2026-03-04,-2,2.75,,no,0
1005,Lima,2026-03-05,1,unknown,cash,no,0
1006,LIMA,2026-03-06,500,3.10,card,no,0
1003,Hanoi,2026-03-03,3,2.75,card,no,0
1007,Lagos,,2,6.00,mobile,yes,12.00
1008,Ha Noi,2026-03-08,4,1.90,card,no,0
1009,Lima,2026-03-09,2,8.25,mobile,no,0
1010,Lagos,2026-03-10,1,5.40,cash,no,0
"""
orders = pd.read_csv(io.StringIO(raw))
```

Then the audit, one check per cell:

```python
print(orders.isna().sum()[lambda s: s > 0])
print(orders.duplicated().sum())
print(orders["city"].unique().tolist())
```

```
order_date    1
payment       1
dtype: int64
1
['Lagos', 'lagos ', 'Hanoi', 'Lima', 'LIMA', 'Ha Noi']
```

`[lambda s: s > 0]` keeps only columns with at least one missing value. `orders.dtypes` shows `unit_price` and `order_date` as text (`str` in pandas 3, `object` in older versions), not numbers or dates. [VERSION] To find the bad price:

```python
bad_price = pd.to_numeric(orders["unit_price"], errors="coerce").isna()
print(orders.loc[bad_price, ["order_id", "unit_price"]])
print(orders["quantity"].describe()[["min", "50%", "max"]])
```

```
   order_id unit_price
4      1005    unknown
min     -2.0
50%      2.0
max    500.0
Name: quantity, dtype: float64
```

Oluwaseun's audit list: 1 duplicate row (order 1003); a missing date (1007) and a missing payment method (1004); `unit_price` stored as text because of "unknown" (1005); dates stored as text; 6 spellings for 3 cities; an impossible quantity of -2 (1004); and a possible outlier of 500 units (1006) to confirm with the Lima shop.

## Common Mistake
Beginners often start fixing the first problem they see, for example deleting the row with 500 units. But 500 may be a real bulk order, and deleting it would remove a genuine customer. Complete the audit first, and separate **impossible** values (errors) from **unusual** ones (questions for a person who knows the business). Also note that the mean quantity here is 47, which describes no real order: one outlier pulled it up. Look at the min, median and max, not only the mean.

## Key Takeaways
1. Audit before you clean: list every problem and the code that found it.
2. Use `isna().sum()`, `duplicated()`, `dtypes`, `unique()` and `describe()` for missing values, copies, wrong types, spellings and extreme values.
3. Impossible values are errors; outliers are questions that need a human decision.

## Hands-on Exercise
**Task:** Audit the messy order file and list every problem you find, with the code that found it.
**Tools:** Google Colab (free) with pandas; the synthetic order data above.
**Steps:**
1. Run the data cell above.
2. Run each of the 5 checks from the Explanation in its own cell.
3. For each problem, record in a text-cell table: the column, the order ID, the problem, and the code that found it.
4. Mark each problem as "error" or "needs a human decision".
5. Add one question you would ask the shop managers.
**What good looks like:** A table listing at least 7 problems: the duplicate, 2 missing values, price stored as text, dates stored as text, inconsistent city spellings, the negative quantity and the 500-unit outlier, each with working code.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Text column dtype names (str in pandas 3, object in earlier versions) and printed output formats differ between pandas versions. Outputs were produced with Python 3.11 and pandas 3.0.6.
- [VERIFY] Curriculum flag for L11–L15 (Gapminder source, access method and licence): this lesson uses only the synthetic order data, so no Gapminder check is needed here.
- The order data is synthetic and was created for this course, as the curriculum requires.
