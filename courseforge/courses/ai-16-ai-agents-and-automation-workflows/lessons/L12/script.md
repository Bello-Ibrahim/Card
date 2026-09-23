# L12 Human-in-the-Loop Approval | Presenter Script

Course: AI-16 · Video: 5 min · Words: 699

## Hook
An agent that drafts a wrong reply costs you a minute. An agent that sends a wrong reply, issues the wrong refund, or deletes a customer record can cost you a customer. The difference is one step: a person saying yes before the action runs.

## Explain
Last time, we gave the agent memory. Now we give it a safety step. Start by sorting the actions in your workflow into two groups. Reversible or internal actions, like reading data, drafting text, or calculating. The agent may do these alone. And irreversible or external actions, like sending a message, issuing a refund, or deleting records. These need a person's approval first.

And decisions about people, such as hiring, credit, insurance claims or closing an account, always keep a person in charge. The agent may collect information and suggest. A person decides, and is accountable.

There are two common ways to add approval in n8n. The first is to pause and wait. A Wait node stops the run until something happens, such as a form being submitted. Some email and chat nodes can also send an approve or decline message, and wait for a click. Always set a time limit. If nobody answers, nothing is sent, and the item goes to review.

The second way uses a sheet and two workflows. The first workflow writes each draft to an approvals tab, marked pending. A person changes it to approved or rejected. A second workflow runs on a schedule, finds approved rows that have not been sent yet, performs the action, and records the time it was sent. It is simple, and easy to audit.

What the approver sees matters. Show the original request, the draft, the reason, and the exact action that will run. An approver who only sees the word approve, with a question mark, will soon approve everything without reading.

Think of the two-signature rule for company payments. A clerk prepares the payment, but it only leaves the bank when a second person signs. The clerk does most of the work. The signature is the control.

## Demonstrate
Let's build it. Diego Ramírez runs customer service for an online clothing shop in Mexico City. His refund agent reads a request, checks the order sheet and the refund policy, and drafts a decision. It never refunds alone. The first workflow ends by adding each draft to an approvals tab, as pending.

He runs it with a sample request: my jacket arrived torn, I want my money back. In the new row, you'll see something like a draft reply, a refund amount, and the reason: damaged on arrival, within the return period.

The second workflow starts on a schedule, every few minutes. It reads rows that are approved and not yet sent. It sends the reply, for the course only to his own test address, and then writes the sent time.

He sets the row to approved, and waits for the schedule. The test email arrives, and the sent time is filled. Then he adds a second request, and rejects it. Nothing is sent. The refund itself stays manual. The agent saves time on reading and drafting. People keep control of money.

A common mistake is to let the sending workflow read all rows. Then the same email is sent twice, or a pending row goes out by mistake. Filter on approved and not yet sent, write the sent time straight after the action, and test the rejected and pending cases too.

## Recap
Let's recap. First, irreversible or external actions, and all decisions about people, need a person's approval before they run. Second, in n8n, pause with a Wait node, or use a sheet with a status column and a second scheduled workflow. Third, show approvers the request, the draft and the reason, and make sure each approved action runs exactly once.

## CTA
Now it is your turn. In the exercise below this video, your agent drafts customer replies into a sheet, and a second workflow sends a reply only after a person sets the row to approved. Test an approved, a rejected and a pending row. It takes about forty minutes. In the next lesson, we cover Error Handling, Retries and Logging. See you there.

## Thumbnail
Headline: A Person Says Yes
Image: Navy background, a drafted message card waiting behind a teal gate with a person icon holding an approve button, headline in teal Inter Bold.

## Production Notes
- [VERSION] n8n approval options: Wait node resume modes (form, webhook, time limit), 'send and wait for response' operations in email and chat nodes, Schedule Trigger and Google Sheets filter options must be checked against the current release.
- Screen recording: the reply is sent only to Diego's own test address; blur the email address. The refund itself is never processed on screen; it stays manual in the shop's payment system.
- The draft reply, refund amount and reason are example outputs.
- Diego Ramírez and his Mexico City clothing shop are fictional; the order sheet and requests are invented.
