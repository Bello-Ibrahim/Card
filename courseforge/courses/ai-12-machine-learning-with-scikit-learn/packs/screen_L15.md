# Screen Demo Pack: AI-12 L15 Which Features Matter? Interpreting Models

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L15_screen_1.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Scroll past the L05 setup and pipeline cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
from sklearn.inspection import permutation_importance
import pandas as pd

result = permutation_importance(pipe, X_test, y_test, scoring="roc_auc",
                                n_repeats=20, random_state=42)
imp = pd.DataFrame({"mean": result.importances_mean, "std": result.importances_std},
                   index=X_test.columns)
print(imp.sort_values("mean", ascending=False).round(3))

**Narration over this clip (for pacing)**

> This cell runs permutation importance on the test set, scored by ROC AUC. It shuffles each original column twenty times, and records the average drop and its spread. Then it prints the columns sorted from most to least important.

## Clip 2: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L15_screen_2.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Highlight the rows calls 0.078, age 0.066 and job 0.065.

**Narration over this clip (for pacing)**

> Shuffling the number of calls lowers ROC AUC by about zero point zero seven eight on average. That is the largest drop. Age follows closely at zero point zero six six, and job at zero point zero six five.

## Clip 3: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L15_screen_3.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Highlight the row contact 0.030 0.013.
2. Highlight the row balance 0.011 0.012 and label it 'no clear effect'.

**Narration over this clip (for pacing)**

> Contact type drops the score by zero point zero three zero. Balance has a mean drop of zero point zero one one, with a spread of zero point zero one two. The spread is larger than the mean, so its effect cannot be separated from zero with this test set.

## Clip 4: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L15_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Add a text cell and type sentence 1 from content.md.

**Narration over this clip (for pacing)**

> Then Mei Lin writes three sentences for the sales manager. One. The number of times we have already called a customer in this campaign is the strongest signal. Customers called many times are less likely to subscribe.

## Clip 5: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L15_screen_5.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Type sentences 2 and 3 from content.md in the same text cell.
2. Highlight 'not proof'.

**Narration over this clip (for pacing)**

> Two. Age and job type matter almost as much. Older and retired customers are more likely to say yes. Three. Account balance adds very little once we know the other information. These are patterns in past data, not proof that calling less will make people subscribe.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The L15 cell uses the fitted logistic pipe, X_test and y_test. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERIFY] Content.md says impurity-based tree importances are computed on training data and favour numeric features with many distinct values. The voiceover only says tree importances have 'known limits'; check the claim against the current scikit-learn user guide before adding detail.
- [VERSION] sklearn.inspection.permutation_importance arguments and result attributes depend on the installed version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on synthetic data; re-run before recording and update the spoken importances if they differ.
- Screen scenes 8 to 12 use one cell copied exactly from the content.md Worked Example. With 20 repeats the cell takes a few seconds.
- Tan Mei Lin and the Kuala Lumpur bank are fictional; the data is synthetic.
