# L13 Scoping Your AI Use Case Proposal

Course: AI-24 · Module: M3 · Objectives: O3, O6 · Video: 5 min

## Hook
"We should use AI for lending." That is not a proposal. It is a wish. A committee can only say yes to something specific: a clear problem, a clear user, clear data and a clear way to measure success. This lesson turns your idea into that.

## Explanation
Your capstone is an **AI use case proposal** for a financial institution, with a **risk and compliance assessment**. You build it in two steps: the scope in this lesson and the risk assessment in L14. Choose a use case you know, from your own work or a realistic hypothetical institution. Use only synthetic or described data, never real customer data.

The proposal template has seven sections.

| Section | Questions to answer |
|---|---|
| 1. Problem | What is going wrong today? For whom? How do you know? |
| 2. Business value | What improves: cost, speed, losses, customer outcomes? What is the rough size? |
| 3. Users | Who uses the output, and what decision do they make with it? |
| 4. Data | Which data, from where, how much history, what quality problems, what legal basis? |
| 5. Model approach | Rules, scorecard, machine learning model or language model assistant? Why that one? |
| 6. Human oversight | Where does a person review, override or stop the output? |
| 7. Success measures | Which 3–5 numbers show it works, including at least one customer or fairness measure? |

Keep the scope narrow. "Support loan officers in reviewing first-time business loans under a set amount" is better than "AI for all lending". A narrow scope makes data, risks and success easier to define.

**Using an AI assistant as a thinking partner.** A free AI assistant can help you test your ideas. Useful prompts include:
- "Here is my problem statement. What assumptions am I making?"
- "What data problems might a lender face with this use case?"
- "Suggest three success measures, and say how each could be misleading."

Use the answers to find gaps, then write the proposal in your own words. Do not copy AI text into your proposal, do not accept its facts about laws or markets without a source, and do not paste confidential information into the tool.

**Analogy:** Scoping a proposal is like an architect's first drawing. Before anyone orders bricks, the drawing shows who will live in the house, how many rooms it needs and where the doors go. Changing a drawing is cheap. Changing a finished building is expensive.

## Worked Example
Joy Villanueva is operations manager at Bayanihan Microfinance, a hypothetical microfinance institution in the Philippines. Its loan officers visit small businesses and write long visit notes. Reviewing applications takes too long.

Her first idea is "an AI that approves loans". After testing her assumptions with an AI assistant, she narrows it down.

1. **Problem:** Loan officers spend a large part of each day summarising visit notes and checking documents, and applicants wait too long for decisions.
2. **Business value:** Faster decisions for applicants and more visits per officer. She will measure the current baseline in a four-week study before claiming any saving.
3. **Users:** Loan officers and branch credit supervisors. The supervisor still makes every lending decision.
4. **Data:** Visit notes, application forms and repayment history of existing clients. Known problems: notes in English, Filipino and local languages; handwritten forms. Consent wording must be reviewed by compliance.
5. **Model approach:** A language model assistant that summarises visit notes into a standard format and lists missing documents. No credit score and no approval decisions.
6. **Human oversight:** The officer checks every summary against the notes and signs it. The supervisor decides.
7. **Success measures:** Time from visit to decision; share of summaries with errors found by officers; officer satisfaction; approval and error rates by client group, to check that summaries do not disadvantage clients who write in local languages.

The assistant helped Joy notice one assumption she had missed: that all notes are written in one language. She did not copy its wording; she used its questions.

## Common Mistake
Many learners describe the technology first ("We will use a large language model") and the problem last. Committees fund solutions to problems, not technologies. Start with the problem and the user, and let the model approach follow. Also, avoid claiming exact savings without a baseline; state how you will measure them.

## Key Takeaways
1. A strong proposal answers seven questions: problem, value, users, data, model approach, human oversight and success measures.
2. A narrow, specific scope makes data, risks and success easier to define and approve.
3. Use an AI assistant to test your assumptions, but write the proposal in your own words and check every fact.

## Hands-on Exercise
**Task:** Capstone step 1: complete the problem, value, data and success-measure sections of the proposal template, using an AI assistant to test your assumptions.
**Tools:** Google Docs or Google Sheets (free); the course's proposal template; Claude or ChatGPT (free plan) [VERSION].
**Steps:**
1. Choose one use case and write a one-sentence scope.
2. Fill in sections 1 (Problem), 2 (Business value), 4 (Data) and 7 (Success measures). Draft sections 3, 5 and 6 briefly.
3. Paste your draft, with no confidential or customer data, into the AI assistant and ask: "What assumptions am I making, and what could go wrong?"
4. Note at least 3 useful challenges from the answer.
5. Revise your sections in your own words to address them.
6. Keep a short log of what the AI suggested and what you changed, for your submission.
**What good looks like:** A narrow scope, a problem stated with evidence or a plan to measure it, specific data sources with known quality issues, 3–5 success measures including one fairness or customer measure, and a log showing how you used the AI.
**Time:** about 45 minutes

## Review Flags
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
