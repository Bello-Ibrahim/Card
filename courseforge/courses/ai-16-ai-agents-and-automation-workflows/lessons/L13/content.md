# L13 Error Handling, Retries and Logging

Course: AI-16 · Module: M4 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
Your workflow will fail. An API key will expire, a sheet column will be renamed, the API will be busy for a minute. The question is not *if* it fails, but whether you find out in five minutes or five weeks.

## Explanation
Reliable workflows plan for four kinds of failure:

- **Temporary errors:** timeouts, a busy API, a rate limit. Usually fixed by trying again.
- **Permanent errors:** a wrong API key, a deleted sheet, a missing field. Trying again will not help; a person must fix them.
- **Bad data:** one item with unexpected content, such as invalid JSON (L06).
- **Wrong results:** the workflow "succeeds" but the output is wrong. Testing (L14) and approval (L12) catch these.

n8n gives you four layers of protection [VERSION]:

1. **Retry On Fail** in a node's settings: a few tries with a wait between them. Use it on API calls for temporary errors. Do not retry an action that sends or pays, unless you are sure a failed try did not already succeed.
2. **On Error** setting per node: stop the workflow, or continue and pass the error on an error output. Use the error output to route one bad item to a **dead-letter** tab (a list of failed items with the error message) while the other items continue.
3. **Error workflow:** a separate workflow that starts with an **Error Trigger** node. In each main workflow's settings, you select it as the error workflow. When a run fails, it receives the workflow name, the failed node, the error message and a link to the execution. [VERSION]
4. **Run log:** one row per run in a "log" sheet: time, workflow, items processed, items failed, tokens used, status. This shows trends, such as rising cost or growing failures.

The error workflow should do two things: **record** the failure (append a row to an "errors" tab) and **notify** a person (an email or chat message). Keep error messages free of personal data and never include API keys.

**Analogy:** Error handling is like a pilot's checklist for emergencies. It is written calmly before the flight, not invented during a problem. When an engine warning appears, the crew follows the list step by step. Your retries, error paths and error workflow are that list, prepared before the failure happens.

## Worked Example
Petra Dvořák automates reports at a hypothetical accounting firm in Prague, Czechia. Her classification workflow runs every night. On screen, she:

1. Creates a new workflow "Error handler" with an **Error Trigger** node. [VERSION]
2. Adds Google Sheets (append to "errors"): `time` = the current time, `workflow` = the workflow name, `node` = the last node that ran, `message` = the error message and `execution_url`. She maps these from the Error Trigger output. [VERSION]
3. Adds an email node that sends her a short message: "Workflow X failed at node Y: message. Link: …". [VERSION]
4. Opens the main workflow's settings and selects "Error handler" as its error workflow. [VERSION]
5. On the Claude HTTP Request node, turns on Retry On Fail with 3 tries and a wait between them, and sets On Error to "continue (using error output)". The error output goes to a "dead_letter" tab with the item ID and error message. [VERSION]
6. At the end of the main workflow, adds a Google Sheets append to "log" with counts and total tokens.
7. Tests by changing the API key in the credential to a wrong value and running the workflow manually.

Petra notices that the error workflow did not start on her manual test. She checks the documentation: in her release, error workflows run for production (triggered) executions, so she tests with the active schedule instead. [VERSION] Then the "errors" row appears and the email arrives. She restores the correct key.

## Common Mistake
Learners often turn on "continue on error" everywhere so the workflow always shows green. Failures then disappear silently: items are skipped, nothing is logged, and nobody knows. Continuing is only safe when the failed item goes somewhere visible, such as a dead-letter tab that a person checks. A green run with lost data is worse than a red run that sends an alert.

## Key Takeaways
1. Use retries for temporary errors, error outputs and a dead-letter tab for bad items, and an error workflow for failures that stop a run.
2. The error workflow should record the failure and notify a person, without personal data or secrets in the message.
3. Keep a run log with one row per run, so you can see failures, volumes and token use over time.

## Hands-on Exercise
**Task:** Break your workflow on purpose with a wrong API key, confirm that the error workflow logs the failure to a sheet and sends you a notification, then fix the key.
**Tools:** n8n self-hosted; Google Sheets; an email account for test messages to yourself.
**Steps:**
1. Build an "Error handler" workflow: Error Trigger, Google Sheets (append to "errors"), email to yourself. [VERSION]
2. Select it as the error workflow in your main workflow's settings.
3. Turn on Retry On Fail on the Claude node and route its error output to a "dead_letter" tab.
4. Add a "log" row at the end of the main workflow.
5. Put a wrong API key in a copy of the credential and run the workflow the way it runs in production (for example, a schedule), as your release requires. [VERSION]
6. Check the "errors" tab, the email and the execution list. Then restore the correct key and run again.
**What good looks like:** One clear error row with workflow, node, message and link; one notification email with no secrets in it; a successful run afterwards with a new "log" row.
**Time:** about 40 minutes

## Review Flags
- [VERSION] n8n Error Trigger node, error workflow setting, Retry On Fail, On Error options (error output), Error Trigger output fields, email node names, and whether error workflows run for manual executions must be checked against the current release.
