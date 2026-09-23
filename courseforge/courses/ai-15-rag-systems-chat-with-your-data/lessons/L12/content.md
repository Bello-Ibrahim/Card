# L12 Measuring Answer Quality: Faithfulness and Relevance

Course: AI-15 · Module: M3 · Objectives: O5, O6 · Video: 5 min (screen demo)

## Hook
Retrieval found the right chunk. The model wrote a fluent answer with two citations. But one sentence in the answer says something the chunk never said. Retrieval metrics cannot see this problem. You need to check the answer itself.

## Explanation
Two answer metrics matter most in RAG:

- **Faithfulness:** every claim in the answer is supported by the retrieved chunks. An answer can be true in the real world and still unfaithful, if it adds facts the context does not contain.
- **Answer relevance:** the answer addresses the question that was asked, completely and without drifting to another topic.

For unanswerable questions, the correct result is the "I don't know" sentence. Score these separately as **correct refusal rate**: how often the system refuses when it should, and how often it refuses when it should not.

**LLM as a judge.** Checking every answer by hand is slow, so we ask an LLM to act as a judge with a clear rubric. Give the judge the question, the retrieved chunks and the answer, and ask for a structured verdict. A forced tool call with a schema such as `{"faithful": "yes" | "partly" | "no", "unsupported_claims": [str], "relevant": 1-3}` works well. The rubric must define each label, for example:

```python
JUDGE_RUBRIC = """Judge the ANSWER using only the CHUNKS.
faithful = "yes" if every claim is supported by the chunks,
"partly" if at least one claim is unsupported, "no" if the main claim is unsupported.
List each unsupported claim. Do not use outside knowledge.
relevant = 3 if the answer fully addresses the QUESTION, 2 if partly, 1 if not."""
```

Use a different prompt, and if possible a different or stronger model, for judging than for answering. Never let the judge see the expected answer when you score faithfulness, because faithfulness is about the chunks, not about the reference.

**Checking the judge.** A judge is a model too, and it can be wrong. Label a sample of answers yourself, without looking at the judge's verdict, and compare:

```python
def agreement(judge, human):
    pairs = list(zip(judge, human))
    same = sum(j == h for j, h in pairs)
    diffs = [(i, j, h) for i, (j, h) in enumerate(pairs) if j != h]
    return same / len(pairs), diffs

judge = ["yes", "yes", "partly", "no", "yes"]
human = ["yes", "partly", "partly", "no", "yes"]
rate, diffs = agreement(judge, human)
print(rate, diffs)
```

Output:

```
0.8 [(1, 'yes', 'partly')]
```

Read every disagreement. If the judge is often too generous, make the rubric stricter or ask it to list claims first and then check each one. Only trust judge scores at scale when agreement on your sample is acceptable for your use.

**Keeping costs low.** The Claude API is paid, so evaluation should be planned. Use the test set from L10 (30–50 questions), not thousands. Save answers and chunks to a file, so you can re-judge without re-generating. For larger runs, the API's batch processing option handles many requests at a lower price with slower delivery. [VERSION] Open-source RAG evaluation libraries offer ready-made faithfulness metrics; if you use one, read how it defines each metric, because definitions differ. [VERSION]

**Analogy:** An LLM judge is like a new teaching assistant who marks exam papers with a marking guide. The assistant is fast, but before you trust their marks, the lead teacher marks a sample of the same papers. If they agree on most papers and the differences make sense, the assistant can mark the rest.

## Worked Example
Kwame is a developer for a hypothetical agricultural advice service in Kumasi, Ghana. Extension officers ask an assistant about crop guidance documents.

On screen, follow his evaluation:

1. He runs 25 test questions (20 answerable, 5 unanswerable) and saves question, chunks and answer to `answers.jsonl`.
2. For the 20 answerable ones, he calls the judge with `JUDGE_RUBRIC` and a forced tool output, and saves the verdicts.
3. He labels 10 answers himself before he opens the judge's file.
4. Agreement is 8 of 10. In both disagreements, the judge said "yes" but the answer had added a planting month that was not in the chunks. He changes the rubric to "list every claim first, then check each claim", re-judges, and agreement rises to 9 of 10.
5. Result (hypothetical): 16 of 20 faithful, 3 partly, 1 no; 4 of 5 correct refusals.

The unfaithful answers share a pattern: the model filled gaps with general farming knowledge. Kwame strengthens the "only from the chunks" instruction and adds this to his list of design changes to test.

## Common Mistake
Many teams run an LLM judge and report its score as if it were the truth. Without a human check on a sample, you do not know whether the judge is strict, generous or random. Another mistake is to judge faithfulness against the expected answer instead of the retrieved chunks. That measures correctness, which is useful, but it is a different question.

## Key Takeaways
1. Faithfulness checks that every claim is supported by the retrieved chunks; answer relevance checks that the answer addresses the question; refusals are scored separately.
2. An LLM judge needs a clear rubric and a structured output, and must be checked against your own labels on a sample.
3. Keep evaluation cheap: small test sets, saved outputs, and batch processing for larger runs.

## Hands-on Exercise
**Task:** Score 20 answers for faithfulness with an LLM judge, label 10 of them yourself, and report how often you and the judge agree.
**Tools:** Python 3, the anthropic SDK (paid; keep runs small), your test set and pipeline. [VERSION]
**Steps:**
1. Run 20 answerable test questions and save question, chunks and answer to a file.
2. Write your rubric and a forced tool schema for the judge.
3. Judge all 20 answers and save the verdicts.
4. Label 10 answers yourself, without looking at the judge's verdicts.
5. Compute agreement with `agreement()` and read every disagreement.
6. Change the rubric once if needed, re-judge, and compare.
**What good looks like:** 20 saved verdicts, 10 human labels, an agreement rate, a short explanation of each disagreement, and a faithfulness score you can defend.
**Time:** about 50 minutes

## Review Flags
- [VERSION] Claude API batch processing option (interface, discount and delivery time), forced tool use for the judge, and model choice (check the current models page).
- [VERSION] Optional open-source RAG evaluation libraries and their metric definitions (course-level flag).
- Kwame's results are hypothetical.
