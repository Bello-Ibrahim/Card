# L08 Accuracy Is Not Enough: The Confusion Matrix | Presenter Script

Course: AI-12 · Video: 5 min · Words: 731

## Hook
Here is a fraud model that is ninety-nine percent accurate, and needs one line of code. It always says not fraud. It never catches a single fraud case. If accuracy can praise a model like that, we need better ways to measure.

## Explain
Accuracy is the share of all predictions that are correct. It works well when the classes are roughly balanced, and both kinds of mistake cost about the same. It fails when one class is rare, which is common in business: fraud, churn, loan default, or customers who buy.

The confusion matrix shows where the model is right and wrong. The rows are the actual classes, and the columns are the predicted classes. So we get true negatives, false positives, false negatives and true positives.

From these four counts come three key metrics. Precision asks, of all the cases the model flagged as yes, how many really were yes? High precision means few false alarms. Recall asks, of all the real yes cases, how many did the model find? High recall means few missed cases.

F one is one number that balances precision and recall. It is high only when both are reasonably high. Precision and recall usually pull against each other. Flag more cases, and you find more real ones, but you also raise more false alarms.

Which one matters more depends on the cost of each mistake, which you wrote down in lesson one. And a useful habit is to compare every model with a baseline that always predicts the most common class.

Think of a smoke alarm that never rings. It is correct on almost every day of the year, because most days have no fire. But it fails on the one day that matters. Recall asks, did it ring when there was a fire? Precision asks, when it rang, was there really a fire?

## Demonstrate
Aigerim Bekova is a data analyst at a payment company in Almaty, Kazakhstan. In her synthetic data, about one in a hundred card payments is fraud. First, she shows her team the lazy baseline.

This cell creates ten thousand synthetic payments, with only one percent fraud. It fits a baseline that always predicts the most common class, then prints its accuracy and its recall.

Accuracy is zero point nine nine. Recall is zero. The model found none of the one hundred fraud cases.

Now back to the term-deposit pipeline from lesson five, where about twelve percent of customers subscribe. This cell predicts the test set, then prints the confusion matrix and a full report of the metrics.

Read the matrix. Of sixty real subscribers, the model found seven, and missed fifty-three. It raised twelve flags, and seven of them were correct. The other four hundred and thirty-five customers were correctly left alone, and five were false alarms.

So precision is seven out of twelve, zero point five eight three. Recall is seven out of sixty, zero point one one seven. And F one is only zero point one nine four.

The accuracy is zero point eight eight four, as in lesson five. But always saying no would score four hundred and forty out of five hundred, which is zero point eight eight. For a bank that wants to find subscribers, this model is weak at the default setting.

A common mistake is to report accuracy alone, or to read the wrong row of the report. The row for class one describes the positive class, usually the one the business cares about. And if your target is text, such as yes and no, tell the metric which label is positive, or convert the target to one and zero.

## Recap
Let's recap. First, with rare classes, a model can have high accuracy and still be useless, so always compare with a baseline. Second, the confusion matrix shows true and false positives and negatives. Precision measures false alarms, and recall measures missed cases. Third, F one balances the two, but the business cost of each mistake decides which matters most.

## CTA
Now it is your turn. In the exercise below this video, you will build a confusion matrix for your own model, calculate precision, recall and F one by hand, and check them with scikit-learn. It takes about twenty-five minutes. In the next lesson, Probabilities, Thresholds and ROC Curves, you will find more subscribers without a new model. See you there.

## Thumbnail
Headline: 99% Accurate, 0% Useful
Image: Navy background, a 2×2 confusion matrix grid with one cell glowing amber, a large '99%' crossed through, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The first L08 cell (fraud baseline) runs on its own; the second cell needs pipe, X_test and y_test from L05. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] classification_report layout and metric defaults depend on the installed version. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data; re-run before recording and update every spoken count and score if they differ.
- Screen scenes 9 and 10 use the first L08 cell; scenes 11 to 14 use the second cell. Both are copied exactly from the content.md Worked Example. Content.md shows a shortened report; show the full report on screen and zoom in on the rows for class 1 and accuracy.
- Scene 13: show the hand calculation as an overlay: 7 / (7 + 5) = 0.583 and 7 / (7 + 53) = 0.117.
- Aigerim Bekova and the Almaty payment company are fictional; the fraud data is synthetic.
