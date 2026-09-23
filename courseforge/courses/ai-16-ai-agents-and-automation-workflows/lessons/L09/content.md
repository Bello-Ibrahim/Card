# L09 Tool Use: Letting the Model Call Functions

Course: AI-16 · Module: M3 · Objectives: O1, O4 · Video: 5 min

## Hook
In L02 you saw that the model does not run tools itself; it only asks for them. Today you see exactly how that request looks, and why the words you write in a tool description decide whether the agent picks the right action.

## Explanation
With **tool use**, you send the model a list of tools together with the messages. Each tool has three parts:

- **name:** a short, clear identifier, such as `check_stock`.
- **description:** plain language that says what the tool does, when to use it, and when *not* to use it. The model chooses tools mainly from these descriptions.
- **input_schema:** a JSON Schema that lists the inputs, their types and which ones are required.

The exchange then works like this [VERSION]:

1. You send the messages and the tools.
2. If the model wants a tool, the response has `stop_reason` equal to `"tool_use"` and a content block of type `tool_use` with an `id`, the tool `name` and the `input`.
3. Your code runs the tool and sends back a new user message with a `tool_result` block that uses the same `tool_use_id`.
4. The model continues. It may ask for another tool, or give a final answer (`stop_reason` is then `"end_turn"`).

The loop from L02 in real code, with the official `anthropic` SDK (`run_tool` is your own function):

```python
messages = [{"role": "user", "content": question}]
for _ in range(MAX_STEPS):
    resp = client.messages.create(model="MODEL", max_tokens=500,
                                  tools=tools, messages=messages)
    if resp.stop_reason != "tool_use":
        break
    messages.append({"role": "assistant", "content": resp.content})
    results = [{"type": "tool_result", "tool_use_id": b.id,
                "content": run_tool(b.name, b.input)}
               for b in resp.content if b.type == "tool_use"]
    messages.append({"role": "user", "content": results})
```

`MODEL` is a placeholder: check the current models page for model IDs. [VERSION] A response can contain more than one tool request, which is why the code collects all `tool_use` blocks.

**Analogy:** The model is a manager who cannot leave the office but can ask an assistant to make phone calls. The manager writes a note: "Call the warehouse, ask about item 4471." The assistant (your code) makes the call and reports back with the answer, quoting the note number. The manager can only ask for calls that are on the assistant's approved list, and the assistant can refuse a call that breaks the rules.

**Writing good tools:**

- One clear job per tool. `check_stock` and `create_reorder` are better than one `manage_inventory` tool.
- Say when not to use the tool: "Do not use this to check prices."
- Use strict inputs: types, enums and required fields.
- Return short, clear results, including errors the model can understand, such as "product not found".
- Separate reading from writing. Tools that change things (create, send, delete) need extra checks, and often human approval (L12).

## Worked Example
Ayesha Siddiqui manages a hypothetical pharmacy in Karachi, Pakistan. She sketches a stock-check agent. One of its tools:

```json
{
  "name": "check_stock",
  "description": "Returns the quantity in stock for one product ID at this pharmacy. Use after find_product has returned an ID. Do not use for prices.",
  "input_schema": {
    "type": "object",
    "properties": {"product_id": {"type": "string", "description": "ID such as P-0412"}},
    "required": ["product_id"]
  }
}
```

A staff member asks, "Do we have enough of product P-0412 for 30 packs?" The model returns a `tool_use` block: name `check_stock`, input `{"product_id": "P-0412"}` (example output). Her code reads the sheet and returns `"18 packs in stock"` as a `tool_result`. The model answers: "No, 18 packs are in stock, 12 short. Do you want me to prepare a reorder request?" (example output)

The reorder tool will only *create a request* in a sheet for a pharmacist to approve. It never places an order with a supplier.

## Common Mistake
Learners write vague descriptions such as "stock tool" or "gets data". The model then uses the wrong tool, invents inputs or skips the tool and guesses the answer. The description is your instruction to the model. Write it as if you were explaining the tool to a new colleague: what it does, what input it needs, what it returns and when not to use it.

## Key Takeaways
1. Each tool has a name, a description and an input schema; the model chooses tools mainly from the descriptions.
2. The loop continues while `stop_reason` is `"tool_use"`: your code runs each tool and returns a `tool_result` with the matching `tool_use_id`.
3. Give each tool one job, strict inputs and clear results, and keep tools that change data separate and controlled.

## Hands-on Exercise
**Task:** Write 3 tool definitions (name, description, inputs) for a stock-check agent at a pharmacy in Karachi: look up a product, check the quantity in stock, and create a reorder request.
**Tools:** A text editor or free notes app; optional: the Claude API documentation page on tool use.
**Steps:**
1. Write `find_product`: input a product name or part of a name; returns matching product IDs.
2. Write `check_stock`, using the example as a model.
3. Write `create_reorder_request`: inputs product ID and quantity; its description says that it only creates a request for a pharmacist to approve.
4. For each tool, add one sentence that says when *not* to use it.
5. Write two test questions and, for each, the order in which you expect the tools to be used.
**What good looks like:** Three tools with one job each, valid JSON Schemas with required fields, descriptions a new colleague could follow, and a reorder tool that clearly cannot place an order alone.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Claude API tool use format: the `tools` fields (`name`, `description`, `input_schema`), `stop_reason` values (`tool_use`, `end_turn`), `tool_use` and `tool_result` blocks, the `anthropic` SDK call, and current model IDs for the MODEL placeholder must be checked against current documentation.
