# Screen Demo Pack: AI-16 L10 Building an Agent in n8n

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L10_screen_1.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Show the 'products' sheet: product_id, name, unit_price, in_stock (invented)
2. Create a new workflow
3. Add a Chat Trigger
4. Add an AI Agent node and connect the trigger to it

**Narration over this clip (for pacing)**

> Let's build it. Kofi Mensah owns a hardware shop in Accra, Ghana. His products sheet has an ID, a name, a unit price and a stock count, all invented. He creates a new workflow, adds a chat trigger, and connects an AI Agent node.

## Clip 2: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L10_screen_2.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Connect an Anthropic Chat Model sub-node
2. Select the Claude credential (blurred) and a MODEL from the current models page
3. Open the AI Agent node and type the system message from content.md

**Narration over this clip (for pacing)**

> He connects an Anthropic chat model, picks his Claude credential, and chooses a model from the current list. Then he writes the system message. Answer stock and price questions for staff. Always look up products in the sheet. Always use the calculator for totals. If a product is not found, say so. Do not guess prices.

## Clip 3: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L10_screen_3.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Connect a Google Sheets tool: read rows from 'products'
2. Fill the tool description: 'Returns all products with ID, name, unit price and quantity in stock. Use it to find a product and its price.'
3. Connect a Calculator tool

**Narration over this clip (for pacing)**

> He connects a Google Sheets tool that only reads the products sheet, and gives it a clear description. Then he connects a calculator tool.

## Clip 4: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L10_screen_4.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Open the chat panel
2. Type: 'Is the 10 mm drill bit in stock, and what is the total for 12 units?'
3. Open the execution log: Sheets tool call → Calculator with 12 * 3.75 → final answer (example output)

**Narration over this clip (for pacing)**

> He opens the chat and asks: is the ten millimetre drill bit in stock, and what is the total for twelve units? In the log, you'll see something like this. The agent calls the Sheets tool, then the calculator, and then answers: yes, forty are in stock, and twelve units cost forty-five cedis.

## Clip 5: scene 12

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L10_screen_5.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Type a question about a product that is not in the sheet
2. Open the log: one Sheets tool call
3. Show the answer 'I could not find that product.' (example output)

**Narration over this clip (for pacing)**

> Then he asks about a product that does not exist. The log shows one Sheets call, and the answer: I could not find that product. That is the correct behaviour. The agent did not invent a product or a price.

## Production notes for this lesson

- [VERSION] n8n AI Agent node, Anthropic Chat Model node, Chat Trigger, Google Sheets tool, Calculator tool, HTTP Request tool, max iterations setting and model-filled tool parameters must be checked against the current release; agent node options change often.
- [VERSION] Current Claude model IDs for the MODEL placeholder. Select the model on screen but do not say its ID in the voiceover; blur the credential.
- The agent's answers (40 in stock, 45.00 cedis for 12 units) and the log entries are example outputs; real runs will differ slightly.
- Kofi Mensah and his Accra hardware shop are fictional; the products sheet is invented.
