# L15 Which Features Matter? Interpreting Models | Presenter Script

Course: AI-12 · Video: 5 min · Words: 697

## Hook
A sales manager asks, your model says who will subscribe, so why those people? If your only answer is the algorithm decided, she will not trust it, and she should not. Today you learn three ways to see which features drive a model.

## Explain
The first way is coefficients, which you met in lesson six. For linear and logistic models, they show the direction and size of each feature's effect, if the features are scaled. They are simple, but they only exist for linear models.

The second way is tree feature importances, in random forests and many tree models. They measure how much each feature improved the splits while the trees were built. They are quick, but they have some known limits, so check them against the third way.

The third way is permutation importance, and it works with any model, including a whole pipeline. It takes one column at a time, shuffles its values randomly, and measures how much the score drops. If the score falls a lot, the model relies on that column. If it barely moves, the model does not need it.

Three limits apply to all of these. Importance is not cause. Changing a feature does not necessarily change the outcome. Correlated features share importance, so if two columns carry the same information, both may look unimportant. And importance describes this model on this data, not the world in general.

Permutation importance is like muting the instruments in a band, one at a time. If the song falls apart without the drums, the drums matter. But if two guitars play the same part, muting either one changes little, and you might wrongly decide that neither guitar matters.

## Demonstrate
Tan Mei Lin is a data scientist at a bank in Kuala Lumpur, Malaysia. She must explain the term-deposit model to the sales team. She continues in the bank notebook, where the logistic regression pipeline is fitted.

This cell runs permutation importance on the test set, scored by ROC AUC. It shuffles each original column twenty times, and records the average drop and its spread. Then it prints the columns sorted from most to least important.

Shuffling the number of calls lowers ROC AUC by about zero point zero seven eight on average. That is the largest drop. Age follows closely at zero point zero six six, and job at zero point zero six five.

Contact type drops the score by zero point zero three zero. Balance has a mean drop of zero point zero one one, with a spread of zero point zero one two. The spread is larger than the mean, so its effect cannot be separated from zero with this test set.

Then Mei Lin writes three sentences for the sales manager. One. The number of times we have already called a customer in this campaign is the strongest signal. Customers called many times are less likely to subscribe.

Two. Age and job type matter almost as much. Older and retired customers are more likely to say yes. Three. Account balance adds very little once we know the other information. These are patterns in past data, not proof that calling less will make people subscribe.

The most common mistake is to present importance as cause, for example, reduce calls and subscriptions will rise. The model only shows that customers with many calls subscribed less in the past. Perhaps the bank kept calling people who were never interested.

## Recap
Let's recap. First, coefficients, tree importances and permutation importance each show which features a model relies on, with different strengths and limits. Second, permutation importance works with any pipeline, and should be run on held-out data, with its spread reported. Third, importance is not cause, so say is linked with, and watch for correlated features that share importance.

## CTA
Now it is your turn. In the exercise below this video, you will calculate permutation importance for your best model, chart it with error bars, and write three plain sentences for a sales manager. It takes about thirty minutes, and it prepares you for the capstone report. In the next lesson, Fairness, Limits and Model Risk, we check who the model serves less well. See you there.

## Thumbnail
Headline: Why Those Customers?
Image: Navy background, a horizontal bar chart of feature importance with error bars (calls, age, job, contact, balance), a muted speaker icon, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The L15 cell uses the fitted logistic pipe, X_test and y_test. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERIFY] Content.md says impurity-based tree importances are computed on training data and favour numeric features with many distinct values. The voiceover only says tree importances have 'known limits'; check the claim against the current scikit-learn user guide before adding detail.
- [VERSION] sklearn.inspection.permutation_importance arguments and result attributes depend on the installed version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on synthetic data; re-run before recording and update the spoken importances if they differ.
- Screen scenes 8 to 12 use one cell copied exactly from the content.md Worked Example. With 20 repeats the cell takes a few seconds.
- Tan Mei Lin and the Kuala Lumpur bank are fictional; the data is synthetic.
