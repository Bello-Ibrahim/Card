# L01 The Landscape of AI in Healthcare

Course: AI-25 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
A nurse opens the morning list and sees that a software tool has moved three patients to the top. Who decided that they should be seen first: the software, the nurse, or the doctor on duty? This course starts with that question, because in healthcare the answer must always be clear.

## Explanation
You already work in or near healthcare, so you know that care depends on data, people and processes. AI is now used in all three. It helps to group the uses into four areas, because each area uses different data and carries different risks.

1. **Diagnostic support.** Tools that help clinicians read images, signals or test results, for example by highlighting a possible abnormality on a scan or flagging a worrying pattern in vital signs. Data: medical images, ECG and other signals, laboratory results, clinical notes.
2. **Operations.** Tools that help the organisation run: scheduling, predicting missed appointments, planning beds and supplies, and drafting documents for staff to review. Data: appointment records, admission and discharge times, stock levels, staff rotas.
3. **Patient engagement.** Tools that talk to patients: reminders, health education and multilingual information services. Data: contact details, preferred language, approved education content, and the messages patients send.
4. **Public health.** Tools that look at populations rather than individuals, for example spotting unusual rises in reported symptoms or helping to plan vaccination outreach. Data: surveillance reports, surveys, anonymised or aggregated records, and sometimes environmental data.

The core principle of this course is simple: **AI supports decisions, and a qualified person remains responsible for them.** A diagnostic support tool can suggest; a clinician decides. An operations tool can predict; a manager decides what to do with the prediction. A patient message service can inform; it passes urgent or complex questions to a human. This course never gives clinical advice, and it never treats AI as a replacement for clinical judgement.

**Analogy:** Think of AI as a well-read assistant who works very fast but has never met the patient. The assistant can point out things worth checking and prepare drafts. The senior clinician still examines the patient, weighs the context and signs the decision.

The same principle helps you ask the right first questions about any tool: What decision does it support? Who makes that decision? What happens if the tool is wrong, and who would notice?

## Worked Example
Here are three hypothetical settings. None of them describes a real organisation.

**A district hospital in Ghana.** Dr. Kwame Asante leads the outpatient department. A diagnostic support tool marks chest X-rays that may need urgent review, so radiology staff can look at those first. The tool does not write the report. The radiologist reads every image and remains accountable for the result. Area: diagnostic support.

**A clinic network in India.** Priya Raghunathan manages 12 primary care clinics. A prediction tool estimates which booked patients are likely to miss their appointment. Priya's team uses this to send extra reminders and offer phone consultations, not to cancel bookings. The clinic manager is accountable for how the predictions are used. Area: operations.

**A telehealth service in Chile.** Valentina Soto coordinates a service that answers patient questions by text message. An AI assistant drafts answers to general questions from content that clinicians have approved. Any message that mentions chest pain, breathing problems or thoughts of self-harm goes straight to a nurse. The clinical lead is accountable for the approved content and the escalation rules. Area: patient engagement.

In each case, the tool changes who sees what and when. It does not remove the person who is responsible.

## Common Mistake
Many people think that a highly accurate tool can make decisions by itself, and that the clinician only needs to check the "difficult" cases. This is not safe. Even an accurate tool makes errors, and those errors are often in the cases that look easy to the tool. Accountability also cannot be passed to software: if a patient is harmed, the organisation and the responsible clinician must answer for the decision. Design every use of AI so that a named person makes, or clearly approves, each decision.

## Key Takeaways
1. AI in healthcare falls into four main areas: diagnostic support, operations, patient engagement and public health, and each uses different types of data.
2. AI supports decisions; a qualified person remains responsible for every clinical and operational decision.
3. For any tool, ask what decision it supports, who makes that decision, and how errors would be noticed.

## Hands-on Exercise
**Task:** Sort 8 AI health applications into the four areas and, for each one, name the person who is accountable for the final decision.
**Tools:** Pen and paper or any notes app. Optional: Claude or ChatGPT (free plan) to compare your answers. Do not enter any patient information.
**Steps:**
1. Read these 8 hypothetical applications: (a) a tool that highlights possible fractures on X-rays; (b) a model that predicts next month's demand for insulin; (c) a text service that reminds patients about vaccination dates; (d) a dashboard that detects unusual rises in fever reports across districts; (e) a tool that drafts discharge letters for doctors to edit; (f) a chatbot that answers questions about clinic opening hours and preparation for a blood test; (g) a model that flags ECGs that may show an irregular rhythm; (h) a model that suggests which villages to visit first in a vaccination campaign.
2. Write the area for each: diagnostic support, operations, patient engagement or public health.
3. For each, write the role of the person accountable for the final decision, for example "reporting radiologist" or "pharmacy manager".
4. Optional: ask an AI assistant to sort the same list and note where it disagrees with you.
**What good looks like:** Every application has one area and one named role. Diagnostic tools (a, g) name a clinician. Operations (b, e) name a manager or the doctor who signs the letter. Patient engagement (c, f) names a clinical lead for content and escalation. Public health (d, h) names a public health officer.
**Time:** about 15 minutes

## Review Flags
- None. All settings and tools are hypothetical and no specific facts, figures or rules are stated.
