# HeyGen Batch Pack: AI-12 M1 (The Machine Learning Workflow)

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

## L01 From Business Question to ML Problem

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M1_L01_presenter.mp4`
- **Expected length:** about 5.2 minutes (722 words). The quality gate accepts ±10%.
- **Pronunciation:** Say the target name is_late as 'is late' and the leaking column as 'driver delay reason'; the slide shows the exact column names.

```text
A manager asks, can we use machine learning to fix late deliveries? That is a wish, not a machine learning problem. Before you open a notebook, you must turn that wish into something a model can actually learn.

Hi, and welcome to Machine Learning with scikit-learn. Over four weeks, you will build, test and explain real models in Python. And everything starts with a well-framed problem.

You already know the idea of supervised learning. We show a model many past examples with known answers, and it learns patterns that connect the inputs to the answers. A good framing has four parts.

First, the business question. What decision will the prediction support? Which deliveries should we warn customers about today is much better than predict delays, because it tells you who uses the result, and when.

Second, the target. This is the one column the model predicts, also called the label, or y. It must be something you can see in past data, with an exact definition. For example, late means it arrived more than twenty-four hours after the promised time.

Third, the features. These are the input columns, also called X. A feature is only useful if it is known at the moment of prediction. The distance of a route is known before the truck leaves. The actual arrival time is not, so it can never be a feature.

Fourth, the success measure. You need a model metric, and also a business measure, such as fewer complaints about surprise delays. Then decide the task type. If the target is a category, such as late or on time, it is classification. If it is a number, such as hours of delay, it is regression.

Here is a simple way to think about it. Framing a problem is like writing the address before you send a parcel. The truck, the driver and the route can all be excellent. But with no clear address, the parcel cannot arrive.

Let's see a real framing. Larissa Mendes is a data analyst at a logistics company in Recife, Brazil. The operations director asks her to use AI to reduce late deliveries. Larissa writes a one-page framing.

Her business question: each morning, which of today's deliveries are likely to be late, so the customer service team can contact those customers early? Her target is called is late. It is one if the parcel arrived more than twenty-four hours after the promised date, and zero otherwise.

Her features are route distance, number of stops, day of the week, vehicle type, depot, and the weather forecast for the day. The task type is binary classification. For success, the model should find most late deliveries, without so many calls that they become useless.

She also removes one tempting column, the driver delay reason. It is filled in after the delivery, so the model would not have it in the morning. Using it would make the model look excellent in testing and fail in real use. You will meet this again as data leakage in lesson five.

Larissa notes one limit too. The company only has eight months of data, so seasonal effects, such as a holiday peak, may be missing.

A common mistake is to pick the target, and then add every column in the table as a feature. That often includes columns recorded after the event, or almost a copy of the target, such as a refund issued for late delivery. It scores well in the notebook, and fails in production. For every feature, ask one question. Would I know this value when I need the prediction?

Let's recap. First, a machine learning problem needs a business question, one target column, features known at prediction time, and a success measure. Second, a category target means classification, and a number target means regression. The decision you support tells you which to choose. Third, decide early which kind of mistake costs more, because that choice will guide your metric.

Now it is your turn. In the exercise below this video, you will frame three business problems, from loan default in Kenya to hotel cancellations in Portugal and crop yield in India. You do not need code, and it takes about twenty minutes. In the next lesson, Your First Model: fit and predict, you will train a real model in Colab. See you there.
```

## L02 Your First Model: fit and predict

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M1_L02_presenter.mp4`
- **Expected length:** about 4.9 minutes (675 words). The quality gate accepts ±10%.

```text
scikit-learn contains dozens of models, from simple lines to large forests of trees. The good news is that you use almost all of them in the same way. Learn two steps today, fit and predict, and you can use most of the library.

In lesson one, you framed a problem. Now let's train a model. In scikit-learn, a model is called an estimator, and every estimator follows the same three stages.

First, you create it and choose its settings, for example a decision tree with a maximum depth of three. Nothing is learned yet. Second, you fit it on a table of features, called X, with one row per example, and a target, called y, with one value per row. Fitting is where learning happens.

Third, you predict on new rows, and the model gives a target value for each one. Some objects do not predict. They change data instead, like a scaler that puts numbers on the same scale. These are called transformers, and you will use them in lesson four.

Two naming rules help you read the documentation. Settings you choose before training are called hyperparameters. Values the model learns during fitting end with an underscore, such as the list of classes it found.

Many estimators also have a score method that returns a default metric, such as accuracy for classifiers. And the exact settings and defaults depend on the version you have installed. So check the version in Colab, and open the matching documentation.

Think of kitchen appliances from one brand. A blender, a toaster and a kettle do very different jobs, but they all have the same on and start buttons. Once you know the buttons, you can use a new appliance quickly. Fit and predict are the buttons.

Kenji Watanabe is a developer in Osaka. He wants a first model before he works with company data. He uses the wine dataset that comes with scikit-learn.

Let's open Google Colab and create a new notebook. In the first cell, we load the wine data, create a decision tree, fit it, and predict five wines. Then we run the cell.

The first line of output describes the data. There are one hundred and seventy-eight wines, with thirteen chemical measurements each. The three classes of wine have fifty-nine, seventy-one and forty-eight examples.

We asked for the data as a pandas table, so the column names stay visible. That makes it much easier to check which chemical measurement is which, and it will matter more when you work with your own data.

Now look at the three stages in the code. First, we create the tree with a fixed random state, so everyone who runs this gets the same tree. Then it learns from all the wines. Then it predicts.

The model predicted classes zero, one, two, zero and one for the five chosen rows. Kenji is pleased. But wait. These five wines were also in the training data. Did the model predict them, or did it simply remember them? That question leads directly to our next lesson.

A common mistake is passing data in the wrong shape. X must always be a table with two dimensions, even for one feature or one row. Another mistake is predicting before fitting, which gives an error. The fix is always the same order. Create, fit, then predict.

Let's recap. First, every scikit-learn estimator is created with settings, learns with fit, and is used with predict. Second, X is a two-dimensional table of features, y is one target value per row, and learned values end with an underscore. Third, set a random state so your results are repeatable, and check your library version before you trust parameter names.

Now it is your turn. In the exercise below this video, you will load the wine data, train a decision tree, and predict five samples next to their true classes. You will also record your library version. It takes about twenty minutes. In the next lesson, Train/Test Split and Why It Matters, we answer Kenji's question. See you there.
```

## L03 Train/Test Split and Why It Matters

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M1_L03_presenter.mp4`
- **Expected length:** about 5.0 minutes (698 words). The quality gate accepts ±10%.

```text
In the last lesson, the decision tree predicted every training row correctly. That sounds perfect, but it tells us almost nothing. Today you will see a model with a perfect training score lose more than a quarter of it on new data.

The goal of a model is generalisation. That means good predictions on new cases. To estimate it, we hold back part of the data as a test set. The model never sees it during training. We train on the training set, and we measure on the test set.

scikit-learn does this with one function, and three settings matter. The test size keeps a share of rows for testing, often between twenty and thirty percent. A fixed random state makes the split repeatable. And stratifying by the target keeps the same share of each class in both sets, which matters when one class is rare.

Comparing the two scores tells you a lot. If the training score is high and the test score is much lower, the model is overfitting. It has learned the noise in the training rows, not the general pattern. If both scores are low, it is underfitting, too simple for the pattern. A good fit has both scores reasonably high, and close together.

Remember this. A very high training score on its own is never evidence of a good model. A flexible model, such as a tree with no depth limit, can almost always reach close to one hundred percent on its own training data.

Think of a fair exam. If a teacher gives the exact questions from the homework, a student who memorised the answers scores one hundred percent. But that score does not show whether the student understands. The test set is the fair exam for your model.

Fatima Zahra is an analyst at an insurance company in Casablanca, Morocco. Before she uses real claims data, she tests the idea on synthetic data, with some label noise added, as real data has.

In a new Colab cell, we create one thousand synthetic rows, split them, and train two decision trees. One tree has no depth limit. The other can ask only three questions in a row. For each tree, we print the training score and the test score.

Before we read the results, look at the split. It returns four pieces, in a fixed order: training features, test features, then training targets and test targets. Mixing up this order is a common bug.

Now the first line of output. The deep tree scores one point zero on training data. That is one hundred percent. But on the test data, it scores only zero point seven two eight. It memorised the training rows, including the noisy labels.

The second line is the shallow tree. Its training score is lower, zero point eight five three. But its test score is higher, zero point eight one two. And its two scores are much closer together.

Fatima chooses the shallow tree as her starting point, and she writes a note in her notebook. The training score of one point zero was a warning sign, not a success.

A common mistake is to use the test set again and again. You try a setting, check the test score, change the setting, and check again. After many rounds, your choices are fitted to the test set, and the final score is too optimistic. Keep the test set for one final check. To choose between settings, you will use cross-validation in lesson ten.

Let's recap. First, hold back a test set, and use a fixed random state and stratification for repeatable, balanced splits. Second, a big gap between a high training score and a lower test score means overfitting, and two low scores mean underfitting. Third, a high training score alone proves nothing, so keep the test set for the final check only.

Now it is your turn. In the exercise below this video, you will compare a deep and a shallow tree, then change the random seed and watch the test scores move. It takes about twenty minutes. In the next lesson, Preprocessing: Scaling and Encoding, you will prepare mixed data for a model. See you there.
```

## L04 Preprocessing: Scaling and Encoding

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M1_L04_presenter.mp4`
- **Expected length:** about 4.9 minutes (672 words). The quality gate accepts ±10%.

```text
Your data has income in the thousands, age in the tens, and a city column with text. Most models cannot read text at all, and some are confused by very different number sizes. Preprocessing fixes both, if you do it in the right order.

In the last lesson, you split data into training and test sets. You already know how to clean data with pandas. Today we add two steps that prepare clean data for a model: scaling numbers, and encoding categories.

Some models compare distances or add up weighted features, for example k-nearest neighbours and logistic regression. If income is in thousands and age in tens, income dominates just because its numbers are bigger. A standard scaler rescales each column so it has an average of zero and a standard deviation of one.

Tree-based models, such as decision trees and random forests, do not need scaling, because they split on one column at a time. For text categories, a one-hot encoder turns a city column into one column per city, with one where the row has that city and zero elsewhere.

We tell the encoder to ignore unknown categories. Then a city that appears only in new data does not cause an error. That row simply gets zero in every city column.

Now the golden rule. A scaler learns averages, and an encoder learns the list of categories. If they learn from all the data, information from the test set leaks into training. So always fit them on the training set only, and then just transform the test set.

Scaling is like converting prices into one currency before you compare them. Five thousand in one currency is not bigger than fifty in another until you convert. And the exchange rate must come from the information you had at the time, not next month's rates.

Valentina Rojas is an analyst at a microfinance firm with offices in Lima, Quito and Bogotá. She has a small table of eight clients, and wants to prepare it for a model.

In Colab, this cell builds the table, splits it first, then fits a scaler on the training numbers and an encoder on the training cities. Only after that does it transform the test rows. Let's run it.

The first output line shows the shapes. The test set has two rows. They become two scaled number columns, and three city columns.

The second line shows readable names for the new columns, one for each city in the training set. You will need these names again when we look inside a model in lesson six.

The third line is the important one. The scaler learned an average income of three thousand, two hundred and sixty-six point seven, and an average age of thirty-seven point seven. These come from the six training rows only, not from all eight clients.

Valentina notices that doing this by hand, for every column, is slow and easy to get wrong. The next lesson shows how to do it all in one object.

The most common mistake is to scale or encode the whole dataset first, and then split it. The code runs, and the scores look normal, so the problem is hard to see. But the test rows have already shaped the average. With other steps, this habit leads to serious leakage. Split first, then fit.

Let's recap. First, scale numbers for distance-based and linear models, but tree models do not need it. Second, turn categories into numbers with a one-hot encoder that ignores unknown values, and check the parameter names for your version. Third, fit preprocessing on the training set only, and transform the test set with the same fitted objects.

Now it is your turn. In the exercise below this video, you will scale and encode a mixed table, fitting on the training set only, and add a new city to check that nothing breaks. It takes about twenty-five minutes. In the next lesson, Pipelines and ColumnTransformer, you will put all of this into one safe object. See you there.
```

## L05 Pipelines and ColumnTransformer

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M1_L05_presenter.mp4`
- **Expected length:** about 5.1 minutes (713 words). The quality gate accepts ±10%.

```text
In the last lesson, you scaled and encoded columns by hand, with separate objects and careful ordering. In a real project with fifteen columns and many experiments, one small slip lets test data leak into training. Today you will remove that risk.

A pipeline chains steps into one estimator. Every step except the last one is a transformer, and the last step is the model. When you fit the pipeline on training data, each step learns from the training data and passes its output to the next step.

When you predict, each step only transforms. So fitting on the training data only happens automatically. You do not have to remember the order yourself.

A column transformer sends different columns to different steps. Numbers go to filling missing values and scaling. Categories go to one-hot encoding. Then the outputs are placed side by side again.

This matters most for data leakage. Leakage means information that would not be available at prediction time reaches the model during training. It makes test scores look better than real performance. Pipelines stop one kind, preprocessing that learns from test rows. They also make cross-validation and tuning safe later in the course.

But pipelines cannot stop the other kind of leakage: a feature that is recorded after the event. You must remove that yourself, as Larissa did in lesson one.

Think of a factory assembly line. Each station does one job in a fixed order, and a product cannot skip a station or enter halfway. The column transformer is where parts are sorted. Metal parts go to one station, plastic parts to another, and then they are joined again.

Oluwaseun Adeyemi is a developer in Lagos. He wants to predict which bank customers will subscribe to a term deposit. To keep the demo repeatable, the course notebook uses synthetic bank marketing data, where about twelve percent of customers subscribe.

First, we run the setup cell. It creates two thousand synthetic customers with age, balance, number of calls, job and contact type. It hides one hundred balances as missing values. Then it splits the data once, keeping a quarter for testing. We will reuse this cell for most of the course.

Look at the last lines of the setup cell. The target is whether the customer subscribed, and the features are all the other columns. The split keeps the same share of subscribers in both sets, and uses a fixed random state, so your numbers will match mine.

Now the pipeline cell. For numbers, a small pipeline fills missing values with the median, then scales. For categories, a one-hot encoder. The column transformer sends each list of columns to its own step, and logistic regression is the final model. Then one fit call, and we print the test accuracy.

The test accuracy is zero point eight eight four. Notice what happened. The one hundred missing balances were filled with the training median, inside the pipeline. And that single fit call ran every step, in the right order.

In Colab, you can display the pipeline itself, and you get a diagram of the steps. Keep that score of zero point eight eight four in mind. In lesson eight, you will see why it is less impressive than it looks.

A common mistake is to build a good pipeline, and then fill missing values or scale the full table first, to clean it. The pipeline is then fed data that already contains test information. Put every step that learns from data inside the pipeline. And check each column's meaning, so no feature is only known after the event.

Let's recap. First, a pipeline chains preprocessing and a model into one estimator, so one fit call learns every step from training data only. Second, a column transformer applies different steps to numbers and categories, and joins the results. Third, pipelines prevent preprocessing leakage, but you must still remove features that are only known after the event.

Now it is your turn. In the exercise below this video, you will build a pipeline that fills, scales, encodes and fits a model in one call, and display its diagram. Use public data only. It takes about thirty minutes. In the next lesson, Logistic Regression for Yes/No Questions, we look inside this model. See you there.
```
