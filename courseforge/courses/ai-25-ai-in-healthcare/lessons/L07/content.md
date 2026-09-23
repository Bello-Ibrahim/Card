# L07 AI for Patient Engagement

Course: AI-25 · Module: M2 · Objectives: O3 · Video: 5 min

## Hook
A patient sends a message at 11 at night: "I have a bad headache since my new tablets. Should I stop them?" The clinic's automated service replies within seconds. What should that reply say, and what must it never say?

## Explanation
Patient engagement tools communicate directly with patients. Common uses are:

- **Reminders** for appointments, vaccinations, medicine refills and tests.
- **Health education** in plain language, such as how to prepare for a procedure or how to use an inhaler, based on content clinicians have approved.
- **Multilingual information services** that answer general questions in the patient's preferred language.

Generative AI makes these tools faster to build, but it adds risk. A language model can produce fluent text that is wrong, out of date or unsuitable for the patient. So patient engagement tools need clear limits:

1. **They do not diagnose or give individual clinical advice.** They give general, approved information.
2. **They work from an approved source.** Messages are drafted from content a clinician has checked, not from the model's general knowledge.
3. **They pass urgent or complex questions to a human.** A defined list of situations, such as possible emergencies, medicine changes, pregnancy concerns, mental health crisis or any question the tool cannot match to approved content, goes to a qualified person, with clear instructions on how to get urgent help.
4. **Every language version is checked.** A qualified speaker, ideally with health knowledge, compares each translation with the source.
5. **Personal data is protected.** Staff never paste identifiable patient information into public AI tools when drafting content.

**Analogy:** A patient engagement tool is like a well-trained clinic receptionist. The receptionist can remind you of your appointment, give you the approved leaflet and explain the clinic's opening hours. When you describe a worrying symptom, a good receptionist does not guess; they get a nurse.

## Worked Example
Youssef Benali is a nurse educator for a hypothetical community health service in Morocco. Patients speak Moroccan Arabic or French, and many prefer short messages. The service wants education messages about preparing for a fasting blood test.

1. **Approved source.** The laboratory lead, Dr. Salma Idrissi, writes a short source text in French and approves it: when to stop eating, that water is allowed, to bring the request form, and to ask the clinic about regular medicines rather than stopping them alone.
2. **Drafting.** Youssef pastes only the approved text, with no patient details, into an AI assistant and asks for a plain-language SMS of no more than 300 characters in French and in Arabic, using only the facts in the source.
3. **Checking against the source.** The French draft is accurate. The Arabic draft adds a sentence that "you may drink tea without sugar". This is not in the source. Youssef removes it.
4. **Language review.** A colleague who is a native Arabic speaker checks the wording for clarity and tone, and changes one formal word to one patients use every day.
5. **Escalation list.** Youssef writes the situations that must go to a nurse: questions about stopping or changing medicines, feeling unwell while fasting, pregnancy, diabetes medicines, or any question not covered by the source. The message ends with the clinic's phone number and a line on how to get emergency help.
6. **Sign-off.** Dr. Idrissi approves both final versions before use.

The AI saved drafting time. The safety came from the approved source, the checks and the escalation rules.

## Common Mistake
Many teams think that if the AI "sounds medical", its extra details are helpful. Additions that are not in the approved source, even small and reasonable-sounding ones like the tea example, are unapproved clinical content. Treat every added fact as an error until a clinician approves it. Check each language version separately, because errors often appear in only one.

## Key Takeaways
1. Patient engagement tools send reminders, education and multilingual information, but they do not diagnose or give individual clinical advice.
2. Draft from a clinician-approved source, check every language version against it, and get clinical sign-off before use.
3. Define in advance which situations go to a human, and make the route to urgent help clear in every message.

## Hands-on Exercise
**Task:** Use Claude or ChatGPT to draft a plain-language appointment reminder and a short education leaflet in two languages from an approved source text. Check both against the source and list the situations that must go to a human.
**Tools:** Claude or ChatGPT (free plan); the course's approved sample source text on preparing for a clinic visit (or a public education leaflet from your own health service); a notes app. Do not enter any patient names, numbers or health details.
**Steps:**
1. Choose two languages you can read, or one you can read and one a colleague can check.
2. Ask the assistant to draft an SMS reminder (no more than 300 characters) and a leaflet (no more than 150 words) in both languages, using only facts from the source.
3. Compare every sentence of each draft with the source. Highlight any fact that was added, removed or changed.
4. Correct the drafts. Record each correction and why you made it.
5. Write a list of at least five situations that must go to a human, and the route for each (for example "clinic nurse by phone" or "emergency services").
6. Note who would need to approve the final versions in a real service.
**What good looks like:** Four short drafts, a correction log showing at least one change, all facts traceable to the source, a clear escalation list including possible emergencies and medicine questions, and a named approval role.
**Time:** about 30 minutes

## Review Flags
- Clinical reviewer sign-off required.
- The Moroccan service, staff and blood-test source text are hypothetical. A clinical reviewer should confirm that the example preparation content and the escalation list are appropriate illustrations and contain no individual clinical advice.
