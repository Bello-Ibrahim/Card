# L12 Writing the Comparison Report

Course: AI-02 · Module: M3 · Objectives: O5, O6, O7 · Video: 5 min

## Hook
You have three outputs, three sets of scores and a page of notes. Your manager does not want to read all of that. They want to know one thing: which tool should we use for this task, and why? Your report must answer that question clearly and honestly.

## Explanation
A good comparison report is short and follows a clear structure. Use these six parts.

**1. The task.** One paragraph: what the task is, who needs the output and why it matters. For example: "Each month our team turns meeting transcripts into summaries for managers."

**2. The method.** How you tested: the three tools, their versions and the test dates, the exact prompt, the input (and how you removed personal data), any settings you changed, and your rubric with weights. A reader should be able to repeat your test.

**3. The results table.** One row per tool, one column per criterion, plus a weighted total. Keep it simple and easy to read.

**4. Strengths and failures.** For each tool, describe what it did well and where it failed. This is where you use what you learned in this course. Do not only describe a failure: **explain the likely cause** using how the model works.

- An invented fact or source in text output → the language model predicts likely text, not checked facts (L02, L04).
- An out-of-date statement → the knowledge cut-off (L04).
- Wrong letters or wrong counts in an image → image models build from visual patterns and do not spell or count reliably (L05, L08).
- A misread number from a photo → multimodal models can misread small or unclear details (L07).
- Very different answers each time → sampling variety, such as temperature (L02), or random starting noise (L05).

**5. Recommendation.** Name the tool you recommend **for this task** and justify it with your criteria: quality, cost, privacy and risk. Say what checks a person must still do. It is acceptable to recommend "none of these" if all three failed on accuracy.

**6. Limits of the test.** Be honest. You tested one task, one prompt and one day. Tools change, and a different prompt might change the results. This section makes your report more trustworthy, not less.

**Length:** 2–3 pages, including the table. Use short paragraphs and headings.

**Analogy:** A comparison report is like a doctor's summary after tests. It says what was tested and how, shows the key results, explains what they mean, gives a clear recommendation and mentions what the tests could not show. The patient does not need every measurement, but they need to trust the method.

## Worked Example
Amara is a coordinator at a hypothetical non-profit organisation in Kigali, Rwanda. She tested three free chatbots on turning volunteer meeting notes into a short action list. Her results section includes this table:

| Tool | Accuracy (x2) | Clarity | Structure | Effort to fix | Weighted total (max 25) |
|---|---|---|---|---|---|
| Tool A | 5 | 4 | 5 | 4 | 23 |
| Tool B | 3 | 5 | 5 | 3 | 19 |
| Tool C | 4 | 3 | 3 | 3 | 17 |

In "Strengths and failures", she writes: "Tool B had the clearest wording but gave a volunteer a deadline that was not in the notes. This is a typical language model hallucination: the model filled a gap with a likely detail." Her recommendation: "Use Tool A for this task. It was the most accurate and needed the least editing. A coordinator must still check every name and date against the notes, and we will remove personal phone numbers before pasting." Her limits section says she tested one set of notes on one day, with each tool's version recorded in the method. [VERSION]

## Common Mistake
Many learners write the recommendation as "Tool A is the best AI." This is too broad. Your test shows only which tool worked best for one task, with one prompt, on one date. The correction is to limit the claim: "For this task, under these conditions, Tool A is the best choice." Then explain the checks a person must still do.

## Key Takeaways
1. A strong report has six parts: task, method, results table, strengths and failures, recommendation, and limits.
2. Explain each failure with its likely cause, using how that type of model works.
3. Make a specific recommendation for this task, justified by quality, cost, privacy and risk, and state the limits of your test.

## Hands-on Exercise
**Task:** Capstone step 3: write a 2–3 page comparison report with a results table and a justified recommendation for which tool to use for this task.
**Tools:** Any word processor or document tool; your capstone document, outputs and log from L10 and L11; the capstone rubric on the course page. Optional: a free chatbot to check your spelling, not to write the report for you.
**Steps:**
1. Read the capstone rubric so you know how the report will be assessed.
2. Write the task and method sections, including tool versions, test dates and your rubric.
3. Build the results table with weighted totals.
4. For each tool, write strengths and failures, and link each failure to a likely cause from the course.
5. Write your recommendation, using quality, cost, privacy and risk, and name the human checks still needed.
6. Write the limits section.
7. Attach your prompt, input (with personal data removed) and outputs as an appendix.
**What good looks like:** A 2–3 page report with all six parts, a clear table, at least one failure per tool explained by how the model works, a recommendation limited to this task, and an honest limits section.
**Time:** about 60 minutes

## Review Flags
- [VERSION] The worked example uses anonymous "Tool A, B, C" on purpose; learners must record real tool names, versions and dates in their own reports.
