# L02 Financial Data: What Models Learn From

Course: AI-24 · Module: M1 · Objectives: O1, O2 · Video: 5 min

## Hook
Two teams build a fraud model with the same software. One model works well; the other fails in its first month. The difference is not the algorithm. It is the data each team gave it.

## Explanation
A model learns patterns from past examples. In finance, those examples come from four main types of data.

- **Transactions:** amount, time, merchant, channel (card, transfer, mobile money), location and device. This is the core data for fraud detection and for understanding customer behaviour.
- **Credit bureau records:** existing loans, repayment history, missed payments and recent applications. This is the core data for traditional credit scoring.
- **Alternative data:** records outside the usual credit file, such as mobile airtime top-ups, utility bill payments or rent. It can help lenders assess people with little credit history, but it needs the customer's consent where required and careful checks for fairness.
- **Text:** complaints, chat messages, call notes and reports. Language models can read this, but it often contains personal details that must be protected.

Each example has **features** (the inputs the model looks at, such as amount or time of day) and, for most finance models, a **label** (the answer the model must learn to predict, such as "fraud" or "not fraud", or "repaid" or "defaulted").

Labels in finance are hard to get. A fraudulent card payment may look normal on the day. It is labelled as fraud only weeks later, when the real cardholder disputes it and a chargeback is completed. A loan is labelled "defaulted" only after months of missed payments. So the most recent data often has incomplete labels, and some fraud is never reported at all.

Data quality usually matters more than the choice of model. Common problems are:

- **Missing values:** blank fields, for example no merchant category.
- **Duplicates:** the same transaction recorded twice.
- **Inconsistent formats:** dates written in different ways, or amounts in different currencies in one column.
- **Impossible values:** negative ages or a payment time of 25:70.
- **Leakage:** a column that contains the answer, such as "chargeback date", which only exists after fraud is known.

**Analogy:** A model is like a trainee analyst who learns only from the files on their desk. If half the files are missing pages, some are copies of each other, and the answers are written on the cover, the trainee will learn the wrong lessons, however intelligent they are.

## Worked Example
Nguyen Thi Lan is a data analyst at a hypothetical payments fintech in Ho Chi Minh City, Vietnam. She opens a synthetic sample of 2,000 card transactions with these columns:

| Column | Role |
|---|---|
| transaction_id | Identifier, not a feature |
| timestamp, amount, currency, merchant_category, country, device_new | Possible features |
| is_fraud | Label |
| chargeback_date | Leakage: it is only filled in after fraud is confirmed |

She sorts and filters the sheet and finds three problems. Some amounts are in VND and some in USD in the same column, so a large number is not always a large payment. Fourteen rows appear twice with the same transaction ID. And "merchant_category" is blank in about one row in twenty.

She also notices that transactions from the last three weeks have almost no fraud labels. That is not because they are safe. It is because disputes have not arrived yet. She decides to leave the most recent weeks out of the training data and to use them later, once the labels mature.

## Common Mistake
Many learners believe that a model with more columns is always better. Adding columns can add leakage, more missing values, or personal data that the model does not need. Keep only the features that make sense for the decision, that you are allowed to use, and that are available at the moment of the decision. If a value is only known after the event, it cannot be a feature.

## Key Takeaways
1. Finance models learn from transactions, credit bureau records, alternative data and text; each type has its own uses and risks.
2. Labels such as "fraud" or "default" arrive late and can be incomplete, so the newest data needs special care.
3. Check for missing values, duplicates, mixed formats, impossible values and leakage before you trust any model.

## Hands-on Exercise
**Task:** Identify features, the label and data quality problems in a synthetic transaction dataset.
**Tools:** Google Sheets (free) and the course's synthetic transaction file.
**Steps:**
1. Open the synthetic transaction file in Google Sheets. It contains no real customer data.
2. Add a row above the headers and label each column "feature", "label", "identifier" or "leakage".
3. Use Data > Create a filter to look for blank cells in each column.
4. Sort by transaction ID and look for duplicate rows.
5. Check the amount and currency columns for mixed currencies or impossible values.
6. Write down 3 data quality problems, where you found them, and how you would fix each one.
**What good looks like:** "is_fraud" is marked as the label, "chargeback_date" is marked as leakage, and your 3 problems each have a location (column and example row) and a practical fix.
**Time:** about 25 minutes

## Review Flags
- None. The company, analyst and dataset are hypothetical and synthetic; the lesson makes no statistical or legal claims.
