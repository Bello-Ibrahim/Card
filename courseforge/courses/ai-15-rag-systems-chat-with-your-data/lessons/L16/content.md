# L16 Capstone Step 2: Evaluate, Improve and Report

Course: AI-15 · Module: M4 · Objectives: O5, O6, O7 · Video: 5 min (screen demo)

## Hook
Your assistant works in a demo. Now a team lead asks, "How good is it, what did you change, and what will it cost?" In this final step you answer with evidence: a measured baseline, two improvements, a second measurement, and a short report that someone else can act on.

## Explanation
Step 2 follows a simple loop: **measure, diagnose, change one thing, measure again.**

**1. Baseline.** Freeze your test set (30–50 items, at least 5 unanswerable) and run the full pipeline once. Record:

- Retrieval: hit@k, recall@k and MRR at the k you use (L11).
- Answers: faithfulness and relevance with your LLM judge, plus a human check on a sample (L12), and the correct refusal rate on unanswerable questions.
- Cost and latency per query (L14).

**2. Diagnose.** Classify the failures by cause (L11). Choose improvements that target the most common cause, not the technique you like most.

**3. At least two evidence-based improvements.** Change one thing at a time and re-run the same test set after each change. Typical choices:

- Table-aware or structure-based chunking for split tables.
- Hybrid search or code normalisation for missed names and codes.
- A reranker for good candidates ranked too low.
- Query rewriting for vague follow-ups.
- A stricter grounded prompt for unfaithful answers.
- A smaller k or prompt caching for cost.

Keep each run's settings and scores in one results file, so the report tables come directly from data:

```python
import json

def log_run(path, version, settings, metrics):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps({"version": version, **settings, **metrics}) + "\n")

def compare(path):
    rows = [json.loads(line) for line in open(path, encoding="utf-8")]
    for r in rows:
        print(f"{r['version']:<10} hit@5={r['hit5']:.2f} "
              f"faithful={r['faithful']:.2f} cost={r['cost']:.4f}")
```

**4. Deploy.** Run the assistant in a place your user group could reach, even if it is only a shared internal server or a free hosting plan for the demo. [VERSION] Keep the API key on the server and apply your access-control filter (L13).

**5. The evaluation report (about 2 pages):**

1. **Purpose:** user group, collection, licence, and what the assistant should and should not do.
2. **Design choices:** chunking, embedding model, vector store, retrieval, prompt, each with the reason or evidence.
3. **Metrics before and after:** one table with retrieval, answer, refusal, latency and cost figures for each version.
4. **Improvements:** what you changed, why, and the measured effect, including changes that did not help.
5. **Known failures:** 3–5 real examples with causes.
6. **Risks and next steps:** access control, freshness, prompt injection, data location, and what you would do next.

**Analogy:** The evaluation report is like a building inspector's report for a new house. It does not only say "the house is good". It lists what was tested, the measurements, the repairs made, and the problems still to fix, so the owner can make informed decisions.

## Worked Example
Camila is a developer in Belo Horizonte, Brazil, building a hypothetical assistant over an open-source web framework's English documentation for Brazilian developers who ask in Portuguese. [VERIFY] licence of the documentation.

On screen, follow her loop (all numbers hypothetical):

1. **Baseline (v1):** hit@5 0.70, MRR 0.52, faithfulness 0.80, correct refusals 4 of 6.
2. **Diagnosis:** most failures are code names such as function names, plus two Portuguese questions with technical terms.
3. **Change 1 (v2):** hybrid search with RRF. Hit@5 rises to 0.83; faithfulness is unchanged.
4. **Change 2 (v3):** a stricter prompt with "reply exactly" for refusals and claim-by-claim citations. Correct refusals rise to 6 of 6, and faithfulness to 0.90.
5. **Tried and rejected:** a reranker added latency with no hit-rate gain on her set, so she removed it and reported this.
6. She logs each run with `log_run`, deploys v3 on a free hosting plan, and writes her report with one results table and five failure examples.

## Common Mistake
Learners often change several things at once and then cannot say which change helped. Others report only the final numbers, or only the improvements that worked. Change one thing per run, keep a log of every run, and include failed attempts in the report. Honest negative results are evidence too.

## Key Takeaways
1. Follow the loop: measure a baseline on a frozen test set, diagnose failures by cause, change one thing, and measure again.
2. Make at least two improvements that target the most common causes, and report every run, including changes that did not help.
3. The evaluation report states purpose, design choices, before-and-after metrics, cost per query, known failures and next steps.

## Hands-on Exercise
**Task:** Capstone step 2: evaluate, improve and deploy the assistant, and write a 2-page evaluation report.
**Tools:** Your capstone project from L15, your test set, retrieval and judge code, the anthropic SDK (paid; plan about 3–4 full runs of 30–50 questions), a hosting option. [VERSION]
**Steps:**
1. Freeze your test set and run the baseline; log it with `log_run`.
2. Classify failures and choose 2 improvements.
3. Apply each improvement separately, re-run, and log the results.
4. Check the judge against your own labels on 10 answers.
5. Deploy the best version and record its URL or a screen recording.
6. Write the 2-page report using the six-part structure above.
**What good looks like:** A results log with at least 3 runs, two improvements with measured effects, a deployed assistant, and a clear, honest report that a team lead could use to decide on next steps.
**Time:** about 150 minutes

## Review Flags
- [VERIFY] Licence of the example open-source documentation (course-level flag).
- [VERSION] Free hosting plans and their limits; Claude model choice and prices for estimating cost per query.
- Camila's results are hypothetical.
