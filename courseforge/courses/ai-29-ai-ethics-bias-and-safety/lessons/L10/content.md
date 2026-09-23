# L10 Writing Your Audit and Recommendations

Course: AI-29 · Module: M2 · Objectives: O6, O7 · Video: 5 min

## Hook
You have tested a tool and rated its risks. Now imagine your manager has five minutes to read your work. What must they understand, and what should they do next?

## Explanation
An **audit report** turns your tests and ratings into decisions. A good report is short and clear. It answers four questions:
1. **What did you test?** The tool, the version or plan, the date, and the tasks you looked at.
2. **What did you find?** Your main results, with evidence from your tests.
3. **How serious is it?** Your risk ratings and the reasons.
4. **What should change?** Your recommendations.

Use this **audit template** for your capstone. Keep the whole report to 1–2 pages.

1. **Scope:** the tool, plan and version (if shown), the date, the uses you considered (for example, "drafting job references"), and what you did not test.
2. **Test design:** how you tested: paired prompts, how many pairs, which details you changed, how many runs, and the checks you did for facts, privacy and safety.
3. **Paired prompts:** a short table of your key pairs: detail changed, a summary of the differences, and how many runs showed the pattern. Put the full table in an appendix.
4. **Findings:** 3–5 clear statements, each with evidence. Include what worked well, not only problems.
5. **Severity:** each finding's likelihood, impact and priority from your L09 matrix.
6. **Limitations:** what your test could not show. For example: few runs, one tool version, invented cases only, and no access to the tool's data or design.
7. **Recommendations:** at least 3, linked to your top risks.

Good recommendations have three qualities:
- **Specific:** they say exactly what should happen.
- **Realistic:** the team can actually do it.
- **Assigned:** a person or team owns it, if possible with a time.

Compare these:
- Weak: "Make the tool fairer."
- Strong: "The HR team reviews every AI-drafted reference before sending, and checks for differences in describing words, from next month."

Write carefully. Describe results as limited tests: "In 4 of 5 runs…", not "the tool is biased". This is honest, and it makes your report harder to dismiss.

**Analogy:** An audit report is like a car inspection report. The mechanic does not write a novel. They list what they checked, what is wrong, how urgent each problem is and what to repair first. They also say what they could not check, such as parts they could not reach. The owner can then make a clear decision.

## Worked Example
Rania Haddad works in student services at a hypothetical university in Jordan. Her team plans to use a free chatbot to draft replies to student questions. She writes a short audit.

- **Scope:** a free chatbot, tested on one date, for drafting replies to questions about fees, deadlines and student support. Not tested: questions in languages other than Arabic and English.
- **Test design:** 6 paired prompts changing one detail each (name, nationality, age, disability), 3 runs each; 5 fact checks against the university's website; privacy review of the prompts staff would need.
- **Paired prompts (summary):** in the "late fee" pair, the reply to an international student mentioned visa rules in 3 of 3 runs, although the question did not mention visas. Other pairs showed no clear pattern.
- **Findings:** (1) the chatbot gave a wrong deadline in 2 of 5 fact checks; (2) replies to international students added unrequested visa warnings; (3) staff would need to share student ID numbers for some tasks; (4) tone was polite and clear in all tests.
- **Severity:** wrong deadlines, high likelihood and high impact (students could miss a deadline): highest priority. Student ID sharing, medium likelihood, high impact: high priority. Visa warnings, high likelihood, medium impact: high priority.
- **Limitations:** a small number of runs, one tool version, invented cases only.
- **Recommendations:**
  1. Staff check every date and fee against the university website before sending. Owner: student services team lead, from next week.
  2. Staff never enter student ID numbers or names; they use placeholders. Owner: Rania, who adds this to staff guidance this month.
  3. Repeat the paired-prompt tests each term, including the visa pattern. Owner: quality officer.

## Common Mistake
Many learners write long reports full of every result, or make strong claims such as "the tool is discriminatory" from a few tests. Both reduce trust. The correction: keep the report short, lead with your most serious findings, show your evidence, state your limitations honestly, and make every recommendation specific, realistic and assigned. Also remember that this is a practical audit, not a legal review: legal questions belong to course AI-30 and to your organisation's legal team.

## Key Takeaways
1. A good audit report is short and says what you tested, what you found, how serious it is and what should change.
2. Use the template: scope, test design, paired prompts, findings, severity, limitations and recommendations.
3. Recommendations should be specific, realistic and assigned to someone, and findings should be described as limited tests.

## Hands-on Exercise
**Task:** Capstone step 3: write a 1–2 page audit report on your chosen tool with your test results, your risk ratings and at least 3 recommendations.
**Tools:** Your L08 test table and L09 risk matrix; any document editor (free options such as Google Docs or LibreOffice Writer). Optional: Claude or ChatGPT to improve clarity, without pasting personal or confidential data.
**Steps:**
1. Copy the seven template headings into a new document.
2. Fill in Scope and Test design from your L08 notes.
3. Add a short paired-prompt summary table, and put your full L08 table in an appendix.
4. Write 3–5 findings, each with evidence, including at least one thing the tool did well.
5. Add Severity from your L09 matrix.
6. Write at least 3 honest Limitations.
7. Write at least 3 Recommendations that are specific, realistic and assigned.
8. Read your report as if you were a busy manager. Remove anything that does not help a decision. Check it against the capstone rubric.
**What good looks like:** A clear 1–2 page report that follows the template, links every finding to evidence, uses careful "limited test" language, and gives at least 3 specific, realistic, assigned recommendations for your top risks.
**Time:** about 45 minutes

## Review Flags
- None. The university case is hypothetical on purpose, and no real incidents or statistics are used. The report template follows the capstone brief in the curriculum.
