# Capstone Rubric: Linear Regression from Scratch

## Task
Implement linear regression from scratch in a Google Colab notebook with NumPy only, and explain every calculation, from the data matrix to the final metrics. You build and train the model in L17 (capstone step 1) and check, evaluate and document it in L18 (capstone step 2). Use only the provided hypothetical kiosk dataset. Do not add personal or confidential data to the notebook.

## Deliverables
- A Colab notebook named "Linear regression from scratch" that runs from top to bottom without errors, using NumPy and Matplotlib only (no machine learning libraries).
- A data section that builds the feature matrix with a column of ones, splits it into 10 training rows and 5 test rows, and prints the shapes.
- A gradient descent training loop with a comment on every line, the learned weights and a plot of the loss falling during training.
- A check of the learned weights against `np.linalg.lstsq`.
- A results table with training MSE, test MSE and baseline test MSE (always predicting the training mean), with the RMSE of each.
- Text cells that explain every step in plain language, one sentence of interpretation per weight, and a short judgement on whether the model is a meaningful improvement.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Data matrix and predictions | O2 | Builds `X` with a column of ones, splits training and test rows correctly, prints and comments on every shape, and explains in words how `X @ w` makes one dot product per row. | Builds `X` with the ones column and correct split; shapes printed; the explanation of `X @ w` is brief but correct. | Matrix built but the ones column, the split or the shape checks are missing or partly wrong. | No data matrix, or predictions not made with matrix multiplication. | 20 |
| Loss, gradient and gradient descent | O4 | Implements MSE, the gradient `2 / n × Xᵀ @ error` and the update step correctly; the first loss is checked by hand; the loss curve falls and flattens; the choice of learning rate is justified with a comparison. | Correct loop with a falling loss curve and reasonable learning rate; limited explanation of the gradient or learning rate. | Loop runs, but the loss does not settle, the gradient sign or scale is wrong, or there is no loss plot. | No working training loop. | 25 |
| Verification and metrics | O5 | Weights match `np.linalg.lstsq` (for example with `np.allclose`); training, test and baseline MSE and RMSE are correct and shown in a table, with a clear statement of what each metric shows and hides. | Weights checked and metrics correct; the table or explanation of the metrics is incomplete. | Some metrics missing or calculated on the wrong data (for example, test error on training rows). | No verification and no metrics. | 20 |
| Judgement: baseline, overfitting and sample size | O6 | Compares test error with training error and the baseline, discusses overfitting, notes the small test set and says what more data would change; interprets weights as links, not causes. | Compares with the baseline and mentions sample size or overfitting; the judgement is reasonable. | Declares the model better or worse without a baseline or without considering sample size. | No judgement of the result. | 15 |
| Plain-language explanation of every calculation | O7 | A clear text cell before every code cell; every line of the loop commented; each weight interpreted with its units; a reader without a maths background could follow the notebook. | Most cells explained and weights interpreted; a few steps are explained only briefly. | Explanations are sparse, copied or use terms without explaining them. | No explanation text. | 20 |

Total: 100

## Submission Checklist
- My notebook runs from top to bottom with "Run all" and uses only NumPy and Matplotlib.
- I used only the provided hypothetical dataset and no personal or confidential data.
- My feature matrix has a column of ones, and I printed and commented on every shape.
- My training loop has a comment on every line, and I plotted the loss curve.
- I checked my first loss by hand and explained my choice of learning rate.
- My weights match `np.linalg.lstsq` to about two decimal places.
- I reported training MSE, test MSE and baseline test MSE, with RMSE, in a table.
- I wrote one sentence per weight and described the weights as links, not causes.
- I wrote a short judgement that mentions the baseline, overfitting and the small test set.
- Every code cell has a plain-language text cell before it.
