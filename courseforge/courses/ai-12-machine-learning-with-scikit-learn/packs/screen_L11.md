# Screen Demo Pack: AI-12 L11 Regression Models and Metrics

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L11_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Start a fresh Colab runtime and add a text cell: Setup cell, shared by L11 to L13.
2. Type this exact code cell from content.md and run it with Shift+Enter:
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
3. In a scratch cell, run bikes.shape and bikes['rentals'].mean() to show 8,760 rows and about 243, then delete the scratch cell.

**Narration over this clip (for pacing)**

> In a fresh notebook, we run the setup cell. It creates one year of hourly data, with temperature, humidity, and a morning and evening rush on workdays. That is eight thousand, seven hundred and sixty hours, with an average of about two hundred and forty-three rentals per hour.

## Clip 2: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L11_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Type this exact code cell from content.md and run it with Shift+Enter:
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

**Narration over this clip (for pacing)**

> The model cell uses three features: temperature, humidity, and the hour of the day. It keeps twenty percent of the hours for testing. Then it trains a linear model and a tree with a depth of eight, and prints MAE, RMSE and R squared for each.

## Clip 3: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L11_screen_3.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Highlight the output line LinearRegression 141.7 186.4 0.268.
2. Add the caption: about 142 bikes per hour off.

**Narration over this clip (for pacing)**

> The linear model has an MAE of one hundred and forty-one point seven, an RMSE of one hundred and eighty-six point four, and R squared of zero point two six eight. In business terms, it is wrong by about one hundred and forty-two bikes per hour, on average.

## Clip 4: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L11_screen_4.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Highlight the output line DecisionTreeRegressor 89.5 124.0 0.676.
2. Add the caption: about 90 bikes per hour off.

**Narration over this clip (for pacing)**

> The tree has an MAE of eighty-nine point five, an RMSE of one hundred and twenty-four point zero, and R squared of zero point six seven six. It is wrong by about ninety bikes per hour. The linear model treats the hour as a straight line, so it cannot capture the rush-hour peaks. The tree can.

## Clip 5: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L11_screen_5.mp4`
- **Target length:** about 10 seconds

**Steps**

1. In a new cell, type and run: import matplotlib.pyplot as plt; plt.scatter(y_test, pred, s=3); plt.plot([0, y_test.max()], [0, y_test.max()]); plt.show()
2. Circle a few points far from the diagonal.

**Narration over this clip (for pacing)**

> Finally, we plot the tree's predictions against the real values, with a diagonal line. Points far from the line are the big misses.

## Production notes for this lesson

- Setup before recording: start a fresh Colab runtime. Scene 8 runs the L11 setup cell (content.md L11 Worked Example, first code block), which is shared by L11, L12 and L13; save this notebook as the bike notebook. Do not run the L05 bank cells in the same runtime, because they reuse the names X_train and y_train.
- [VERIFY] Availability, licence, column names and file encoding of the UCI Seoul Bike Sharing Demand dataset. The voiceover only mentions a public bike-sharing dataset for the exercise and does not describe it.
- [VERSION] root_mean_squared_error replaced mean_squared_error(squared=False) in recent releases; check the Colab version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6, NumPy 2.4 and Python 3.11 on synthetic data; re-run before recording and update every spoken value if it differs.
- Screen scenes 8 to 11 use the two cells copied exactly from the content.md Worked Example; the scratch check of bikes.shape and the mean in scene 8 only confirms the 8,760 hours and about 243 rentals that content.md states. Scene 12 (scatter plot): content.md gives only plt.scatter(y_test, pred, s=3) plus 'a diagonal line'; the extra import and plt.plot line in the screen steps are a suggestion for review. pred holds the tree's predictions because the tree is the last model in the loop.
- Park Ji-woo and the city bike-sharing scheme are fictional. Speak R² as 'R squared'.
