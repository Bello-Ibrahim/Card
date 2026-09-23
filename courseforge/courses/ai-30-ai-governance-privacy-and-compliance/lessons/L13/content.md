# L13 Drafting the AI Governance Policy

Course: AI-30 · Module: M3 · Objectives: O6 · Video: 5 min

## Hook
An AI tool can write a ten-page AI policy in less than a minute. It will look professional. It may also cite laws incorrectly, invent duties and describe processes your organisation does not have. Your job is not to generate the policy. Your job is to make it true.

## Explanation
This lesson is educational and is not legal advice. A policy you draft in this course is a learning exercise and must be reviewed by qualified advisers before any real use.

A good AI governance policy is short, specific and usable. It tells staff what they must do, not only what the organisation believes. Use this outline:

**Policy outline template**
1. **Purpose and scope:** why the policy exists; which systems, teams, locations and suppliers it covers (built, bought and embedded AI).
2. **Definitions:** AI system, system owner, high-risk use and other key terms, aligned with the laws you follow.
3. **Principles:** the organisation's short list of commitments.
4. **Roles and responsibilities:** accountable executive, AI governance group, DPO, system owners and all staff.
5. **Approval process:** the lifecycle gates from intake to retirement, and who approves at each risk level.
6. **Acceptable and prohibited uses:** examples of allowed uses; uses that are banned by law; uses the organisation bans by choice.
7. **Personal data rules:** lawful basis, minimisation, transparency, rights handling, transfers, and a clear rule that staff must not paste personal or confidential data into unapproved AI tools.
8. **Assessment triggers:** when a DPIA, an AI Act assessment or a classification review is required.
9. **Training:** who needs which training, and how often.
10. **Monitoring and incidents:** added in L14.
11. **Review cycle and ownership:** who owns the policy and how often it is reviewed.

**Using Claude for a first draft.** Claude can speed up the first draft of a section. Features and interface may change [VERSION]. A safe approach:

1. Give Claude the outline, a free template's structure and fictional facts about the organisation only. Never paste confidential documents or personal data.
2. Ask for plain-language clauses, with placeholders instead of article numbers or deadlines.
3. Check every clause yourself against the official legal texts and the organisation's real facts.
4. Mark what you changed and why. This record shows your professional judgement.

A sample prompt: "Draft the 'Roles and responsibilities' section of an AI governance policy for a fictional logistics company with offices in the Netherlands and Nigeria. Use plain English, short numbered clauses, and write [placeholder] wherever a legal reference or deadline would appear. Do not invent legal requirements."

**Analogy:** An AI first draft is like a junior colleague's draft on their first day. It saves you time and gives you a structure, but you would never send it to the board without reading every line, checking the facts and correcting what they could not know.

## Worked Example
Diego Álvarez is legal counsel at Velmora Tradeways Ltd, the fictional capstone organisation. He uses Claude to draft section 6, "Acceptable and prohibited uses".

The draft is clear and well organised. Diego then reviews it clause by clause:

- **Kept:** "Staff may use approved AI tools to draft internal documents, provided a person reviews the output before use."
- **Changed:** the draft said "Employees must obtain consent before using AI on customer data." Consent is not always the right lawful basis (L07). Diego rewrites: "Any new use of customer data in an AI system requires a documented lawful basis, confirmed by the DPO."
- **Removed:** the draft cited a specific article number for prohibited practices. Diego replaces it with "[prohibited practices under the EU AI Act, see legal register]" [VERIFY] [REGION].
- **Added:** a Velmora-specific ban on using the driver-monitoring camera for performance ratings, which the AI could not know about.

He keeps a change log: 14 clauses drafted, 6 kept, 5 changed, 2 removed, 1 added.

## Common Mistake
Many people check an AI-drafted policy only for style and grammar. The dangerous errors are in the substance: invented duties, wrong legal references and processes the organisation does not have. A policy that describes processes that do not exist is worse than no policy, because it creates a record of promises you do not keep. Check every clause against the law and the facts.

## Key Takeaways
1. A good AI governance policy covers scope, principles, roles, approval, acceptable and prohibited uses, personal data rules, assessment triggers, training and review.
2. Claude can produce a useful first draft from fictional facts and a template, but never paste personal or confidential data into it.
3. Every AI-drafted clause must be checked by a person against the law and the organisation's facts; this course is educational, not legal advice.

## Hands-on Exercise
**Task:** Capstone step 2: draft a 2–3 page AI governance policy for the sample organisation, starting from a free policy template and using Claude for a first draft of at least one section, then mark what you changed.
**Tools:** A free AI policy template from an official or reputable source [VERIFY]; Claude (free plan) [VERSION]; a word processor with track changes.
**Steps:**
1. Build your document using the 11-section outline above. Leave section 10 as a heading for L14.
2. Choose at least one section and ask Claude for a first draft, using only fictional Velmora facts.
3. Paste the draft into your document and turn on track changes.
4. Review every clause against the laws and Velmora's facts. Keep, change, remove or add.
5. Write a short change log at the end: what you changed and why.
6. Use placeholders for all article numbers, deadlines and penalty figures.
**What good looks like:** A 2–3 page policy that is specific to Velmora, with visible tracked changes on the AI-drafted section, a clear change log and no unverified legal references.
**Time:** about 60 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERSION] Claude interface, features and free-plan availability may change; check before scripting. No screen demo is proposed (curriculum flag).
- [VERIFY] [REGION] The placeholder for prohibited practices must remain a placeholder unless verified against the official text.
- [VERIFY] The free policy template must be chosen from an official or reputable source, with licence and date recorded.
- Fictional organisation: "Velmora Tradeways Ltd" must be checked so it does not match a real company (see L11).
