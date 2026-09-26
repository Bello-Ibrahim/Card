# Screen Demo Pack: AI-15 L08 Query Rewriting and Conversational Retrieval

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L08_screen_1.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open the chat notebook with the pipeline from earlier lessons.
2. Ask 'What is the travel allowance for Astana?' and show the answer with a citation to the travel policy chunk.

**Narration over this clip (for pacing)**

> Let's follow Aigerim. She builds an HR policy assistant for a logistics company in Almaty, Kazakhstan. Policies are in Russian and English. First question: what is the travel allowance for Astana? Retrieval works, and the answer cites the travel policy.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L08_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Ask 'And for drivers?' with no rewriting.
2. Print the top 5 retrieved chunks and highlight the vehicle maintenance titles.

**Narration over this clip (for pacing)**

> Second question: and for drivers? Without rewriting, the top chunks are about vehicle maintenance for drivers. The answer is wrong, and it is easy to see why when we print the retrieved chunks. The search engine saw only the word drivers, so it found drivers, but the wrong topic.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L08_screen_3.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show the rewrite function: history[-6:], output_config with REWRITE_SCHEMA, json.loads of the text block.
2. Run rewrite(history, 'And for drivers?') and show the JSON from the real run.

**Narration over this clip (for pacing)**

> Now she adds the rewrite function. It sends the last six messages and the new question, with the schema, and reads back the JSON. You'll see something like a standalone query about the travel allowance for drivers going to Astana, plus a short variant about a driver's daily allowance.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L08_screen_4.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Retrieve with the standalone query and each variant, then fuse the lists with rrf.
2. Show the drivers' section of the travel policy as the top chunk.
3. Show the debug panel line 'Searched for: …' under the answer.

**Narration over this clip (for pacing)**

> She searches with all three queries, fuses them, and the drivers' section of the travel policy is now the top chunk. She also shows the rewritten query in a debug panel, so testers can see exactly what was searched. That makes problems much easier to find later.

## Clip 5: scene 11

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L08_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run rewrite on a complete first question and compare it with the original.
2. Show the answer call using the original question, not the rewritten one.

**Narration over this clip (for pacing)**

> Two rules keep this safe. First, a complete question should come back almost unchanged, so she tests one, and gets only small word changes. Second, the rewrite is for search only. The final answer step still receives the user's original words.

## Production notes for this lesson

- [VERSION] Claude API structured outputs (output_config with a JSON Schema; a forced tool_choice is rejected by some current models), the response content block format, and model choice (MODEL read from the environment; check the current models page). Never say a model ID or price.
- The rewrite output on screen comes from a real API run; the voiceover says 'you'll see something like' and the wording will differ from content.md.
- Aigerim and the Almaty logistics company are hypothetical; HR policies and conversations are invented, with no personal data.
- Russian-language policy text, if shown on screen, should be checked by a Russian speaker before release.
