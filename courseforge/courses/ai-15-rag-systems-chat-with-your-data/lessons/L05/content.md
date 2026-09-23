# L05 Chunking Strategies

Course: AI-15 · Module: M2 · Objectives: O3, O6 · Video: 5 min (screen demo)

## Hook
In L03, one answer failed because a fixed-size chunk cut a table in half. Chunking looks like a small technical detail, but it decides what retrieval can find. A chunk that is too small loses its meaning, and a chunk that is too large hides the answer among other topics.

## Explanation
A **chunk** is the unit you embed, retrieve and cite. Three common strategies are:

- **Fixed-size with overlap:** cut every N characters (or tokens) and repeat the last few as the start of the next chunk. It is simple and predictable, but it can cut sentences and tables.
- **Sentence or paragraph based:** collect whole sentences until you reach a size limit. Chunks end at natural boundaries.
- **Structure based:** split by headings in Markdown or HTML, then split long sections further. Each chunk stays inside one topic.

A simple improvement that helps all three is to **add the document and section title** to each chunk's text. A chunk that says only "The limit is 30 days" becomes "Refund policy > Online orders: The limit is 30 days", and a question about refunds can now find it.

Here is a sentence-based chunker with overlap and a title prefix. It is plain Python, so you can run it now:

```python
import re

def chunk_sentences(text, title, max_chars=500, overlap=1):
    sents = re.split(r"(?<=[.!?])\s+", text.strip())
    chunks, cur = [], []
    for s in sents:
        if cur and len(" ".join(cur + [s])) > max_chars:
            chunks.append(f"{title}: " + " ".join(cur))
            cur = cur[-overlap:] if overlap else []
        cur.append(s)
    if cur:
        chunks.append(f"{title}: " + " ".join(cur))
    return chunks

text = ("Orders ship in 2 days. Returns are free. "
        "Refunds take 10 days. Gift cards cannot be refunded.")
for c in chunk_sentences(text, "Returns > Online", max_chars=60):
    print(c)
```

Output:

```
Returns > Online: Orders ship in 2 days. Returns are free.
Returns > Online: Returns are free. Refunds take 10 days.
Returns > Online: Refunds take 10 days. Gift cards cannot be refunded.
```

The overlap of one sentence means a fact near a boundary appears in two chunks, so it is less likely to be lost. The cost is a larger index.

**Measure, do not guess.** There is no best chunk size for every collection. Short, factual FAQs work well with small chunks; long technical explanations often need larger ones. The reliable method is to build the index with several settings and compare them on the same test questions. The simplest measure is **hit@5**: for each question, is a chunk that contains the answer in the top 5 results? You will learn fuller metrics in L11.

```python
def hit_at_k(results, expected, k=5):
    hits = sum(1 for q, ids in results.items() if expected[q] & set(ids[:k]))
    return hits / len(results)

results = {"q1": ["d3#2", "d1#0"], "q2": ["d2#4", "d2#5"]}
expected = {"q1": {"d1#0"}, "q2": {"d9#1"}}
print(hit_at_k(results, expected))  # 0.5
```

Because chunk IDs change when the chunk size changes, label the expected answer by document and a short phrase, then mark a chunk as correct if it comes from that document and contains the phrase.

**Analogy:** Chunking is like cutting a book into index cards for a study group. If each card holds half a sentence, nobody understands it. If each card holds a whole chapter, you cannot find the fact you need. Good cards hold one idea each, with the chapter title written at the top.

## Worked Example
Mei-Lin maintains technical manuals for a hypothetical equipment maker in Hsinchu, Taiwan. Engineers ask questions such as "What torque does the M4 bolt on the cooling plate need?"

She builds three indexes: 300, 800 and 1,500 characters, each with a one-sentence overlap and the section title as a prefix. For 10 test questions she records whether a correct chunk is in the top 5.

Hypothetical results: 300 characters finds 6 of 10, 800 finds 9 of 10, and 1,500 finds 7 of 10. The small chunks lost the name of the part, which was in the previous sentence. The large chunks mixed several procedures, so their vectors became less specific. She chooses 800 and records why, with the numbers, in her design notes.

## Common Mistake
Learners often copy a chunk size from a tutorial and never test it. A setting that worked for news articles may fail for legal contracts or code documentation. The second mistake is to measure only answer quality. Measure retrieval directly, because a good prompt cannot fix a missing chunk.

## Key Takeaways
1. Fixed-size, sentence-based and structure-based chunking each have trade-offs; overlap protects facts near chunk boundaries.
2. Adding the document and section title to each chunk gives short chunks the context they need to be found.
3. Choose chunk size by measuring a retrieval metric, such as hit@5, on your own test questions.

## Hands-on Exercise
**Task:** Index your collection with 3 chunk sizes, and compare how often the right chunk is in the top 5 for 10 test questions.
**Tools:** Python 3, your `records.jsonl` from L04, chromadb and sentence-transformers (free). [VERSION]
**Steps:**
1. Write 10 test questions. For each, note the expected document and a short phrase from the answer.
2. Chunk your records with `chunk_sentences` at 3 sizes, for example 300, 800 and 1,500 characters.
3. Create one Chroma collection per size, for example `chunks_300`. Store `doc_id` and `page` as metadata.
4. For each question and each collection, retrieve the top 5 chunks and mark a hit if one comes from the expected document and contains the phrase.
5. Show a small table: chunk size, number of chunks, hit@5.
6. Pick a size and write 2 sentences explaining why, using your numbers.
**What good looks like:** Three collections, a results table with hit@5 for each size, and a choice that is justified by the numbers, not by a tutorial default.
**Time:** about 45 minutes

## Review Flags
- [VERSION] chromadb and sentence-transformers APIs used in the exercise.
- The Mei-Lin results are hypothetical and illustrate the method only.
