# L09 Distributions: Normal and Binomial | Presenter Script

Course: AI-05 · Video: 5 min · Words: 686

## Hook
If a model is right eighty percent of the time, will it get exactly sixteen out of twenty test questions right? Sometimes. Sometimes fourteen, sometimes nineteen. A distribution tells you how often each result appears, and you can see it yourself with code.

## Explain
In the last lesson, we counted people in a table. Today we look at the shape of data. A distribution describes how often each possible value appears. Its best picture is a histogram: a bar chart where each bar shows how many values fall into a range.

The normal distribution describes many measurements that cluster around an average, like delivery times or adult heights. Its histogram is the famous bell curve. It has two settings, called parameters. The mean sets the centre of the bell, and the standard deviation sets how wide it is.

A useful rule of thumb: in a normal distribution, about sixty-eight percent of values lie within one standard deviation of the mean, and about ninety-five percent lie within two.

The binomial distribution counts successes in a fixed number of yes-or-no trials, when each trial has the same chance. Like heads in ten coin flips, or correct predictions out of twenty. Its parameters are n, the number of trials, and p, the chance of success. The average is n times p. For twenty predictions with p equal to zero point eight, that is sixteen.

You rarely need the formulas. With NumPy, you can simulate: generate thousands of random values and draw the histogram. Picture footprints on a path across a park. Most people walk near the centre, so the grass is most worn there. A histogram shows where values usually fall, in the same way.

## Demonstrate
Kofi is a machine learning engineer at a logistics start-up in Kumasi, Ghana. His settings are invented. If his model is right eighty percent of the time, the average number correct out of twenty is sixteen. And if delivery times average thirty minutes with a standard deviation of five, about sixty-eight percent should fall between twenty-five and thirty-five minutes.

Let's check in Colab. In a new code cell, Kofi imports NumPy and Matplotlib, the plotting library. Then he creates a random number generator with a fixed seed, forty-two, so the results can be repeated.

Next, he simulates one thousand tests of twenty predictions with p of zero point eight, and one thousand delivery times with a mean of thirty and a standard deviation of five. He prints both averages. In this run, the number correct averages sixteen point zero two three, and the times average twenty-nine point six one.

Now he plots a histogram of the correct counts. Most tests score fifteen, sixteen or seventeen. But some score as low as ten, or as high as twenty.

Then he swaps correct for times, removes the bins setting, and runs again. The bell shape appears around thirty. In this run, about sixty-seven percent of the times fell between twenty-five and thirty-five minutes, close to the sixty-eight percent rule.

A common mistake is to expect every result to equal the average. You see fourteen correct out of twenty, and decide the model got worse. But the histogram shows that fourteen is normal for a model with an eighty percent success rate. Before you react to one number, ask what range chance would produce.

## Recap
Let's recap. First, a distribution shows how often each value appears, and a histogram is its picture. Second, the normal distribution is a bell set by its mean and standard deviation, and the binomial counts successes out of n trials, with average n times p. Third, you can explore any distribution by simulating values in NumPy and plotting a histogram.

## CTA
Your turn. In the exercise, you simulate one thousand coin-flip experiments and one thousand normal values in Colab, plot them, and change one parameter to see the shape move. There is no hurry, so play with the numbers and enjoy watching the shapes change. It takes about twenty-five minutes. Next: Samples, Uncertainty and Meaningful Differences. See you there.

## Thumbnail
Headline: Why Results Wobble
Image: Navy background, a teal bell-shaped histogram next to a bar histogram peaking at 16, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Colab: confirm current sign-in requirements, free usage limits and the interface before recording the screen scenes.
- [VERSION] NumPy random generator: the outputs 16.023 and 29.61 and the 'about 67%' share were produced with default_rng(42) in NumPy 2.4. Confirm they are the same in Colab's current NumPy version, and that Matplotlib is still pre-installed. If they differ, update the on-screen numbers and the voiceover in scenes 9 and 11.
- Kofi and the Kumasi logistics start-up are fictional; the 80% accuracy and the 30-minute, 5-minute delivery settings are invented.
- The 68% and 95% figures are the standard rule of thumb for normal distributions.
