# L02 Financial Data: What Models Learn From | Presenter Script

Course: AI-24 · Video: 5 min · Words: 690

## Hook
Two teams build a fraud model with the same software. One model works well. The other fails in its first month. The difference is not the algorithm. It is the data each team gave it.

## Explain
In the last lesson, we mapped five families of AI use cases. Every one of them depends on data. So today we look at what models learn from, and why data quality usually matters more than the choice of model.

In finance, there are four main types of data. Transactions: the amount, time, merchant, channel, location and device. Credit bureau records: existing loans, repayment history and missed payments. Alternative data, such as mobile airtime top-ups or utility bills. And text, such as complaints and call notes.

Each type has its own risks. Alternative data needs the customer's consent where required, and careful checks for fairness. Text often contains personal details that must be protected.

Each example has features and, for most finance models, a label. Features are the inputs the model looks at, such as amount or time of day. The label is the answer it must learn to predict, such as fraud or not fraud, repaid or defaulted.

Labels in finance are hard to get. A fraudulent card payment may look normal on the day. It is labelled as fraud only weeks later, when the real cardholder disputes it and a chargeback is completed. So the newest data often has incomplete labels, and some fraud is never reported at all.

Then there are data quality problems. Missing values. Duplicates, where the same transaction is recorded twice. Inconsistent formats, like two currencies in one column. Impossible values. And leakage: a column that contains the answer, such as a chargeback date, which only exists after fraud is known.

Think of a model as a trainee analyst who learns only from the files on their desk. If half the files are missing pages, some are copies of each other, and the answers are written on the cover, the trainee will learn the wrong lessons, however intelligent they are.

## Demonstrate
Let's see this with Nguyen Thi Lan. She is a data analyst at a hypothetical payments fintech in Ho Chi Minh City, Vietnam. She opens a synthetic sample of two thousand card transactions.

First, she gives each column a role. The transaction ID is an identifier, not a feature. Time, amount, currency, merchant category, country and a new-device flag are possible features. Is fraud is the label. And chargeback date is leakage, because it is only filled in after fraud is confirmed.

Next, she sorts and filters the sheet, and finds three problems. Some amounts are in Vietnamese dong and some in US dollars, in the same column. Fourteen rows appear twice with the same transaction ID. And merchant category is blank in about one row in twenty.

She also notices that transactions from the last three weeks have almost no fraud labels. That is not because they are safe. It is because disputes have not arrived yet. So she leaves the most recent weeks out of the training data, and will use them later, once the labels mature.

A common mistake is to believe more columns always make a better model. Extra columns can add leakage, missing values, or personal data you do not need. If a value is only known after the event, it cannot be a feature.

## Recap
Let's recap. First, finance models learn from transactions, credit bureau records, alternative data and text, and each type has its own uses and risks. Second, labels such as fraud or default arrive late and can be incomplete, so the newest data needs special care. Third, check for missing values, duplicates, mixed formats, impossible values and leakage before you trust any model.

## CTA
Now it is your turn. In the exercise below this video, you will open the synthetic transaction file in Google Sheets. Mark each column as a feature, the label, an identifier or leakage, and find three data quality problems, each with a practical fix. It takes about twenty-five minutes. In the next lesson, we look at fraud detection, with rules and models. See you there.

## Thumbnail
Headline: Data Beats the Algorithm
Image: Navy background, a spreadsheet grid with one column highlighted in teal as the label and one struck through in red as leakage, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the company, analyst and dataset are hypothetical and synthetic; the lesson makes no statistical or legal claims (content.md Review Flags: None).
- Nguyen Thi Lan and her payments fintech in Ho Chi Minh City are fictional. The on-screen table must use the synthetic column names from content.md only.
- Pronunciation: Nguyen Thi Lan (roughly 'nwen tee lan'); VND is spoken as 'Vietnamese dong'.
