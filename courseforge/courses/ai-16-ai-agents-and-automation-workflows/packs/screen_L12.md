# Screen Demo Pack: AI-16 L12 Human-in-the-Loop Approval

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L12_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Show workflow 1: trigger → AI Agent with read-only tools for orders and policy
2. Add Google Sheets: append to 'approvals' with order_id, request, draft_reply, refund_amount, reason, status = pending

**Narration over this clip (for pacing)**

> Let's build it. Diego Ramírez runs customer service for an online clothing shop in Mexico City. His refund agent reads a request, checks the order sheet and the refund policy, and drafts a decision. It never refunds alone. The first workflow ends by adding each draft to an approvals tab, as pending.

## Clip 2: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L12_screen_2.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Run with the sample request 'My jacket arrived torn, I want my money back.'
2. Open the 'approvals' tab and show the new row: draft_reply, refund_amount, reason, status pending (example output)

**Narration over this clip (for pacing)**

> He runs it with a sample request: my jacket arrived torn, I want my money back. In the new row, you'll see something like a draft reply, a refund amount, and the reason: damaged on arrival, within the return period.

## Clip 3: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L12_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Workflow 2: Schedule Trigger every few minutes
2. Google Sheets: get rows where status = approved AND sent_at is empty
3. Send the reply to his own test address (blurred)
4. Google Sheets: update sent_at

**Narration over this clip (for pacing)**

> The second workflow starts on a schedule, every few minutes. It reads rows that are approved and not yet sent. It sends the reply, for the course only to his own test address, and then writes the sent time.

## Clip 4: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L12_screen_4.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Change the row's status to 'approved'
2. Wait for the schedule: show the test email arriving and sent_at filled
3. Add a second request and set it to 'rejected'
4. Run the schedule: nothing is sent

**Narration over this clip (for pacing)**

> He sets the row to approved, and waits for the schedule. The test email arrives, and the sent time is filled. Then he adds a second request, and rejects it. Nothing is sent. The refund itself stays manual. The agent saves time on reading and drafting. People keep control of money.

## Production notes for this lesson

- [VERSION] n8n approval options: Wait node resume modes (form, webhook, time limit), 'send and wait for response' operations in email and chat nodes, Schedule Trigger and Google Sheets filter options must be checked against the current release.
- Screen recording: the reply is sent only to Diego's own test address; blur the email address. The refund itself is never processed on screen; it stays manual in the shop's payment system.
- The draft reply, refund amount and reason are example outputs.
- Diego Ramírez and his Mexico City clothing shop are fictional; the order sheet and requests are invented.
