# L08 Accuracy Is Not Enough: The Confusion Matrix

Course: AI-12 · Module: M2 · Objectives: O4 · Video: 6 min (screen demo)

## Hook
Here is a fraud model that is 99% accurate and needs one line of code: it always says "not fraud". It never catches a single fraud case. If accuracy can praise a model like that, we need better ways to measure.

## Explanation
**Accuracy** is the share of all predictions that are correct. It works well when the classes are roughly balanced and both kinds of mistake cost about the same. It fails when one class is rare, which is common in business: fraud, churn, loan default, customers who buy.

The **confusion matrix** shows where the model is right and wrong. For a yes/no problem, scikit-learn prints it with actual classes as rows and predicted classes as columns:

|  | predicted no | predicted yes |
|---|---|---|
| **actual no** | true negatives (TN) | false positives (FP) |
| **actual yes** | false negatives (FN) | true positives (TP) |

From these four counts come three key metrics. The maths was covered in AI-05, so here is what each one means in words:

- **Precision:** of all the cases the model flagged as "yes", what share really were "yes"? High precision means few false alarms.
- **Recall:** of all the real "yes" cases, what share did the model find? High recall means few missed cases.
- **F1:** one number that balances precision and recall. It is high only when both are reasonably high.

Precision and recall usually pull against each other. Flag more cases and you find more real ones (recall up) but also more false alarms (precision down). Which one matters more depends on the cost of each mistake, which you wrote down in L01.

A useful habit is to compare every model with a **baseline** that always predicts the most common class. scikit-learn provides one: `DummyClassifier`.

**Analogy:** A smoke alarm that never rings is "correct" on almost every day of the year, because most days have no fire. But it fails on the one day that matters. Recall asks, "Did it ring when there was a fire?" Precision asks, "When it rang, was there really a fire?"

## Worked Example
Aigerim Bekova is a data analyst at a hypothetical payment company in Almaty, Kazakhstan. About 1 in 100 card payments in her synthetic test data is fraud. She first shows her team the "lazy" baseline.

On screen, the presenter runs:

```python
from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, recall_score

Xf, yf = make_classification(n_samples=10000, weights=[0.99], flip_y=0,
                             random_state=1)
lazy = DummyClassifier(strategy="most_frequent").fit(Xf, yf)
pred = lazy.predict(Xf)
print(round(accuracy_score(yf, pred), 3), recall_score(yf, pred))
```

Output (scikit-learn 1.9.1): `0.99 0.0` [VERSION]

Accuracy is 99%, recall is 0. The model found none of the 100 fraud cases.

Next, the presenter returns to the term-deposit pipeline from L05 (about 12% of customers subscribe) and prints its confusion matrix and report:

```python
from sklearn.metrics import confusion_matrix, classification_report

y_pred = pipe.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))
```

Output (shortened): [VERSION]

```
[[435   5]
 [ 53   7]]
              precision    recall  f1-score   support
           0      0.891     0.989     0.938       440
           1      0.583     0.117     0.194        60
    accuracy                          0.884       500
```

Reading the matrix: of 60 real subscribers, the model found 7 (TP) and missed 53 (FN). It raised 12 flags, and 7 of them were correct.

- Precision = 7 / (7 + 5) = 0.583
- Recall = 7 / (7 + 53) = 0.117
- F1 = 0.194

The accuracy of 0.884 from L05 is only a little better than always saying "no", which would score 440 / 500 = 0.88. For a bank that wants to find subscribers, this model at the 0.5 threshold is weak. L09 shows how to improve recall without retraining.

## Common Mistake
Learners often report accuracy alone, or read the wrong row of the classification report. The row for class 1 describes the positive class, which is usually the one the business cares about. Also, check which class scikit-learn treats as positive: by default it is the label `1`. If your target is text, such as "yes" and "no", set `pos_label="yes"` in the metric functions or convert the target to 0 and 1.

## Key Takeaways
1. With rare classes, a model can have high accuracy and still be useless; always compare with a `DummyClassifier` baseline.
2. The confusion matrix shows true and false positives and negatives; precision measures false alarms and recall measures missed cases.
3. F1 balances precision and recall, but the business cost of each mistake decides which matters most.

## Hands-on Exercise
**Task:** Build a confusion matrix for your Bank Marketing model and calculate precision, recall and F1 by hand, then check them with scikit-learn.
**Tools:** Google Colab (free), scikit-learn; your L05 pipeline. A calculator or a notebook cell for the hand calculation.
**Steps:**
1. Predict on the test set and print `confusion_matrix(y_test, y_pred)`.
2. Label each of the four numbers as TN, FP, FN or TP in a text cell.
3. Calculate precision, recall and F1 by hand from those counts.
4. Check your numbers with `precision_score`, `recall_score` and `f1_score`.
5. Fit a `DummyClassifier(strategy="most_frequent")` and compare its accuracy and recall with your model.
6. Write 2 sentences for a marketing manager: how many real subscribers the model finds, and how many flags are correct.
**What good looks like:** Hand calculations that match scikit-learn to 3 decimals, a baseline comparison, and 2 plain sentences with counts, not only percentages.
**Time:** about 25 minutes

## Review Flags
- [VERSION] `classification_report` layout and metric defaults depend on the installed version. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data; re-run in the current Colab version before recording.
