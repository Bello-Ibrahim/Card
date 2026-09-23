# L03 Your First RAG Pipeline | Presenter Script

Course: AI-15 · Video: 5 min · Words: 699

## Hook
You know the six stages of RAG, and you know how embeddings work. Now we connect them. In about forty lines of Python, you will ask a question about a real report and get an answer that cites its sources.

## Explain
The goal today is a pipeline that works from end to end, not a perfect one. Each later lesson improves one stage.

There are four steps. First, load one text file and cut it into fixed-size pieces with a small overlap. Second, store the chunks in a local Chroma collection, which calls a sentence-transformers model to embed them for us. Third, send the question to Chroma and get the closest chunks with their IDs. Fourth, send the numbered chunks and the question to the Claude API.

The system prompt is short and strict. Answer only from the context chunks. Cite the chunk IDs. And if the context does not contain the answer, say I don't know. These three rules turn a chatbot into a grounded assistant.

You set up the Anthropic software kit and your API key in the previous course. Remember that the Claude API is paid. So use a smaller model while you develop, keep runs short, and read the model name from an environment variable, instead of writing it into your code.

Think of this first pipeline as a bicycle built from basic parts. It has wheels, brakes and pedals, and it moves. It is not fast or comfortable yet, but you can ride it, and you can see which part to upgrade next.

## Demonstrate
Let's follow Lucía, a data analyst at an energy research institute in Santiago, Chile. She has a public sixty-page report on renewable energy policy, saved as plain text. First she sets two environment variables in the terminal: her API key, and the model to use. The API is paid, so she picks a smaller model for development.

Here is the script. The chunk function cuts the text into pieces with overlap. A persistent Chroma client saves the index to disk, and each chunk gets an ID like c zero, c one, and so on, plus a source in its metadata. One tip. If you run the add step again with the same IDs, delete the folder first, or use upsert instead.

The ask function queries Chroma for the top four chunks, joins them with their IDs in square brackets, and sends them to Claude with the strict system prompt. It returns both the answer and the retrieved IDs, so we can always check them.

She runs the script once to build the index, and checks the chunk count. Then she asks: what target does the report set for solar capacity? You'll see something like this. An answer that states the target and cites two chunk IDs, with the four retrieved IDs printed next to it.

Lucía opens the two cited chunks and confirms the claims. Then she asks about a topic the report does not cover, and gets, I don't know. That is the right answer. A question whose answer sits in a table gets an incomplete answer, because a fixed-size chunk cut the table in half. She notes this for lesson five.

A common mistake is to change the prompt every time an answer is wrong. Often the right chunk was never retrieved. Always print the retrieved IDs and open them. Not there? Fix retrieval. There, but still wrong? Fix generation.

## Recap
Let's recap. First, a minimal RAG pipeline chunks, embeds and stores text in Chroma, retrieves the top chunks, and sends them with the question to the Claude API. Second, keep chunk IDs with the text so the model can cite them, and tell it to say I don't know. Third, when an answer is wrong, check retrieval before you change the prompt.

## CTA
Now build your own. In the exercise below, run the pipeline over one public report and ask it five questions, including one it cannot answer. For each one, record the answer, the retrieved IDs, and whether it was a retrieval or a generation problem. In the next lesson, Loading and Preparing a Document Collection, we move from one clean file to a real collection.

## Thumbnail
Headline: Your First Cited Answer
Image: Navy background, a code editor window on the left and a chat answer with teal citation tags [c41] [c42] on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API model: read from the CLAUDE_MODEL environment variable, set after checking the current models page at recording time. Never show or say a model ID or price in the voiceover; blur the terminal line if a model ID is visible.
- [VERIFY] Realistic cost per learner, as the Claude API is paid. The voiceover only says 'paid' and 'keep runs short'.
- [VERSION] Chroma client API (PersistentClient, get_or_create_collection, add, upsert, query result format, SentenceTransformerEmbeddingFunction); it changed between major versions.
- [VERSION] Embedding model name; [VERIFY] its licence and the licence of the example report used on screen.
- Hide the API key: set ANTHROPIC_API_KEY off camera or mask it in the edit.
- The example answer and retrieved IDs (c41, c42, c7, c88) are illustrative. Record a real run; the voiceover says 'you'll see something like' and the IDs on screen come from the real run.
- Lucía and the Santiago energy research institute are hypothetical; the report must be a real public report whose licence allows reuse.
