# L08 Measuring Classification Quality

Course: AI-19 · Module: M2 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
A model reports 86% accuracy. That sounds good, until you learn that it misses most of the glass bottles it was built to find. One number can hide the most important failure. In this lesson you learn to see what the accuracy number hides.

## Explanation
**Accuracy** is the share of all predictions that are correct. It is a useful first number, but it treats every image the same. When one class is much larger than the others, which is called **unbalanced data**, a model can reach high accuracy by doing well on the large class and badly on the small ones.

A **confusion matrix** shows every combination of true class and predicted class. Rows are the true classes and columns are the predicted classes (this is the scikit-learn convention). The diagonal holds correct predictions. Every cell off the diagonal is a specific kind of mistake, such as "glass predicted as plastic".

For each class you can then calculate two numbers:

- **Precision:** of all images the model *called* this class, how many really were this class? Low precision means false alarms.
- **Recall:** of all images that *really were* this class, how many did the model find? Low recall means missed cases.

Which one matters more depends on the cost of each mistake. If a missed case is expensive, such as a diseased leaf that spreads to a whole field, focus on recall. If a false alarm is expensive, such as stopping a production line for no reason, focus on precision. The **F1 score** combines both into one number per class. The **macro average** gives every class the same weight, so small classes are not hidden.

Numbers tell you *which* classes fail. To learn *why*, open the wrong images and look at them. Sort them into groups: poor lighting, unusual angle, blur, object partly hidden, busy background, a label error in the dataset, or two classes that really look alike. The group with the most images tells you what to fix first.

**Analogy:** Accuracy is like a school's overall exam pass rate. A school with 90% passes may still fail almost every student in one small class. The confusion matrix is the report for each class and each subject, and looking at the wrong images is talking to the students who failed.

## Worked Example
Sipho Dlamini builds a recycling sorter for a waste company in Durban, South Africa. His model classifies items on a belt as plastic, glass or metal. His test set has 80 plastic, 15 glass and 5 metal items, which matches what arrives on the belt.

```python
from sklearn.metrics import confusion_matrix, classification_report

labels = ["plastic", "glass", "metal"]
y_true = ["plastic"] * 80 + ["glass"] * 15 + ["metal"] * 5
y_pred = (["plastic"] * 78 + ["glass"] * 2 +
          ["plastic"] * 9 + ["glass"] * 6 +
          ["plastic"] * 3 + ["metal"] * 2)

print(confusion_matrix(y_true, y_pred, labels=labels))
print(classification_report(y_true, y_pred, labels=labels, digits=2))
```

Output (shortened; from these hand-made example labels):

```text
[[78  2  0]
 [ 9  6  0]
 [ 3  0  2]]
              precision    recall  f1-score   support
     plastic       0.87      0.97      0.92        80
       glass       0.75      0.40      0.52        15
       metal       1.00      0.40      0.57         5
    accuracy                           0.86       100
   macro avg       0.87      0.59      0.67       100
```

Accuracy is 0.86, but recall for glass and metal is only 0.40. The matrix shows why: 9 glass items and 3 metal items were predicted as plastic. The model has learned to say "plastic" when it is unsure, because plastic dominates the training data.

Sipho opens the 9 wrong glass images. Seven show clear glass bottles under strong top lighting, where the glass looks shiny like plastic. He plans two fixes: collect more glass images under the belt's real lighting, and use class weights during training so that mistakes on small classes cost more.

**On screen (presenter steps):**
1. Load the saved model from L07 in Colab and predict the test split.
2. Print the confusion matrix and the classification report.
3. Plot the matrix with `ConfusionMatrixDisplay.from_predictions` from scikit-learn.
4. Filter the test images where the true and predicted class differ, and show 8 of them in a grid with both labels.
5. Group the wrong images by likely cause and count each group.

## Common Mistake
Many learners balance the *test* set by removing images from the large class, so accuracy "looks fair". The test set should reflect the data the model will really meet, otherwise your numbers promise a performance you will not get. Instead, keep a realistic test set and report per-class precision and recall and the macro average. Balance the *training* data, or use class weights, if the small classes matter.

## Key Takeaways
1. Accuracy can hide poor results on small classes when data is unbalanced; always check per-class results.
2. The confusion matrix shows which classes are mixed up; precision counts false alarms and recall counts missed cases.
3. Look at the wrong images and group them by cause, such as lighting or angle, to decide what to fix first.

## Hands-on Exercise
**Task:** Build a confusion matrix for your fine-tuned model, calculate precision and recall per class, and write 3 sentences on the most common mistake and how you could fix it.
**Tools:** Google Colab; your saved model from L07; scikit-learn and Matplotlib (pre-installed in Colab [VERSION]).
**Steps:**
1. Load your fine-tuned model and predict every image in the test split.
2. Print the confusion matrix and plot it with class names on both axes.
3. Print the classification report with precision, recall and F1 for each class.
4. Find the largest cell off the diagonal and name the mistake, for example "bean rust predicted as angular leaf spot".
5. Display all images with that mistake and group them by likely cause.
6. Write 3 sentences: the most common mistake, the likely cause, and one realistic fix.
**What good looks like:** A labelled confusion matrix, a per-class report, a grid of wrong images and 3 sentences that link the numbers to what you saw in the images.
**Time:** about 30 minutes

## Review Flags
- [VERSION] scikit-learn functions (`confusion_matrix`, `classification_report`, `ConfusionMatrixDisplay.from_predictions`) and their availability in Colab. The worked example code was run with scikit-learn on the hand-made labels shown; its numbers are an illustration, not a benchmark.
