# L13 Feature Engineering That Helps | Presenter Script

Course: AI-12 · Video: 5 min · Words: 753

## Hook
In the last lesson, we changed the model and saved about sixty bikes per hour of error. Today we keep the model the same, and change only what it sees. One new column, made from a timestamp we already had, will cut the error in half.

## Explain
Feature engineering means creating new input columns from the data you already have, so the pattern becomes easier to learn. Date and time parts are a classic example: hour, day of the week, month, or is it a weekend. A raw timestamp means little to a model, but its parts often carry the pattern.

Other useful types are ratios, such as debt divided by income, or spend per visit. Interactions, where two features together behave differently, such as hot and weekend. And bins, such as age bands, which help linear models follow patterns that are not straight lines.

Two rules keep feature engineering honest. First, test every new feature with cross-validation. Keep it only if it helps by more than the normal spread. More columns are not automatically better. Useless features add noise, and make models slower and harder to explain.

Second, never use future information. Average rentals for the whole day uses hours that have not happened yet at eight in the morning, so it leaks the answer. Rentals at the same hour yesterday is fine, because it is already known.

One more note. For simplicity, today's demo uses a random split. For real forecasting, use a time-ordered split, which always trains on earlier hours and tests on later ones. A random split can make scores look a little better than they will be.

Feature engineering is like preparing ingredients before cooking. The same oven gives a much better result when the vegetables are washed and cut to the right size. But you cannot use an ingredient that will only arrive tomorrow.

## Demonstrate
Sofia Petrova is a data analyst for a bike-sharing scheme in Sofia, Bulgaria. Her boosting model from the last lesson has an RMSE of about one hundred and twenty-three bikes per hour. She suspects it misses the difference between workdays and weekends.

We continue in the bike notebook. This cell builds a table of candidate features from the timestamp: the hour, the day of the week, a weekend flag, and temperature times humidity. It uses the same training rows as before, and a small helper cross-validates the boosting model on any list of columns.

The base set of temperature, humidity and hour gives a cross-validated RMSE of one hundred and twenty-two point six. Adding the day of the week cuts it to fifty-seven point two bikes per hour. The model can now separate weekday rush hours from the weekend afternoon pattern.

The weekend flag gives almost the same gain, fifty-seven point one. It carries the same information in a simpler form, so Sofia keeps one of the two, not both.

Temperature times humidity makes no real difference: one hundred and twenty-two point eight, against one hundred and twenty-two point six. So she drops it. A tree ensemble can already combine those two features by itself.

Sofia notes one more thing. In this synthetic data, the random noise has a standard deviation of sixty, so an error near fifty-seven is close to the best any model can do. With real data, she would not know that limit, which is why every step must be measured.

A common mistake is to build features from the whole dataset using the target or future rows, such as average rentals per hour over the whole year, test rows included. That is leakage. Features that use only the row's own values are safe before the split. Anything that learns from other rows belongs inside the pipeline.

## Recap
Let's recap. First, good features, such as time parts, ratios and interactions, can improve a model more than a change of algorithm. Second, keep a new feature only if it improves the cross-validated score by more than the normal spread. Third, every feature must be known at prediction time, because statistics that use the target or future rows leak information.

## CTA
Now it is your turn. In the exercise below this video, you will add three new features to the bike data, measure each one with cross-validation, and keep only those that help. It takes about thirty minutes. In the next lesson, Hyperparameter Tuning with Grid and Random Search, you will let scikit-learn search for better settings. See you there.

## Thumbnail
Headline: One Column Halves Error
Image: Navy background, a timestamp splitting into hour, weekday and weekend tags, an RMSE bar shrinking from 122.6 to 57.2, headline in teal Inter Bold.

## Production Notes
- Setup before recording: in a fresh Colab runtime, run the L11 setup cell (content.md L11 Worked Example, first code block: synthetic hourly bike data) and then the L11 model cell (second code block: features, the split with random_state=0, and the two models). Then run the L12 cell (content.md L12 Worked Example), which defines cv, cross_val_score and HistGradientBoostingRegressor. The L13 cell uses bikes, X_train, y_train and cv from these three cells. Do not run the L05 bank cells in the same runtime, because they reuse the names X_train and y_train.
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11 on synthetic data. The pandas .dt accessors, KBinsDiscretizer and TimeSeriesSplit should be checked against the Colab versions before recording; update the spoken RMSE values if the output differs.
- Screen scenes 9 to 13 use one cell copied exactly from the content.md Worked Example. Each cross-validation run takes a few seconds; cut the wait in editing.
- Hook: 'about sixty bikes per hour' is the L12 difference between linear (182.3) and boosting (122.6); 'cut the error in half' refers to 122.6 falling to 57.2.
- Sofia Petrova and the Sofia bike-sharing scheme are fictional; the data is synthetic.
