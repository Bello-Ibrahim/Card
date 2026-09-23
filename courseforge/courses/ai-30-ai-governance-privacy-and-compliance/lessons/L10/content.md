# L10 Impact Assessments: DPIAs and AI Risk Assessments

Course: AI-30 · Module: M2 · Objectives: O5 · Video: 5 min

## Hook
A project team says, "The system is ready. We just need you to sign the DPIA by Friday." If the assessment starts when the system is finished, it can only describe risks, not prevent them. When should it start, and how do you decide whether the remaining risk is acceptable?

## Explanation
This lesson is educational and is not legal advice. When each assessment is mandatory, and what it must contain, is set out in [the GDPR DPIA article], [the NDPA impact assessment section] and [the EU AI Act fundamental rights impact assessment article] [VERIFY] [REGION].

**The DPIA.** Under both the GDPR and the NDPA, a data protection impact assessment is required when processing is likely to result in a high risk to people's rights and freedoms [VERIFY] [REGION]. Many AI uses meet that test, because they often involve new technology, large-scale data, profiling, automated decisions, sensitive data or monitoring. EU regulators publish lists of processing that needs a DPIA [VERIFY] [REGION].

A DPIA usually contains four parts:

1. **Description:** the processing, its purpose, data, people affected, systems and recipients.
2. **Necessity and proportionality:** why the processing is needed, the lawful basis, minimisation and how rights are respected.
3. **Risks to people:** what could go wrong for individuals, such as discrimination, loss of privacy, wrong decisions or security breaches, rated by likelihood and severity.
4. **Measures and residual risk:** controls that reduce each risk, and the risk that remains after them. If high residual risk remains, prior consultation with the regulator may be required [VERIFY] [REGION].

**The AI Act assessment.** The EU AI Act requires some deployers of high-risk systems to carry out a **fundamental rights impact assessment (FRIA)** before use [VERIFY] [REGION]. It looks wider than privacy, for example at non-discrimination, fair treatment and access to services. Where a DPIA already exists, the FRIA can build on it [VERIFY] [REGION]. Many organisations combine both into one process with one set of documents.

**Judging residual risk.** Ask: after the controls, is the remaining risk low enough given the benefit? Is it within the organisation's stated risk appetite? Are the people affected protected by meaningful safeguards? Record who made the judgement and why.

**Analogy:** A DPIA is like an architect's structural review done while the plans are still on paper. Moving a wall at the drawing stage costs little. Moving it after the building is finished is expensive, and sometimes impossible. Start the assessment when the design can still change.

## Worked Example
Thandiwe Mokoena is privacy manager for a hypothetical company whose office in Johannesburg plans a facial-recognition entry system to replace staff access cards. The company applies its group DPIA method; South African data protection law must also be checked [VERIFY] [REGION].

- **Description:** cameras match staff faces against enrolled templates to open doors. About 300 staff. Biometric data used for identification.
- **Necessity:** access cards work but are often shared. Is face recognition necessary, or would a card plus PIN be enough? Staff may feel they cannot refuse, because the employer holds power over them.
- **Risks:** biometric templates leaked (high severity); false rejections that affect some groups more than others; function creep, such as using the cameras to track attendance.
- **Measures:** offer a card-plus-PIN alternative with no disadvantage; store templates encrypted on-site; delete them when staff leave; test error rates across groups; a written rule forbidding use for attendance or performance.
- **Residual risk:** with a genuine alternative and strict purpose limits, Thandiwe rates it medium. She recommends a pilot with volunteers only, and a review after three months.

## Common Mistake
Many teams treat a DPIA as a form to complete at the end. The value of a DPIA is in the changes it causes. If your DPIA did not change anything in the design, either the system was already well designed or the assessment was too late or too shallow. Another mistake is to rate risks to the organisation (fines, reputation) instead of risks to people. A DPIA must focus on the people affected.

## Key Takeaways
1. A DPIA is required when processing is likely to result in high risk to people, and many AI uses meet that test.
2. Some deployers of high-risk AI systems must also carry out a fundamental rights impact assessment, which can be combined with the DPIA in one process.
3. Start early, focus on risks to people, and record who judged the residual risk acceptable and why; this lesson is educational, not legal advice.

## Hands-on Exercise
**Task:** Complete a free DPIA template for a hypothetical AI chatbot that handles customer complaints, then judge whether the remaining risk is acceptable and explain why.
**Tools:** A free DPIA template from an official data protection regulator [VERIFY]; a word processor.
**Steps:**
1. Scenario: a water utility in Kenya and Ireland uses a chatbot to receive complaints, summarise them and route them to staff. Customers sometimes mention health problems.
2. Complete the description and necessity sections.
3. List at least 4 risks to people and rate each by likelihood and severity.
4. Add at least one control for each risk.
5. Write a residual-risk judgement of 4 to 6 sentences: acceptable, acceptable with conditions, or not acceptable, and why.
6. Use invented details only. Do not paste real complaints into any AI tool.
**What good looks like:** A completed template, risks written from the customer's point of view, controls linked to each risk, and a clear, reasoned residual-risk judgement with a named decision-maker role.
**Time:** about 35 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [REGION] When a DPIA is mandatory under the GDPR and the NDPA, required DPIA content, regulator lists of high-risk processing, prior consultation, and the EU AI Act fundamental rights impact assessment duty for certain deployers must be checked (curriculum flag).
- [VERIFY] [REGION] Applicable South African law for the Johannesburg worked example must be noted by the legal reviewer.
- [VERIFY] The free DPIA template must be chosen from an official source, with licence and date recorded.
