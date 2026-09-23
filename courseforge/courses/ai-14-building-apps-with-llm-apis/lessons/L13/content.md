# L13 Cost Control in Practice

Course: AI-14 · Module: M4 · Objectives: O2, O6 · Video: 5 min (screen demo)

## Hook
Your app sends the same 3,000-token system prompt with every question. A thousand questions a day means paying to send the same instructions a thousand times. Cost control starts with noticing what you pay for again and again.

## Explanation
There are five main levers. Use your usage log (L04) to find which one matters most for your app.

**1. Prompt caching for repeated context.** If the start of your request is the same every time (tools, system prompt, a long document), you can mark it for caching. The first request writes it to a cache; later requests within a short time read it from the cache at a much lower price. Cached content must be an exact match from the start of the request, so put stable content first and changing content, such as the user's question, last. There is a minimum length for caching, a limited cache lifetime and a small extra charge for writing to the cache. Check the current rules and discounts. [VERSION]

```python
response = client.messages.create(
    model=MODEL,
    max_tokens=400,
    system=[{"type": "text", "text": LONG_SYSTEM_PROMPT,
             "cache_control": {"type": "ephemeral"}}],   # [VERSION]
    messages=[{"role": "user", "content": question}],
)
u = response.usage
print(u.input_tokens, u.cache_creation_input_tokens, u.cache_read_input_tokens)
```

**2. Batch processing for jobs that can wait.** The Message Batches API accepts many requests at once and returns results later, for about 50% of the normal price. It suits nightly reports, bulk extraction and eval runs, not live chat. Results can arrive in any order, so match them by your own `custom_id`. [VERSION]

**3. Send easy tasks to a smaller model.** Classification, short extraction and routing often work well on a smaller, cheaper model. Keep the larger model for tasks where your eval set shows it is needed.

**4. Output limits.** Output tokens usually cost more than input tokens. Set max_tokens per feature, and ask for short answers in the prompt when that is what users need.

**5. Per-user quotas.** Limit messages or tokens per user per day, so one user or a bot cannot spend your whole budget.

**Measure quality before and after.** A cheaper setup that fails more cases is not cheaper per useful answer. Run your eval set (L12) after every change and compare pass rate and cost together.

**Analogy:** Cost control is like reducing a restaurant's food bill. You buy staple ingredients in bulk when they keep (batching), prepare the base sauce once in the morning instead of for every plate (caching), give simple dishes to the junior cook (smaller model), serve sensible portions (output limits), and limit free refills (quotas). You still taste every dish before it goes out (evals).

## Worked Example
Aroha Ngata builds a study helper for a tutoring company in Wellington, New Zealand. Every request includes a 3,500-token system prompt with the course rules and examples. She follows these steps on screen:

1. She sends the same question twice without caching and logs usage.
2. She adds `cache_control` to the system prompt block, as in the code above, and sends two different questions within a minute.
3. She compares the usage fields. Example output:

```text
No cache, call 1:   input 3620, cache write 0,    cache read 0
No cache, call 2:   input 3615, cache write 0,    cache read 0
With cache, call 1: input 120,  cache write 3500, cache read 0
With cache, call 2: input 115,  cache write 0,    cache read 3500
```

4. She calculates the cost of each call with the current prices for normal input, cache writes and cache reads, and adds them to her cost helper. [VERSION]
5. She runs her eval set with caching on. The pass rate is unchanged, because caching does not change what the model sees.

She also moves her nightly "summarise today's questions" report to the Batch API, and sends simple topic classification to a smaller model after checking it on 20 cases.

## Common Mistake
Many developers add caching but put something that changes on every request, such as the current time or the user's name, at the start of the system prompt. The prefix is then never the same, and every call writes to the cache instead of reading from it, which can cost more than no caching at all. Put stable content first, and check that `cache_read_input_tokens` is above zero on repeated calls.

## Key Takeaways
1. Use prompt caching for long, stable context at the start of the request, and confirm cache reads in the usage fields.
2. Use batch processing for work that can wait, a smaller model for easy tasks, and output limits and per-user quotas everywhere.
3. Measure quality with your eval set before and after each cost change, and compare cost per useful answer.

## Hands-on Exercise
**Task:** Apply prompt caching to a request with a long system prompt, and compare the cached and uncached token usage and cost.
**Tools:** Your L02 setup and L04 cost helper; the current prompt-caching and pricing docs. [VERSION]
**Steps:**
1. Write or reuse a system prompt that is long enough to be cached (check the current minimum length). [VERSION]
2. Send 3 different questions without caching, and log usage for each.
3. Add `cache_control` to the system prompt block and send the same 3 questions within a few minutes.
4. Record input tokens, cache write tokens and cache read tokens for all 6 calls.
5. Extend your cost helper with the current cache write and cache read prices, and calculate the cost of each call. [VERSION]
6. Write 3 sentences: how much you saved, after how many calls caching paid off, and one other lever that would suit your app.
**What good looks like:** A table of 6 calls where the cached calls after the first show cache reads, correct cost calculations for both setups, and a short, number-based conclusion.
**Time:** about 35 minutes

## Review Flags
- [VERSION] Prompt caching syntax, minimum cacheable length, cache lifetime, cache write and read prices, the usage field names, and the Batch API discount (about 50%) and rules must be checked against the current docs.
- The token numbers in the worked example are illustrative.
