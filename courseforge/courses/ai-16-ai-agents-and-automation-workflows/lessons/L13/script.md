# L13 Error Handling, Retries and Logging | Presenter Script

Course: AI-16 · Video: 5 min · Words: 688

## Hook
Your workflow will fail. An API key will expire. A sheet column will be renamed. The API will be busy for a minute. The question is not if it fails, but whether you find out in five minutes, or five weeks.

## Explain
Last time, we added human approval. In this final module, we make the whole system reliable. Plan for four kinds of failure. Temporary errors, like a busy API, are usually fixed by trying again. Permanent errors, like a wrong key, need a person. Bad data is one item with unexpected content. And wrong results are runs that succeed, but give the wrong output.

n8n gives you four layers of protection. First, retry on fail, for temporary errors on API calls. But do not retry an action that sends or pays, unless you are sure the failed try did not already succeed.

Second, the on error setting. A node can continue and pass a failed item to an error output. That output goes to a dead letter tab, a list of failed items with the error message, while the other items continue. One bad item should not stop the whole batch.

Third, an error workflow. It is a separate workflow that starts with an error trigger, and you select it in each main workflow's settings. When a run fails, it receives the workflow name, the failed node, the message, and a link. It should record the failure in a sheet, and notify a person. Never include personal data or API keys.

Fourth, a run log. Add one row per run to a log sheet, with the time, the items processed, the failures, the tokens used and the status. Over time, this shows trends, such as rising cost or growing failures, before they become a problem.

Think of a pilot's emergency checklist. When a warning light appears, the crew follows it step by step. It is written calmly before the flight, not invented during a problem. Your retries, error paths and error workflow are that checklist.

## Demonstrate
Let's build it. Petra Dvořák automates reports at an accounting firm in Prague, Czechia. Her classification workflow runs every night. First, she creates a new workflow called Error handler, with an error trigger. It adds a row to an errors tab, with the time, workflow, node, message and link.

Then it sends her a short email: which workflow failed, at which node, the message, and the link. In the main workflow's settings, she selects Error handler as its error workflow.

On the Claude request node, she turns on retry on fail, with three tries and a wait. She sets on error to continue, using the error output, which goes to a dead letter tab. At the end, she adds a log row with counts and total tokens.

Now she breaks it on purpose, with a wrong API key, and runs it by hand. The error workflow does not start. She checks the documentation. In her release, error workflows run only for triggered runs. So she tests with the active schedule. The error row appears, and the email arrives: one clear row, one short email, and no secrets in it. Then she restores the correct key.

A common mistake is to turn on continue on error everywhere, so every run looks green. Then failures disappear silently. Continuing is only safe when the failed item goes somewhere a person checks. A green run with lost data is worse than a red run that sends an alert.

## Recap
Let's recap. First, use retries for temporary errors, error outputs and a dead letter tab for bad items, and an error workflow for failures that stop a run. Second, the error workflow records the failure and notifies a person, without personal data or secrets. Third, keep a run log with one row per run.

## CTA
Now it is your turn. In the exercise below this video, you will break your workflow with a wrong API key, confirm that the error workflow logs the failure and notifies you, and then fix the key. It takes about forty minutes. In the next lesson, we cover Testing and Evaluating Agents. See you there.

## Thumbnail
Headline: Find Failures in Minutes
Image: Navy background, a workflow line with one red node, a teal alert bell and a log sheet row appearing beside it, headline in teal Inter Bold.

## Production Notes
- [VERSION] n8n Error Trigger node, error workflow setting, Retry On Fail, On Error options (error output), Error Trigger output fields, email node names, and whether error workflows run for manual executions must be checked against the current release. The voiceover says only that 'in her release' the error workflow did not start on a manual run; re-record that line if the current release behaves differently.
- Screen recording: the wrong API key is a fake value in a copy of the credential; blur all real keys and email addresses. The notification email must show no key or personal data.
- Petra Dvořák and her Prague accounting firm are fictional.
