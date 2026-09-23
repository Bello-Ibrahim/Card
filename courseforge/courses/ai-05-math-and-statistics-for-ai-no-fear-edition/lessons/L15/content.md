# L15 Classification Metrics: Confusion Matrix, Precision and Recall

Course: AI-05 · Module: M4 · Objectives: O1, O5 · Video: 5 min

## Hook
A fraud detector is 99% accurate. Impressive? Now imagine a "detector" that never flags anything at all. In the hypothetical example in this lesson, it is also 99% accurate. One number can hide a lot, and this lesson shows you how to see what it hides.

## Explanation
A **classifier** predicts a category, such as "fraud" or "not fraud". We call the class we are looking for the **positive** class (here, fraud) and the other the **negative** class. "Positive" does not mean "good"; it means "the thing we are searching for".

Every prediction falls into one of four groups:

- **True positive (TP):** predicted fraud, and it was fraud.
- **False positive (FP):** predicted fraud, but it was honest. A false alarm.
- **False negative (FN):** predicted honest, but it was fraud. A miss.
- **True negative (TN):** predicted honest, and it was honest.

A **confusion matrix** is a 2 × 2 table of these four counts. Rows show the truth and columns show the prediction. It shows exactly where the model is "confused".

Three metrics come from it:

- **Accuracy** = (TP + TN) ÷ all predictions. In words: the fraction of all predictions that were correct.
- **Precision** = TP ÷ (TP + FP). In words: of everything the model flagged, what fraction was really positive? This is the Bayes question from L08.
- **Recall** = TP ÷ (TP + FN). In words: of all the real positives, what fraction did the model find?

Accuracy is misleading when one class is rare, which is called **class imbalance**. If 99% of cases are negative, a model can reach 99% accuracy by always saying "negative", and find nothing.

Precision and recall usually pull against each other. Flag more cases and you catch more fraud (higher recall) but raise more false alarms (lower precision). Which one matters more depends on the **cost** of each mistake. Missing fraud may cost a lot of money; a false alarm may only annoy a customer. In other tasks, the balance is the opposite.

**Analogy:** Think of fishing with a net. Recall asks, "Of all the fish in the lake, how many did my net catch?" Precision asks, "Of everything in my net, how much is fish and how much is old boots?" A huge net catches many fish but also many boots. A small, careful net has few boots but misses many fish.

## Worked Example
Farhana is a hypothetical risk analyst at a mobile payments company in Dhaka, Bangladesh. She tests a new fraud detector on 10,000 transactions. All numbers are invented for teaching: 100 transactions are fraud and 9,900 are honest.

| | Predicted fraud | Predicted honest |
|---|---|---|
| **Actually fraud** | TP = 20 | FN = 80 |
| **Actually honest** | FP = 20 | TN = 9,880 |

**Hand calculation:**

- Accuracy = (20 + 9,880) ÷ 10,000 = 9,900 ÷ 10,000 = 0.99, or 99%.
- Precision = 20 ÷ (20 + 20) = 0.5. Half of the alerts are real fraud.
- Recall = 20 ÷ (20 + 80) = 0.2. The detector finds only 20% of the fraud.

Now compare a "lazy" model that always predicts "honest": TP = 0, FN = 100, FP = 0, TN = 9,900. Its accuracy is also 9,900 ÷ 10,000 = 99%, but its recall is 0. The 99% accuracy hides that the real detector misses 80 of 100 frauds.

**Code:**

```python
tp, fp, fn, tn = 20, 20, 80, 9880
print((tp + tn) / (tp + fp + fn + tn))  # accuracy 0.99
print(tp / (tp + fp))                   # precision 0.5
print(tp / (tp + fn))                   # recall 0.2
```

Farhana reports recall first, because each missed fraud is costly, and asks the team to improve it while watching that precision does not fall too far.

## Common Mistake
Learners often judge a classifier by accuracy alone. With imbalanced data, always build the confusion matrix first and compare with the "always predict the common class" baseline. A second mistake is mixing up precision and recall. Remember what each one divides by: precision divides by everything **predicted** positive; recall divides by everything **actually** positive.

## Key Takeaways
1. A confusion matrix counts true positives, false positives, false negatives and true negatives.
2. Precision is TP ÷ (TP + FP), "how many alerts are real"; recall is TP ÷ (TP + FN), "how many real cases we found".
3. Accuracy can hide poor performance when one class is rare, so compare with an "always the common class" baseline and choose metrics by the cost of each mistake.

## Hands-on Exercise
**Task:** Build a confusion matrix from 20 hypothetical predictions, calculate accuracy, precision and recall with NumPy, and explain which metric matters most for this case.
**Tools:** Pen and paper; Google Colab with NumPy.
**Steps:**
1. Use these hypothetical labels, where 1 = fraud and 0 = honest:
   `y_true = [1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0]`
   `y_pred = [1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0]`
2. By hand, compare each pair and count TP, FP, FN and TN. Draw the 2 × 2 table.
3. In Colab, turn both lists into NumPy arrays and count each group, for example `tp = np.sum((y_true == 1) & (y_pred == 1))`.
4. Calculate accuracy, precision and recall.
5. Calculate the accuracy of a model that always predicts 0.
6. Write three sentences: which metric matters most for fraud, and why.
**What good looks like:** TP = 3, FP = 1, FN = 2, TN = 14. Accuracy 0.85, precision 0.75 and recall 0.6. The "always 0" model scores 0.75 accuracy. Your explanation connects recall to the cost of missed fraud.
**Time:** about 25 minutes

## Review Flags
- All fraud rates and counts are hypothetical on purpose and must not be presented as real statistics about mobile payments in Bangladesh or elsewhere (carried from the curriculum flags).
- No review tags are needed otherwise: the code uses only basic Python and NumPy, and every output was recalculated.
