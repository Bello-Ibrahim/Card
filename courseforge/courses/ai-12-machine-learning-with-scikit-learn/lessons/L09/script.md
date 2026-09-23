# L09 Probabilities, Thresholds and ROC Curves | Presenter Script

Course: AI-12 · Video: 5 min · Words: 711

## Hook
In the last lesson, the model found only seven of sixty subscribers. You do not need a new model to do better. The model already gives a probability for every customer. The cut-off of zero point five was simply a default.

## Explain
The model's probability of yes becomes a decision at a threshold. By default, that threshold is zero point five, but you can choose any threshold yourself. A lower threshold flags more cases. Recall goes up, and precision usually goes down. A higher threshold does the opposite.

Two curves show every threshold at once. The ROC curve plots the share of real positives found against the share of negatives wrongly flagged. ROC AUC sums it up in one number. It is the chance that the model gives a random positive case a higher probability than a random negative case.

Zero point five is random guessing, and one is perfect ranking. ROC AUC does not depend on the threshold, so it measures how well the model ranks cases. The precision-recall curve plots precision against recall. With rare positive cases, it is often more informative.

So how do you pick the threshold? Put a cost on each kind of mistake, and choose the threshold with the lowest total cost. Choose it on the training data, with cross-validated predictions, not on the test set.

Think of the height of a net on a fishing boat. Lower the net, and you catch more fish, but also more weeds. Raise it, and some fish escape. The right height depends on how much a fish is worth, compared with the time spent sorting weeds.

## Demonstrate
Dr. Wanjiru Kamau runs a community clinic in Nairobi. Her team uses a risk score to decide whom to call for a free screening. Missing a patient who needs care is much worse than an extra phone call, so she prefers a low threshold.

To practise without any patient data, her analyst uses the term-deposit model from lesson five. It has the same shape of problem.

This cell takes the model's probabilities for the test customers and prints the ROC AUC. Then it tries three thresholds, and for each one it prints precision and recall.

ROC AUC is zero point seven five two. At zero point five, precision is zero point five eight three and recall is zero point one one seven, the same as last lesson. At zero point three, precision falls to zero point three nine six, and recall rises to zero point three one seven.

At zero point one five, the model finds two thirds of subscribers, a recall of zero point six six seven. But only about twenty-nine percent of flags are correct, a precision of zero point two nine two.

Now we add costs. An unneeded call costs one unit, and a missed case costs eight. This cell gets cross-validated probabilities on the training data only, then adds up the cost of each mistake for thresholds from zero point zero five to zero point nine.

The best threshold is zero point one. It costs eight hundred and thirteen units, against one thousand, three hundred and eighty-one at the default zero point five. With these costs, a low threshold is clearly better.

A common mistake is to think a better threshold makes a better model. It does not. The threshold changes the decisions, not the model's ability to rank cases. ROC AUC stays at zero point seven five two, whatever threshold you pick. And never tune the threshold on the test set.

## Recap
Let's recap. First, the model gives probabilities, and the threshold turns them into decisions, trading precision against recall. Second, ROC AUC measures how well the model ranks cases, whatever the threshold, and precision-recall curves are more useful for rare positives. Third, choose the threshold from the business cost of each mistake, using cross-validated predictions on training data.

## CTA
Now it is your turn. In the exercise below this video, you will plot total cost against threshold for two different cost pairs, pick the best threshold, and apply it once to the test set. It takes about thirty minutes. In the next lesson, Cross-Validation for Reliable Scores, you will learn how much a score can move. See you there.

## Thumbnail
Headline: Move the Cut-off
Image: Navy background, a horizontal probability slider with the marker moving from 0.5 down to 0.15, a fishing net icon, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The second L09 cell also needs numpy, imported in the first L09 cell, so run the two L09 cells in order. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] RocCurveDisplay, PrecisionRecallDisplay and TunedThresholdClassifierCV depend on the installed version; the voiceover mentions only the display tools in general terms. Outputs were recorded with scikit-learn 1.9.1, NumPy 2.4 and Python 3.11 on synthetic data; re-run before recording and update every spoken value if it differs.
- Screen scenes 9 to 11 use the first L09 cell; scenes 12 and 13 use the second cell. Both are copied exactly from the content.md Worked Example.
- The clinic case is hypothetical on purpose (curriculum flag), to avoid unverified claims about real organisations; no patient data is used. Stock footage must not show a real clinic name, logo or identifiable patients.
- Dr. Wanjiru Kamau is fictional. Speak thresholds as 'zero point one five' and costs as 'eight hundred and thirteen' and 'one thousand, three hundred and eighty-one'.
