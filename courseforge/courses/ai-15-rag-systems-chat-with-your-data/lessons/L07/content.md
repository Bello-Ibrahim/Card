# L07 Hybrid Search and Reranking

Course: AI-15 · Module: M2 · Objectives: O6 · Video: 5 min (screen demo)

## Hook
A technician types "error E-4107 on pump PX-220". Your vector search returns general passages about pump errors, but not the one page that lists E-4107. Embeddings are good at meaning and weaker at exact strings. This lesson adds the missing piece.

## Explanation
**Keyword search** ranks chunks by the words they share with the question. The standard method is **BM25**. It gives a high score when a rare word, such as a product code, appears in a chunk, and a low score for common words. It is fast, needs no model, and is very good at names, codes, numbers and rare technical terms. It does not understand synonyms or other languages.

**Vector search** is the opposite: good at meaning and paraphrase, weaker at exact codes. **Hybrid search** runs both and combines the two ranked lists.

The scores from BM25 and cosine similarity are on different scales, so we do not add them. **Reciprocal rank fusion (RRF)** uses only the rank positions. Each chunk gets `1 / (k + rank)` from each list, and the totals are summed. The constant `k` (often 60) reduces the weight of small rank differences.

```python
def rrf(ranked_lists, k=60):
    scores = {}
    for ranking in ranked_lists:
        for rank, cid in enumerate(ranking, start=1):
            scores[cid] = scores.get(cid, 0) + 1 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)

vector_ids = ["c12", "c7", "c33", "c2"]
bm25_ids = ["c90", "c12", "c5"]
print(rrf([vector_ids, bm25_ids]))
```

Output:

```
['c12', 'c90', 'c7', 'c33', 'c5', 'c2']
```

Chunk c12 appears high in both lists, so it wins. Chunk c90 was found only by BM25, but its first place there puts it second overall.

For BM25 in Python, the small `rank_bm25` library is enough for course-sized collections. Chroma and PostgreSQL also offer full-text search options you can explore. [VERSION]

```python
from rank_bm25 import BM25Okapi  # [VERSION]
tokenised = [text.lower().split() for text in chunk_texts]
bm25 = BM25Okapi(tokenised)
scores = bm25.get_scores("error e-4107 px-220".split())
```

**Reranking.** Both searches compare a question vector (or word list) with each chunk separately. A **cross-encoder** reads the question and one chunk together, so it can judge relevance more precisely, but it is too slow to run on the whole collection. The usual design is: retrieve about 20–30 candidates with hybrid search, rerank them with a cross-encoder, and keep the top 5 for the LLM.

```python
from sentence_transformers import CrossEncoder
RERANK_MODEL = "your-cross-encoder-model"  # [VERSION] [VERIFY licence]
reranker = CrossEncoder(RERANK_MODEL)
pairs = [(question, texts[cid]) for cid in candidates]
scores = reranker.predict(pairs)
top5 = [cid for _, cid in sorted(zip(scores, candidates), reverse=True)[:5]]
```

**Analogy:** Hybrid search with reranking is like hiring. One recruiter searches CVs for exact job titles and certificates, another looks for people with similar experience described in other words. You combine both shortlists, and then an experienced manager interviews the top 20 carefully and chooses 5. The interviews are slow, so you only do them for the shortlist.

## Worked Example
Rafael is a developer at a hypothetical car-parts distributor in Porto, Portugal. Sales staff search a catalogue of 8,000 product sheets with questions such as "Is BR-7732 compatible with the 2019 van model?"

On screen, follow his comparison on 10 questions that contain part codes:

1. Vector search alone: the correct sheet is in the top 5 for 4 of 10 questions. Similar brake parts crowd out the exact code.
2. BM25 alone: 8 of 10. It fails when staff type the code without the dash.
3. Hybrid with RRF: 9 of 10.
4. Hybrid, then reranking 25 candidates down to 5: still 9 of 10, and the correct sheet moves to rank 1 more often.

These numbers are hypothetical. Rafael also normalises codes (removes dashes and spaces) in both the chunks and the questions before BM25, which fixes the remaining failure. He records the added reranking time per query for L14.

## Common Mistake
A common mistake is to add a reranker and assume it can fix everything. A reranker only reorders the candidates it receives. If the right chunk is not among them, reranking cannot find it. Check recall of the candidate list first, then use reranking to improve the order. A second mistake is to add raw BM25 and cosine scores together; use rank fusion instead.

## Key Takeaways
1. BM25 keyword search finds exact names, codes and numbers that embeddings can miss; vector search finds paraphrases and other languages.
2. Reciprocal rank fusion combines ranked lists by position, so you do not need to compare scores on different scales.
3. A cross-encoder reranker improves the order of a candidate list but cannot recover chunks that retrieval missed.

## Hands-on Exercise
**Task:** Add BM25 and a reranker to your pipeline, and compare retrieval results on questions that contain product codes or names.
**Tools:** Python 3, rank_bm25, sentence-transformers (CrossEncoder) and your Chroma collection (all free). [VERSION]
**Steps:**
1. Write 8 questions that contain exact names, codes, version numbers or rare terms from your collection, with the expected document for each.
2. Build a BM25 index over the same chunks you stored in Chroma.
3. For each question, get the top 20 from vector search and the top 20 from BM25, and fuse them with `rrf`.
4. Rerank the top 25 fused candidates with a cross-encoder and keep 5. Check the model card and licence first. [VERIFY]
5. Record hit@5 for vector only, BM25 only, hybrid, and hybrid with reranking.
6. Measure the extra time the reranker adds per question.
**What good looks like:** A table with four rows of hit@5, a timing note, and a short recommendation (for example "hybrid plus reranker, because it fixed 3 code questions at a cost of X ms").
**Time:** about 45 minutes

## Review Flags
- [VERSION] rank_bm25 (`BM25Okapi`, `get_scores`), sentence-transformers `CrossEncoder` API, full-text search options in Chroma and PostgreSQL, and current reranker model names.
- [VERIFY] Licence of the cross-encoder reranker model used in the demo (course-level flag).
- Rafael's results are hypothetical.
