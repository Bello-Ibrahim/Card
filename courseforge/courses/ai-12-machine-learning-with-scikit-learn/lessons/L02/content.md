# L02 Your First Model: fit and predict

Course: AI-12 · Module: M1 · Objectives: O1, O3 · Video: 5 min (screen demo)

## Hook
scikit-learn contains dozens of models, from simple lines to large forests of trees. The good news is that you use almost all of them in the same way. Learn two method calls today, `fit` and `predict`, and you can use most of the library.

## Explanation
In scikit-learn, a model is called an **estimator**. Every estimator follows the same pattern:

1. **Create** it and choose its settings, for example `DecisionTreeClassifier(max_depth=3)`. Nothing is learned yet.
2. **Fit** it with `model.fit(X, y)`. `X` is a table of features, with one row per example and one column per feature. `y` is the target, with one value per row. Fitting is where learning happens.
3. **Predict** with `model.predict(X_new)`. The model uses what it learned to give a target value for each new row.

Some objects do not predict. They change data instead, such as a scaler that puts numbers on the same scale. These are called **transformers**, and they use `fit` and `transform`. You will use them in L04. Many estimators also have a `score` method that returns a default metric, such as accuracy for classifiers.

Two naming rules help you read the documentation. Settings you choose before training are **hyperparameters**, passed to the constructor. Values the model learns during `fit` end with an underscore, such as `classes_` or `feature_importances_`.

The exact list of settings and defaults depends on your installed version, so check `sklearn.__version__` in Colab and open the matching documentation. [VERSION]

**Analogy:** scikit-learn estimators are like kitchen appliances from one brand. A blender, a toaster and a kettle do very different jobs, but they all have the same "on" and "start" buttons. Once you know where the buttons are, you can use a new appliance quickly. `fit` and `predict` are the buttons.

## Worked Example
Kenji Watanabe is a developer in Osaka who wants a first model before he works with company data. He uses the wine dataset that ships with scikit-learn: 178 wines, 13 chemical measurements each, and 3 classes of wine.

On screen, the presenter follows these steps in a new Colab notebook:

1. Open Google Colab and create a new notebook.
2. In the first cell, type the code below and run it with Shift+Enter.
3. Point out the shape `(178, 13)` and the class counts.
4. Point out the three stages: create, fit, predict.

```python
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier

X, y = load_wine(return_X_y=True, as_frame=True)
print(X.shape, y.value_counts().sort_index().tolist())

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)
print(model.predict(X.iloc[[0, 60, 130, 20, 100]]))
```

Output (scikit-learn 1.9.1): [VERSION]

```
(178, 13) [59, 71, 48]
[0 1 2 0 1]
```

`as_frame=True` returns a pandas DataFrame, so the column names stay visible. `random_state=0` makes the result repeatable: the tree has a small random element, and a fixed seed means everyone who runs this code gets the same tree.

The model predicted classes 0, 1, 2, 0 and 1 for the five chosen rows. Kenji is pleased, but the presenter asks a question: these five wines were also in the training data. Did the model predict them, or did it remember them? That question leads directly to L03.

## Common Mistake
Many learners pass the data in the wrong shape. `X` must be two-dimensional, even for one feature: use `df[["alcohol"]]` (a DataFrame), not `df["alcohol"]` (a Series). To predict one row, keep it as a table, for example `X.iloc[[0]]` with double brackets. A related mistake is calling `predict` before `fit`, which raises a `NotFittedError`. The fix is always the same order: create, fit, then predict.

## Key Takeaways
1. Every scikit-learn estimator is created with settings, learns with `fit(X, y)` and is used with `predict(X_new)`.
2. `X` is a two-dimensional table of features and `y` is one target value per row; learned values end with an underscore.
3. Set `random_state` so that your results are repeatable, and check your library version before trusting parameter names.

## Hands-on Exercise
**Task:** Load the wine dataset, train a `DecisionTreeClassifier`, and predict the class of 5 samples.
**Tools:** Google Colab (free), scikit-learn and pandas (already installed in Colab).
**Steps:**
1. Open a new Colab notebook and run `import sklearn; print(sklearn.__version__)`. Write the version in a text cell.
2. Load the wine data with `load_wine(return_X_y=True, as_frame=True)` and print `X.head()` and `X.shape`.
3. Create `DecisionTreeClassifier(random_state=0)` and fit it on `X` and `y`.
4. Choose 5 row numbers and predict their classes with `X.iloc[[...]]`.
5. Compare the predictions with `y.iloc[[...]]`.
6. Print `model.classes_` and explain in a text cell what the underscore means.
**What good looks like:** A notebook that runs from top to bottom without errors, shows the library version, 5 predictions next to the true classes, and one sentence noting that these rows were seen during training, so this is not yet a fair test.
**Time:** about 20 minutes

## Review Flags
- [VERSION] scikit-learn API details (`load_wine` with `as_frame`, estimator defaults) depend on the installed version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11; re-run in the current Colab version before recording.
