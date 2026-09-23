# L05 Credit Scoring with AI

Course: AI-24 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
A vegetable trader has sold at the same market for eight years and has never missed a supplier payment. But she has never had a bank loan, so the credit bureau has nothing on her. To a traditional scorecard, she is invisible. Can AI see her?

## Explanation
Credit scoring estimates the **probability of default**: the chance that a borrower will not repay as agreed within a set period. The lender turns that estimate into a decision (approve, decline or refer to a person), a limit and sometimes a price.

There are two common approaches.

**Scorecards** are the traditional method. Each factor, such as repayment history or existing debt, adds or removes a fixed number of points. The points are usually set with a statistical method called logistic regression. Scorecards are easy to read: you can see exactly why an applicant received their score.

**Machine learning models**, such as gradient-boosted trees, can combine many more factors and find patterns a scorecard misses, for example how spending changes in the months before a missed payment. They can be more accurate, but they are harder to explain. Lenders often use explanation methods to show which factors pushed a score up or down (L10).

Both approaches learn from past borrowers: their data at the time of application and whether they later repaid. This means both can copy patterns from the past, including unfair ones (L06).

**Thin-file customers** have little or no credit history. Many people in emerging markets, young adults and new arrivals in a country are in this group. **Alternative data**, such as mobile-wallet activity, airtime top-ups, rent or utility payments, can give lenders evidence of reliable behaviour. This is often presented as a route to financial inclusion. Claims that alternative data increases approvals or inclusion by a certain amount must come from a named, checked source [VERIFY]. This course does not quote such figures.

Alternative data also brings risks. Customers may not know it is being used. Some data, such as phone type or the apps on a phone, can act as a proxy for income, age or ethnicity. And its use needs a lawful basis and often consent under local data protection law [REGION].

**Analogy:** A traditional scorecard is like a job interviewer who only reads CVs. A candidate without a CV is rejected before the interview. Alternative data is like also asking for references from people who have seen the candidate work. It can open the door to good candidates, but only if the references are relevant, collected with permission and checked for bias.

## Worked Example
Dewi Lestari sells vegetables at a market in Surabaya, Indonesia. She applies for a small working-capital loan at a hypothetical digital lender. She has no bureau history, so the lender uses a scorecard that includes alternative data. The lender approves applications that score 420 or more.

| Factor | Dewi's value | Points |
|---|---|---|
| Starting points | | 300 |
| Months of regular mobile-wallet sales | 18 | +90 |
| Utility bills paid on time, last 12 months | 11 of 12 | +70 |
| Existing loans | 1 small loan, always paid on time | +20 |
| Monthly income variability | High | −40 |
| Credit bureau history | None | 0 |
| **Total** | | **440** |

Dewi is approved with a modest starting limit. Her main positive drivers are her mobile-wallet sales history and her on-time utility payments. Her main negative driver is her variable monthly income, which is common for market traders. The lack of bureau history did not reduce her score in this scorecard; it simply added nothing.

The credit officer, Hendra Wijaya, checks one thing before final approval: that the mobile-wallet data was shared with Dewi's consent, as the lender's policy requires.

## Common Mistake
Many people assume that a score from a machine learning model is more "objective" than a person's judgement. A model is only as fair as the past decisions and data it learned from. If a group of people was rarely approved in the past, the model has little evidence about how they repay and may keep scoring them low. A score is an estimate, not a fact about the person.

## Key Takeaways
1. Credit scoring estimates the probability of default; the lender turns it into a decision, a limit and a price.
2. Scorecards are easy to explain; machine learning models can be more accurate but need extra work to explain.
3. Alternative data can help thin-file customers, but it needs consent, relevance and fairness checks, and any inclusion claim needs a source.

## Hands-on Exercise
**Task:** Ask an AI assistant to explain the drivers of a synthetic applicant's score, then check every claim against the data.
**Tools:** Claude or ChatGPT (free plan) [VERSION]; the scorecard table for Dewi from this lesson, or the synthetic applicant table on the course page.
**Steps:**
1. Copy the synthetic applicant table. Never paste real applicant or customer data into a public AI tool.
2. Ask: "Explain the three main drivers of this applicant's score in plain language, and say which factor lowered the score most."
3. Copy the answer into a document.
4. Check each statement against the table: are the points, directions and ranking correct?
5. Mark each claim "correct", "wrong" or "not supported by the data". For example, a claim that missing bureau history lowered the score is wrong in this table.
6. Write one sentence on whether you would use the AI's explanation without review.
**What good looks like:** Every AI claim is checked and marked, at least one error or unsupported claim is found or its absence is confirmed, and your final sentence explains why a human must review AI explanations.
**Time:** about 20 minutes

## Review Flags
- [VERIFY] Any statistic about alternative data and financial inclusion needs a named source or must be removed; the lesson currently quotes none.
- [REGION] Consent and lawful-basis rules for using alternative data differ by country; confirm with local data protection law.
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
