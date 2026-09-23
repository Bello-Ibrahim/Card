# L09 Distributions: Normal and Binomial

Course: AI-05 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
If a model is right 80% of the time, will it get exactly 16 out of 20 test questions right? Sometimes. Sometimes 14, sometimes 19. A distribution tells you how often each result appears, and you can see it for yourself with a few lines of code.

## Explanation
A **distribution** describes how often each possible value appears. The best picture of a distribution is a **histogram**: a bar chart where each bar shows how many values fall into a range.

Two distributions appear again and again in machine learning.

**The normal distribution** describes many measurements that cluster around an average, such as delivery times or the heights of adults. Its histogram is the famous "bell curve": high in the middle and falling away evenly on both sides. It has two settings, called **parameters**:

- the **mean**, which sets the centre of the bell;
- the **standard deviation**, which sets how wide the bell is.

A useful rule of thumb: in a normal distribution, about 68% of values lie within one standard deviation of the mean, and about 95% lie within two.

**The binomial distribution** counts successes in a fixed number of yes-or-no trials, when each trial has the same chance of success. Examples: the number of heads in 10 coin flips, or the number of correct predictions out of 20 test examples. It also has two parameters:

- `n`, the number of trials;
- `p`, the probability of success in each trial.

The average number of successes is `n × p`. For 20 predictions with p = 0.8, the average is 20 × 0.8 = 16. The actual count changes from one test to the next, and the binomial distribution tells you how much.

You rarely need the formulas for these distributions. With NumPy you can **simulate** them: ask the computer to generate thousands of random values and draw the histogram. This "simulate and look" habit is one of the most useful tools in this course.

**Analogy:** A distribution is like the pattern of footprints on a path across a park. Most people walk near the centre of the path, so the grass is most worn there. A few people walk at the edges, and almost nobody walks far away. The pattern of wear shows where people usually go, just as a histogram shows where values usually fall.

## Worked Example
Kofi is a hypothetical machine learning engineer at a logistics start-up in Kumasi, Ghana. He wants to understand two things, using invented settings:

1. If his model is right 80% of the time, how many correct predictions will it make in a test of 20 examples?
2. What do delivery times look like if they average 30 minutes with a standard deviation of 5 minutes?

**Hand calculation:** the average number correct is 20 × 0.8 = 16. For delivery times, one standard deviation either side of 30 is 25 to 35 minutes, so about 68% of times should fall there.

**Code:** a presenter can follow these steps in Colab on screen.

1. Create a new code cell and import NumPy and Matplotlib.
2. Create a random number generator with a fixed **seed** (42), so that the results can be repeated.
3. Simulate 1,000 tests of 20 predictions, and 1,000 delivery times.
4. Print the averages, then draw one histogram at a time.

```python
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(42)
correct = rng.binomial(n=20, p=0.8, size=1000)
times = rng.normal(loc=30, scale=5, size=1000)
print(correct.mean())          # 16.023
print(times.mean().round(2))   # 29.61
plt.hist(correct, bins=range(8, 22))
plt.show()
```

5. Run the cell and point at the histogram. Most tests score 15, 16 or 17, but some score as low as 10 or as high as 20.
6. Replace `correct` with `times` in the `plt.hist` line, remove the `bins` setting and run again. The bell shape appears around 30.

In this run, about 67% of the simulated times fell between 25 and 35 minutes, close to the 68% rule. With a different NumPy version or seed your numbers may differ slightly, but the shapes will look the same. [VERSION]

## Common Mistake
Learners often expect every result to equal the average. They see 14 correct out of 20 and decide that the model has become worse. The histogram shows that 14 is a normal result for a model with an 80% success rate. Random variation is always present. Before you react to one number, ask what range of results the distribution would produce by chance. L10 builds on exactly this idea.

## Key Takeaways
1. A distribution shows how often each value appears, and a histogram is its picture.
2. The normal distribution is a bell shape set by its mean and standard deviation; the binomial distribution counts successes out of `n` trials with success probability `p`, with average `n × p`.
3. You can explore any distribution by simulating many values in NumPy and plotting a histogram.

## Hands-on Exercise
**Task:** Simulate 1,000 coin-flip experiments and 1,000 normal values in Colab, plot histograms, and change one parameter to see how the shape changes.
**Tools:** Google Colab with NumPy and Matplotlib (both available in Colab) [VERSION].
**Steps:**
1. Predict by hand: how many heads, on average, in 10 fair coin flips?
2. Simulate 1,000 experiments of 10 flips with `rng.binomial(n=10, p=0.5, size=1000)`, print the mean and plot a histogram.
3. Simulate 1,000 normal values with a mean and standard deviation of your choice, print the mean and plot a histogram.
4. Change one parameter: for example, set `p=0.9` for the coins or double the standard deviation. Plot again.
5. Write two sentences describing how the shape changed and why.
**What good looks like:** The coin mean is close to 5 and the histogram peaks at 5. Your normal histogram is a bell centred near your chosen mean. Your sentences correctly say, for example, that a larger standard deviation makes the bell wider and flatter, or that `p=0.9` moves the peak towards 9.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Google Colab: confirm current sign-in requirements, free usage limits and the interface before scripting the screen demo (carried from the curriculum flags).
- [VERSION] NumPy random generator: the outputs 16.023 and 29.61 were produced with `default_rng(42)` in NumPy 2.4; confirm they are the same in Colab's current NumPy version, and that Matplotlib is still pre-installed.
