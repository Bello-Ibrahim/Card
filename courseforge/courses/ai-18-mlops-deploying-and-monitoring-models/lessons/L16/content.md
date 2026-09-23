# L16 Detecting Data and Prediction Drift

Course: AI-18 · Module: M4 · Objectives: O5, O6 · Video: 5 min (screen demo)

## Hook
Nothing in your code changed and your tests still pass. But the data your model sees today is not the data it learned from. How do you notice, and what should you do?

## Explanation
**Drift** means production data no longer looks like the training data. Three kinds matter:

- **Data drift:** the distribution of an input feature changes, for example average alcohol rises.
- **Prediction drift:** the distribution of the model's outputs changes, for example many more "good" predictions.
- **Concept drift:** the relationship between inputs and the true outcome changes. You can only measure it when true labels arrive.

To detect drift, compare a **reference** sample (training data) with a **current** sample (recent requests from your log), feature by feature.

Two common methods:

- **Kolmogorov-Smirnov (KS) test:** measures the largest gap between two cumulative distributions and gives a p-value. With thousands of rows, even tiny, harmless differences become "significant", so do not use the p-value alone.
- **Population stability index (PSI):** split the reference into bins, then compare the share of rows in each bin: `PSI = sum((current% - reference%) * ln(current% / reference%))`. It measures the size of the shift, not only whether one exists.

```python
import numpy as np
from scipy.stats import ks_2samp

def psi(expected, actual, bins=10):
    edges = np.quantile(expected, np.linspace(0, 1, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    e = np.histogram(expected, edges)[0] / len(expected)
    a = np.histogram(actual, edges)[0] / len(actual)
    e, a = np.clip(e, 1e-6, None), np.clip(a, 1e-6, None)
    return float(np.sum((a - e) * np.log(a / e)))

for col in train.columns:
    ks = ks_2samp(train[col], new[col])
    print(f"{col:17s} PSI={psi(train[col], new[col]):.3f}  KS p={ks.pvalue:.3g}")
```

A frequently quoted **rule of thumb** says PSI below 0.1 means little change, 0.1 to 0.25 means a moderate change, and above 0.25 means a large change. [VERIFY] These are conventions from practice, not a formal standard. Calibrate them on your own data, for example by computing PSI between two normal weeks.

Drift is a signal, not a decision. For each alert, choose one of three responses:

1. **Retrain** when the change is real, lasting and affects important features, and you have new labelled data.
2. **Investigate** when the cause is unclear: it may be a data pipeline bug, such as a unit change, not a real-world change.
3. **Ignore** when the feature has little effect on predictions, or the change is expected and temporary.

**Analogy:** Drift detection is like a shop that sells winter coats and checks who walks in. If the customers suddenly look different, it first asks why before changing its stock.

## Worked Example
Sofía Castro is a risk analyst at a hypothetical consumer lender in Medellín, Colombia. Her credit model was trained on applicants who mostly came through bank branches. After a new online marketing campaign, many younger applicants with shorter credit histories apply. Her monitoring shows PSI above her calibrated alert level for "age" and "months of credit history", and the approval rate falls. Her team decides to **investigate** first: they confirm that the change is real, not a data error, and see that it will last. They then **retrain** with recent labelled applications and review fairness across age groups before promotion. Credit decisions can be regulated, so the review follows local lending rules. [REGION]

On screen, the presenter simulates the same idea with the wine model:

1. Load the reference sample: `train, _ = load_data(seed=42)`.
2. Create a new batch: `new, _ = load_data(seed=7)`.
3. Simulate drift in one feature: `new["alcohol"] = new["alcohol"] + 0.8`.
4. Run the PSI and KS loop above. The real output was:

```text
alcohol           PSI=0.505  KS p=1.54e-65
volatile_acidity  PSI=0.003  KS p=0.863
sulphates         PSI=0.011  KS p=0.786
citric_acid       PSI=0.006  KS p=0.415
```

5. Point out that only `alcohol` shifted; the other features have PSI close to 0.
6. Compute PSI on the model's predicted probabilities for both batches to check prediction drift.
7. Write the decision on screen: "Investigate: check whether the alcohol measurement or unit changed at the source; retrain only if the change is real and labels are available."

## Common Mistake
Many learners retrain automatically every time a drift test fires. If the cause is a broken data pipeline, such as a unit change, retraining teaches the model the bug. Investigate the cause first, and keep retraining behind the champion-challenger comparison from L14.

## Key Takeaways
1. Data drift, prediction drift and concept drift are different; only concept drift needs true labels to measure.
2. Use PSI to measure the size of a shift and KS as a supporting test; treat common PSI thresholds as rules of thumb and calibrate them.
3. For each drift alert, decide to retrain, investigate or ignore, and investigate before retraining.

## Hands-on Exercise
**Task:** Simulate drift by changing one feature in a new batch of requests. Detect it with a statistical test, and write a short decision: retrain, investigate or ignore.
**Tools:** Python with NumPy, SciPy and pandas (free), your prediction log or `load_data()`.
**Steps:**
1. Take a reference sample from your training data.
2. Create a new batch of at least 500 rows and change one feature (shift, scale or replace some values).
3. Compute PSI and the KS p-value for every feature.
4. Compute PSI for the predicted probabilities of both batches.
5. Calibrate: compute PSI between two unchanged batches and compare.
6. Write a decision of three to five sentences: retrain, investigate or ignore, with your evidence.
**What good looks like:** A table in which the changed feature clearly stands out, a calibration value for unchanged data, a prediction-drift result, and a decision that names the likely cause and the next action.
**Time:** about 35 minutes

## Review Flags
- [VERIFY] PSI thresholds (0.1 and 0.25) are commonly quoted rules of thumb, not standards; confirm the wording presents them that way.
- [VERIFY] The credit-model drift example is hypothetical.
- [REGION] Lending regulations and fairness review requirements differ by country; no specific rule is stated.
- PSI and KS outputs are real results from the synthetic fallback data (SciPy 1.17.1, NumPy 2.4.6).
