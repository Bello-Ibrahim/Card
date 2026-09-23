# L18 Building an ML-Ready Table

Course: AI-11 · Module: M4 · Objectives: O6 · Video: 5 min (screen demo)

## Hook
Imagine a model that predicts returned orders with perfect accuracy in testing, and then fails completely with real customers. One common reason is a column that secretly contained the answer. This lesson shows how to build a table a model can learn from honestly.

## Explanation
An **ML-ready table** has a simple shape:

- **One row per example.** Each row is one thing you want to predict for, such as one order.
- **One target column.** The **target** (also called the label) is the value you want the model to predict, such as `returned` (1 for yes, 0 for no).
- **Feature columns, all numeric.** Every other column is a feature the model can use. After L16 and L17, these should contain only numbers, with no missing values.

Some columns must be **removed** before training:

- **Identifiers**, such as `order_id` or a customer name. They are unique labels, not information about the order. A model could memorise them, and that memory would be useless for new orders.
- **Leaky columns.** **Data leakage** happens when a feature contains information that would not be available at the moment of prediction, often because it is created **after** the outcome. A `refund` amount exists only because an order was returned, so it reveals the answer. A model trained with it looks excellent in testing and fails in real use.
- **Raw columns already converted**, such as the original date after you extracted month and weekday, or the text city column after one-hot encoding.

To test a column for leakage, ask: "At the moment I want to make the prediction, would I already know this value?" If the answer is no, remove it.

Finally, save the table with `to_csv("name.csv", index=False)`. `index=False` stops pandas from writing the row labels as an extra column. Splitting the data into training and test sets and training models are covered in the next course, AI-12.

**Analogy:** Leakage is like an exam where the answers are printed faintly on the back of the question paper. A student who notices them gets full marks, but has learned nothing, and fails the next exam that has no answers on the back. A model with a leaky column is that student.

## Worked Example
Anjali is a data analyst in Pune, India. The marketplace from L14 asks her to prepare a table for a future model that predicts whether an order will be returned. She starts from Hamza's `encoded` table from L17.

The presenter runs the earlier cells, then:

```python
print(encoded[["returned", "refund"]].head(3))
```

```
  returned  refund
0       no     0.0
1      yes    12.0
2       no     0.0
```

The presenter points out the pattern: the refund is above 0 only when the order was returned. That is leakage. Next:

```python
ml = encoded.copy()
ml["returned"] = (ml["returned"] == "yes").astype(int)
ml = ml.drop(columns=["order_id", "refund", "order_date"])
print(ml.shape)
print(ml.columns.tolist())
```

```
(8, 11)
['quantity', 'unit_price', 'returned', 'month', 'weekday', 'city_hanoi', 'city_lagos', 'city_lima', 'payment_card', 'payment_cash', 'payment_other']
```

The comparison `== "yes"` gives True or False, and `astype(int)` turns it into 1 or 0. Anjali checks that every column is numeric and then saves the file:

```python
print(ml.select_dtypes("number").shape[1] == ml.shape[1])
ml.to_csv("orders_ml_ready.csv", index=False)
```

```
True
```

She adds a warning to her notes: the target has only 1 returned order out of 8 rows. That is enough to practise the steps, but far too few examples for a real model. A real project needs many examples of each outcome.

## Common Mistake
Beginners often keep every column "because more data is better". But identifiers and leaky columns make a model look better in testing while making it worse in real use. The opposite mistake also happens: removing useful features because they "look similar" to the target. Use the timing question for each column, and write down why you kept or removed it.

## Key Takeaways
1. An ML-ready table has one row per example, one target column and only numeric feature columns with no missing values.
2. Remove identifiers, leaky columns (information available only after the outcome) and raw columns you have already converted.
3. Save the result with `to_csv(..., index=False)`, and note any limits, such as too few examples of one outcome.

## Hands-on Exercise
**Task:** From your cleaned file, choose a target and 5 features, explain why you removed 2 columns, and save an ML-ready CSV.
**Tools:** Google Colab (free) with pandas; your encoded order table from L17.
**Steps:**
1. Choose a target, for example `returned`, and convert it to 0 and 1.
2. For every other column, ask the timing question and decide: keep as a feature, or remove.
3. Keep at least 5 feature columns, for example `quantity`, `unit_price`, `weekday`, `month` and the city columns.
4. Remove at least 2 columns, such as `order_id` and `refund`, and write one sentence for each explaining why.
5. Check that all columns are numeric and that `ml.isna().sum().sum()` is 0.
6. Save the table with `to_csv("orders_ml_ready.csv", index=False)` and download it from the Colab file panel. [VERSION]
**What good looks like:** A CSV file with one target column and at least 5 numeric feature columns, no identifiers, no leaky columns and no missing values, plus a short note that explains each removed column and the small number of returned orders.
**Time:** about 25 minutes

## Review Flags
- [VERSION] The Colab file panel and its download option must be checked against the live interface.
- The order data is synthetic and created for this course, and every output was produced by running the code with Python 3.11 and pandas 3.0.6 (also tested with pandas 2.2.3).
