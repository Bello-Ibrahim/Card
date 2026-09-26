# L15 Capstone Build: Design and Build Your Agent | Presenter Script

Course: AI-16 · Video: 5 min · Words: 695

## Hook
You now have every part: triggers, Sheets, the Claude API, validation, routing, tools, memory, approval and error handling. In the capstone, you put them together to automate one real business process, from the first input to the final action.

## Explain
The capstone has two steps. In this lesson, you design and build a first working version. In the next lesson, you test it, make it reliable, and present it.

Choose a process that is real, repeated, and has clear inputs and outputs. For example, supplier invoice intake, event registration, or customer enquiry triage.

Avoid processes that make automated decisions about people. If yours touches hiring, credit, insurance or housing, the agent may only collect and summarise. A person decides, and your design must show that approval step.

Before you build, write a one-page design with six parts. The trigger that starts a run. The steps in order, marking which are rules and which use the model. The tools, and whether each one reads or writes. The approval points, and who approves. The failure modes, and what happens then. And the data: what flows where, and confirmation that it is sample data.

Think of an architect's floor plan. You can move a wall on paper in a minute. Moving it after the concrete is poured takes weeks. Ten minutes on the design page saves hours of rebuilding nodes.

Then build the simplest version first. Start with a fixed workflow, and add an AI step where needed. Use the agent node only for the part where the steps really depend on the input. Get it running end to end on five inputs, before you add polish.

## Demonstrate
Let's see an example. Nguyen Thi Lan organises conferences for an events company in Hanoi, Vietnam. She automates registration questions for a sample event. Her design starts with a webhook that receives form submissions. A rule rejects empty ones. Claude classifies each message, as validated data. A Switch routes it.

Session changes go to an agent with three tools. Two only read: registrations and session capacity. The third only writes a proposal row. Every reply needs approval, and every refund request goes to finance staff, never to the agent. And she uses only invented attendee names and emails.

She also plans for failure. If the JSON is not valid, the workflow retries once, then sends the item to review. If the API is down, it retries, then the error workflow takes over. And if a session is full, the agent says so, and proposes alternatives.

Now she builds. She adds a webhook node, copies its test address, and sends one sample submission from a free API client. Then she adds the rule, the Claude request, and the validation code from lesson six.

She adds a Switch, and connects session changes to an AI Agent, with the Anthropic chat model and her three tools. Every branch ends in the approvals tab, marked pending.

Finally, she sends five test submissions, one of each type. Each one lands in the approvals tab. In each row, you'll see something like a sensible draft. It works end to end. Error handling and the full test set come next.

A common mistake is to design one agent that does everything, with ten tools and a long system message. It is hard to test, and hard to explain. Most of your process should be a clear workflow. Use the agent only where it is really needed, and keep write actions behind approval.

## Recap
Let's recap. First, choose a real, repeated process, and keep a person in charge of any decision about people. Second, write a one-page design: trigger, steps, tools, approval points, failure modes and data. Third, build the simplest version that runs end to end on five inputs.

## CTA
Now it is your turn. This is step one of your capstone. In the exercise below this video, you will write your design page, and build a working version of your agent that runs end to end on five test inputs, with Google Sheets and the Claude API. Allow about ninety minutes. In the next lesson, the final one, we cover Capstone: Test, Harden and Present. See you there.

## Thumbnail
Headline: Design, Then Build
Image: Navy background, a one-page floor-plan style design sheet on the left and a connected n8n-style workflow on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] n8n Webhook node (test and production URLs), Schedule Trigger, Chat Trigger, AI Agent node and Anthropic Chat Model node must be checked against the current release.
- [REGION] Capstone data: storing personal data (such as attendee names and emails) in Google Sheets and sending it to an external API may be restricted by local data protection law. Learners must use invented or anonymised sample data; the demo uses invented attendees only.
- Screen recording: the 'free API client' used to send test submissions is shown generically; do not name or show a brand. Blur the webhook URL if it contains a host name.
- Nguyen Thi Lan and her Hanoi events company are fictional; the event and attendees are invented.
