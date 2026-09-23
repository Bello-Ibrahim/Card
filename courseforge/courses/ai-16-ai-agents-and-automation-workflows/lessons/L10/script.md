# L10 Building an Agent in n8n | Presenter Script

Course: AI-16 · Video: 5 min · Words: 684

## Hook
In the last lesson, you saw the agent loop in code. n8n can run the same loop for you, and it shows every decision in the execution log. Today, you build an agent that looks things up and calculates, and you watch it choose its tools.

## Explain
In n8n, the AI Agent node runs the agent loop. You connect other nodes to it. A chat model makes the decisions. We use the Anthropic chat model node, with your Claude API credential. Memory is optional, and comes in the next lesson. And tools are the nodes the agent may call, such as a Google Sheets tool, a calculator, or an HTTP request.

A chat trigger lets you talk to the agent in a chat panel inside the editor. In the agent node, you write a system message, with the goal, the rules and the limits. You can also set a maximum number of steps.

Each tool node has a description field. As in the last lesson, this text tells the model what the tool does, and when to use it. So write it carefully. n8n can also let the model fill some tool settings itself, such as the product name to search for.

Why a calculator? Language models can make mistakes with arithmetic. A calculator gives exact results, and the log shows the calculation, so you can check it.

Here is a picture. The agent node is like a project coordinator at a desk with a telephone. The chat model is the coordinator's judgement. The tools are the numbers on the speed-dial list. And the execution log is the call record.

One safety rule for this lesson. Give the agent read-only tools. A Sheets tool that only reads rows cannot damage your data. Tools that write or send come later, with approval steps.

## Demonstrate
Let's build it. Kofi Mensah owns a hardware shop in Accra, Ghana. His products sheet has an ID, a name, a unit price and a stock count, all invented. He creates a new workflow, adds a chat trigger, and connects an AI Agent node.

He connects an Anthropic chat model, picks his Claude credential, and chooses a model from the current list. Then he writes the system message. Answer stock and price questions for staff. Always look up products in the sheet. Always use the calculator for totals. If a product is not found, say so. Do not guess prices.

He connects a Google Sheets tool that only reads the products sheet, and gives it a clear description. Then he connects a calculator tool.

He opens the chat and asks: is the ten millimetre drill bit in stock, and what is the total for twelve units? In the log, you'll see something like this. The agent calls the Sheets tool, then the calculator, and then answers: yes, forty are in stock, and twelve units cost forty-five cedis.

Then he asks about a product that does not exist. The log shows one Sheets call, and the answer: I could not find that product. That is the correct behaviour. The agent did not invent a product or a price.

A common mistake is to connect many tools, just in case. The agent then has more choices, makes more wrong ones, and uses more tokens, because every tool description is sent with every request. Connect only what the task needs. If it picks the wrong tool, improve the descriptions first.

## Recap
Let's recap. First, the AI Agent node runs the loop, with a chat model, optional memory and connected tools. Second, the tool descriptions and system message guide which tool it picks, and the log shows every choice. Third, start with a few read-only tools, and use a calculator for arithmetic.

## CTA
Now it is your turn. In the exercise below this video, you will build a stock and price agent from your own products sheet. Test it with five questions, including a missing product and a spelling mistake, and note which tools it used each time. It takes about forty minutes. In the next lesson, we add Memory and Context. See you there.

## Thumbnail
Headline: Watch Your Agent Choose
Image: Navy background, an AI Agent node in the centre with three teal sub-nodes (chat model, sheet, calculator) attached below it, headline in teal Inter Bold.

## Production Notes
- [VERSION] n8n AI Agent node, Anthropic Chat Model node, Chat Trigger, Google Sheets tool, Calculator tool, HTTP Request tool, max iterations setting and model-filled tool parameters must be checked against the current release; agent node options change often.
- [VERSION] Current Claude model IDs for the MODEL placeholder. Select the model on screen but do not say its ID in the voiceover; blur the credential.
- The agent's answers (40 in stock, 45.00 cedis for 12 units) and the log entries are example outputs; real runs will differ slightly.
- Kofi Mensah and his Accra hardware shop are fictional; the products sheet is invented.
