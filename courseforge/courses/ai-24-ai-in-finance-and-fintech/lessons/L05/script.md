# L05 Credit Scoring with AI | Presenter Script

Course: AI-24 · Video: 5 min · Words: 701

## Hook
A vegetable trader has sold at the same market for eight years and has never missed a supplier payment. But she has never had a bank loan, so the credit bureau has nothing on her. To a traditional scorecard, she is invisible. Can AI see her?

## Explain
We have spent two lessons on fraud. Now we turn to lending. Credit scoring estimates the probability of default: the chance that a borrower will not repay as agreed within a set period. The lender turns that estimate into a decision, a limit, and sometimes a price.

There are two common approaches. Scorecards are the traditional method. Each factor, such as repayment history or existing debt, adds or removes a fixed number of points. Scorecards are easy to read. You can see exactly why an applicant received their score.

Machine learning models can combine many more factors, and find patterns a scorecard misses, for example how spending changes in the months before a missed payment. They can be more accurate, but they are harder to explain. We come back to explanations in lesson ten.

Both approaches learn from past borrowers. So both can copy patterns from the past, including unfair ones. That is the subject of lesson six.

Thin-file customers have little or no credit history. Many people in emerging markets, young adults and new arrivals in a country are in this group. Alternative data, such as mobile-wallet activity, airtime top-ups, rent or utility payments, can give lenders evidence of reliable behaviour.

But alternative data brings risks. Customers may not know it is being used. Some data, such as phone type, can act as a proxy for income, age or ethnicity. And its use needs a lawful basis, and often consent, under local data protection law.

Here is a picture. A traditional scorecard is like an interviewer who only reads CVs. No CV, no interview. Alternative data is like also asking for references. It can open the door to good candidates, but only if the references are relevant, collected with permission, and checked for bias.

## Demonstrate
Meet Dewi Lestari. She sells vegetables at a market in Surabaya, Indonesia, and applies for a small working-capital loan at a hypothetical digital lender. She has no bureau history. The lender approves applications that score four hundred and twenty or more.

Dewi starts with three hundred points. Eighteen months of regular mobile-wallet sales add ninety. Utility bills paid on time, eleven out of twelve, add seventy. One small loan, always paid on time, adds twenty. High monthly income variability removes forty. And no bureau history adds nothing. Her total is four hundred and forty.

Dewi is approved with a modest starting limit. Her main positive drivers are her wallet sales and on-time utility payments. Her main negative driver is her variable income, which is common for market traders. Notice that missing bureau history did not lower her score. It simply added nothing.

Before final approval, the credit officer, Hendra Wijaya, checks one thing: that the mobile-wallet data was shared with Dewi's consent, as the lender's policy requires. And in the exercise, remember: never paste real applicant data into a public AI tool.

A common mistake is to think a model score is more objective than a person. A model is only as fair as the past decisions and data it learned from. A score is an estimate, not a fact about the person.

## Recap
Let's recap. First, credit scoring estimates the probability of default, and the lender turns it into a decision, a limit and a price. Second, scorecards are easy to explain, while machine learning models can be more accurate but need extra work to explain. Third, alternative data can help thin-file customers, but it needs consent, relevance and fairness checks, and any inclusion claim needs a source.

## CTA
Now it is your turn. In the exercise below this video, you will give Claude or ChatGPT the synthetic applicant table and ask it to explain the main drivers of the score. Then check every claim against the data, and mark any that are wrong. It takes about twenty minutes. In the next lesson, we look at fairness in credit decisions. See you there.

## Thumbnail
Headline: Invisible to the Bureau?
Image: Navy background, a market trader silhouette beside an empty credit file and a teal score card reading 440, headline in teal Inter Bold.

## Production Notes
- [VERIFY] The script quotes no statistic about alternative data and financial inclusion. Do not add one in slides or captions unless a named, checked source is approved.
- [REGION] Consent and lawful-basis rules for alternative data differ by country. The script says only that its use needs consent and a lawful basis where the law requires it.
- [VERSION] The exercise uses Claude or ChatGPT free plans: check free-plan access and data-use terms before recording.
- Dewi Lestari, Hendra Wijaya and the Surabaya digital lender are fictional. Scorecard points on screen must match content.md exactly (300, +90, +70, +20, −40, 0, total 440; approval at 420).
