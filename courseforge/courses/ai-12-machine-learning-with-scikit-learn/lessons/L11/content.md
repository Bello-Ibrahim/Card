# L11 Regression Models and Metrics

Course: AI-12 · Module: M3 · Objectives: O3, O4 · Video: 6 min (screen demo)

## Hook
A bike-sharing manager does not ask "Will people rent bikes?" She asks "How many bikes will we need at 8 a.m. tomorrow?" When the answer is a number, you need regression, and you need metrics that speak in bikes, not in abstract scores.

## Explanation
Regression models predict a number. The scikit-learn workflow is exactly the same as for classification: create, `fit`, `predict`. Two model families are a good start:

- **LinearRegression** fits a weighted sum of the features. It is fast and easy to explain, but it can only draw straight-line relationships unless you create new features (L13).
- **DecisionTreeRegressor** splits the data like a classification tree, and each leaf predicts the average of its training rows. It can follow curves and peaks, but it overfits if it grows too deep.

Three metrics, explained in words (the maths was covered in AI-05):

- **MAE (mean absolute error):** the average size of the error, in the target's own units. "On average, our prediction is 90 bikes away from the real number."
- **RMSE (root mean squared error):** also in the target's units, but it punishes large errors more. If RMSE is much larger than MAE, the model makes some big misses.
- **R² (coefficient of determination):** how much of the variation in the target the model explains, compared with always predicting the average. 1.0 is perfect, 0 is no better than the average, and it can be negative for a very poor model. It has no units, so it is harder to use in a business conversation.

`root_mean_squared_error` is a recent addition; older code uses `mean_squared_error(..., squared=False)`, which newer versions no longer accept. [VERSION]

**Analogy:** MAE is like the average number of minutes a bus is late. RMSE is like the same measure, but where a bus that is 40 minutes late counts much more than four buses that are 10 minutes late. Passengers remember the very late bus, and RMSE does too.

## Worked Example
Park Ji-woo is an analyst for a hypothetical city bike-sharing scheme. The course exercise uses the UCI Seoul Bike Sharing Demand data [VERIFY], but the demo uses a synthetic year of hourly data with a similar shape, so results are reproducible.

On screen, the presenter runs the setup cell (shared by L11 to L13):

```python
import numpy as np, pandas as pd

rng = np.random.default_rng(7)
ts = pd.date_range("2025-01-01", periods=24 * 365, freq="h")
hour, workday = np.asarray(ts.hour), np.asarray(ts.dayofweek < 5)
season = np.sin(2 * np.pi * (np.asarray(ts.dayofyear) - 110) / 365)
rush = np.exp(-(hour - 8) ** 2 / 3) + np.exp(-(hour - 18) ** 2 / 3)
bikes = pd.DataFrame({"timestamp": ts,
                      "temp": 12 + 10 * season + rng.normal(0, 3, len(ts)),
                      "humidity": rng.uniform(20, 95, len(ts))})
bikes["rentals"] = np.clip(
    40 + 15 * bikes["temp"] - 2 * bikes["humidity"] + 600 * rush * workday
    + 200 * ~workday * ((hour > 10) & (hour < 19)) + rng.normal(0, 60, len(ts)),
    0, None).round()
```

The data has 8,760 hours, with an average of about 243 rentals per hour. Then the models:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

X = bikes[["temp", "humidity"]].assign(hour=bikes["timestamp"].dt.hour)
y = bikes["rentals"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

for model in [LinearRegression(), DecisionTreeRegressor(max_depth=8, random_state=0)]:
    pred = model.fit(X_train, y_train).predict(X_test)
    print(type(model).__name__, round(mean_absolute_error(y_test, pred), 1),
          round(root_mean_squared_error(y_test, pred), 1), round(r2_score(y_test, pred), 3))
```

Output (scikit-learn 1.9.1, pandas 3.0.6): [VERSION]

```
LinearRegression 141.7 186.4 0.268
DecisionTreeRegressor 89.5 124.0 0.676
```

The presenter translates: the linear model is wrong by about 142 bikes per hour on average; the tree by about 90. Linear regression treats `hour` as a straight line, so it cannot capture the morning and evening peaks. The tree can, because it splits the hours into groups. For a plot, the presenter runs `plt.scatter(y_test, pred, s=3)` for the tree and adds a diagonal line: points far from the line are the big misses.

## Common Mistake
Learners often report R² alone, for example "R² is 0.68, so the model is good". A manager cannot plan bikes with R². Report MAE or RMSE in business units, and compare them with the size of the target: an MAE of 90 bikes is large when the average is 243. Also pass `(y_true, y_pred)` in that order; for R² the order changes the result.

## Key Takeaways
1. Regression uses the same `fit` and `predict` workflow; linear models draw straight lines, while trees can follow peaks.
2. MAE and RMSE are in the target's units; RMSE is larger when the model makes some big misses.
3. R² shows the share of variation explained, but report MAE or RMSE in business units to stakeholders.

## Hands-on Exercise
**Task:** Predict hourly bike rentals, report MAE and RMSE in "bikes per hour", and plot predicted against actual values.
**Tools:** Google Colab (free), scikit-learn, pandas, matplotlib; the UCI Seoul Bike Sharing Demand dataset [VERIFY] or the synthetic data above.
**Steps:**
1. Load the data. For the UCI file, check the column names for the count, hour, temperature and humidity, and the file encoding. [VERIFY]
2. Choose 3 to 5 numeric features and the rentals target.
3. Split with `test_size=0.2` and `random_state=0`.
4. Train `LinearRegression` and `DecisionTreeRegressor(max_depth=8)`.
5. Print MAE, RMSE and R² for both, rounded.
6. Plot predicted against actual for the better model, with a diagonal reference line.
7. Write 2 sentences in business language, using "bikes per hour".
**What good looks like:** A results table for 2 models, a labelled scatter plot, and 2 sentences such as "On average, the forecast is about N bikes per hour away from the real number."
**Time:** about 30 minutes

## Review Flags
- [VERIFY] Availability, licence, column names and file encoding of the UCI Seoul Bike Sharing Demand dataset.
- [VERSION] `root_mean_squared_error` replaced `mean_squared_error(squared=False)` in recent releases; check the Colab version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6, NumPy 2.4 and Python 3.11 on synthetic data.
