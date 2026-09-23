# Capstone Rubric: Automate a Business Process with an AI Agent

## Task
Design, build and test a multi-step AI agent in self-hosted n8n that uses the Claude API and Google Sheets to automate a real business process end to end, with human approval, error handling and a test set. You write the design and build the first version in L15 (capstone step 1), and you harden, test and present it in L16 (capstone step 2). Use invented or anonymised sample data only. If the process involves decisions about people, such as hiring or credit, the agent may only collect and summarise information; a person decides.

## Deliverables
- A one-page design: trigger, steps (rule or model), tools, approval points, failure modes and data.
- The exported n8n workflows (JSON), including the error workflow, with no API keys inside.
- The Google Sheet with the data, approval, log, errors and dead-letter tabs.
- A test sheet with at least 20 cases (including at least 3 prompt-injection cases), scored twice: before and after your main fix, with pass rate, average tokens and average time.
- A one-page runbook: what it does, how it fails, who approves, how to stop it, limits.
- A 3-minute screen-recorded demo with a verdict: ready, ready with limits, or not ready.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Working end-to-end build with validated output | O3, O7 | Runs end to end on all test inputs from trigger to final sheet; every model output is validated before use; rules are used where a rule is enough; the design page matches the build. | Runs end to end on most inputs; validation on the main model output; design mostly matches. | Runs only with manual fixes, or model output is used without validation. | Workflow does not run end to end. | 25 |
| Tool and agent design | O4 | Agent is used only where steps depend on the input; each tool has one job, a clear description with when not to use it, and strict inputs; write tools are limited; memory size is justified. | Sensible tools with clear descriptions; minor overlap or missing "when not to use" notes. | Vague tool descriptions, too many tools, or an agent used where a fixed workflow would do. | No tools, or tools that the agent cannot use correctly. | 15 |
| Reliability, error handling and human approval | O5 | Retries on API calls, error outputs to a dead-letter tab, an error workflow that logs and notifies, a run log, cost controls, and approval before every irreversible action and every decision about people; approved actions run exactly once. | Most of these are present and working; one minor gap. | Some error handling or approval, but important gaps, such as a send action without approval. | No error handling and no approval steps. | 25 |
| Testing, evaluation and verdict | O6 | 20+ realistic cases with normal, edge, out-of-scope and 3+ injection cases; two full scored runs; pass rate, cost and time reported; the highest-risk failure fixed; an honest verdict supported by evidence. | 20 cases with injections, scored at least once with a fix and a reasonable verdict. | Fewer than 20 cases, no injection cases, or a verdict without evidence. | No test set. | 20 |
| Runbook and demo | O7 | Runbook that a colleague could follow, covering all five parts; a clear 3-minute demo showing a normal run, an approval and a handled failure or injection. | Runbook and demo cover most parts clearly. | Runbook or demo is incomplete or hard to follow. | Runbook or demo missing. | 15 |

Total: 100

## Submission Checklist
- My design page covers trigger, steps, tools, approval points, failure modes and data.
- My workflow runs end to end, and every model output is validated before it is used.
- My exported workflows contain no API keys, and my API key is stored in an n8n credential.
- I set a spending limit for the Claude API and kept my test runs small.
- Every irreversible or external action, and every decision about people, waits for human approval.
- Retries, a dead-letter tab, an error workflow and a run log are in place and tested.
- My test set has at least 20 cases, including at least 3 prompt-injection cases, and I ran it twice.
- I used only invented or anonymised sample data.
- My runbook explains what the agent does, how it fails, who approves, how to stop it and its limits.
- My demo is about 3 minutes long and ends with an honest verdict.
