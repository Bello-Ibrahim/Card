# Screen Demo Pack: AI-15 L03 Your First RAG Pipeline

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L03_screen_1.mp4`
- **Target length:** about 25 seconds

**Steps**

1. In the terminal, set ANTHROPIC_API_KEY (masked) and CLAUDE_MODEL.
2. Show report.txt open briefly in the editor: a long plain-text report.

**Narration over this clip (for pacing)**

> Let's follow Lucía, a data analyst at an energy research institute in Santiago, Chile. She has a public sixty-page report on renewable energy policy, saved as plain text. First she sets two environment variables in the terminal: her API key, and the model to use. The API is paid, so she picks a smaller model for development.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L03_screen_2.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Scroll through the script: imports, MODEL read from the environment, the chunk function with size 800 and overlap 100.
2. Highlight chromadb.PersistentClient(path='./rag_db'), the SentenceTransformerEmbeddingFunction and get_or_create_collection('report').
3. Highlight col.add with ids c0, c1, … and metadatas source report.txt.

**Narration over this clip (for pacing)**

> Here is the script. The chunk function cuts the text into pieces with overlap. A persistent Chroma client saves the index to disk, and each chunk gets an ID like c zero, c one, and so on, plus a source in its metadata. One tip. If you run the add step again with the same IDs, delete the folder first, or use upsert instead.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L03_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Highlight the ask function: col.query with n_results=k, the context built as [id] text, client.messages.create with system=SYSTEM.
2. Point to the return value: the answer text and res['ids'][0].

**Narration over this clip (for pacing)**

> The ask function queries Chroma for the top four chunks, joins them with their IDs in square brackets, and sends them to Claude with the strict system prompt. It returns both the answer and the retrieved IDs, so we can always check them.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L03_screen_4.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Run the script to build the index, then run col.count() and show the number.
2. Call ask('What target does the report set for solar capacity?').
3. Print the answer and the retrieved IDs side by side (real run output).

**Narration over this clip (for pacing)**

> She runs the script once to build the index, and checks the chunk count. Then she asks: what target does the report set for solar capacity? You'll see something like this. An answer that states the target and cites two chunk IDs, with the four retrieved IDs printed next to it.

## Clip 5: scene 11

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L03_screen_5.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Print the documents for the two cited chunk IDs and highlight the matching sentences.
2. Ask an off-topic question and show the reply 'I don't know.'
3. Ask a table question, show the incomplete answer, then print the retrieved chunk that ends mid-table.

**Narration over this clip (for pacing)**

> Lucía opens the two cited chunks and confirms the claims. Then she asks about a topic the report does not cover, and gets, I don't know. That is the right answer. A question whose answer sits in a table gets an incomplete answer, because a fixed-size chunk cut the table in half. She notes this for lesson five.

## Production notes for this lesson

- [VERSION] Claude API model: read from the CLAUDE_MODEL environment variable, set after checking the current models page at recording time. Never show or say a model ID or price in the voiceover; blur the terminal line if a model ID is visible.
- [VERIFY] Realistic cost per learner, as the Claude API is paid. The voiceover only says 'paid' and 'keep runs short'.
- [VERSION] Chroma client API (PersistentClient, get_or_create_collection, add, upsert, query result format, SentenceTransformerEmbeddingFunction); it changed between major versions.
- [VERSION] Embedding model name; [VERIFY] its licence and the licence of the example report used on screen.
- Hide the API key: set ANTHROPIC_API_KEY off camera or mask it in the edit.
- The example answer and retrieved IDs (c41, c42, c7, c88) are illustrative. Record a real run; the voiceover says 'you'll see something like' and the IDs on screen come from the real run.
- Lucía and the Santiago energy research institute are hypothetical; the report must be a real public report whose licence allows reuse.
