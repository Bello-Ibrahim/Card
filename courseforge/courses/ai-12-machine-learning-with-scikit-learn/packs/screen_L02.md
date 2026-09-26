# Screen Demo Pack: AI-12 L02 Your First Model: fit and predict

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L02_screen_1.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Open Google Colab in the browser and create a new notebook.
2. Type this exact code cell from content.md and run it with Shift+Enter:
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier

X, y = load_wine(return_X_y=True, as_frame=True)
print(X.shape, y.value_counts().sort_index().tolist())

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)
print(model.predict(X.iloc[[0, 60, 130, 20, 100]]))
3. Pause on the finished cell before scrolling to the output.

**Narration over this clip (for pacing)**

> Let's open Google Colab and create a new notebook. In the first cell, we load the wine data, create a decision tree, fit it, and predict five wines. Then we run the cell.

## Clip 2: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L02_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Highlight the first output line: (178, 13) [59, 71, 48].
2. Point to 178 rows, then 13 columns, then the three class counts.

**Narration over this clip (for pacing)**

> The first line of output describes the data. There are one hundred and seventy-eight wines, with thirteen chemical measurements each. The three classes of wine have fifty-nine, seventy-one and forty-eight examples.

## Clip 3: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L02_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Highlight as_frame=True in the load_wine line.
2. Add a callout next to it: returns a pandas DataFrame, so column names stay visible.

**Narration over this clip (for pacing)**

> We asked for the data as a pandas table, so the column names stay visible. That makes it much easier to check which chemical measurement is which, and it will matter more when you work with your own data.

## Clip 4: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L02_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Highlight the line that creates DecisionTreeClassifier(random_state=0) and label it 'Create'.
2. Highlight model.fit(X, y) and label it 'Fit'.
3. Highlight model.predict(...) and label it 'Predict'.

**Narration over this clip (for pacing)**

> Now look at the three stages in the code. First, we create the tree with a fixed random state, so everyone who runs this gets the same tree. Then it learns from all the wines. Then it predicts.

## Clip 5: scene 13

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L02_screen_5.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Highlight the second output line: [0 1 2 0 1].
2. Point back to X.iloc[[0, 60, 130, 20, 100]] and note these rows were used in fit.

**Narration over this clip (for pacing)**

> The model predicted classes zero, one, two, zero and one for the five chosen rows. Kenji is pleased. But wait. These five wines were also in the training data. Did the model predict them, or did it simply remember them? That question leads directly to our next lesson.

## Production notes for this lesson

- [VERSION] Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11. Re-run the cell in the current Colab version before recording; if the printed shape, class counts or predictions differ, update the voiceover and captions to match the new output.
- [VERSION] Check load_wine with as_frame and the estimator defaults against the installed version; show sklearn.__version__ if the output differs.
- Screen scenes 9 to 13 use one Colab cell, copied exactly from the content.md Worked Example. Run it once off camera to warm up the runtime, then record a clean run.
- Kenji Watanabe is fictional. The wine dataset ships with scikit-learn, so no download is needed.
- Speak printed values as numbers, for example 'one hundred and seventy-eight' and 'fifty-nine, seventy-one, forty-eight'; the screen shows the exact output.
