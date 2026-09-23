# L02 How an Agent Works: The Agent Loop

Course: AI-16 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
A language model on its own can only produce text. It cannot open a file, check a database or send a message. So how does an "agent" complete a task with several steps? The answer is a simple loop that your software runs around the model.

## Explanation
An agent repeats four actions until a stop condition is met:

1. **Observe.** Collect the current situation: the task, the conversation so far and the results of earlier steps.
2. **Decide.** Send all of this to the model. The model replies either with a final answer or with a request to use a tool, for example "look up policy for category: meals".
3. **Act.** Your software (not the model) runs the requested tool and gets a result.
4. **Check.** Add the result to the situation and go back to step 1.

The loop stops when the model gives a final answer, or when a limit is reached: a maximum number of steps, a time limit or a cost limit. Always set a maximum. Without one, a confused agent can call tools again and again.

Every agent has four parts:

- **The model** makes the decisions. It reads text and returns text or tool requests.
- **The tools** are the actions it may request. Each tool has a name, a description and the inputs it expects. The agent can only do what its tools allow, so the tool list is your main safety control.
- **The memory** is what the agent can see from earlier steps: the messages and tool results in the current task, and sometimes records stored from earlier tasks (L11).
- **The instructions** (the system prompt) describe the goal, the rules, the tone and when to stop or ask a person.

**Analogy:** Think of a detective working on a case. The detective looks at the evidence (observe), decides which witness to interview next (decide), goes to the interview (act) and adds the new facts to the case file (check). The detective repeats this until the case is solved or the manager says "stop, we are out of time". The detective is the model, the interviews are the tools, the case file is the memory and the manager's brief is the instructions.

In code, the loop is short. This is pseudocode, not a real library:

```python
steps = 0
while steps < MAX_STEPS:
    reply = model.decide(instructions, memory, tools)
    if reply.is_final_answer:
        break
    result = run_tool(reply.tool_name, reply.tool_input)
    memory.append(reply, result)
    steps += 1
```

You will see the real format for the Claude API in L09, and n8n's AI Agent node runs this loop for you in L10.

## Worked Example
Priya Raman works in finance at a hypothetical consultancy in Chennai, India. She designs an expense-checking agent with sample data only.

- **Instructions:** "Check each expense claim against the travel policy. Flag any problem with a reason. Never approve or reject a claim yourself."
- **Tools:** `read_receipt` (returns date, amount, category and vendor from the claim sheet), `lookup_policy` (returns the limit and rules for a category), `flag_claim` (writes a flag and reason to the review sheet).
- **Memory:** the messages and tool results for the current claim only.
- **Stop condition:** a final summary, or at most 6 tool calls.

One run looks like this:

1. Observe: "Check claim 104." Decide: call `read_receipt(104)`. Result: meal, 3 people, amount above the usual level.
2. Decide: call `lookup_policy("meals")`. Result: a per-person limit and "client meals need the client name".
3. Decide: the amount per person is above the limit and no client name is given. Call `flag_claim(104, "over meal limit; client name missing")`.
4. Decide: final answer, "Claim 104 flagged for review: two issues." The loop stops.

Notice what the agent did *not* do. It did not reject the claim. A person makes that decision, using the agent's reasons.

## Common Mistake
People often think the model runs the tools itself or "has access to" the internet or the database. It does not. The model only *asks* for a tool; your software decides whether to run it, runs it and returns the result. This is good news: it means you control exactly which actions are possible, and you can check or block a request before it runs.

## Key Takeaways
1. An agent repeats observe, decide, act and check until it gives a final answer or reaches a step, time or cost limit.
2. The four parts of an agent are the model, the tools, the memory and the instructions.
3. The model only requests tools; your software runs them, which makes the tool list your main safety control.

## Hands-on Exercise
**Task:** Draw the agent loop for a customer-support agent, label its tools and write its stop condition.
**Tools:** Pen and paper, or draw.io (free, in a browser).
**Steps:**
1. Choose a scenario: a support agent for a hypothetical online bookshop that answers questions about orders and delivery.
2. Draw four boxes in a circle: Observe, Decide, Act, Check. Put "Model" next to Decide.
3. List 3 to 4 tools next to Act, each with a one-line description, for example `get_order_status(order_id)`.
4. Write the instructions in two or three sentences, including one thing the agent must never do alone.
5. Write the stop condition: when it gives a final answer, and the maximum number of steps.
6. Add one arrow to "Ask a person" for cases the agent cannot handle.
**What good looks like:** A clear loop with four labelled stages, tools that match the scenario and are limited to what it needs, a maximum step count, and a path to a person for refunds or unclear cases.
**Time:** about 20 minutes

## Review Flags
- None. The lesson is conceptual, uses pseudocode rather than a real API, and uses a hypothetical example.
