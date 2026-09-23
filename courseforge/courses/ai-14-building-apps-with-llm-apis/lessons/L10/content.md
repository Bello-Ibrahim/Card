# L10 Tool Loops and Guardrails

Course: AI-14 · Module: M3 · Objectives: O4, O5 · Video: 5 min (screen demo)

## Hook
A tool that reads data can give a wrong answer. A tool that changes data can send a parcel to the wrong city. Once your model can call functions that act in the real world, your code must set the limits, because the model will not.

## Explanation
The L09 loop works for one read-only tool. Real apps need five guardrails.

**1. Handle several tool calls in one turn.** One response can contain more than one `tool_use` block, for example two tracking codes in one question. Run each one and return **all** the `tool_result` blocks together in a single user message.

**2. Cap the number of steps.** A loop that runs "while the stop reason is tool_use" could, in rare cases, keep going and spend money. Set a maximum, such as 5 steps, and stop with a clear message when it is reached.

**3. Check tool inputs strictly.** The input is a parsed object, but treat it like any user input. Validate types, formats and allowed values in your code, for example with Pydantic. Tool definitions can also ask the API for strict schema checking. [VERSION] If an input fails, return a `tool_result` with `"is_error": True` and a short message, so the model can correct itself. Also return an error for any unknown tool name.

**4. Ask a human before any action that changes data.** Reading an order status is safe. Changing an address, cancelling an order or sending money is not. Your code, not the model, must show the planned action to the user and wait for a clear "yes" before running it.

**5. Give each tool the smallest permissions it needs.** The address tool should change only the address field, only for the logged-in customer's own orders, and only through your normal business rules. Never give the model a general "run SQL" or "call any URL" tool.

This lesson keeps tool use inside one app. Multi-step agents and approval workflows are covered in AI-16.

**Analogy:** A new bank clerk can look up balances freely, but every transfer needs a second signature and has a daily limit. The clerk may be very capable; the rules exist because mistakes that move money are expensive and hard to undo.

## Worked Example
Carlos Mendoza runs support for an online furniture shop in Medellín, Colombia. He adds a second tool, `change_delivery_address`, next to the status tool from L09. The core of his loop:

```python
MAX_STEPS = 5
WRITE_TOOLS = {"change_delivery_address"}

for step in range(MAX_STEPS):
    response = client.messages.create(model=MODEL, max_tokens=500,
                                      tools=tools, messages=messages)
    if response.stop_reason != "tool_use":
        break
    messages.append({"role": "assistant", "content": response.content})
    results = []
    for block in response.content:
        if block.type != "tool_use":
            continue
        args = block.input                     # a parsed dict
        if block.name not in HANDLERS:
            out, err = "Unknown tool", True
        elif block.name in WRITE_TOOLS and not confirm(block.name, args):
            out, err = "The customer did not confirm this change.", True
        else:
            out, err = HANDLERS[block.name](args), False
        results.append({"type": "tool_result", "tool_use_id": block.id,
                        "content": out, "is_error": err})
    messages.append({"role": "user", "content": results})
else:
    print("Stopped: too many tool steps. A person will follow up.")
```

`confirm()` shows: "Change the address of order CO-778 to Calle 10 #43-12, Medellín? (yes/no)" and returns `True` only for "yes". Each handler validates its input first: the address handler checks that the order belongs to the current customer, that the order has not shipped, and that the address fields are not empty.

On screen, Carlos tests "Send my order CO-778 to my office instead" and answers "no". The model replies (example output): "No problem, I have not changed the address." Then he asks for four orders at once and sees the loop return four results in one message.

## Common Mistake
Many developers put the safety rule only in the system prompt: "Always ask the user before changing an address." The model usually follows it, but a prompt is a request, not a control. A confusing message or an injected instruction (L11) can lead the model to skip it. Put confirmations, permission checks and step limits in your code, where the model cannot change them.

## Key Takeaways
1. Return all tool results from one turn in a single user message, and cap the loop at a fixed number of steps.
2. Validate every tool input in your code and return an error result for invalid inputs or unknown tools.
3. Require human confirmation in code before any action that changes data, and give each tool the smallest permissions it needs.

## Hands-on Exercise
**Task:** Add a second tool that changes a delivery address, require user confirmation before it runs, and cap the loop at 5 steps.
**Tools:** Your L09 code; `pydantic` for input checks; the current tool-use docs. [VERSION]
**Steps:**
1. Add a `change_delivery_address` tool with an input schema for the order number and new address.
2. Write a handler that validates the input and changes the address only in your local dictionary.
3. Add a `confirm()` function that prints the planned change and waits for "yes".
4. Rewrite your loop with `MAX_STEPS = 5`, an unknown-tool check and error results.
5. Test: a status question with two order numbers; an address change you confirm; one you refuse; an invalid order number.
6. Temporarily set `MAX_STEPS = 1` and check that the stop message appears.
**What good looks like:** Address changes run only after "yes", refusals and invalid inputs return error results without crashing, multi-order questions get all results in one message, and the step limit stops the loop.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Strict tool schema checking, the `is_error` field on tool results and parallel tool-call behaviour must be checked against the current tool-use docs.
- The shop, orders and address in the worked example are invented.
