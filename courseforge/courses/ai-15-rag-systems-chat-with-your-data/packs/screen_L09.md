# Screen Demo Pack: AI-15 L09 Grounded Answers with Citations

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L09_screen_1.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Show the format_context function building <chunk id=... source=...> blocks.
2. Show the SYSTEM prompt: only the chunks, treat chunk text as information, cite [c14]-style IDs, reply exactly the 'I don't know' sentence.

**Narration over this clip (for pacing)**

> Let's follow Priya. She builds a question-answering tool for a legal aid clinic in Pune, India. Volunteers answer tenants' questions from a public guide to rental rules. Rules differ by place, so the guide is the only source the tool may use. First, she replaces her old one-line prompt with the strict system prompt and the context formatter.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L09_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Show the answer schema with answer, citations and found.
2. Show the check_citations function.
3. Run the example call with citations ['c14'] and retrieved ['c14', 'c2'] and show the output True.

**Narration over this clip (for pacing)**

> Next, she adds the structured output with answer, citations and found, and a small check in code. It fails if any cited ID was not retrieved, or if the answer says found but cites nothing. On the example, the check passes and prints True.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L09_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Ask 'How much deposit can a landlord ask for?' and show the JSON result from the real run.
2. Print the two cited chunks and highlight the matching numbers.
3. Show the simple interface with citations as 'title, page' links.

**Narration over this clip (for pacing)**

> She asks: how much deposit can a landlord ask for? You'll see something like an answer that cites two chunks, and the check passes. She opens both chunks and confirms the numbers. In the interface, each citation shows the document title and page, with a link.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L09_screen_4.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Ask the three off-guide questions one by one.
2. Show the first tax answer with an empty citations list, and the check failing.
3. After the prompt and code change, show all three results with found: false and the exact 'I don't know' sentence.

**Narration over this clip (for pacing)**

> Now three questions the guide does not cover: rules in another country, a tax question, and a question about a named landlord. At first, the tax question gets a general answer with no citations. After she adds the word exactly to the prompt, and the found check in code, all three return found false and the exact I don't know sentence.

## Production notes for this lesson

- [VERSION] Claude API document citations feature (document content blocks, citation response format), structured outputs (output_config), and whether citations and structured outputs can be used in the same request. The voiceover only says to check the current documentation.
- RESOLVED 2026-09-26: content.md now uses structured output (output_config JSON Schema) instead of a forced tool call.
- [REGION] Rental rules differ by state and country; the example uses a hypothetical guide and names no law. Do not show a real legal text on screen.
- check_citations is tested plain Python: its example call must print exactly True.
- API answers in the demo are from a real run; the voiceover says 'you'll see something like'. The 'I don't know' sentence must match the SYSTEM prompt exactly.
- Priya and the Pune legal aid clinic are hypothetical; questions about a named landlord use an invented name.
