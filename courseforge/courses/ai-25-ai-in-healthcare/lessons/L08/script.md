# L08 Generative AI in Clinical Work: Uses and Limits | Presenter Script

Course: AI-25 · Video: 5 min · Words: 688

## Hook
An AI summary of a long discharge note reads perfectly. It is clear, well organised and confident. It also says the patient's allergy is none known, when the note says penicillin. How would you catch that?

## Explain
In the last lesson, we used generative AI to draft messages for patients. Now we look at clinical work itself. Large language models are used to summarise notes, for example into a short handover. They draft referral or discharge letters that a clinician edits and signs. And they support literature searches, by suggesting search terms or summarising abstracts that a person then reads.

These uses can save time. But language models have four typical failure types. Omission, where an important fact is left out, such as an allergy or a pending result. Invention, often called hallucination, where the model adds a fact that is not in the source. Distortion, where a fact is changed, such as left becoming right. And loss of uncertainty, where possible pneumonia becomes pneumonia.

Because these errors look fluent, they are easy to miss. So every output needs review by a qualified person, who checks it against the source before it is used. The clinician who signs the document remains responsible for its content.

There is also a firm privacy rule. Identifiable patient data must never be pasted into public AI tools. Depending on their terms and settings, free plans may store conversations. Clinical use of real patient data needs a tool your organisation has approved, with the right contracts and data protection. In this course, you only use synthetic notes.

Here is a simple way to picture it. A language model summary is like a first draft from a fast new junior colleague, who writes confidently even when unsure. The draft saves time. But the senior clinician reads it line by line against the record before signing.

## Demonstrate
Let's see this with an example. Doctor Mei Takahashi is a hospital doctor in Japan, testing whether an AI assistant could help draft discharge summaries. She uses a synthetic note written for training, about a sixty-seven-year-old patient admitted with pneumonia.

Among other facts, the note records a penicillin allergy, oxygen stopped on day three, high blood glucose to be checked by the family doctor, and a chest X-ray to repeat in six weeks. Keep those four facts in mind.

She asks the assistant to summarise the note in under one hundred and twenty words for the family doctor, using only information in the note. Then she audits the summary against the note, line by line, with four columns: correct, omitted, invented and distorted.

Here is what she finds. Omitted: the request for the family doctor to check blood glucose. Invented: discharged on oral amoxicillin, a penicillin-type antibiotic that is not in the note, and unsafe for this patient. Distorted: repeat chest X-ray in six months, instead of six weeks. Correct: the diagnosis, the allergy, oxygen stopped, and the length of stay.

The invented antibiotic could cause harm if a busy reader trusted it. Mei concludes that a tool like this might save time only inside an approved system, with a mandatory line-by-line check.

A common mistake is to check an AI summary by reading it and asking, does this sound right? Fluent text almost always sounds right. Check it against the source, fact by fact. A quick read will not find omissions at all, because you cannot see what is not there.

## Recap
Let's recap. First, generative AI can help summarise notes, draft letters and support literature searches, but it can omit, invent or distort facts, and remove uncertainty. Second, every output must be checked against the source by a qualified person, who stays responsible for the final document. Third, never paste identifiable patient data into public AI tools.

## CTA
Now it is your turn. In the exercise below this video, you will summarise the course's synthetic discharge note with an AI assistant, then audit the summary for errors, missing facts and invented details. It takes about thirty minutes. In the next lesson, we look at bias, equity and dataset shift. See you there.

## Thumbnail
Headline: Fluent Is Not Correct
Image: Navy background, a neat AI summary card beside a longer note, with one line on each linked by a teal line and a red mark on the mismatch, headline in teal Inter Bold.

## Production Notes
- Clinical reviewer sign-off required.
- A clinical reviewer should confirm that the synthetic pneumonia note and the audit contain no clinical advice and that the 'invented antibiotic' example (oral amoxicillin, a penicillin-type antibiotic, unsafe with a recorded penicillin allergy) is described correctly (content.md Review Flags).
- On-screen note: use only the course file assets/L08_synthetic_discharge_note.md (fictional patient Taro Sample, Brookfield General Hospital), with its 'FICTIONAL TEXT FOR TEACHING ONLY' banner visible. That file carries its own [VERIFY] clinical reviewer approval flag, which must be cleared before release. NEVER show assets/L08_instructor_notes.md on screen.
- The AI summary and its errors shown on the audit slide are the hypothetical results described in content.md (omitted glucose check, invented oral amoxicillin, six months instead of six weeks). Build them as a slide; do not present them as live output of any named tool.
- [VERSION] Data-use and retention terms of free AI assistant plans (whether conversations are stored or used for training, and available settings) must be checked for each tool before recording. The voiceover only says free plans may store conversations depending on their terms.
- Dr. Mei Takahashi (Japan) is fictional.
