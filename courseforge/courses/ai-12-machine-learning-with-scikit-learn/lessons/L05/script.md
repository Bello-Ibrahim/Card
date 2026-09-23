# L05 Pipelines and ColumnTransformer | Presenter Script

Course: AI-12 · Video: 5 min · Words: 717

## Hook
In the last lesson, you scaled and encoded columns by hand, with separate objects and careful ordering. In a real project with fifteen columns and many experiments, one small slip lets test data leak into training. Today you will remove that risk.

## Explain
A pipeline chains steps into one estimator. Every step except the last one is a transformer, and the last step is the model. When you fit the pipeline on training data, each step learns from the training data and passes its output to the next step.

When you predict, each step only transforms. So fitting on the training data only happens automatically. You do not have to remember the order yourself.

A column transformer sends different columns to different steps. Numbers go to filling missing values and scaling. Categories go to one-hot encoding. Then the outputs are placed side by side again.

This matters most for data leakage. Leakage means information that would not be available at prediction time reaches the model during training. It makes test scores look better than real performance. Pipelines stop one kind, preprocessing that learns from test rows. They also make cross-validation and tuning safe later in the course.

But pipelines cannot stop the other kind of leakage: a feature that is recorded after the event. You must remove that yourself, as Larissa did in lesson one.

Think of a factory assembly line. Each station does one job in a fixed order, and a product cannot skip a station or enter halfway. The column transformer is where parts are sorted. Metal parts go to one station, plastic parts to another, and then they are joined again.

## Demonstrate
Oluwaseun Adeyemi is a developer in Lagos. He wants to predict which bank customers will subscribe to a term deposit. To keep the demo repeatable, the course notebook uses synthetic bank marketing data, where about twelve percent of customers subscribe.

First, we run the setup cell. It creates two thousand synthetic customers with age, balance, number of calls, job and contact type. It hides one hundred balances as missing values. Then it splits the data once, keeping a quarter for testing. We will reuse this cell for most of the course.

Look at the last lines of the setup cell. The target is whether the customer subscribed, and the features are all the other columns. The split keeps the same share of subscribers in both sets, and uses a fixed random state, so your numbers will match mine.

Now the pipeline cell. For numbers, a small pipeline fills missing values with the median, then scales. For categories, a one-hot encoder. The column transformer sends each list of columns to its own step, and logistic regression is the final model. Then one fit call, and we print the test accuracy.

The test accuracy is zero point eight eight four. Notice what happened. The one hundred missing balances were filled with the training median, inside the pipeline. And that single fit call ran every step, in the right order.

In Colab, you can display the pipeline itself, and you get a diagram of the steps. Keep that score of zero point eight eight four in mind. In lesson eight, you will see why it is less impressive than it looks.

A common mistake is to build a good pipeline, and then fill missing values or scale the full table first, to clean it. The pipeline is then fed data that already contains test information. Put every step that learns from data inside the pipeline. And check each column's meaning, so no feature is only known after the event.

## Recap
Let's recap. First, a pipeline chains preprocessing and a model into one estimator, so one fit call learns every step from training data only. Second, a column transformer applies different steps to numbers and categories, and joins the results. Third, pipelines prevent preprocessing leakage, but you must still remove features that are only known after the event.

## CTA
Now it is your turn. In the exercise below this video, you will build a pipeline that fills, scales, encodes and fits a model in one call, and display its diagram. Use public data only. It takes about thirty minutes. In the next lesson, Logistic Regression for Yes/No Questions, we look inside this model. See you there.

## Thumbnail
Headline: One Object, One Fit
Image: Navy background, an assembly line of three stations (impute, scale, encode) feeding a model box, headline in teal Inter Bold.

## Production Notes
- content.md lists this lesson as 6 minutes; the script is held to the brief's 5-minute word range (630 to 770 words), so it runs about five and a half minutes.
- [VERIFY] The voiceover does not describe the UCI Bank Marketing dataset (source, column names campaign and duration, target y, licence). Content.md says it comes from a Portuguese bank's phone campaign for term deposits and that duration is only known after the call; both claims stay here for review and are not spoken.
- [VERSION] set_output(transform="pandas"), OneHotEncoder(sparse_output=...) and the pipeline diagram display in Colab depend on the installed scikit-learn version. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11; re-run and update the spoken 0.884 if the output differs.
- Setup: scene 9 runs the shared setup cell (content.md Worked Example, first code block). This cell and the pipeline cell in scene 11 are reused in L06, L08, L09, L10, L14, L15, L16 and L17, so save the recording notebook as the course notebook.
- Scene 13: after the pipeline cell, run a new cell containing only pipe to show the Colab diagram, as content.md describes.
- Oluwaseun Adeyemi is fictional; the data is synthetic.
