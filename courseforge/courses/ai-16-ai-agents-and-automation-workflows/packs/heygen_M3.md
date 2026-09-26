# HeyGen Batch Pack: AI-16 M3 (Agents That Use Tools)

Course: AI Agents and Automation Workflows. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L09 Tool Use: Letting the Model Call Functions

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M3_L09_presenter.mp4`
- **Expected length:** about 5.0 minutes (702 words). The quality gate accepts ±10%.

```text
In lesson two, you saw that the model does not run tools itself. It only asks for them. Today, you see exactly how that request looks, and why the words in a tool description decide whether the agent picks the right action.

With tool use, you send the model a list of tools, together with the messages. Each tool has three parts. A short, clear name. A description in plain language, saying what the tool does, when to use it, and when not to. And an input schema, which lists the inputs, their types, and which ones are required.

The model chooses tools mainly from the descriptions. So the description is really an instruction.

Here is the exchange. You send the messages and the tools. If the model wants a tool, its reply says it stopped for tool use, and names the tool and the input. Your code runs the tool, and sends back the result, marked with the same ID. Then the model continues. It may ask for another tool, or give a final answer.

On screen is the loop from lesson two, in real code with the official software kit. While the model keeps asking for tools, the code runs each one, and adds the results to the conversation. A reply can hold more than one tool request, so the code collects all of them.

Here is a picture. The model is a manager who cannot leave the office, but can ask an assistant to make phone calls. The manager writes a note: call the warehouse, and ask about item four four seven one.

The assistant, which is your code, makes the call, and reports back, quoting the note number. The manager can only ask for calls on the approved list. And the assistant can refuse a call that breaks the rules.

So, how do you write good tools? Give each tool one clear job. Say when not to use it. Use strict inputs. Return short, clear results, including errors the model can understand, like product not found. And keep reading separate from writing. Tools that create, send or delete need extra checks, and often a person's approval.

Let's look at one tool. Ayesha Siddiqui manages a pharmacy in Karachi, Pakistan. She sketches a stock-check agent.

Here is her check stock tool. The description says it returns the quantity in stock for one product ID. It says to use it after the find product tool has returned an ID. And it says, do not use it for prices. The only input is the product ID, and it is required.

A staff member asks: do we have enough of product P zero four one two for thirty packs? You'll see something like this. The model asks for check stock, with that product ID. Her code reads the sheet, and returns eighteen packs in stock.

The model answers: no, eighteen packs are in stock, twelve short. Do you want me to prepare a reorder request? And notice the limit. The reorder tool only creates a request in a sheet, for a pharmacist to approve. It never places an order with a supplier.

A common mistake is to write vague descriptions, such as stock tool, or gets data. The model then uses the wrong tool, invents inputs, or skips the tool and guesses. Write each description as if you were explaining the tool to a new colleague: what it does, what it needs, what it returns, and when not to use it.

Let's recap. First, each tool has a name, a description and an input schema, and the model chooses mainly from the descriptions. Second, the loop continues while the model asks for tools. Your code runs each one, and returns the result with the matching ID. Third, give each tool one job, strict inputs and clear results, and keep tools that change data separate and controlled.

Now it is your turn. In the exercise below this video, you will write three tool definitions for Ayesha's pharmacy agent: find a product, check the stock, and create a reorder request that a pharmacist must approve. It takes about twenty-five minutes. In the next lesson, we are Building an Agent in n8n. See you there.
```

## L10 Building an Agent in n8n

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M3_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (680 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERSION] Current Claude model IDs for the MODEL placeholder. Select the model on screen but do not say its ID in the voiceover; blur the credential.

```text
In the last lesson, you saw the agent loop in code. n8n can run the same loop for you, and it shows every decision in the execution log. Today, you build an agent that looks things up and calculates, and you watch it choose its tools.

In n8n, the AI Agent node runs the agent loop. You connect other nodes to it. A chat model makes the decisions. We use the Anthropic chat model node, with your Claude API credential. Memory is optional, and comes in the next lesson. And tools are the nodes the agent may call, such as a Google Sheets tool, a calculator, or an HTTP request.

A chat trigger lets you talk to the agent in a chat panel inside the editor. In the agent node, you write a system message, with the goal, the rules and the limits. You can also set a maximum number of steps.

Each tool node has a description field. As in the last lesson, this text tells the model what the tool does, and when to use it. So write it carefully. n8n can also let the model fill some tool settings itself, such as the product name to search for.

Why a calculator? Language models can make mistakes with arithmetic. A calculator gives exact results, and the log shows the calculation, so you can check it.

Here is a picture. The agent node is like a project coordinator at a desk with a telephone. The chat model is the coordinator's judgement. The tools are the numbers on the speed-dial list. And the execution log is the call record.

One safety rule for this lesson. Give the agent read-only tools. A Sheets tool that only reads rows cannot damage your data. Tools that write or send come later, with approval steps.

Let's build it. Kofi Mensah owns a hardware shop in Accra, Ghana. His products sheet has an ID, a name, a unit price and a stock count, all invented. He creates a new workflow, adds a chat trigger, and connects an AI Agent node.

He connects an Anthropic chat model, picks his Claude credential, and chooses a model from the current list. Then he writes the system message. Answer stock and price questions for staff. Always look up products in the sheet. Always use the calculator for totals. If a product is not found, say so. Do not guess prices.

He connects a Google Sheets tool that only reads the products sheet, and gives it a clear description. Then he connects a calculator tool.

He opens the chat and asks: is the ten millimetre drill bit in stock, and what is the total for twelve units? In the log, you'll see something like this. The agent calls the Sheets tool, then the calculator, and then answers: yes, forty are in stock, and twelve units cost forty-five cedis.

Then he asks about a product that does not exist. The log shows one Sheets call, and the answer: I could not find that product. That is the correct behaviour. The agent did not invent a product or a price.

A common mistake is to connect many tools, just in case. The agent then has more choices, makes more wrong ones, and uses more tokens, because every tool description is sent with every request. Connect only what the task needs. If it picks the wrong tool, improve the descriptions first.

Let's recap. First, the AI Agent node runs the loop, with a chat model, optional memory and connected tools. Second, the tool descriptions and system message guide which tool it picks, and the log shows every choice. Third, start with a few read-only tools, and use a calculator for arithmetic.

Now it is your turn. In the exercise below this video, you will build a stock and price agent from your own products sheet. Test it with five questions, including a missing product and a spelling mistake, and note which tools it used each time. It takes about forty minutes. In the next lesson, we add Memory and Context. See you there.
```

## L11 Memory and Context

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M3_L11_presenter.mp4`
- **Expected length:** about 4.8 minutes (665 words). The quality gate accepts ±10%.

```text
Ask your agent, what does product P zero four one two cost? And then, how many are in stock? Without memory, the second question makes no sense to it. With too much memory, it becomes slow, expensive and confused. Today, you find the right amount.

Here is the key fact. A model has no memory between API calls. Each request must contain everything the model should know. So memory in an agent is simply the information your system chooses to send again. There are two kinds.

Short-term memory is the recent conversation. In n8n, you connect a memory node, such as Simple Memory, to the agent. Two settings matter. The session key says which conversation the memory belongs to. Each user needs their own key, or conversations will mix. And the window length says how many recent exchanges to keep. Older ones are dropped.

Longer-term context is information the agent looks up only when it needs it. For example, a customer's order history, a policy document, or notes from an earlier case. You give the agent a tool to fetch it. This is usually better than putting everything into memory.

More memory is not always better. Cost: every remembered message is sent again with each request. Confusion: long, mixed histories can lead the model to use old details. And privacy: anything stored may include personal data. Rules on this differ by country. So store only what the task needs, and use sample data in this course.

Picture a receptionist. Short-term memory is the notepad on the desk: the last few things the visitor said. Longer-term context is the filing cabinet. The receptionist opens the right file only when needed.

A receptionist who copies every old file onto the notepad cannot find anything. And a notepad left on the desk may be read by the wrong person.

Let's test it. Elena Popescu runs a travel agency in Bucharest, Romania. Her agent answers questions about invented tour packages from a sheet. It is built like the agent from the last lesson, with no memory yet.

She asks: what is the price of the Danube Delta tour? Then: is it available in May? You'll see something like: which tour do you mean? Without memory, the second question has lost its subject.

She connects a Simple Memory node, with the session key from the chat, and a window of two. Then she holds a six-turn conversation: the tour, the price, May, a group of eight, a second tour, and finally, so for the first tour, what is the total for my group?

At turn six, the agent asks which tour she means. The first tour and the group size have dropped out of the window.

She changes the window to six, and repeats. Now the answer is correct. But the execution log shows more input tokens on each later turn. So she settles on a window of four, and adds a rule to the system message: when a question refers to details you do not have, ask for them.

A common mistake is to think the agent remembers a customer because it answered well yesterday. In a new session, the details are gone. Another is to set a huge window and store full personal details, to be safe. Decide what the agent really needs, and fetch records with tools.

Let's recap. First, the model itself remembers nothing. Memory is the history your system sends again with each request. Second, keep a short window of recent messages, and fetch longer-term records with tools. Third, more memory costs more tokens, can confuse the model, and may store personal data, so keep only what the task needs.

Now it is your turn. In the exercise below this video, you will add memory to your agent, hold a six-turn conversation, and note where it forgets. Then change the window size, compare the tokens, and justify your choice. It takes about thirty minutes. In the next lesson, we add Human-in-the-Loop Approval. See you there.
```

## L12 Human-in-the-Loop Approval

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M3_L12_presenter.mp4`
- **Expected length:** about 5.0 minutes (698 words). The quality gate accepts ±10%.

```text
An agent that drafts a wrong reply costs you a minute. An agent that sends a wrong reply, issues the wrong refund, or deletes a customer record can cost you a customer. The difference is one step: a person saying yes before the action runs.

Last time, we gave the agent memory. Now we give it a safety step. Start by sorting the actions in your workflow into two groups. Reversible or internal actions, like reading data, drafting text, or calculating. The agent may do these alone. And irreversible or external actions, like sending a message, issuing a refund, or deleting records. These need a person's approval first.

And decisions about people, such as hiring, credit, insurance claims or closing an account, always keep a person in charge. The agent may collect information and suggest. A person decides, and is accountable.

There are two common ways to add approval in n8n. The first is to pause and wait. A Wait node stops the run until something happens, such as a form being submitted. Some email and chat nodes can also send an approve or decline message, and wait for a click. Always set a time limit. If nobody answers, nothing is sent, and the item goes to review.

The second way uses a sheet and two workflows. The first workflow writes each draft to an approvals tab, marked pending. A person changes it to approved or rejected. A second workflow runs on a schedule, finds approved rows that have not been sent yet, performs the action, and records the time it was sent. It is simple, and easy to audit.

What the approver sees matters. Show the original request, the draft, the reason, and the exact action that will run. An approver who only sees the word approve, with a question mark, will soon approve everything without reading.

Think of the two-signature rule for company payments. A clerk prepares the payment, but it only leaves the bank when a second person signs. The clerk does most of the work. The signature is the control.

Let's build it. Diego Ramírez runs customer service for an online clothing shop in Mexico City. His refund agent reads a request, checks the order sheet and the refund policy, and drafts a decision. It never refunds alone. The first workflow ends by adding each draft to an approvals tab, as pending.

He runs it with a sample request: my jacket arrived torn, I want my money back. In the new row, you'll see something like a draft reply, a refund amount, and the reason: damaged on arrival, within the return period.

The second workflow starts on a schedule, every few minutes. It reads rows that are approved and not yet sent. It sends the reply, for the course only to his own test address, and then writes the sent time.

He sets the row to approved, and waits for the schedule. The test email arrives, and the sent time is filled. Then he adds a second request, and rejects it. Nothing is sent. The refund itself stays manual. The agent saves time on reading and drafting. People keep control of money.

A common mistake is to let the sending workflow read all rows. Then the same email is sent twice, or a pending row goes out by mistake. Filter on approved and not yet sent, write the sent time straight after the action, and test the rejected and pending cases too.

Let's recap. First, irreversible or external actions, and all decisions about people, need a person's approval before they run. Second, in n8n, pause with a Wait node, or use a sheet with a status column and a second scheduled workflow. Third, show approvers the request, the draft and the reason, and make sure each approved action runs exactly once.

Now it is your turn. In the exercise below this video, your agent drafts customer replies into a sheet, and a second workflow sends a reply only after a person sets the row to approved. Test an approved, a rejected and a pending row. It takes about forty minutes. In the next lesson, we cover Error Handling, Retries and Logging. See you there.
```
