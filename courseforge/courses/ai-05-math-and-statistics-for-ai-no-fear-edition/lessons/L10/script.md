# L10 Samples, Uncertainty and Meaningful Differences | Presenter Script

Course: AI-05 · Video: 5 min · Words: 689

## Hook
Your new model scores eighty-seven percent accuracy. The old one scored eighty-five. Time to celebrate? Maybe not. If you tested on only one hundred examples, the old model could reach eighty-seven percent on a lucky day, too.

## Explain
This lesson gives you a simple way to know when a difference is real. A test set is a sample: a small part of all the examples the model will ever see. The accuracy you measure is an estimate of the true accuracy, its accuracy on all possible examples. You can never measure that directly.

Because the test set is a sample, the score contains random variation. A different sample of one hundred examples would give a slightly different score, just as the coin experiments in the last lesson did not always give exactly five heads.

How big is this variation? It depends mainly on the sample size. With a small test set, the score jumps around a lot. With a large one, it stays close to the true accuracy. To make the variation ten times smaller, you need about one hundred times more examples. So going from one hundred to ten thousand makes it about ten times smaller.

So here is the practical rule for this course. Compare the size of a difference with the size of the random variation. If a two-point gain is smaller than the normal ups and downs of the score, you cannot claim the new model is better.

Statisticians have formal tools for this, but we use simulation, because you can see the variation directly. Think of judging a restaurant from one meal. One great or poor dinner can happen by chance. After one hundred meals, you know much more reliably. The food did not change. Your evidence did.

## Demonstrate
Ananya is a data scientist at an insurance company in Pune, India. Her current model has a true accuracy of eighty-five percent. We know that because, in this invented example, we set it. A colleague's new model scores eighty-seven percent on one hundred claims. Is that a real improvement?

She pretends to test the current model one thousand times, first on test sets of one hundred examples, then of ten thousand. Each test is a binomial experiment from the last lesson, with every example correct with probability zero point eight five. Dividing by n turns the count into an accuracy.

Now the results. With one hundred examples, the standard deviation is about zero point zero three five, or three point five percentage points. The scores ranged from seventy-two to ninety-six percent. With ten thousand examples, it is about zero point three five points. That is ten times smaller, just as the square-root pattern predicts.

And the key number: the old model reached eighty-seven percent or more in about thirty-one percent of the small tests, purely by chance. In the large tests, it never did.

So on one hundred examples, a two-point difference is well inside normal variation, and Ananya cannot say the new model is better. On ten thousand examples, the same difference would be very convincing. She asks for a larger test set before she decides.

A common mistake is to report a single score as if it were exact, and compare models by tiny differences. Always ask two questions. How many test examples was this measured on? And how much would the score move by chance? A quick simulation answers the second in seconds.

## Recap
Let's recap. First, a test score is measured on a sample, so it always includes random variation around the true value. Second, larger test sets give much steadier scores: about one hundred times more examples makes the variation about ten times smaller. Third, a difference is meaningful only when it is clearly larger than the normal random variation.

## CTA
Great work: that completes Module 2. In the exercise, you simulate your own model on one hundred and on ten thousand examples, plot both, and write a short note for a manager. It takes about twenty-five minutes. Next, we start calculus, gently, with Functions, Slopes and Derivatives. See you there.

## Thumbnail
Headline: Is 87% Really Better?
Image: Navy background, a wide histogram and a narrow histogram both centred on 85%, headline in teal Inter Bold.

## Production Notes
- No facts to verify: content.md Review Flags say None. The simulation outputs (0.035, 0.0035, 0.313, 0.0, range 72% to 96%) were produced with NumPy 2.4 and default_rng(0).
- Judgement call carried from the curriculum: the lesson names confidence intervals and hypothesis tests but does not teach p-values. A reviewer may want a short extra mention.
- Ananya and the Pune insurance company are fictional; all accuracies are hypothetical. No real insurer logos in stock footage.
- Not a screen demo lesson: the simulation appears on a code slide, not as a live notebook.
