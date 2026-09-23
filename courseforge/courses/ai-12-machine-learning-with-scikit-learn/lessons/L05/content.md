# L05 Pipelines and ColumnTransformer

Course: AI-12 · Module: M1 · Objectives: O2, O3 · Video: 6 min (screen demo)

## Hook
In L04 you scaled and encoded columns by hand, with separate objects and careful ordering. In a real project with 15 columns and many experiments, one small slip lets test data leak into training. A pipeline removes that risk: one object, one `fit`, and the right order every time.

## Explanation
A **Pipeline** chains steps into one estimator. Every step except the last is a transformer; the last step is the model. When you call `pipe.fit(X_train, y_train)`, each transformer is fitted on the training data and passes its output to the next step. When you call `pipe.predict(X_test)`, each step only transforms. Fitting on training data only happens automatically.

A **ColumnTransformer** sends different columns to different steps. Numbers go to imputation and scaling; categories go to one-hot encoding. The outputs are placed side by side.

This matters most for **data leakage**: any situation where information that would not be available at prediction time reaches the model during training. Leakage makes test scores look better than real performance. Pipelines stop one kind, preprocessing that learns from test rows. They also make cross-validation (L10) and tuning (L14) safe, because the whole chain is refitted inside every fold. They cannot stop the other kind, a feature that is recorded after the event, which you must remove yourself (L01).

`set_output(transform="pandas")` makes transformers return DataFrames with column names, which helps when you inspect the result. It needs a dense one-hot output (`sparse_output=False`). [VERSION]

**Analogy:** A pipeline is like a factory assembly line. Each station does one job in a fixed order, and a product cannot skip a station or enter halfway. The ColumnTransformer is the point where parts are sorted: metal parts go to one station and plastic parts to another, then they are joined again.

## Worked Example
Oluwaseun Adeyemi is a developer in Lagos who is learning with the UCI Bank Marketing data, which comes from a Portuguese bank's phone campaign for term deposits. [VERIFY] To keep the demo reproducible, the course notebook uses a synthetic stand-in with similar columns: `calls` plays the role of the real `campaign` column (number of contacts in this campaign), and about 12% of customers subscribe.

On screen, the presenter first runs the setup cell (shared by L05 to L17):

```python
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
```

Then the pipeline:

```python
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
```

Output (scikit-learn 1.9.1): `0.884` [VERSION]

The presenter points out that the 100 missing balances were filled with the training median inside the pipeline, and that one `fit` call ran all the steps. In Colab, displaying `pipe` shows a diagram of the steps. Keep the 0.884 in mind: in L08 you will see why it is less impressive than it looks.

## Common Mistake
Learners often build a good pipeline and then run `SimpleImputer` or `StandardScaler` on the full DataFrame "to clean it first". The pipeline is then fed data that already contains test information. Put every step that learns from data (imputers, scalers, encoders, feature selectors) inside the pipeline. Also check each column's meaning: in the real Bank Marketing data, the call `duration` is only known after the call ends, so it leaks the result and should not be a feature for a model used before calling. [VERIFY]

## Key Takeaways
1. A Pipeline chains preprocessing and a model into one estimator, so one `fit` call learns every step from training data only.
2. A ColumnTransformer applies different steps to numeric and categorical columns and joins the results.
3. Pipelines prevent preprocessing leakage, but you must still remove features that are only known after the event.

## Hands-on Exercise
**Task:** Build a pipeline for the Bank Marketing data that imputes, scales, encodes and fits a model, all in one fit call.
**Tools:** Google Colab (free), scikit-learn, pandas; the UCI Bank Marketing dataset [VERIFY], or the synthetic stand-in above. Use public data only; do not upload personal or confidential customer data to Colab or any AI tool.
**Steps:**
1. Load the data. For the UCI file, map the target `y` to 1 for "yes" and 0 for "no", and drop `duration`.
2. Split with `stratify=y` and `random_state=42`.
3. List your numeric and categorical columns.
4. Build the numeric sub-pipeline (median imputer, scaler) and the ColumnTransformer with `OneHotEncoder(handle_unknown="ignore")`.
5. Add `LogisticRegression(max_iter=1000)` as the last step and call `fit` once.
6. Print the test accuracy and display the pipeline diagram.
**What good looks like:** One pipeline object that runs without errors on raw training data, a test score, and a text cell that names which columns go to which step and why `duration` was removed.
**Time:** about 30 minutes

## Review Flags
- [VERIFY] Availability, description and licence of the UCI Bank Marketing dataset, including its column names (`campaign`, `duration`, target `y`) and the dataset notes about `duration`.
- [VERSION] `set_output(transform="pandas")` and `OneHotEncoder(sparse_output=...)` depend on the installed scikit-learn version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11.
