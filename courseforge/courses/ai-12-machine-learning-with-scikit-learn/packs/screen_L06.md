# Screen Demo Pack: AI-12 L06 Logistic Regression for Yes/No Questions

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L06_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Scroll past the L05 setup and pipeline cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
import pandas as pd

names = pipe.named_steps["prep"].get_feature_names_out()
coefs = pd.Series(pipe.named_steps["model"].coef_[0], index=names)
print(coefs.sort_values().round(2))

print(pipe.predict_proba(X_test.head(3))[:, 1].round(2))
print(pipe.predict(X_test.head(3)))

**Narration over this clip (for pacing)**

> This cell takes the readable feature names from the preprocessing step, pairs them with the model's coefficients, and sorts them. Then it prints the probability of yes for the first three test customers, and the model's yes or no decision for each.

## Clip 2: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L06_screen_2.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Highlight the last three rows: num__balance 0.42, num__age 0.58, cat__job_retired 0.82.

**Narration over this clip (for pacing)**

> At the bottom of the list are the largest positive coefficients. Being retired has the strongest push, zero point eight two. Then older age, zero point five eight, and a higher balance, zero point four two. These raise the probability of subscribing.

## Clip 3: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L06_screen_3.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Highlight the first three rows: num__calls -0.69, cat__contact_telephone -0.36, cat__job_technician -0.34.

**Narration over this clip (for pacing)**

> At the top are the largest negative ones. More calls in this campaign, minus zero point six nine. Telephone contact, minus zero point three six. And technician jobs, minus zero point three four. These lower the probability.

## Clip 4: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L06_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Highlight the output [0.03 0.02 0.17].
2. Highlight the output [0 0 0].
3. Point to the num__ and cat__ prefixes in the coefficient list.

**Narration over this clip (for pacing)**

> Now the first three test customers. Their probabilities of yes are three percent, two percent and seventeen percent. All are below zero point five, so all three are predicted no. The prefixes num and cat simply come from the step names in the column transformer.

## Clip 5: scene 13

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L06_screen_5.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Add a text cell: More calls is linked with fewer subscriptions. Cause unknown.

**Narration over this clip (for pacing)**

> Priya notes one thing. More calls lowers the probability. That could mean repeated calls annoy people. Or it could mean the bank keeps calling people who were never interested. The model cannot tell which.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] get_feature_names_out, named_steps and LogisticRegression defaults (regularisation, solver) depend on the installed version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on the synthetic stand-in data; re-run before recording and update the spoken coefficients and probabilities if they differ.
- Screen scenes 9 to 13 use one cell copied exactly from the content.md Worked Example.
- Speak negative coefficients as 'minus zero point six nine'; the screen shows -0.69. Speak probabilities as percentages, as content.md does (3%, 2% and 17%).
- Priya Nair and the Kochi bank are fictional; the data is synthetic.
