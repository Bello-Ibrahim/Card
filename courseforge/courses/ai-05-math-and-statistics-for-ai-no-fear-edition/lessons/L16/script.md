# L16 Overfitting, Train/Test Splits and Baselines | Presenter Script

Course: AI-05 · Video: 5 min · Words: 688

## Hook
A student memorises every answer in last year's exam and scores one hundred percent on it. Then the real exam has new questions, and the score falls to fifty percent. Models can do exactly the same thing.

## Explain
Last time, we saw how one number can hide a lot. Today: how to catch a model that memorises, and how to tell if a model is worth using at all. When a model fits its training data very closely but fails on new data, that is called overfitting. It learned the noise, not the general pattern. A model too simple to capture the pattern is underfitting.

So never judge a model only on the data it learned from. Use a train and test split. The training set fits the weights. The test set is kept aside, and used only at the end, on examples the model has never seen. A common split is about seventy to eighty percent for training. Shuffle the rows first, so both parts look similar.

Then compare training error and test error. Both low and close together: the model generalises well. Training error very low but test error much higher: overfitting. Both high: underfitting.

Finally, every model needs a baseline: the simplest sensible prediction, which a real model must beat. For numbers, always predict the average of the training targets. For classes, always predict the most common class. If your model does not clearly beat the baseline on the test set, it has not learned anything useful. And remember lesson ten: with a small test set, a small difference may be random variation.

Think of a weather forecaster who always says: tomorrow will be like today. It sounds too simple, but it is right surprisingly often. A new forecasting system is only worth paying for if it clearly beats that rule on days it has never seen.

## Demonstrate
Lucía runs an ice-cream kiosk in Guadalajara, Mexico. She records ten days of temperature and cones sold. All values are invented. She uses the first seven days for training and the last three for testing. With real data, shuffle first.

She compares three approaches. A baseline that always predicts the training mean, about forty-eight point three cones. A simple straight line: sales equals w times temperature plus b. And a wiggly curve, a polynomial of degree six, that can bend through every training point.

In NumPy, poly fit finds the best curve of a chosen degree, and poly val uses it to predict. Lucía calculates the mean squared error on the training days and on the test days.

Here are the results. The baseline's test error is seventy-six point zero three. The straight line: one point eight seven on training, and four point one eight on test. The wiggly curve: zero on training, a perfect score, but thirty point eight nine on test.

The wiggly curve is perfect on training data but much worse on new days. That is overfitting. The straight line beats the baseline clearly, four point one eight against seventy-six point zero three. Lucía chooses the line. But three test days is a very small sample, so she will collect more days before relying on it.

The most common mistake is choosing the model with the lowest training error. That rewards memorising. A quieter mistake is looking at the test set again and again while you adjust the model. Each look lets information leak in, so the test set slowly stops being new. Keep it aside until the end.

## Recap
Let's recap. First, overfitting means very low training error but much higher test error. The model memorised instead of learning. Second, split your data, fit only on the training set, and judge on the test set. Third, every model must clearly beat a simple baseline on the test set, and a small test set means extra caution.

## CTA
Your turn. In the exercise, you split a small study-hours dataset, compare a baseline with a straight line, and decide if it is a real improvement. It takes about thirty minutes. Then the capstone begins. Next: Capstone Build: Linear Regression from Scratch. See you there.

## Thumbnail
Headline: Memorised, Not Learned
Image: Navy background, a wiggly teal curve passing through every dot next to a calm straight line, headline in teal Inter Bold.

## Production Notes
- [VERSION] NumPy: confirm that np.polyfit and np.polyval behave as shown and give no warning for the degree-6 fit in the current NumPy version. Outputs (76.03, 1.87, 4.18, 0.00, 30.89) were checked with NumPy 2.4.
- Lucía and the Guadalajara ice-cream kiosk are fictional; all temperatures and sales are invented. No real ice-cream brands or logos in stock footage.
- Not a screen demo lesson: code appears only on code slides.
- The CTA points ahead to the capstone, which starts in L17.
