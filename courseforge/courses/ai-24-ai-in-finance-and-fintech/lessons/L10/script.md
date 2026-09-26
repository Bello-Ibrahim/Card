# L10 Explainability: Why Was I Declined? | Presenter Script

Course: AI-24 · Video: 5 min · Words: 688

## Hook
Your application was unsuccessful. This decision was based on a number of factors. Imagine receiving that message after applying for a loan for your family business. What would you do next? You would not know. And that is the problem this lesson solves.

## Explain
In lessons six and seven, we measured whether decisions are fair. Now we ask whether they can be explained. Three groups need to understand a credit decision. Customers need to know why they were declined, and what they could change. Staff need to explain and check decisions. And supervisors and auditors need evidence that the model works as intended.

In many countries, lenders must give applicants the main reasons for a decline, and some laws give people rights around automated decisions. The rules differ from place to place, so always check the rules where you work. Lesson eleven looks at examples.

Lenders use two main tools. Reason codes are short, standard statements linked to the factors that lowered a score the most. For example, high level of existing debt compared with income. In a scorecard, they come directly from the points. In a machine learning model, they come from an explanation method.

The second tool is feature importance. Global importance shows which features matter most across all decisions. Local importance shows which features pushed one applicant's score up or down. That is what a decline reason needs. These methods give estimates, not perfect truth, so they must be tested too.

There is a big difference between an accurate explanation and a comforting one. We had a very high number of applications this month may feel kind. But if it is not the real reason, it is misleading, and it stops the customer fixing the real problem. A good reason is true, specific, understandable, actionable where possible, and respectful. And it never names a protected characteristic or a proxy.

It is like a doctor explaining a test result. Your results were not ideal is kind but useless. Your blood pressure is high, and reducing salt could help, is true, specific and useful.

## Demonstrate
Youssef Hassan applies for a personal loan at Nile Gate Finance, a hypothetical lender in Cairo, Egypt. The model declines him. The top three factors are his debt payments, at fifty-two percent of his income, two missed payments in the last twelve months, and a credit card balance at ninety-five percent of its limit.

The system's first draft reads: declined, debt-to-income above threshold, two delinquencies in twelve months, utilisation high. It is accurate, but full of jargon and abbreviations. A customer would not understand it, and could not act on it.

The credit officer, Nour El-Sayed, rewrites it. We could not approve your application at this time. The main reasons were: your monthly debt payments are high compared with your income. Two payments were missed in the last twelve months. And your credit card balance is close to its limit. Reducing your debt and paying on time can improve future applications.

She checks that each reason matches the data and the order of importance, and that the letter makes no promise of future approval. A common mistake is to let an explanation tool or an AI assistant write reasons with no check. The result may be fluent but wrong, for example naming a factor that did not lower the score. Every reason must be traced back to that applicant's data.

## Recap
Let's recap. First, customers, staff and supervisors all need explanations, and many countries require decline reasons. Second, reason codes and local feature importance show which factors lowered one applicant's score, and they must be tested and checked. Third, a good decline reason is true, specific, understandable, actionable and respectful. A comforting but inaccurate reason is misleading.

## CTA
Now it is your turn. In the exercise below this video, you will write customer-friendly decline reasons for three synthetic applicants. Ask an AI assistant to check them for jargon, without adding new reasons. Then confirm that each reason matches the data. It takes about twenty-five minutes. Next week, we start with regulatory principles for AI in finance. See you there.

## Thumbnail
Headline: Why Was I Declined?
Image: Navy background, a letter with three short teal reason lines replacing a vague grey sentence, headline in teal Inter Bold.

## Production Notes
- [REGION] Requirements to give decline reasons, and rights about automated decisions, differ by country. The script says 'in many countries' and points to lesson 11; do not name a specific law here.
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
- Youssef Hassan, Nour El-Sayed and Nile Gate Finance are fictional. Factor values on screen must match content.md (52%, 2 missed payments, 95%). The rewritten letter must contain no promise of future approval.
- Content.md mentions an Arabic version of the letter reviewed by the same team; it is not shown on screen. If added later, it needs a native Arabic speaker check.
