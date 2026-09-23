# L12 Human-in-the-Loop Approval

Course: AI-16 · Module: M3 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
An agent that drafts a wrong reply costs you a minute. An agent that *sends* a wrong reply, issues the wrong refund or deletes a customer record can cost you a customer. The difference is one step: a person saying "yes" before the action runs.

## Explanation
Sort the actions in your workflow into two groups:

- **Reversible or internal:** reading data, drafting text, writing to a review tab, calculating. The agent may do these alone.
- **Irreversible or external:** sending an email or message, issuing a refund or payment, deleting or overwriting records, changing a customer's account. These need **human approval** first.

Decisions about people, such as hiring, credit, insurance claims or account closure, always keep a person in charge. The agent may collect information and suggest, but a person decides and is accountable.

There are two common ways to add approval in n8n.

**1. Pause and wait.** A **Wait** node stops the run until something happens, for example a form submission or a call to a special resume URL. [VERSION] Some nodes, such as email and chat nodes, also offer a "send and wait for response" operation that sends an approve/decline message and pauses until someone clicks. [VERSION] Set a time limit, and decide what happens when nobody answers: normally, nothing is sent and the item goes to a review list.

**2. Approve in a sheet (two workflows).** The first workflow drafts and writes each item to an "approvals" tab with `status` = "pending". A person reviews the row and changes `status` to "approved" or "rejected". A second workflow, on a **Schedule Trigger**, reads rows where status is "approved" and `sent_at` is empty, performs the action and writes `sent_at`. This is simple, easy to audit and easy to learn.

What the approver sees matters. Show the original request, the agent's draft, the reason for its choice and the exact action that will run. An approver who sees only "Approve?" will soon approve everything without reading.

**Analogy:** Approval is like the two-signature rule for company payments. A clerk can prepare the payment, but it only leaves the bank when a second person signs. The clerk does most of the work; the signature is the control.

## Worked Example
Diego Ramírez runs customer service for a hypothetical online clothing shop in Mexico City. His refund agent reads a request, checks the invented order sheet and the refund policy, and drafts a decision. It never refunds alone. On screen, he:

1. Builds the first workflow: trigger, AI Agent (read-only tools for orders and policy), then Google Sheets (append to "approvals" with `order_id`, `request`, `draft_reply`, `refund_amount`, `reason`, `status` = "pending"). [VERSION]
2. Runs it with a sample request: "My jacket arrived torn, I want my money back." The row shows a draft reply, a refund amount and the reason "damaged on arrival, within return period" (example output).
3. Builds the second workflow: **Schedule Trigger** every few minutes, Google Sheets (get rows where `status` = "approved" and `sent_at` is empty), a node that sends the reply (for the course, a test email to himself), then Google Sheets (update `sent_at`). [VERSION]
4. Changes the row's status to "approved" and waits for the schedule. The test email arrives and `sent_at` is filled.
5. Adds a second request that is rejected. Nothing is sent.

The refund itself stays manual in the shop's payment system. The agent saves time on reading and drafting; people keep control of money.

## Common Mistake
Learners often add approval but let the sending workflow read *all* rows, not only approved and unsent ones. When the schedule runs again, the same email is sent twice, or a pending row is sent by mistake. Filter on both `status` = "approved" and an empty `sent_at`, and write `sent_at` straight after the action. Test the rejected and pending cases, not only the approved one.

## Key Takeaways
1. Irreversible or external actions, and all decisions about people, need a human approval step before they run.
2. In n8n, pause with a Wait node or a send-and-wait operation, or use a sheet with a status column and a second scheduled workflow.
3. Show approvers the request, the draft and the reason, and make sure each approved action runs exactly once.

## Hands-on Exercise
**Task:** Add an approval step: the agent drafts a customer reply into a sheet, and the workflow sends the reply only after a person sets the row to "approved".
**Tools:** n8n self-hosted; Google Sheets; Claude API; an email account for test messages to yourself.
**Steps:**
1. Create an "approvals" tab with `request`, `draft_reply`, `reason`, `status` and `sent_at`.
2. Change your agent so it appends each draft with `status` = "pending". Use invented customer requests only.
3. Build a second workflow with a Schedule Trigger that reads rows where `status` = "approved" and `sent_at` is empty. [VERSION]
4. Send the reply to your own test address, then write `sent_at`.
5. Test three rows: approved, rejected and left pending. Run the schedule twice.
**What good looks like:** Only the approved row is sent, it is sent exactly once, and rejected and pending rows are never sent.
**Time:** about 40 minutes

## Review Flags
- [VERSION] n8n approval options: Wait node resume modes (form, webhook, time limit), "send and wait for response" operations in email and chat nodes, Schedule Trigger and Google Sheets filter options must be checked against the current release.
