# L01 From Scripts to Agents

Course: AI-16 · Module: M1 · Objectives: O1, O2 · Video: 5 min

## Hook
Two teams want to "use AI agents". One needs to copy invoice totals into a spreadsheet every morning. The other needs to answer unusual customer questions that nobody can predict. Only one of them needs an agent. By the end of this lesson you will know which one, and why.

## Explanation
Automation is not one thing. It is a spectrum with three main points.

**1. Fixed workflow (rules only).** A trigger starts a sequence of steps that never changes: "When a new row appears, copy column B to the accounts sheet and send a confirmation." Every run follows the same path. It is fast, cheap, easy to test and easy to explain. It fails when the input does not match what the rules expect.

**2. Workflow with an AI step.** The path is still fixed, but one step asks a language model to do something rules cannot do well, such as summarise a message, classify it or extract fields from free text. The model does not decide *what happens next*. Your workflow does, often using the model's output in an IF or Switch step.

**3. Agent.** The model receives a goal, a set of tools and some instructions. It then chooses its own next step, runs a tool, looks at the result and decides again, until it reaches the goal or a stop condition. The path is not written in advance.

As you move from 1 to 3, you gain flexibility. You also pay more, because an agent may call the model many times for one task. The result becomes harder to predict and test, and the risk grows, because the system can take actions you did not plan for.

A useful rule: **choose the least freedom that solves the problem.** Use a fixed workflow when the steps are known. Add an AI step when one part needs language understanding. Use an agent only when the steps really depend on the situation and you can limit what it is allowed to do.

**Analogy:** A fixed workflow is a recipe that a cook follows exactly: same ingredients, same order, same result. An agent is a chef who opens the fridge, sees what is there and decides what to cook. The chef can handle surprises, but you cannot be sure what will arrive on the plate, and the chef may use expensive ingredients. For a school canteen that serves the same meal to 500 children, you want the recipe.

The building blocks you will use in this course are:

- **Trigger:** what starts a run (a schedule, a new sheet row, a webhook, a button).
- **Node:** one step in a workflow (read a sheet, call an API, check a condition).
- **Tool:** an action that an agent is allowed to choose, such as "look up an order".
- **Memory:** information the agent keeps between steps or messages.
- **Agent loop:** the repeated cycle of decide, act and check (L02).

## Worked Example
Tomás Herrera manages operations at a hypothetical logistics company in Montevideo, Uruguay. He lists three tasks.

| Task | Choice | Reason |
|---|---|---|
| Copy delivery counts from a scanner export into a report sheet every night | Fixed workflow | The format never changes; rules are cheaper and always correct. |
| Read driver notes such as "gate locked, left with neighbour" and tag them as delivered, failed or needs follow-up | Workflow with an AI step | The notes are free text, but the next steps for each tag are known. |
| Handle a customer who writes "my parcel is late, can I change the address, and why was I charged twice?" | Agent, with limits | The steps depend on the message: check tracking, check billing, maybe draft an address change. |

For the third task, Tomás does not let the agent issue refunds or change addresses alone. It may look up data and draft replies, but a person approves any change. That keeps the flexibility and limits the risk.

## Common Mistake
Many teams start with an agent because it sounds more advanced. They then find that it is slower, costs more per task, and sometimes takes a different path for the same input. Most business processes are mainly fixed, with one or two steps that need language understanding. Start with the simplest design that works, and add freedom only where a fixed path clearly fails.

## Key Takeaways
1. Automation is a spectrum: fixed workflow, workflow with an AI step, and agent. Each step to the right adds flexibility, cost and risk.
2. An agent chooses its own next step using tools and a loop; a workflow with an AI step still follows a path that you designed.
3. Choose the least freedom that solves the problem, and limit what an agent may do on its own.

## Hands-on Exercise
**Task:** Sort 8 business tasks into "fixed workflow", "workflow with an AI step" or "agent", and justify two choices.
**Tools:** Pen and paper, or any free notes or spreadsheet app.
**Steps:**
1. Read the 8 tasks: (a) invoice entry for a supplier in Lagos whose invoices always use the same template; (b) email triage for a shop in São Paulo that receives questions, complaints and orders; (c) sending a weekly stock report every Monday; (d) extracting names and amounts from scanned receipts in different layouts; (e) answering open customer questions that may need order, stock and delivery data; (f) renaming uploaded files by date; (g) translating product descriptions into three languages; (h) researching a new supplier and preparing a comparison from several sources.
2. Label each task with one of the three categories.
3. Choose the two labels you were least sure about and write one sentence of justification for each, using cost, reliability or risk.
**What good looks like:** Tasks with a stable format (a, c, f) are fixed workflows. Tasks that need language understanding but have a known path (b, d, g) are workflows with an AI step. Only tasks whose steps depend on the situation (e, h) are agents, and your justification mentions a limit on what the agent may do.
**Time:** about 15 minutes

## Review Flags
- None. The lesson is conceptual and uses hypothetical examples, so no facts, tool versions or regional rules need checking.
