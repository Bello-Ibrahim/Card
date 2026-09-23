# L17 Capstone Build: Linear Regression from Scratch

Course: AI-05 · Module: M4 · Objectives: O2, O4, O7 · Video: 5 min (screen demo)

## Hook
Four weeks ago, a page of maths symbols may have made you nervous. Today you will build a working machine learning model yourself, and every line uses an idea you have already calculated by hand.

## Explanation
**Linear regression** predicts a number as a weighted sum of features plus a bias. For one feature it is `y = w*x + b`. Here is how the course fits together:

1. **Data as a matrix (L04).** Each row of `X` is one example. We add a first column of ones, so that the bias becomes just another weight: `w = [bias, w1, w2]`.
2. **Predictions with matrix multiplication (L05).** `X @ w` makes one prediction per row.
3. **Loss (L12).** The error is prediction minus truth, and the loss is the mean squared error.
4. **Gradient (L13).** For MSE, the gradient for all weights at once is `2 / n × Xᵀ @ error`. In words: for each weight, multiply every error by that weight's feature value, add them up, and scale by 2 ÷ n. This is the chain rule from L13 for every weight at once.
5. **Gradient descent (L14).** Repeat: predict, measure the error, calculate the gradient, step against it.

**Shapes are your safety check.** With 10 training rows and 3 columns: `X_tr` is (10, 3), `w` has 3 numbers, `X_tr @ w` gives 10 predictions, `X_tr.T` is (3, 10), and `X_tr.T @ err` gives 3 numbers: one gradient value per weight. If a shape is different, stop and check.

**The capstone brief.** Implement linear regression with NumPy only on the dataset below. Train with gradient descent, plot the loss falling, and keep 5 rows as a test set for L18.

**Analogy:** Building this model is like assembling flat-pack furniture from parts you have already inspected. The matrix is the frame, the loss is the spirit level that shows what is uneven, and gradient descent is the small adjustments you make until the level reads flat.

## Worked Example
Baraka runs a hypothetical cold-drink kiosk in Mombasa, Kenya. For 15 invented days he has hours of sunshine, foot traffic (hundreds of people passing) and drinks sold, which he wants to predict. The first 10 days are for training and the last 5 are the test set.

**Hand check before coding:** all weights start at 0, so every first prediction is 0. The first loss is therefore the mean of the squared sales of the 10 training days, about 3,284.7.

**Code:** a presenter can follow these steps in Colab on screen.

1. Add a text cell "1. Data" and the data code. Check that `X.shape` is (15, 3).
2. Add a text cell "2. Training" and type the loop, explaining each line aloud.
3. Run it and show the weights, the losses and the loss curve.

```python
import numpy as np
import matplotlib.pyplot as plt
# Hypothetical data: sunshine hours, foot traffic (hundreds), drinks sold
sun     = np.array([10, 7, 7, 9, 6, 8, 9, 3, 1, 4, 3, 9, 10, 1, 5])
traffic = np.array([7, 2, 7, 1, 4, 7, 3, 3, 3, 6, 3, 8, 4, 4, 5])
drinks  = np.array([89, 41, 74, 41, 49, 73, 58, 31, 28, 57, 34, 81, 67, 33, 55])
X = np.column_stack([np.ones(15), sun, traffic])  # (15, 3)
X_tr, y_tr = X[:10], drinks[:10]   # training rows
X_te, y_te = X[10:], drinks[10:]   # test rows for L18
w = np.zeros(3)                    # [bias, w_sun, w_traffic]
lr, losses = 0.01, []
for step in range(5000):
    err = X_tr @ w - y_tr                   # prediction - truth
    losses.append(np.mean(err ** 2))        # MSE
    grad = 2 / len(y_tr) * X_tr.T @ err     # gradient
    w = w - lr * grad                       # step downhill
print(w.round(2))                  # [2.02 3.75 6.53]
print(round(losses[0], 1), round(losses[-1], 2))  # 3284.7 5.91
plt.plot(losses); plt.yscale("log"); plt.show()
```

The loss falls from 3,284.7 to 5.91: steeply, then flat. The weights are a bias of about 2.02, about 3.75 drinks per hour of sunshine and about 6.53 drinks per hundred people passing.

4. Show a learning rate of 0.02: the loss explodes and NumPy prints overflow warnings. This is divergence (L14). [VERSION]

## Common Mistake
The most common capstone mistake is forgetting the column of ones. The model then has no bias and must pass through zero, so the fit is worse. The second is writing `y_tr - X_tr @ w`: with the error reversed, the gradient has the wrong sign and the loss grows. Keep "prediction minus truth", as in L12.

## Key Takeaways
1. Linear regression is `X @ w`: a dot product of features and weights for every row, with a column of ones for the bias.
2. Training repeats four lines: predict, calculate the error, calculate the gradient `2 / n × Xᵀ @ error`, and step against it.
3. Check shapes, check the first loss by hand and plot the loss curve; a steep fall followed by a flat line means training worked.

## Hands-on Exercise
**Task:** Capstone step 1: in Colab, implement linear regression with NumPy only on the provided hypothetical dataset, and plot the loss falling during training.
**Tools:** Google Colab [VERSION]; NumPy and Matplotlib only (no machine learning libraries).
**Steps:**
1. Create a new notebook named "Linear regression from scratch".
2. Add the data cell, print all shapes and write the expected shapes in a comment.
3. Calculate the first loss before training.
4. Type the training loop yourself. Add a comment on every line in your own words.
5. Train for 5,000 steps with a learning rate of 0.01, print the weights and plot the loss curve.
6. Try a smaller learning rate and describe how the curve changes.
7. Save the notebook. Use only the provided dataset, never personal or confidential data.
**What good looks like:** Weights close to `[2.02, 3.75, 6.53]`, a loss that falls from about 3,284.7 to about 5.91, a labelled loss plot and a comment on every line of the loop.
**Time:** about 60 minutes

## Review Flags
- [VERSION] Google Colab: confirm current sign-in requirements, free usage limits and the interface before scripting the screen demo (carried from the curriculum flags).
- [VERSION] NumPy: confirm that the learning rate of 0.02 still produces overflow `RuntimeWarning` messages, and that all outputs shown match the current Colab NumPy version. Outputs were checked with NumPy 2.4.
