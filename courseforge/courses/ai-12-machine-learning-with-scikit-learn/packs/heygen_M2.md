# HeyGen Batch Pack: AI-12 M2 (Classification: Models and Metrics)

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

## L06 Logistic Regression for Yes/No Questions

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M2_L06_presenter.mp4`
- **Expected length:** about 5.1 minutes (706 words). The quality gate accepts ±10%.

```text
Will this customer subscribe? Yes or no. But a bank calling thousands of people wants more than yes or no. It wants to know how likely each person is to say yes, so it can call the most promising customers first.

In the last lesson, you built a pipeline with logistic regression at the end. Today we look inside it. Despite its name, logistic regression is a classification model, and it works in two stages.

First, it combines the features into one score. Each feature is multiplied by a weight, called a coefficient, and the results are added up with a starting value. Second, it squeezes that score into a probability between zero and one.

The model can give you these probabilities directly. Its normal prediction applies a threshold of zero point five. A probability of zero point five or more becomes yes, and anything lower becomes no. The threshold is a business choice, not a law of nature, and in lesson nine you will move it.

A positive coefficient pushes the probability of yes up as the feature increases. A negative one pushes it down. The size shows the strength, but only if features are on comparable scales. That is why we scale numbers first. For one-hot columns, the coefficient compares that category with the others.

Two cautions. Coefficients describe what the model learned from this data. They do not prove cause and effect. And when features are strongly related, the model can share weight between them in unstable ways.

Think of a panel of judges giving points. Each feature is a judge who adds or removes points, and some judges have a stronger voice. The total becomes a percentage, and the bank decides how high it must be before it picks up the phone.

Priya Nair is a marketing analyst at a bank in Kochi, India. She wants to know which customer groups respond to term-deposit calls. She continues in the course notebook, where the setup cell and the pipeline from lesson five have already run.

This cell takes the readable feature names from the preprocessing step, pairs them with the model's coefficients, and sorts them. Then it prints the probability of yes for the first three test customers, and the model's yes or no decision for each.

At the bottom of the list are the largest positive coefficients. Being retired has the strongest push, zero point eight two. Then older age, zero point five eight, and a higher balance, zero point four two. These raise the probability of subscribing.

At the top are the largest negative ones. More calls in this campaign, minus zero point six nine. Telephone contact, minus zero point three six. And technician jobs, minus zero point three four. These lower the probability.

Now the first three test customers. Their probabilities of yes are three percent, two percent and seventeen percent. All are below zero point five, so all three are predicted no. The prefixes num and cat simply come from the step names in the column transformer.

Priya notes one thing. More calls lowers the probability. That could mean repeated calls annoy people. Or it could mean the bank keeps calling people who were never interested. The model cannot tell which.

A common mistake is to compare coefficients of features that were not scaled. A weight per unit of income cannot be compared with a weight per year of age. Always read coefficients from a pipeline that scales numbers, and describe them as associations, not causes.

Let's recap. First, logistic regression is a classifier that outputs a probability, and by default it turns that into yes or no at zero point five. Second, positive coefficients push the probability of yes up, and negative ones push it down, but compare sizes only after scaling. Third, coefficients show what the model learned from this data, not what causes the outcome.

Now it is your turn. In the exercise below this video, you will list the three largest positive and negative coefficients in your own pipeline, and describe each one in plain words, using is linked with rather than causes. It takes about twenty-five minutes. In the next lesson, Decision Trees and k-Nearest Neighbours, we meet two new models. See you there.
```

## L07 Decision Trees and k-Nearest Neighbours

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M2_L07_presenter.mp4`
- **Expected length:** about 5.2 minutes (712 words). The quality gate accepts ±10%.

```text
Two models, two very different ideas. One asks a series of yes or no questions. The other asks, which past cases look most like this one? Both are easy to understand, and both show clearly how a model can be too simple, or too flexible.

In lesson three, you saw a deep tree memorise its training data. Let's look at trees more closely. A decision tree is a flowchart. At each point, it asks a question about one feature, such as, is age above forty-five? It sends the row left or right, and at the end a leaf gives the prediction.

The most important setting is the maximum depth, the number of questions in a row. A shallow tree asks too few questions and misses real patterns. That is underfitting. A very deep tree keeps splitting until each leaf holds only a handful of training rows. It memorises noise. That is overfitting.

k-nearest neighbours does not build rules. To predict, it finds the k training rows closest to the new row, and takes a vote. It measures closeness as a distance across all features, so scaling matters. A small k follows single noisy points, and a very large k smooths away real differences.

The best way to see this is a validation curve. You plot the training and test scores while you change one setting. Where the training score keeps rising, but the test score stops rising or falls, the model has started to overfit.

A tree is like the game Twenty Questions. A few good questions find the answer. But with a thousand very specific questions, you are describing one person, not learning about people. And k-nearest neighbours is like asking your closest neighbours for advice. Useful, but only if you measure close fairly.

Mateo Fernández works for a farming cooperative in Argentina. He wants to understand model flexibility before he predicts crop problems. He uses the same synthetic data and split as lesson three.

This cell trains twenty trees, with depths from one to twenty. For each tree, it records the training score and the test score. Then it plots both lines, so we can see the whole story at once.

At depth one, the tree scores zero point six eight nine on training data and zero point six four eight on test data. Too simple. At depth four, the test score is at its highest, zero point eight two eight, with training at zero point eight six five.

After that, training keeps rising. At depth eight, it is zero point nine four seven, but test has fallen to zero point seven nine two. From depth thirteen to twenty, training is a perfect one, and test drops to zero point seven two eight. That is overfitting.

Next, k-nearest neighbours on the wine data. This cell trains the same model twice. Once on the raw measurements, and once inside a small pipeline that scales the features first. Then it prints both test scores.

Without scaling, the test accuracy is zero point seven two two. With scaling, it jumps to zero point nine six three. One wine feature has values in the hundreds or thousands, so without scaling, it decides the distance almost alone.

A common mistake is to choose the depth or k with the highest training score. For trees, that is always the deepest tree. For k-nearest neighbours, it is k equals one, because each training row is its own nearest neighbour. Both choices overfit. Choose settings using held-out data, and later with cross-validation and tuning.

Let's recap. First, a decision tree asks yes or no questions, so limit its depth or leaf size to stop it memorising the training data. Second, k-nearest neighbours predicts from the most similar training rows, so always scale features first. Third, a plot of training and test scores against one setting shows where underfitting ends and overfitting begins.

Now it is your turn. In the exercise below this video, you will vary the depth from one to twenty, plot both scores, and mark where your model starts to overfit. Then you will do the same for k-nearest neighbours. It takes about thirty minutes. In the next lesson, Accuracy Is Not Enough: The Confusion Matrix, we look at better ways to measure. See you there.
```

## L08 Accuracy Is Not Enough: The Confusion Matrix

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M2_L08_presenter.mp4`
- **Expected length:** about 5.2 minutes (725 words). The quality gate accepts ±10%.

```text
Here is a fraud model that is ninety-nine percent accurate, and needs one line of code. It always says not fraud. It never catches a single fraud case. If accuracy can praise a model like that, we need better ways to measure.

Accuracy is the share of all predictions that are correct. It works well when the classes are roughly balanced, and both kinds of mistake cost about the same. It fails when one class is rare, which is common in business: fraud, churn, loan default, or customers who buy.

The confusion matrix shows where the model is right and wrong. The rows are the actual classes, and the columns are the predicted classes. So we get true negatives, false positives, false negatives and true positives.

From these four counts come three key metrics. Precision asks, of all the cases the model flagged as yes, how many really were yes? High precision means few false alarms. Recall asks, of all the real yes cases, how many did the model find? High recall means few missed cases.

F one is one number that balances precision and recall. It is high only when both are reasonably high. Precision and recall usually pull against each other. Flag more cases, and you find more real ones, but you also raise more false alarms.

Which one matters more depends on the cost of each mistake, which you wrote down in lesson one. And a useful habit is to compare every model with a baseline that always predicts the most common class.

Think of a smoke alarm that never rings. It is correct on almost every day of the year, because most days have no fire. But it fails on the one day that matters. Recall asks, did it ring when there was a fire? Precision asks, when it rang, was there really a fire?

Aigerim Bekova is a data analyst at a payment company in Almaty, Kazakhstan. In her synthetic data, about one in a hundred card payments is fraud. First, she shows her team the lazy baseline.

This cell creates ten thousand synthetic payments, with only one percent fraud. It fits a baseline that always predicts the most common class, then prints its accuracy and its recall.

Accuracy is zero point nine nine. Recall is zero. The model found none of the one hundred fraud cases.

Now back to the term-deposit pipeline from lesson five, where about twelve percent of customers subscribe. This cell predicts the test set, then prints the confusion matrix and a full report of the metrics.

Read the matrix. Of sixty real subscribers, the model found seven, and missed fifty-three. It raised twelve flags, and seven of them were correct. The other four hundred and thirty-five customers were correctly left alone, and five were false alarms.

So precision is seven out of twelve, zero point five eight three. Recall is seven out of sixty, zero point one one seven. And F one is only zero point one nine four.

The accuracy is zero point eight eight four, as in lesson five. But always saying no would score four hundred and forty out of five hundred, which is zero point eight eight. For a bank that wants to find subscribers, this model is weak at the default setting.

A common mistake is to report accuracy alone, or to read the wrong row of the report. The row for class one describes the positive class, usually the one the business cares about. And if your target is text, such as yes and no, tell the metric which label is positive, or convert the target to one and zero.

Let's recap. First, with rare classes, a model can have high accuracy and still be useless, so always compare with a baseline. Second, the confusion matrix shows true and false positives and negatives. Precision measures false alarms, and recall measures missed cases. Third, F one balances the two, but the business cost of each mistake decides which matters most.

Now it is your turn. In the exercise below this video, you will build a confusion matrix for your own model, calculate precision, recall and F one by hand, and check them with scikit-learn. It takes about twenty-five minutes. In the next lesson, Probabilities, Thresholds and ROC Curves, you will find more subscribers without a new model. See you there.
```

## L09 Probabilities, Thresholds and ROC Curves

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M2_L09_presenter.mp4`
- **Expected length:** about 5.1 minutes (701 words). The quality gate accepts ±10%.

```text
In the last lesson, the model found only seven of sixty subscribers. You do not need a new model to do better. The model already gives a probability for every customer. The cut-off of zero point five was simply a default.

The model's probability of yes becomes a decision at a threshold. By default, that threshold is zero point five, but you can choose any threshold yourself. A lower threshold flags more cases. Recall goes up, and precision usually goes down. A higher threshold does the opposite.

Two curves show every threshold at once. The ROC curve plots the share of real positives found against the share of negatives wrongly flagged. ROC AUC sums it up in one number. It is the chance that the model gives a random positive case a higher probability than a random negative case.

Zero point five is random guessing, and one is perfect ranking. ROC AUC does not depend on the threshold, so it measures how well the model ranks cases. The precision-recall curve plots precision against recall. With rare positive cases, it is often more informative.

So how do you pick the threshold? Put a cost on each kind of mistake, and choose the threshold with the lowest total cost. Choose it on the training data, with cross-validated predictions, not on the test set.

Think of the height of a net on a fishing boat. Lower the net, and you catch more fish, but also more weeds. Raise it, and some fish escape. The right height depends on how much a fish is worth, compared with the time spent sorting weeds.

Dr. Wanjiru Kamau runs a community clinic in Nairobi. Her team uses a risk score to decide whom to call for a free screening. Missing a patient who needs care is much worse than an extra phone call, so she prefers a low threshold.

To practise without any patient data, her analyst uses the term-deposit model from lesson five. It has the same shape of problem.

This cell takes the model's probabilities for the test customers and prints the ROC AUC. Then it tries three thresholds, and for each one it prints precision and recall.

ROC AUC is zero point seven five two. At zero point five, precision is zero point five eight three and recall is zero point one one seven, the same as last lesson. At zero point three, precision falls to zero point three nine six, and recall rises to zero point three one seven.

At zero point one five, the model finds two thirds of subscribers, a recall of zero point six six seven. But only about twenty-nine percent of flags are correct, a precision of zero point two nine two.

Now we add costs. An unneeded call costs one unit, and a missed case costs eight. This cell gets cross-validated probabilities on the training data only, then adds up the cost of each mistake for thresholds from zero point zero five to zero point nine.

The best threshold is zero point one. It costs eight hundred and thirteen units, against one thousand, three hundred and eighty-one at the default zero point five. With these costs, a low threshold is clearly better.

A common mistake is to think a better threshold makes a better model. It does not. The threshold changes the decisions, not the model's ability to rank cases. ROC AUC stays at zero point seven five two, whatever threshold you pick. And never tune the threshold on the test set.

Let's recap. First, the model gives probabilities, and the threshold turns them into decisions, trading precision against recall. Second, ROC AUC measures how well the model ranks cases, whatever the threshold, and precision-recall curves are more useful for rare positives. Third, choose the threshold from the business cost of each mistake, using cross-validated predictions on training data.

Now it is your turn. In the exercise below this video, you will plot total cost against threshold for two different cost pairs, pick the best threshold, and apply it once to the test set. It takes about thirty minutes. In the next lesson, Cross-Validation for Reliable Scores, you will learn how much a score can move. See you there.
```

## L10 Cross-Validation for Reliable Scores

- **Filename:** `ai-12-machine-learning-with-scikit-learn_M2_L10_presenter.mp4`
- **Expected length:** about 5.0 minutes (683 words). The quality gate accepts ±10%.

```text
In lesson three, you changed only the random seed of the split, and the test score moved. If one split can be lucky or unlucky, how can you trust a comparison between two models that differ by one hundredth?

Cross-validation gives you a score, and a measure of how much it moves. In k-fold cross-validation, the training data is split into k equal parts, called folds. The model is trained k times. Each time, one fold is held out for scoring, and the others are used for training.

You get k scores, one per fold, and every row is used for scoring exactly once. For classification, use stratified folds, which keep the class balance the same in every fold. This is important when one class is rare.

Always report two numbers: the mean score, and the standard deviation, which shows the spread. If model A scores zero point seven seven, and model B scores zero point seven six, both with a spread of zero point zero five, the difference is smaller than the normal variation. You cannot say A is better.

Cross-validation runs on the training set only. The test set is still kept for one final check. And because you pass a whole pipeline, the preprocessing is refitted inside every fold, which keeps each fold free of leakage.

Judging a student by one exam can be unfair. The questions may happen to suit them, or not. Five short exams on different topics give a better picture, and the gap between the best and worst exam shows how consistent the student is.

Lars Eriksson is an analyst at an energy company in Sweden. He is testing a workflow for predicting which customers will accept a new contract. He practises on the term-deposit data from lesson five.

This cell sets up five stratified folds. Then it builds three pipelines with the same preprocessing and a different model each: logistic regression, a decision tree, and k-nearest neighbours. For each one, it prints the mean ROC AUC across the folds, and the spread.

Logistic regression has the highest mean, zero point seven seven four, with a spread of zero point zero four eight. The tree scores zero point six eight two, with a spread of zero point zero three four. Its lead over the tree, about zero point zero nine, is larger than the spread. That is a real difference.

k-nearest neighbours scores zero point seven three three, with a spread of zero point zero four seven. The lead of logistic regression here is about zero point zero four, smaller than one standard deviation. So Lars writes, probably better, not certain.

Next, this cell shows the individual fold scores for the logistic pipeline, for two metrics at once: ROC AUC and recall.

ROC AUC ranges from zero point seven one eight to zero point eight four three across the folds. A single split could have reported either end. And recall at the default threshold is low in every fold, between zero point zero two seven and zero point one zero eight, which matches lesson eight.

A common mistake is to cross-validate on the full dataset, including the test rows, and then report a test score on those same rows. Another is to preprocess first, and cross-validate only the model. Split off the test set first, and cross-validate the whole pipeline on the training set.

Let's recap. First, k-fold cross-validation trains and scores a model k times, so every training row is scored once, and you should use stratified folds for classification. Second, report the mean and the standard deviation, because differences smaller than the spread are not reliable. Third, cross-validate the whole pipeline on the training set only, and keep the test set for the final check.

Now it is your turn. In the exercise below this video, you will cross-validate three classifiers, put the mean and spread of each in a small table, and decide which model to carry forward. It takes about twenty-five minutes. In the next lesson, Regression Models and Metrics, we move from yes or no to predicting numbers. See you there.
```
