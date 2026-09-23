# L03 Fraud Detection: Rules and Models

Course: AI-24 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
A card is used to buy groceries in Lagos. Twenty minutes later, the same card is used to buy a laptop in Singapore. No person can travel that far in twenty minutes. How does a bank notice this in the fraction of a second before it approves the second payment?

## Explanation
Fraud detection systems use two main approaches, and most institutions combine them.

**Rules** are fixed instructions written by fraud analysts. For example: "Block any payment above a set amount from a device the customer has never used." Rules are easy to explain and quick to change. But they only catch patterns someone has already thought of, and criminals learn to stay just below the limits.

**Models** learn patterns from thousands or millions of past transactions labelled "fraud" or "genuine". For each new transaction, the model produces a **risk score**, for example a number from 0 to 1000. Higher scores mean the transaction looks more like past fraud. The score is calculated in a fraction of a second, while the payment is being authorised.

The model combines many signals that a single rule cannot weigh together:

- **Behaviour:** Is this amount normal for this customer? Is this a merchant type they use?
- **Velocity:** How many payments in the last hour? How many different countries?
- **Device and channel:** Is the phone or browser new? Is the card physically present?
- **Location:** Is the distance between two payments possible in the time between them?

The institution then sets actions by score band, for example: approve below 600, ask for extra verification (such as a one-time code) between 600 and 850, and decline above 850. These bands are a business choice, not a feature of the model. L04 looks at how to choose them.

Fraud patterns change. When one method is blocked, criminals try another. A model trained on last year's fraud slowly becomes less accurate. This is called **drift**. Models therefore need new labelled data and regular retraining, and rules are still useful as a fast response to a new attack while the model catches up.

**Analogy:** Rules are like a security guard with a printed list of banned faces. The guard is reliable for people on the list and blind to everyone else. A model is like an experienced guard who has watched the entrance for years and notices when someone's behaviour "feels wrong", even if that person is not on any list. The best entrance has both guards, and the experienced guard still needs to keep learning as new tricks appear.

## Worked Example
Chinedu Okafor is a fraud analyst at a hypothetical card issuer in Lagos, Nigeria. A customer's card makes two payments: a supermarket payment in Lagos at 14:02 and a laptop purchase at a shop in Singapore at 14:22.

A simple rule, "two countries within one hour", flags the second payment. The model also scores it: 930 out of 1000. Its main signals are the impossible travel time, a merchant type the customer has never used, and an amount far above the customer's usual spending. The payment falls in the decline band, and the customer receives a text message asking them to confirm recent activity.

Chinedu then tests three rules on a synthetic sample of 5,000 transactions that includes 40 known fraud cases:

| Rule | Flagged | Fraud among flagged | Share of flags that are fraud |
|---|---|---|---|
| Amount above a high limit | 120 | 12 | 10% |
| New device and foreign country | 60 | 18 | 30% |
| Two countries within one hour | 15 | 11 | about 73% |

The third rule is precise but rare. The first rule creates many false alarms. No single rule catches most of the 40 cases, which is why the issuer also uses a model that combines the signals.

## Common Mistake
Many people think a fraud model "knows" which transactions are fraud. It does not. It gives a score based on how similar a transaction is to past fraud. A genuine customer who travels suddenly or makes an unusual large purchase can receive a high score. That is why the score leads to an action with a human-friendly check, such as a confirmation message, rather than an automatic accusation.

## Key Takeaways
1. Rules catch known patterns and are easy to explain; models combine many signals into a risk score in a fraction of a second.
2. Score bands (approve, verify, decline) are a business decision that sits on top of the model.
3. Fraud patterns change, so models drift and need new labelled data and regular retraining, with rules as a fast backup.

## Hands-on Exercise
**Task:** Write 3 fraud rules, count how many transactions each flags, and compare the flags with the fraud labels.
**Tools:** Google Sheets (free) and the course's synthetic transaction file from L02.
**Steps:**
1. Open the synthetic transaction file. It contains no real customer data.
2. Write 3 rules in plain words, for example "amount above 1,000" or "new device and foreign country".
3. For each rule, add a column with a formula that returns 1 if the rule is true, for example =IF(AND(G2=1,F2<>"NG"),1,0). Adjust the column letters to match your sheet.
4. Use SUM to count the flags for each rule.
5. Use COUNTIFS to count how many flagged rows have is_fraud = 1.
6. Build a small table like Chinedu's: rule, flagged, fraud among flagged, and share of flags that are fraud.
7. Write two sentences: which rule is most useful, and what kind of fraud none of your rules catch.
**What good looks like:** 3 clear rules, correct counts that match the sheet, a comparison table, and an honest note on the fraud your rules miss.
**Time:** about 30 minutes

## Review Flags
- None. The card issuer, analyst and figures are hypothetical and synthetic; score bands are illustrative, not an industry standard.
