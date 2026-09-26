# Screen Demo Pack: AI-12 L09 Probabilities, Thresholds and ROC Curves

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L09_screen_1.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Scroll past the L05 setup and pipeline cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
pred = (proba >= 0.3).astype(int)

**Narration over this clip (for pacing)**

> This cell takes the model's probabilities for the test customers and prints the ROC AUC. Then it tries three thresholds, and for each one it prints precision and recall.

## Clip 2: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L09_screen_2.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Highlight ROC AUC: 0.752.
2. Highlight the rows 0.5 0.583 0.117 and 0.3 0.396 0.317.

**Narration over this clip (for pacing)**

> ROC AUC is zero point seven five two. At zero point five, precision is zero point five eight three and recall is zero point one one seven, the same as last lesson. At zero point three, precision falls to zero point three nine six, and recall rises to zero point three one seven.

## Clip 3: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L09_screen_3.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Highlight the row 0.15 0.292 0.667.
2. Add a caption: finds 2 in 3, about 29% of flags correct.

**Narration over this clip (for pacing)**

> At zero point one five, the model finds two thirds of subscribers, a recall of zero point six six seven. But only about twenty-nine percent of flags are correct, a precision of zero point two nine two.

## Clip 4: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L09_screen_4.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Type this exact code cell from content.md and run it with Shift+Enter:
import numpy as np
from sklearn.metrics import roc_auc_score, precision_score, recall_score

proba = pipe.predict_proba(X_test)[:, 1]
print("ROC AUC:", round(roc_auc_score(y_test, proba), 3))
for t in [0.5, 0.3, 0.15]:
    pred = (proba >= t).astype(int)
    print(t, round(precision_score(y_test, pred), 3), round(recall_score(y_test, pred), 3))

**Narration over this clip (for pacing)**

> Now we add costs. An unneeded call costs one unit, and a missed case costs eight. This cell gets cross-validated probabilities on the training data only, then adds up the cost of each mistake for thresholds from zero point zero five to zero point nine.

## Clip 5: scene 13

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L09_screen_5.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Highlight the output 0.1 813 1381.
2. Label: best threshold 0.1 · cost 813 · cost at 0.5: 1381.

**Narration over this clip (for pacing)**

> The best threshold is zero point one. It costs eight hundred and thirteen units, against one thousand, three hundred and eighty-one at the default zero point five. With these costs, a low threshold is clearly better.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The second L09 cell also needs numpy, imported in the first L09 cell, so run the two L09 cells in order. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] RocCurveDisplay, PrecisionRecallDisplay and TunedThresholdClassifierCV depend on the installed version; the voiceover mentions only the display tools in general terms. Outputs were recorded with scikit-learn 1.9.1, NumPy 2.4 and Python 3.11 on synthetic data; re-run before recording and update every spoken value if it differs.
- Screen scenes 9 to 11 use the first L09 cell; scenes 12 and 13 use the second cell. Both are copied exactly from the content.md Worked Example.
- The clinic case is hypothetical on purpose (curriculum flag), to avoid unverified claims about real organisations; no patient data is used. Stock footage must not show a real clinic name, logo or identifiable patients.
- Dr. Wanjiru Kamau is fictional. Speak thresholds as 'zero point one five' and costs as 'eight hundred and thirteen' and 'one thousand, three hundred and eighty-one'.
