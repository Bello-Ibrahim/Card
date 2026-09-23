# L09 Tool Use: Letting the Model Call Your Functions | Presenter Script

Course: AI-14 · Video: 5 min · Words: 674

## Hook
A customer asks your assistant, where is my parcel? The model has never seen your shipping database, so any answer it writes alone is a guess. With tool use, the model can ask your code to look it up, and then answer with real data.

## Explain
In the last lesson, you put a chat app on the web. Now let's give it real data. Tool use, also called function calling, lets the model request that your code runs a function. The model never runs anything itself. It only asks, and your code decides what to do.

A tool has three parts. A name, a description, and an input schema, like the schemas from lesson five. The model reads the description to decide when to use the tool, so write it carefully. You send the list of tools with your request. Other options exist, such as strict schema checking, so check the current docs.

Here is the cycle. If the model wants a tool, the stop reason is tool use, and the reply contains a tool use block with an ID, the tool name and its input. The SDK gives you the input as a parsed dictionary, so read fields by key, never with string matching.

Your code runs the function. You add the model's full reply to the messages, then a user message with a tool result that carries the same ID. Then you call the API again, and the model writes its answer. You repeat this while the stop reason is tool use.

Picture a shop manager on the phone with a customer who asks if a jacket is in stock. The manager does not guess. They ask an assistant to check the stock system, and then answer.

The model is the manager. Your function is the assistant. And the manager never touches the stock system directly.

## Demonstrate
Nguyen Thi Lan builds a support assistant for a courier company in Ho Chi Minh City, Vietnam. She starts with a mock tracking function and a small local dictionary, not the real system.

At the top of her file is the dictionary with two invented shipments. Then the tool definition, with a clear description and a schema that requires a tracking code. The function itself just looks up the code.

She sends the question with the tools list, and prints the reply content. On screen, you can see the tool use block, with its ID, the tool name and the input, a parsed dictionary with the tracking code.

Now the loop. While the stop reason is tool use, she appends the full reply as the assistant turn. For each tool use block, she runs the function, reading the input by key, and builds a tool result with the same ID. She sends the results back and calls the API again.

She runs it. You'll see something like, your parcel is out for delivery in Da Nang and should reach you soon. Then she asks about opening hours. The model answers without calling the tool, because the description says it is for tracking codes.

A common mistake is to send the tool result without the model's previous reply, or with a different ID. The API rejects that request. Always add the full reply as the assistant turn first, then the results in the next user turn.

## Recap
Let's recap. First, a tool has a name, a description and an input schema, and the description tells the model when to use it. Second, when the stop reason is tool use, your code runs the function and returns a tool result with the matching ID. Third, the model only requests tools. Your code runs them, reads the input as a parsed object, and decides what is allowed.

## CTA
Now it is your turn. In the exercise, you will add a tool that looks up an order status in a local dictionary, and test it with five customer questions, including an unknown number and an unrelated question. In the next lesson, Tool Loops and Guardrails, you will make tools safe. See you there.

## Thumbnail
Headline: The Model Asks, You Run
Image: Navy background, a chat bubble passing a small request card to a code function box that returns a result, headline in teal Inter Bold.

## Production Notes
- [VERSION] Tool-definition options (strict mode, tool choice and other fields) and the exact response block format (tool_use, tool_result, tool_use_id) must be checked against the current tool-use docs before recording.
- The final answer about parcel VN-4471 is example output; the voiceover says 'something like'.
- Nguyen Thi Lan, the Ho Chi Minh City courier company and all tracking codes are invented; the shipment data is a local dictionary, not a real system.
