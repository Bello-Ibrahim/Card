# HeyGen Batch Pack: AI-12 M3 (Regression and Model Improvement)

Course: Machine Learning with scikit-learn. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L11 Regression Models and Metrics

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M3_L11_presenter.mp4`
- **Expected length:** about 5.1 minutes (702 words). The quality gate accepts ±10%.

```text
A bike-sharing manager does not ask, will people rent bikes? She asks, how many bikes will we need at eight tomorrow morning? When the answer is a number, you need regression, and you need metrics that speak in bikes.

So far, our models answered yes or no questions. Regression models predict a number. The workflow is exactly the same: create, fit, predict. Two model families are a good start.

Linear regression fits a weighted sum of the features. It is fast and easy to explain, but it can only draw straight-line relationships. A decision tree for regression splits the data, and each leaf predicts the average of its training rows. It can follow curves and peaks, but it overfits if it grows too deep.

Now three metrics, in words. MAE, the mean absolute error, is the average size of the error, in the target's own units. For example, on average our prediction is ninety bikes away from the real number. RMSE, the root mean squared error, is also in the target's units, but it punishes large errors more.

If RMSE is much larger than MAE, the model makes some big misses. R squared shows how much of the variation in the target the model explains, compared with always predicting the average. One is perfect, and zero is no better than the average. It has no units, so it is harder to use with a manager.

MAE is like the average number of minutes a bus is late. RMSE is the same idea, but a bus that is forty minutes late counts much more than four buses that are ten minutes late. Passengers remember the very late bus, and RMSE does too.

Park Ji-woo is an analyst for a city bike-sharing scheme. The exercise uses a public bike-sharing dataset, but the demo uses a synthetic year of hourly data with a similar shape, so the results are repeatable.

In a fresh notebook, we run the setup cell. It creates one year of hourly data, with temperature, humidity, and a morning and evening rush on workdays. That is eight thousand, seven hundred and sixty hours, with an average of about two hundred and forty-three rentals per hour.

The model cell uses three features: temperature, humidity, and the hour of the day. It keeps twenty percent of the hours for testing. Then it trains a linear model and a tree with a depth of eight, and prints MAE, RMSE and R squared for each.

The linear model has an MAE of one hundred and forty-one point seven, an RMSE of one hundred and eighty-six point four, and R squared of zero point two six eight. In business terms, it is wrong by about one hundred and forty-two bikes per hour, on average.

The tree has an MAE of eighty-nine point five, an RMSE of one hundred and twenty-four point zero, and R squared of zero point six seven six. It is wrong by about ninety bikes per hour. The linear model treats the hour as a straight line, so it cannot capture the rush-hour peaks. The tree can.

Finally, we plot the tree's predictions against the real values, with a diagonal line. Points far from the line are the big misses.

A common mistake is to report R squared alone. A manager cannot plan bikes with R squared. Report MAE or RMSE in business units, and compare them with the size of the target. An error of ninety bikes is large when the average is two hundred and forty-three.

Let's recap. First, regression uses the same fit and predict workflow. Linear models draw straight lines, while trees can follow peaks. Second, MAE and RMSE are in the target's units, and RMSE is larger when the model makes some big misses. Third, R squared shows the share of variation explained, but report MAE or RMSE in business units to stakeholders.

Now it is your turn. In the exercise below this video, you will predict hourly bike rentals, report your errors in bikes per hour, and plot predicted against actual values. It takes about thirty minutes. In the next lesson, Ensembles: Random Forests and Gradient Boosting, we combine many trees into one stronger model. See you there.
```

## L12 Ensembles: Random Forests and Gradient Boosting

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (678 words). The quality gate accepts ±10%.

```text
One decision tree is easy to understand, but unstable. Change a few rows, and it can grow very differently. What if you trained hundreds of trees and combined them? That simple idea is behind two of the strongest model families for business data.

An ensemble combines many models into one prediction. The first approach is a random forest. It trains many deep trees, each on a random sample of the rows, and each looking at a random subset of features at every split. So each tree makes different mistakes.

For regression, the forest averages the trees' predictions. For classification, it combines their votes. Averaging cancels out much of each tree's noise, so a forest overfits much less than one deep tree. The trees are independent, so they can train in parallel.

The second approach is gradient boosting. It trains small trees one after another. Each new tree tries to correct the errors the earlier trees still make. It is often the most accurate model on tables of data, but it has more settings, and it can overfit if it runs too long.

scikit-learn has fast versions, called histogram gradient boosting. They group values into bins, handle missing values without an imputer, and can stop early. Neither ensemble needs scaled features, because both are built from trees. Start with a simple baseline, try a random forest next, then boosting when you want the best accuracy.

Ask one person to guess the number of beans in a jar, and the guess may be far off. Ask two hundred people and average their guesses, and the average is often closer. A random forest is that crowd. Boosting is a team where each new member fixes what the team got wrong so far.

Amara Diallo runs analytics for a scooter-rental start-up in Dakar, Senegal. She has the same kind of hourly demand problem as lesson eleven, and wants to know if ensembles are worth their extra complexity.

We continue in the bike notebook, with the training data ready. This cell creates five folds, then cross-validates three models on the same folds: linear regression, a forest of two hundred trees, and gradient boosting. For each, it prints the mean RMSE and the spread.

Two details. scikit-learn scores follow the rule that higher is better, so errors come back as negative numbers. The minus sign at the start turns them into normal RMSE values. And we use plain folds, not stratified ones, because the target is a number.

The results. Linear regression has an RMSE of one hundred and eighty-two point three, with a spread of two point eight. The forest scores one hundred and twenty-eight point seven, spread one point six. Boosting scores one hundred and twenty-two point six, spread one point eight.

Both ensembles cut the error by more than fifty bikes per hour, far more than the spread. Boosting is about six bikes per hour better than the forest, also more than the spread. So Amara picks gradient boosting. But all three models still see only temperature, humidity and hour.

A common mistake is to assume the most complex model always wins, and skip the baseline. On small or noisy data, a simple linear model can match an untuned ensemble. Always compare with a baseline on the same folds. And do not forget the minus sign on error scores.

Let's recap. First, a random forest averages many different trees, which reduces overfitting, so it is a strong, low-effort second model. Second, gradient boosting adds trees one by one to correct earlier errors, and the histogram versions are fast and handle missing values. Third, compare ensembles with a simple baseline on the same folds, and remember that error scores are negative in scikit-learn.

Now it is your turn. In the exercise below this video, you will compare the three models on the bike data, add a second error metric and training times, and choose one. It takes about thirty minutes. In the next lesson, Feature Engineering That Helps, we keep the model the same and change what it sees. See you there.
```

## L13 Feature Engineering That Helps

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M3_L13_presenter.mp4`
- **Expected length:** about 5.4 minutes (738 words). The quality gate accepts ±10%.

```text
In the last lesson, we changed the model and saved about sixty bikes per hour of error. Today we keep the model the same, and change only what it sees. One new column, made from a timestamp we already had, will cut the error in half.

Feature engineering means creating new input columns from the data you already have, so the pattern becomes easier to learn. Date and time parts are a classic example: hour, day of the week, month, or is it a weekend. A raw timestamp means little to a model, but its parts often carry the pattern.

Other useful types are ratios, such as debt divided by income, or spend per visit. Interactions, where two features together behave differently, such as hot and weekend. And bins, such as age bands, which help linear models follow patterns that are not straight lines.

Two rules keep feature engineering honest. First, test every new feature with cross-validation. Keep it only if it helps by more than the normal spread. More columns are not automatically better. Useless features add noise, and make models slower and harder to explain.

Second, never use future information. Average rentals for the whole day uses hours that have not happened yet at eight in the morning, so it leaks the answer. Rentals at the same hour yesterday is fine, because it is already known.

One more note. For simplicity, today's demo uses a random split. For real forecasting, use a time-ordered split, which always trains on earlier hours and tests on later ones. A random split can make scores look a little better than they will be.

Feature engineering is like preparing ingredients before cooking. The same oven gives a much better result when the vegetables are washed and cut to the right size. But you cannot use an ingredient that will only arrive tomorrow.

Sofia Petrova is a data analyst for a bike-sharing scheme in Sofia, Bulgaria. Her boosting model from the last lesson has an RMSE of about one hundred and twenty-three bikes per hour. She suspects it misses the difference between workdays and weekends.

We continue in the bike notebook. This cell builds a table of candidate features from the timestamp: the hour, the day of the week, a weekend flag, and temperature times humidity. It uses the same training rows as before, and a small helper cross-validates the boosting model on any list of columns.

The base set of temperature, humidity and hour gives a cross-validated RMSE of one hundred and twenty-two point six. Adding the day of the week cuts it to fifty-seven point two bikes per hour. The model can now separate weekday rush hours from the weekend afternoon pattern.

The weekend flag gives almost the same gain, fifty-seven point one. It carries the same information in a simpler form, so Sofia keeps one of the two, not both.

Temperature times humidity makes no real difference: one hundred and twenty-two point eight, against one hundred and twenty-two point six. So she drops it. A tree ensemble can already combine those two features by itself.

Sofia notes one more thing. In this synthetic data, the random noise has a standard deviation of sixty, so an error near fifty-seven is close to the best any model can do. With real data, she would not know that limit, which is why every step must be measured.

A common mistake is to build features from the whole dataset using the target or future rows, such as average rentals per hour over the whole year, test rows included. That is leakage. Features that use only the row's own values are safe before the split. Anything that learns from other rows belongs inside the pipeline.

Let's recap. First, good features, such as time parts, ratios and interactions, can improve a model more than a change of algorithm. Second, keep a new feature only if it improves the cross-validated score by more than the normal spread. Third, every feature must be known at prediction time, because statistics that use the target or future rows leak information.

Now it is your turn. In the exercise below this video, you will add three new features to the bike data, measure each one with cross-validation, and keep only those that help. It takes about thirty minutes. In the next lesson, Hyperparameter Tuning with Grid and Random Search, you will let scikit-learn search for better settings. See you there.
```

## L14 Hyperparameter Tuning with Grid and Random Search

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M3_L14_presenter.mp4`
- **Expected length:** about 5.1 minutes (703 words). The quality gate accepts ±10%.

```text
Every model so far used default settings, or settings we picked by hand. Defaults are a reasonable start, not the best choice for your data. Today, scikit-learn searches for better settings, and you will see that tuning helps, but does not work miracles.

Hyperparameters are settings you choose before training, such as the maximum depth, the minimum leaf size, or the number of trees. The model does not learn them from data. Tuning means trying many combinations, and keeping the one with the best cross-validated score.

Grid search tries every combination in a grid. Three values for each of four settings means eighty-one combinations. With five folds, that is four hundred and five fits. Grids grow very quickly. Random search tries a fixed number of random combinations, and often finds settings nearly as good, in much less time.

Both work on a whole pipeline, so preprocessing is refitted inside every fold. To reach a setting inside a pipeline, you use the step name, then two underscores, then the setting name. After the search, you get the best settings, their mean score, and the best pipeline, refitted on all the training data.

The rule from lesson three still holds. The test set stays untouched until the very end. The search uses only training data, and you look at the test score once, after all choices are made.

Tuning is like adjusting a new sewing machine: stitch length, thread tension and speed. You could test every combination on a practice cloth, or test twenty random ones and keep the best. Either way, you practise on scrap cloth, not on the customer's dress. The test set is the customer's dress.

Youssef Haddad is a data scientist at a bank in Beirut, Lebanon. His random forest for term-deposit subscriptions uses default settings, and he wants to know whether tuning helps.

We continue in the bank notebook. This cell puts a random forest into the pipeline, defines ranges for four settings, and runs a random search of twenty combinations with five folds, scored by ROC AUC. Then it scores the untuned and tuned pipelines on the test set, once.

The search chose two hundred trees, the square-root feature setting, a maximum depth of twelve, and a minimum of forty customers per leaf. Its mean cross-validated ROC AUC is zero point seven six nine.

Forty customers per leaf is the key choice. It stops the trees from memorising individual people. That fits what you saw in lesson seven. The default forest was too flexible for fifteen hundred noisy training rows.

On the test set, ROC AUC rose from zero point seven zero one to zero point seven three seven. But the logistic regression pipeline from lesson nine scored zero point seven five two on the same test set. Tuning improved the forest, yet the simpler model is still slightly ahead.

Youssef's conclusion: tuning helped the forest, but for this data, the logistic model is simpler, easier to explain, and at least as good. He will carry it forward. That is a good result. The search saved him from assuming that a complex model is better.

A common mistake is to tune on the test set, or to search before splitting. Then the best settings have seen the test rows, and the final score is too optimistic. Another is a huge grid that runs for hours. Start with a random search over wide ranges, then, if needed, a small grid around the best values.

Let's recap. First, hyperparameters are settings you choose before training, and tuning searches for the combination with the best cross-validated score. Second, random search is usually more efficient than grid search, and step name plus two underscores reaches a setting inside a pipeline. Third, search on training data only, check the test set once, and compare the tuned model with a simple baseline.

Now it is your turn. In the exercise below this video, you will tune a random forest with random search, score it once on the test set, and compare it with the untuned model and your best simple model. It takes about thirty-five minutes. In the next lesson, Which Features Matter? Interpreting Models, you will explain what drives your model. See you there.
```
