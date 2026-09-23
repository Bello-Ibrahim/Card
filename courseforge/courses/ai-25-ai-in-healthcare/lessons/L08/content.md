# L08 Generative AI in Clinical Work: Uses and Limits

Course: AI-25 · Module: M2 · Objectives: O3, O4 · Video: 5 min

## Hook
An AI summary of a long discharge note reads perfectly. It is clear, well organised and confident. It also says the patient's allergy is "none known", when the note says penicillin. How would you catch that?

## Explanation
Large language models (LLMs) are now used in clinical settings for tasks such as:

- **Summarising notes**, for example turning a long admission record into a short handover summary.
- **Drafting letters**, such as referral or discharge letters that a clinician edits and signs.
- **Supporting literature searches**, by suggesting search terms or summarising abstracts that a person then reads.

These uses can save time. But LLMs have typical failure types that matter greatly in clinical work:

1. **Omission:** an important fact is left out, such as an allergy, a pending test result or a follow-up instruction.
2. **Invention (often called hallucination):** the model adds a fact that is not in the source, such as a medicine, a dose or a reference to a paper that does not exist.
3. **Distortion:** a fact is changed, such as left becoming right, "no chest pain" becoming "chest pain", or a dose changing units.
4. **Loss of uncertainty:** "possible pneumonia" becomes "pneumonia".

Because these errors look fluent, they are easy to miss. So **every output needs review by a qualified person** who checks it against the source before it is used. The clinician who signs the document remains responsible for its content.

There is also a firm privacy rule: **identifiable patient data must never be pasted into public AI tools.** Free plans of AI assistants may store conversations or use them to improve models, depending on their current terms and settings [VERSION]. Clinical use of real patient data needs a tool your organisation has approved, with the right contracts and data protection in place. In this course you only use synthetic notes.

**Analogy:** An LLM summary is like a first draft from a fast new junior colleague who writes confidently even when unsure. The draft saves time, but the senior clinician reads it line by line against the record before signing.

## Worked Example
Dr. Mei Takahashi is a hospital doctor in Japan who is testing whether an AI assistant could help draft discharge summaries. She uses a **synthetic** note, written for training, about a 67-year-old patient admitted with community-acquired pneumonia. The note includes: penicillin allergy (rash); treated with a non-penicillin antibiotic; oxygen stopped on day 3; blood glucose was high during admission and needs checking by the family doctor; chest X-ray to be repeated in six weeks.

She asks the assistant: "Summarise this note in under 120 words for the patient's family doctor. Use only information in the note."

She then audits the summary against the note, line by line, with four columns: correct, omitted, invented, distorted.

- **Omitted:** the request for the family doctor to check blood glucose.
- **Invented:** "discharged on oral amoxicillin", which is a penicillin-type antibiotic not mentioned in the note, and unsafe for this patient.
- **Distorted:** "repeat chest X-ray in 6 months" instead of six weeks.
- **Correct:** diagnosis, allergy, oxygen stopped, length of stay.

One key fact was omitted, one was distorted and one unsafe fact was invented. The invented antibiotic could cause harm if a busy reader trusted it. Mei concludes that a tool like this might save drafting time only inside an approved system, with a mandatory line-by-line check, and that her audit method should be part of any evaluation.

## Common Mistake
Many people check an AI summary by reading it and asking, "Does this sound right?" Fluent text almost always sounds right. The correct method is to check the summary **against the source**, fact by fact, including what is missing. A quick read will not find omissions at all, because you cannot see what is not there.

## Key Takeaways
1. Generative AI can help summarise notes, draft letters and support literature searches, but it can omit, invent or distort facts and remove uncertainty.
2. Every output must be checked against the source by a qualified person, who remains responsible for the final document.
3. Never paste identifiable patient data into public AI tools; clinical use needs an approved system.

## Hands-on Exercise
**Task:** Summarise a synthetic discharge note with an AI assistant, then audit the summary for errors, missing facts and invented details.
**Tools:** Claude or ChatGPT (free plan) [VERSION]; the course's synthetic discharge note; a table in any notes app or spreadsheet. Use only the synthetic note; never enter real patient information.
**Steps:**
1. Read the synthetic note and list its 8–10 most important facts (diagnosis, allergies, medicines, pending results, follow-up actions).
2. Ask the assistant to summarise the note in under 120 words for a family doctor, using only information in the note.
3. Create a table with the columns: fact from note, in summary (yes/no), correct/omitted/invented/distorted, possible harm.
4. Check every fact in your list, then read the summary again and mark any sentence that is not supported by the note.
5. Try one improved prompt, such as asking the assistant to list allergies, medicines and follow-up actions under separate headings, and audit again.
6. Write two sentences on whether the improved prompt removed the need for human review. (It should not.)
**What good looks like:** A complete audit table, at least one error type found or a clear statement that none were found after a full check, a comparison of the two prompts, and a conclusion that clinician review remains necessary.
**Time:** about 30 minutes

## Review Flags
- Clinical reviewer sign-off required.
- [VERSION] Data-use and retention terms of free AI assistant plans (whether conversations are stored or used for training, and available settings) must be checked for each tool before recording. The lesson tells learners never to enter identifiable patient data regardless.
- The synthetic pneumonia note and the audit results are hypothetical. A clinical reviewer should confirm that the example contains no clinical advice and that the "invented antibiotic" example is described correctly.
