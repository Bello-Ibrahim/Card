# L06 Vector Databases: Chroma and pgvector

Course: AI-15 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
A user asks, "What did the 2023 reports say about water prices?" Your index returns a perfect passage from a 2015 report. The meaning matches, but the year does not. A vector database can combine meaning with rules like "only 2023", and that combination is where much of the practical value is.

## Explanation
A **vector database** stores vectors with their text and metadata, and answers the question "which stored vectors are closest to this one?" Four ideas matter:

- **Collection (or table):** a named group of chunks that share one embedding model.
- **Adding:** each item has an ID, a vector (or text to embed), the text itself and metadata.
- **Similarity search:** return the k nearest vectors by cosine distance or a related measure.
- **Metadata filters:** limit the search to items whose metadata matches a condition, such as year or document type.

**Chroma** is our default. It is free, open source and runs inside your Python process with a local folder for storage. Metadata filters use a `where` argument: [VERSION]

```python
res = col.query(
    query_texts=["water prices"],
    n_results=5,
    where={"$and": [{"year": {"$gte": 2023}}, {"doc_type": "report"}]},
)
for cid, meta, dist in zip(res["ids"][0], res["metadatas"][0], res["distances"][0]):
    print(cid, meta["title"], meta["year"], round(dist, 3))
```

Store numbers such as `year` as integers, not strings, or range filters like `$gte` will not work as expected. A smaller distance means a closer match.

**pgvector** is an extension for PostgreSQL. Choose it when your data and user permissions already live in PostgreSQL, because you can join chunks with other tables and use normal SQL. It needs a PostgreSQL server, for example in local Docker or on a hosted free plan, so it is the optional path in this course. [VERSION]

```sql
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE chunks (
  id text PRIMARY KEY, doc_id text, year int, text text,
  embedding vector(384)  -- must match your model's vector size
);
CREATE INDEX ON chunks USING hnsw (embedding vector_cosine_ops);

SELECT id, text, embedding <=> %(q)s AS distance
FROM chunks WHERE year >= 2023
ORDER BY embedding <=> %(q)s LIMIT 5;
```

Here `<=>` is the cosine distance operator. With pgvector you compute the query vector yourself in Python and pass it as a parameter. [VERSION]

**Approximate search.** Comparing a question with every stored vector is exact but slow for millions of chunks. **Approximate nearest-neighbour (ANN)** indexes, such as **HNSW** (a layered graph of neighbours), check only a small part of the data. They are much faster and usually return almost the same results. Chroma uses an HNSW index by default; pgvector offers HNSW and IVFFlat. [VERSION] For a course-sized collection, the difference is small, but you should know that ANN results can occasionally miss a close neighbour, and filters combined with ANN can return fewer than k results.

**Analogy:** A vector database is like a large music shop where records are shelved by sound, not by artist name. Similar sounds sit together, so you can walk to the right shelf quickly. Metadata filters are the signs on each aisle, such as "released after 2020", that stop you from searching shelves you do not need.

## Worked Example
Oluwaseun is a backend developer at a hypothetical payments start-up in Lagos, Nigeria. Support staff ask questions about internal policies, and the company already runs PostgreSQL. His team lead asks whether to use Chroma or pgvector.

On screen, follow his comparison:

1. He loads 1,200 chunks into a Chroma collection with `year` and `doc_type` metadata.
2. He runs "chargeback time limit" with no filter. The top result is from a 2019 policy that was replaced.
3. He adds `where={"year": {"$gte": 2024}}` and gets the current policy first.
4. He loads the same chunks into a pgvector table in a local Docker container, with an HNSW index, and runs the same query with `WHERE year >= 2024`.
5. Both return the same top 3 chunks.

His decision: Chroma for fast local development and teaching; pgvector for production, because permissions, audit logs and document tables are already in PostgreSQL, and a single database is easier to back up.

## Common Mistake
Developers often store all metadata as text, or forget it completely. Then they cannot filter by year, language or document type, and must rebuild the index. Decide your metadata fields before ingestion, use the right types, and test at least one filter early. A second mistake is to mix chunks from two embedding models in one collection; keep one model per collection.

## Key Takeaways
1. A vector database stores vectors, text and metadata, and returns the nearest chunks, optionally limited by metadata filters.
2. Chroma is the free, local default; pgvector suits teams whose data and permissions already live in PostgreSQL.
3. ANN indexes such as HNSW trade a small amount of accuracy for large speed gains; test filters with them, because they can reduce the number of results.

## Hands-on Exercise
**Task:** Store your chunks in Chroma (or pgvector), run searches with and without a metadata filter by year or document type, and compare.
**Tools:** Python 3 and chromadb (free). Optional: PostgreSQL with pgvector in local Docker or a hosted free plan. [VERSION]
**Steps:**
1. Add your chunks from L05 to a collection with metadata `doc_id`, `title`, `page`, `year` (integer) and `doc_type`.
2. Write 5 questions where the year or document type matters.
3. Run each question without a filter and record the top 5 IDs with their metadata.
4. Run each again with a `where` filter and record the results.
5. Optional: repeat steps 3 and 4 in pgvector and compare the top 3.
6. Write 3 sentences on when filters helped and when they removed useful results.
**What good looks like:** A table of 5 questions with filtered and unfiltered top results, correct metadata types, and a clear note on when filtering improved relevance.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Chroma API: `query` with `where` filters, operators such as `$and` and `$gte`, the result format and the default index type.
- [VERSION] pgvector: `vector(n)` type, `<=>` operator, HNSW and IVFFlat index syntax and operator classes, and free plans of hosted PostgreSQL services (course-level flag).
- The vector size 384 is an example and depends on the chosen embedding model.
