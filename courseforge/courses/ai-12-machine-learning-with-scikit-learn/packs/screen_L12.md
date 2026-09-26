# Screen Demo Pack: AI-12 L12 Ensembles: Random Forests and Gradient Boosting

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L12_screen_1.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Scroll past the L11 setup and model cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
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

**Narration over this clip (for pacing)**

> We continue in the bike notebook, with the training data ready. This cell creates five folds, then cross-validates three models on the same folds: linear regression, a forest of two hundred trees, and gradient boosting. For each, it prints the mean RMSE and the spread.

## Clip 2: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L12_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Highlight the minus sign before cross_val_score and scoring="neg_root_mean_squared_error".
2. Highlight KFold(n_splits=5, shuffle=True, random_state=0).

**Narration over this clip (for pacing)**

> Two details. scikit-learn scores follow the rule that higher is better, so errors come back as negative numbers. The minus sign at the start turns them into normal RMSE values. And we use plain folds, not stratified ones, because the target is a number.

## Clip 3: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L12_screen_3.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Highlight the three output lines: linear RMSE=182.3 (std 2.8), forest RMSE=128.7 (std 1.6), boosting RMSE=122.6 (std 1.8).

**Narration over this clip (for pacing)**

> The results. Linear regression has an RMSE of one hundred and eighty-two point three, with a spread of two point eight. The forest scores one hundred and twenty-eight point seven, spread one point six. Boosting scores one hundred and twenty-two point six, spread one point eight.

## Clip 4: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L12_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Add the overlay: ensembles about 50+ bikes/hour better than linear.
2. Add a text cell: Choice: gradient boosting. Next: better features.

**Narration over this clip (for pacing)**

> Both ensembles cut the error by more than fifty bikes per hour, far more than the spread. Boosting is about six bikes per hour better than the forest, also more than the spread. So Amara picks gradient boosting. But all three models still see only temperature, humidity and hour.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L11 setup cell (content.md L11 Worked Example, first code block: synthetic hourly bike data) and then the L11 model cell (second code block: features, the split with random_state=0, and the two models). The L12 cell uses X_train, y_train and LinearRegression from those cells. Do not run the L05 bank cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] Estimator names, import paths and defaults for RandomForestRegressor and HistGradientBoostingRegressor, and scorer names such as neg_root_mean_squared_error, depend on the installed version. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data; re-run before recording and update the spoken RMSE values and spreads if they differ.
- Content.md says boosting 'trained faster in this run'; the voiceover leaves out training time because it depends on Colab hardware.
- Screen scenes 8 to 11 use one cell copied exactly from the content.md Worked Example. The forest with 200 trees can take several seconds; cut the wait in editing.
- Amara Diallo and the Dakar scooter-rental start-up are fictional; the data is synthetic.
