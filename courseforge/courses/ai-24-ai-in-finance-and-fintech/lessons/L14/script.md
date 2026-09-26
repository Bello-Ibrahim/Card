# L14 Risk and Compliance Assessment | Presenter Script

Course: AI-24 · Video: 5 min · Words: 688

## Hook
Every AI proposal promises benefits. But the committee's real question is different. What could go wrong, how bad would it be, and what will you do about it? A clear risk register answers that question on one page.

## Explain
In the last lesson, you scoped your proposal. Now, in this final lesson, you assess its risks. A risk register lists the main risks of your use case in a table, one row per risk.

For each risk, you write what could go wrong, as a cause and an effect. You give it a category. You rate likelihood and impact from one to three, and multiply them for a score from one to nine. Then you add controls, an owner, and a residual rating after the controls.

Cover all six categories from this course. Fairness means outcomes are worse for some groups. Privacy means data is used without a lawful basis, or shared too widely. Explainability means staff or customers cannot understand the outputs.

Security covers data leaks, manipulation of the model, or misuse of the assistant. Third-party covers a vendor that changes its model, uses your data for its own purposes, or stops the service. And operational covers errors, drift, staff over-trusting outputs, or no fallback process.

Then make a recommendation. Go means risks are low or well controlled, so you launch with monitoring. Pilot means the value looks real, but some risks are uncertain, so you test at small scale for a set time. No-go means a high risk cannot be controlled, or the value does not justify it.

A pilot is not a way to avoid a decision. It needs a clear end date, clear measures, and a named person who decides what happens next.

A risk register is like a pre-flight checklist. The pilot does not refuse to fly because things can go wrong. She lists what could go wrong, checks each control, and flies only when the list is complete. If a critical item fails, the flight waits.

## Demonstrate
Rafael Dizon is a compliance officer at Bayanihan Microfinance. He builds the register for Joy's visit-note assistant from the last lesson. The fairness risk: summaries of notes in local languages contain more errors. Likelihood two, impact three, score six. Controls: test error rates by language before launch, and officers check every summary. Residual three.

Other rows cover explainability, staff pasting data into public tools, and a vendor changing its model. The operational risk is officers signing summaries without reading them. Likelihood three, impact two. With random supervisor checks and error monitoring, the residual is four, the highest in the register.

The fairness risk needs evidence that only a real test can give. So Rafael recommends a pilot: two branches, three months, with a stop rule if the summary error rate for any language group is clearly higher than for English notes. The credit committee chair decides at the end.

Your capstone also needs a short principles check. For each of the six principles from lesson eleven, write one line on how your proposal meets it, and what must be confirmed locally. Then write your recommendation in one paragraph, with reasons. For a pilot, give its scope, length and stop rule.

A common mistake is weak controls, such as be careful or monitor the model. A control says who does what, how often, and what happens at a limit. And do not score every risk as one. Committees trust honest registers more.

## Recap
Let's recap. First, a risk register records each risk with its category, likelihood, impact, score, controls, owner and residual rating. Second, cover fairness, privacy, explainability, security, third-party and operational risks, with specific controls for each. Third, end with a clear go, pilot or no-go recommendation, and give any pilot an end date, measures and a named decision-maker.

## CTA
Congratulations on reaching the end of AI in Finance and Fintech. Your last exercise is capstone step two. Complete the risk register in Google Sheets, add a principles check, and finish with your recommendation. Check it against the rubric and checklist, then submit your capstone proposal. Well done, and good luck.

## Thumbnail
Headline: Go, Pilot or No-Go?
Image: Navy background, a one-page risk register with a traffic-light column and three teal buttons labelled Go, Pilot and No-Go, headline in teal Inter Bold.

## Production Notes
- [REGION] Consent and data processing requirements for using client data with an external AI service differ by country. The privacy row on screen keeps the note 'consent wording reviewed (confirm locally)'.
- Risk register figures must match content.md exactly (likelihood, impact, score and residual for all six rows; highest residual 4 from over-trust; pilot of two branches for three months).
- Rafael Dizon, Joy Villanueva and Bayanihan Microfinance are fictional.
- Last lesson of the course: the CTA congratulates learners and points to the capstone submission, rubric and checklist.
