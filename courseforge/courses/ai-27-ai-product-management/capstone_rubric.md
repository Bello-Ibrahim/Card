# Capstone Rubric: AI Feature PRD and Evaluation Plan

## Task
Write a complete PRD and evaluation plan for one AI product feature, using the AI PRD template from L13. You write the product sections and the FigJam flow in L13 (capstone step 1), the evaluation plan in L14 (capstone step 2), and review and finalise both in L15 (capstone step 3). Use a real or invented product. Do not include confidential company information or personal data, and do not paste such information into AI tools.

## Deliverables
- An AI PRD with all 12 template sections: problem and users; scope and capability; experience; data needs; model behaviour spec; build approach and cost; evaluation plan; failure modes; human oversight; risks and launch guardrails; rollout and monitoring; open questions.
- A FigJam (or similar) flow showing the happy path and four failure paths: wrong, unsure, should not answer and unavailable.
- An opportunity score (value, feasibility and error cost) showing why this feature was chosen.
- A cost estimate in Google Sheets using the method tokens × price per token, with prices marked as placeholders or checked on a named date.
- An evaluation plan with a test set design (at least 20 core cases), a rubric, a threshold table and a review schedule with owners.
- A short record of the critical review from L15: the questions raised and the decision taken for each.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Problem, opportunity and scope | O3 | Real user pain with evidence; opportunity scored on value, feasibility and error cost with reasons; narrow scope with one user, one task, human in the loop and fallback; clear reason why AI is needed instead of a rule. | Clear problem and scored opportunity; scope mostly narrow with a fallback. | Problem stated without evidence, or scoring or scope is vague. | No clear user problem or scope. | 15 |
| Data, build approach and cost | O4 | Data table with sources, owners, labels, coverage, consent and a cold-start plan; build-or-buy choice compared on cost, speed, quality, data terms and supplier dependence; correct cost formula with a higher-usage scenario and placeholder prices marked. | Data table and build choice present; cost estimate correct but with one scenario only. | Data needs listed without owners or privacy questions, or the cost method has errors. | Data and cost not addressed. | 20 |
| Experience and model behaviour spec | O6 | Flow with all four failure paths and user actions; behaviour spec with testable must, must-never, unsure and refusal rules and at least 3 examples; failure modes and human oversight clearly described. | Flow and behaviour spec mostly complete; a few rules are vague. | Only the happy path is designed, or rules cannot be tested. | No flow or behaviour spec. | 20 |
| Evaluation plan | O5 | Test set of at least 20 core cases covering common, edge, user group or language, and refusal cases; rubric with examples; metrics in all three layers; pass and fail thresholds for each group and zero tolerance for critical failures; LLM-as-judge used with human spot checks; review schedule with owners. | Test set and metrics in all three layers; thresholds set but not for each group. | Metrics listed without thresholds, or the test set covers only common cases. | No evaluation plan. | 25 |
| Guardrails, rollout and monitoring | O5 | Risk table covering the five risk types with an owner for every guardrail and legal questions for each launch country; three rollout stages with numeric gate metrics and stop criteria; monitoring for drift and a named kill-switch owner. | Risks, guardrails and rollout present; some owners or numbers missing. | General risk statements, or stop criteria are not numeric. | No guardrails or rollout plan. | 10 |
| Review, clarity and honest trade-offs | O6 | Checklist completed; each critical-review question has a visible decision; the PRD is clear and specific; the summary states limits, unknowns, the option not chosen and one decision requested. | Review done and most questions handled; clear summary. | Review done but decisions not recorded, or the summary hides limits. | No review or summary. | 10 |

Total: 100

## Submission Checklist
- My PRD has all 12 template sections.
- My problem is supported by evidence, and I explained why AI is needed instead of a rule.
- My opportunity score shows value, feasibility and error cost.
- My FigJam flow shows the happy path and all four failure paths.
- Every rule in my behaviour spec could become a test case.
- My cost estimate uses tokens × price per token, with prices marked as placeholders or checked on a named date.
- My test set has at least 20 core cases, including edge, user group or language, and refusal cases.
- My thresholds were set before seeing results and include each user group and critical failures.
- Every guardrail has a named owner, and I listed legal questions for my launch countries.
- My rollout plan has numeric stop criteria and a kill-switch owner.
- I recorded the critical-review questions and my decision for each.
- I did not include confidential company information or personal data.
