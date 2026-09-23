# L15 Which Features Matter? Interpreting Models

Course: AI-12 · Module: M4 · Objectives: O4, O6 · Video: 6 min (screen demo)

## Hook
A sales manager asks, "Your model says who will subscribe. Why those people?" If your only answer is "the algorithm decided", she will not trust it, and she should not. Today you learn three ways to see which features drive a model, and the limits of each.

## Explanation
**Coefficients** (linear and logistic models, L06) show the direction and size of each feature's effect in the model, if features are scaled. They are simple, but they only exist for linear models, and related features can share weight in confusing ways.

**Tree feature importances** (`feature_importances_` in random forests and many tree models) measure how much each feature improved the splits during training. They are quick, but they have two known weaknesses: they are calculated on training data, and they tend to favour numeric features with many distinct values over features with few values. [VERIFY]

**Permutation importance** (`sklearn.inspection.permutation_importance`) works with any model, including a whole pipeline. It takes one column at a time, shuffles its values randomly, and measures how much the score drops. If shuffling a column hurts the score a lot, the model relies on it. If the score barely moves, the model does not need it. Run it on **held-out data**, so it shows what matters for new customers, not what the model memorised. Because it works on the original columns of a pipeline, it gives one number for "job", not one per one-hot column. [VERSION]

Three limits apply to all of these methods:

- **Importance is not cause.** A feature can be important because it is linked to the real cause. Changing the feature does not necessarily change the outcome.
- **Correlated features share importance.** If two columns carry the same information, shuffling one does little harm, because the other still carries it. Both may look unimportant.
- **Importance describes this model on this data**, not the world in general.

**Analogy:** Permutation importance is like testing which instruments a band needs by muting them one at a time. If the song falls apart without the drums, the drums matter. But if two guitars play the same part, muting either one changes little, and you might wrongly decide that neither guitar matters.

## Worked Example
Tan Mei Lin is a data scientist at a hypothetical bank in Kuala Lumpur, Malaysia. She must explain the term-deposit model to the sales team. She continues from the L05 notebook, where `pipe` (the logistic regression pipeline) is fitted.

On screen, the presenter runs:

```python
from sklearn.inspection import permutation_importance
import pandas as pd

result = permutation_importance(pipe, X_test, y_test, scoring="roc_auc",
                                n_repeats=20, random_state=42)
imp = pd.DataFrame({"mean": result.importances_mean, "std": result.importances_std},
                   index=X_test.columns)
print(imp.sort_values("mean", ascending=False).round(3))
```

Output (scikit-learn 1.9.1, pandas 3.0.6): [VERSION]

```
          mean    std
calls    0.078  0.019
age      0.066  0.013
job      0.065  0.011
contact  0.030  0.013
balance  0.011  0.012
```

The presenter explains: shuffling `calls` lowers ROC AUC by about 0.078 on average over 20 shuffles, the largest drop. `age` and `job` follow closely. `balance` has a mean drop of 0.011 with a standard deviation of 0.012, so its effect cannot be separated from zero with this test set.

Mei Lin then writes three sentences for the sales manager:

1. "The number of times we have already called a customer in this campaign is the strongest signal: customers called many times are less likely to subscribe."
2. "Age and job type matter almost as much; older and retired customers are more likely to say yes."
3. "Account balance adds very little once we know the other information. These are patterns in past data, not proof that calling less will make people subscribe."

## Common Mistake
The most common mistake is to present importance as cause: "Reduce calls and subscriptions will rise." The model only shows that customers with many calls subscribed less in the past. Perhaps the bank kept calling people who were never interested. Another mistake is to trust `feature_importances_` from a tree model on training data without checking it with permutation importance on held-out data.

## Key Takeaways
1. Coefficients, tree importances and permutation importance each show which features a model relies on, with different strengths and limits.
2. Permutation importance works with any pipeline and should be run on held-out data, with its spread reported.
3. Importance is not cause; say "is linked with", and watch for correlated features that share importance.

## Hands-on Exercise
**Task:** Calculate permutation importance for your best model and write 3 plain-language sentences a sales manager could understand.
**Tools:** Google Colab (free), scikit-learn, pandas; your best pipeline from L10 or L14.
**Steps:**
1. Load or refit your best pipeline on the training data.
2. Run `permutation_importance` on the test set with a metric that fits your problem, `n_repeats=20` and `random_state=42`.
3. Put the mean and standard deviation in a sorted DataFrame and draw a horizontal bar chart with error bars.
4. Mark any feature whose mean is smaller than its standard deviation as "no clear effect".
5. If your model is a tree ensemble, compare the ranking with `feature_importances_` and note any differences.
6. Write 3 sentences without technical terms, using "is linked with" rather than "causes".
**What good looks like:** A clear chart, an honest note on features with no clear effect, and 3 sentences that a manager can read in 30 seconds and that avoid claims of cause and effect.
**Time:** about 30 minutes

## Review Flags
- [VERSION] `sklearn.inspection.permutation_importance` arguments and result attributes depend on the installed version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on synthetic data.
- [VERIFY] The statement that impurity-based tree importances are computed on training data and favour high-cardinality numeric features should be checked against the current scikit-learn user guide.
