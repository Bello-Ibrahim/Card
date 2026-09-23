# L14 Writing the Evaluation Plan

Course: AI-27 · Module: M3 · Objectives: O5, O6 · Video: 5 min

## Hook
"We will evaluate it carefully" is not a plan. A plan says what you measure, on which data, against which number, at which moment, and who decides what happens next.

## Explanation
Your evaluation plan turns the metric tree (L08) and test set (L09) into a schedule of decisions. It has five parts.

**1. Test set design.** Size, case types and their shares (common, edge, user groups and languages, should refuse), who writes the expected behaviour, and how the set is updated. Add new cases from real failures after launch, but keep a fixed core set so results stay comparable over time.

**2. Rubric and rating method.** The scoring scale with a definition and an example for each score. Who rates (humans as the reference), where LLM-as-judge is used, and the human spot-check rule, such as "humans rate at least 20% of judge-scored cases and every case in a weak language".

**3. Metrics and thresholds.** For each metric, a **pass threshold** (good enough to continue) and, for critical metrics, a **fail threshold** (stop or roll back). Set them before you see results. Critical failures, such as invented refunds or exposed personal data, usually have a threshold of zero in the test set.

**4. Three evaluation moments.**
- **Before launch:** offline evaluation on the test set, which must pass before any user sees the feature.
- **During the pilot:** online metrics against a baseline, weekly human review of real outputs, and guardrail metrics.
- **After launch:** a monitoring dashboard, a regular sample review, and a test-set rerun after every model, prompt or data change.

**5. Review schedule and owners.** Who looks at which results, how often, and who has authority to decide continue, fix or stop.

**Analogy:** An evaluation plan is like the inspection schedule for a new bridge. Engineers test the design before building, test the structure before opening, and inspect it on a fixed schedule after opening, with clear limits that close the bridge. Nobody decides the limits after seeing the cracks.

## Worked Example
Dewi Lestari is a PM at a hypothetical telecom company in Indonesia. Her feature drafts replies for support agents answering customer messages about data packages, billing and network problems. Agents edit and send each draft.

**Test set:** 150 invented cases: 70 common, 30 edge (such as a customer with two SIM cards), 30 split between formal Indonesian, informal Indonesian and English, and 20 that should refuse or redirect (such as a request to change another person's account). Two senior agents write the expected behaviour for each case. After launch, new failure cases are added every month; the core 150 stay fixed.

**Rubric:** 2 = correct, complete and follows policy; 1 = correct but needs editing; 0 = wrong, invents an offer or refund, or answers when it should redirect. LLM-as-judge scores the full set after each change. Senior agents rate a random 30 of those cases plus every informal-language and refusal case.

**Thresholds:**

| Metric | Moment | Pass | Fail (stop) |
|---|---|---|---|
| Pass rate (score 2), whole set | Before launch | At least 80% | Below 70% |
| Pass rate, each language group | Before launch | At least 75% | Below 65% |
| Invented offers or refunds | Before launch and weekly | 0 in test set | Any in test set |
| Correct redirects on refusal cases | Before launch | All 20 | Any refusal case answered |
| Drafts sent with light or no editing | Pilot | Higher than 50% by week 4 | — |
| Average handling time | Pilot | Lower than baseline | Higher than baseline for 2 weeks |
| Complaint re-open rate | Pilot and after launch | Not above baseline | Above baseline for 2 weeks |

**Review schedule:** the ML engineer shares test-set results after every change; the support quality lead reviews 50 real drafts each week; Dewi and the support operations lead meet every two weeks to decide continue, fix or stop. The operations lead owns the kill switch.

## Common Mistake
Many learners write thresholds only for the overall pass rate. A feature can pass overall while failing a whole language group or answering requests it should refuse. Add thresholds for each case type and user group, and set zero-tolerance thresholds for critical failures.

## Key Takeaways
1. An evaluation plan covers test set design, rubric and rating method, metrics with thresholds, three evaluation moments and a review schedule with owners.
2. Set pass and fail thresholds before seeing results, including thresholds for each user group and zero tolerance for critical failures.
3. Evaluation continues after launch: sample reviews, monitoring and test-set reruns after every change.

## Hands-on Exercise
**Task:** Capstone step 2: write the evaluation plan, including the test set design, metrics, thresholds and review schedule.
**Tools:** Google Docs or any document; Google Sheets for the threshold table [VERSION]; optional: Claude (free plan) [VERSION].
**Steps:**
1. Describe your test set: size, case types and their shares, who writes expected behaviour, and how it is updated. Use your 20 cases from L09 as the starting core.
2. Write your rubric with an example for each score, and your LLM-as-judge and human spot-check rules.
3. Build a threshold table with at least 6 metrics covering offline, online and guardrail layers, each with a moment, a pass threshold and, where critical, a fail threshold.
4. Add the review schedule: who, how often, and who decides.
5. Optional: ask Claude which threshold in your table is easiest to misread. Do not paste confidential data.
6. Add the plan to section 7 of your PRD.
**What good looks like:** A plan another PM could run without asking you questions, with thresholds for each group, zero-tolerance rules for critical failures, and named owners.
**Time:** about 45 minutes

## Review Flags
- [VERSION] Google Sheets features and Claude free-plan limits and data-use terms must be checked before recording.
