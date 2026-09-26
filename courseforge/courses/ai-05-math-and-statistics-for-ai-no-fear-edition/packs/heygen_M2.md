# HeyGen Batch Pack: AI-05 M2 (Probability and Statistics)

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

## L06 Describing Data: Mean, Median and Spread

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M2_L06_presenter.mp4`
- **Expected length:** about 5.0 minutes (702 words). The quality gate accepts ±10%.

```text
Five people work in a small team. Four of them earn about the same, and one earns six times more. Someone says: the average income in this team is ten thousand. Is that true? Yes. Is it fair? Not really.

Now we begin Module 2, probability and statistics. Before you train any model, you describe your data with a few numbers. They answer two questions. Where is the centre of the data? And how spread out is it?

First, the centre. The mean is the ordinary average: add all the values, and divide by how many there are. The median is the middle value after you sort the data. With an even number of values, it is the mean of the two middle ones.

The mean uses every value, so one very large or very small value, called an outlier, can pull it a long way. The median only cares about the middle position, so outliers hardly move it.

Now the spread. The variance measures how far values are from the mean, on average. Find each distance from the mean, square it, then take the mean of those squares. Squaring makes every distance positive, and makes big distances count more. The standard deviation is the square root of the variance, so it is in the same units as the data.

In NumPy, you use mean, median, var and std. One detail: n p dot std divides by the number of values, n. Some tools divide by n minus one instead, which gives a slightly larger answer for a sample. Both are correct. Just be consistent.

Here is a picture. The mean is like the balance point of a see-saw. If one very heavy person sits at the far end, the balance point moves a long way. The median is like the person in the middle of a queue sorted by height. The tallest person does not change who stands in the middle.

Kwame leads a team of five at a software company in Accra, Ghana. Their monthly incomes, in thousands of Ghana cedis, are invented for this example: four, five, five, six and thirty. The last one belongs to a senior partner.

Picture a dot plot. Four dots sit close together near five, and one dot sits far away at thirty. Now the centre. Four plus five plus five plus six plus thirty is fifty, and fifty divided by five is ten. That is the mean. Sorted, the middle value is five. That is the median.

The mean of ten is higher than what four of the five people earn. The median of five describes a typical team member much better.

Now the spread. Subtract the mean of ten from each value: minus six, minus five, minus five, minus four, and twenty. Square them: thirty-six, twenty-five, twenty-five, sixteen and four hundred. They add up to five hundred and two. Divide by five, and the variance is one hundred point four. The standard deviation is about ten point zero two.

Without the senior partner, the values four, five, five and six have a mean of five, a variance of zero point five, and a standard deviation of about zero point seven one. One value changed the spread enormously. And in NumPy, the four functions give the same results as our hand calculation for the full team.

A common mistake is to report only the mean, and assume it is typical. With incomes, house prices or delivery times, the mean can mislead. Always look at the median and the standard deviation too, and draw a quick plot.

Let's recap. First, the mean is the sum divided by the count, and the median is the middle sorted value, which resists outliers. Second, the variance is the mean of the squared distances from the mean, and the standard deviation is its square root, in the original units. Third, always report centre and spread together, and compare mean and median to spot outliers.

Your turn. In the exercise, you take ten delivery times, find the mean, median and standard deviation by hand, check them in NumPy, then add an outlier and watch what changes. It takes about twenty-five minutes. Next: Probability and Conditional Probability. See you there.
```

## L07 Probability and Conditional Probability

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M2_L07_presenter.mp4`
- **Expected length:** about 5.0 minutes (696 words). The quality gate accepts ±10%.
- **Pronunciation:** No facts to verify: content.md Review Flags say None. All counts and probabilities are hypothetical. Say P(spam | prize) as 'the probability of spam, given prize'; the slides show the notation.

```text
An email arrives with the word prize in the subject line. Is it spam? You probably feel: very likely. But how likely, exactly? With one small table and some counting, you can put a number on that feeling.

Last time, we described data with a few numbers. Today we measure how likely things are. Probability is a number from zero to one. Zero means it never happens, one means it always happens, and zero point five means half of the time. You can also say zero point two is twenty percent.

When you have counts, probability is simply a fraction: the number of times the event happens, divided by the total number of cases. We write P of A, the probability of A. Joint probability is the chance that two things are both true, like spam and contains prize.

Conditional probability is the chance that something is true, when we already know something else is true. We write P of A, a vertical line, then B. The line is read as given. The rule in words: look only at the cases where B is true, and ask what fraction of them also have A.

A two-way frequency table makes this visible. The rows answer one question, spam or not. The columns answer another, contains prize or not. Machine learning uses this all the time. When a classifier says eighty-five percent likely to be spam, that is a conditional probability: the chance of a class, given the features it sees.

Here is an easy way to picture it. Conditional probability is like a filter in a spreadsheet. First you filter the table to show only the rows where B is true. Then you count how many visible rows also have A. Everything filtered out no longer matters.

Aigerim is a data analyst for an email service in Almaty, Kazakhstan. She takes a sample of one thousand labelled emails. All the counts are invented for the example.

Two hundred emails are spam, and eight hundred are not. Of the spam emails, sixty contain prize and one hundred and forty do not. Of the other emails, twenty contain prize and seven hundred and eighty do not. So eighty emails in total contain prize.

First, the simple ones. The probability of spam is two hundred divided by one thousand, which is zero point two. The probability of prize is eighty divided by one thousand, zero point zero eight. The probability of spam and prize is sixty divided by one thousand, zero point zero six.

Now the conditional ones. Spam given prize: look only at the prize column. It has eighty emails, and sixty are spam. Sixty divided by eighty is zero point seven five. Prize given spam: look only at the spam row. It has two hundred emails, and sixty contain prize. Sixty divided by two hundred is zero point three.

So knowing that an email contains prize raises the chance of spam from zero point two to zero point seven five. But only thirty percent of spam contains prize, so this word alone would miss most spam. In NumPy, Aigerim puts the four inner counts in an array and gets the same three answers.

The most common mistake is swapping the two sides of the line. Spam given prize and prize given spam are different questions, with different answers: zero point seven five and zero point three. Before you divide, say in words which group you are looking inside. That group goes at the bottom of the fraction.

Let's recap. First, probability is a number from zero to one, and with counts it is matching cases divided by the total. Second, P of A given B means: look only at the cases where B is true, and find the fraction that also have A. Third, A given B and B given A are usually different, because they divide by different groups.

Your turn. In the exercise, you fill in a table for five hundred online orders, late or on time, returned or kept, and calculate five probabilities. It takes about twenty-five minutes. Next, we use these tables to update beliefs, in Bayes' Theorem with Frequency Tables. See you there.
```

## L08 Bayes' Theorem with Frequency Tables

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.

```text
A screening test is correct for ninety percent of people who have a condition. Your result is positive. What is the chance you really have it? Most people say about ninety percent. In our hypothetical example, the answer is about fifteen percent.

Don't worry. By the end of this lesson, you will see why, with simple counting. Bayes' theorem is a rule for updating a belief when new evidence arrives. You start with a prior: how likely something is before the evidence. Then you see evidence, like a positive test. The result is the posterior: how likely it is after.

The formula uses the conditional probabilities from the last lesson. In words: the chance of A given evidence B equals the chance of B when A is true, times the prior chance of A, divided by the overall chance of B. You do not need to memorise it.

There is an easier method that gives the same answer. Imagine a large group of people, and count. Turn every percentage into a number of people, fill in a frequency table, then read the answer from one column. Many people find this much easier to trust.

The key lesson is about rare events. When something is rare, most people in the group do not have it. So even a small false-alarm rate on that big group can produce more false alarms than true cases. In machine learning, when a model flags fraud or spam, what fraction of the flags are real? That is a Bayes question, and in lesson fifteen we call it precision.

Think of a kitchen smoke alarm. Real fires are very rare, but toast burns often. Even a good alarm that almost never misses a fire will ring mostly for toast. Not because the alarm is bad, but because fires are rare and toast is common.

Valeria is a health data analyst in Lima, Peru. She evaluates a screening test. The numbers are invented for teaching. One percent of people have the condition. If they have it, the test is positive ninety percent of the time. If they do not, it is still positive five percent of the time.

Now imagine ten thousand people. One percent is one hundred people with the condition, and nine thousand nine hundred without. Of the one hundred, ninety percent test positive: ninety people. Ten are missed. Of the nine thousand nine hundred, five percent test positive: four hundred and ninety-five people.

Here is the table. Look only at the test positive column. There are five hundred and eighty-five positive results, and only ninety belong to people with the condition. Ninety divided by five hundred and eighty-five is about zero point one five four. About fifteen percent.

The formula agrees. Zero point nine times zero point zero one, divided by zero point zero five eight five, is about zero point one five four. In Python, a few lines calculate the true positives and false positives, and print about zero point one five three eight.

A positive result raised the chance from one percent to about fifteen percent. That is a big increase, but most positive results are still false alarms.

The classic mistake is confusing positive given condition, which is ninety percent, with condition given positive, which is about fifteen percent. This is sometimes called ignoring the base rate. So whenever someone quotes a detection rate, ask: how common is the thing we are looking for?

Let's recap. First, Bayes' theorem updates a prior belief into a posterior belief when new evidence arrives. Second, the easiest way to use it is to imagine a large group, turn percentages into counts, and read the answer from a table. Third, when an event is rare, even an accurate test or model can produce more false alarms than true cases.

Your turn. In the exercise, you use a frequency table for a hypothetical bank fraud alert on ten thousand transactions, and check your answer in Python. Take your time with the counting, because the counting is the whole trick. It takes about twenty-five minutes. Next: Distributions, Normal and Binomial. See you there.
```

## L09 Distributions: Normal and Binomial

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M2_L09_presenter.mp4`
- **Expected length:** about 4.9 minutes (670 words). The quality gate accepts ±10%.

```text
If a model is right eighty percent of the time, will it get exactly sixteen out of twenty test questions right? Sometimes. Sometimes fourteen, sometimes nineteen. A distribution tells you how often each result appears, and you can see it yourself with code.

In the last lesson, we counted people in a table. Today we look at the shape of data. A distribution describes how often each possible value appears. Its best picture is a histogram: a bar chart where each bar shows how many values fall into a range.

The normal distribution describes many measurements that cluster around an average, like delivery times or adult heights. Its histogram is the famous bell curve. It has two settings, called parameters. The mean sets the centre of the bell, and the standard deviation sets how wide it is.

A useful rule of thumb: in a normal distribution, about sixty-eight percent of values lie within one standard deviation of the mean, and about ninety-five percent lie within two.

The binomial distribution counts successes in a fixed number of yes-or-no trials, when each trial has the same chance. Like heads in ten coin flips, or correct predictions out of twenty. Its parameters are n, the number of trials, and p, the chance of success. The average is n times p. For twenty predictions with p equal to zero point eight, that is sixteen.

You rarely need the formulas. With NumPy, you can simulate: generate thousands of random values and draw the histogram. Picture footprints on a path across a park. Most people walk near the centre, so the grass is most worn there. A histogram shows where values usually fall, in the same way.

Kofi is a machine learning engineer at a logistics start-up in Kumasi, Ghana. His settings are invented. If his model is right eighty percent of the time, the average number correct out of twenty is sixteen. And if delivery times average thirty minutes with a standard deviation of five, about sixty-eight percent should fall between twenty-five and thirty-five minutes.

Let's check in Colab. In a new code cell, Kofi imports NumPy and Matplotlib, the plotting library. Then he creates a random number generator with a fixed seed, forty-two, so the results can be repeated.

Next, he simulates one thousand tests of twenty predictions with p of zero point eight, and one thousand delivery times with a mean of thirty and a standard deviation of five. He prints both averages. In this run, the number correct averages sixteen point zero two three, and the times average twenty-nine point six one.

Now he plots a histogram of the correct counts. Most tests score fifteen, sixteen or seventeen. But some score as low as ten, or as high as twenty.

Then he swaps correct for times, removes the bins setting, and runs again. The bell shape appears around thirty. In this run, about sixty-seven percent of the times fell between twenty-five and thirty-five minutes, close to the sixty-eight percent rule.

A common mistake is to expect every result to equal the average. You see fourteen correct out of twenty, and decide the model got worse. But the histogram shows that fourteen is normal for a model with an eighty percent success rate. Before you react to one number, ask what range chance would produce.

Let's recap. First, a distribution shows how often each value appears, and a histogram is its picture. Second, the normal distribution is a bell set by its mean and standard deviation, and the binomial counts successes out of n trials, with average n times p. Third, you can explore any distribution by simulating values in NumPy and plotting a histogram.

Your turn. In the exercise, you simulate one thousand coin-flip experiments and one thousand normal values in Colab, plot them, and change one parameter to see the shape move. There is no hurry, so play with the numbers and enjoy watching the shapes change. It takes about twenty-five minutes. Next: Samples, Uncertainty and Meaningful Differences. See you there.
```

## L10 Samples, Uncertainty and Meaningful Differences

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_M2_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (676 words). The quality gate accepts ±10%.
- **Pronunciation:** No facts to verify: content.md Review Flags say None. The simulation outputs (0.035, 0.0035, 0.313, 0.0, range 72% to 96%) were produced with NumPy 2.4 and default_rng(0).

```text
Your new model scores eighty-seven percent accuracy. The old one scored eighty-five. Time to celebrate? Maybe not. If you tested on only one hundred examples, the old model could reach eighty-seven percent on a lucky day, too.

This lesson gives you a simple way to know when a difference is real. A test set is a sample: a small part of all the examples the model will ever see. The accuracy you measure is an estimate of the true accuracy, its accuracy on all possible examples. You can never measure that directly.

Because the test set is a sample, the score contains random variation. A different sample of one hundred examples would give a slightly different score, just as the coin experiments in the last lesson did not always give exactly five heads.

How big is this variation? It depends mainly on the sample size. With a small test set, the score jumps around a lot. With a large one, it stays close to the true accuracy. To make the variation ten times smaller, you need about one hundred times more examples. So going from one hundred to ten thousand makes it about ten times smaller.

So here is the practical rule for this course. Compare the size of a difference with the size of the random variation. If a two-point gain is smaller than the normal ups and downs of the score, you cannot claim the new model is better.

Statisticians have formal tools for this, but we use simulation, because you can see the variation directly. Think of judging a restaurant from one meal. One great or poor dinner can happen by chance. After one hundred meals, you know much more reliably. The food did not change. Your evidence did.

Ananya is a data scientist at an insurance company in Pune, India. Her current model has a true accuracy of eighty-five percent. We know that because, in this invented example, we set it. A colleague's new model scores eighty-seven percent on one hundred claims. Is that a real improvement?

She pretends to test the current model one thousand times, first on test sets of one hundred examples, then of ten thousand. Each test is a binomial experiment from the last lesson, with every example correct with probability zero point eight five. Dividing by n turns the count into an accuracy.

Now the results. With one hundred examples, the standard deviation is about zero point zero three five, or three point five percentage points. The scores ranged from seventy-two to ninety-six percent. With ten thousand examples, it is about zero point three five points. That is ten times smaller, just as the square-root pattern predicts.

And the key number: the old model reached eighty-seven percent or more in about thirty-one percent of the small tests, purely by chance. In the large tests, it never did.

So on one hundred examples, a two-point difference is well inside normal variation, and Ananya cannot say the new model is better. On ten thousand examples, the same difference would be very convincing. She asks for a larger test set before she decides.

A common mistake is to report a single score as if it were exact, and compare models by tiny differences. Always ask two questions. How many test examples was this measured on? And how much would the score move by chance? A quick simulation answers the second in seconds.

Let's recap. First, a test score is measured on a sample, so it always includes random variation around the true value. Second, larger test sets give much steadier scores: about one hundred times more examples makes the variation about ten times smaller. Third, a difference is meaningful only when it is clearly larger than the normal random variation.

Great work: that completes Module 2. In the exercise, you simulate your own model on one hundred and on ten thousand examples, plot both, and write a short note for a manager. It takes about twenty-five minutes. Next, we start calculus, gently, with Functions, Slopes and Derivatives. See you there.
```
