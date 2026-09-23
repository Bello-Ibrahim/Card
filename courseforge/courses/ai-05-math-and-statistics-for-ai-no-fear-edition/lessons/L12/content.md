# L12 Loss Functions: How Wrong Is the Model?

Course: AI-05 · Module: M3 · Objectives: O4, O5 · Video: 5 min

## Hook
A model makes five predictions. Two are almost perfect, two are a little wrong and one is badly wrong. Is this a good model? To improve anything, you first need to measure it, and that means turning all those errors into one number.

## Explanation
An **error** (also called a **residual**) is the difference between a prediction and the true value. In words: prediction minus truth. A positive error means the model predicted too high; a negative one means too low.

A **loss function** combines all the errors into a single number that tells you how wrong the model is overall. A smaller loss means a better fit. **Training** a model means searching for the weights that make the loss as small as possible. So the loss is the model's "score to beat", and every learning step in L14 tries to reduce it.

The most common loss for predicting numbers is the **mean squared error (MSE)**. In words: take each error, square it, then take the mean of the squares. As a formula:

`MSE = mean((y_pred − y_true)²)`

Here `y_true` is the vector of true values and `y_pred` is the vector of predictions.

Why square the errors?

1. **Squares are never negative.** An error of −10 and an error of +10 would cancel each other if we simply added them. After squaring, both count as 100.
2. **Big errors count much more.** An error of 2 becomes 4, but an error of 30 becomes 900. MSE strongly punishes large mistakes, which is often what we want.
3. **It is smooth.** The square has a simple derivative, which makes gradients easy to calculate in L13.

Two related measures help with interpretation:

- **RMSE** (root mean squared error) is the square root of MSE. It is back in the original units, such as lira or minutes.
- **MAE** (mean absolute error) is the mean of the errors without their signs. It treats every unit of error equally, so it is less affected by one large error.

**Analogy:** MSE is like a teacher who marks late homework with a penalty that grows faster and faster: one day late loses 1 point, two days lose 4 points, five days lose 25. A few small delays hardly matter, but one very late assignment costs a lot. The model, like the student, learns that big mistakes are the ones to avoid.

## Worked Example
Emre is a hypothetical data analyst for a taxi app in Istanbul, Türkiye. He compares five fare predictions with the real fares. All values are invented, in lira.

| Trip | True fare | Predicted | Error | Squared error |
|---|---|---|---|---|
| 1 | 120 | 110 | −10 | 100 |
| 2 | 85 | 90 | 5 | 25 |
| 3 | 200 | 230 | 30 | 900 |
| 4 | 60 | 58 | −2 | 4 |
| 5 | 150 | 150 | 0 | 0 |

**Hand calculation:** the squared errors add up to 100 + 25 + 900 + 4 + 0 = 1,029. The mean is 1,029 ÷ 5 = 205.8. So MSE = 205.8, and RMSE is the square root, about 14.3 lira.

Look at trip 3. Its squared error of 900 is about 87% of the total 1,029. One large mistake dominates the loss. MAE tells a different story: (10 + 5 + 30 + 2 + 0) ÷ 5 = 9.4 lira, a typical error size.

**Code:**

```python
import numpy as np
def mse(y_true, y_pred):
    return np.mean((y_pred - y_true) ** 2)

y_true = np.array([120, 85, 200, 60, 150])
y_pred = np.array([110, 90, 230, 58, 150])
print(mse(y_true, y_pred))         # 205.8
print(np.sqrt(mse(y_true, y_pred)))  # about 14.35
```

Emre learns two things. The model is close on most trips, and the biggest improvement would come from understanding trip 3, perhaps a long airport trip.

## Common Mistake
Learners often compare an MSE directly with the size of the data. They see "205.8" and think the model is off by 205.8 lira. It is not: MSE is in **squared** units. Take the square root to get RMSE (about 14.3 lira) before you describe the error size to anyone. A second mistake is to compare MSE values from different datasets. MSE depends on the scale of the target, so it is useful only for comparing models on the same data.

## Key Takeaways
1. A loss function turns all prediction errors into one number, and training searches for weights that make it as small as possible.
2. MSE is the mean of the squared errors; squaring removes signs and punishes big errors much more than small ones.
3. MSE is in squared units: report RMSE (its square root) or MAE when you explain error size in plain language.

## Hands-on Exercise
**Task:** Calculate the mean squared error for five predictions by hand, then write a NumPy function `mse(y_true, y_pred)` and test it.
**Tools:** Pen and paper or a free spreadsheet; Google Colab with NumPy.
**Steps:**
1. Use hypothetical true values `[3, 5, 2, 8, 6]` and predictions `[4, 5, 1, 6, 9]`.
2. Make a table with columns for error and squared error, and calculate the MSE by hand.
3. In Colab, write the `mse` function from the worked example.
4. Test it with your numbers. Then test it with `y_pred` equal to `y_true` and confirm the answer is 0.
5. Change one prediction so that its error is 10. Recalculate and describe how much the MSE changed.
6. Calculate RMSE and MAE too, and write one sentence on which you would report to a non-technical colleague.
**What good looks like:** Errors 1, 0, −1, −2 and 3; squared errors 1, 0, 1, 4 and 9; MSE = 15 ÷ 5 = 3. Your function returns 3.0 and 0.0 for the two tests, and your sentence explains that RMSE or MAE are in the original units.
**Time:** about 25 minutes

## Review Flags
- None. All fares and values are hypothetical, and every calculation and code output shown was recalculated with NumPy 2.4.
