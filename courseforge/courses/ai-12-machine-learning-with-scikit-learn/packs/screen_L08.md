# Screen Demo Pack: AI-12 L08 Accuracy Is Not Enough: The Confusion Matrix

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L08_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Type this exact code cell from content.md and run it with Shift+Enter:
from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, recall_score

Xf, yf = make_classification(n_samples=10000, weights=[0.99], flip_y=0,
                             random_state=1)
lazy = DummyClassifier(strategy="most_frequent").fit(Xf, yf)
pred = lazy.predict(Xf)
print(round(accuracy_score(yf, pred), 3), recall_score(yf, pred))

**Narration over this clip (for pacing)**

> This cell creates ten thousand synthetic payments, with only one percent fraud. It fits a baseline that always predicts the most common class, then prints its accuracy and its recall.

## Clip 2: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L08_screen_2.mp4`
- **Target length:** about 8 seconds

**Steps**

1. Highlight the output 0.99 0.0.
2. Label 0.99 'accuracy' and 0.0 'recall'.

**Narration over this clip (for pacing)**

> Accuracy is zero point nine nine. Recall is zero. The model found none of the one hundred fraud cases.

## Clip 3: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L08_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Scroll up to show the L05 setup and pipeline cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
from sklearn.metrics import confusion_matrix, classification_report

y_pred = pipe.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))

**Narration over this clip (for pacing)**

> Now back to the term-deposit pipeline from lesson five, where about twelve percent of customers subscribe. This cell predicts the test set, then prints the confusion matrix and a full report of the metrics.

## Clip 4: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L08_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Highlight the matrix [[435 5] [53 7]].
2. Label the cells TN 435, FP 5, FN 53, TP 7.

**Narration over this clip (for pacing)**

> Read the matrix. Of sixty real subscribers, the model found seven, and missed fifty-three. It raised twelve flags, and seven of them were correct. The other four hundred and thirty-five customers were correctly left alone, and five were false alarms.

## Clip 5: scene 13

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L08_screen_5.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Zoom in on the report row for class 1: 0.583, 0.117, 0.194, support 60.
2. Show the overlay calculation 7 / (7 + 5) and 7 / (7 + 53).

**Narration over this clip (for pacing)**

> So precision is seven out of twelve, zero point five eight three. Recall is seven out of sixty, zero point one one seven. And F one is only zero point one nine four.

## Clip 6: scene 14

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L08_screen_6.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Highlight the accuracy row: 0.884, 500.
2. Show the overlay 440 / 500 = 0.88 next to it.

**Narration over this clip (for pacing)**

> The accuracy is zero point eight eight four, as in lesson five. But always saying no would score four hundred and forty out of five hundred, which is zero point eight eight. For a bank that wants to find subscribers, this model is weak at the default setting.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The first L08 cell (fraud baseline) runs on its own; the second cell needs pipe, X_test and y_test from L05. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] classification_report layout and metric defaults depend on the installed version. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data; re-run before recording and update every spoken count and score if they differ.
- Screen scenes 9 and 10 use the first L08 cell; scenes 11 to 14 use the second cell. Both are copied exactly from the content.md Worked Example. Content.md shows a shortened report; show the full report on screen and zoom in on the rows for class 1 and accuracy.
- Scene 13: show the hand calculation as an overlay: 7 / (7 + 5) = 0.583 and 7 / (7 + 53) = 0.117.
- Aigerim Bekova and the Almaty payment company are fictional; the fraud data is synthetic.
