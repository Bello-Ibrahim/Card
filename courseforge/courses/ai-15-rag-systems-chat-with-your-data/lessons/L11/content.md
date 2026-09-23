# L11 Measuring Retrieval Quality

Course: AI-15 · Module: M3 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
If the right chunk never reaches the model, the answer cannot be correct and grounded at the same time. So before you judge answers, measure retrieval. It is fast, it is free (no LLM calls), and it tells you exactly where your pipeline is losing information.

## Explanation
For each answerable question in your test set, you know which chunks are **relevant**: those from the expected source that contain the evidence phrase. Retrieval returns a ranked list. Three metrics compare the two.

- **Hit rate@k:** the share of questions where at least one relevant chunk is in the top k. It answers "does the model get a chance to see the answer?"
- **Recall@k:** for each question, the share of its relevant chunks that are in the top k, averaged over questions. It matters when an answer needs several chunks, such as a comparison.
- **Mean reciprocal rank (MRR):** for each question, 1 divided by the rank of the first relevant chunk (0 if none is found), averaged. A relevant chunk at rank 1 scores 1, at rank 2 scores 0.5, at rank 4 scores 0.25. It shows how high the right chunk is, which matters when you pass only a few chunks to the model.

Skip unanswerable questions for these metrics; you will test them with answer metrics in L12.

```python
def retrieval_metrics(runs, k=5):
    """runs: list of (retrieved_ids, relevant_ids_set) per question."""
    hits = recall = rr = 0.0
    for retrieved, relevant in runs:
        top = retrieved[:k]
        found = [c for c in top if c in relevant]
        hits += 1 if found else 0
        recall += len(found) / len(relevant)
        rr += next((1 / (i + 1) for i, c in enumerate(top) if c in relevant), 0)
    n = len(runs)
    return {"hit@k": hits / n, "recall@k": recall / n, "mrr": rr / n}

runs = [(["a", "b", "c"], {"a"}),
        (["d", "e", "f"], {"f", "x"}),
        (["g", "h", "i"], {"z"})]
print({m: round(v, 3) for m, v in retrieval_metrics(runs, k=3).items()})
```

Output:

```
{'hit@k': 0.667, 'recall@k': 0.5, 'mrr': 0.444}
```

The first question finds its chunk at rank 1, the second finds one of two relevant chunks at rank 3, and the third finds nothing.

**Reading failures one by one.** Numbers tell you how much is wrong; they do not tell you why. For each failed question, open the retrieved chunks and the relevant chunk and classify the cause:

- **Chunking:** the answer is split across two chunks, or buried in a very long chunk.
- **Embeddings:** the meaning is close but the model ranks other chunks higher, often with specialist words or another language.
- **Missing keywords:** the question contains a code, name or number that vector search ignores (hybrid search helps).
- **Vague question:** the question itself is unclear or depends on context (query rewriting helps, or the test item needs editing).
- **Parsing or data:** the text was never extracted correctly, such as a table or a scanned page.

**Analogy:** Retrieval metrics are like a doctor's basic measurements: temperature, pulse and blood pressure. They quickly tell you that something is wrong and how serious it is. But to treat the patient, the doctor still has to examine them and find the cause.

## Worked Example
Hana is an engineer at a hypothetical insurance company in Prague, Czech Republic. Her assistant answers questions about claims procedures. She compares two versions on 32 answerable test questions:

- **Version A:** 800-character chunks, vector search only.
- **Version B:** the same chunks, hybrid search with RRF.

On screen, follow her steps:

1. She runs both versions over the test set, saving the top 10 IDs per question to `runs_A.json` and `runs_B.json`.
2. She computes metrics at k=5. Hypothetical results: A has hit@5 0.72 and MRR 0.51; B has hit@5 0.84 and MRR 0.63.
3. She lists the 5 questions that B still fails and opens each one.
4. Her classification: 2 are chunking (a table split across chunks), 1 is embeddings (a Czech legal term), 1 is a vague question ("what about the form?"), and 1 is parsing (a scanned appendix).

The metrics show B is better. The failure analysis gives her a clear next step: fix table chunking first, because it causes the most failures.

## Common Mistake
Learners often report only one number, such as hit@10, and choose a large k to make it look good. But if you only pass 5 chunks to the model, hit@10 is not the number that matters. Report metrics at the k you actually use, add MRR to show ranking quality, and always look at individual failures. A second mistake is to count a chunk as relevant only by its old ID; after re-chunking, match by source and evidence phrase instead.

## Key Takeaways
1. Hit rate@k and recall@k show whether relevant chunks reach the model; MRR shows how high the first relevant chunk is ranked.
2. Measure at the k your pipeline actually uses, on answerable questions from a frozen test set.
3. Classify each failure by cause (chunking, embeddings, missing keywords, vague question, parsing) to decide what to fix next.

## Hands-on Exercise
**Task:** Compute hit rate, recall@5 and MRR for 2 versions of your pipeline, and classify the causes of 5 failures.
**Tools:** Python 3, your test set from L10, your pipeline versions from L05–L08 (no API calls needed).
**Steps:**
1. Write a function that marks a retrieved chunk as relevant if it comes from the expected source and contains the evidence phrase.
2. Choose 2 versions of your pipeline, for example vector only and hybrid.
3. Run all answerable questions through both versions and save the ranked IDs.
4. Compute `retrieval_metrics` at k=5 for both and put them in a table.
5. Pick 5 failures from the better version and classify each cause.
6. Write one sentence on what you would fix first and why.
**What good looks like:** A table with hit@5, recall@5 and MRR for 2 versions, 5 classified failures with a short note each, and a next step linked to the most common cause.
**Time:** about 45 minutes

## Review Flags
- None. The metrics code is plain Python and was tested; Hana's results are hypothetical and illustrate the method.
