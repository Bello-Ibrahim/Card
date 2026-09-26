# Screen Demo Pack: AI-12 L17 Capstone Step 1: Build an End-to-End Model

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L17_screen_1.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Scroll past the L05 setup and pipeline cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
import joblib, sklearn
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_auc_score

baseline = Pipeline([("prep", prep), ("model", DummyClassifier(strategy="prior"))])
print("baseline CV AUC:", cross_val_score(baseline, X_train, y_train, cv=5,
                                          scoring="roc_auc").mean().round(3))
print("model CV AUC:", cross_val_score(pipe, X_train, y_train, cv=5,
                                       scoring="roc_auc").mean().round(3))

final = pipe.fit(X_train, y_train)          # after all tuning is finished
print("test AUC:", round(roc_auc_score(y_test, final.predict_proba(X_test)[:, 1]), 3))

joblib.dump(final, "term_deposit_model.joblib")
print("saved with scikit-learn", sklearn.__version__)
loaded = joblib.load("term_deposit_model.joblib")   # only files you created yourself
print(loaded.predict(X_test.head(3)))

**Narration over this clip (for pacing)**

> This cell cross-validates a dummy baseline and the real pipeline. Then it fits the final pipeline, scores it once on the test set, saves it to a file with the library version, loads it back, and predicts three customers.

## Clip 2: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L17_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Highlight the line baseline = Pipeline([("prep", prep), ("model", DummyClassifier(strategy="prior"))]).
2. Highlight cv=5 in both cross_val_score calls.

**Narration over this clip (for pacing)**

> Notice that the baseline sits inside the same pipeline, with the same preprocessing and five folds as the real model. So the comparison is fair. The only difference is the model at the end, and the baseline simply predicts the share of subscribers for everyone.

## Clip 3: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L17_screen_3.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Highlight baseline CV AUC: 0.5 and model CV AUC: 0.778.

**Narration over this clip (for pacing)**

> The baseline scores zero point five, which is random ranking. The model scores zero point seven seven eight in cross-validation, so it clearly learns something.

## Clip 4: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L17_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Highlight test AUC: 0.752.
2. Add the caption: final number, scored once.

**Narration over this clip (for pacing)**

> The single test score is zero point seven five two. It is a little lower than the cross-validation mean, but within the spread you saw in lesson ten. Elena reports it as her final number.

## Clip 5: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L17_screen_5.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Highlight saved with scikit-learn 1.9.1.
2. Highlight the loaded model's prediction [0 0 0].

**Narration over this clip (for pacing)**

> The whole pipeline, including preprocessing, is saved to one file, with scikit-learn version one point nine point one. Loading it back and predicting three customers confirms that the file works.

## Clip 6: scene 13

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L17_screen_6.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open the Colab Files panel, right-click term_deposit_model.joblib and choose Download.
2. Add a text cell: scikit-learn 1.9.1 · threshold 0.15 (L09) · date.

**Narration over this clip (for pacing)**

> Colab storage is temporary, so we download the file from the Files panel. Elena also adds a text cell with the library version, her chosen threshold of zero point one five from lesson nine, and the date.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The L17 cell uses Pipeline, prep, pipe, X_train, y_train, X_test and y_test from those cells. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERIFY] Availability and licences of the suggested datasets (UCI Bank Marketing, UCI Online Shoppers Purchasing Intention, UCI Seoul Bike Sharing Demand, Kaggle telecom churn and hotel booking datasets), and that Kaggle needs a free account. The voiceover names only UCI and Kaggle as places to look and tells learners to read and record each licence; it does not name specific datasets.
- [VERSION] Kaggle download steps in Colab (account, API token, commands) and the Colab Files panel may change. Check the download step in scene 13 against the live interface.
- [VERSION] joblib model files depend on scikit-learn and dependency versions and must not be loaded from untrusted sources. Outputs were recorded with scikit-learn 1.9.1, joblib 1.6.0 and Python 3.11 on synthetic data; re-run before recording and update the spoken scores and version if they differ.
- Screen scenes 8 to 13 use one cell copied exactly from the content.md Worked Example.
- Elena Popescu and the Cluj-Napoca bank are fictional; the data is synthetic.
