# L10 Explainability: Why Was I Declined?

Course: AI-24 · Module: M2 · Objectives: O4, O5 · Video: 5 min

## Hook
"Your application was unsuccessful. This decision was based on a number of factors." Imagine receiving that message after applying for a loan for your family business. What would you do next? You would not know, and that is the problem this lesson solves.

## Explanation
Three groups need to understand a credit decision.

- **Customers** need to know why they were declined and what they could change.
- **Staff**, such as credit officers and complaint handlers, need to explain and check decisions.
- **Supervisors and auditors** need evidence that the model works as intended and treats customers fairly.

In many countries, lenders must give applicants the main reasons for a decline, and some laws give people rights around automated decisions [REGION]. L11 looks at examples.

Lenders use two main tools.

**Reason codes** are short, standard statements linked to the factors that lowered a score the most, for example "Payments missed in the last 12 months" or "High level of existing debt compared with income". In a scorecard, these come directly from the points. In a machine learning model, they come from an explanation method.

**Feature importance** describes which inputs affect the model's output. At a high level there are two views:
- **Global importance:** which features matter most across all decisions. This helps the model owner and the validator.
- **Local importance:** which features pushed this one applicant's score up or down. This is what a decline reason needs.

Explanation methods give estimates, not perfect truth. They must be tested, like the model itself.

There is an important difference between an **accurate explanation** and a **comforting explanation**. A comforting message such as "We had a very high number of applications this month" may feel kind, but if it is not the real reason, it is misleading. It also stops the customer from fixing the real problem. A good decline reason is:

- **True:** it matches the factors that actually drove the decision.
- **Specific:** it names the factor, not "a number of factors".
- **Understandable:** no jargon, such as "DTI" or "utilisation".
- **Actionable where possible:** it shows what the customer could change.
- **Respectful:** it does not blame or judge the customer.

It must also never name a protected characteristic or a proxy as a reason. If a proxy appears among the top factors, that is a fairness problem to fix (L06, L07), not a reason to explain.

**Analogy:** A decline reason is like a doctor explaining a test result. "Your results were not ideal" is kind but useless. "Your blood pressure is high, and reducing salt could help" is true, specific and useful. Patients, and borrowers, deserve the second kind of explanation.

## Worked Example
Youssef Hassan applies for a personal loan at Nile Gate Finance, a hypothetical lender in Cairo, Egypt. The model declines the application. The top three factors that lowered his score are:

| Factor | Youssef's value | Effect on score |
|---|---|---|
| Existing monthly debt payments ÷ monthly income | 52% | Large negative |
| Payments missed in the last 12 months | 2 | Medium negative |
| Credit card balance ÷ credit card limit | 95% | Small negative |

The first draft from the system reads: "Declined: DTI > threshold; delinquency_12m = 2; utilisation high." This is accurate but full of jargon.

The credit officer, Nour El-Sayed, rewrites it:

"We could not approve your application at this time. The main reasons were:
1. Your current monthly debt payments are high compared with your income.
2. Two payments were missed on your existing accounts in the last 12 months.
3. Your credit card balance is close to its limit.
You can apply again later. Reducing your existing debt and making payments on time can improve future applications."

She checks that each reason matches the data and the order of importance, and that the letter contains no promise of future approval. The bank's Arabic version is reviewed by the same team.

## Common Mistake
Many teams let a generic explanation tool or an AI assistant write decline reasons with no check. The result may be fluent but wrong, for example naming a factor that did not lower the score. Every reason must be traced back to the actual data and model output for that applicant.

## Key Takeaways
1. Customers, staff and supervisors all need explanations, and many countries require lenders to give decline reasons.
2. Reason codes and local feature importance show which factors lowered one applicant's score; they must be tested and checked.
3. A good decline reason is true, specific, understandable, actionable and respectful; a comforting but inaccurate reason is misleading.

## Hands-on Exercise
**Task:** Write customer-friendly decline reasons for 3 synthetic applicants, check them for jargon with an AI assistant, and confirm each reason matches the data.
**Tools:** Claude or ChatGPT (free plan) [VERSION]; the course's table of 3 synthetic applicants with their top factors.
**Steps:**
1. Open the synthetic applicant table. It contains no real customer data.
2. For each applicant, write up to three reasons in plain language, in order of importance.
3. Paste only your draft reasons into the AI assistant and ask: "Point out any jargon or unclear wording, and suggest simpler words. Do not add new reasons."
4. Accept only the wording changes you agree with.
5. Check each final reason against the table: correct factor, correct direction, correct order.
6. Confirm that no reason mentions a protected characteristic or a proxy such as postcode.
**What good looks like:** Three short letters with true, specific, jargon-free reasons in the right order, and a note for each applicant confirming the check against the data.
**Time:** about 25 minutes

## Review Flags
- [REGION] Requirements to give decline reasons, and rights about automated decisions, differ by country; confirm local rules.
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
