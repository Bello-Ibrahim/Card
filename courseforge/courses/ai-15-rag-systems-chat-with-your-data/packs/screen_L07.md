# Screen Demo Pack: AI-15 L07 Hybrid Search and Reranking

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L07_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Show the rrf function with k=60.
2. Show vector_ids = ['c12', 'c7', 'c33', 'c2'] and bm25_ids = ['c90', 'c12', 'c5'].
3. Run print(rrf([vector_ids, bm25_ids])) and show the exact output ['c12', 'c90', 'c7', 'c33', 'c5', 'c2'].

**Narration over this clip (for pacing)**

> Let's see fusion in plain Python. We have a vector list with four chunk IDs and a BM25 list with three. After fusion, c twelve comes first, because it is high in both lists. Chunk c ninety was found only by BM25, but its first place there puts it second overall.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L07_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show the product sheet chunks and a sample sheet with code BR-7732.
2. Build the BM25 index: lower-case, split into words, BM25Okapi(tokenised).
3. Run bm25.get_scores for a code question and show the top chunk IDs.

**Narration over this clip (for pacing)**

> Now a real catalogue. Rafael is a developer at a car-parts distributor in Porto, Portugal. Sales staff search eight thousand product sheets with questions like: is BR 7732 compatible with the twenty nineteen van model? He builds a BM25 index over the same chunks he stored in Chroma.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L07_screen_3.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show the CrossEncoder cell with RERANK_MODEL read from a variable.
2. Build question and chunk pairs for 25 fused candidates and run reranker.predict.
3. Print the top 5 IDs before and after reranking side by side.

**Narration over this clip (for pacing)**

> Next he adds the reranker. For each question, he fuses the top twenty from both searches, sends twenty-five candidates to a cross-encoder with the question, and keeps the five with the highest scores. You'll see something like a new order, with the exact product sheet moving up.

## Clip 4: scene 11

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L07_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show a small normalise function that removes dashes and spaces from codes.
2. Re-run the failed question typed as BR7732 and show the right sheet now retrieved.
3. Print the average reranking time per question.

**Narration over this clip (for pacing)**

> To fix the last failure, Rafael normalises the codes, removing dashes and spaces in both the chunks and the questions before BM25. He also records the extra reranking time per question, for the cost lesson later. Now the code question typed without a dash finds the right sheet too.

## Production notes for this lesson

- [VERSION] rank_bm25 (BM25Okapi, get_scores), the sentence-transformers CrossEncoder API, full-text search options in Chroma and PostgreSQL, and current reranker model names. Do not say a reranker model name in the voiceover.
- [VERIFY] Licence of the cross-encoder reranker model used in the demo.
- The rrf output is tested plain Python: the screen must show exactly ['c12', 'c90', 'c7', 'c33', 'c5', 'c2'].
- Rafael's results (4, 8, 9 and 9 of 10) are hypothetical; the voiceover calls them example results and the slide carries a 'hypothetical results' label.
- Part codes BR-7732, E-4107 and PX-220 are invented; Rafael and the Porto car-parts distributor are hypothetical.
