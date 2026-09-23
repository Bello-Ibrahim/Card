# L07 Decision Trees and k-Nearest Neighbours

Course: AI-12 · Module: M2 · Objectives: O2, O3 · Video: 6 min (screen demo)

## Hook
Two models, two very different ideas. One asks a series of yes/no questions. The other asks, "Which past cases look most like this one?" Both are easy to understand, and both show clearly how a model can be too simple or too flexible.

## Explanation
A **decision tree** is a flowchart. At each node it asks a question about one feature, such as "Is age above 45?", and sends the row left or right. It chooses questions that separate the classes best. At the end, a leaf gives the prediction. The most important setting is `max_depth`, the number of questions in a row:

- A **shallow** tree (depth 1 or 2) asks too few questions and misses real patterns: **underfitting**.
- A **very deep** tree keeps splitting until each leaf holds a handful of training rows, often only one. It memorises noise: **overfitting**.

Other settings, such as `min_samples_leaf`, also limit how detailed the tree can become.

**k-nearest neighbours (KNN)** does not build rules. When it predicts, it finds the `k` training rows that are closest to the new row and takes a vote. It measures closeness as a distance across all features, so **scaling matters**. If one feature is in thousands and the others are below 10, the large feature decides almost alone. The setting `n_neighbors` controls flexibility: a small `k` follows single noisy points (overfitting); a very large `k` smooths away real differences (underfitting).

The best way to see this is a **validation curve**: plot the training and test scores while you change one setting. Where the training score keeps rising but the test score stops rising or falls, the model has started to overfit.

**Analogy:** A decision tree is like the game "Twenty Questions". A few good questions find the answer. But if you are allowed a thousand very specific questions about one person, you are no longer learning about people in general, you are describing that one person. KNN is like asking your closest neighbours for advice: useful, but only if you measure "close" fairly.

## Worked Example
Mateo Fernández works for a hypothetical farming cooperative in Argentina. He wants to understand model flexibility before he predicts crop problems. He uses the same synthetic data as L03, with the split already done.

On screen, the presenter runs a loop over tree depths and plots it:

```python
import matplotlib.pyplot as plt

depths, train_acc, test_acc = range(1, 21), [], []
for d in depths:
    tree = DecisionTreeClassifier(max_depth=d, random_state=42).fit(X_train, y_train)
    train_acc.append(tree.score(X_train, y_train))
    test_acc.append(tree.score(X_test, y_test))

plt.plot(depths, train_acc, label="train")
plt.plot(depths, test_acc, label="test")
plt.xlabel("max_depth"); plt.ylabel("accuracy"); plt.legend(); plt.show()
```

Selected values from the run (scikit-learn 1.9.1): [VERSION]

| max_depth | train | test |
|---|---|---|
| 1 | 0.689 | 0.648 |
| 4 | 0.865 | 0.828 |
| 8 | 0.947 | 0.792 |
| 13 to 20 | 1.000 | 0.728 |

The presenter points to depth 4, where the test score is highest. After that, training accuracy keeps rising to 1.0 but test accuracy falls. That is the start of overfitting.

Next, KNN on the wine data, with and without scaling:

```python
from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

Xw, yw = load_wine(return_X_y=True)
Xw_tr, Xw_te, yw_tr, yw_te = train_test_split(
    Xw, yw, test_size=0.3, stratify=yw, random_state=0)
raw = KNeighborsClassifier(n_neighbors=5).fit(Xw_tr, yw_tr)
scaled = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
scaled.fit(Xw_tr, yw_tr)
print(round(raw.score(Xw_te, yw_te), 3), round(scaled.score(Xw_te, yw_te), 3))
```

Output: `0.722 0.963` [VERSION]

One wine feature has values in the hundreds or thousands, so without scaling it dominates the distance. Scaling raises test accuracy from 0.722 to 0.963.

## Common Mistake
Learners often choose the depth or `k` with the highest **training** score. For trees that is always the deepest tree, and for KNN it is `k=1`, because each training row is its own nearest neighbour. Both choices overfit. Choose settings using held-out data, and later with cross-validation (L10) and tuning (L14).

## Key Takeaways
1. A decision tree asks yes/no questions; limit `max_depth` or `min_samples_leaf` to stop it memorising the training data.
2. KNN predicts from the most similar training rows, so always scale features first.
3. A plot of training and test scores against one setting shows where underfitting ends and overfitting begins.

## Hands-on Exercise
**Task:** Vary `max_depth` from 1 to 20, plot training and test scores, and mark where the model starts to overfit.
**Tools:** Google Colab (free), scikit-learn, matplotlib.
**Steps:**
1. Recreate the L03 data and split, or use your Bank Marketing pipeline with a `DecisionTreeClassifier` as the last step.
2. Run the loop above and draw the plot.
3. Add a vertical line at the depth with the best test score: `plt.axvline(best_depth, linestyle="--")`.
4. Label the underfitting area and the overfitting area in a text cell.
5. Repeat for KNN with `n_neighbors` from 1 to 30 inside a scaled pipeline, and compare the two plots.
**What good looks like:** Two clear plots with labelled axes and legends, the best setting marked, and 2 to 3 sentences that explain the shape of each curve.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, matplotlib 3.11 and Python 3.11. Tree results and the wine split can change between versions; re-run in the current Colab version before recording.
