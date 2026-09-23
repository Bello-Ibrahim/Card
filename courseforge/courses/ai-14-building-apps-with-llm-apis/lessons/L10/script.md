# L10 Tool Loops and Guardrails | Presenter Script

Course: AI-14 · Video: 5 min · Words: 690

## Hook
A tool that reads data can give a wrong answer. A tool that changes data can send a parcel to the wrong city. Once your model can call functions that act in the real world, your code must set the limits, because the model will not.

## Explain
The loop from the last lesson works for one read-only tool. Real apps need five guardrails. First, handle several tool calls in one turn. One reply can ask for more than one tool, for example two tracking codes in one question. Run each one, and return all the results together in a single user message.

Second, cap the number of steps. A loop that runs while the model asks for tools could, in rare cases, keep going and spend money. Set a maximum, such as five steps, and stop with a clear message when it is reached.

Third, check tool inputs strictly. The input is already parsed, but treat it like any user input, and validate types, formats and allowed values in your code. If an input fails, return an error result with a short message, so the model can correct itself. Do the same for an unknown tool name.

Fourth, ask a human before any action that changes data. Reading a status is safe. Changing an address or cancelling an order is not. Your code, not the model, shows the planned action and waits for a clear yes. Fifth, give each tool the smallest permissions it needs. Never give the model a general tool that can run any database query or call any web address.

Think of a new bank clerk. They can look up balances freely, but every transfer needs a second signature and has a daily limit. The rules exist because mistakes that move money are expensive and hard to undo. Longer multi-step agents are covered in course AI sixteen.

## Demonstrate
Carlos Mendoza runs support for an online furniture shop in Medellín, Colombia. Next to the status tool, he adds a second tool that changes a delivery address.

Here is the core of his loop. It runs for at most five steps. For each tool request, it first checks that the tool exists. If it is a tool that writes data, it asks the customer to confirm. Only then does it run the handler. Every result carries an error flag, and if the loop reaches the limit, it stops and says a person will follow up.

Each handler validates its input first. The address handler checks that the order belongs to the customer who is logged in, that it has not shipped yet, and that the address is not empty. It changes only the address field, through the shop's normal business rules.

Now he tests it. He writes, send my order to my office instead. His code shows the planned change and asks yes or no. He answers no. You'll see something like, no problem, I have not changed the address.

Then he asks about four orders at once. The loop returns four results in one message. Finally, he sets the step limit to one, and checks that the stop message appears.

A common mistake is to put the safety rule only in the system prompt. A prompt is a request, not a control. A confusing message or an injected instruction can make the model skip it. Put confirmations, permission checks and step limits in your code.

## Recap
Let's recap. First, return all tool results from one turn in a single user message, and cap the loop at a fixed number of steps. Second, validate every tool input in your code, and return an error result for invalid inputs or unknown tools. Third, require human confirmation in code before any action that changes data, and give each tool the smallest permissions it needs.

## CTA
Now it is your turn. In the exercise, you will add a tool that changes a delivery address, require confirmation before it runs, and cap your loop at five steps. Then test a refusal and an invalid order number. In the next lesson, Security: Prompt Injection and Data Privacy, you will attack your own app. See you there.

## Thumbnail
Headline: Your Code Sets Limits
Image: Navy background, a looping arrow with a counter capped at five and a yes/no confirmation button, headline in teal Inter Bold.

## Production Notes
- [VERSION] Strict tool schema checking, the is_error field on tool results and parallel tool-call behaviour must be checked against the current tool-use docs before recording.
- The model reply 'No problem, I have not changed the address.' is example output; the voiceover says 'something like'.
- Scope note: multi-step agents and approval workflows are covered in AI-16; the voiceover mentions this once.
- Carlos Mendoza, the Medellín furniture shop, order numbers and the address are invented; the data is a local dictionary.
