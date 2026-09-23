# L08 Bayes' Theorem with Frequency Tables

Course: AI-05 · Module: M2 · Objectives: O3, O5 · Video: 5 min

## Hook
A screening test is correct for 90% of people who have a condition. Your result is positive. What is the chance that you really have the condition? Most people answer "about 90%". In the hypothetical example in this lesson, the true answer is about 15%. By the end, you will be able to show why with simple counting.

## Explanation
**Bayes' theorem** is a rule for updating a belief when new evidence arrives. You start with a **prior**: how likely something is before the evidence. Then you see evidence, such as a positive test. The result is the **posterior**: how likely it is after the evidence.

The formula uses the conditional probabilities from L07:

`P(A | B) = P(B | A) × P(A) / P(B)`

In words: the chance of A given the evidence B equals the chance of seeing B when A is true, times the prior chance of A, divided by the overall chance of seeing B.

You do not need to memorise the formula. There is an easier method that gives the same answer: **imagine a large group of people and count.** Turn every percentage into a number of people, fill in a frequency table, and then read the answer from one column. This is the method we use in this course, and many people find it much easier to trust.

The key lesson is about **rare events**. When the thing you are looking for is rare, most of the people in the large group do not have it. Even a small false-alarm rate applied to that large group can produce more false alarms than true cases.

This matters directly for machine learning. When a model flags something as positive, such as fraud, spam or a fault, the question "what fraction of the flagged cases are really positive?" is exactly this kind of Bayes question. In L15 you will meet it again under the name **precision**.

**Analogy:** Imagine a smoke alarm in a kitchen. Real fires are very rare, but toast burns often. Even a good alarm that almost never misses a fire will ring mostly for toast. When it rings, the chance of a real fire is still low, not because the alarm is bad, but because fires are rare and toast is common.

## Worked Example
Valeria is a hypothetical health data analyst in Lima, Peru. She evaluates a screening test. All numbers are invented for teaching, not real medical statistics:

- 1% of people have the condition (the prior).
- If a person has the condition, the test is positive 90% of the time.
- If a person does not have the condition, the test is still positive 5% of the time (a false alarm).

**Picture and counting:** imagine 10,000 people.

- 1% of 10,000 = 100 people have the condition. 9,900 do not.
- Of the 100 with the condition, 90% test positive: 90 people. 10 are missed.
- Of the 9,900 without it, 5% test positive: 495 people.

| | Test positive | Test negative | Total |
|---|---|---|---|
| Has condition | 90 | 10 | 100 |
| No condition | 495 | 9,405 | 9,900 |
| Total | 585 | 9,415 | 10,000 |

**Hand calculation:** look only at the "Test positive" column. There are 585 positive results, and 90 of them belong to people with the condition. So `P(condition | positive)` = 90 ÷ 585 ≈ 0.154, about 15%.

The formula gives the same answer: 0.9 × 0.01 ÷ 0.0585 ≈ 0.154, because 585 ÷ 10,000 = 0.0585.

**Code:**

```python
n = 10000
has = n * 0.01                 # 100 people
true_pos = has * 0.90          # 90
false_pos = (n - has) * 0.05   # 495
print(true_pos / (true_pos + false_pos))  # about 0.1538
```

A positive result raised the chance from 1% to about 15%. That is a big increase, but most positive results are still false alarms. In practice, a second, different test is often used to confirm. [VERIFY]

## Common Mistake
The classic mistake is confusing `P(positive | condition)`, which is 90%, with `P(condition | positive)`, which is about 15%. This is the same "swapping the sides" mistake from L07, and it is sometimes called ignoring the **base rate**. The base rate is the prior, here 1%. Whenever someone quotes a detection rate, ask: "How common is the thing we are looking for?"

## Key Takeaways
1. Bayes' theorem updates a prior belief into a posterior belief when new evidence arrives.
2. The easiest way to use it is to imagine a large group, turn percentages into counts, and read the answer from a frequency table.
3. When an event is rare, even an accurate test or model can produce more false alarms than true cases.

## Hands-on Exercise
**Task:** Use a frequency table to answer a Bayes question about a hypothetical fraud alert, then check the result with a short NumPy calculation.
**Tools:** Pen and paper; Google Colab with Python (NumPy optional).
**Steps:**
1. A bank's hypothetical fraud alert is used on 10,000 transactions. 0.5% of transactions are fraud. The alert catches 80% of fraud. It also flags 2% of honest transactions.
2. Turn each percentage into a count and fill in a 2 × 2 table with totals.
3. Find how many transactions are flagged in total.
4. Calculate `P(fraud | alert)` from the "flagged" column.
5. Check your answer with a few lines of Python, like the worked example.
6. Write two sentences for a hypothetical bank manager explaining what an alert means.
**What good looks like:** 50 fraud and 9,950 honest transactions; 40 true alerts and 199 false alerts, so 239 alerts in total. `P(fraud | alert)` = 40 ÷ 239 ≈ 0.167, about 17%. Your note explains that most alerts are not fraud because fraud is rare.
**Time:** about 25 minutes

## Review Flags
- The screening test and fraud alert numbers are hypothetical on purpose and must not be presented as real medical or banking statistics (carried from the curriculum flags).
- [VERIFY] The statement that a positive screening result is often followed by a second, different confirmation test is general practice; a reviewer should confirm the wording is suitably general and not medical advice.
