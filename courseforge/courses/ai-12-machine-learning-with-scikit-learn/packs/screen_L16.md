# Screen Demo Pack: AI-12 L16 Fairness, Limits and Model Risk

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L16_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Scroll past the L05 setup and pipeline cells, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
import pandas as pd

threshold = 0.15                      # chosen in L09
results = pd.DataFrame({
    "age_band": pd.cut(X_test["age"], bins=[17, 30, 50, 80],
                       labels=["18-30", "31-50", "51-79"]),
    "actual": y_test,
    "pred": (pipe.predict_proba(X_test)[:, 1] >= threshold).astype(int),
})
buyers = results[results["actual"] == 1]
summary = buyers.groupby("age_band", observed=True).agg(
    positives=("actual", "size"), recall=("pred", "mean"))
print(summary.round(2))

**Narration over this clip (for pacing)**

> We continue in the bank notebook. This cell groups test customers into three age bands, and applies the threshold of zero point one five. Then it keeps only the real subscribers, and for each band, counts them and calculates the share the model found. Among real subscribers, that share is the recall.

## Clip 2: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L16_screen_2.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Highlight the row 51-79: positives 40, recall 0.72.

**Narration over this clip (for pacing)**

> For customers aged fifty-one to seventy-nine, there are forty subscribers, and the model finds zero point seven two, or seventy-two percent of them.

## Clip 3: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L16_screen_3.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Highlight the row 31-50: positives 15, recall 0.53, in amber.

**Narration over this clip (for pacing)**

> For ages thirty-one to fifty, there are fifteen subscribers, and recall is only zero point five three. Fifty-three percent. That is the weakest group.

## Clip 4: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L16_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Highlight the row 18-30: positives 5, recall 0.60.
2. Add the label 'too small to judge'.

**Narration over this clip (for pacing)**

> The youngest group, eighteen to thirty, has a recall of zero point six zero. But it has only five subscribers in the test set, so that number could easily change with a different sample.

## Clip 5: scene 13

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L16_screen_5.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Add a text cell with the three-row risk note from content.md: risk and mitigation for each.

**Narration over this clip (for pacing)**

> Nomvula writes her risk note. Lower recall for ages thirty-one to fifty: review a lower threshold or better features. Too few young subscribers to judge: collect more data. Behaviour may change when interest rates change: check recall by group every month, and retrain when it falls below an agreed level.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The L16 cell uses the fitted logistic pipe, X_test and y_test, and the 0.15 threshold chosen in L09 (typed into the cell, so the L09 cells do not need to run). Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [REGION] Rules on collecting and using sensitive or protected attributes (for example gender or ethnicity) for fairness checks differ by country and sector. The voiceover says only that it depends on local law and company policy; do not add country-specific rules.
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on synthetic data. pd.cut and the observed argument of groupby should be checked against the Colab pandas version; re-run before recording and update the spoken group sizes and recall values if they differ.
- Screen scenes 9 to 13 use one cell copied exactly from the content.md Worked Example.
- The bank and the subgroup failure are hypothetical on purpose (curriculum flag), to avoid unverified claims about real organisations. Nomvula Dlamini is fictional. The hook's 90% and 30% are an illustrative 'what if', not results.
- Stock footage for scene 8 must not show identifiable customers' personal data or a real bank's name or logo.
