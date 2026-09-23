# L11 Legal, Ethical and Data Risks

Course: AI-28 · Module: M3 · Objectives: O6 · Video: 5 min

## Hook
Your MVP works and your first customers are happy. Then a customer asks: "Where does my data go? Who owns the text your AI writes? What happens if it gives wrong advice?" If you cannot answer, that customer may leave, and in some cases a regulator may ask the same questions.

## Explanation
This lesson helps you **spot** risks early. It is **not legal advice**. Laws differ by country and change over time, so before you launch, get advice from a qualified lawyer in each country where you operate.

Five areas matter for most AI startups:

**1. Data protection.** Many countries have laws about how organisations collect, store and use **personal data**: information that can identify a person, such as a name, phone number or health record. Common principles include collecting only what you need, telling people how you use it, keeping it secure and deleting it when it is no longer needed. The European Union's GDPR (General Data Protection Regulation) is one well-known example of such a law [REGION] [VERIFY].

**2. Consent.** Consent means a person clearly agrees to something. Ask before you record interviews, use customer data to improve your product, or share data with another company, including your model supplier. Do not hide this in long terms that nobody reads.

**3. Ownership of AI outputs.** Who owns text or images produced with AI, and whether they can be protected by copyright, is still unclear in many countries [REGION] [VERIFY]. Agree in your customer terms who may use the outputs and how.

**4. Model supplier terms.** When you send data to a model supplier, their terms decide how that data may be stored or used, and what uses of the model are not allowed. Read the terms for the plan you use; free and paid plans may differ [VERSION].

**5. Sector rules.** Health, finance, law, education and employment often have extra rules. Some countries also have rules specific to AI. For example, the EU AI Act sorts AI systems by risk level, and uses such as screening job applicants are treated as higher risk, with extra duties such as human oversight and record keeping [REGION] [VERIFY].

There are also **ethical risks** that may not be illegal but can still harm people and your reputation: biased results against some groups, overconfident answers, and replacing human judgement where it is needed.

**Analogy:** Opening a food stall is not only about cooking well. You also need to know the hygiene rules, label allergens, and store food at the right temperature. A great recipe does not protect you if customers become ill. Legal and data risks are the hygiene rules of an AI startup.

## Worked Example
Zofia is a hypothetical founder in Kraków, Poland. Her MVP reads job applications for small companies and suggests which candidates to interview. Because she works in the EU, she uses the GDPR and the EU AI Act as her examples [REGION] [VERIFY]. She fills in a risk checklist:

| Risk | Level | Next step |
|---|---|---|
| Applications contain personal data (names, work history) | High | Get legal advice on data protection duties; collect only what employers need; set a deletion period |
| Screening job applicants may be a higher-risk AI use | High | Ask a lawyer which duties apply; make sure a person makes every final decision |
| Model may favour some groups unfairly (for example, by age or gender) | High | Remove names, photos and ages before AI review; test results across groups; publish how she checks |
| Model supplier terms on data use | Medium | Read the terms for her plan and choose settings that do not allow data to be used for training, if available |
| Ownership of AI-written summaries | Low | State in her terms that customers may use the summaries freely |

Zofia decides to change her product: instead of **ranking** candidates, it will **summarise** each application against the employer's criteria, and a person will make every decision. This reduces risk and keeps her product useful.

## Common Mistake
Many founders think legal questions only matter "later, when we are bigger". But some choices are hard to change later, such as what data you collect and what you promise customers. Another mistake is copying terms and privacy pages from another company. Their business, data and country may be very different from yours. Use them only to learn which topics to cover, and get local advice.

## Key Takeaways
1. Check five areas early: data protection, consent, ownership of AI outputs, model supplier terms and sector rules.
2. Laws differ by country; GDPR and the EU AI Act are examples, not a global standard, and this lesson is not legal advice.
3. Rate each risk as low, medium or high, and give every high risk a concrete next step, such as removing data, adding human review or getting legal advice.

## Hands-on Exercise
**Task:** Complete a risk checklist for your startup and mark each item as low, medium or high risk, with one next step for each high risk.
**Tools:** A free spreadsheet or document; your model supplier's current terms [VERSION]; optional Claude (free plan).
**Steps:**
1. Create a table with columns: risk, area, level, next step.
2. Add at least one risk for each of the five areas, plus one ethical risk.
3. Mark each as low, medium or high. Consider how likely it is and how much harm it could cause.
4. For every high risk, write one specific next step.
5. Optional: describe your product to Claude, without personal or confidential data, and ask: "What legal, ethical and data risks might I be missing? Which questions should I ask a lawyer in my country?" Treat the answer as a list of questions, not as legal advice.
6. Write three questions to ask a local lawyer or a startup legal clinic.
**What good looks like:** A table with at least six risks across all five areas plus ethics, honest levels, specific next steps for every high risk, and three clear questions for a lawyer.
**Time:** about 35 minutes

## Review Flags
- [REGION] [VERIFY] GDPR and the EU AI Act are named only as examples. The descriptions of GDPR principles, the EU AI Act's risk levels, and the treatment of job-applicant screening as a higher-risk use with duties such as human oversight must be checked by a qualified reviewer before recording.
- [REGION] [VERIFY] The statement that ownership and copyright of AI outputs is unclear in many countries must be checked.
- [VERSION] Model supplier terms and data-use settings differ by plan and change over time.
- The lesson states it is not legal advice; this statement must stay in the script.
