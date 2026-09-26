# L10 Impact Assessments: DPIAs and AI Risk Assessments | Presenter Script

Course: AI-30 · Video: 5 min · Words: 686

## Hook
A project team says, the system is ready, we just need you to sign the DPIA by Friday. If the assessment starts when the system is finished, it can only describe risks, not prevent them. So when should it start?

## Explain
In the last lesson, we handled rights requests. Today, we look at impact assessments, and how to judge whether the remaining risk is acceptable. This lesson is educational and is not legal advice. When each assessment is required, and what it must contain, must be checked for each law.

Under both the GDPR and the NDPA, a data protection impact assessment, or DPIA, is required when processing is likely to result in a high risk to people's rights and freedoms. Many AI uses meet that test, because they often involve new technology, large-scale data, profiling, automated decisions, sensitive data or monitoring.

A DPIA usually has four parts. First, a description of the processing, its purpose, data, people affected and recipients. Second, necessity and proportionality: why the processing is needed, its lawful basis and how rights are respected. Third, the risks to people, rated by likelihood and severity.

Fourth, the measures that reduce each risk, and the residual risk that remains after them. If high residual risk remains, you may need to consult the regulator before you start.

The EU AI Act adds its own assessment. Some deployers of high-risk systems must carry out a fundamental rights impact assessment before use. It looks wider than privacy, at issues like non-discrimination and access to services. It can build on an existing DPIA, and many organisations combine both in one process.

To judge residual risk, ask three questions. After the controls, is the remaining risk low enough, given the benefit? Is it within the organisation's risk appetite? Are the people affected protected by meaningful safeguards? Then record who made the judgement, and why.

Think of an architect's structural review, done while the plans are still on paper. Moving a wall at the drawing stage costs little. Moving it after the building is finished is expensive, and sometimes impossible. So start the assessment while the design can still change.

## Demonstrate
Let's look at a short DPIA. Thandiwe Mokoena is privacy manager for a fictional company whose office in Johannesburg plans a facial-recognition entry system to replace staff access cards. Local data protection law must also be checked.

Description: cameras match the faces of about three hundred staff against enrolled templates, which is biometric data used for identification. Necessity: cards work but are often shared. Would a card plus a PIN be enough? And staff may feel they cannot refuse their employer.

Risks: leaked biometric templates, which is high severity. False rejections that affect some groups more than others. And function creep, such as using the cameras to track attendance.

Measures: a card-plus-PIN alternative with no disadvantage, encrypted templates stored on-site and deleted when staff leave, error-rate tests across groups, and a written ban on using the system for attendance. With these, Thandiwe rates the residual risk as medium, and recommends a volunteer pilot with a review after three months.

A common mistake is to treat a DPIA as a form to complete at the end. Its value is in the changes it causes. Another mistake is to rate risks to the organisation, such as fines, instead of risks to people. A DPIA must focus on the people affected.

## Recap
Let's recap. First, a DPIA is required when processing is likely to result in high risk to people, and many AI uses meet that test. Second, some deployers of high-risk AI systems must also carry out a fundamental rights impact assessment, which can be combined with the DPIA. Third, start early, focus on people, and record who judged the residual risk acceptable.

## CTA
In the exercise below this video, you will complete a free DPIA template for a fictional AI chatbot that handles customer complaints. Then judge whether the remaining risk is acceptable, and explain why.

That completes module two. In the next lesson, we start building: designing an AI governance framework. See you there.

## Thumbnail
Headline: Assess Before You Build
Image: Navy background, an architect's blueprint with a teal magnifying glass over one wall, headline in teal Inter Bold.

## Production Notes
- Legal/compliance reviewer sign-off required before release.
- Disclaimer spoken once in scene 2 (educational, not legal advice).
- [VERIFY] [REGION] DPIA: content.md placeholders [the GDPR DPIA article] and [the NDPA impact assessment section]. When a DPIA is mandatory, its required content and regulator lists of high-risk processing (scenes 3 and 4) must be checked.
- [VERIFY] [REGION] Prior consultation with the regulator where high residual risk remains (scene 5) must be checked. No regulator is named.
- [VERIFY] [REGION] Fundamental rights impact assessment: content.md placeholder [the EU AI Act fundamental rights impact assessment article]. Which deployers must carry it out, and how it can build on a DPIA (scene 6), must be checked.
- [VERIFY] [REGION] Applicable South African data protection law for the Johannesburg worked example must be noted by the legal reviewer. The voiceover says only that local law must also be checked (scene 9).
- [VERIFY] The free DPIA template for the exercise must be chosen from an official source, with licence and date recorded.
- Thandiwe Mokoena and the Johannesburg office are fictional. The three-month pilot review is the fictional company's own choice, not a legal deadline. Stock footage of face scanners must not show a real product brand.
