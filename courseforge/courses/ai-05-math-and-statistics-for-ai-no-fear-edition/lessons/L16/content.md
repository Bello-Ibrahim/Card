# L16 Overfitting, Train/Test Splits and Baselines

Course: AI-05 · Module: M4 · Objectives: O5, O6 · Video: 5 min

## Hook
A student memorises every answer in last year's exam and scores 100% on it. Then the real exam has new questions, and the score falls to 50%. Models can do exactly the same thing. This lesson shows you how to catch it, and how to tell whether a model is worth using at all.

## Explanation
A model can fit its training data very closely and still fail on new data. This is called **overfitting**. The model has learned the noise and accidents in the training examples, not the general pattern. The opposite problem, a model too simple to capture the pattern, is called **underfitting**.

To detect overfitting, you never judge a model only on the data it learned from. Instead you use a **train/test split**:

- the **training set** is used to fit the weights;
- the **test set** is kept aside and used only at the end, to measure performance on examples the model has never seen.

A common split is about 70–80% for training and the rest for testing. Before splitting, you usually **shuffle** the rows randomly, so that both parts look similar.

Then compare two numbers: **training error** and **test error**.

- Both low and close together: the model generalises well.
- Training error very low but test error much higher: overfitting.
- Both high: underfitting.

Finally, every model needs a **baseline**: the simplest sensible prediction, which a real model must beat. For predicting numbers, a common baseline is "always predict the average of the training targets". For classification, it is "always predict the most common class", as in L15. If your model does not clearly beat the baseline on the test set, it has not learned anything useful. And remember L10: with a small test set, a small difference may be random variation.

**Analogy:** A baseline is like a weather forecaster who always says "tomorrow will be like today". It sounds too simple, but it is right surprisingly often. A new forecasting system is only worth paying for if it clearly beats that simple rule on days it has never seen.

## Worked Example
Lucía runs a hypothetical ice-cream kiosk in Guadalajara, Mexico. She records 10 days of temperature (°C) and cones sold. All values are invented. For simplicity, she uses the first 7 days for training and the last 3 for testing. With real data, shuffle first.

She compares three approaches:

1. **Baseline:** always predict the mean of the training sales, about 48.3 cones.
2. **Simple model:** a straight line, `sales = w × temperature + b`.
3. **Wiggly model:** a very flexible curve (a polynomial of degree 6) that can bend through every training point.

**Code:** `np.polyfit` finds the best curve of a chosen degree, and `np.polyval` uses it to predict. [VERSION]

```python
import numpy as np
temp  = np.array([18, 20, 22, 24, 26, 28, 30, 21, 25, 29])
sales = np.array([30, 38, 41, 50, 52, 61, 66, 40, 53, 60])
x_tr, y_tr, x_te, y_te = temp[:7], sales[:7], temp[7:], sales[7:]
def mse(t, p): return np.mean((p - t) ** 2)
print(mse(y_te, np.full(3, y_tr.mean())).round(2))  # baseline
for deg in [1, 6]:
    c = np.polyfit(x_tr, y_tr, deg)
    print(deg, mse(y_tr, np.polyval(c, x_tr)).round(2),
          mse(y_te, np.polyval(c, x_te)).round(2))
```

**Results (MSE):**

| Approach | Training MSE | Test MSE |
|---|---|---|
| Baseline (mean) | — | 76.03 |
| Straight line | 1.87 | 4.18 |
| Wiggly curve | 0.00 | 30.89 |

**Reading the results:** the wiggly curve is perfect on training data (MSE 0) but much worse on the test days. That is overfitting. The straight line has slightly higher training error but by far the lowest test error, and it beats the baseline clearly: 4.18 against 76.03. Lucía chooses the straight line. She also notes that 3 test days is a very small sample, so she will collect more days before relying on it.

## Common Mistake
The most common mistake is choosing the model with the lowest **training** error. That rewards memorising. Always compare models on the test set, and always include a baseline. A second, quieter mistake is to look at the test set many times while adjusting the model. Each look lets information leak in, so the test set slowly stops being "new". Keep it aside until the end.

## Key Takeaways
1. Overfitting means very low training error but much higher test error; the model memorised instead of learning the pattern.
2. Split data into training and test sets, fit only on training data, and judge the model on the test set.
3. Every model must clearly beat a simple baseline, such as the training mean, on the test set, and a small test set means extra caution.

## Hands-on Exercise
**Task:** Split a small dataset in NumPy, compare a baseline with a simple model on the test set, and decide whether the model is a real improvement.
**Tools:** Google Colab with NumPy.
**Steps:**
1. Use these hypothetical study hours and exam scores:
   `x = [2, 4, 5, 7, 8, 10, 3, 6, 9, 1]` and `y = [52, 60, 61, 70, 72, 80, 55, 66, 78, 49]`.
2. Shuffle the row positions with `idx = np.random.default_rng(1).permutation(10)`. Use the first 7 positions for training and the last 3 for testing.
3. Calculate the baseline test MSE, using the mean of the training scores.
4. Fit a straight line with `np.polyfit(..., 1)` on the training data, and calculate training and test MSE.
5. Repeat with degree 6 and compare.
6. Write three sentences: is the straight line a real improvement, and how confident are you with only 3 test examples?
**What good looks like:** With this seed, the baseline test MSE is 159.0, the straight line gives about 0.92 (training) and 0.29 (test), and degree 6 gives a test MSE in the thousands. Your notebook shows these side by side, and your conclusion mentions the small test set.
**Time:** about 30 minutes

## Review Flags
- [VERSION] NumPy: confirm that `np.polyfit` and `np.polyval` behave as shown and give no warning for the degree-6 fits in the current NumPy version, and that `default_rng(1).permutation(10)` still gives the same order. Outputs were checked with NumPy 2.4 with warnings treated as errors.
