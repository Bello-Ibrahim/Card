# Screen Demo Pack: AI-12 L13 Feature Engineering That Helps

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L13_screen_1.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Scroll past the L11 and L12 cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
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

**Narration over this clip (for pacing)**

> We continue in the bike notebook. This cell builds a table of candidate features from the timestamp: the hour, the day of the week, a weekend flag, and temperature times humidity. It uses the same training rows as before, and a small helper cross-validates the boosting model on any list of columns.

## Clip 2: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L13_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Highlight the output lines base 122.6 and + weekday 57.2.
2. Add the overlay: error cut by more than half.

**Narration over this clip (for pacing)**

> The base set of temperature, humidity and hour gives a cross-validated RMSE of one hundred and twenty-two point six. Adding the day of the week cuts it to fifty-seven point two bikes per hour. The model can now separate weekday rush hours from the weekend afternoon pattern.

## Clip 3: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L13_screen_3.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Highlight the output line + is_weekend 57.1.

**Narration over this clip (for pacing)**

> The weekend flag gives almost the same gain, fifty-seven point one. It carries the same information in a simpler form, so Sofia keeps one of the two, not both.

## Clip 4: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L13_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Highlight the output line + temp_x_humidity 122.8.
2. Strike it through and label it 'drop'.

**Narration over this clip (for pacing)**

> Temperature times humidity makes no real difference: one hundred and twenty-two point eight, against one hundred and twenty-two point six. So she drops it. A tree ensemble can already combine those two features by itself.

## Clip 5: scene 13

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L13_screen_5.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Scroll up to the L11 setup cell and highlight rng.normal(0, 60, len(ts)).
2. Add a text cell: Noise std 60, so RMSE near 57 is close to the limit.

**Narration over this clip (for pacing)**

> Sofia notes one more thing. In this synthetic data, the random noise has a standard deviation of sixty, so an error near fifty-seven is close to the best any model can do. With real data, she would not know that limit, which is why every step must be measured.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L11 setup cell (content.md L11 Worked Example, first code block: synthetic hourly bike data) and then the L11 model cell (second code block: features, the split with random_state=0, and the two models). Then run the L12 cell (content.md L12 Worked Example), which defines cv, cross_val_score and HistGradientBoostingRegressor. The L13 cell uses bikes, X_train, y_train and cv from these three cells. Do not run the L05 bank cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on synthetic data. The pandas .dt accessors, KBinsDiscretizer and TimeSeriesSplit should be checked against the Colab versions before recording; update the spoken RMSE values if the output differs.
- Screen scenes 9 to 13 use one cell copied exactly from the content.md Worked Example. Each cross-validation run takes a few seconds; cut the wait in editing.
- Hook: 'about sixty bikes per hour' is the L12 difference between linear (182.3) and boosting (122.6); 'cut the error in half' refers to 122.6 falling to 57.2.
- Sofia Petrova and the Sofia bike-sharing scheme are fictional; the data is synthetic.
