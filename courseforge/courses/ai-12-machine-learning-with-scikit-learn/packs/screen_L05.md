# Screen Demo Pack: AI-12 L05 Pipelines and ColumnTransformer

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L05_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Open a new Colab notebook and add a text cell: Setup cell, shared by L05 to L17.
2. Type this exact code cell from content.md and run it with Shift+Enter:
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(42)
n = 2000
df = pd.DataFrame({
    "age": rng.integers(18, 80, n),
    "balance": rng.normal(1500, 800, n).round(),
    "calls": rng.integers(1, 8, n),
    "job": rng.choice(["admin", "technician", "services", "retired"], n),
    "contact": rng.choice(["cellular", "telephone"], n),
})
score = (-3 + 0.03 * (df["age"] - 40) + 0.0006 * df["balance"] - 0.3 * df["calls"]
         + 1.2 * (df["job"] == "retired") + 0.8 * (df["contact"] == "cellular"))
df["subscribed"] = (rng.random(n) < 1 / (1 + np.exp(-score))).astype(int)
df.loc[rng.choice(n, 100, replace=False), "balance"] = np.nan

X, y = df.drop(columns="subscribed"), df["subscribed"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42)

**Narration over this clip (for pacing)**

> First, we run the setup cell. It creates two thousand synthetic customers with age, balance, number of calls, job and contact type. It hides one hundred balances as missing values. Then it splits the data once, keeping a quarter for testing. We will reuse this cell for most of the course.

## Clip 2: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L05_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Highlight the line X, y = df.drop(columns="subscribed"), df["subscribed"].
2. Highlight stratify=y and random_state=42 in the train_test_split call.

**Narration over this clip (for pacing)**

> Look at the last lines of the setup cell. The target is whether the customer subscribed, and the features are all the other columns. The split keeps the same share of subscribers in both sets, and uses a fixed random state, so your numbers will match mine.

## Clip 3: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L05_screen_3.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Type this exact code cell from content.md and run it with Shift+Enter:
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

num_cols = ["age", "balance", "calls"]
cat_cols = ["job", "contact"]
numeric = Pipeline([("impute", SimpleImputer(strategy="median")),
                    ("scale", StandardScaler())])
prep = ColumnTransformer([
    ("num", numeric, num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
])
pipe = Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=1000))])
pipe.fit(X_train, y_train)
print(round(pipe.score(X_test, y_test), 3))

**Narration over this clip (for pacing)**

> Now the pipeline cell. For numbers, a small pipeline fills missing values with the median, then scales. For categories, a one-hot encoder. The column transformer sends each list of columns to its own step, and logistic regression is the final model. Then one fit call, and we print the test accuracy.

## Clip 4: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L05_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Highlight the output 0.884.
2. Highlight pipe.fit(X_train, y_train) and add a caption: one fit, every step.

**Narration over this clip (for pacing)**

> The test accuracy is zero point eight eight four. Notice what happened. The one hundred missing balances were filled with the training median, inside the pipeline. And that single fit call ran every step, in the right order.

## Clip 5: scene 13

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L05_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. In a new cell, type pipe and run it.
2. Click to expand the diagram: prep (num: impute, scale; cat: one-hot) and model.
3. Point back to 0.884.

**Narration over this clip (for pacing)**

> In Colab, you can display the pipeline itself, and you get a diagram of the steps. Keep that score of zero point eight eight four in mind. In lesson eight, you will see why it is less impressive than it looks.

## Production notes for this lesson

- content.md lists this lesson as 6 minutes; the script is held to the brief's 5-minute word range (630 to 770 words), so it runs about five and a half minutes.
- [VERIFY] The voiceover does not describe the UCI Bank Marketing dataset (source, column names campaign and duration, target y, licence). Content.md says it comes from a Portuguese bank's phone campaign for term deposits and that duration is only known after the call; both claims stay here for review and are not spoken.
- [VERSION] set_output(transform="pandas"), OneHotEncoder(sparse_output=...) and the pipeline diagram display in Colab depend on the installed scikit-learn version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11; re-run and update the spoken 0.884 if the output differs.
- Setup: scene 9 runs the shared setup cell (content.md Worked Example, first code block). This cell and the pipeline cell in scene 11 are reused in L06, L08, L09, L10, L14, L15, L16 and L17, so save the recording notebook as the course notebook.
- Scene 13: after the pipeline cell, run a new cell containing only pipe to show the Colab diagram, as content.md describes.
- Oluwaseun Adeyemi is fictional; the data is synthetic.
