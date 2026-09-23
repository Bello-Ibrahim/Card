# L10 Building an Agent in n8n

Course: AI-16 · Module: M3 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
In L09 you wrote the agent loop in code. n8n can run the same loop for you, and it shows every decision in the execution log. Today you build an agent that looks things up and calculates, and you watch it choose its tools.

## Explanation
n8n's **AI Agent** node runs the agent loop. You connect other nodes to it [VERSION]:

- **Chat Model:** the model that makes the decisions. We use the **Anthropic Chat Model** node with a credential that holds your Claude API key, and a MODEL chosen from the current models page. [VERSION]
- **Memory (optional):** keeps earlier messages; see L11.
- **Tools:** nodes the agent may call. Useful ones for this lesson are a **Google Sheets tool** (read rows), a **Calculator** tool and an **HTTP Request tool** (call an API). [VERSION]

A **Chat Trigger** node lets you talk to the agent in a chat panel inside the editor. [VERSION] In the AI Agent node you write a **system message** with the agent's goal, rules and limits. You can also set a maximum number of iterations. [VERSION]

Each tool node has a **description** field. As in L09, this text tells the model what the tool does and when to use it, so write it carefully. n8n can also let the model fill some tool parameters itself, for example a product name to search for. [VERSION]

Why a calculator? Language models can make mistakes with arithmetic. A calculator tool gives exact results, and the log shows the calculation, so you can check it.

**Analogy:** The AI Agent node is like a project coordinator sitting at a desk with a telephone. The chat model is the coordinator's judgement, the tools are the numbers on the speed-dial list, and the execution log is the call record: who was called, what was asked and what came back.

**Safety in this lesson:** give the agent read-only tools. A Sheets tool that only reads rows cannot damage your data. Tools that write or send come later, with approval steps.

## Worked Example
Kofi Mensah owns a hypothetical hardware shop in Accra, Ghana. He has a "products" sheet with `product_id`, `name`, `unit_price`, `in_stock`, all invented. On screen, he:

1. Creates a new workflow and adds a **Chat Trigger**. [VERSION]
2. Adds an **AI Agent** node and connects the trigger to it.
3. Connects an **Anthropic Chat Model** sub-node, selects his Claude credential and enters a MODEL from the current models page. [VERSION]
4. Writes the system message: "You answer stock and price questions for the shop's staff. Always look up products in the sheet. Always use the calculator for totals. If a product is not found, say so. Do not guess prices."
5. Connects a **Google Sheets** tool set to read rows from "products", with the description: "Returns all products with ID, name, unit price and quantity in stock. Use it to find a product and its price." [VERSION]
6. Connects a **Calculator** tool. [VERSION]
7. Opens the chat and types: "Is the 10 mm drill bit in stock, and what is the total for 12 units?"
8. Opens the execution log. It shows the agent calling the Sheets tool, then the Calculator with `12 * 3.75`, then answering: "Yes, 40 are in stock. 12 units cost 45.00 cedis." (example output)

He then asks about a product that does not exist. The log shows one Sheets call and the answer "I could not find that product." That is the correct behaviour.

## Common Mistake
Learners often connect many tools "just in case". The agent then has more choices, makes more wrong ones and uses more tokens, because every tool description is sent with every request. Connect only the tools the task needs. If the agent picks the wrong tool, improve the tool descriptions and the system message before you add anything else.

## Key Takeaways
1. The AI Agent node runs the agent loop with a chat model, optional memory and connected tool nodes.
2. Tool descriptions and the system message guide which tool the agent picks; the execution log shows every choice.
3. Start with few, read-only tools and use a calculator tool for arithmetic instead of trusting the model's mental maths.

## Hands-on Exercise
**Task:** Build an agent that answers "Is product X in stock, and what is the total price for N units?" from a product sheet. Test it with 5 questions and note which tools it used each time.
**Tools:** n8n self-hosted; Google Sheets; Claude API (keep the conversation short).
**Steps:**
1. Create a "products" sheet with 10 invented products.
2. Build: Chat Trigger, AI Agent, Anthropic Chat Model, Google Sheets tool (read only), Calculator tool. [VERSION]
3. Write a system message with the goal, the rule to always use the calculator, and what to do when a product is not found.
4. Ask 5 questions: 3 normal, 1 with a product that does not exist, and 1 with a spelling mistake in the product name.
5. For each question, record in a table: tools used in order, the final answer, and whether it was correct.
6. Improve one tool description or the system message, and repeat the question that failed.
**What good looks like:** A table with 5 rows showing tools used and correctness, totals that match the calculator, a clear "not found" answer for the missing product, and one documented improvement.
**Time:** about 40 minutes

## Review Flags
- [VERSION] n8n AI Agent node, Anthropic Chat Model node, Chat Trigger, Google Sheets tool, Calculator tool, HTTP Request tool, max iterations setting and model-filled tool parameters must be checked against the current release; agent node options change often.
- [VERSION] Current Claude model IDs for the MODEL placeholder.
