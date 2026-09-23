# L05 Classifying an AI System Step by Step

Course: AI-30 · Module: M1 · Objectives: O4 · Video: 5 min

## Hook
A regulator asks you: "Why did you decide this system is not high-risk?" If your answer is "it seemed fine", you have a problem. A classification is only as strong as the reasoning you can show later.

## Explanation
This lesson is educational and is not legal advice. It gives a repeatable method, but every step must be checked against the official text of the EU AI Act.

The method has five steps. Work through them in order and write down your answer and your reason at each step.

**Step 1: Describe the system and its purpose.** What does it do, who uses it, who is affected, and what decisions does its output support? Use the provider's stated intended purpose and your actual use. If they differ, record both.

**Step 2: Is it an AI system under the Act?** The Act has its own definition, based on features such as operating with some autonomy and inferring from inputs how to produce outputs like predictions, content, recommendations or decisions [VERIFY] [REGION]. Simple rule-based software may fall outside it. The definition is in [the definitions article], and official guidance on it should be read too [VERIFY] [REGION].

**Step 3: Check the prohibited list.** Compare the purpose against each prohibited practice in [the article on prohibited practices] [VERIFY] [REGION]. If there is a possible match, stop and escalate to legal counsel.

**Step 4: Check the high-risk categories.** Is the system a safety component of a regulated product? Is it used in one of the listed areas, such as employment or education [VERIFY] [REGION]? Note that the Act allows some systems in listed areas not to be treated as high-risk, for example where they only perform a narrow procedural task, under conditions that must be documented [VERIFY] [REGION]. Record why any such exception applies.

**Step 5: Check the transparency duties.** Does the system interact directly with people, create or change content, or recognise emotions or biometric categories [VERIFY] [REGION]? These duties can apply in addition to high-risk duties.

Finish with a **classification note**: the tier, the reasoning at each step, the sources you used with their dates, your confidence, the name of the reviewer and a date to review the decision again.

**Analogy:** The method is like a doctor's diagnosis checklist. The doctor does not jump to a conclusion from one symptom; she goes through the same questions every time and writes down what she found. If another doctor reads the notes later, they can see exactly how she reached her decision.

## Worked Example
Katrin Hoffmann is legal counsel at a hypothetical recruitment agency in Hamburg, Germany. The agency plans to use a CV-screening tool bought from a vendor.

1. **Describe:** the tool reads CVs, scores each one against a job description and produces a shortlist. Recruiters normally interview only the top 20 candidates. Candidates are affected directly.
2. **AI system?** The vendor's documentation says the tool uses a trained language model to infer match scores. Likely yes [VERIFY] [REGION].
3. **Prohibited?** It does not use emotion recognition or manipulative techniques. No match found.
4. **High-risk?** Recruitment and selection of candidates is a listed employment use. The tool shapes who gets an interview, so the narrow-task exception does not seem to fit. Likely **high-risk** [VERIFY] [REGION]. The agency is a **deployer**.
5. **Transparency?** Candidates do not chat with the tool, but they must be informed about its use under other rules too, such as data protection law.

Katrin's note records "high-risk, deployer, confidence: high", lists the sources and sets a review date for six months later or earlier if the vendor changes the tool.

## Common Mistake
Many teams classify once and never look again. A classification depends on purpose and use. If the agency starts using the same tool to rank existing staff for promotion, or the vendor adds a video-interview feature that analyses facial expressions, the answer may change. Record triggers for review in the note itself.

## Key Takeaways
1. Use five steps in order: describe the system, check the AI system definition, check prohibited practices, check high-risk categories, check transparency duties.
2. Write a classification note with the reasoning, sources, confidence, reviewer and review date, because the decision must be explainable later.
3. Classification is not permanent: a new purpose or feature can change the tier; this method is educational, not legal advice.

## Hands-on Exercise
**Task:** Use the 5-step method on a hypothetical customer-service chatbot and on a hypothetical exam-proctoring tool, and write a short classification note for each.
**Tools:** The 5-step method above; the official text of the EU AI Act or official Commission guidance [VERIFY]; a word processor.
**Steps:**
1. Chatbot: a telecoms company in Belgium uses it to answer billing questions; it can hand the customer to a human.
2. Proctoring tool: a university in Italy uses webcams to flag possible cheating during online exams; staff review the flags.
3. For each system, answer all five steps in one or two sentences each.
4. Write a classification note: tier, role, confidence, sources with dates and review triggers.
5. Use only the facts given. Do not paste real student or customer data into any tool.
**What good looks like:** Two notes of about half a page each, with clear reasoning at every step, a likely transparency duty for the chatbot, a careful high-risk analysis for the proctoring tool, and at least one review trigger each.
**Time:** about 30 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [REGION] The AI system definition, prohibited practices, high-risk categories and annexes, the narrow-task exception and its conditions, and transparency duties must be checked against the official text (curriculum flag).
- [VERIFY] [REGION] The worked example conclusions (AI system, high-risk, deployer) must be confirmed by the legal reviewer.
- [VERIFY] Official source and guidance for the exercise must be chosen, with date recorded.
