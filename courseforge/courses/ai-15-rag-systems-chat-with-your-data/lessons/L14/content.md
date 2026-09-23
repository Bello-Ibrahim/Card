# L14 Cost, Latency and Deployment

Course: AI-15 · Module: M4 · Objectives: O6 · Video: 5 min (screen demo)

## Hook
Your assistant is accurate, but each answer takes eight seconds, and your manager asks what it will cost for a thousand users. You cannot answer either question by guessing. You need to measure where the time and money go in one query.

## Explanation
One RAG query has four main stages:

1. **Rewriting (optional):** one LLM call, small input and output.
2. **Embedding the question:** free when the model runs locally; usually a small share of total time on a CPU.
3. **Retrieval and reranking:** vector search is fast for course-sized collections; a cross-encoder reranker adds time for every candidate.
4. **Generation:** usually the largest share of both time and cost. Cost depends on **input tokens** (system prompt plus chunks plus question) and **output tokens** (the answer).

Measure each stage separately and read token counts from the API response:

```python
import os
import time

PRICE_IN = float(os.environ["PRICE_IN_PER_MTOK"])    # from the current pricing page [VERSION]
PRICE_OUT = float(os.environ["PRICE_OUT_PER_MTOK"])  # [VERSION]

def timed_answer(question, k):
    t0 = time.perf_counter()
    res = col.query(query_texts=[question], n_results=k)
    t1 = time.perf_counter()
    msg = client.messages.create(
        model=MODEL, max_tokens=400,  # MODEL: check the current models page
        system=SYSTEM_BLOCKS,
        messages=[{"role": "user", "content": build_prompt(question, res)}])
    t2 = time.perf_counter()
    u = msg.usage
    cost = (u.input_tokens * PRICE_IN + u.output_tokens * PRICE_OUT) / 1_000_000
    return {"retrieve_s": t1 - t0, "generate_s": t2 - t1,
            "in_tok": u.input_tokens, "out_tok": u.output_tokens, "cost": cost}
```

Prices change, so read them from configuration after checking the provider's pricing page; never write them into code. [VERSION]

**Levers you control:**

- **Top-k and chunk size:** more chunks usually raise recall but also input tokens, cost and latency, and can add distracting text. Choose k from your evaluation results, not by default.
- **max_tokens and answer style:** ask for short answers with citations; long answers cost more and take longer.
- **Prompt caching:** the system prompt and instructions are the same for every query. The API can cache a stable prompt prefix, so repeated requests process it at a lower cost and often faster. Mark the stable block with a cache control setting; minimum lengths and prices apply. [VERSION]

```python
SYSTEM_BLOCKS = [{"type": "text", "text": SYSTEM,
                  "cache_control": {"type": "ephemeral"}}]  # [VERSION]
```

- **Model size:** a smaller model may be good enough for rewriting or simple questions; test it on your test set.
- **Streaming:** from AI-14; it does not reduce total time, but users see the first words sooner.

**Deployment.** For a demo or internal tool, **Streamlit** gives a chat interface in a few lines of Python. For an application that other systems call, wrap your pipeline in a **FastAPI** endpoint:

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/ask")
def ask_endpoint(payload: dict):
    return answer_with_sources(payload["question"], role=current_role())
```

Keep the API key in an environment variable on the server, never in the browser. Free hosting plans exist but change often; check their limits for memory, sleep time and storage before you rely on them. [VERSION]

**Analogy:** Tuning cost and latency is like planning a delivery route. You time each part of the trip: loading, driving, waiting at the door. Only then can you decide whether a bigger van, fewer stops or a different route saves the most time and fuel.

## Worked Example
Tomás runs support tooling for a hypothetical online electronics shop in Rosario, Argentina. His RAG assistant answers staff questions about return and warranty policies.

On screen, follow his measurement:

1. He runs 20 test questions at k=3, k=5 and k=10 with `timed_answer` and saves the results.
2. He adds the hit@k and faithfulness scores he already has from L11 and L12.
3. His hypothetical table: k=3 has the lowest cost but misses answers that need two policies; k=5 raises hit rate clearly and adds about 40% more input tokens; k=10 adds almost no hit-rate gain but doubles the input tokens of k=5 and slows answers.
4. He chooses k=5, turns on prompt caching for the system prompt, and sets `max_tokens` to 400.
5. He deploys a Streamlit app on an internal server for 5 support staff, with the API key stored as a server environment variable.

## Common Mistake
Many teams measure only average latency and a rough cost from the pricing page. Averages hide slow queries, and real token counts include the system prompt, all chunks and the rewriting step. Record per-stage timings, report a slow-case figure such as the 90th percentile, and calculate cost from the usage numbers in API responses.

## Key Takeaways
1. Generation usually dominates cost and latency; local embeddings are free, and rerankers add time per candidate.
2. Choose top-k, chunk size, max_tokens and model size using your evaluation results together with measured cost and latency.
3. Cache the stable part of the prompt, read prices and model names from configuration, and deploy with Streamlit for demos or FastAPI for services.

## Hands-on Exercise
**Task:** Measure latency and estimated cost per query for 3 top-k settings, and choose one based on quality and cost.
**Tools:** Python 3, your pipeline, the anthropic SDK (paid; 20 questions × 3 settings), your L11 and L12 results. [VERSION]
**Steps:**
1. Add `timed_answer` to your pipeline and set current prices as environment variables.
2. Run 20 test questions at 3 top-k values.
3. Record median and slowest latency, average input and output tokens, and cost per query.
4. Add hit@k for each k from your L11 code.
5. Turn on prompt caching for the system prompt and re-run one setting.
6. Choose a k and write 3 sentences to justify it.
**What good looks like:** A table with quality, latency and cost for 3 settings, a caching comparison, and a choice justified by the numbers.
**Time:** about 45 minutes

## Review Flags
- [VERSION] Claude API prices, usage fields (`input_tokens`, `output_tokens`), prompt caching syntax, minimum cacheable length and cache pricing, and model names (course-level flag). [VERIFY] realistic cost per learner.
- [VERSION] Streamlit, FastAPI and free hosting plan limits.
- Tomás's figures are hypothetical.
