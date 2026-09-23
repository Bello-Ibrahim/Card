# L11 Regression Models and Metrics | Presenter Script

Course: AI-12 · Video: 5 min · Words: 715

## Hook
A bike-sharing manager does not ask, will people rent bikes? She asks, how many bikes will we need at eight tomorrow morning? When the answer is a number, you need regression, and you need metrics that speak in bikes.

## Explain
So far, our models answered yes or no questions. Regression models predict a number. The workflow is exactly the same: create, fit, predict. Two model families are a good start.

Linear regression fits a weighted sum of the features. It is fast and easy to explain, but it can only draw straight-line relationships. A decision tree for regression splits the data, and each leaf predicts the average of its training rows. It can follow curves and peaks, but it overfits if it grows too deep.

Now three metrics, in words. MAE, the mean absolute error, is the average size of the error, in the target's own units. For example, on average our prediction is ninety bikes away from the real number. RMSE, the root mean squared error, is also in the target's units, but it punishes large errors more.

If RMSE is much larger than MAE, the model makes some big misses. R squared shows how much of the variation in the target the model explains, compared with always predicting the average. One is perfect, and zero is no better than the average. It has no units, so it is harder to use with a manager.

MAE is like the average number of minutes a bus is late. RMSE is the same idea, but a bus that is forty minutes late counts much more than four buses that are ten minutes late. Passengers remember the very late bus, and RMSE does too.

## Demonstrate
Park Ji-woo is an analyst for a city bike-sharing scheme. The exercise uses a public bike-sharing dataset, but the demo uses a synthetic year of hourly data with a similar shape, so the results are repeatable.

In a fresh notebook, we run the setup cell. It creates one year of hourly data, with temperature, humidity, and a morning and evening rush on workdays. That is eight thousand, seven hundred and sixty hours, with an average of about two hundred and forty-three rentals per hour.

The model cell uses three features: temperature, humidity, and the hour of the day. It keeps twenty percent of the hours for testing. Then it trains a linear model and a tree with a depth of eight, and prints MAE, RMSE and R squared for each.

The linear model has an MAE of one hundred and forty-one point seven, an RMSE of one hundred and eighty-six point four, and R squared of zero point two six eight. In business terms, it is wrong by about one hundred and forty-two bikes per hour, on average.

The tree has an MAE of eighty-nine point five, an RMSE of one hundred and twenty-four point zero, and R squared of zero point six seven six. It is wrong by about ninety bikes per hour. The linear model treats the hour as a straight line, so it cannot capture the rush-hour peaks. The tree can.

Finally, we plot the tree's predictions against the real values, with a diagonal line. Points far from the line are the big misses.

A common mistake is to report R squared alone. A manager cannot plan bikes with R squared. Report MAE or RMSE in business units, and compare them with the size of the target. An error of ninety bikes is large when the average is two hundred and forty-three.

## Recap
Let's recap. First, regression uses the same fit and predict workflow. Linear models draw straight lines, while trees can follow peaks. Second, MAE and RMSE are in the target's units, and RMSE is larger when the model makes some big misses. Third, R squared shows the share of variation explained, but report MAE or RMSE in business units to stakeholders.

## CTA
Now it is your turn. In the exercise below this video, you will predict hourly bike rentals, report your errors in bikes per hour, and plot predicted against actual values. It takes about thirty minutes. In the next lesson, Ensembles: Random Forests and Gradient Boosting, we combine many trees into one stronger model. See you there.

## Thumbnail
Headline: Errors Measured in Bikes
Image: Navy background, a row of shared bikes at a dock with a small bar chart of hourly rentals peaking at 8 and 18, headline in teal Inter Bold.

## Production Notes
- Setup before recording: start a fresh Colab runtime. Scene 8 runs the L11 setup cell (content.md L11 Worked Example, first code block), which is shared by L11, L12 and L13; save this notebook as the bike notebook. Do not run the L05 bank cells in the same runtime, because they reuse the names X_train and y_train.
- [VERIFY] Availability, licence, column names and file encoding of the UCI Seoul Bike Sharing Demand dataset. The voiceover only mentions a public bike-sharing dataset for the exercise and does not describe it.
- [VERSION] root_mean_squared_error replaced mean_squared_error(squared=False) in recent releases; check the Colab version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6, NumPy 2.4 and Python 3.11 on synthetic data; re-run before recording and update every spoken value if it differs.
- Screen scenes 8 to 11 use the two cells copied exactly from the content.md Worked Example; the scratch check of bikes.shape and the mean in scene 8 only confirms the 8,760 hours and about 243 rentals that content.md states. Scene 12 (scatter plot): content.md gives only plt.scatter(y_test, pred, s=3) plus 'a diagonal line'; the extra import and plt.plot line in the screen steps are a suggestion for review. pred holds the tree's predictions because the tree is the last model in the loop.
- Park Ji-woo and the city bike-sharing scheme are fictional. Speak R² as 'R squared'.
