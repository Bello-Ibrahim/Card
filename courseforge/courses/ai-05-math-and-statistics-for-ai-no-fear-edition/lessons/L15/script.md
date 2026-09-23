# L15 Classification Metrics: Confusion Matrix, Precision and Recall | Presenter Script

Course: AI-05 · Video: 5 min · Words: 654

## Hook
A fraud detector is ninety-nine percent accurate. Impressive? Now imagine a detector that never flags anything at all. In our hypothetical example, it is also ninety-nine percent accurate. One number can hide a lot.

## Explain
This is the final module, and you have come a long way. This lesson shows you how to see what one number hides. A classifier predicts a category, like fraud or not fraud. The class we are looking for is called positive. Positive does not mean good. It means the thing we are searching for.

Every prediction falls into one of four groups. A true positive: predicted fraud, and it was fraud. A false positive: predicted fraud, but it was honest, a false alarm. A false negative: predicted honest, but it was fraud, a miss. And a true negative: predicted honest, and it was honest. Together they make a two by two table, the confusion matrix.

Three metrics come from it. Accuracy is the fraction of all predictions that were correct. Precision asks: of everything the model flagged, what fraction was really positive? That is the Bayes question from lesson eight. Recall asks: of all the real positives, what fraction did the model find?

Accuracy misleads when one class is rare. This is called class imbalance. And precision and recall usually pull against each other. Flag more cases, and you catch more fraud, but raise more false alarms. Which one matters more depends on the cost of each mistake.

Think of fishing with a net. Recall asks: of all the fish in the lake, how many did my net catch? Precision asks: of everything in my net, how much is fish, and how much is old boots? A huge net catches many fish, but also many boots.

## Demonstrate
Farhana is a risk analyst at a mobile payments company in Dhaka, Bangladesh. She tests a new fraud detector on ten thousand transactions. All numbers are invented for teaching. One hundred transactions are fraud, and nine thousand nine hundred are honest.

Here is her confusion matrix. Twenty true positives. Eighty frauds were missed. Twenty false alarms. And nine thousand eight hundred and eighty true negatives. Accuracy is twenty plus nine thousand eight hundred and eighty, divided by ten thousand. That is zero point nine nine, or ninety-nine percent.

Precision is twenty divided by twenty plus twenty, which is zero point five. Half of the alerts are real fraud. Recall is twenty divided by twenty plus eighty, which is zero point two. The detector finds only twenty percent of the fraud.

Now compare a lazy model that always predicts honest. It has zero true positives, one hundred misses, zero false alarms, and nine thousand nine hundred true negatives. Its accuracy is also ninety-nine percent, but its recall is zero. The ninety-nine percent hides that the real detector misses eighty of one hundred frauds.

Farhana reports recall first, because each missed fraud is costly. She asks the team to improve it, while watching that precision does not fall too far.

A common mistake is to judge a classifier by accuracy alone. With imbalanced data, build the confusion matrix first, and compare with an always predict the common class baseline. And remember: precision divides by everything predicted positive. Recall divides by everything actually positive.

## Recap
Let's recap. First, a confusion matrix counts true positives, false positives, false negatives and true negatives. Second, precision tells you how many alerts are real, and recall tells you how many real cases you found. Third, accuracy can hide poor performance when one class is rare, so compare with a common-class baseline and choose metrics by the cost of each mistake.

## CTA
Your turn. In the exercise, you build a confusion matrix from twenty hypothetical predictions, calculate the three metrics in NumPy, and decide which one matters most for fraud. It takes about twenty-five minutes. Next: Overfitting, Train and Test Splits, and Baselines. See you there.

## Thumbnail
Headline: 99% Accurate, Still Useless?
Image: Navy background, a 2 × 2 grid with one tiny teal cell and one huge grey cell, headline in teal Inter Bold.

## Production Notes
- All fraud rates and counts are hypothetical on purpose and must not be presented as real statistics about mobile payments in Bangladesh or elsewhere. Keep the label 'hypothetical numbers' on scenes 8 to 11.
- Farhana and the Dhaka mobile payments company are fictional. Stock footage must not show a real payments app, brand or readable account details.
- Not a screen demo lesson: code appears only on a code slide.
