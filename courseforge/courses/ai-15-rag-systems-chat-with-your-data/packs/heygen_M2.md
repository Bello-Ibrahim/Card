# HeyGen Batch Pack: AI-15 M2 (Chunking, Indexing and Retrieval)

Course: RAG Systems: Chat with Your Data. Make one HeyGen video per lesson below, using these settings for every video.

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

## L05 Chunking Strategies

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M2_L05_presenter.mp4`
- **Expected length:** about 5.0 minutes (687 words). The quality gate accepts ±10%.

```text
In lesson three, one answer failed because a chunk cut a table in half. Chunking looks like a small detail, but it decides what retrieval can find. Too small, and a chunk loses its meaning. Too large, and the answer hides among other topics.

Welcome to week two. We start with chunking. A chunk is the unit you embed, retrieve and cite, so its size and shape matter at every later stage.

There are three common strategies. Fixed-size chunks cut every so many characters, with a small overlap. They are simple, but they can cut sentences and tables. Sentence-based chunks collect whole sentences up to a size limit. Structure-based chunks split by headings, so each chunk stays inside one topic. Short, factual FAQs often work well with small chunks. Long technical explanations often need larger ones.

One simple improvement helps all three. Add the document and section title to each chunk. A chunk that says only, the limit is thirty days, becomes, refund policy, online orders, the limit is thirty days. Now a question about refunds can find it.

Think of cutting a book into index cards for a study group. If each card holds half a sentence, nobody understands it. If each card holds a whole chapter, you cannot find the fact you need. Good cards hold one idea each, with the chapter title written at the top.

Here is a sentence-based chunker in plain Python. It splits the text into sentences, collects them until the next one would pass the size limit, and then starts a new chunk. It carries the last sentence into the next chunk as overlap, and puts the title at the front.

We run it on four short sentences about orders, returns and refunds, with the title Returns, Online, and a limit of sixty characters. We get three chunks. Each starts with the title, and each shares one sentence with its neighbour. So a fact near a boundary appears in two chunks, and is less likely to be lost.

But which size is best? There is no answer for every collection, so measure, do not guess. The simplest measure is hit at five: for each question, is a correct chunk in the top five results? In this tiny test, one of two questions finds its chunk, so the score is zero point five.

Now a real comparison. Mei-Lin maintains technical manuals for an equipment maker in Hsinchu, Taiwan. Engineers ask things like, what torque does the M4 bolt on the cooling plate need? She builds three Chroma collections, with chunks of three hundred, eight hundred and fifteen hundred characters, each with overlap and the section title.

Chunk IDs change when the size changes, so she labels each expected answer by document and a short phrase instead. Then, for ten test questions, she checks the top five chunks in each collection.

Here are her example results. The small chunks find six of ten, because they lost the name of the part, which was in the previous sentence. The large chunks find seven of ten, because they mixed several procedures. The middle size finds nine of ten. She chooses eight hundred, and writes down why, with the numbers.

A common mistake is to copy a chunk size from a tutorial and never test it. A size that works for news may fail for contracts. And measure retrieval directly, because a good prompt cannot fix a missing chunk.

Let's recap. First, fixed-size, sentence-based and structure-based chunking each have trade-offs, and overlap protects facts near chunk boundaries. Second, adding the document and section title gives short chunks the context they need to be found. Third, choose chunk size by measuring a retrieval metric, such as hit at five, on your own test questions.

Now it is your turn. In the exercise below, index your collection with three chunk sizes, and check ten test questions against each one. Make a small table of size, number of chunks and hit at five, and choose a size based on your numbers. In the next lesson, Vector Databases: Chroma and pgvector, we look closely at where these chunks live.
```

## L06 Vector Databases: Chroma and pgvector

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M2_L06_presenter.mp4`
- **Expected length:** about 5.0 minutes (691 words). The quality gate accepts ±10%.

```text
A user asks what the twenty twenty-three reports said about water prices. Your index returns a perfect passage from a twenty fifteen report. The meaning matches, but the year does not. Today we fix that by combining meaning with simple rules.

In the last lesson, we cut our records into chunks. Now we look at where they live: the vector database.

A vector database stores vectors with their text and metadata, and answers one question: which stored vectors are closest to this one? Four ideas matter. A collection is a named group of chunks that share one embedding model. Each item you add has an ID, the text, a vector and metadata. Similarity search returns the nearest items. And metadata filters limit the search, for example by year.

Think of a large music shop where records are shelved by sound, not by artist name. Similar sounds sit together, so you walk to the right shelf quickly. Metadata filters are the signs on each aisle, like released after twenty twenty, that stop you from searching shelves you do not need.

Chroma is our default. It is free, open source, and runs inside your Python program with a local folder for storage. pgvector is an extension for PostgreSQL. Choose it when your data and user permissions already live there, because you can join chunks with other tables using normal SQL.

Comparing a question with every stored vector is exact, but slow for millions of chunks. Approximate nearest-neighbour indexes, such as HNSW, a layered graph of neighbours, check only a small part of the data. They are much faster, and usually return almost the same results. But combined with filters, they can sometimes return fewer results than you asked for.

Let's compare them. Oluwaseun is a backend developer at a payments start-up in Lagos, Nigeria. Support staff ask about internal policies, and the company already runs PostgreSQL. His team lead asks: Chroma or pgvector? First, he loads twelve hundred chunks into a Chroma collection, with year and document type as metadata.

He searches for chargeback time limit, with no filter. You'll see something like this: a list of chunk IDs, titles, years and distances, where a smaller distance means a closer match. But the top result is from a twenty nineteen policy that was replaced.

Now he adds a filter: year greater than or equal to twenty twenty-four. The current policy comes first. One detail matters here. Store numbers like the year as integers, not text, or range filters will not work as expected.

Next, pgvector. In a local Docker container, he enables the extension, and creates a chunks table with a vector column that matches his model's vector size. He adds an HNSW index for cosine distance. With pgvector, he computes the question's vector himself in Python, and passes it to the query.

He runs the same search, ordered by cosine distance, with the same year filter in a normal where clause. Both databases return the same top three chunks. So the choice is not about search quality here. It is about where your data already lives.

His decision: Chroma for fast local development and teaching. pgvector for production, because permissions, audit logs and document tables already live in PostgreSQL, and one database is easier to back up.

A common mistake is to store all metadata as text, or to forget it. Then you cannot filter, and you must rebuild the index. Decide your fields before ingestion, and keep one embedding model per collection.

Let's recap. First, a vector database stores vectors, text and metadata, and returns the nearest chunks, optionally limited by filters. Second, Chroma is the free, local default, and pgvector suits teams whose data already lives in PostgreSQL. Third, approximate indexes like HNSW trade a little accuracy for a lot of speed, so test your filters with them.

Now it is your turn. In the exercise below, store your chunks with typed metadata, write five questions where the year or document type matters, and compare results with and without a filter. In the next lesson, Hybrid Search and Reranking, we find the exact names and codes that embeddings can miss.
```

## L07 Hybrid Search and Reranking

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M2_L07_presenter.mp4`
- **Expected length:** about 4.9 minutes (681 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERSION] rank_bm25 (BM25Okapi, get_scores), the sentence-transformers CrossEncoder API, full-text search options in Chroma and PostgreSQL, and current reranker model names. Do not say a reranker model name in the voiceover.

```text
A technician types: error E 4107 on pump PX 220. Your vector search returns general passages about pump errors, but not the one page that lists that exact code. Embeddings are good at meaning, and weaker at exact strings. Let's add the missing piece.

In the last lesson, we stored chunks in a vector database. Today we add keyword search, and then a second opinion called reranking.

Keyword search ranks chunks by the words they share with the question. The standard method is called BM25. It gives a high score when a rare word, like a product code, appears in a chunk. It is fast, needs no model, and is very good at names, codes and numbers. But it does not understand synonyms or other languages.

Hybrid search runs both and combines the two ranked lists. The scores are on different scales, so we do not add them. Reciprocal rank fusion uses only the positions. Each chunk gets one divided by sixty plus its rank from each list, and the totals are summed.

Then comes reranking. A cross-encoder reads the question and one chunk together, so it judges relevance more precisely. But it is too slow for the whole collection. So we retrieve about twenty to thirty candidates with hybrid search, rerank them, and keep the top five for the model.

Think of hiring. One recruiter searches CVs for exact job titles. Another looks for similar experience described in other words. You combine both shortlists, and an experienced manager interviews only the top twenty, carefully, and chooses five. The interviews are slow, so you only do them for the shortlist.

Let's see fusion in plain Python. We have a vector list with four chunk IDs and a BM25 list with three. After fusion, c twelve comes first, because it is high in both lists. Chunk c ninety was found only by BM25, but its first place there puts it second overall.

Now a real catalogue. Rafael is a developer at a car-parts distributor in Porto, Portugal. Sales staff search eight thousand product sheets with questions like: is BR 7732 compatible with the twenty nineteen van model? He builds a BM25 index over the same chunks he stored in Chroma.

Next he adds the reranker. For each question, he fuses the top twenty from both searches, sends twenty-five candidates to a cross-encoder with the question, and keeps the five with the highest scores. You'll see something like a new order, with the exact product sheet moving up.

Here are his example results on ten code questions. Vector search alone finds the right sheet in the top five for four. BM25 alone finds eight, but fails when staff type the code without the dash. Hybrid finds nine. With reranking, still nine, but the right sheet reaches first place more often.

To fix the last failure, Rafael normalises the codes, removing dashes and spaces in both the chunks and the questions before BM25. He also records the extra reranking time per question, for the cost lesson later. Now the code question typed without a dash finds the right sheet too.

A common mistake is to think a reranker fixes everything. It only reorders the candidates it receives. If the right chunk is not there, reranking cannot find it. Check the candidate list first. And never add raw BM25 and cosine scores together. Use rank fusion instead.

Let's recap. First, BM25 keyword search finds exact names, codes and numbers that embeddings can miss, and vector search finds paraphrases and other languages. Second, reciprocal rank fusion combines ranked lists by position, so you never add scores on different scales. Third, a cross-encoder reranker improves the order of the candidates, but cannot recover chunks that retrieval missed.

Now it is your turn. In the exercise below, write eight questions with exact names or codes, add BM25 and a reranker, and compare four setups with hit at five. Measure the extra time the reranker adds, and write a short recommendation. In the next lesson, Query Rewriting and Conversational Retrieval, we handle follow-up questions like, and for last year?
```

## L08 Query Rewriting and Conversational Retrieval

- **Filename:** `ai-15-rag-systems-chat-with-your-data_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.
- **Pronunciation:** [VERSION] Claude API structured outputs (output_config with a JSON Schema; a forced tool_choice is rejected by some current models), the response content block format, and model choice (MODEL read from the environment; check the current models page). Never say a model ID or price.

```text
A user asks how many days of parental leave employees get. Your assistant answers well. Then the user asks: and for contractors? Search for those three words alone, and you get random passages. The question only makes sense inside the conversation.

In the last lesson, we improved retrieval with hybrid search and reranking. Today we fix the question itself, before it ever reaches retrieval.

Retrieval works one query at a time, and it has no memory. In a chat, many questions depend on earlier turns. And in twenty twenty-two? What about the second option? These are follow-up questions. Before retrieval, we rewrite them into standalone queries, such as: how many days of parental leave do contractors get?

The language model is good at this. From the previous course, you know how to ask for a structured output that your code can trust. Here, the request includes a small schema with two fields: one standalone query, and a list of up to three other phrasings. A schema in the request is the safest way to get this, because the reply must match it.

This gives us two techniques. Standalone rewriting resolves words like that, it, and and for, using only the last few turns. Multi-query retrieval searches with every phrasing, then fuses the lists with rank fusion from the last lesson. Different words reach different chunks. This improves recall when users write vaguely.

Think of a good receptionist taking a phone message. The caller says: tell her it's about the same thing as yesterday. The receptionist writes a note that names the person, the invoice and the order. The reader was not on the call, so the note must stand alone.

Let's follow Aigerim. She builds an HR policy assistant for a logistics company in Almaty, Kazakhstan. Policies are in Russian and English. First question: what is the travel allowance for Astana? Retrieval works, and the answer cites the travel policy.

Second question: and for drivers? Without rewriting, the top chunks are about vehicle maintenance for drivers. The answer is wrong, and it is easy to see why when we print the retrieved chunks. The search engine saw only the word drivers, so it found drivers, but the wrong topic.

Now she adds the rewrite function. It sends the last six messages and the new question, with the schema, and reads back the JSON. You'll see something like a standalone query about the travel allowance for drivers going to Astana, plus a short variant about a driver's daily allowance.

She searches with all three queries, fuses them, and the drivers' section of the travel policy is now the top chunk. She also shows the rewritten query in a debug panel, so testers can see exactly what was searched. That makes problems much easier to find later.

Two rules keep this safe. First, a complete question should come back almost unchanged, so she tests one, and gets only small word changes. Second, the rewrite is for search only. The final answer step still receives the user's original words.

A common mistake is to send the whole chat history to the embedding model as the query. Long histories mix topics, so retrieval becomes vague. Rewrite into one focused query instead. And remember, rewriting adds one model call per turn, so you can skip it for the first message, and use a smaller model for it.

Let's recap. First, follow-up questions depend on earlier turns, so rewrite them into standalone queries before retrieval. Second, a structured output gives your code a reliable standalone query, plus extra phrasings for multi-query retrieval. Third, use the rewrite only for search, keep the user's original question for the answer, and test that complete questions stay the same.

Now it is your turn. In the exercise below, write five short conversations with follow-up questions, add rewriting, and compare retrieval with and without it. For each follow-up, mark whether the expected chunk is in the top five. Note any rewrite that changed the meaning. That completes week two. In the next lesson, Grounded Answers with Citations, we make every answer show its sources.
```
