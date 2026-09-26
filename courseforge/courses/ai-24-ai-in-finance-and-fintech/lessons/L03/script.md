# L03 Fraud Detection: Rules and Models | Presenter Script

Course: AI-24 · Video: 5 min · Words: 715

## Hook
A card buys groceries in Lagos. Twenty minutes later, the same card buys a laptop in Singapore. No person can travel that far in twenty minutes. So how does a bank notice, in the fraction of a second before it approves the second payment?

## Explain
Last time, we saw how fraud labels arrive late. Today we look at how fraud detection actually works. There are two main approaches, rules and models, and most institutions combine them.

Rules are fixed instructions written by fraud analysts. For example, block any payment above a set amount from a device the customer has never used. Rules are easy to explain and quick to change. But they only catch patterns someone has already thought of, and criminals learn to stay just below the limits.

Models learn patterns from past transactions labelled fraud or genuine. For each new transaction, the model produces a risk score, for example a number from zero to one thousand. A higher score means the transaction looks more like past fraud. And the score is ready while the payment is still being authorised.

A model weighs many signals together. Behaviour: is this amount normal for this customer? Velocity: how many payments in the last hour? Device and channel: is the phone new? And location: is the distance between two payments possible in the time between them?

The institution then sets actions by score band. For example, approve below six hundred, ask for a one-time code between six hundred and eight hundred and fifty, and decline above that. These bands are a business choice, not a feature of the model.

Fraud patterns also change. When one method is blocked, criminals try another. A model trained on last year's fraud slowly becomes less accurate. This is called drift. So models need new labelled data and regular retraining, and rules stay useful as a fast response while the model catches up.

Think of rules as a security guard with a printed list of banned faces, reliable for the list and blind to everyone else. A model is an experienced guard who notices when behaviour feels wrong. The best entrance has both guards.

## Demonstrate
Chinedu Okafor is a fraud analyst at a hypothetical card issuer in Lagos, Nigeria. A customer's card pays at a supermarket in Lagos at two minutes past two. At twenty-two minutes past two, it buys a laptop in Singapore.

A simple rule, two countries within one hour, flags the second payment. The model scores it nine hundred and thirty out of one thousand. Its main signals are the impossible travel time, a merchant type the customer has never used, and an amount far above their usual spending. The payment is declined, and the customer gets a text asking them to confirm recent activity.

Chinedu then tests three rules on a synthetic sample of five thousand transactions, with forty known fraud cases. A high-amount rule flags one hundred and twenty, but only twelve are fraud. New device and foreign country flags sixty, and eighteen are fraud. Two countries within one hour flags fifteen, and eleven are fraud.

The third rule is precise but rare. The first creates many false alarms. No single rule catches most of the forty cases. That is why the issuer also uses a model that combines the signals.

One warning. A fraud model does not know which payments are fraud. A genuine customer who travels suddenly can get a high score. So the score leads to a friendly check, not an accusation.

## Recap
Let's recap. First, rules catch known patterns and are easy to explain, while models combine many signals into a risk score in a fraction of a second. Second, score bands for approve, verify and decline are a business decision that sits on top of the model. Third, fraud patterns change, so models drift and need new labelled data and regular retraining, with rules as a fast backup.

## CTA
Now it is your turn. In the exercise below this video, you will write three fraud rules in Google Sheets, count how many transactions each one flags, and compare the flags with the fraud labels, just like Chinedu's table. It takes about thirty minutes. In the next lesson, we look at false alarms and missed fraud, and the cost trade-off. See you there.

## Thumbnail
Headline: Lagos to Singapore?
Image: Navy background, a world map outline with a teal line from Lagos to Singapore and a clock showing 20 minutes, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the card issuer, analyst and figures are hypothetical and synthetic (content.md Review Flags: None).
- Score bands (approve below 600, verify 600 to 850, decline above 850) are illustrative, not an industry standard. Keep the word 'for example' on the slide.
- Chinedu Okafor and his card issuer in Lagos are fictional. Stock footage must not show a real card brand, bank logo or readable card number.
