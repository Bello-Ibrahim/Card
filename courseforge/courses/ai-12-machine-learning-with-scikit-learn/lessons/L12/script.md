# L12 Ensembles: Random Forests and Gradient Boosting | Presenter Script

Course: AI-12 · Video: 5 min · Words: 688

## Hook
One decision tree is easy to understand, but unstable. Change a few rows, and it can grow very differently. What if you trained hundreds of trees and combined them? That simple idea is behind two of the strongest model families for business data.

## Explain
An ensemble combines many models into one prediction. The first approach is a random forest. It trains many deep trees, each on a random sample of the rows, and each looking at a random subset of features at every split. So each tree makes different mistakes.

For regression, the forest averages the trees' predictions. For classification, it combines their votes. Averaging cancels out much of each tree's noise, so a forest overfits much less than one deep tree. The trees are independent, so they can train in parallel.

The second approach is gradient boosting. It trains small trees one after another. Each new tree tries to correct the errors the earlier trees still make. It is often the most accurate model on tables of data, but it has more settings, and it can overfit if it runs too long.

scikit-learn has fast versions, called histogram gradient boosting. They group values into bins, handle missing values without an imputer, and can stop early. Neither ensemble needs scaled features, because both are built from trees. Start with a simple baseline, try a random forest next, then boosting when you want the best accuracy.

Ask one person to guess the number of beans in a jar, and the guess may be far off. Ask two hundred people and average their guesses, and the average is often closer. A random forest is that crowd. Boosting is a team where each new member fixes what the team got wrong so far.

## Demonstrate
Amara Diallo runs analytics for a scooter-rental start-up in Dakar, Senegal. She has the same kind of hourly demand problem as lesson eleven, and wants to know if ensembles are worth their extra complexity.

We continue in the bike notebook, with the training data ready. This cell creates five folds, then cross-validates three models on the same folds: linear regression, a forest of two hundred trees, and gradient boosting. For each, it prints the mean RMSE and the spread.

Two details. scikit-learn scores follow the rule that higher is better, so errors come back as negative numbers. The minus sign at the start turns them into normal RMSE values. And we use plain folds, not stratified ones, because the target is a number.

The results. Linear regression has an RMSE of one hundred and eighty-two point three, with a spread of two point eight. The forest scores one hundred and twenty-eight point seven, spread one point six. Boosting scores one hundred and twenty-two point six, spread one point eight.

Both ensembles cut the error by more than fifty bikes per hour, far more than the spread. Boosting is about six bikes per hour better than the forest, also more than the spread. So Amara picks gradient boosting. But all three models still see only temperature, humidity and hour.

A common mistake is to assume the most complex model always wins, and skip the baseline. On small or noisy data, a simple linear model can match an untuned ensemble. Always compare with a baseline on the same folds. And do not forget the minus sign on error scores.

## Recap
Let's recap. First, a random forest averages many different trees, which reduces overfitting, so it is a strong, low-effort second model. Second, gradient boosting adds trees one by one to correct earlier errors, and the histogram versions are fast and handle missing values. Third, compare ensembles with a simple baseline on the same folds, and remember that error scores are negative in scikit-learn.

## CTA
Now it is your turn. In the exercise below this video, you will compare the three models on the bike data, add a second error metric and training times, and choose one. It takes about thirty minutes. In the next lesson, Feature Engineering That Helps, we keep the model the same and change what it sees. See you there.

## Thumbnail
Headline: Many Trees Beat One
Image: Navy background, a small forest of stylised trees feeding arrows into one averaged prediction, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L11 setup cell (content.md L11 Worked Example, first code block: synthetic hourly bike data) and then the L11 model cell (second code block: features, the split with random_state=0, and the two models). The L12 cell uses X_train, y_train and LinearRegression from those cells. Do not run the L05 bank cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] Estimator names, import paths and defaults for RandomForestRegressor and HistGradientBoostingRegressor, and scorer names such as neg_root_mean_squared_error, depend on the installed version. Outputs were recorded with scikit-learn 1.9.1 and Python 3.11 on synthetic data; re-run before recording and update the spoken RMSE values and spreads if they differ.
- Content.md says boosting 'trained faster in this run'; the voiceover leaves out training time because it depends on Colab hardware.
- Screen scenes 8 to 11 use one cell copied exactly from the content.md Worked Example. The forest with 200 trees can take several seconds; cut the wait in editing.
- Amara Diallo and the Dakar scooter-rental start-up are fictional; the data is synthetic.
