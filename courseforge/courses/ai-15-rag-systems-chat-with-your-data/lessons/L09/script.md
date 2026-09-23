# L09 Grounded Answers with Citations | Presenter Script

Course: AI-15 · Video: 5 min · Words: 691

## Hook
Your assistant says tenants must give sixty days' notice. Is that from the guide you indexed, or a rule the model remembered from another country? Without a citation, the user cannot tell. Without a clear I don't know, they cannot tell when to stop trusting it.

## Explain
Welcome to week three. We start with the heart of RAG: grounded answers that show their sources. In lesson three, our first prompt was only one line. Today we make it strict, and we check the result in code.

A grounded answer uses only the retrieved context, and every claim can be traced to a chunk. Three instructions make this work. Answer only from the context. Cite the chunk ID after each claim. And when the context does not contain the answer, say I don't know, and do not guess.

Give the model the chunks in a clear format. Each chunk sits inside tags, with its ID and its source title and page in the header. The tags also tell the model that the chunk text is material to read, not instructions to follow. We return to that in lesson thirteen.

For an application, JSON is better than brackets in free text. So we ask for a structured output with three fields: the answer, a list of cited IDs, and a found flag. There is also another route. The Claude API has a citations feature that points to the exact passage used. Check the current documentation, because it may not combine with structured outputs in one request.

Think of a good student essay with footnotes. Every important claim points to a page in the course reader. And if the reader does not cover a topic, the student says so, instead of inventing a source. That honesty is what makes the essay trustworthy.

## Demonstrate
Let's follow Priya. She builds a question-answering tool for a legal aid clinic in Pune, India. Volunteers answer tenants' questions from a public guide to rental rules. Rules differ by place, so the guide is the only source the tool may use. First, she replaces her old one-line prompt with the strict system prompt and the context formatter.

Next, she adds the structured output with answer, citations and found, and a small check in code. It fails if any cited ID was not retrieved, or if the answer says found but cites nothing. On the example, the check passes and prints True.

She asks: how much deposit can a landlord ask for? You'll see something like an answer that cites two chunks, and the check passes. She opens both chunks and confirms the numbers. In the interface, each citation shows the document title and page, with a link.

Now three questions the guide does not cover: rules in another country, a tax question, and a question about a named landlord. At first, the tax question gets a general answer with no citations. After she adds the word exactly to the prompt, and the found check in code, all three return found false and the exact I don't know sentence.

A common mistake is to ask for citations but never check them. Models can cite an ID that was not in the context. Validate IDs in code, and sample answers by hand. The check does not prove support. That is faithfulness, which we measure in lesson twelve. And never hide I don't know as an error.

## Recap
Let's recap. First, tell the model to answer only from the numbered chunks, cite chunk IDs, and say I don't know when the context does not contain the answer. Second, return the answer, citations and a found flag as structured output, and check in code that every cited ID was retrieved. Third, the API's citations feature can point to exact passages, so check how it fits your request.

## CTA
Now it is your turn. In the exercise below, change your pipeline so every answer lists its sources, and test it with three questions your documents cannot answer. Treat a clear I don't know as a success. In the next lesson, Building a RAG Test Set, we create the questions that tell us whether all this really works.

## Thumbnail
Headline: Cite It or Say No
Image: Navy background, an answer card with teal citation tags [c14] [c22] next to a second card reading 'I don't know', headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API document citations feature (document content blocks, citation response format), structured outputs and forced tool use, and whether citations and structured outputs can be used in the same request. The voiceover only says to check the current documentation.
- Content check: content.md says 'use a forced tool call, as in L08', but L08 uses a JSON Schema in output_config and warns that some current models reject a forced tool_choice. The voiceover says 'structured output, as in the last lesson'. Record the demo with the same method as L08, and ask the content owner to align the L09 text. [VERSION]
- [REGION] Rental rules differ by state and country; the example uses a hypothetical guide and names no law. Do not show a real legal text on screen.
- check_citations is tested plain Python: its example call must print exactly True.
- API answers in the demo are from a real run; the voiceover says 'you'll see something like'. The 'I don't know' sentence must match the SYSTEM prompt exactly.
- Priya and the Pune legal aid clinic are hypothetical; questions about a named landlord use an invented name.
