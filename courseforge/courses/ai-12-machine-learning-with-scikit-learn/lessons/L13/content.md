# L13 Feature Engineering That Helps

Course: AI-12 · Module: M3 · Objectives: O5 · Video: 6 min (screen demo)

## Hook
In L12 we changed the model and saved about 60 bikes per hour of error. Today we keep the model the same and change only what it sees. One new column, created from a timestamp we already had, will cut the error in half.

## Explanation
**Feature engineering** means creating new input columns from the data you already have, so that the pattern becomes easier for the model to learn. Useful types:

- **Date and time parts:** hour, day of the week, month, "is weekend", "is public holiday". A raw timestamp means little to a model; its parts often carry the pattern.
- **Ratios:** debt divided by income, spend per visit, price per square metre. A ratio can be more meaningful than either number alone.
- **Interactions:** two features multiplied or combined, such as "hot and weekend", when their effect together differs from their effects apart.
- **Bins:** age bands or distance bands, which can help linear models follow non-straight patterns. `KBinsDiscretizer` can create them inside a pipeline.

Two rules keep feature engineering honest.

1. **Test every new feature with cross-validation.** Add it, measure the cross-validated score, and keep it only if it helps by more than the normal spread. More columns are not automatically better: useless features add noise and make models slower and harder to explain.
2. **Never use future information.** Each feature must be known at the moment of prediction. "Average rentals for the whole day" uses hours that have not happened yet at 8 a.m., so it leaks the answer. "Rentals at the same hour yesterday" is fine, because it is already known.

For time-ordered data, also consider `TimeSeriesSplit`, which always trains on earlier rows and tests on later ones. A random split, as used in this demo for simplicity, lets the model train on hours that surround each test hour, which can make scores look a little better than in real forecasting.

**Analogy:** Feature engineering is like preparing ingredients before cooking. The same oven (the model) gives a much better result when the vegetables are washed and cut to the right size. But you cannot use an ingredient that will only arrive tomorrow.

## Worked Example
Sofia Petrova is a data analyst for a hypothetical bike-sharing scheme in Sofia, Bulgaria. Her boosting model from L12 has an RMSE of about 123 bikes per hour. She suspects that the model is missing the difference between workdays and weekends.

On screen, the presenter continues from the L11 and L12 notebook (with `bikes`, `X_train`, `y_train` and `cv` ready) and runs:

```python
feats = bikes[["temp", "humidity"]].assign(
    hour=bikes["timestamp"].dt.hour,
    weekday=bikes["timestamp"].dt.dayofweek,
    is_weekend=(bikes["timestamp"].dt.dayofweek >= 5).astype(int),
    temp_x_humidity=bikes["temp"] * bikes["humidity"],
)
train_idx = X_train.index            # same rows as the L11 split
model = HistGradientBoostingRegressor(random_state=0)

def cv_rmse(cols):
    scores = cross_val_score(model, feats.loc[train_idx, cols], y_train, cv=cv,
                             scoring="neg_root_mean_squared_error")
    return round(-scores.mean(), 1)

base = ["temp", "humidity", "hour"]
print("base", cv_rmse(base))
for extra in ["weekday", "is_weekend", "temp_x_humidity"]:
    print("+", extra, cv_rmse(base + [extra]))
```

Output (scikit-learn 1.9.1, pandas 3.0.6): [VERSION]

```
base 122.6
+ weekday 57.2
+ is_weekend 57.1
+ temp_x_humidity 122.8
```

The presenter reads the results:

- **weekday** cuts cross-validated RMSE from 122.6 to 57.2 bikes per hour. The model can now separate the weekday rush hours from the weekend afternoon pattern.
- **is_weekend** gives almost the same gain (57.1). It carries the same information in a simpler form, so Sofia keeps one of the two, not both.
- **temp_x_humidity** makes no real difference (122.8 against 122.6), so she drops it. A tree ensemble can already combine temperature and humidity by itself.

Sofia also notes that in this synthetic data the random noise has a standard deviation of 60, so an RMSE near 57 is close to the best any model can do. With real data she would not know that limit, which is why each step must be measured.

## Common Mistake
Learners often create features on the full dataset with statistics that use the target or future rows, for example "average rentals per hour of day" calculated over the whole year, including the test rows. This is target leakage and makes the score too optimistic. Features that only use the row's own values, such as the hour or a ratio of two columns, are safe to create before the split. Features that learn from other rows or from the target must be calculated inside the pipeline or from training data only.

## Key Takeaways
1. Good features, such as time parts, ratios and interactions, can improve a model more than a change of algorithm.
2. Keep a new feature only if it improves the cross-validated score by more than the normal spread.
3. Every feature must be known at prediction time; statistics that use the target or future rows leak information.

## Hands-on Exercise
**Task:** Add 3 new features to the bike data, measure the change in cross-validated RMSE, and keep only the features that help.
**Tools:** Google Colab (free), scikit-learn, pandas; your L11 and L12 notebook.
**Steps:**
1. Record the baseline cross-validated RMSE of your chosen model from L12.
2. Create 3 new features, such as weekday, is_weekend, month, or a "rush hour" flag.
3. For each feature, write one sentence confirming that it is known at prediction time.
4. Add each feature on its own to the baseline set and record the cross-validated RMSE and its standard deviation.
5. Keep only the features that improve RMSE by more than the spread, and run the final set together.
6. Optional: repeat the final comparison with `TimeSeriesSplit(n_splits=5)` on data sorted by time, and compare the scores.
**What good looks like:** A table with one row per feature (RMSE, change against baseline, keep or drop), a final feature list, and a leakage check sentence for each feature.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on synthetic data. The pandas `.dt` accessors, `KBinsDiscretizer` and `TimeSeriesSplit` should be checked against the Colab versions before recording.
