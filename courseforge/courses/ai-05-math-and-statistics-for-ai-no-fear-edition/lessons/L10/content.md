# L10 Samples, Uncertainty and Meaningful Differences

Course: AI-05 · Module: M2 · Objectives: O6 · Video: 5 min

## Hook
Your new model scores 87% accuracy. The old one scored 85%. Time to celebrate? Maybe not. If you tested on only 100 examples, the old model could reach 87% on a lucky day, too. This lesson gives you a simple way to know when a difference is real.

## Explanation
A **test set** is a **sample**: a small part of all the examples the model will ever see. The accuracy you measure on it is an estimate of the model's **true accuracy**, which is its accuracy on all possible examples. You can never measure the true accuracy directly.

Because the test set is a sample, the measured score contains **random variation**. A different sample of 100 examples would give a slightly different score, just as the coin experiments in L09 did not always give exactly 5 heads.

How big is this variation? It depends mainly on the **sample size**, the number of test examples.

- With a small test set, the measured accuracy jumps around a lot.
- With a large test set, it stays close to the true accuracy.

There is a useful pattern: to make the variation 10 times smaller, you need about 100 times more examples. In words, the variation shrinks with the square root of the sample size. So going from 100 to 10,000 examples (100 times more) makes the variation about 10 times smaller.

The practical rule for this course: **compare the size of a difference with the size of the random variation.** If a 2-point improvement is smaller than the normal ups and downs of the score, you cannot claim that the new model is better. If it is much larger, the evidence is convincing.

Statisticians have formal tools for this, such as confidence intervals and hypothesis tests. In this course we use simulation instead, because you can see the variation directly and it needs no new formulas.

**Analogy:** Judging a model on 100 test examples is like judging a restaurant from one meal. One excellent or poor dinner can happen by chance. After 100 meals, you know much more reliably whether the restaurant is good. The food did not change; your evidence did.

## Worked Example
Ananya is a hypothetical data scientist at an insurance company in Pune, India. Her current model has a true accuracy of 85% (in this invented example, we know the true value because we set it). A colleague's new model scores 87% on a test set of 100 claims. Is that a real improvement?

**Picture:** two histograms of measured accuracy, one wide and one narrow, both centred at 85%.

**Simulation:** she pretends to test the current model 1,000 times on new test sets, first with 100 examples each and then with 10,000 each. Each test is a binomial experiment from L09: `n` examples, each correct with probability 0.85. Dividing by `n` turns the count into an accuracy.

```python
import numpy as np
rng = np.random.default_rng(0)
small = rng.binomial(n=100, p=0.85, size=1000) / 100
large = rng.binomial(n=10000, p=0.85, size=1000) / 10000
print(small.std().round(3), large.std().round(4))  # 0.035 0.0035
print(np.mean(small >= 0.87))  # 0.313
print(np.mean(large >= 0.87))  # 0.0
```

**Reading the results:**

- With 100 examples, the standard deviation of measured accuracy is about 0.035, or 3.5 percentage points. The scores ranged from 72% to 96%.
- With 10,000 examples, it is about 0.0035, or 0.35 points: 10 times smaller, as the square-root pattern predicts.
- The **old** model reached 87% or more in about 31% of the small tests, purely by chance. In the large tests, it never did.

**Conclusion:** on 100 examples, a 2-point difference is well inside normal variation, so Ananya cannot say the new model is better. On 10,000 examples, the same 2-point difference would be very convincing. She asks for a larger test set before making a decision.

## Common Mistake
Many people report a single score, such as "87%", as if it were exact. Then they compare models by very small differences, sometimes changing the model because of noise. Always ask two questions: "How many test examples was this measured on?" and "How much would the score move by chance?" A quick simulation answers the second question in a few seconds.

## Key Takeaways
1. A test score is measured on a sample, so it always includes random variation around the true value.
2. Larger test sets give much steadier scores: about 100 times more examples makes the variation about 10 times smaller.
3. A difference is meaningful only when it is clearly larger than the normal random variation of the score.

## Hands-on Exercise
**Task:** Simulate a model with a fixed true accuracy tested on 100 and on 10,000 examples many times, and compare how much the measured accuracy varies.
**Tools:** Google Colab with NumPy and Matplotlib.
**Steps:**
1. Choose a true accuracy between 0.7 and 0.95.
2. Simulate 1,000 test sets of 100 examples and 1,000 test sets of 10,000 examples, as in the worked example.
3. Print the minimum, maximum and standard deviation of each set of scores.
4. Plot both histograms. Use `plt.hist(small, alpha=0.5)` and then `plt.hist(large, alpha=0.5)` so that both are visible.
5. Choose a score 2 points above your true accuracy and calculate how often each test size reaches it by chance.
6. Write three sentences for a hypothetical manager: what you found, and how many test examples you would recommend.
**What good looks like:** The small-test scores spread over a wide range and the large-test scores over a narrow one, with a standard deviation about 10 times smaller. Your note explains in plain words why a 2-point gain on 100 examples is not enough evidence.
**Time:** about 25 minutes

## Review Flags
- None. All accuracies are hypothetical, and the simulation outputs shown were produced with NumPy 2.4 and `default_rng(0)`.
- Judgement call carried from the curriculum: this lesson teaches uncertainty through simulation and only names confidence intervals and hypothesis tests without teaching p-values; a reviewer may want a short additional mention.
