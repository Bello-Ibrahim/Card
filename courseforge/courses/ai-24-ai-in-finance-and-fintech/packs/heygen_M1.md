# HeyGen Batch Pack: AI-24 M1 (Where AI Fits in Finance)

Course: AI in Finance and Fintech. Make one HeyGen video per lesson below, using these settings for every video.

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

## L01 The AI Map of Financial Services

- **Filename:** `ai-24-ai-in-finance-and-fintech_M1_L01_presenter.mp4`
- **Expected length:** about 5.3 minutes (733 words). The quality gate accepts ±10%.

```text
A customer opens an account on her phone, pays a supplier, applies for a loan, asks a question at midnight, and repays on time. At how many of those steps did an AI system look at her data? The answer can be every one.

Hello, and welcome to AI in Finance and Fintech. In this first lesson, we draw a map. Where does AI actually fit inside a financial institution, and what data does each use depend on?

AI in finance is not one product. It is a set of tools that support different steps of the value chain. In this course, we group them into five families.

The first family is onboarding and identity. For example, matching a selfie to an ID photo and screening new customers against watch lists. The second is payments and fraud detection, where each card payment, transfer or mobile-money transaction gets a fraud score in real time.

The third family is lending and credit scoring. It estimates how likely an applicant is to repay, and spots early signs of arrears. The fourth is customer service, with assistants that answer routine questions, block lost cards and guide disputes.

The fifth family is back-office analysis and compliance. That means summarising reports, drafting management commentary, reconciling accounts, and flagging unusual activity for anti-money-laundering teams.

Two points apply to all five families. First, each use case is only as good as the data behind it. Second, each one produces an output that a person or a process must act on. Approve, block, reply or report. The quality of that human step matters as much as the model.

Here is a useful way to picture it. Think of AI as an extra pair of eyes at each step of a loan's journey. One pair checks the applicant's documents. Another looks at the risk of non-payment.

Another watches repayments for early warning signs. Another reads the customer's messages. None of these eyes makes the final decision alone. Each one helps the responsible person at that step to see more, and faster.

And not every task needs AI. A fee that follows a fixed table is better done with a simple formula. AI helps most when there are many cases, patterns change, and speed matters.

Let's look at three hypothetical institutions. Mavuno Pay is a mobile-money provider in Kenya. Its main use case is fraud detection. A model scores each transfer and holds the riskiest ones for a quick check. A simple classifier also sorts complaints into wrong transfer, PIN problem, and other.

Aurora Digital is a digital bank in Brazil. It uses AI in onboarding, to match selfies to ID documents, and in lending, for small personal loans. A human credit officer reviews every application that the model places near the decision boundary.

Rheinfeld Insurance is an insurer in Germany. It uses AI in the back office. An assistant drafts summaries of long claim files, and a model flags unusual claims for the fraud team. Handlers make every final decision.

Juliana Costa is a product manager at Aurora Digital. She maps all of this in a simple table: the step, the use case family, the data needed, and who acts on the output. The table quickly shows her a gap. The bank has no AI support in customer service, which is exactly where queue times are longest.

A common mistake is to think AI in finance means one large model that runs the whole bank. In practice, institutions run many small, separate models, each with its own data, owner and risks. So always assess one specific task, not AI in general.

Let's recap. First, AI use cases in finance fall into five families: onboarding and identity, payments and fraud, lending and credit, customer service, and back-office analysis and compliance. Second, each use case depends on specific data, and on the human step that acts on the output. Third, assess AI one task at a time, and use a simple formula when a task follows fixed rules.

Now it is your turn. In the exercise below this video, you will list eight finance tasks from your own work in Google Sheets, place each one in a family, and note the data it would need. Describe data types only, never real customer data. It takes about twenty minutes. In the next lesson, we look at financial data, and what models learn from. See you there.
```

## L02 Financial Data: What Models Learn From

- **Filename:** `ai-24-ai-in-finance-and-fintech_M1_L02_presenter.mp4`
- **Expected length:** about 4.9 minutes (687 words). The quality gate accepts ±10%.
- **Pronunciation:** Pronunciation: Nguyen Thi Lan (roughly 'nwen tee lan'); VND is spoken as 'Vietnamese dong'.

```text
Two teams build a fraud model with the same software. One model works well. The other fails in its first month. The difference is not the algorithm. It is the data each team gave it.

In the last lesson, we mapped five families of AI use cases. Every one of them depends on data. So today we look at what models learn from, and why data quality usually matters more than the choice of model.

In finance, there are four main types of data. Transactions: the amount, time, merchant, channel, location and device. Credit bureau records: existing loans, repayment history and missed payments. Alternative data, such as mobile airtime top-ups or utility bills. And text, such as complaints and call notes.

Each type has its own risks. Alternative data needs the customer's consent where required, and careful checks for fairness. Text often contains personal details that must be protected.

Each example has features and, for most finance models, a label. Features are the inputs the model looks at, such as amount or time of day. The label is the answer it must learn to predict, such as fraud or not fraud, repaid or defaulted.

Labels in finance are hard to get. A fraudulent card payment may look normal on the day. It is labelled as fraud only weeks later, when the real cardholder disputes it and a chargeback is completed. So the newest data often has incomplete labels, and some fraud is never reported at all.

Then there are data quality problems. Missing values. Duplicates, where the same transaction is recorded twice. Inconsistent formats, like two currencies in one column. Impossible values. And leakage: a column that contains the answer, such as a chargeback date, which only exists after fraud is known.

Think of a model as a trainee analyst who learns only from the files on their desk. If half the files are missing pages, some are copies of each other, and the answers are written on the cover, the trainee will learn the wrong lessons, however intelligent they are.

Let's see this with Nguyen Thi Lan. She is a data analyst at a hypothetical payments fintech in Ho Chi Minh City, Vietnam. She opens a synthetic sample of two thousand card transactions.

First, she gives each column a role. The transaction ID is an identifier, not a feature. Time, amount, currency, merchant category, country and a new-device flag are possible features. Is fraud is the label. And chargeback date is leakage, because it is only filled in after fraud is confirmed.

Next, she sorts and filters the sheet, and finds three problems. Some amounts are in Vietnamese dong and some in US dollars, in the same column. Fourteen rows appear twice with the same transaction ID. And merchant category is blank in about one row in twenty.

She also notices that transactions from the last three weeks have almost no fraud labels. That is not because they are safe. It is because disputes have not arrived yet. So she leaves the most recent weeks out of the training data, and will use them later, once the labels mature.

A common mistake is to believe more columns always make a better model. Extra columns can add leakage, missing values, or personal data you do not need. If a value is only known after the event, it cannot be a feature.

Let's recap. First, finance models learn from transactions, credit bureau records, alternative data and text, and each type has its own uses and risks. Second, labels such as fraud or default arrive late and can be incomplete, so the newest data needs special care. Third, check for missing values, duplicates, mixed formats, impossible values and leakage before you trust any model.

Now it is your turn. In the exercise below this video, you will open the synthetic transaction file in Google Sheets. Mark each column as a feature, the label, an identifier or leakage, and find three data quality problems, each with a practical fix. It takes about twenty-five minutes. In the next lesson, we look at fraud detection, with rules and models. See you there.
```

## L03 Fraud Detection: Rules and Models

- **Filename:** `ai-24-ai-in-finance-and-fintech_M1_L03_presenter.mp4`
- **Expected length:** about 5.1 minutes (711 words). The quality gate accepts ±10%.

```text
A card buys groceries in Lagos. Twenty minutes later, the same card buys a laptop in Singapore. No person can travel that far in twenty minutes. So how does a bank notice, in the fraction of a second before it approves the second payment?

Last time, we saw how fraud labels arrive late. Today we look at how fraud detection actually works. There are two main approaches, rules and models, and most institutions combine them.

Rules are fixed instructions written by fraud analysts. For example, block any payment above a set amount from a device the customer has never used. Rules are easy to explain and quick to change. But they only catch patterns someone has already thought of, and criminals learn to stay just below the limits.

Models learn patterns from past transactions labelled fraud or genuine. For each new transaction, the model produces a risk score, for example a number from zero to one thousand. A higher score means the transaction looks more like past fraud. And the score is ready while the payment is still being authorised.

A model weighs many signals together. Behaviour: is this amount normal for this customer? Velocity: how many payments in the last hour? Device and channel: is the phone new? And location: is the distance between two payments possible in the time between them?

The institution then sets actions by score band. For example, approve below six hundred, ask for a one-time code between six hundred and eight hundred and fifty, and decline above that. These bands are a business choice, not a feature of the model.

Fraud patterns also change. When one method is blocked, criminals try another. A model trained on last year's fraud slowly becomes less accurate. This is called drift. So models need new labelled data and regular retraining, and rules stay useful as a fast response while the model catches up.

Think of rules as a security guard with a printed list of banned faces, reliable for the list and blind to everyone else. A model is an experienced guard who notices when behaviour feels wrong. The best entrance has both guards.

Chinedu Okafor is a fraud analyst at a hypothetical card issuer in Lagos, Nigeria. A customer's card pays at a supermarket in Lagos at two minutes past two. At twenty-two minutes past two, it buys a laptop in Singapore.

A simple rule, two countries within one hour, flags the second payment. The model scores it nine hundred and thirty out of one thousand. Its main signals are the impossible travel time, a merchant type the customer has never used, and an amount far above their usual spending. The payment is declined, and the customer gets a text asking them to confirm recent activity.

Chinedu then tests three rules on a synthetic sample of five thousand transactions, with forty known fraud cases. A high-amount rule flags one hundred and twenty, but only twelve are fraud. New device and foreign country flags sixty, and eighteen are fraud. Two countries within one hour flags fifteen, and eleven are fraud.

The third rule is precise but rare. The first creates many false alarms. No single rule catches most of the forty cases. That is why the issuer also uses a model that combines the signals.

One warning. A fraud model does not know which payments are fraud. A genuine customer who travels suddenly can get a high score. So the score leads to a friendly check, not an accusation.

Let's recap. First, rules catch known patterns and are easy to explain, while models combine many signals into a risk score in a fraction of a second. Second, score bands for approve, verify and decline are a business decision that sits on top of the model. Third, fraud patterns change, so models drift and need new labelled data and regular retraining, with rules as a fast backup.

Now it is your turn. In the exercise below this video, you will write three fraud rules in Google Sheets, count how many transactions each one flags, and compare the flags with the fraud labels, just like Chinedu's table. It takes about thirty minutes. In the next lesson, we look at false alarms and missed fraud, and the cost trade-off. See you there.
```

## L04 False Alarms and Missed Fraud: The Cost Trade-off

- **Filename:** `ai-24-ai-in-finance-and-fintech_M1_L04_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.

```text
A fraud model that blocks every payment catches all the fraud. It also stops every honest customer from buying anything. So where exactly should the line be drawn, and who pays for each mistake?

In the last lesson, a fraud model gave each payment a risk score. Today we decide what to do with that score, and what each kind of mistake costs.

Every fraud model makes two kinds of error. A false positive is a false alarm. A genuine payment is blocked, the customer is embarrassed at the till, calls the contact centre, and may move to another bank. A false negative is missed fraud. The money is lost, and there are investigation and chargeback costs.

A confusion matrix puts all outcomes in one table. Fraud the model catches is a true positive. Fraud it misses is a false negative. A genuine payment it blocks is a false positive. And a genuine payment it approves is a true negative.

The institution picks a threshold. Any score above it is treated as fraud. A strict threshold flags more payments. It catches more fraud, but creates more false alarms. A relaxed threshold creates fewer false alarms, but misses more fraud. Moving the threshold alone cannot reduce both errors. Only a better model or better data does that.

So the right threshold depends on costs, not only on accuracy. Total cost equals missed fraud times the cost of one missed fraud, plus false alarms times the cost of one false alarm. Then you compare the totals.

A threshold is like the sensitivity setting on a smoke alarm. Set it very sensitive and it warns you about every real fire, and also every time you make toast. Set it less sensitive and the toast is quiet, but a small fire may be missed.

Marta Kowalska is a risk manager at a hypothetical payments company in Warsaw, Poland. She studies a synthetic set of ten thousand card payments. Fifty of them are fraud. At a strict threshold, she catches forty-five, misses five, and has four hundred false alarms. At a relaxed threshold, she catches thirty-five, misses fifteen, and has one hundred false alarms.

Each missed fraud costs three hundred on average. The cost of a false alarm is less certain, so she tests two assumptions. In assumption A, a false alarm costs five. The strict threshold then costs three thousand five hundred in total. The relaxed one costs five thousand. Strict is cheaper.

In assumption B, a false alarm costs twenty, because the payment is blocked at the till and the customer may leave. Now the strict threshold costs nine thousand five hundred. The relaxed one costs six thousand five hundred. Relaxed is cheaper.

The model has not changed. Only the business assumption has changed. So Marta's recommendation starts with the cost assumptions, and she asks the customer experience team for better evidence on the true cost of a false alarm.

A common mistake is to choose the threshold with the highest accuracy. With fifty fraud cases in ten thousand payments, a model that approves everything is ninety-nine point five percent accurate, and catches no fraud at all.

Always look at the two error types separately, and put a cost on each. Also remember that false alarms may not fall evenly on all customers. We look at that in lessons six and seven.

Let's recap. First, false positives block genuine customers, and false negatives let fraud through. Both have real costs for the institution and the customer. Second, moving the threshold trades one error for the other, and only a better model or better data reduces both. Third, choose the threshold by comparing total costs under clear, stated cost assumptions, not by accuracy alone.

Now it is your turn. In the exercise below this video, you will use the confusion-matrix sheet to try two thresholds and calculate the total cost per ten thousand transactions under two cost assumptions. Then write one sentence on which threshold you would choose, and why. It takes about twenty-five minutes. In the next lesson, we look at credit scoring with AI. See you there.
```

## L05 Credit Scoring with AI

- **Filename:** `ai-24-ai-in-finance-and-fintech_M1_L05_presenter.mp4`
- **Expected length:** about 5.0 minutes (693 words). The quality gate accepts ±10%.

```text
A vegetable trader has sold at the same market for eight years and has never missed a supplier payment. But she has never had a bank loan, so the credit bureau has nothing on her. To a traditional scorecard, she is invisible. Can AI see her?

We have spent two lessons on fraud. Now we turn to lending. Credit scoring estimates the probability of default: the chance that a borrower will not repay as agreed within a set period. The lender turns that estimate into a decision, a limit, and sometimes a price.

There are two common approaches. Scorecards are the traditional method. Each factor, such as repayment history or existing debt, adds or removes a fixed number of points. Scorecards are easy to read. You can see exactly why an applicant received their score.

Machine learning models can combine many more factors, and find patterns a scorecard misses, for example how spending changes in the months before a missed payment. They can be more accurate, but they are harder to explain. We come back to explanations in lesson ten.

Both approaches learn from past borrowers. So both can copy patterns from the past, including unfair ones. That is the subject of lesson six.

Thin-file customers have little or no credit history. Many people in emerging markets, young adults and new arrivals in a country are in this group. Alternative data, such as mobile-wallet activity, airtime top-ups, rent or utility payments, can give lenders evidence of reliable behaviour.

But alternative data brings risks. Customers may not know it is being used. Some data, such as phone type, can act as a proxy for income, age or ethnicity. And its use needs a lawful basis, and often consent, under local data protection law.

Here is a picture. A traditional scorecard is like an interviewer who only reads CVs. No CV, no interview. Alternative data is like also asking for references. It can open the door to good candidates, but only if the references are relevant, collected with permission, and checked for bias.

Meet Dewi Lestari. She sells vegetables at a market in Surabaya, Indonesia, and applies for a small working-capital loan at a hypothetical digital lender. She has no bureau history. The lender approves applications that score four hundred and twenty or more.

Dewi starts with three hundred points. Eighteen months of regular mobile-wallet sales add ninety. Utility bills paid on time, eleven out of twelve, add seventy. One small loan, always paid on time, adds twenty. High monthly income variability removes forty. And no bureau history adds nothing. Her total is four hundred and forty.

Dewi is approved with a modest starting limit. Her main positive drivers are her wallet sales and on-time utility payments. Her main negative driver is her variable income, which is common for market traders. Notice that missing bureau history did not lower her score. It simply added nothing.

Before final approval, the credit officer, Hendra Wijaya, checks one thing: that the mobile-wallet data was shared with Dewi's consent, as the lender's policy requires. And in the exercise, remember: never paste real applicant data into a public AI tool.

A common mistake is to think a model score is more objective than a person. A model is only as fair as the past decisions and data it learned from. A score is an estimate, not a fact about the person.

Let's recap. First, credit scoring estimates the probability of default, and the lender turns it into a decision, a limit and a price. Second, scorecards are easy to explain, while machine learning models can be more accurate but need extra work to explain. Third, alternative data can help thin-file customers, but it needs consent, relevance and fairness checks, and any inclusion claim needs a source.

Now it is your turn. In the exercise below this video, you will give Claude or ChatGPT the synthetic applicant table and ask it to explain the main drivers of the score. Then check every claim against the data, and mark any that are wrong. It takes about twenty minutes. In the next lesson, we look at fairness in credit decisions. See you there.
```
