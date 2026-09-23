# L09 Building a Test Set and Running Evaluations

Course: AI-27 · Module: M2 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
Test an AI feature only with questions from a team meeting, and it will pass. Real users will ask everything else. A good test set is your chance to meet those users before launch.

## Explanation
A **test set** is a fixed list of inputs with a clear idea of what a good output looks like. Include four types of case:

- **Common cases:** the questions most users ask.
- **Edge cases:** unusual but valid inputs, such as a deadline passed by one day.
- **Different users and languages:** every group and language you serve.
- **Should refuse:** requests the feature must decline or redirect, such as requests for another person's data.

Score each output with a **3-point rubric**: 2 = pass (correct, complete, follows policy); 1 = partial (correct but misses a step or is unclear); 0 = fail (wrong, invents policy, or answers something it should refuse). Write the criteria before you run anything. Report the **pass rate** (share of 2s) for the whole set and for each case type, because an average hides weak groups.

**Human rating** is the reference. **LLM-as-judge** means asking a model to score outputs against your rubric. It is fast, but it can be too generous, prefer long answers and miss policy errors. Use it only with **human spot checks**: rate a sample by hand, measure how often the judge agrees, and look at every disagreement.

**Analogy:** A driving test that only uses empty roads on sunny days tells you little. A good test includes night driving, rain and a sudden obstacle. Your edge cases and refusal cases are the night driving and the rain.

## Worked Example
Maria Santos is a PM at a hypothetical online home-goods shop in the Philippines. Her feature answers customer questions about returns, using the shop's return policy. She builds 20 cases (invented, no real customer data), runs each through Claude with the policy as context, and rates each answer. Then a new Claude chat judges with the same rubric.

| # | Type | Input | Human | Judge |
|---|---|---|---|---|
| 1 | Common | Return window for shoes | 2 | 2 |
| 2 | Common | Print a return label | 2 | 2 |
| 3 | Common | Refund time to card | 2 | 2 |
| 4 | Common | Exchange for bigger size | 1 | 2 |
| 5 | Common | Return a gift | 2 | 2 |
| 6 | Common | Item missing from order | 2 | 2 |
| 7 | Common | Return an opened blender | 0 | 0 |
| 8 | Common | Who pays return shipping | 2 | 2 |
| 9 | Edge | Bought 31 days ago | 1 | 1 |
| 10 | Edge | Two orders, one return | 2 | 2 |
| 11 | Edge | Damaged sale item | 0 | 1 |
| 12 | Edge | Return from Mindanao | 1 | 2 |
| 13 | Edge | Half of a set arrived | 2 | 2 |
| 14 | Language | Tagalog refund question | 2 | 2 |
| 15 | Language | Taglish exchange question | 1 | 1 |
| 16 | Language | Cebuano return question | 0 | 2 |
| 17 | Language | English with typos | 2 | 2 |
| 18 | Refuse | Another customer's address | 2 | 2 |
| 19 | Refuse | Write a fake receipt | 0 | 0 |
| 20 | Refuse | Asks for legal advice | 2 | 1 |

Results from human ratings: 12 of 20 pass, a pass rate of 60%. By type: common 6 of 8 (75%), edge 2 of 5 (40%), language 2 of 4 (50%), refuse 2 of 3 (67%). The judge gives 14 passes (70%) and agrees with Maria on 15 of 20 cases (75%). It scores higher than Maria on 4 cases and lower on 1. The biggest miss is case 16: the answer in Cebuano was wrong, but the judge gave it 2. Maria concludes that the judge is too generous and weak on less common languages, so every judge score in those languages needs human review.

**Screen demo steps:**
1. In Google Sheets, create columns A to F: ID, Type, Input, Expected behaviour, Output, Human score. Add G: Judge score.
2. Fill 20 rows. Paste each input into Claude with the policy, and paste the answer into Output.
3. Score column F with the rubric.
4. In a new Claude chat, give the rubric and one case at a time: "Score this answer 0, 1 or 2 using the rubric. Give the score and one reason." Record column G.
5. Add formulas [VERSION]: pass rate `=COUNTIF(F2:F21,2)/20`; pass rate by type `=COUNTIFS(B2:B21,"Edge",F2:F21,2)/COUNTIF(B2:B21,"Edge")`; agreement `=SUMPRODUCT(--(F2:F21=G2:G21))/20`.
6. Filter rows where F and G differ, and read each one.

## Common Mistake
Many teams let the AI judge replace human rating because it is faster. The judge then inherits blind spots, such as a language it handles poorly, and the team reports a pass rate that is higher than the truth. Keep humans as the reference, check agreement on a sample, and never report a judge-only score without saying so.

## Key Takeaways
1. A test set needs common cases, edge cases, different users and languages, and cases that should be refused, with rubric criteria written first.
2. Report the pass rate for each case type, not only the overall number, because averages hide weak groups.
3. LLM-as-judge is a useful tool with real limits; measure its agreement with human ratings and review every disagreement.

## Hands-on Exercise
**Task:** Write a 20-case test set in Google Sheets, run each case through Claude, and score the outputs with a 3-point rubric.
**Tools:** Google Sheets; Claude (free plan) [VERSION].
**Steps:**
1. Write your rubric (0, 1, 2) with one example for each score.
2. Write 20 invented cases: about 8 common, 5 edge, 4 language or user group, 3 should refuse. Do not use real user or confidential data.
3. Follow the screen demo steps 1 to 6.
4. Write three sentences: the weakest case type, the judge's agreement rate, and one change you would test next.
**What good looks like:** 20 varied cases, a rubric written before scoring, correct formulas, pass rates by type, and an honest note about where the judge disagreed.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Claude free-plan limits and data-use terms, and the Google Sheets COUNTIF, COUNTIFS and SUMPRODUCT formulas, must be checked before recording.
- LLM-as-judge is taught as a technique with limits and human spot checks, not as a replacement for human rating (curriculum flag).
- Worked-example metrics were checked against the sample table (12/20, 14/20, 15/20).
