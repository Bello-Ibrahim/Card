# L11 Regulation, Privacy and Ethics Frameworks

Course: AI-25 · Module: M3 · Objectives: O5 · Video: 5 min

## Hook
Is your AI tool a medical device? Can patient photos leave the country? The answers depend on where you are, but the questions are almost the same everywhere. This lesson teaches the questions.

## Explanation
Rules differ by country and change over time, so this course teaches the common principles found in most frameworks, not the rules of one country.

**1. Software as a medical device.** In many countries, software that is intended to diagnose, treat, monitor or prevent disease can be regulated as a medical device, even with no hardware. The **intended use** is central: the same software may be regulated or not, depending on what the manufacturer says it is for. A scheduling tool is usually not a medical device; a tool that flags possible cancer on images usually is.

**2. Risk-based classification.** Regulators usually place devices in risk classes. A tool that informs a serious diagnosis or drives treatment is usually in a higher class, with stricter evidence and oversight, than one that supports low-risk decisions.

**3. Data protection.** Health data is usually treated as a special or sensitive category. Common requirements include a lawful basis for processing, collecting only the data needed, security, limits on transfer across borders, and rights for patients to access their data.

**4. Consent.** Depending on the law and the use, patients may need to give consent, be informed, or be able to object. Consent for care is not automatically consent for training an AI model.

**5. Transparency.** Patients and clinicians should know when AI is used, what it is for and what its limits are.

**6. Accountability.** There must be clear responsibility for the tool's performance, for decisions made with it, and for reporting and fixing problems.

International guidance brings these principles together. An example is the WHO guidance on ethics and governance of artificial intelligence for health [VERIFY], which sets out principles such as protecting human autonomy, promoting well-being and safety, transparency, accountability, and inclusiveness and equity.

Named regulators and laws are **examples only**, to show what such rules can look like:

- Oversight of software as a medical device by the US Food and Drug Administration (FDA) [REGION] [VERIFY].
- The EU Medical Device Regulation (EU MDR) and the EU AI Act, which treats some AI medical tools as high-risk [REGION] [VERIFY].
- Data protection laws such as HIPAA in the United States, the GDPR in the European Union, and Kenya's Data Protection Act [REGION] [VERIFY].

Always confirm local rules with your organisation's regulatory affairs lead or data protection officer.

**Analogy:** Regulation is like building safety codes. The details differ from city to city, but every code asks similar questions: what is the building for, how many people will use it, what happens in a fire, and who signs off.

## Worked Example
Achieng Otieno is the product lead for a hypothetical health-tech start-up in Kenya. Her team is building a tool that suggests which antenatal patients may need earlier review, for midwives to consider. She plans to sell it in Kenya and possibly in Europe.

She does not try to become a lawyer. Instead, she uses the six principles to prepare questions:

- **Medical device:** "Our intended use is to support midwives in prioritising review. Does this make it a medical device here, and in which risk class?" (to check locally)
- **Data protection:** "Is antenatal data a sensitive category? Can we store it with a cloud provider outside the country?" (to check locally)
- **Consent:** "Do we need separate consent to use past records to train the model?" (to check locally)
- **Transparency:** "What must we tell patients about the tool?" (to check locally)
- **Accountability:** "If the tool misses a high-risk patient, who is responsible, and how do we report it?" (to check locally)

She takes the list to the company's legal adviser and a data protection specialist. For Europe, she plans separate advice.

## Common Mistake
Many teams believe that if a tool is only "decision support" and a clinician makes the final decision, it cannot be a medical device. This is often not true. Many frameworks regulate decision support software based on its intended use and risk, even when a clinician remains responsible. Do not decide this yourself; ask your regulatory lead.

## Key Takeaways
1. Common principles across frameworks are: software as a medical device, risk-based classification, data protection, consent, transparency and accountability.
2. Intended use is central to whether and how a tool is regulated.
3. Named laws and regulators are examples; always confirm local rules with your regulatory or data protection officer.

## Hands-on Exercise
**Task:** For one AI health tool category, write a list of questions for your local regulator or data protection officer, and mark each one as "to check locally".
**Tools:** Pen and paper or any notes app. Optional: Claude or ChatGPT (free plan) to suggest extra questions; do not ask it for a final legal answer and do not enter patient data.
**Steps:**
1. Choose one tool category, for example image-reading support, a missed-appointment model, a patient message assistant or a note-summarising tool.
2. Write a one-sentence intended use statement.
3. Write at least one question for each of the six principles.
4. Mark each question "to check locally" and name the role you would ask, such as regulatory affairs lead or data protection officer.
5. Add one question about international data transfer if the tool is hosted in the cloud.
**What good looks like:** At least 7 clear questions covering all six principles, each marked "to check locally" with a named role, and no statement of legal fact without a source.
**Time:** about 20 minutes

## Review Flags
- [VERIFY] WHO guidance on ethics and governance of AI for health: confirm the exact title, year and the list of principles before recording.
- [REGION] [VERIFY] US FDA oversight of software as a medical device.
- [REGION] [VERIFY] EU Medical Device Regulation and EU AI Act, including how AI medical tools are classified.
- [REGION] [VERIFY] HIPAA (US), GDPR (EU) and Kenya's Data Protection Act: confirm names and that they apply to health data as described. No article numbers or dates are given.
