# L14 Risk and Compliance Assessment

Course: AI-24 · Module: M3 · Objectives: O5, O6 · Video: 5 min

## Hook
Every AI proposal promises benefits. The committee's real question is different: "What could go wrong, how bad would it be, and what will you do about it?" A clear risk register answers that question on one page.

## Explanation
A **risk register** lists the main risks of your use case in a table. For each risk, you record:

- **Risk:** what could go wrong, written as a cause and an effect.
- **Category:** fairness, privacy, explainability, security, third-party or operational.
- **Likelihood:** how likely it is, on a simple scale: 1 = low, 2 = medium, 3 = high.
- **Impact:** how much harm it would cause to customers or the institution: 1 = low, 2 = medium, 3 = high.
- **Score:** likelihood × impact, from 1 to 9.
- **Controls:** what reduces the risk, such as testing, human review, limits or contract terms.
- **Owner:** the role responsible.
- **Residual rating:** the score after controls.

Cover all six categories from this course:

- **Fairness:** outcomes worse for some groups (L06, L07).
- **Privacy and data protection:** data used without a lawful basis, or shared too widely (L11).
- **Explainability:** staff or customers cannot understand outputs (L10).
- **Security:** data leaks, manipulation of the model, or misuse of the assistant.
- **Third-party:** the vendor changes the model, uses your data for its own purposes, or stops the service.
- **Operational:** errors, drift, staff over-trusting outputs, or no fallback process (L12).

Then make a **recommendation**:

- **Go:** risks are low or well controlled. Launch with monitoring.
- **Pilot:** the value looks real, but some risks are uncertain. Test at small scale, for a set time, with success and stop criteria.
- **No-go:** a high risk cannot be controlled, or the value does not justify the risk.

A pilot is not a way to avoid a decision. It must have a clear end date, clear measures and a named person who decides what happens next.

**Analogy:** A risk register is like a pre-flight checklist. The pilot does not refuse to fly because things can go wrong. The pilot lists what could go wrong, checks each control, and flies only when the list is complete. If a critical item fails, the flight waits.

## Worked Example
Rafael Dizon, compliance officer at the hypothetical Bayanihan Microfinance, builds the risk register for Joy Villanueva's visit-note summary assistant from L13.

| Risk | Category | L | I | Score | Controls | Owner | Residual |
|---|---|---|---|---|---|---|---|
| Summaries of notes in local languages contain more errors, so some clients are judged on worse information | Fairness | 2 | 3 | 6 | Test error rates by language before launch; officer checks every summary | Operations manager | 3 |
| Client data sent to an external AI service without a lawful basis | Privacy | 2 | 3 | 6 | Approved enterprise tool only; data processing agreement; consent wording reviewed [REGION] | Data protection officer | 2 |
| Officers cannot tell which parts of a summary came from which note | Explainability | 2 | 2 | 4 | Summary links each point to the source line | Product owner | 2 |
| Staff paste data into unapproved public tools | Security | 2 | 3 | 6 | Policy, training and blocked access to unapproved tools | Information security | 3 |
| Vendor changes its model and quality drops | Third-party | 2 | 2 | 4 | Contract notice terms; monthly quality sample | Vendor manager | 2 |
| Officers sign summaries without reading them | Operational | 3 | 2 | 6 | Random supervisor checks; error-rate monitoring | Branch supervisor | 4 |

The highest residual score is 4, from over-trust. The fairness risk needs evidence that only a real test can give. Rafael recommends a **pilot**: two branches, three months, with a stop rule if the summary error rate for any language group is clearly higher than for English notes. The credit committee chair decides at the end of the pilot.

## Common Mistake
Many learners list risks but write weak controls, such as "be careful" or "monitor the model". A control must be specific: who does what, how often, and what happens if a limit is reached. Also, do not give every risk a score of 1 to make the proposal look safe. Committees trust honest registers more.

## Key Takeaways
1. A risk register records each risk with its category, likelihood, impact, score, controls, owner and residual rating.
2. Cover fairness, privacy, explainability, security, third-party and operational risks, with specific controls for each.
3. End with a clear go, pilot or no-go recommendation, and give any pilot an end date, measures and a named decision-maker.

## Hands-on Exercise
**Task:** Capstone step 2: complete the risk and compliance assessment in Google Sheets and finish your proposal with a recommendation.
**Tools:** Google Sheets (free); the course's risk-register template; your proposal from L13; the capstone rubric.
**Steps:**
1. Copy the risk-register template with the columns shown in this lesson.
2. Add at least 6 risks, at least one from each of the six categories.
3. Score likelihood and impact from 1 to 3, and calculate the score with a formula.
4. Write a specific control and an owner role for each risk, then give a residual rating.
5. Add a short principles check: for each of the six principles from L11, one line on how your proposal meets it and what must be confirmed locally.
6. Write your recommendation (go, pilot or no-go) in one paragraph, with reasons and, for a pilot, its scope, length and stop rule.
7. Check your work against the capstone rubric and submission checklist before you submit.
**What good looks like:** A complete register with honest scores and specific controls, a principles check, and a recommendation that follows logically from the highest risks.
**Time:** about 60 minutes

## Review Flags
- [REGION] Consent and data processing requirements for using client data with an external AI service differ by country; confirm with local data protection law.
