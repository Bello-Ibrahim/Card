# Screen Demo Pack: AI-12 L10 Cross-Validation for Reliable Scores

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L10_screen_1.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Scroll past the L05 setup and pipeline cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
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

**Narration over this clip (for pacing)**

> This cell sets up five stratified folds. Then it builds three pipelines with the same preprocessing and a different model each: logistic regression, a decision tree, and k-nearest neighbours. For each one, it prints the mean ROC AUC across the folds, and the spread.

## Clip 2: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L10_screen_2.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Highlight logistic mean=0.774 std=0.048.
2. Highlight tree mean=0.682 std=0.034.
3. Show the overlay: gap about 0.09 > spread.

**Narration over this clip (for pacing)**

> Logistic regression has the highest mean, zero point seven seven four, with a spread of zero point zero four eight. The tree scores zero point six eight two, with a spread of zero point zero three four. Its lead over the tree, about zero point zero nine, is larger than the spread. That is a real difference.

## Clip 3: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L10_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Highlight knn mean=0.733 std=0.047.
2. Add a text cell: Logistic vs KNN: probably better, not certain.

**Narration over this clip (for pacing)**

> k-nearest neighbours scores zero point seven three three, with a spread of zero point zero four seven. The lead of logistic regression here is about zero point zero four, smaller than one standard deviation. So Lars writes, probably better, not certain.

## Clip 4: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L10_screen_4.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Type this exact code cell from content.md and run it with Shift+Enter:
from sklearn.model_selection import cross_validate
res = cross_validate(pipe, X_train, y_train, cv=cv, scoring=["roc_auc", "recall"])
print(res["test_roc_auc"].round(3), res["test_recall"].round(3))

**Narration over this clip (for pacing)**

> Next, this cell shows the individual fold scores for the logistic pipeline, for two metrics at once: ROC AUC and recall.

## Clip 5: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L10_screen_5.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Highlight the first array [0.775 0.81 0.725 0.718 0.843] and mark the lowest 0.718 and highest 0.843.
2. Highlight the second array [0.056 0.056 0.028 0.027 0.108].

**Narration over this clip (for pacing)**

> ROC AUC ranges from zero point seven one eight to zero point eight four three across the folds. A single split could have reported either end. And recall at the default threshold is low in every fold, between zero point zero two seven and zero point one zero eight, which matches lesson eight.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The first L10 cell uses prep, Pipeline and LogisticRegression from those cells; the second L10 cell uses cv from the first, so run them in order. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] cross_validate result keys (such as test_roc_auc) and scoring names depend on the installed version. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data; re-run before recording and update every spoken mean, spread and fold score if they differ.
- Screen scenes 8 to 10 use the first L10 cell; scenes 11 and 12 use the second cell. Both are copied exactly from the content.md Worked Example.
- Speak 'mean' and 'standard deviation' in words; the screen shows mean= and std=.
- Lars Eriksson and the Swedish energy company are fictional; the data is synthetic.
