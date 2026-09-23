# L12 Choosing a Tool and Assessing Clinical Value

Course: AI-25 · Module: M3 · Objectives: O5, O6 · Video: 5 min

## Hook
"Our tool uses advanced AI" is not a reason to use it in a clinic. The first question for any tool is simpler and harder: what will be better for which patients, compared with what we do today?

## Explanation
Your capstone is a written **evaluation of an AI health tool**. You build it in three steps across L12, L13 and L14.

**Choosing a tool.** You have two options:
- A **hypothetical tool** that you describe yourself, for example a missed-appointment model for a clinic network, or a tool that flags retinal photographs for specialist review.
- A **real tool described only from its public documentation**, such as its website, published instructions for use or public regulatory summaries. Do not make claims that go beyond what the documentation says. Mark any figure you quote with its source, and treat unverified claims as unverified.

Use only public or synthetic information. Never include identifiable patient data.

**Evaluation template.** Use these sections in your final document:

1. **Tool description and intended use** (L12)
2. **Clinical value**: problem, outcome, patients, comparison with current practice (L12)
3. **Evidence**: level of evidence and performance claims (L04, L05)
4. **Data and privacy**: data used, quality, protection (L02, L11)
5. **Bias and equity**: patient groups and settings at risk (L09)
6. **Risks and failure modes**, with mitigations and owners (L10, L13)
7. **Workflow and accountability**: who sees the output, who decides (L01, L13)
8. **Regulatory position**: questions to check locally (L11)
9. **Safe implementation plan** (L14)
10. **Recommendation**: adopt, pilot, or do not adopt, with reasons (L14)

**Intended use statement.** One or two sentences that say: what the tool does, for which patients, in which setting, for which user, and what decision it supports. For example: "The tool flags 12-lead ECGs from adult outpatients that may show atrial fibrillation, for review by a cardiologist, who makes the diagnosis."

**Clinical value.** Answer four questions:
- **Problem:** What current problem does the tool address? Be specific: delays, missed cases, workload, access.
- **Outcome:** Which outcome should improve, and how will you measure it? Prefer outcomes that matter to patients, such as time to treatment, rather than only accuracy.
- **For whom:** Which patients benefit, and are any groups likely to benefit less or be harmed?
- **Compared with what:** What is current practice, and what evidence suggests the tool is better, not just different?

Also ask what the tool could cost in other ways: staff time to review outputs, extra tests after false positives, and effort to maintain it.

**Analogy:** Assessing clinical value is like deciding whether to add a new test to a care pathway. A test that is accurate but changes no decisions adds cost and delay. A test is worth adding only if its result leads to better care for someone.

## Worked Example
Farah Haddad is a health-tech product analyst in Jordan. For her capstone she chooses a hypothetical tool: a model that flags adults with diabetes who are overdue for eye screening and at higher risk of missing it, so that primary care nurses can contact them.

**Intended use:** "The tool identifies adults with diabetes in a primary care network who are overdue for retinal screening and ranks them by predicted likelihood of not attending, for primary care nurses to contact and support. It does not diagnose eye disease."

**Clinical value:**
- **Problem:** Many patients in her hypothetical network are overdue for screening, and nurses have limited time to contact everyone.
- **Outcome:** The share of patients screened within the recommended interval, measured for all patients and by age, sex and district.
- **For whom:** Adults with diabetes who are overdue. She notes a risk that patients without a mobile phone may be contacted less.
- **Compared with what:** Current practice is a monthly list sorted by date. She notes that there is no evidence yet that ranking by predicted risk improves screening rates over contacting everyone overdue, so this must be tested.

Her conclusion for this section: potential value is clear, but not yet shown.

## Common Mistake
Many learners describe what the tool does ("it detects X with 90% sensitivity") and call that clinical value. Performance is not value. Value is a change in care or outcomes for patients, compared with current practice. A tool with high sensitivity that finds cases already found by current practice adds little value.

## Key Takeaways
1. The capstone evaluates a hypothetical tool, or a real tool described only from its public documentation, using public or synthetic information.
2. An intended use statement names what the tool does, for whom, where, for which user and which decision it supports.
3. Clinical value means a better outcome for defined patients compared with current practice, not only good performance figures.

## Hands-on Exercise
**Task:** Capstone step 1: write the intended use statement and the clinical value section of your evaluation.
**Tools:** Any word processor (Google Docs, LibreOffice Writer or Word); the evaluation template above; the capstone rubric. Optional: Claude or ChatGPT (free plan) for feedback on clarity; do not paste confidential or patient information.
**Steps:**
1. Choose your tool: hypothetical, or real and described only from public documentation. Save the documentation links if you use a real tool.
2. Create a document with the 10 section headings from the template.
3. Write the tool description and an intended use statement of no more than two sentences.
4. Write the clinical value section with the four headings: problem, outcome, for whom, compared with what.
5. Add one sentence on possible hidden costs, such as staff review time.
6. Check your work against the capstone rubric and mark any claim that needs a source.
**What good looks like:** A specific, testable intended use statement that names the user and decision; a clinical value section that names a measurable patient-relevant outcome, the groups who may benefit less, and an honest comparison with current practice.
**Time:** about 40 minutes

## Review Flags
- None. The worked example is hypothetical, and the lesson tells learners to source any claim about a real tool from its public documentation.
