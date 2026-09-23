# L10 Cross-Validation for Reliable Scores

Course: AI-12 · Module: M2 · Objectives: O2, O4 · Video: 5 min (screen demo)

## Hook
In L03 you changed only the random seed of the split, and the test score moved. If one split can be lucky or unlucky, how can you trust a comparison between two models that differ by 0.01? Cross-validation gives you a score and a measure of how much it moves.

## Explanation
**k-fold cross-validation** splits the training data into k equal parts, called folds. It trains the model k times. Each time, one fold is held out for scoring and the other k − 1 folds are used for training. You get k scores, one per fold. Every row is used for scoring exactly once.

For classification, use **stratified k-fold**, which keeps the class balance the same in every fold. This is important when one class is rare. `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` gives repeatable, balanced folds.

Two functions do the work:

- `cross_val_score(model, X, y, cv=cv, scoring="roc_auc")` returns an array of scores for one metric.
- `cross_validate(model, X, y, cv=cv, scoring=["roc_auc", "recall"])` returns several metrics and the fit times.

Always report two numbers: the **mean** score and the **standard deviation** (the spread). If model A scores 0.77 ± 0.05 and model B scores 0.76 ± 0.05, the difference is smaller than the normal variation between folds, so you cannot say A is better.

Cross-validation runs on the **training set only**. The test set is still kept for one final check. And because you pass a whole pipeline, the preprocessing is refitted inside every fold, which keeps each fold free of leakage.

**Analogy:** Judging a student by one exam can be unfair: the questions may happen to suit them, or not. Five short exams on different topics give a better picture, and the difference between the best and worst exam shows how consistent the student is. Cross-validation gives your model five exams.

## Worked Example
Lars Eriksson is an analyst at a hypothetical energy company in Sweden. He is testing a workflow for predicting which customers will accept a new contract. He practises on the term-deposit data from L05, where `prep` is the ColumnTransformer and `X_train`, `y_train` are ready.

On screen, the presenter runs:

```python
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
models = {"logistic": LogisticRegression(max_iter=1000),
          "tree": DecisionTreeClassifier(max_depth=4, random_state=42),
          "knn": KNeighborsClassifier(n_neighbors=25)}

for name, model in models.items():
    candidate = Pipeline([("prep", prep), ("model", model)])
    scores = cross_val_score(candidate, X_train, y_train, cv=cv, scoring="roc_auc")
    print(f"{name:9} mean={scores.mean():.3f} std={scores.std():.3f}")
```

Output (scikit-learn 1.9.1): [VERSION]

```
logistic  mean=0.774 std=0.048
tree      mean=0.682 std=0.034
knn       mean=0.733 std=0.047
```

The presenter reads the table: logistic regression has the highest mean ROC AUC. Its lead over the tree (about 0.09) is larger than the spread, so it is a real difference. Its lead over KNN (about 0.04) is smaller than one standard deviation, so Lars notes it as "probably better, not certain".

Then the presenter shows the individual fold scores for the logistic model with `cross_validate`:

```python
from sklearn.model_selection import cross_validate
res = cross_validate(pipe, X_train, y_train, cv=cv, scoring=["roc_auc", "recall"])
print(res["test_roc_auc"].round(3), res["test_recall"].round(3))
```

Output: `[0.775 0.81  0.725 0.718 0.843] [0.056 0.056 0.028 0.027 0.108]` [VERSION]

ROC AUC ranges from 0.718 to 0.843 across folds. A single split could have reported either end. Recall at the default threshold is low in every fold, which matches L08.

## Common Mistake
Learners sometimes run cross-validation on the full dataset, including the test rows, and then also report a "test" score on those same rows. The test set is then not independent. Another common mistake is to preprocess the data first and cross-validate only the model; the preprocessing has then seen every fold. Split off the test set first, and cross-validate the whole pipeline on the training set.

## Key Takeaways
1. k-fold cross-validation trains and scores a model k times, so every training row is used for scoring once; use stratified folds for classification.
2. Report the mean and the standard deviation; differences smaller than the spread are not reliable.
3. Cross-validate the whole pipeline on the training set only, and keep the test set for the final check.

## Hands-on Exercise
**Task:** Run 5-fold cross-validation for 3 classifiers and report each one's mean score and standard deviation in a small table.
**Tools:** Google Colab (free), scikit-learn, pandas; your L05 data and preprocessing.
**Steps:**
1. Create `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)`.
2. Build 3 pipelines with the same `prep` and different models: logistic regression, a decision tree and KNN.
3. Run `cross_val_score` with `scoring="roc_auc"` for each.
4. Put the results in a pandas DataFrame with columns model, mean and std, sorted by mean.
5. Run `cross_validate` for your best model with 2 metrics and print the fold scores.
6. Write 2 sentences: which model you would carry forward, and whether the difference is larger than the spread.
**What good looks like:** A clean 3-row table, fold-level scores for the best model, and a conclusion that mentions the standard deviation.
**Time:** about 25 minutes

## Review Flags
- [VERSION] `cross_validate` result keys (such as `test_roc_auc`) and scoring names depend on the installed version. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data.
