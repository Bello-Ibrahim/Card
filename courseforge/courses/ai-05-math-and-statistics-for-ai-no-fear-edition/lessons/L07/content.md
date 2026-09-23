# L07 Probability and Conditional Probability

Course: AI-05 · Module: M2 · Objectives: O1, O3 · Video: 5 min

## Hook
An email arrives with the word "prize" in the subject line. Is it spam? You probably feel "very likely", but how likely, exactly? With one small table and some counting, you can put a number on that feeling.

## Explanation
**Probability** measures how likely an event is, on a scale from 0 to 1. A probability of 0 means it never happens, 1 means it always happens, and 0.5 means it happens half of the time. You can also write it as a percentage: 0.2 is 20%.

When you have counts, probability is simply a fraction. In words: the number of times the event happens, divided by the total number of cases. We write the probability of an event A as `P(A)`, read "the probability of A".

**Joint probability** is the chance that two things are both true, such as "spam **and** contains 'prize'". We write it `P(A and B)`.

**Conditional probability** is the chance that something is true when we already know that something else is true. We write it `P(A | B)`. The vertical line is read "given". So `P(spam | prize)` means "the probability that an email is spam, given that it contains 'prize'".

In words, the rule is: **only look at the cases where B is true, and ask what fraction of them also have A.** As a formula: `P(A | B) = count(A and B) / count(B)`.

A **two-way frequency table** makes all of this visible. The rows show one question (spam or not) and the columns show another (contains "prize" or not). Every cell is a count. To find a conditional probability, you choose one row or one column and ignore the rest.

Machine learning uses this constantly. A classifier's output, such as "85% likely to be spam", is a conditional probability: the chance of a class **given** the features it sees.

**Analogy:** Conditional probability is like using a filter in a spreadsheet. You first filter the table to show only the rows where B is true. Then you count how many of the visible rows also have A. Everything that was filtered out no longer matters.

## Worked Example
Aigerim is a hypothetical data analyst for an email service in Almaty, Kazakhstan. She takes a sample of 1,000 labelled emails. All counts below are invented for the example.

| | Contains "prize" | No "prize" | Total |
|---|---|---|---|
| Spam | 60 | 140 | 200 |
| Not spam | 20 | 780 | 800 |
| Total | 80 | 920 | 1,000 |

**Picture:** 1,000 small squares, with 200 coloured red for spam. Among them, 60 red squares and 20 grey squares have a star for "prize".

**Hand calculation:**

- `P(spam)` = 200 ÷ 1,000 = 0.2
- `P(prize)` = 80 ÷ 1,000 = 0.08
- `P(spam and prize)` = 60 ÷ 1,000 = 0.06
- `P(spam | prize)`: look only at the "Contains prize" column. It has 80 emails, and 60 are spam. So 60 ÷ 80 = 0.75.
- `P(prize | spam)`: look only at the "Spam" row. It has 200 emails, and 60 contain "prize". So 60 ÷ 200 = 0.3.

Knowing that an email contains "prize" raises the chance of spam from 0.2 to 0.75. But only 30% of spam emails contain "prize", so this word alone would miss most spam.

**Code:**

```python
import numpy as np
# rows: spam, not spam; columns: prize, no prize
t = np.array([[60, 140],
              [20, 780]])
print(t[0].sum() / t.sum())          # P(spam) = 0.2
print(t[0, 0] / t[:, 0].sum())       # P(spam | prize) = 0.75
print(t[0, 0] / t[0].sum())          # P(prize | spam) = 0.3
```

## Common Mistake
The most common mistake is swapping the two sides of the line: treating `P(spam | prize)` and `P(prize | spam)` as the same thing. They are different questions with different answers, 0.75 and 0.3 here. The first divides by the number of "prize" emails, and the second divides by the number of spam emails. Before you divide, always say in words which group you are looking inside. That group gives the number at the bottom of the fraction.

## Key Takeaways
1. Probability is a number from 0 to 1; with counts, it is the number of matching cases divided by the total.
2. `P(A | B)` means "the probability of A given B": look only at the cases where B is true and find the fraction that also have A.
3. `P(A | B)` and `P(B | A)` are usually different, because they divide by different groups.

## Hands-on Exercise
**Task:** Fill in a two-way frequency table for a hypothetical dataset and calculate three probabilities and two conditional probabilities.
**Tools:** Pen and paper or a free spreadsheet; Google Colab with NumPy.
**Steps:**
1. An online shop has 500 hypothetical orders. 100 were delivered late and 400 on time. Of the late orders, 30 were returned. Of the on-time orders, 40 were returned.
2. Draw a table with rows "Late" and "On time", columns "Returned" and "Kept", and a total row and column. Fill in every cell.
3. Calculate `P(late)`, `P(returned)` and `P(late and returned)`.
4. Calculate `P(returned | late)` and `P(returned | on time)`. For each, write in words which group you are looking inside.
5. Put the four inner counts into a NumPy array and check your answers.
6. Write one sentence on what the two conditional probabilities suggest about late deliveries.
**What good looks like:** Kept counts of 70 and 360; `P(late)` = 0.2, `P(returned)` = 0.14, `P(late and returned)` = 0.06, `P(returned | late)` = 0.3 and `P(returned | on time)` = 0.1. NumPy agrees, and your sentence says late orders were returned three times as often in this data.
**Time:** about 25 minutes

## Review Flags
- None. All counts and probabilities are hypothetical and were recalculated; no tool interface or external fact needs checking.
