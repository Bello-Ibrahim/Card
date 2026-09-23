# L06 Vector Databases: Chroma and pgvector | Presenter Script

Course: AI-15 · Video: 5 min · Words: 695

## Hook
A user asks what the twenty twenty-three reports said about water prices. Your index returns a perfect passage from a twenty fifteen report. The meaning matches, but the year does not. Today we fix that by combining meaning with simple rules.

## Explain
In the last lesson, we cut our records into chunks. Now we look at where they live: the vector database.

A vector database stores vectors with their text and metadata, and answers one question: which stored vectors are closest to this one? Four ideas matter. A collection is a named group of chunks that share one embedding model. Each item you add has an ID, the text, a vector and metadata. Similarity search returns the nearest items. And metadata filters limit the search, for example by year.

Think of a large music shop where records are shelved by sound, not by artist name. Similar sounds sit together, so you walk to the right shelf quickly. Metadata filters are the signs on each aisle, like released after twenty twenty, that stop you from searching shelves you do not need.

Chroma is our default. It is free, open source, and runs inside your Python program with a local folder for storage. pgvector is an extension for PostgreSQL. Choose it when your data and user permissions already live there, because you can join chunks with other tables using normal SQL.

Comparing a question with every stored vector is exact, but slow for millions of chunks. Approximate nearest-neighbour indexes, such as HNSW, a layered graph of neighbours, check only a small part of the data. They are much faster, and usually return almost the same results. But combined with filters, they can sometimes return fewer results than you asked for.

## Demonstrate
Let's compare them. Oluwaseun is a backend developer at a payments start-up in Lagos, Nigeria. Support staff ask about internal policies, and the company already runs PostgreSQL. His team lead asks: Chroma or pgvector? First, he loads twelve hundred chunks into a Chroma collection, with year and document type as metadata.

He searches for chargeback time limit, with no filter. You'll see something like this: a list of chunk IDs, titles, years and distances, where a smaller distance means a closer match. But the top result is from a twenty nineteen policy that was replaced.

Now he adds a filter: year greater than or equal to twenty twenty-four. The current policy comes first. One detail matters here. Store numbers like the year as integers, not text, or range filters will not work as expected.

Next, pgvector. In a local Docker container, he enables the extension, and creates a chunks table with a vector column that matches his model's vector size. He adds an HNSW index for cosine distance. With pgvector, he computes the question's vector himself in Python, and passes it to the query.

He runs the same search, ordered by cosine distance, with the same year filter in a normal where clause. Both databases return the same top three chunks. So the choice is not about search quality here. It is about where your data already lives.

His decision: Chroma for fast local development and teaching. pgvector for production, because permissions, audit logs and document tables already live in PostgreSQL, and one database is easier to back up.

A common mistake is to store all metadata as text, or to forget it. Then you cannot filter, and you must rebuild the index. Decide your fields before ingestion, and keep one embedding model per collection.

## Recap
Let's recap. First, a vector database stores vectors, text and metadata, and returns the nearest chunks, optionally limited by filters. Second, Chroma is the free, local default, and pgvector suits teams whose data already lives in PostgreSQL. Third, approximate indexes like HNSW trade a little accuracy for a lot of speed, so test your filters with them.

## CTA
Now it is your turn. In the exercise below, store your chunks with typed metadata, write five questions where the year or document type matters, and compare results with and without a filter. In the next lesson, Hybrid Search and Reranking, we find the exact names and codes that embeddings can miss.

## Thumbnail
Headline: Meaning Plus Filters
Image: Navy background, clusters of glowing dots on shelves with a teal aisle sign reading 'year ≥ 2024', headline in teal Inter Bold.

## Production Notes
- [VERSION] Chroma API: query with where filters, operators such as $and and $gte, the result format and the default index type.
- [VERSION] pgvector: vector(n) type, the <=> operator, HNSW and IVFFlat index syntax and operator classes, and free plans of hosted PostgreSQL services. The voiceover does not name any hosted provider or plan.
- The vector size 384 in the SQL is an example; it must match the embedding model used in the recording.
- Search results, titles and distances in the demo are from a real run; the voiceover says 'you'll see something like' and gives no exact distances.
- Oluwaseun and the Lagos payments start-up are hypothetical; the 1,200 policy chunks are synthetic teaching data.
