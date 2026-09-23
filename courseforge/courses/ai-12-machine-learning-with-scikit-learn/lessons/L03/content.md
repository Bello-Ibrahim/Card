# L03 Train/Test Split and Why It Matters

Course: AI-12 · Module: M1 · Objectives: O2 · Video: 5 min (screen demo)

## Hook
In L02 the decision tree predicted every training row correctly. That sounds perfect, but it tells us almost nothing. A model is useful only if it works on data it has never seen. Today you will see a model with 100% training accuracy lose more than a quarter of that on new data.

## Explanation
The goal of a model is **generalisation**: good predictions on new cases. To estimate this, we hold back part of the data as a **test set**. The model never sees it during training. We train on the **training set** and measure on the test set.

scikit-learn does this with `train_test_split`. Three arguments matter:

- `test_size=0.25` keeps 25% of rows for testing. Values between 0.2 and 0.3 are common for medium-sized data.
- `random_state=42` fixes the shuffle, so everyone gets the same split and your results are repeatable.
- `stratify=y` keeps the same share of each class in both sets. This matters when one class is rare. Without it, a small test set could, by chance, contain very few positive cases.

Comparing training and test scores tells you a lot:

- **Overfitting:** the training score is high and the test score is much lower. The model has learned the noise and details of the training rows instead of the general pattern.
- **Underfitting:** both scores are low. The model is too simple to capture the pattern.
- **A good fit:** both scores are reasonably high and close to each other.

A very high training score on its own is never evidence of a good model. A flexible model, such as a decision tree with no depth limit, can always reach close to 100% on its own training data.

**Analogy:** A fair exam uses questions the student has not seen before. If a teacher gives the exact questions from the homework, a student who memorised the answers will score 100%, but the score does not show whether the student understands the subject. The test set is the fair exam for your model.

## Worked Example
Fatima Zahra is an analyst at a hypothetical insurance company in Casablanca, Morocco. Before she uses real claims data, she tests the idea on synthetic data from `make_classification`, which creates a reproducible classification problem. The setting `flip_y=0.1` adds label noise, as real data has.

On screen, the presenter runs this cell and reads each line of output aloud:

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = make_classification(n_samples=1000, n_features=10, n_informative=4,
                           flip_y=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42)

for depth in [None, 3]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    print(depth, round(tree.score(X_train, y_train), 3),
          round(tree.score(X_test, y_test), 3))
```

Output (scikit-learn 1.9.1): [VERSION]

```
None 1.0 0.728
3 0.853 0.812
```

The deep tree (`max_depth=None`) scores 1.0 on training data and 0.728 on test data. It memorised the training rows, including the noisy labels. The shallow tree scores lower on training data (0.853) but higher on test data (0.812), and its two scores are much closer. Fatima chooses the shallow tree as her starting point and writes: "The training score of 1.0 was a warning sign, not a success."

Note the order of the four outputs: `X_train, X_test, y_train, y_test`. Mixing up this order is a common bug, so the presenter should point to it on screen.

## Common Mistake
Many learners use the test set again and again: they try a setting, check the test score, change the setting, and check again. After many rounds, the test set is no longer "unseen", because your choices have been fitted to it, and the final score is too optimistic. Keep the test set for one final check. For choosing between models and settings, use cross-validation on the training set, which you will learn in L10.

## Key Takeaways
1. Hold back a test set with `train_test_split`, and use `random_state` and `stratify=y` for repeatable, balanced splits.
2. A large gap between a high training score and a lower test score means overfitting; two low scores mean underfitting.
3. A high training score alone proves nothing. Keep the test set for the final check only.

## Hands-on Exercise
**Task:** Compare training and test accuracy for a deep and a shallow decision tree, and explain the gap in 2 sentences.
**Tools:** Google Colab (free), scikit-learn.
**Steps:**
1. Create the synthetic data with the code above, or use the wine data from L02.
2. Split the data with `test_size=0.25`, `stratify=y` and `random_state=42`.
3. Train one tree with `max_depth=None` and one with `max_depth=3`.
4. Print training and test accuracy for both, rounded to 3 decimals.
5. Change `random_state` in the split to 0 and 7, and run again. Note how much the test scores move.
6. Write 2 sentences that explain the gap for the deep tree and which tree you would choose.
**What good looks like:** A small table of 4 numbers per split, and 2 clear sentences that use the words "overfitting" and "unseen data". You notice that the test score changes a little with each split, which prepares you for L10.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Outputs were recorded with scikit-learn 1.9.1 and Python 3.11. `make_classification` and `train_test_split` results can change between versions; re-run in the current Colab version before recording.
