# L09 Tool Use: Letting the Model Call Your Functions

Course: AI-14 · Module: M3 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
A customer asks your assistant: "Where is my parcel VN-4471?" The model has never seen your shipping database, so any answer it writes alone is a guess. With tool use, the model can ask your code to look it up, and then answer with real data.

## Explanation
**Tool use** (also called function calling) lets the model request that your code runs a function. The model never runs anything itself. It only asks, and your code decides what to do.

**1. Define the tool.** A tool has three parts:

- `name`: a short identifier, such as `get_shipment_status`.
- `description`: what the tool does and when to use it. The model reads this to decide, so write it carefully.
- `input_schema`: a JSON Schema for the inputs, like the schemas in L05.

**2. Send the tools with the request.** Pass a `tools` list to `messages.create`. Other tool-definition options exist, such as strict schema checking and tool-choice settings. Check the current docs. [VERSION]

**3. The model asks for a tool.** If the model decides to use a tool, the response has `stop_reason` = `"tool_use"`, and the content includes a `tool_use` block with an `id`, the tool `name` and an `input` object. The SDK gives you `input` as a parsed dictionary. Read fields by key; never search the text of the input with string matching.

**4. Your code runs the function and sends the result back.** Add the model's full reply to the messages as an `assistant` message. Then add a `user` message that contains a `tool_result` block with the same `tool_use_id` and the result as `content`.

**5. The model writes the final answer.** Call the API again with the updated messages. Repeat while the stop reason is `"tool_use"`.

**Analogy:** A shop manager is on the phone with a customer who asks if a jacket is in stock. The manager does not guess. They ask an assistant: "Check the stock system for item 2291." The assistant checks and reports "3 in stock", and the manager answers the customer. The model is the manager, your function is the assistant, and the manager never touches the stock system directly.

## Worked Example
Nguyen Thi Lan builds a support assistant for a courier company in Ho Chi Minh City, Vietnam. She starts with a mock tracking function and a local dictionary instead of the real system.

```python
import json

SHIPMENTS = {"VN-4471": "Out for delivery, Da Nang",
             "VN-5820": "Held at customs, Hanoi"}

tools = [{
    "name": "get_shipment_status",
    "description": "Look up the current status of a shipment by its "
                   "tracking code, for example VN-4471.",
    "input_schema": {
        "type": "object",
        "properties": {"tracking_code": {"type": "string"}},
        "required": ["tracking_code"],
    },
}]

def get_shipment_status(tracking_code):
    return SHIPMENTS.get(tracking_code, "Unknown tracking code")

messages = [{"role": "user", "content": "Where is my parcel VN-4471?"}]
response = client.messages.create(model=MODEL, max_tokens=500,
                                  tools=tools, messages=messages)

while response.stop_reason == "tool_use":
    messages.append({"role": "assistant", "content": response.content})
    results = []
    for block in response.content:
        if block.type == "tool_use" and block.name == "get_shipment_status":
            status = get_shipment_status(block.input["tracking_code"])
            results.append({"type": "tool_result", "tool_use_id": block.id,
                            "content": json.dumps({"status": status})})
    messages.append({"role": "user", "content": results})
    response = client.messages.create(model=MODEL, max_tokens=500,
                                      tools=tools, messages=messages)

print(next(b.text for b in response.content if b.type == "text"))
```

Example output: "Your parcel VN-4471 is out for delivery in Da Nang and should reach you soon."

On screen, Lan prints `response.content` after the first call, so learners can see the `tool_use` block, its `id` and its `input`. When she asks "What are your opening hours?", the model answers without calling the tool, because the description says the tool is for tracking codes.

## Common Mistake
Many developers send the tool result back without the model's previous reply, or with a different `tool_use_id`. The API then rejects the request, because every `tool_result` must follow the `assistant` message that contains the matching `tool_use` block. Always append the full `response.content` as the assistant turn, then the results in the next user turn.

## Key Takeaways
1. A tool has a name, a description and an input schema; the description tells the model when to use it.
2. When `stop_reason` is `"tool_use"`, your code runs the function and returns a `tool_result` block with the matching `tool_use_id` in a user message.
3. The model only requests tools. Your code runs them, reads the input as a parsed object, and decides what is allowed.

## Hands-on Exercise
**Task:** Add a tool that looks up an order status in a local dictionary, and test it with 5 customer questions.
**Tools:** Your L02 setup; a text editor; the current tool-use docs. [VERSION]
**Steps:**
1. Create a dictionary with 4 invented order numbers and statuses. Do not use real customer data.
2. Define a `get_order_status` tool with a clear description and an input schema.
3. Write the tool loop from the worked example, adapted to your tool.
4. Print `response.content` after the first call, so you can see the `tool_use` block.
5. Test 5 questions: two with valid order numbers, one with an unknown number, one without any number, and one unrelated question.
6. For each question, record whether the tool was called, with which input, and whether the final answer was correct.
**What good looks like:** The tool is called for the valid and unknown numbers, the unknown number gives a polite "not found" answer, the model asks for a number when none is given, and the unrelated question is answered without the tool.
**Time:** about 35 minutes

## Review Flags
- [VERSION] Tool-definition options (strict mode, tool choice and other fields) and the exact response block format must be checked against the current tool-use docs before scripting.
- The courier company and tracking data are invented.
