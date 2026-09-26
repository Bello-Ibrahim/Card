# L11 Responsible AI Risks and Guardrails | Presenter Script

Course: AI-27 · Video: 5 min · Words: 682

## Hook
Most AI harms do not come from bad intentions. They come from a reasonable feature, used at scale, with a risk nobody wrote down. A risk table with a named owner for each guardrail is one of the most useful documents a PM can write.

## Explain
This is week three. You have a scoped feature, a data plan and an evaluation design. Now we make it safe to launch. Five risk types appear in most AI features.

Unfair outcomes: the feature works worse for some groups, such as speakers of a language, older users or people from certain regions. Privacy: personal data is used or exposed in ways users did not expect. Misuse: people use the feature for harm, such as generating spam or extracting other users' data.

Harmful or false outputs: invented facts, dangerous advice or offensive content. And lack of transparency: users do not know that AI is involved, why it gave a result, or how to challenge it.

Guardrails reduce these risks. Input checks block unsafe or out of scope requests before they reach the model. Output checks filter or flag outputs, such as removing personal data. Human review means a person approves higher risk outputs. Usage limits reduce misuse and control cost. And clear user messages say that AI is involved, and how to reach a person.

Every guardrail needs an owner, a person or team responsible for it working. A guardrail without an owner is often switched off or forgotten.

Legal duties also differ by country, and by how sensitive the use is. This lesson is not legal advice. Write your legal questions down, involve your legal team early, and check the current rules for every country where you launch.

Think of a building. It has smoke detectors, fire doors and exit signs, and someone checks each one regularly. You do not add them after a fire. Guardrails are the safety features of an AI product, and the owners are the people who test the alarms.

## Demonstrate
Let's build a table. Sofie de Vries is a PM at a hypothetical job platform in the Netherlands. Employers want AI to summarise each applicant's CV against the job requirements. Hiring is a sensitive area, so Sofie brings legal in before design. She keeps the scope narrow. The AI summarises, and it never ranks, scores or rejects applicants.

Unfair outcomes: summaries could be weaker for Dutch CVs, or mention age or nationality. The guardrail is a test set in both languages, and an output check that removes those details. The ML lead owns it. Privacy: CV data could be stored by a provider. Legal approves the data terms, and the privacy officer owns it.

False output: a summary claims a skill the CV does not show. So each claim links to its CV line, and Sofie owns that. Misuse: an employer asks which applicant is best. An input check declines ranking requests, owned by the engineering lead. Transparency: applicants are told AI summaries are used, and how to ask for human review.

Sofie adds one more rule to her PRD. Any future plan to rank applicants needs a new legal review before discovery starts.

A common mistake is treating responsible AI as a legal check just before launch. By then, the risky design choices are built. List risks during scoping, and involve legal early, especially in hiring, lending, health and education.

## Recap
Let's recap. First, the main risks are unfair outcomes, privacy, misuse, harmful or false outputs, and lack of transparency. Second, guardrails include input and output checks, human review, usage limits and clear user messages, and each needs a named owner. Third, legal duties differ by country and by use, so check the current rules with your legal team early.

## CTA
Now it is your turn. In the exercise below, complete a risk and guardrail table for your feature, with at least one row for each risk type, and an owner for every guardrail. It takes about twenty five minutes. You will reuse it in your capstone PRD. In the next lesson, we plan the launch: pilots, rollouts and monitoring. See you there.

## Thumbnail
Headline: Guardrails Need Owners
Image: Navy background, a building cross-section with a smoke detector, fire door and exit sign, each with a small name tag, headline in teal Inter Bold.

## Production Notes
- [REGION] [VERIFY] Left out of the voiceover on purpose: content.md's description of the EU AI Act risk levels (prohibited, high-risk with duties such as risk management, human oversight and documentation, transparency duties, few duties for most uses) and the claim that hiring uses are treated as high-risk. A legal reviewer must check these against current official texts before any of it is added to slides or the lesson page.
- [REGION] [VERIFY] Left out of the voiceover: content.md's summary of EU General Data Protection Regulation principles (lawful reason, only the data needed, respecting people's rights). The script says only that legal duties differ by country and must be checked with the legal team.
- In the worked example, content.md says EU rules 'may treat' hiring as high-risk [REGION] [VERIFY]; the voiceover says only that hiring is a sensitive area, so Sofie brings legal in before design.
- [VERSION] Claude free-plan limits and data-use terms must be checked before recording (optional exercise tool).
- Sofie de Vries and the job platform in the Netherlands are hypothetical; stock footage must not show a real job site, CV or logo.
