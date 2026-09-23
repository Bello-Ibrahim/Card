# L08 Bayes' Theorem with Frequency Tables | Presenter Script

Course: AI-05 · Video: 5 min · Words: 690

## Hook
A screening test is correct for ninety percent of people who have a condition. Your result is positive. What is the chance you really have it? Most people say about ninety percent. In our hypothetical example, the answer is about fifteen percent.

## Explain
Don't worry. By the end of this lesson, you will see why, with simple counting. Bayes' theorem is a rule for updating a belief when new evidence arrives. You start with a prior: how likely something is before the evidence. Then you see evidence, like a positive test. The result is the posterior: how likely it is after.

The formula uses the conditional probabilities from the last lesson. In words: the chance of A given evidence B equals the chance of B when A is true, times the prior chance of A, divided by the overall chance of B. You do not need to memorise it.

There is an easier method that gives the same answer. Imagine a large group of people, and count. Turn every percentage into a number of people, fill in a frequency table, then read the answer from one column. Many people find this much easier to trust.

The key lesson is about rare events. When something is rare, most people in the group do not have it. So even a small false-alarm rate on that big group can produce more false alarms than true cases. In machine learning, when a model flags fraud or spam, what fraction of the flags are real? That is a Bayes question, and in lesson fifteen we call it precision.

Think of a kitchen smoke alarm. Real fires are very rare, but toast burns often. Even a good alarm that almost never misses a fire will ring mostly for toast. Not because the alarm is bad, but because fires are rare and toast is common.

## Demonstrate
Valeria is a health data analyst in Lima, Peru. She evaluates a screening test. The numbers are invented for teaching. One percent of people have the condition. If they have it, the test is positive ninety percent of the time. If they do not, it is still positive five percent of the time.

Now imagine ten thousand people. One percent is one hundred people with the condition, and nine thousand nine hundred without. Of the one hundred, ninety percent test positive: ninety people. Ten are missed. Of the nine thousand nine hundred, five percent test positive: four hundred and ninety-five people.

Here is the table. Look only at the test positive column. There are five hundred and eighty-five positive results, and only ninety belong to people with the condition. Ninety divided by five hundred and eighty-five is about zero point one five four. About fifteen percent.

The formula agrees. Zero point nine times zero point zero one, divided by zero point zero five eight five, is about zero point one five four. In Python, a few lines calculate the true positives and false positives, and print about zero point one five three eight.

A positive result raised the chance from one percent to about fifteen percent. That is a big increase, but most positive results are still false alarms.

The classic mistake is confusing positive given condition, which is ninety percent, with condition given positive, which is about fifteen percent. This is sometimes called ignoring the base rate. So whenever someone quotes a detection rate, ask: how common is the thing we are looking for?

## Recap
Let's recap. First, Bayes' theorem updates a prior belief into a posterior belief when new evidence arrives. Second, the easiest way to use it is to imagine a large group, turn percentages into counts, and read the answer from a table. Third, when an event is rare, even an accurate test or model can produce more false alarms than true cases.

## CTA
Your turn. In the exercise, you use a frequency table for a hypothetical bank fraud alert on ten thousand transactions, and check your answer in Python. Take your time with the counting, because the counting is the whole trick. It takes about twenty-five minutes. Next: Distributions, Normal and Binomial. See you there.

## Thumbnail
Headline: Positive Test, Only 15%?
Image: Navy background, a crowd of 100 small figures with a few highlighted in teal and many in grey inside a 'positive' box, headline in teal Inter Bold.

## Production Notes
- All screening test and fraud alert numbers are hypothetical on purpose and must not be presented as real medical or banking statistics. Keep the on-screen label 'hypothetical numbers' on scenes 7 to 10.
- [VERIFY] Left out of the voiceover: content.md says a positive screening result is often followed by a second, different confirmation test. A reviewer should confirm suitably general wording before it is added anywhere; it must not read as medical advice.
- Valeria and the Lima health data team are fictional. Stock footage must not show real patients, readable medical records or hospital logos.
- Not a screen demo lesson: code appears only on a code slide.
