# L04 Matrices: A Whole Dataset at Once

Course: AI-05 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
You already know how to read a spreadsheet: each row is one record and each column is one kind of information. Good news: that is almost exactly what a matrix is. You have been using matrices for years without the name.

## Explanation
A **matrix** is a rectangle of numbers arranged in rows and columns. In machine learning, a data matrix follows one simple rule:

- each **row** is one **example** (one day, one customer, one flat);
- each **column** is one **feature** (temperature, age, price).

So each row of a matrix is a vector, like the vectors in L02. A matrix is many vectors stacked on top of each other.

The **shape** of a matrix tells you its size as "rows × columns". A matrix with 4 rows and 3 columns has shape 4 × 3, which you read as "four by three". In NumPy, `X.shape` gives `(4, 3)`. The shape is the first thing to check in any dataset, because it tells you how many examples and how many features you have. By tradition, a data matrix is called `X` with a capital letter, and a vector is written with a small letter, such as `w`.

To get one number, you give its row and its column. NumPy counts from **0**, not 1, so the first row is row 0. `X[1, 2]` means "row 1, column 2", which is the second row and the third column.

To select a whole column, you use a colon, which means "all rows": `X[:, 2]` is every value in column 2. To select a whole row, give only the row number: `X[1]`.

The **transpose** flips a matrix so that rows become columns and columns become rows. In words: the first row becomes the first column. A 4 × 3 matrix becomes 3 × 4. In NumPy you write `X.T`. You will need the transpose in the capstone, when you calculate gradients.

**Analogy:** A matrix is like the seating plan of a cinema. Every seat has a row and a seat number, and you need both to find one seat. A whole row is one line of seats, and a column is every seat with the same number, from front to back. Transposing is like turning the plan on its side so that you read it from the side of the room.

## Worked Example
Zofia manages a hypothetical bicycle rental shop in Kraków, Poland. She records four days in a spreadsheet with three columns: temperature in °C, rain in millimetres and bikes rented. The numbers are invented.

| Day | Temperature | Rain | Bikes rented |
|---|---|---|---|
| 1 | 18 | 0 | 120 |
| 2 | 22 | 2 | 95 |
| 3 | 15 | 10 | 40 |
| 4 | 25 | 0 | 150 |

**Picture:** the table itself. Four rows, three columns, so the shape is 4 × 3.

**Hand calculation:** row 1 (the second day) is `[22, 2, 95]`. Column 2 (bikes rented) is `[120, 95, 40, 150]`. The value at row 1, column 2 is 95.

**Code:**

```python
import numpy as np
X = np.array([[18, 0, 120],
              [22, 2, 95],
              [15, 10, 40],
              [25, 0, 150]])
print(X.shape)      # (4, 3)
print(X[:, 2])      # [120  95  40 150]
print(X[1])         # [22  2 95]
print(X[1, 2])      # 95
print(X.T.shape)    # (3, 4)
```

Zofia notices something important. Bikes rented is the value she wants to predict, so it should not sit in the same matrix as the inputs. In machine learning we usually split the table into a feature matrix `X` (temperature and rain) and a target vector `y` (bikes rented). You will do this in the capstone.

## Common Mistake
The most common mistake is counting from 1. A learner wants the first column and writes `X[:, 1]`, but gets the second column. NumPy starts at 0, so the first column is `X[:, 0]`. A second mistake is mixing up the order inside the brackets. It is always row first, then column. If a result looks strange, print `X.shape` and the selected values, and compare them with the table.

## Key Takeaways
1. A data matrix stores one example per row and one feature per column, and its shape is "rows × columns".
2. NumPy counts from 0: `X[1, 2]` is the second row and third column, `X[:, 2]` is a whole column and `X[1]` is a whole row.
3. The transpose `X.T` swaps rows and columns, so a 4 × 3 matrix becomes 3 × 4.

## Hands-on Exercise
**Task:** Build a 6 × 3 NumPy matrix from a small hypothetical sales table, print its shape, select one column and one row, and transpose it.
**Tools:** A spreadsheet (Google Sheets or any free spreadsheet app) or paper; Google Colab with NumPy.
**Steps:**
1. Invent a sales table with 6 rows (days or shops) and 3 columns, for example price, advertising spend and units sold. Use made-up numbers, not real company data.
2. Write down, before any code, what shape you expect.
3. Type the table into Colab as `X = np.array([...])`, with one inner list per row.
4. Print `X.shape`, the units-sold column, the fourth row, and one single value.
5. Print `X.T` and its shape, and describe in one sentence what changed.
6. Split the table into `X` (first two columns) and `y` (last column) with `X[:, :2]` and `X[:, 2]`. Here `:2` means "columns 0 and 1, stopping before 2".
**What good looks like:** The shape prints as `(6, 3)` and the transpose as `(3, 6)`. Each selected value matches the value you expected from your table, and you can explain why the fourth row is `X[3]`.
**Time:** about 20 minutes

## Review Flags
- None. All data is hypothetical, and the NumPy indexing and output shown were run and confirmed; no tool interface or external fact needs checking.
