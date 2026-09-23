# L07 Hybrid Search and Reranking | Presenter Script

Course: AI-15 · Video: 5 min · Words: 687

## Hook
A technician types: error E 4107 on pump PX 220. Your vector search returns general passages about pump errors, but not the one page that lists that exact code. Embeddings are good at meaning, and weaker at exact strings. Let's add the missing piece.

## Explain
In the last lesson, we stored chunks in a vector database. Today we add keyword search, and then a second opinion called reranking.

Keyword search ranks chunks by the words they share with the question. The standard method is called BM25. It gives a high score when a rare word, like a product code, appears in a chunk. It is fast, needs no model, and is very good at names, codes and numbers. But it does not understand synonyms or other languages.

Hybrid search runs both and combines the two ranked lists. The scores are on different scales, so we do not add them. Reciprocal rank fusion uses only the positions. Each chunk gets one divided by sixty plus its rank from each list, and the totals are summed.

Then comes reranking. A cross-encoder reads the question and one chunk together, so it judges relevance more precisely. But it is too slow for the whole collection. So we retrieve about twenty to thirty candidates with hybrid search, rerank them, and keep the top five for the model.

Think of hiring. One recruiter searches CVs for exact job titles. Another looks for similar experience described in other words. You combine both shortlists, and an experienced manager interviews only the top twenty, carefully, and chooses five. The interviews are slow, so you only do them for the shortlist.

## Demonstrate
Let's see fusion in plain Python. We have a vector list with four chunk IDs and a BM25 list with three. After fusion, c twelve comes first, because it is high in both lists. Chunk c ninety was found only by BM25, but its first place there puts it second overall.

Now a real catalogue. Rafael is a developer at a car-parts distributor in Porto, Portugal. Sales staff search eight thousand product sheets with questions like: is BR 7732 compatible with the twenty nineteen van model? He builds a BM25 index over the same chunks he stored in Chroma.

Next he adds the reranker. For each question, he fuses the top twenty from both searches, sends twenty-five candidates to a cross-encoder with the question, and keeps the five with the highest scores. You'll see something like a new order, with the exact product sheet moving up.

Here are his example results on ten code questions. Vector search alone finds the right sheet in the top five for four. BM25 alone finds eight, but fails when staff type the code without the dash. Hybrid finds nine. With reranking, still nine, but the right sheet reaches first place more often.

To fix the last failure, Rafael normalises the codes, removing dashes and spaces in both the chunks and the questions before BM25. He also records the extra reranking time per question, for the cost lesson later. Now the code question typed without a dash finds the right sheet too.

A common mistake is to think a reranker fixes everything. It only reorders the candidates it receives. If the right chunk is not there, reranking cannot find it. Check the candidate list first. And never add raw BM25 and cosine scores together. Use rank fusion instead.

## Recap
Let's recap. First, BM25 keyword search finds exact names, codes and numbers that embeddings can miss, and vector search finds paraphrases and other languages. Second, reciprocal rank fusion combines ranked lists by position, so you never add scores on different scales. Third, a cross-encoder reranker improves the order of the candidates, but cannot recover chunks that retrieval missed.

## CTA
Now it is your turn. In the exercise below, write eight questions with exact names or codes, add BM25 and a reranker, and compare four setups with hit at five. Measure the extra time the reranker adds, and write a short recommendation. In the next lesson, Query Rewriting and Conversational Retrieval, we handle follow-up questions like, and for last year?

## Thumbnail
Headline: Find the Exact Code
Image: Navy background, a part code 'BR-7732' in a search box, two result lists merging into one with a teal arrow, headline in teal Inter Bold.

## Production Notes
- [VERSION] rank_bm25 (BM25Okapi, get_scores), the sentence-transformers CrossEncoder API, full-text search options in Chroma and PostgreSQL, and current reranker model names. Do not say a reranker model name in the voiceover.
- [VERIFY] Licence of the cross-encoder reranker model used in the demo.
- The rrf output is tested plain Python: the screen must show exactly ['c12', 'c90', 'c7', 'c33', 'c5', 'c2'].
- Rafael's results (4, 8, 9 and 9 of 10) are hypothetical; the voiceover calls them example results and the slide carries a 'hypothetical results' label.
- Part codes BR-7732, E-4107 and PX-220 are invented; Rafael and the Porto car-parts distributor are hypothetical.
