# L04 False Alarms and Missed Fraud: The Cost Trade-off

Course: AI-24 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
A fraud model that blocks every payment catches all the fraud. It also stops every honest customer from buying anything. Where exactly should the line be drawn, and who pays for each mistake?

## Explanation
Every fraud model makes two kinds of error.

- A **false positive** is a false alarm: a genuine payment is blocked or delayed. The customer is embarrassed at the till, may call the contact centre, and may move to another bank. The institution pays for the call, the lost payment fee and, over time, the lost customer.
- A **false negative** is missed fraud: a fraudulent payment is approved. The institution or the customer loses the money, and there are investigation and chargeback costs.

A **confusion matrix** puts all outcomes in one table:

| | Model says "fraud" | Model says "genuine" |
|---|---|---|
| **Actually fraud** | True positive (caught) | False negative (missed) |
| **Actually genuine** | False positive (false alarm) | True negative (correct approval) |

The model gives a risk score, and the institution picks a **threshold**: any score above it is treated as fraud. Moving the threshold changes both errors at the same time. A strict (low) threshold flags more payments, so it catches more fraud but creates more false alarms. A relaxed (high) threshold creates fewer false alarms but misses more fraud. You cannot reduce both errors just by moving the threshold. Only a better model or better data does that.

So the right threshold depends on **costs**, not only on accuracy. A simple method is: total cost = (missed fraud × cost of one missed fraud) + (false alarms × cost of one false alarm). Then compare the totals.

**Analogy:** A threshold is like the sensitivity setting on a smoke alarm. Set it very sensitive and it will warn you about every real fire, and also every time you make toast. Set it less sensitive and the toast is quiet, but a small fire may be missed. The right setting depends on what a false alarm costs you and what a missed fire costs you.

## Worked Example
Marta Kowalska is a risk manager at a hypothetical payments company in Warsaw, Poland. She studies a synthetic set of 10,000 card payments. Of these, 50 are fraud. She compares two thresholds.

| Threshold | Fraud caught | Fraud missed | False alarms |
|---|---|---|---|
| Strict | 45 | 5 | 400 |
| Relaxed | 35 | 15 | 100 |

She uses an average loss of 300 (in the company's currency) for each missed fraud. The cost of a false alarm is less certain, so she tests two assumptions.

**Assumption A: a false alarm costs 5** (a short automated message and a small chance of a support call).
- Strict: 5 × 300 + 400 × 5 = 1,500 + 2,000 = **3,500**
- Relaxed: 15 × 300 + 100 × 5 = 4,500 + 500 = **5,000**

**Assumption B: a false alarm costs 20** (a blocked payment at the till, a call and some risk of losing the customer).
- Strict: 5 × 300 + 400 × 20 = 1,500 + 8,000 = **9,500**
- Relaxed: 15 × 300 + 100 × 20 = 4,500 + 2,000 = **6,500**

Under assumption A, the strict threshold is cheaper. Under assumption B, the relaxed threshold is cheaper. The model has not changed. Only the business assumption has changed. Marta's recommendation to her committee therefore starts with the cost assumptions, and she asks the customer experience team for better evidence on the true cost of a false alarm.

## Common Mistake
Many teams choose the threshold with the highest "accuracy". In fraud, this is misleading. With 50 fraud cases in 10,000 payments, a model that approves every payment is 99.5% accurate and catches no fraud at all. Always look at the two error types separately, and put a cost on each. Also remember that false alarms may not fall evenly on all customers. L06 and L07 look at that question.

## Key Takeaways
1. False positives block genuine customers; false negatives let fraud through. Both have real costs for the institution and the customer.
2. Moving the threshold trades one error for the other; only a better model or better data reduces both.
3. Choose the threshold by comparing total costs under clear, stated cost assumptions, not by accuracy alone.

## Hands-on Exercise
**Task:** Calculate the total cost per 10,000 transactions at two thresholds under two cost assumptions, and choose a threshold.
**Tools:** Google Sheets (free) and the course's synthetic confusion-matrix sheet.
**Steps:**
1. Open the confusion-matrix sheet. It contains synthetic scores and labels only.
2. Enter a threshold in the input cell and note the counts of caught fraud, missed fraud and false alarms that the sheet calculates.
3. Repeat for a second threshold.
4. In a new table, enter a cost for one missed fraud and two different costs for one false alarm.
5. Calculate the total cost for each threshold under each assumption, using the formula from this lesson.
6. Write one sentence on which threshold you would choose and why, naming the cost assumption you trust more.
**What good looks like:** Four correct cost totals, a clear link between the assumption and the choice, and a sentence that mentions the customer impact of false alarms, not only money.
**Time:** about 25 minutes

## Review Flags
- None. The company, counts and cost figures are hypothetical and synthetic; all calculations have been checked.
