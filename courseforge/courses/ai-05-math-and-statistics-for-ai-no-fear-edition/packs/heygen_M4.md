# HeyGen Batch Pack: AI-05 M4 (Metrics and the Capstone)

Course: Math and Statistics for AI (No-Fear Edition). Make one HeyGen video per lesson below, using these settings for every video.

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

## L15 Classification Metrics: Confusion Matrix, Precision and Recall

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M4_L15_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
A fraud detector is ninety-nine percent accurate. Impressive? Now imagine a detector that never flags anything at all. In our hypothetical example, it is also ninety-nine percent accurate. One number can hide a lot.

This is the final module, and you have come a long way. This lesson shows you how to see what one number hides. A classifier predicts a category, like fraud or not fraud. The class we are looking for is called positive. Positive does not mean good. It means the thing we are searching for.

Every prediction falls into one of four groups. A true positive: predicted fraud, and it was fraud. A false positive: predicted fraud, but it was honest, a false alarm. A false negative: predicted honest, but it was fraud, a miss. And a true negative: predicted honest, and it was honest. Together they make a two by two table, the confusion matrix.

Three metrics come from it. Accuracy is the fraction of all predictions that were correct. Precision asks: of everything the model flagged, what fraction was really positive? That is the Bayes question from lesson eight. Recall asks: of all the real positives, what fraction did the model find?

Accuracy misleads when one class is rare. This is called class imbalance. And precision and recall usually pull against each other. Flag more cases, and you catch more fraud, but raise more false alarms. Which one matters more depends on the cost of each mistake. In other tasks, the balance can be the opposite.

Think of fishing with a net. Recall asks: of all the fish in the lake, how many did my net catch? Precision asks: of everything in my net, how much is fish, and how much is old boots? A huge net catches many fish, but also many boots.

Farhana is a risk analyst at a mobile payments company in Dhaka, Bangladesh. She tests a new fraud detector on ten thousand transactions. All numbers are invented for teaching. One hundred transactions are fraud, and nine thousand nine hundred are honest.

Here is her confusion matrix. Twenty true positives. Eighty frauds were missed. Twenty false alarms. And nine thousand eight hundred and eighty true negatives. Accuracy is twenty plus nine thousand eight hundred and eighty, divided by ten thousand. That is zero point nine nine, or ninety-nine percent.

Precision is twenty divided by twenty plus twenty, which is zero point five. Half of the alerts are real fraud. Recall is twenty divided by twenty plus eighty, which is zero point two. The detector finds only twenty percent of the fraud.

Now compare a lazy model that always predicts honest. It has zero true positives, one hundred misses, zero false alarms, and nine thousand nine hundred true negatives. Its accuracy is also ninety-nine percent, but its recall is zero. The ninety-nine percent hides that the real detector misses eighty of one hundred frauds.

Farhana reports recall first, because each missed fraud is costly. Missing fraud may cost a lot of money, while a false alarm may only annoy a customer. She asks the team to improve it, while watching that precision does not fall too far.

A common mistake is to judge a classifier by accuracy alone. With imbalanced data, build the confusion matrix first, and compare with an always predict the common class baseline. And remember: precision divides by everything predicted positive. Recall divides by everything actually positive.

Let's recap. First, a confusion matrix counts true positives, false positives, false negatives and true negatives. Second, precision tells you how many alerts are real, and recall tells you how many real cases you found. Third, accuracy can hide poor performance when one class is rare, so compare with a common-class baseline and choose metrics by the cost of each mistake.

Your turn. In the exercise, you build a confusion matrix from twenty hypothetical predictions, calculate the three metrics in NumPy, and decide which one matters most for fraud. Take your time with the counting. It takes about twenty-five minutes. Next: Overfitting, Train and Test Splits, and Baselines. See you there.
```

## L16 Overfitting, Train/Test Splits and Baselines

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M4_L16_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.

```text
A student memorises every answer in last year's exam and scores one hundred percent on it. Then the real exam has new questions, and the score falls to fifty percent. Models can do exactly the same thing.

Last time, we saw how one number can hide a lot. Today: how to catch a model that memorises, and how to tell if a model is worth using at all. When a model fits its training data very closely but fails on new data, that is called overfitting. It learned the noise, not the general pattern. A model too simple to capture the pattern is underfitting.

So never judge a model only on the data it learned from. Use a train and test split. The training set fits the weights. The test set is kept aside, and used only at the end, on examples the model has never seen. A common split is about seventy to eighty percent for training. Shuffle the rows first, so both parts look similar.

Then compare training error and test error. Both low and close together: the model generalises well. Training error very low but test error much higher: overfitting. Both high: underfitting.

Finally, every model needs a baseline: the simplest sensible prediction, which a real model must beat. For numbers, always predict the average of the training targets. For classes, always predict the most common class. If your model does not clearly beat the baseline on the test set, it has not learned anything useful. And remember lesson ten: with a small test set, a small difference may be random variation.

Think of a weather forecaster who always says: tomorrow will be like today. It sounds too simple, but it is right surprisingly often. A new forecasting system is only worth paying for if it clearly beats that rule on days it has never seen.

Lucía runs an ice-cream kiosk in Guadalajara, Mexico. She records ten days of temperature and cones sold. All values are invented. She uses the first seven days for training and the last three for testing. With real data, shuffle first.

She compares three approaches. A baseline that always predicts the training mean, about forty-eight point three cones. A simple straight line: sales equals w times temperature plus b. And a wiggly curve, a polynomial of degree six, that can bend through every training point.

In NumPy, poly fit finds the best curve of a chosen degree, and poly val uses it to predict. Lucía calculates the mean squared error on the training days and on the test days.

Here are the results. The baseline's test error is seventy-six point zero three. The straight line: one point eight seven on training, and four point one eight on test. The wiggly curve: zero on training, a perfect score, but thirty point eight nine on test.

The wiggly curve is perfect on training data but much worse on new days. That is overfitting. The straight line beats the baseline clearly, four point one eight against seventy-six point zero three. Lucía chooses the line. But three test days is a very small sample, so she will collect more days before relying on it.

The most common mistake is choosing the model with the lowest training error. That rewards memorising. A quieter mistake is looking at the test set again and again while you adjust the model. Each look lets information leak in, so the test set slowly stops being new. Keep it aside until the end.

Let's recap. First, overfitting means very low training error but much higher test error. The model memorised instead of learning. Second, split your data, fit only on the training set, and judge on the test set. Third, every model must clearly beat a simple baseline on the test set, and a small test set means extra caution.

Your turn. In the exercise, you split a small study-hours dataset, compare a baseline with a straight line, and decide if it is a real improvement. It takes about thirty minutes. Then the capstone begins. Next: Capstone Build: Linear Regression from Scratch. See you there.
```

## L17 Capstone Build: Linear Regression from Scratch

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M4_L17_presenter.mp4`
- **Expected length:** about 5.0 minutes (699 words). The quality gate accepts ±10%.

```text
Four weeks ago, a page of maths symbols may have made you nervous. Today you will build a working machine learning model yourself. And every line uses an idea you have already calculated by hand.

Linear regression predicts a number as a weighted sum of features, plus a bias. For one feature, y equals w times x plus b. Here is how the whole course fits together, in five steps.

One, data as a matrix. Each row of X is one example, and we add a first column of ones, so the bias becomes just another weight. Two, predictions with matrix multiplication: X at w makes one prediction per row. Three, the loss: the error is prediction minus truth, and the loss is the mean squared error.

Four, the gradient. For all weights at once, it is two over n, times X transpose, at the error. In words: for each weight, multiply every error by that weight's feature, add them up, and scale by two over n. Five, gradient descent: predict, measure the error, calculate the gradient, and step against it. Repeat.

Shapes are your safety check. With ten training rows and three columns, X train is ten by three, and w has three numbers. X train at w gives ten predictions. X train transpose is three by ten, and times the error it gives three numbers, one gradient value per weight.

Here is the capstone brief. Implement linear regression with NumPy only, on the dataset provided. Train it with gradient descent, plot the loss falling, and keep five rows as a test set for the next lesson. It is like flat-pack furniture: every part is one you have already inspected.

Baraka runs a cold-drink kiosk in Mombasa, Kenya. For fifteen invented days he has hours of sunshine, foot traffic in hundreds of people, and drinks sold, which he wants to predict. The first ten days are for training, and the last five are the test set.

In Colab, add a text cell called Data, then the data cell. It holds the three columns, then builds X with a column of ones in front. Check the shape: fifteen by three. Then split it into ten training rows and five test rows.

Before any code runs, a hand check. All weights start at zero, so every first prediction is zero. The first loss is the mean of the squared sales of the ten training days, about three thousand two hundred and eighty-four point seven.

Now a text cell called Training, and the loop. The learning rate is zero point zero one, for five thousand steps. Each step calculates the error, prediction minus truth. It saves the mean squared error. It calculates the gradient. And it steps downhill. Four lines, four ideas you already know.

Run it. The weights are about two point zero two for the bias, three point seven five drinks per hour of sunshine, and six point five three drinks per hundred people passing. The loss falls from three thousand two hundred and eighty-four point seven to five point nine one. Steep, then flat.

One more test. Change the learning rate to zero point zero two and run again. The loss explodes, and NumPy prints overflow warnings. That is divergence, from lesson fourteen. Change it back.

The most common capstone mistake is forgetting the column of ones. Then there is no bias, and the fit is worse. The second is reversing the error, truth minus prediction. The gradient gets the wrong sign, and the loss grows. Keep prediction minus truth.

Let's recap. First, linear regression is X at w: a dot product of features and weights for every row, with a column of ones for the bias. Second, training repeats four lines: predict, find the error, calculate the gradient, and step against it. Third, check the shapes, check the first loss by hand, and plot the loss curve.

This is capstone step one. Build your own notebook with the provided data, comment every line of the loop, and plot your loss curve. Give yourself about sixty minutes. In the final lesson, we check, interpret and document your model, in Capstone Explain: Check, Interpret and Document. See you there.
```

## L18 Capstone Explain: Check, Interpret and Document

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M4_L18_presenter.mp4`
- **Expected length:** about 5.0 minutes (690 words). The quality gate accepts ±10%.

```text
Your model has trained, and the loss has fallen. But are the weights right, and what do they mean? A model you cannot check or explain is not finished. In this final lesson, you will prove your result and explain it clearly.

Finishing the capstone takes four steps. Step one: check the weights. Linear regression is special, because its best weights can also be calculated directly, without a loop. NumPy's least squares function does this. If your loop's weights match it to about two decimal places, your loop is correct.

Step two: interpret each weight. A weight is the change in the prediction when its feature goes up by one, and the other features stay the same. The bias is the prediction when every feature is zero. That may not be realistic, so use it with care.

Step three: compare with a baseline on the test set. Calculate training error, test error, and the test error of always predicting the training mean. Report R M S E too, because it is in real units. Step four: judge and document. How many test examples are there? Could the difference be random? Then add a plain-language text cell before every code cell.

Checking with least squares is like checking a long division on a calculator. You still did the work yourself, and you understand each step. A second method just confirms you made no small slip.

Back to Baraka's kiosk notebook in Colab. Add a text cell called Check with least squares, and run least squares on the training data. The first result is a list of values, and we keep only the weights. They are two point zero two, three point seven five and six point five three.

Then n p dot all close compares both sets of weights, and prints True. They match to better than zero point zero zero one. Your loop was correct.

Now a text cell called Evaluate. Using the m s e function, the training error is five point nine one. The test error is eleven point two. And the baseline on the test set is three hundred and forty-eight point zero one.

In real units, that is an R M S E of about three drinks on the test days, against about nineteen for the baseline. Now the weights, all hypothetical. With the same foot traffic, each extra hour of sunshine is linked to about three point seven five more drinks. With the same sunshine, each extra hundred people passing is linked to about six point five more.

The bias, about two point zero two, is the prediction for a day with no sun and no passers-by. No such day is in the data, so Baraka does not rely on it. And the largest miss is the test day with eighty-one drinks, where the model predicted about eighty-eight.

Baraka writes his judgement in a text cell. The gain over the baseline is very large, so it is unlikely to be random. But there are only five test days, so: promising, but check again after one more month of data. The weights show links in this data, not proof that sunshine causes sales.

A common mistake is saying the model is ninety-six percent better, without saying better than what, on which data, and with how many examples. Always name the metric, the data, the baseline and the sample size. And never describe a weight as a cause.

Let's recap. First, confirm your gradient descent weights with least squares. Matching weights prove the loop is correct. Second, each weight is the change in prediction for one extra unit of its feature, with the others fixed. It shows a link, not a cause. Third, report training error, test error and a baseline together, with R M S E and a note on sample size.

Congratulations. You may have started this course nervous about symbols, and you have built and explained a real model from scratch. Now finish capstone step two, check your notebook against the rubric and the submission checklist, run it from the top, and submit it. I am proud of what you have done. Well done.
```
