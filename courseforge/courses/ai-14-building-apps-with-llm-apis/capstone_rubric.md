# Capstone Rubric: AI-Powered Web App with a Cost Dashboard

## Task
Design, build and deploy a small web app that uses an LLM API (the Claude API in the main path) for one clear feature. The app must return validated structured outputs, stream any free-text output to the web page, and may use one tool with safe limits. It must log every API call and show usage and cost on a dashboard page. You build the core feature in L14 (step 1), add logging and the dashboard in L15 (step 2), and test, deploy and present the app in L16 (step 3). Use invented or public test data only; do not send personal or confidential data to the API.

## Deliverables
- A one-page spec: user and problem, input and output schema, prompt plan, optional tool, limits and success measure.
- A public link to the deployed app on a free hosting plan (for example, Streamlit Community Cloud or Vercel).
- A Git repository with the code, prompt files and eval set, and no API keys or secret files.
- An eval set of at least 20 cases plus at least 3 prompt-injection cases, with the saved results (pass rate and cost of a run).
- A dashboard page that shows cost per day, average cost per request, error rate and a budget alert.
- A README with architecture, output schema, any tool, model used, measured cost per request, eval results and known limits.
- A demo video of 3 minutes or less that shows a normal case, a hard or failure case, and the dashboard.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Structured outputs and streaming | O3 | A clear schema (Pydantic or Zod) is used with the structured-output feature or a tool schema; results are parsed into objects, checked against business rules, and stop reasons are handled; free text streams smoothly in the web page. | Schema-validated output and streaming work; business checks or stop-reason handling are incomplete. | Output is JSON but not validated against a schema, or streaming is missing. | Output is free text parsed with string matching, or the feature does not work. | 25 |
| Tool use with safe limits | O4 | If a tool is used: clear definition, correct tool loop, input validation, step limit, error results and confirmation for any data change. If no tool is used: the spec gives a sound reason, and all model output that the app acts on is validated in code. | Tool works with most guardrails, or a reasonable no-tool decision with basic validation. | Tool works but lacks limits or input checks, or no reason is given for leaving it out. | Tool loop is broken, or a tool can change data without checks. | 15 |
| Testing and security | O5 | Eval set of 20+ cases with automatic checks, results before and after at least one fix, no untreated regressions; injection cases tested with at least one fix; errors handled by type; no secrets in prompts or the repository. | Eval set of 20+ cases with results; injection cases tested; basic error handling. | Fewer than 20 cases or no saved results; injection testing is minimal. | No evaluation or security testing. | 20 |
| Cost logging and dashboard | O6 | Every call is logged, including failures and streamed calls; the dashboard shows cost per day, cost per request, error rate and a working budget alert; the README justifies at least one cost choice (model, caching, batching, limits or quotas) with numbers. | Logging and dashboard work with most measures; a cost choice is described without full numbers. | Logging misses failed or streamed calls, or the dashboard shows only totals. | No logging or dashboard. | 20 |
| Deployed app, README and demo | O7 | The public link works; the spend limit, max_tokens and request limits are in place; the README has all required sections, including measured cost per request and honest known limits; the demo is under 3 minutes and shows a failure case. | The app is deployed and the README and demo cover most requirements. | The app runs only locally, or the README or demo is missing key parts. | No working app, README or demo. | 20 |

Total: 100

## Submission Checklist
- My spec fits on one page and covers all six headings.
- My public link works, and I tested it with a normal, a hard and a failure case.
- My output is validated against a schema and parsed into objects, not read with string matching.
- Free-text output streams to the page, and I check stop reasons.
- Any tool has input checks, a step limit and confirmation before changing data (or my spec explains why I used no tool).
- My eval set has at least 20 cases plus injection cases, and I saved the pass rate and cost.
- Every API call is logged, including failures, and the dashboard shows cost per day, cost per request, error rate and a budget alert.
- A spend limit is set, and my API key is only in environment variables or the host's secrets settings.
- My README states the model, cost per request, eval results and known limits.
- My demo is 3 minutes or less, and no personal data or API key appears on screen.
