# L04 Scoring Opportunities: Value, Feasibility and Risk

Course: AI-27 · Module: M1 · Objectives: O3, O4 · Video: 5 min

## Hook
Two AI ideas can promise the same value. One saves staff a few minutes when it is wrong. The other pays out money to the wrong person when it is wrong. A good scoring method sees that difference before anyone writes code.

## Explanation
You already know how to prioritise a backlog. For AI features, add one dimension that normal scoring often ignores: **the cost of errors**. Because AI outputs are probabilistic (L01), some outputs will be wrong. The question is how much a wrong output hurts.

Use a simple matrix with three dimensions, each scored from 1 to 5:

- **Value (V):** How much does this help users and the business? Consider how many users, how often, and how painful the problem is.
- **Feasibility (F):** Do we have the data, the skills and a realistic technical path? A feature with no available examples scores low, however valuable it is.
- **Error cost (E):** How bad is a wrong output? 1 means a user loses a few seconds. 5 means financial, legal, safety or serious trust harm.

Because high error cost is bad, flip it before adding: **Total = V + F + (6 − E)**. The maximum is 15. You can weight value more if your team prefers, but keep the formula visible and the same for every idea.

The numbers are not precise. Their purpose is to make the team state its assumptions and argue about the right thing. Write one sentence of reasoning next to each score.

The most useful insight comes from ideas with **high value and high error cost**. Do not simply drop them. Ask whether a **narrower scope** lowers the error cost. You can narrow in several ways: suggest instead of decide, keep a human in the loop, limit it to low-stakes cases, or help staff instead of customers. Then score the narrow version as a new row.

**Analogy:** An investment committee does not only ask, "How much could this project earn?" It also asks, "What could go wrong, and how much would we lose?" A project with large possible gains and large possible losses might still be approved, but with a smaller first investment and clear conditions. Narrowing an AI feature is the same as making a smaller first investment.

## Worked Example
Youssef Amrani is a PM at a hypothetical car insurance company in Morocco. His team has five AI ideas for the claims journey. They score each one:

| Idea | V | F | E | 6 − E | Total |
|---|---|---|---|---|---|
| A. Plain-language summary of claim status for customers | 4 | 5 | 2 | 4 | 13 |
| B. Estimate repair cost from customer photos | 5 | 2 | 5 | 1 | 8 |
| C. Checklist of missing documents for a claim | 3 | 5 | 1 | 5 | 13 |
| D. Flag possibly fraudulent claims for human reviewers | 4 | 3 | 3 | 3 | 10 |
| E. Automatically approve small claims | 5 | 3 | 5 | 1 | 9 |

Ideas A and C score highest. Both use data the company already has, and a wrong output is easy to notice and correct.

Idea E has the highest value but a very high error cost: a wrong approval pays money, and a wrong rejection harms a customer. Youssef proposes a narrower version, E2: "Suggest approve or refer for small claims, and a claims officer confirms every decision." The team scores E2 at V 4, F 3, E 2, so 4 + 3 + 4 = 11. It is now a serious candidate, and it creates labelled data (officer decisions) that could support a wider version later.

Idea B, photo estimates, has low feasibility because the company has few labelled photos. Youssef notes it as a data problem to revisit, not a dead idea.

His top 3 are A, C and E2, each with one sentence of reasoning.

## Common Mistake
Teams often score only value and feasibility, because that is what they use for normal features. Then the most valuable but most dangerous ideas rise to the top. Others make the opposite mistake: they give up on any high-risk idea. Score error cost separately, and always test whether a narrower scope with human review keeps most of the value.

## Key Takeaways
1. Score AI opportunities on value, feasibility and error cost, and keep the formula the same for every idea.
2. Feasibility depends mostly on data: an idea without available examples is not ready, however valuable.
3. For high-value, high-risk ideas, score a narrower version, such as a suggestion with human confirmation, before deciding.

## Hands-on Exercise
**Task:** Score your opportunities from L03 in a Google Sheets matrix and choose the top 3, with one sentence of reasoning each.
**Tools:** Google Sheets (free with a Google account) [VERSION].
**Steps:**
1. Open the sheet from L03. Add columns: V, F, E, Flipped E, Total, Reasoning.
2. Score each kept idea from 1 to 5 for V, F and E. Write a short reason for each score.
3. In Flipped E, enter a formula such as `=6-D2`. In Total, enter `=B2+C2+E2`, adjusting the letters to your columns.
4. Sort by Total, highest first.
5. For any idea with V of 4 or 5 and E of 4 or 5, add a narrower version as a new row and score it.
6. Choose your top 3 and write one sentence for each explaining why it is worth doing first.
**What good looks like:** Every score has a reason, the formula is consistent, at least one risky idea has a narrower version, and the top 3 reasoning mentions both value and error cost.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Google Sheets formula and sorting features used in the exercise must be checked before recording.
