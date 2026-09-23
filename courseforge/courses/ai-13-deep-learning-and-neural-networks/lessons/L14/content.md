# L14 Evaluating Deep Models Properly

Course: AI-13 · Module: M3 · Objectives: O5, O6 · Video: 5 min (screen demo)

## Hook
You change the learning rate and your model's accuracy goes up by one percentage point. Is the new setting better? Run the old setting again with a different random seed, and it may move by one point on its own. Before you compare models, you need to know how much a result changes by chance.

## Explanation
**Quick recap from AI-12.** Use three splits: **training** to fit weights, **validation** to make choices (epochs, hyperparameters, architecture), and **test** to measure the final choice once. Look beyond one number: a **confusion matrix** and per-class precision, recall and F1 show which classes are confused.

Deep models add two reasons to be careful.

**1. Randomness is everywhere.** The random seed controls the new layer's initial weights, the data shuffling order, dropout masks and augmentation. Two runs with identical settings but different seeds can give noticeably different scores, especially on small datasets. Run important settings with **3 or more seeds** and report the **mean and the spread** (standard deviation, or minimum and maximum). If two settings' ranges overlap a lot, you have not shown that one is better.

**2. Many choices use up the validation set.** Every time you look at validation results and change something, you fit your decisions a little to that split. After many experiments, the validation score becomes optimistic. This is why the test set stays locked until the end (L19).

**Error analysis** turns a score into a plan. Collect the misclassified validation examples, read them, and group them: wrong or unclear labels, examples that really belong to two classes, very short or unusual inputs, or a pattern the model has not learned. Each group suggests a different fix: cleaning labels, changing the class definitions, collecting data, or changing the model.

**Analogy:** One football match does not tell you which team is stronger. A lucky goal can decide it. A league of many matches gives a fairer picture. Running several seeds is a small league for your models, and error analysis is watching the recording of the matches you lost.

## Worked Example
Ayesha is an ML engineer at a hypothetical non-profit in Dhaka, Bangladesh, that sorts English news summaries by topic for a media-monitoring project. She uses the AG News setup from L13 and wants to report a trustworthy result.

**Screen demo steps:**

1. Wrap the L13 training code in a function that takes a seed and returns the validation predictions and scores.
2. Run it with 3 seeds and report the mean and spread.
3. Show the confusion matrix for one run and list misclassified examples.

```python
import numpy as np
from sklearn.metrics import f1_score, ConfusionMatrixDisplay

results = []
for seed in [0, 1, 2]:
    preds, labels = run_experiment(seed=seed)        # your L13 code; returns NumPy arrays
    results.append(f1_score(labels, preds, average="macro"))
print(f"macro F1: mean {np.mean(results):.3f}, std {np.std(results):.3f}, "
      f"min {min(results):.3f}, max {max(results):.3f}")

ConfusionMatrixDisplay.from_predictions(labels, preds,
    display_labels=["World", "Sports", "Business", "Sci/Tech"])

val_texts = val_split["text"]                        # same order as preds
wrong = np.where(preds != labels)[0]
for i in wrong[:10]:
    print(labels[i], "->", preds[i], "|", val_texts[i][:120])
```

`run_experiment` must set the seed in `TrainingArguments` and in any subset shuffling, so that each run is repeatable. Ayesha finds that most errors are between Business and Sci/Tech: summaries about technology companies' earnings could fit either label. A few look mislabelled. Her conclusion: a larger model may help a little, but the class definitions themselves overlap, and she writes this down as a limitation.

## Common Mistake
Many learners compare two settings using one run each and report the winner, even when the difference is smaller than the normal variation between seeds. Another mistake is doing error analysis on the test set, then changing the model based on what they saw. The test set has then become a second validation set, and the final score is no longer an honest estimate. Do error analysis on validation data, and keep the test set for the final, single check.

## Key Takeaways
1. Keep separate validation and test splits; make every choice on validation and use test once, at the end.
2. Run key settings with at least 3 seeds and report the mean and spread before claiming that one setting is better.
3. Read and group misclassified examples to find whether the problem is the labels, the class definitions, the data or the model.

## Hands-on Exercise
**Task:** Run your text model with 3 seeds, report the mean and spread, and review 10 misclassified examples to find a pattern.
**Tools:** Google Colab with a GPU runtime (free; optional); your L13 notebook; scikit-learn. CPU fallback: use the smaller L13 subset and 1 epoch per run.
**Steps:**
1. Turn your L13 training code into a function with a `seed` argument that returns validation predictions and labels.
2. Run it with seeds 0, 1 and 2, and record accuracy and macro F1 for each.
3. Report the mean, standard deviation, minimum and maximum for both metrics.
4. Plot a confusion matrix for one run and name the most confused pair of classes.
5. Read 10 misclassified validation examples, give each a short reason, and group the reasons.
6. Write one paragraph: how stable is the model, what is the main error pattern, and what would you change first?
**What good looks like:** Three seeded runs with a clear mean and spread, a labelled confusion matrix, 10 examples with reasons grouped into patterns, and a recommendation that follows from the evidence. The test set is not used.
**Time:** about 40 minutes

## Review Flags
- [VERIFY] AG News dataset licence and source (carried from L13), because the dataset is reused in this lesson.
