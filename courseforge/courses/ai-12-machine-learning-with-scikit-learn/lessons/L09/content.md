# L09 Probabilities, Thresholds and ROC Curves

Course: AI-12 · Module: M2 · Objectives: O4, O5 · Video: 6 min (screen demo)

## Hook
In L08 the model found only 7 of 60 subscribers. You do not need a new model to do better. The model already gives a probability for every customer; the 0.5 cut-off was simply a default. Move the cut-off, and you change the trade-off between false alarms and missed cases.

## Explanation
`predict_proba` returns the model's probability of "yes". `predict` turns it into a decision with a threshold of 0.5. You can choose any threshold yourself:

```python
pred = (proba >= 0.3).astype(int)
```

- A **lower threshold** flags more cases: recall goes up, precision usually goes down.
- A **higher threshold** flags fewer cases: precision usually goes up, recall goes down.

Two tools help you see all thresholds at once:

- The **ROC curve** plots the share of real positives found (recall) against the share of negatives wrongly flagged, for every threshold. **ROC AUC** summarises it in one number: the chance that the model gives a random positive case a higher probability than a random negative case. 0.5 is random guessing and 1.0 is perfect ranking. ROC AUC does not depend on the threshold, so it measures how well the model *ranks* cases.
- The **precision-recall curve** plots precision against recall. With rare positive classes, it is often more informative than the ROC curve, because it focuses on the positive cases.

`RocCurveDisplay.from_estimator` and `PrecisionRecallDisplay.from_estimator` draw these curves in one line. [VERSION]

How do you pick the threshold? Put a cost on each mistake and choose the threshold with the lowest total cost. Choose it on **training data with cross-validated predictions**, not on the test set, so the test set stays a fair final check. Recent releases also include `TunedThresholdClassifierCV`, which automates this search. [VERSION]

**Analogy:** A threshold is like the height of a net in a fishing boat. Lower the net and you catch more fish, but also more weeds. Raise it and you catch less weed, but some fish escape. The right height depends on how much a fish is worth compared with the time spent sorting weeds.

## Worked Example
Dr. Wanjiru Kamau runs a hypothetical community clinic in Nairobi. Her team uses a risk score to decide whom to call for a free screening. Missing a patient who needs care is much worse than making an extra phone call, so she prefers a low threshold. To practise without any patient data, her analyst uses the term-deposit model from L05, which has the same shape of problem.

On screen, the presenter runs:

```python
import numpy as np
from sklearn.metrics import roc_auc_score, precision_score, recall_score

proba = pipe.predict_proba(X_test)[:, 1]
print("ROC AUC:", round(roc_auc_score(y_test, proba), 3))
for t in [0.5, 0.3, 0.15]:
    pred = (proba >= t).astype(int)
    print(t, round(precision_score(y_test, pred), 3), round(recall_score(y_test, pred), 3))
```

Output (scikit-learn 1.9.1): [VERSION]

```
ROC AUC: 0.752
0.5 0.583 0.117
0.3 0.396 0.317
0.15 0.292 0.667
```

At 0.15 the model finds two thirds of subscribers, but only about 29% of flags are correct. Now the presenter adds costs: a false positive (an unneeded call) costs 1 unit and a false negative (a missed case) costs 8 units.

```python
from sklearn.model_selection import cross_val_predict

cv_proba = cross_val_predict(pipe, X_train, y_train, cv=5,
                             method="predict_proba")[:, 1]

def total_cost(t, cost_fp=1, cost_fn=8):
    fp = ((cv_proba >= t) & (y_train == 0)).sum()
    fn = ((cv_proba < t) & (y_train == 1)).sum()
    return cost_fp * fp + cost_fn * fn

thresholds = np.arange(0.05, 0.95, 0.05)
costs = [total_cost(t) for t in thresholds]
print(round(thresholds[np.argmin(costs)], 2), min(costs), total_cost(0.5))
```

Output: `0.1 813 1381` [VERSION]

On the training folds, a threshold of 0.1 costs 813 units against 1,381 at the default 0.5. With these costs, a low threshold is clearly better.

## Common Mistake
Learners often think a better threshold makes a better model. It does not: the threshold changes the *decisions*, not the model's ability to rank cases. ROC AUC stays at 0.752 whatever threshold you pick. If ranking is weak, you need better features or a better model (Module 3). Also, never tune the threshold on the test set, for the same reason you do not tune any other setting there.

## Key Takeaways
1. `predict_proba` gives probabilities; the threshold turns them into decisions and trades precision against recall.
2. ROC AUC measures how well the model ranks cases, independent of any threshold; precision-recall curves are more useful for rare positives.
3. Choose the threshold from the business cost of each mistake, using cross-validated predictions on training data.

## Hands-on Exercise
**Task:** Given a cost for each false positive and false negative, find the threshold that gives the lowest total cost.
**Tools:** Google Colab (free), scikit-learn, NumPy; your L05 pipeline.
**Steps:**
1. Get cross-validated probabilities on the training set with `cross_val_predict(..., method="predict_proba")`.
2. Use the costs from the example (1 and 8), then try your own pair, such as 5 and 20.
3. Calculate the total cost for thresholds from 0.05 to 0.90 and plot cost against threshold.
4. Mark the lowest point and write down the threshold.
5. Apply that threshold once to the test set and print precision, recall and the confusion matrix.
6. Draw the ROC and precision-recall curves with the display classes.
**What good looks like:** A cost plot with a clear minimum, one chosen threshold for each cost pair, test results at that threshold, and a sentence explaining why the choice changes when the costs change.
**Time:** about 30 minutes

## Review Flags
- [VERSION] `RocCurveDisplay`, `PrecisionRecallDisplay` and `TunedThresholdClassifierCV` depend on the installed version. Outputs were recorded with scikit-learn 1.9.1, NumPy 2.4 and Python 3.11 on synthetic data.
- The clinic case is hypothetical on purpose (curriculum flag), to avoid unverified claims about real organisations; no patient data is used.
