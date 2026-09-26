# Screen Demo Pack: AI-12 L14 Hyperparameter Tuning with Grid and Random Search

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L14_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Scroll past the L05 setup and pipeline cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
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

**Narration over this clip (for pacing)**

> We continue in the bank notebook. This cell puts a random forest into the pipeline, defines ranges for four settings, and runs a random search of twenty combinations with five folds, scored by ROC AUC. Then it scores the untuned and tuned pipelines on the test set, once.

## Clip 2: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L14_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Highlight the best_params_ output line and the score 0.769.

**Narration over this clip (for pacing)**

> The search chose two hundred trees, the square-root feature setting, a maximum depth of twelve, and a minimum of forty customers per leaf. Its mean cross-validated ROC AUC is zero point seven six nine.

## Clip 3: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L14_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Highlight 'model__min_samples_leaf': 40.
2. Add the caption: at least 40 customers per leaf.

**Narration over this clip (for pacing)**

> Forty customers per leaf is the key choice. It stops the trees from memorising individual people. That fits what you saw in lesson seven. The default forest was too flexible for fifteen hundred noisy training rows.

## Clip 4: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L14_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Highlight the output lines untuned 0.701 and tuned 0.737.
2. Show the overlay: logistic (L09) 0.752.

**Narration over this clip (for pacing)**

> On the test set, ROC AUC rose from zero point seven zero one to zero point seven three seven. But the logistic regression pipeline from lesson nine scored zero point seven five two on the same test set. Tuning improved the forest, yet the simpler model is still slightly ahead.

## Clip 5: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L14_screen_5.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Add a text cell: Tuning helped the forest, but logistic regression is simpler and at least as good. Carry it forward.

**Narration over this clip (for pacing)**

> Youssef's conclusion: tuning helped the forest, but for this data, the logistic model is simpler, easier to explain, and at least as good. He will carry it forward. That is a good result. The search saved him from assuming that a complex model is better.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The L14 cell uses prep, Pipeline, X_train, y_train, X_test and y_test from those cells. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] GridSearchCV and RandomizedSearchCV arguments, the order of keys in best_params_, and search run time in Colab depend on the installed version and hardware. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data; re-run before recording and update the spoken settings and scores if they differ.
- Screen scenes 8 to 12 use one cell copied exactly from the content.md Worked Example. The search takes about half a minute; cut the wait in editing.
- Scene 11 compares with the logistic pipeline's test ROC AUC of 0.752 from L09; show it as an overlay, since it is not printed by this cell.
- Youssef Haddad and the Beirut bank are fictional; the data is synthetic.
