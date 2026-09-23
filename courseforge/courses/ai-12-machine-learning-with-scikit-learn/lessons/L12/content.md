# L12 Ensembles: Random Forests and Gradient Boosting

Course: AI-12 · Module: M3 · Objectives: O3, O4 · Video: 5 min (screen demo)

## Hook
One decision tree is easy to understand but unstable: change a few rows and it can grow very differently. What if you trained hundreds of trees and combined them? That simple idea is behind two of the strongest model families for tables of business data.

## Explanation
An **ensemble** combines many models into one prediction. Two approaches matter most in scikit-learn.

**Random forest.** It trains many deep trees, each on a random sample of the rows and considering a random subset of features at each split. Each tree makes different mistakes. For regression, the forest averages the trees' predictions; for classification, it combines their votes. Averaging cancels out much of each tree's noise, so a forest overfits much less than one deep tree. Key settings: `n_estimators` (number of trees), `max_depth`, `min_samples_leaf` and `max_features`. Trees are independent, so `n_jobs=-1` can train them in parallel.

**Gradient boosting.** It trains trees one after another. Each new, small tree tries to correct the errors the previous trees still make. The result is often the most accurate model on tabular data, but it has more settings to tune, and it can overfit if it runs for too many rounds. In scikit-learn, `HistGradientBoostingRegressor` and `HistGradientBoostingClassifier` are the fast versions: they group feature values into bins, handle missing values without an imputer, and can stop early when the score stops improving. Older tutorials may import them from an "experimental" module, which is no longer needed in recent releases. [VERSION]

When to try each one:

- Start with a **simple baseline** (linear or logistic regression) so you know what "good" means.
- Try a **random forest** next: it works well with default settings and is hard to break.
- Try **gradient boosting** when you want the best accuracy and have time to tune it.

Neither needs scaled features, because both are built from trees.

**Analogy:** Ask one person to guess the number of beans in a jar and the guess may be far off. Ask 200 people and average their guesses, and the average is often closer than most single guesses, because individual errors cancel out. A random forest is that crowd. Gradient boosting is more like a team where each new member studies what the team got wrong so far and focuses on fixing it.

## Worked Example
Amara Diallo runs analytics for a hypothetical scooter-rental start-up in Dakar, Senegal. She has the same kind of hourly demand problem as L11 and wants to know whether ensembles are worth their extra complexity. She continues from the L11 notebook, with `X_train` and `y_train` ready.

On screen, the presenter runs:

```python
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestRegressor, HistGradientBoostingRegressor

cv = KFold(n_splits=5, shuffle=True, random_state=0)
models = {"linear": LinearRegression(),
          "forest": RandomForestRegressor(n_estimators=200, n_jobs=-1, random_state=0),
          "boosting": HistGradientBoostingRegressor(random_state=0)}
for name, model in models.items():
    rmse = -cross_val_score(model, X_train, y_train, cv=cv,
                            scoring="neg_root_mean_squared_error")
    print(f"{name:8} RMSE={rmse.mean():.1f} (std {rmse.std():.1f})")
```

Output (scikit-learn 1.9.1): [VERSION]

```
linear   RMSE=182.3 (std 2.8)
forest   RMSE=128.7 (std 1.6)
boosting RMSE=122.6 (std 1.8)
```

The presenter explains two details. First, scikit-learn scorers follow the rule "higher is better", so error metrics are returned as negative numbers; the minus sign in front of `cross_val_score` turns them back into normal RMSE values. Second, `KFold` is used instead of `StratifiedKFold` because the target is a number.

Amara's reading: both ensembles cut the error by more than 50 bikes per hour compared with the linear model, and the gap is far larger than the spread. Boosting is about 6 bikes per hour better than the forest, which is also larger than the spread, and it trained faster in this run. She picks gradient boosting and notes that all three models still have the same weakness: they only see temperature, humidity and hour. L13 adds better features.

## Common Mistake
Learners often assume that the most complex model always wins and skip the baseline. On small or noisy data, a well-regularised linear model can match or beat an untuned ensemble, as you will see with the term-deposit data in L14. Always compare with a simple baseline using the same cross-validation folds. Another mistake is to read `neg_root_mean_squared_error` scores without the minus sign and conclude that the error is negative.

## Key Takeaways
1. A random forest averages many different trees, which reduces overfitting; it is a strong, low-effort second model.
2. Gradient boosting adds trees one by one to correct earlier errors; `HistGradientBoosting` models are fast and handle missing values.
3. Compare ensembles with a simple baseline on the same folds, and remember that error scorers are negative in scikit-learn.

## Hands-on Exercise
**Task:** Compare linear regression, a random forest and gradient boosting on the bike data with cross-validation, and pick one.
**Tools:** Google Colab (free), scikit-learn, pandas; your L11 data.
**Steps:**
1. Reuse `X_train` and `y_train` from L11.
2. Create `KFold(n_splits=5, shuffle=True, random_state=0)`.
3. Run the loop above, and also record MAE with `scoring="neg_mean_absolute_error"`.
4. Put the results in a table with mean and standard deviation for each metric.
5. Time each model with `%%time` in Colab and add the times to the table.
6. Write 3 sentences: which model you pick, how much better it is in bikes per hour, and what it costs in training time.
**What good looks like:** A table of 3 models × 2 metrics with spreads, training times, and a choice justified by both accuracy and practical cost.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Estimator names, import paths and defaults for `RandomForestRegressor` and `HistGradientBoostingRegressor`, and scorer names such as `neg_root_mean_squared_error`, depend on the installed version. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data.
