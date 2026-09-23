# L14 Hyperparameter Tuning with Grid and Random Search | Presenter Script

Course: AI-12 · Video: 5 min · Words: 711

## Hook
Every model so far used default settings, or settings we picked by hand. Defaults are a reasonable start, not the best choice for your data. Today, scikit-learn searches for better settings, and you will see that tuning helps, but does not work miracles.

## Explain
Hyperparameters are settings you choose before training, such as the maximum depth, the minimum leaf size, or the number of trees. The model does not learn them from data. Tuning means trying many combinations, and keeping the one with the best cross-validated score.

Grid search tries every combination in a grid. Three values for each of four settings means eighty-one combinations. With five folds, that is four hundred and five fits. Grids grow very quickly. Random search tries a fixed number of random combinations, and often finds settings nearly as good, in much less time.

Both work on a whole pipeline, so preprocessing is refitted inside every fold. To reach a setting inside a pipeline, you use the step name, then two underscores, then the setting name. After the search, you get the best settings, their mean score, and the best pipeline, refitted on all the training data.

The rule from lesson three still holds. The test set stays untouched until the very end. The search uses only training data, and you look at the test score once, after all choices are made.

Tuning is like adjusting a new sewing machine: stitch length, thread tension and speed. You could test every combination on a practice cloth, or test twenty random ones and keep the best. Either way, you practise on scrap cloth, not on the customer's dress. The test set is the customer's dress.

## Demonstrate
Youssef Haddad is a data scientist at a bank in Beirut, Lebanon. His random forest for term-deposit subscriptions uses default settings, and he wants to know whether tuning helps.

We continue in the bank notebook. This cell puts a random forest into the pipeline, defines ranges for four settings, and runs a random search of twenty combinations with five folds, scored by ROC AUC. Then it scores the untuned and tuned pipelines on the test set, once.

The search chose two hundred trees, the square-root feature setting, a maximum depth of twelve, and a minimum of forty customers per leaf. Its mean cross-validated ROC AUC is zero point seven six nine.

Forty customers per leaf is the key choice. It stops the trees from memorising individual people. That fits what you saw in lesson seven. The default forest was too flexible for fifteen hundred noisy training rows.

On the test set, ROC AUC rose from zero point seven zero one to zero point seven three seven. But the logistic regression pipeline from lesson nine scored zero point seven five two on the same test set. Tuning improved the forest, yet the simpler model is still slightly ahead.

Youssef's conclusion: tuning helped the forest, but for this data, the logistic model is simpler, easier to explain, and at least as good. He will carry it forward. That is a good result. The search saved him from assuming that a complex model is better.

A common mistake is to tune on the test set, or to search before splitting. Then the best settings have seen the test rows, and the final score is too optimistic. Another is a huge grid that runs for hours. Start with a random search over wide ranges, then, if needed, a small grid around the best values.

## Recap
Let's recap. First, hyperparameters are settings you choose before training, and tuning searches for the combination with the best cross-validated score. Second, random search is usually more efficient than grid search, and step name plus two underscores reaches a setting inside a pipeline. Third, search on training data only, check the test set once, and compare the tuned model with a simple baseline.

## CTA
Now it is your turn. In the exercise below this video, you will tune a random forest with random search, score it once on the test set, and compare it with the untuned model and your best simple model. It takes about thirty-five minutes. In the next lesson, Which Features Matter? Interpreting Models, you will explain what drives your model. See you there.

## Thumbnail
Headline: Tuning Helps, No Miracles
Image: Navy background, a grid of small dots with a few randomly highlighted in teal and one marked as best, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L05 setup cell (content.md L05 Worked Example, first code block: synthetic bank data and the stratified split) and then the L05 pipeline cell (second code block: prep, pipe, pipe.fit). The L14 cell uses prep, Pipeline, X_train, y_train, X_test and y_test from those cells. Run them off camera or show them already executed at the top of the notebook; do not run the L03 or L11 cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] GridSearchCV and RandomizedSearchCV arguments, the order of keys in best_params_, and search run time in Colab depend on the installed version and hardware. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data; re-run before recording and update the spoken settings and scores if they differ.
- Screen scenes 9 to 13 use one cell copied exactly from the content.md Worked Example. The search takes about half a minute; cut the wait in editing.
- Scene 12 compares with the logistic pipeline's test ROC AUC of 0.752 from L09; show it as an overlay, since it is not printed by this cell.
- Youssef Haddad and the Beirut bank are fictional; the data is synthetic.
