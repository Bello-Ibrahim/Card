# L18 Capstone Explain: Check, Interpret and Document

Course: AI-05 · Module: M4 · Objectives: O5, O6, O7 · Video: 5 min (screen demo)

## Hook
Your model has trained and the loss has fallen. But are the weights right, and what do they mean? A model you cannot check or explain is not finished. In this final lesson you will prove your result and explain it clearly.

## Explanation
Finishing the capstone takes four steps.

**1. Check the weights.** Linear regression is special: its best weights can also be calculated directly, without a loop. NumPy's `np.linalg.lstsq` ("least squares") does this. [VERSION] If your gradient descent weights match it to about two decimal places, your loop is correct. If not, check the learning rate, the number of steps and the sign of the error.

**2. Interpret each weight.** In words: each weight is the change in the prediction when its feature increases by 1 and the other features stay the same. The bias is the prediction when every feature is 0. That may not be a realistic situation, so interpret it with care.

**3. Compare with a baseline on the test set.** Calculate the training MSE and the test MSE, and the test MSE of the baseline from L16: always predicting the training mean. A test error close to the training error suggests the model is not overfitting. A test error far below the baseline shows that the model learned something useful. Report RMSE as well, because it is in the original units.

**4. Judge and document.** Ask the questions from L10 and L16: how many test examples are there, and could the difference be random? Then add a plain-language text cell before every code cell.

**Analogy:** Checking your weights with `lstsq` is like checking a long division on a calculator. You still did the work yourself, and you understand each step, but a second method confirms that you did not make a small slip along the way.

## Worked Example
Baraka continues with his hypothetical kiosk data from L17. A presenter can follow these steps in Colab on screen.

1. Add a text cell "3. Check with least squares" and a code cell underneath.
2. Run `lstsq` on the training data and compare with the loop's weights.
3. Add a text cell "4. Evaluate" and calculate training, test and baseline errors.

```python
w_ls, *_ = np.linalg.lstsq(X_tr, y_tr, rcond=None)
print(w_ls.round(2))                    # [2.02 3.75 6.53]
print(np.allclose(w, w_ls, atol=0.001)) # True
def mse(t, p): return np.mean((p - t) ** 2)
print(mse(y_tr, X_tr @ w).round(2))                  # 5.91 training
print(mse(y_te, X_te @ w).round(2))                  # 11.2 test
print(mse(y_te, np.full(5, y_tr.mean())).round(2))   # 348.01 baseline
```

The first result is a list of values; `w_ls, *_` keeps only the weights. [VERSION] The weights match the loop to better than 0.001.

**Interpretation (all values hypothetical):**

- **Sunshine: about 3.75.** With the same foot traffic, each extra hour of sunshine is linked to about 3.75 more drinks sold.
- **Foot traffic: about 6.53.** With the same sunshine, each extra hundred people passing is linked to about 6.5 more drinks.
- **Bias: about 2.02.** The model's prediction for a day with no sun and no passers-by. No such day is in the data, so Baraka does not rely on it.

**Evaluation:**

| | MSE | RMSE (drinks) |
|---|---|---|
| Training | 5.91 | 2.43 |
| Test | 11.2 | 3.35 |
| Baseline on test | 348.01 | 18.66 |

The test error is higher than the training error, which is normal, but still small: about 3 drinks, compared with about 19 for the baseline. The largest miss is the test day with 81 drinks, where the model predicted about 88.

**Judgement:** the improvement over the baseline is very large, so it is unlikely to be random. However, there are only 5 test days and 10 training days, so Baraka writes: "Promising, but check again after one more month of data." The weights show links in this data, not proof that sunshine causes sales.

## Common Mistake
Learners often write "the model is 96% better" or similar without saying better than what, on which data and with how many examples. Always name the metric, the data (training or test), the baseline and the sample size. A second mistake is describing weights as causes. A regression weight shows how the prediction changes with a feature; it does not prove that the feature causes the result.

## Key Takeaways
1. Confirm gradient descent weights with `np.linalg.lstsq`; matching weights prove the loop is correct.
2. Each weight is the change in prediction for one extra unit of its feature, with the other features fixed; it shows a link, not a cause.
3. Report training error, test error and a baseline together, with RMSE in real units and a clear note on sample size.

## Hands-on Exercise
**Task:** Capstone step 2: verify your result with `np.linalg.lstsq`, report training and test error against a baseline, and add a plain-language explanation for every step of the notebook.
**Tools:** Google Colab with your L17 notebook [VERSION]; NumPy only.
**Steps:**
1. Add the `lstsq` check and print whether your weights match.
2. Calculate training MSE, test MSE and baseline test MSE, and the RMSE of each. Put them in a small table in a text cell.
3. Write one sentence per weight explaining its meaning, including a caution about the bias.
4. Write a short judgement: is the model a real improvement, and what limits your confidence?
5. Add a text cell before every code cell explaining what it does and why, in plain language.
6. Check your notebook against the capstone rubric and submission checklist, then run all cells from the top to confirm that everything works.
**What good looks like:** Matching weights, a table with 5.91, 11.2 and 348.01, three clear weight interpretations, an honest note about the small test set, and a text explanation above every code cell.
**Time:** about 60 minutes

## Review Flags
- [VERSION] NumPy: confirm that `np.linalg.lstsq` with `rcond=None` returns four values, gives no warning, and matches the outputs shown in the current NumPy version (carried from the curriculum flags). Outputs were checked with NumPy 2.4.
- [VERSION] Google Colab: confirm the interface for adding text cells and running all cells before scripting the screen demo.
