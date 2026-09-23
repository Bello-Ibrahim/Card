# L18 Capstone Explain: Check, Interpret and Document | Presenter Script

Course: AI-05 · Video: 5 min · Words: 696

## Hook
Your model has trained, and the loss has fallen. But are the weights right, and what do they mean? A model you cannot check or explain is not finished. In this final lesson, you will prove your result and explain it clearly.

## Explain
Finishing the capstone takes four steps. Step one: check the weights. Linear regression is special, because its best weights can also be calculated directly, without a loop. NumPy's least squares function does this. If your loop's weights match it to about two decimal places, your loop is correct.

Step two: interpret each weight. A weight is the change in the prediction when its feature goes up by one, and the other features stay the same. The bias is the prediction when every feature is zero. That may not be realistic, so use it with care.

Step three: compare with a baseline on the test set. Calculate training error, test error, and the test error of always predicting the training mean. Report R M S E too, because it is in real units. Step four: judge and document. How many test examples are there? Could the difference be random? Then add a plain-language text cell before every code cell.

Checking with least squares is like checking a long division on a calculator. You still did the work yourself, and you understand each step. A second method just confirms you made no small slip.

## Demonstrate
Back to Baraka's kiosk notebook in Colab. Add a text cell called Check with least squares, and run least squares on the training data. The first result is a list of values, and we keep only the weights. They are two point zero two, three point seven five and six point five three.

Then n p dot all close compares both sets of weights, and prints True. They match to better than zero point zero zero one. Your loop was correct.

Now a text cell called Evaluate. Using the m s e function, the training error is five point nine one. The test error is eleven point two. And the baseline on the test set is three hundred and forty-eight point zero one.

In real units, that is an R M S E of about three drinks on the test days, against about nineteen for the baseline. Now the weights, all hypothetical. With the same foot traffic, each extra hour of sunshine is linked to about three point seven five more drinks. With the same sunshine, each extra hundred people passing is linked to about six point five more.

The bias, about two point zero two, is the prediction for a day with no sun and no passers-by. No such day is in the data, so Baraka does not rely on it. And the largest miss is the test day with eighty-one drinks, where the model predicted about eighty-eight.

Baraka writes his judgement in a text cell. The gain over the baseline is very large, so it is unlikely to be random. But there are only five test days, so: promising, but check again after one more month of data. The weights show links in this data, not proof that sunshine causes sales.

A common mistake is saying the model is ninety-six percent better, without saying better than what, on which data, and with how many examples. Always name the metric, the data, the baseline and the sample size. And never describe a weight as a cause.

## Recap
Let's recap. First, confirm your gradient descent weights with least squares. Matching weights prove the loop is correct. Second, each weight is the change in prediction for one extra unit of its feature, with the others fixed. It shows a link, not a cause. Third, report training error, test error and a baseline together, with R M S E and a note on sample size.

## CTA
Congratulations. You may have started this course nervous about symbols, and you have built and explained a real model from scratch. Now finish capstone step two, check your notebook against the rubric and the submission checklist, run it from the top, and submit it. I am proud of what you have done. Well done.

## Thumbnail
Headline: Prove It, Explain It
Image: Navy background, two matching rows of weights with a teal tick between them, headline in teal Inter Bold.

## Production Notes
- [VERSION] NumPy: confirm that np.linalg.lstsq with rcond=None returns four values, gives no warning, and matches the outputs shown (weights 2.02, 3.75, 6.53; MSE 5.91, 11.2, 348.01) in the current Colab NumPy version. Outputs were checked with NumPy 2.4.
- [VERSION] Google Colab: confirm the interface for adding text cells and running all cells before recording the screen scenes.
- Baraka and the Mombasa kiosk data are hypothetical. Weight interpretations must stay worded as links, not causes.
- The CTA points learners to the capstone rubric and submission checklist (capstone_rubric.md).
