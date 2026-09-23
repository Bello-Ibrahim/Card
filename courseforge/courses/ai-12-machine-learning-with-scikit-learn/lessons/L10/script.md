# L10 Cross-Validation for Reliable Scores | Presenter Script

Course: AI-12 · Video: 5 min · Words: 698

## Hook
In lesson three, you changed only the random seed of the split, and the test score moved. If one split can be lucky or unlucky, how can you trust a comparison between two models that differ by one hundredth?

## Explain
Cross-validation gives you a score, and a measure of how much it moves. In k-fold cross-validation, the training data is split into k equal parts, called folds. The model is trained k times. Each time, one fold is held out for scoring, and the others are used for training.

You get k scores, one per fold, and every row is used for scoring exactly once. For classification, use stratified folds, which keep the class balance the same in every fold. This is important when one class is rare.

Always report two numbers: the mean score, and the standard deviation, which shows the spread. If model A scores zero point seven seven, and model B scores zero point seven six, both with a spread of zero point zero five, the difference is smaller than the normal variation. You cannot say A is better.

Cross-validation runs on the training set only. The test set is still kept for one final check. And because you pass a whole pipeline, the preprocessing is refitted inside every fold, which keeps each fold free of leakage.

Judging a student by one exam can be unfair. The questions may happen to suit them, or not. Five short exams on different topics give a better picture, and the gap between the best and worst exam shows how consistent the student is.

## Demonstrate
Lars Eriksson is an analyst at an energy company in Sweden. He is testing a workflow for predicting which customers will accept a new contract. He practises on the term-deposit data from lesson five.

This cell sets up five stratified folds. Then it builds three pipelines with the same preprocessing and a different model each: logistic regression, a decision tree, and k-nearest neighbours. For each one, it prints the mean ROC AUC across the folds, and the spread.

Logistic regression has the highest mean, zero point seven seven four, with a spread of zero point zero four eight. The tree scores zero point six eight two, with a spread of zero point zero three four. Its lead over the tree, about zero point zero nine, is larger than the spread. That is a real difference.

k-nearest neighbours scores zero point seven three three, with a spread of zero point zero four seven. The lead of logistic regression here is about zero point zero four, smaller than one standard deviation. So Lars writes, probably better, not certain.

Next, this cell shows the individual fold scores for the logistic pipeline, for two metrics at once: ROC AUC and recall.

ROC AUC ranges from zero point seven one eight to zero point eight four three across the folds. A single split could have reported either end. And recall at the default threshold is low in every fold, between zero point zero two seven and zero point one zero eight, which matches lesson eight.

A common mistake is to cross-validate on the full dataset, including the test rows, and then report a test score on those same rows. Another is to preprocess first, and cross-validate only the model. Split off the test set first, and cross-validate the whole pipeline on the training set.

## Recap
Let's recap. First, k-fold cross-validation trains and scores a model k times, so every training row is scored once, and you should use stratified folds for classification. Second, report the mean and the standard deviation, because differences smaller than the spread are not reliable. Third, cross-validate the whole pipeline on the training set only, and keep the test set for the final check.

## CTA
Now it is your turn. In the exercise below this video, you will cross-validate three classifiers, put the mean and spread of each in a small table, and decide which model to carry forward. It takes about twenty-five minutes. In the next lesson, Regression Models and Metrics, we move from yes or no to predicting numbers. See you there.

## Thumbnail
Headline: Five Exams, Not One
Image: Navy background, a data bar split into five coloured folds with one fold highlighted in turn, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The first L10 cell uses prep, Pipeline and LogisticRegression from those cells; the second L10 cell uses cv from the first, so run them in order. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] cross_validate result keys (such as test_roc_auc) and scoring names depend on the installed version. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data; re-run before recording and update every spoken mean, spread and fold score if they differ.
- Screen scenes 8 to 10 use the first L10 cell; scenes 11 and 12 use the second cell. Both are copied exactly from the content.md Worked Example.
- Speak 'mean' and 'standard deviation' in words; the screen shows mean= and std=.
- Lars Eriksson and the Swedish energy company are fictional; the data is synthetic.
