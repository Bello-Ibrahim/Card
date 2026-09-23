# L05 Matrix Multiplication as Many Predictions

Course: AI-05 · Module: M1 · Objectives: O2 · Video: 5 min (screen demo)

## Hook
In L03 you made one prediction with one dot product. But a real model may need to make a million predictions. Do you write a million lines of code? No. You write one short line, and matrix multiplication does the rest.

## Explanation
Here is the key idea in words: **multiplying a data matrix by a weight vector does one dot product for every row.** Each row is one example, so each dot product is one prediction. The result is a vector with one prediction per example.

Suppose `X` is a data matrix with 3 rows and 2 columns, and `w` is a weight vector with 2 numbers. Then:

- prediction for row 0 = row 0 · w
- prediction for row 1 = row 1 · w
- prediction for row 2 = row 2 · w

In NumPy you write this as `X @ w`. The `@` symbol means matrix multiplication.

**The shape rule.** Matrix multiplication only works when the shapes fit together. Write the two shapes next to each other: (3 × 2) and (2 × 1). The two **inner** numbers must be equal: here 2 and 2. This makes sense, because every row has 2 features and there must be exactly one weight for each feature. The two **outer** numbers give the shape of the result: 3 × 1, which is one prediction for each of the 3 examples.

If the inner numbers are different, for example (3 × 2) and (3 × 1), the multiplication is not defined. NumPy stops with an error. This error is your friend: it tells you that the number of weights does not match the number of features.

Note that order matters. `X @ w` is not the same as `w @ X`, and often only one of them is allowed by the shape rule.

**Analogy:** Think of a cashier with a price list. Each customer's basket is one row of the matrix. The price list is the weight vector. The cashier calculates one bill for every customer in the queue with the same price list. Matrix multiplication is the whole queue served in one go. The shape rule simply says that the price list must have one price for every type of item in the baskets.

## Worked Example
Linh runs a hypothetical online clothing shop in Hanoi, Viet Nam. She sells shirts and pairs of socks. In this invented example, a shirt costs 10 and a pair of socks costs 3 (in any currency). Three orders arrived today:

| Order | Shirts | Socks |
|---|---|---|
| 0 | 2 | 1 |
| 1 | 3 | 4 |
| 2 | 5 | 2 |

**Picture:** the table is a 3 × 2 matrix `X`. The prices `[10, 3]` form the weight vector `w` with 2 numbers (shape 2 × 1).

**Hand calculation:** one dot product per row.

- Order 0: 2 × 10 + 1 × 3 = 20 + 3 = 23
- Order 1: 3 × 10 + 4 × 3 = 30 + 12 = 42
- Order 2: 5 × 10 + 2 × 3 = 50 + 6 = 56

Shapes: (3 × 2) times (2 × 1) gives (3 × 1). Three totals: 23, 42 and 56.

**Code:** a presenter can follow these steps on screen in Colab.

1. Create the matrix and the weights, and print both shapes.
2. Multiply with `@` and compare with the hand calculation.
3. Make a shape error on purpose by adding a third weight, run the cell and read the error.

```python
import numpy as np
X = np.array([[2, 1], [3, 4], [5, 2]])
w = np.array([10, 3])
print(X.shape, w.shape)   # (3, 2) (2,)
print(X @ w)              # [23 42 56]
X @ np.array([10, 3, 1])  # ValueError: matmul: ... mismatch ...
```

The last line produces a `ValueError` that says there is a "mismatch in its core dimension" and "size 3 is different from 2". [VERSION] In plain words: the matrix has 2 columns but you gave 3 weights. Notice also that NumPy shows the shape of `w` as `(2,)`, a plain vector with 2 numbers. NumPy treats it as 2 × 1 when you multiply.

## Common Mistake
Learners often "fix" a shape error by changing the data until the error goes away, for example by adding a column of zeros. The code then runs, but the model is wrong. Instead, read the two shapes, find which inner numbers differ and ask why. Usually a feature is missing, a weight is extra, or the data needs a transpose. Always write the expected shapes as a comment before you multiply.

## Key Takeaways
1. `X @ w` performs one dot product per row, so it makes a prediction for every example at once.
2. The inner sizes must match: (3 × 2) times (2 × 1) works, and the outer sizes give the result shape, 3 × 1.
3. A shape error means the number of weights does not match the number of features; read the shapes before you change anything.

## Hands-on Exercise
**Task:** Multiply a 3 × 2 matrix by a 2 × 1 vector by hand, check it with the `@` operator in NumPy, and explain one shape error on purpose.
**Tools:** Pen and paper; Google Colab with NumPy.
**Steps:**
1. Use `X = [[1, 4], [2, 0], [3, 5]]` and `w = [2, 1]`.
2. Write the shapes and predict the shape of the result before you calculate.
3. Calculate the three dot products by hand, showing each multiplication.
4. In Colab, create `X` and `w` with `np.array`, print both shapes and print `X @ w`.
5. Change `w` to three numbers, run the cell again and copy the last line of the error.
6. In a text cell, explain the error in one or two plain sentences.
**What good looks like:** Your hand result and NumPy both give `[6, 4, 11]`. Your explanation says that `X` has 2 columns but `w` has 3 numbers, so the inner sizes do not match.
**Time:** about 20 minutes

## Review Flags
- [VERSION] NumPy: the `@` operator is stable, but confirm the exact wording of the shape-mismatch `ValueError` against the current NumPy version before scripting the screen demo. The message shown was checked with NumPy 2.4.
- All prices and orders are hypothetical.
