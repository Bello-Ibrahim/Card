# L11 Responsible AI Risks and Guardrails

Course: AI-27 · Module: M3 · Objectives: O5 · Video: 5 min

## Hook
Most AI harms do not come from bad intentions. They come from a reasonable feature, used at scale, with a risk nobody wrote down. A risk table with a named owner for each guardrail is one of the simplest and most useful documents a PM can write.

## Explanation
Five risk types appear in most AI features:

1. **Unfair outcomes:** the feature works worse, or decides differently, for some groups, such as speakers of a language, older users or people from certain regions.
2. **Privacy:** personal data is collected, used, stored or exposed in ways users did not expect or agree to.
3. **Misuse:** people use the feature for something harmful, such as generating spam or extracting other users' data.
4. **Harmful or false outputs:** invented facts, dangerous advice or offensive content.
5. **Lack of transparency:** users do not know that AI is involved, why it gave a result, or how to challenge it.

**Guardrails** reduce these risks. Common types:

- **Input checks:** block or redirect unsafe or out-of-scope requests before they reach the model.
- **Output checks:** filter or flag outputs, such as removing personal data or checking that a number matches the source.
- **Human review:** a person approves outputs above a certain risk level.
- **Usage limits:** limits per user or per hour, to reduce misuse and control cost.
- **Clear user messages:** say that AI is involved, what it can and cannot do, and how to report a problem or reach a person.

Every guardrail needs an **owner**: a person or team responsible for it working. A guardrail without an owner is often switched off or forgotten.

**Legal requirements differ by country.** Treat the following as principles to discuss with your legal team, not legal advice. The EU AI Act groups AI uses by risk level: some uses are prohibited, "high-risk" uses have strict duties such as risk management, human oversight and documentation, some uses mainly have transparency duties such as telling people they are interacting with AI, and most other uses have few specific duties [REGION] [VERIFY]. Uses in areas such as hiring are among those treated as high-risk [REGION] [VERIFY]. Data protection laws, such as the EU General Data Protection Regulation, generally require a lawful reason for using personal data, using only the data you need, and respecting people's rights over their data [REGION] [VERIFY]. Check the current rules for every country where you launch.

**Analogy:** A building has smoke detectors, fire doors and exit signs, and each has someone who checks it regularly. You do not add them after a fire. Guardrails are the safety features of an AI product, and the owners are the people who test the alarms.

## Worked Example
Sofie de Vries is a PM at a hypothetical job platform in the Netherlands. Employers want AI to summarise each applicant's CV against the job requirements. Sofie knows that hiring is a sensitive area and that EU rules may treat it as high-risk [REGION] [VERIFY], so she brings legal in before design, and she keeps the scope narrow: the AI summarises, and it never ranks, scores or rejects applicants.

Her risk and guardrail table (part):

| Risk | Example | Guardrail | Owner |
|---|---|---|---|
| Unfair outcomes | Summaries are weaker for CVs in Dutch than in English, or mention age or nationality | Test set with CVs in both languages and different backgrounds; output check that removes age, nationality and photo details | ML lead |
| Privacy | CV data sent to a provider that stores it | Legal approves the provider's data terms; only CV text is sent; no data used for training | Privacy officer |
| Harmful or false output | Summary claims a skill the CV does not show | Each claim links to the CV line it came from; recruiters see the original CV next to it | PM (Sofie) |
| Misuse | Employer asks the AI "which applicant is best?" | Input check that declines ranking requests with a clear message | Engineering lead |
| Transparency | Applicants do not know AI is used | Notice to applicants that AI summaries are used, and how to ask for human review | Legal and PM |

Sofie adds one more rule to her PRD: any future plan to rank applicants needs a new legal review before discovery starts.

## Common Mistake
Teams often treat responsible AI as a legal check at the end, just before launch. By then, the risky design choices are already built. List risks during scoping, design guardrails into the MVP, give each one an owner, and involve legal early, especially in sensitive areas such as hiring, lending, health and education.

## Key Takeaways
1. The main risks are unfair outcomes, privacy, misuse, harmful or false outputs, and lack of transparency.
2. Guardrails include input and output checks, human review, usage limits and clear user messages, and each needs a named owner.
3. Legal duties differ by country and by risk level of the use, so check current rules with your legal team early [REGION] [VERIFY].

## Hands-on Exercise
**Task:** Complete a risk and guardrail table for your feature, with an owner for each guardrail.
**Tools:** Google Sheets or a document; optional: Claude (free plan) to suggest missing risks [VERSION].
**Steps:**
1. Create columns: risk type, specific example in your feature, likelihood (low/medium/high), impact (low/medium/high), guardrail, owner.
2. Add at least one row for each of the five risk types.
3. For each risk, write a specific example, not a general statement.
4. Assign a real role as owner for each guardrail.
5. Note whether your feature is in a sensitive area and which legal question you would ask.
6. Optional: describe your feature to Claude in general terms, without confidential details, and ask what risks are missing.
**What good looks like:** Five or more specific risks, guardrails that match each risk, a named owner for every guardrail, and a clear legal question for your launch countries.
**Time:** about 25 minutes

## Review Flags
- [REGION] [VERIFY] EU AI Act risk categories, the duties for high-risk uses, and whether hiring uses such as CV summaries fall into the high-risk category must be checked by a legal reviewer against current official texts and guidance.
- [REGION] [VERIFY] The description of the EU General Data Protection Regulation principles is a general summary and must be checked.
- [VERSION] Claude free-plan limits and data-use terms must be checked before recording.
