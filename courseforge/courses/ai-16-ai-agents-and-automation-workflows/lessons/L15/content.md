# L15 Capstone Build: Design and Build Your Agent

Course: AI-16 · Module: M4 · Objectives: O3, O4, O7 · Video: 5 min (screen demo)

## Hook
You now have every part: triggers, Sheets, the Claude API, validation, routing, tools, memory, approval and error handling. In the capstone you put them together to automate one real business process, from the first input to the final action.

## Explanation
The capstone has two steps. In this lesson you **design and build a first working version**. In L16 you test it, make it reliable and present it.

**Choose a process** that is real, repeated and has clear inputs and outputs. Good examples:

- Supplier invoice intake: extract fields, check against purchase orders, queue for payment approval.
- Event registration: read sign-ups, answer questions, assign sessions, draft confirmations.
- Customer enquiry triage: classify, look up order data, draft replies, route hard cases.

Avoid processes that make automated decisions about people. If your process touches hiring, credit, insurance, housing or similar decisions, the agent may only collect and summarise information; a person decides, and your design must show that approval step.

**Write a one-page design** before you build. It has six parts:

1. **Trigger:** what starts a run (Schedule, new sheet row, **Webhook**, form, Chat Trigger). [VERSION]
2. **Steps:** the path in order, marking which steps are rules and which use the model (L01, L07).
3. **Tools:** each tool with name, description and whether it reads or writes (L09).
4. **Approval points:** every irreversible or external action, and who approves (L12).
5. **Failure modes:** what can go wrong at each step and what the workflow does then (L13).
6. **Data:** what data flows where, confirmation that you use sample or anonymised data, and what is stored. [REGION]

**Build the simplest version first.** Start with a fixed workflow and add an AI step where needed. Use the AI Agent node only for the part where the steps really depend on the input. Get it running end to end on 5 inputs before you add polish.

**Analogy:** The design page is an architect's floor plan. You can move a wall on paper in a minute; moving it after the concrete is poured takes weeks. Ten minutes on the design page saves hours of rebuilding nodes.

## Worked Example
Nguyen Thi Lan organises conferences for a hypothetical events company in Hanoi, Vietnam. She automates registration questions for a sample event. Her design page:

- **Trigger:** a **Webhook** node that receives form submissions (for testing, she sends requests with a free API client); a **Schedule Trigger** for the approval sender. [VERSION]
- **Steps:** (1) rule: reject empty submissions; (2) Claude: classify as registration, session_change, dietary_request, refund_request or not_sure, as validated JSON; (3) Switch; (4) for session_change, an AI Agent with tools; (5) draft reply to "approvals".
- **Tools:** `get_registration` (read), `get_session_capacity` (read), `propose_session_change` (writes a *proposal* row only).
- **Approval points:** all replies; every refund request goes to finance staff, never to the agent.
- **Failure modes:** invalid JSON (retry once, then review), API down (retry, then error workflow), session full (agent says so, proposes alternatives).
- **Data:** invented attendee names and emails only. [REGION]

On screen, she builds the first version:

1. Adds the **Webhook** node, copies its test URL and sends one sample submission from her API client. [VERSION]
2. Adds the IF rule, the Claude HTTP Request, and the validation Code node from L06.
3. Adds a Switch; connects session_change to an **AI Agent** with the Anthropic Chat Model and her three tools. [VERSION]
4. Connects all branches to a Google Sheets append to "approvals" with `status` = "pending".
5. Sends 5 test submissions, one of each type, and checks that each lands in "approvals" with a sensible draft.

It works end to end. Error handling and the full test set come in L16.

## Common Mistake
Learners often design an agent that does everything: one AI Agent node with ten tools and a long system message. It is hard to test and hard to explain. Most of your process should be a clear workflow. Use the agent only for the step that really needs its flexibility, and keep write actions behind approval.

## Key Takeaways
1. Choose a real, repeated process with clear inputs and outputs, and keep a person in charge of any decision about people.
2. Write a one-page design: trigger, steps, tools, approval points, failure modes and data.
3. Build the simplest version that runs end to end on 5 inputs, using an agent only where the steps depend on the input.

## Hands-on Exercise
**Task:** Capstone step 1: write the design page and build a working version of your agent in n8n that runs end to end on 5 test inputs using Google Sheets and the Claude API.
**Tools:** n8n self-hosted; Google Sheets; Claude API; a document editor for the design page.
**Steps:**
1. Choose your process and write one sentence on why it is worth automating.
2. Write the one-page design with all six parts. Mark every rule step and every model step.
3. Create the sheets you need with invented sample data. Do not use real personal or confidential data. [REGION]
4. Build the trigger, the main path and at least one tool used by the agent or the workflow. [VERSION]
5. Send all output that would reach a customer or change a record to an approval tab.
6. Run 5 different test inputs end to end and save the execution links or screenshots.
**What good looks like:** A clear design page that someone else could build from, a workflow that completes 5 runs without manual fixes, sensible outputs in the sheets, and no irreversible action without approval.
**Time:** about 90 minutes

## Review Flags
- [VERSION] n8n Webhook node (test and production URLs), Schedule Trigger, Chat Trigger, AI Agent node and Anthropic Chat Model node must be checked against the current release.
- [REGION] Capstone data: storing personal data (such as attendee names and emails) in Google Sheets and sending it to an external API may be restricted by local data protection law. Learners must use invented or anonymised sample data.
