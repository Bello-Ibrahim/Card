# L02 Your First Model: fit and predict | Presenter Script

Course: AI-12 · Video: 5 min · Words: 685

## Hook
scikit-learn contains dozens of models, from simple lines to large forests of trees. The good news is that you use almost all of them in the same way. Learn two steps today, fit and predict, and you can use most of the library.

## Explain
In lesson one, you framed a problem. Now let's train a model. In scikit-learn, a model is called an estimator, and every estimator follows the same three stages.

First, you create it and choose its settings, for example a decision tree with a maximum depth of three. Nothing is learned yet. Second, you fit it on a table of features, called X, with one row per example, and a target, called y, with one value per row. Fitting is where learning happens.

Third, you predict on new rows, and the model gives a target value for each one. Some objects do not predict. They change data instead, like a scaler that puts numbers on the same scale. These are called transformers, and you will use them in lesson four.

Two naming rules help you read the documentation. Settings you choose before training are called hyperparameters. Values the model learns during fitting end with an underscore, such as the list of classes it found.

Many estimators also have a score method that returns a default metric, such as accuracy for classifiers. And the exact settings and defaults depend on the version you have installed. So check the version in Colab, and open the matching documentation.

Think of kitchen appliances from one brand. A blender, a toaster and a kettle do very different jobs, but they all have the same on and start buttons. Once you know the buttons, you can use a new appliance quickly. Fit and predict are the buttons.

## Demonstrate
Kenji Watanabe is a developer in Osaka. He wants a first model before he works with company data. He uses the wine dataset that comes with scikit-learn.

Let's open Google Colab and create a new notebook. In the first cell, we load the wine data, create a decision tree, fit it, and predict five wines. Then we run the cell.

The first line of output describes the data. There are one hundred and seventy-eight wines, with thirteen chemical measurements each. The three classes of wine have fifty-nine, seventy-one and forty-eight examples.

We asked for the data as a pandas table, so the column names stay visible. That makes it much easier to check which chemical measurement is which, and it will matter more when you work with your own data.

Now look at the three stages in the code. First, we create the tree with a fixed random state, so everyone who runs this gets the same tree. Then it learns from all the wines. Then it predicts.

The model predicted classes zero, one, two, zero and one for the five chosen rows. Kenji is pleased. But wait. These five wines were also in the training data. Did the model predict them, or did it simply remember them? That question leads directly to our next lesson.

A common mistake is passing data in the wrong shape. X must always be a table with two dimensions, even for one feature or one row. Another mistake is predicting before fitting, which gives an error. The fix is always the same order. Create, fit, then predict.

## Recap
Let's recap. First, every scikit-learn estimator is created with settings, learns with fit, and is used with predict. Second, X is a two-dimensional table of features, y is one target value per row, and learned values end with an underscore. Third, set a random state so your results are repeatable, and check your library version before you trust parameter names.

## CTA
Now it is your turn. In the exercise below this video, you will load the wine data, train a decision tree, and predict five samples next to their true classes. You will also record your library version. It takes about twenty minutes. In the next lesson, Train/Test Split and Why It Matters, we answer Kenji's question. See you there.

## Thumbnail
Headline: Two Calls: fit, predict
Image: Navy background, a Colab-style code cell with two highlighted buttons labelled fit and predict, a wine glass icon in the corner, headline in teal Inter Bold.

## Production Notes
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11. Re-run the cell in the current Colab version before recording; if the printed shape, class counts or predictions differ, update the voiceover and captions to match the new output.
- [VERSION] Check load_wine with as_frame and the estimator defaults against the installed version; show sklearn.__version__ if the output differs.
- Screen scenes 9 to 13 use one Colab cell, copied exactly from the content.md Worked Example. Run it once off camera to warm up the runtime, then record a clean run.
- Kenji Watanabe is fictional. The wine dataset ships with scikit-learn, so no download is needed.
- Speak printed values as numbers, for example 'one hundred and seventy-eight' and 'fifty-nine, seventy-one, forty-eight'; the screen shows the exact output.
