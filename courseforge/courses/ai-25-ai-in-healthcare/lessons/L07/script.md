# L07 AI for Patient Engagement | Presenter Script

Course: AI-25 · Video: 5 min · Words: 686

## Hook
A patient sends a message at eleven at night. I have a bad headache since my new tablets. Should I stop them? The clinic's automated service replies within seconds. What should that reply say, and what must it never say?

## Explain
In the last lesson, we saw operational AI working behind the scenes. Now we look at a different kind of tool, the kind that talks directly to patients. Common uses are reminders for appointments, vaccinations and tests, health education in plain language, and information services that answer general questions in the patient's preferred language.

Generative AI makes these tools faster to build, but it adds risk. A language model can write fluent text that is wrong, out of date, or unsuitable for the patient. So these tools need clear limits. First, they do not diagnose or give individual clinical advice. Second, they work only from a source that a clinician has approved.

Third, they pass urgent or complex questions to a human. Possible emergencies, medicine changes, pregnancy concerns, or anything the tool cannot match to approved content goes to a qualified person. Fourth, every language version is checked by a qualified speaker. Fifth, staff never paste identifiable patient information into public AI tools.

Here is a simple way to picture it. A patient engagement tool is like a well-trained clinic receptionist. The receptionist can remind you of your appointment, give you the approved leaflet, and explain the opening hours. When you describe a worrying symptom, a good receptionist does not guess. They get a nurse.

## Demonstrate
Let's see this in practice. Youssef Benali is a nurse educator for a hypothetical community health service in Morocco. Patients speak Moroccan Arabic or French, and many prefer short messages. The service wants education messages about preparing for a fasting blood test.

First, the laboratory lead, Doctor Salma Idrissi, writes a short source text in French and approves it. Then Youssef pastes only that approved text, with no patient details, into an AI assistant. He asks for a plain-language text message of no more than three hundred characters, in French and in Arabic, using only the facts in the source.

Next, he checks each draft against the source. The French draft is accurate. But the Arabic draft adds a sentence saying that you may drink tea without sugar. This is not in the source, so Youssef removes it. Then a colleague who is a native Arabic speaker checks the wording, and changes one formal word to one patients use every day.

Youssef also writes an escalation list. Questions about stopping or changing medicines, feeling unwell while fasting, pregnancy, diabetes medicines, or anything not covered by the source must go to a nurse. Every message ends with the clinic's phone number and a line on how to get emergency help. Finally, Doctor Idrissi approves both versions before use.

The AI saved drafting time. The safety came from the approved source, the checks and the escalation rules. And here is a common mistake. Teams think that if the AI sounds medical, its extra details are helpful. Treat every added fact as an error until a clinician approves it, and check each language separately.

## Recap
Let's recap. First, patient engagement tools send reminders, education and multilingual information, but they do not diagnose or give individual clinical advice. Second, draft from a clinician-approved source, check every language version against it, and get clinical sign-off before use. Third, decide in advance which situations go to a human, and make the route to urgent help clear.

## CTA
Now it is your turn. In the exercise below this video, you will use Claude or ChatGPT to draft a reminder and a short leaflet in two languages, from the course's approved sample source text for a fictional clinic.

You will check both drafts against the source, and list the situations that must go to a human. Then you will note who would need to approve the final versions in a real service. It takes about thirty minutes. In the next lesson, we look at generative AI in clinical work, its uses and its limits. See you there.

## Thumbnail
Headline: Inform, Never Diagnose
Image: Navy background, a phone showing two short message bubbles in French and Arabic script shapes, with a small nurse icon on a teal arrow beside it, headline in teal Inter Bold.

## Production Notes
- Clinical reviewer sign-off required.
- A clinical reviewer should confirm that the fasting blood test preparation content and the escalation list are appropriate illustrations and contain no individual clinical advice (content.md Review Flags). The script never tells patients what to do about their own medicines; it only says such questions go to a nurse.
- The hook message ('headache since my new tablets') is a fictional example. Do not answer it on screen; the only on-screen answer is that the question goes to a human.
- The exercise slide shows the course file assets/L07_sample_source_text.md (fictional Brookfield Community Clinic). Keep its 'FICTIONAL TEXT FOR TEACHING ONLY' banner visible. That file carries its own [VERIFY] clinical reviewer approval flag, which must be cleared before release.
- Youssef Benali, Dr. Salma Idrissi and the Moroccan service are hypothetical. Arabic and French text on slides must be checked by a native speaker before recording; if unavailable, show neutral placeholder text shapes rather than real words.
- Do not show any real messaging app brand or logo on the phone mock-ups.
