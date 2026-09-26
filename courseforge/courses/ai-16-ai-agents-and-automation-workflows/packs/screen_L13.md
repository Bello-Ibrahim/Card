# Screen Demo Pack: AI-16 L13 Error Handling, Retries and Logging

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L13_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Create a new workflow 'Error handler'
2. Add an Error Trigger node
3. Add Google Sheets: append to 'errors' with time, workflow, node, message, execution_url mapped from the Error Trigger output

**Narration over this clip (for pacing)**

> Let's build it. Petra Dvořák automates reports at an accounting firm in Prague, Czechia. Her classification workflow runs every night. First, she creates a new workflow called Error handler, with an error trigger. It adds a row to an errors tab, with the time, workflow, node, message and link.

## Clip 2: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L13_screen_2.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Add an email node: 'Workflow X failed at node Y: message. Link: …' to her own address (blurred)
2. Open the main workflow → Settings → Error workflow: 'Error handler'

**Narration over this clip (for pacing)**

> Then it sends her a short email: which workflow failed, at which node, the message, and the link. In the main workflow's settings, she selects Error handler as its error workflow.

## Clip 3: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L13_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Claude HTTP Request node → Settings → Retry On Fail: 3 tries, wait between tries
2. On Error: continue (using error output)
3. Error output → Google Sheets append to 'dead_letter' with item ID and error message
4. End of workflow: Google Sheets append to 'log' with counts and total tokens

**Narration over this clip (for pacing)**

> On the Claude request node, she turns on retry on fail, with three tries and a wait. She sets on error to continue, using the error output, which goes to a dead letter tab. At the end, she adds a log row with counts and total tokens.

## Clip 4: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L13_screen_4.mp4`
- **Target length:** about 29 seconds

**Steps**

1. Put a fake key in a copy of the credential
2. Run manually: the Error handler does not start
3. Activate the schedule and let it run
4. Show the new 'errors' row and the email with no secrets
5. Restore the correct key and run again

**Narration over this clip (for pacing)**

> Now she breaks it on purpose, with a wrong API key, and runs it by hand. The error workflow does not start. She checks the documentation. In her release, error workflows run only for triggered runs. So she tests with the active schedule. The error row appears, and the email arrives: one clear row, one short email, and no secrets in it. Then she restores the correct key.

## Production notes for this lesson

- [VERSION] n8n Error Trigger node, error workflow setting, Retry On Fail, On Error options (error output), Error Trigger output fields, email node names, and whether error workflows run for manual executions must be checked against the current release. The voiceover says only that 'in her release' the error workflow did not start on a manual run; re-record that line if the current release behaves differently.
- Screen recording: the wrong API key is a fake value in a copy of the credential; blur all real keys and email addresses. The notification email must show no key or personal data.
- Petra Dvořák and her Prague accounting firm are fictional.
