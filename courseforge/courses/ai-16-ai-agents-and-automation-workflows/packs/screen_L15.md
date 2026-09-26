# Screen Demo Pack: AI-16 L15 Capstone Build: Design and Build Your Agent

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L15_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open Lan's one-page design in a document editor
2. Scroll to Tools: get_registration (read), get_session_capacity (read), propose_session_change (writes a proposal only)
3. Scroll to Approval points: all replies; refund requests → finance staff
4. Scroll to Data: invented attendee names and emails only

**Narration over this clip (for pacing)**

> Session changes go to an agent with three tools. Two only read: registrations and session capacity. The third only writes a proposal row. Every reply needs approval, and every refund request goes to finance staff, never to the agent. And she uses only invented attendee names and emails.

## Clip 2: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L15_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Scroll to Failure modes in the design page
2. Highlight: invalid JSON → retry once, then review
3. Highlight: API down → retry, then error workflow
4. Highlight: session full → agent says so, proposes alternatives

**Narration over this clip (for pacing)**

> She also plans for failure. If the JSON is not valid, the workflow retries once, then sends the item to review. If the API is down, it retries, then the error workflow takes over. And if a session is full, the agent says so, and proposes alternatives.

## Clip 3: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L15_screen_3.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Add a Webhook node and copy its test URL
2. Send one sample submission from a free API client
3. Add the IF rule rejecting empty submissions
4. Add the Claude HTTP Request with the classification prompt
5. Add the validation Code node from L06

**Narration over this clip (for pacing)**

> Now she builds. She adds a webhook node, copies its test address, and sends one sample submission from a free API client. Then she adds the rule, the Claude request, and the validation code from lesson six.

## Clip 4: scene 12

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L15_screen_4.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Add a Switch node on category
2. Connect session_change to an AI Agent with the Anthropic Chat Model
3. Attach the three tools: get_registration, get_session_capacity, propose_session_change
4. Connect every branch to Google Sheets append to 'approvals' with status = pending

**Narration over this clip (for pacing)**

> She adds a Switch, and connects session changes to an AI Agent, with the Anthropic chat model and her three tools. Every branch ends in the approvals tab, marked pending.

## Clip 5: scene 13

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L15_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Send 5 test submissions, one per category
2. Open the executions list: 5 successful runs
3. Open the 'approvals' tab: 5 pending rows with drafts (example output)

**Narration over this clip (for pacing)**

> Finally, she sends five test submissions, one of each type. Each one lands in the approvals tab. In each row, you'll see something like a sensible draft. It works end to end. Error handling and the full test set come next.

## Production notes for this lesson

- [VERSION] n8n Webhook node (test and production URLs), Schedule Trigger, Chat Trigger, AI Agent node and Anthropic Chat Model node must be checked against the current release.
- [REGION] Capstone data: storing personal data (such as attendee names and emails) in Google Sheets and sending it to an external API may be restricted by local data protection law. Learners must use invented or anonymised sample data; the demo uses invented attendees only.
- Screen recording: the 'free API client' used to send test submissions is shown generically; do not name or show a brand. Blur the webhook URL if it contains a host name.
- Nguyen Thi Lan and her Hanoi events company are fictional; the event and attendees are invented.
