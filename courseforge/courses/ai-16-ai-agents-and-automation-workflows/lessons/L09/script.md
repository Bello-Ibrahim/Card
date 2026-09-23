# L09 Tool Use: Letting the Model Call Functions | Presenter Script

Course: AI-16 · Video: 5 min · Words: 704

## Hook
In lesson two, you saw that the model does not run tools itself. It only asks for them. Today, you see exactly how that request looks, and why the words in a tool description decide whether the agent picks the right action.

## Explain
With tool use, you send the model a list of tools, together with the messages. Each tool has three parts. A short, clear name. A description in plain language, saying what the tool does, when to use it, and when not to. And an input schema, which lists the inputs, their types, and which ones are required.

The model chooses tools mainly from the descriptions. So the description is really an instruction.

Here is the exchange. You send the messages and the tools. If the model wants a tool, its reply says it stopped for tool use, and names the tool and the input. Your code runs the tool, and sends back the result, marked with the same ID. Then the model continues. It may ask for another tool, or give a final answer.

On screen is the loop from lesson two, in real code with the official software kit. While the model keeps asking for tools, the code runs each one, and adds the results to the conversation. A reply can hold more than one tool request, so the code collects all of them.

Here is a picture. The model is a manager who cannot leave the office, but can ask an assistant to make phone calls. The manager writes a note: call the warehouse, and ask about item four four seven one.

The assistant, which is your code, makes the call, and reports back, quoting the note number. The manager can only ask for calls on the approved list. And the assistant can refuse a call that breaks the rules.

So, how do you write good tools? Give each tool one clear job. Say when not to use it. Use strict inputs. Return short, clear results, including errors the model can understand, like product not found. And keep reading separate from writing. Tools that create, send or delete need extra checks, and often a person's approval.

## Demonstrate
Let's look at one tool. Ayesha Siddiqui manages a pharmacy in Karachi, Pakistan. She sketches a stock-check agent.

Here is her check stock tool. The description says it returns the quantity in stock for one product ID. It says to use it after the find product tool has returned an ID. And it says, do not use it for prices. The only input is the product ID, and it is required.

A staff member asks: do we have enough of product P zero four one two for thirty packs? You'll see something like this. The model asks for check stock, with that product ID. Her code reads the sheet, and returns eighteen packs in stock.

The model answers: no, eighteen packs are in stock, twelve short. Do you want me to prepare a reorder request? And notice the limit. The reorder tool only creates a request in a sheet, for a pharmacist to approve. It never places an order with a supplier.

A common mistake is to write vague descriptions, such as stock tool, or gets data. The model then uses the wrong tool, invents inputs, or skips the tool and guesses. Write each description as if you were explaining the tool to a new colleague: what it does, what it needs, what it returns, and when not to use it.

## Recap
Let's recap. First, each tool has a name, a description and an input schema, and the model chooses mainly from the descriptions. Second, the loop continues while the model asks for tools. Your code runs each one, and returns the result with the matching ID. Third, give each tool one job, strict inputs and clear results, and keep tools that change data separate and controlled.

## CTA
Now it is your turn. In the exercise below this video, you will write three tool definitions for Ayesha's pharmacy agent: find a product, check the stock, and create a reorder request that a pharmacist must approve. It takes about twenty-five minutes. In the next lesson, we are Building an Agent in n8n. See you there.

## Thumbnail
Headline: Words That Choose Tools
Image: Navy background, a model icon passing a small note to a toolbox with three labelled drawers, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API tool use format: the tools fields (name, description, input_schema), stop_reason values (tool_use, end_turn), tool_use and tool_result blocks, the anthropic SDK call, and current model IDs for the MODEL placeholder must be checked against current documentation.
- This lesson is not a screen demo: code and JSON appear only on code-layout slides. The voiceover describes them and never reads field syntax, JSON or model IDs aloud.
- The tool_use request and the model's answer about P-0412 are example outputs; label them 'example output' on the slides.
- Ayesha Siddiqui and her Karachi pharmacy are fictional; product IDs and stock numbers are invented.
