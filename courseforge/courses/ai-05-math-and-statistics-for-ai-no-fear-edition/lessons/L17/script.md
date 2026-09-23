# L17 Capstone Build: Linear Regression from Scratch | Presenter Script

Course: AI-05 · Video: 5 min · Words: 703

## Hook
Four weeks ago, a page of maths symbols may have made you nervous. Today you will build a working machine learning model yourself. And every line uses an idea you have already calculated by hand.

## Explain
Linear regression predicts a number as a weighted sum of features, plus a bias. For one feature, y equals w times x plus b. Here is how the whole course fits together, in five steps.

One, data as a matrix. Each row of X is one example, and we add a first column of ones, so the bias becomes just another weight. Two, predictions with matrix multiplication: X at w makes one prediction per row. Three, the loss: the error is prediction minus truth, and the loss is the mean squared error.

Four, the gradient. For all weights at once, it is two over n, times X transpose, at the error. In words: for each weight, multiply every error by that weight's feature, add them up, and scale by two over n. Five, gradient descent: predict, measure the error, calculate the gradient, and step against it. Repeat.

Shapes are your safety check. With ten training rows and three columns, X train is ten by three, and w has three numbers. X train at w gives ten predictions. X train transpose is three by ten, and times the error it gives three numbers, one gradient value per weight.

Here is the capstone brief. Implement linear regression with NumPy only, on the dataset provided. Train it with gradient descent, plot the loss falling, and keep five rows as a test set for the next lesson. It is like flat-pack furniture: every part is one you have already inspected.

## Demonstrate
Baraka runs a cold-drink kiosk in Mombasa, Kenya. For fifteen invented days he has hours of sunshine, foot traffic in hundreds of people, and drinks sold, which he wants to predict. The first ten days are for training, and the last five are the test set.

In Colab, add a text cell called Data, then the data cell. It holds the three columns, then builds X with a column of ones in front. Check the shape: fifteen by three. Then split it into ten training rows and five test rows.

Before any code runs, a hand check. All weights start at zero, so every first prediction is zero. The first loss is the mean of the squared sales of the ten training days, about three thousand two hundred and eighty-four point seven.

Now a text cell called Training, and the loop. The learning rate is zero point zero one, for five thousand steps. Each step calculates the error, prediction minus truth. It saves the mean squared error. It calculates the gradient. And it steps downhill. Four lines, four ideas you already know.

Run it. The weights are about two point zero two for the bias, three point seven five drinks per hour of sunshine, and six point five three drinks per hundred people passing. The loss falls from three thousand two hundred and eighty-four point seven to five point nine one. Steep, then flat.

One more test. Change the learning rate to zero point zero two and run again. The loss explodes, and NumPy prints overflow warnings. That is divergence, from lesson fourteen. Change it back.

The most common capstone mistake is forgetting the column of ones. Then there is no bias, and the fit is worse. The second is reversing the error, truth minus prediction. The gradient gets the wrong sign, and the loss grows. Keep prediction minus truth.

## Recap
Let's recap. First, linear regression is X at w: a dot product of features and weights for every row, with a column of ones for the bias. Second, training repeats four lines: predict, find the error, calculate the gradient, and step against it. Third, check the shapes, check the first loss by hand, and plot the loss curve.

## CTA
This is capstone step one. Build your own notebook with the provided data, comment every line of the loop, and plot your loss curve. Give yourself about sixty minutes. In the final lesson, we check, interpret and document your model, in Capstone Explain: Check, Interpret and Document. See you there.

## Thumbnail
Headline: Build It From Scratch
Image: Navy background, a teal loss curve falling steeply then flattening, with a notebook cell outline behind it, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Colab: confirm current sign-in requirements, free usage limits and the interface before recording the screen scenes.
- [VERSION] NumPy: confirm that a learning rate of 0.02 still produces overflow RuntimeWarning messages (scene 12), and that all outputs shown (weights 2.02, 3.75, 6.53; loss 3,284.7 to 5.91) match the current Colab NumPy version. Outputs were checked with NumPy 2.4.
- Baraka and the Mombasa cold-drink kiosk are fictional; the 15 days of data are invented.
- The presenter describes the code in words; the screen shows every line. Type at a readable speed or use a pre-typed cell revealed line by line.
