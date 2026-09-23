# L14 Hyperparameter Tuning with Grid and Random Search

Course: AI-12 · Module: M3 · Objectives: O5 · Video: 6 min (screen demo)

## Hook
Every model you have trained so far used default settings, or settings we picked by hand. Defaults are a reasonable starting point, not the best choice for your data. Today you will let scikit-learn search for better settings, and you will see that tuning helps, but does not work miracles.

## Explanation
**Hyperparameters** are settings you choose before training, such as `max_depth`, `min_samples_leaf` or `n_estimators`. The model does not learn them from data. **Tuning** means trying many combinations and keeping the one with the best cross-validated score.

scikit-learn offers two main search tools:

- **GridSearchCV** tries every combination in a grid. Three values for each of four settings means 3 × 3 × 3 × 3 = 81 combinations, each trained once per fold. With 5 folds, that is 405 fits. Grids grow very quickly.
- **RandomizedSearchCV** tries a fixed number of random combinations (`n_iter`). It often finds settings nearly as good as a full grid in much less time, especially when only a few settings really matter.

Both work on a **whole pipeline**, so preprocessing is refitted inside every fold. To reach a setting inside a pipeline, use the step name, two underscores, and the parameter name: `model__max_depth` means "the `max_depth` of the step called `model`".

After the search, `best_params_` shows the winning settings, `best_score_` shows their mean cross-validated score, and `best_estimator_` is that pipeline refitted on the whole training set.

The rule from L03 still holds: **the test set stays untouched until the very end.** The search uses only training data. You look at the test score once, after all choices are made.

**Analogy:** Tuning is like adjusting the settings on a new sewing machine: stitch length, thread tension and speed. You could test every combination on a practice cloth (grid search), or test twenty random combinations and keep the best (random search). Either way, you practise on scrap cloth, not on the customer's dress. The test set is the customer's dress.

## Worked Example
Youssef Haddad is a data scientist at a hypothetical bank in Beirut, Lebanon. His random forest for term-deposit subscriptions uses default settings, and he wants to know whether tuning helps. He continues from the L05 notebook, with `prep`, `X_train`, `y_train`, `X_test` and `y_test` ready.

On screen, the presenter runs (the search takes about half a minute):

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import roc_auc_score

rf_pipe = Pipeline([("prep", prep),
                    ("model", RandomForestClassifier(random_state=42))])
params = {"model__n_estimators": [100, 200, 400],
          "model__max_depth": [3, 5, 8, 12, None],
          "model__min_samples_leaf": [1, 5, 10, 20, 40],
          "model__max_features": ["sqrt", 0.5, 1.0]}
search = RandomizedSearchCV(rf_pipe, params, n_iter=20, cv=5, scoring="roc_auc",
                            random_state=42, n_jobs=-1)
search.fit(X_train, y_train)
print(search.best_params_, round(search.best_score_, 3))

untuned = rf_pipe.fit(X_train, y_train)
for name, m in [("untuned", untuned), ("tuned", search.best_estimator_)]:
    print(name, round(roc_auc_score(y_test, m.predict_proba(X_test)[:, 1]), 3))
```

Output (scikit-learn 1.9.1): [VERSION]

```
{'model__n_estimators': 200, 'model__min_samples_leaf': 40, 'model__max_features': 'sqrt', 'model__max_depth': 12} 0.769
untuned 0.701
tuned 0.737
```

The presenter reads the results:

- The search chose `min_samples_leaf=40`. Each leaf must hold at least 40 customers, which stops the trees from memorising individual people. This fits the lesson from L07: the default forest was too flexible for 1,500 noisy training rows.
- Test ROC AUC rose from 0.701 to 0.737.
- But the logistic regression pipeline from L09 scored 0.752 on the same test set. Tuning improved the forest, yet the simpler model is still slightly ahead.

Youssef's conclusion: "Tuning helped the forest, but for this data the logistic model is simpler, easier to explain and at least as good. I will carry it forward." That is a good result: the search saved him from assuming that a complex model is better.

## Common Mistake
Learners often tune on the test set, or run the search on the full dataset before splitting. Then the "best" settings have seen the test rows, and the final score is too optimistic. Another common mistake is a huge grid with thousands of combinations, which can run for hours in Colab. Start with a random search over wide ranges, then, if needed, a small grid around the best values.

## Key Takeaways
1. Hyperparameters are settings you choose before training; tuning searches for the combination with the best cross-validated score.
2. RandomizedSearchCV is usually more efficient than GridSearchCV; use `step__parameter` names to tune settings inside a pipeline.
3. Search on training data only, check the test set once at the end, and compare the tuned model with a simple baseline.

## Hands-on Exercise
**Task:** Tune a random forest with RandomizedSearchCV and compare its test score with the untuned model.
**Tools:** Google Colab (free), scikit-learn; your L05 Bank Marketing pipeline, or the bike data with `RandomForestRegressor` and an RMSE scorer.
**Steps:**
1. Build a pipeline with your preprocessing and `RandomForestClassifier(random_state=42)`.
2. Define a parameter space with at least 4 settings, using `model__` names.
3. Run `RandomizedSearchCV` with `n_iter=20`, `cv=5`, `random_state=42` and a metric that suits your problem.
4. Print `best_params_` and `best_score_`.
5. Only now, score the untuned and tuned pipelines once on the test set.
6. Add your best simple model (logistic or linear regression) to the comparison.
7. Write 3 sentences: what changed, how much it helped, and which model you would choose and why.
**What good looks like:** A clear table of cross-validated and test scores for 3 models, the chosen settings, and an honest conclusion, even if tuning helped only a little.
**Time:** about 35 minutes

## Review Flags
- [VERSION] `GridSearchCV` and `RandomizedSearchCV` arguments, the order of keys in `best_params_`, and search run time in Colab depend on the installed version and hardware. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data.
