# Screen Demo Pack: AI-15 L06 Vector Databases: Chroma and pgvector

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L06_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Show the add step: ids, documents and metadatas with year as an integer and doc_type.
2. Run col.count() and show 1,200.

**Narration over this clip (for pacing)**

> Let's compare them. Oluwaseun is a backend developer at a payments start-up in Lagos, Nigeria. Support staff ask about internal policies, and the company already runs PostgreSQL. His team lead asks: Chroma or pgvector? First, he loads twelve hundred chunks into a Chroma collection, with year and document type as metadata.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L06_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Run col.query(query_texts=['chargeback time limit'], n_results=5) without a where argument.
2. Print id, title, year and rounded distance for each result.
3. Highlight the top result with year 2019.

**Narration over this clip (for pacing)**

> He searches for chargeback time limit, with no filter. You'll see something like this: a list of chunk IDs, titles, years and distances, where a smaller distance means a closer match. But the top result is from a twenty nineteen policy that was replaced.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L06_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Add where={'year': {'$gte': 2024}} to the same query and run it.
2. Show the current policy as the top result.
3. Show briefly the $and example combining year and doc_type from content.md.

**Narration over this clip (for pacing)**

> Now he adds a filter: year greater than or equal to twenty twenty-four. The current policy comes first. One detail matters here. Store numbers like the year as integers, not text, or range filters will not work as expected.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L06_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show the terminal with a local PostgreSQL Docker container running.
2. Run the SQL: CREATE EXTENSION vector, CREATE TABLE chunks with embedding vector(n), CREATE INDEX using hnsw with vector_cosine_ops.
3. In Python, encode the question and pass the vector as the query parameter.

**Narration over this clip (for pacing)**

> Next, pgvector. In a local Docker container, he enables the extension, and creates a chunks table with a vector column that matches his model's vector size. He adds an HNSW index for cosine distance. With pgvector, he computes the question's vector himself in Python, and passes it to the query.

## Clip 5: scene 11

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L06_screen_5.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Run the SELECT with ORDER BY embedding <=> query vector, WHERE year >= 2024, LIMIT 5.
2. Place the Chroma top 3 and the pgvector top 3 side by side and show that they match.

**Narration over this clip (for pacing)**

> He runs the same search, ordered by cosine distance, with the same year filter in a normal where clause. Both databases return the same top three chunks. So the choice is not about search quality here. It is about where your data already lives.

## Production notes for this lesson

- [VERSION] Chroma API: query with where filters, operators such as $and and $gte, the result format and the default index type.
- [VERSION] pgvector: vector(n) type, the <=> operator, HNSW and IVFFlat index syntax and operator classes, and free plans of hosted PostgreSQL services. The voiceover does not name any hosted provider or plan.
- The vector size 384 in the SQL is an example; it must match the embedding model used in the recording.
- Search results, titles and distances in the demo are from a real run; the voiceover says 'you'll see something like' and gives no exact distances.
- Oluwaseun and the Lagos payments start-up are hypothetical; the 1,200 policy chunks are synthetic teaching data.
