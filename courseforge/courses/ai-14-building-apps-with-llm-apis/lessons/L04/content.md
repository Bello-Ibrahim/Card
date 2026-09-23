# L04 Tokens, Context and Cost

Course: AI-14 · Module: M1 · Objectives: O2, O6 · Video: 5 min (screen demo)

## Hook
Two apps use the same model and answer the same number of questions each day. One costs ten times more than the other. The difference is not the model. It is how many tokens each app sends and receives.

## Explanation
Every response includes a `usage` object. The two fields you need first are:

- `usage.input_tokens`: tokens you sent (system prompt, messages, tool definitions).
- `usage.output_tokens`: tokens the model wrote.

When you use prompt caching (L13), you will also see cache fields in `usage`.

**The cost formula.** Prices are listed per million tokens, and output tokens usually cost more than input tokens. For one call:

cost = input_tokens × input price ÷ 1,000,000 + output_tokens × output price ÷ 1,000,000

Prices differ by model and change over time, so read them from the pricing page and keep them in one place in your code. [VERSION]

**Counting before you send.** The API has a token-counting endpoint. You pass the same model, system prompt and messages, and it returns the input token count without generating a reply. Use it to check that a long document fits in the context window, or to warn a user before an expensive request. Check the current docs for its limits and pricing. [VERSION]

```python
count = client.messages.count_tokens(
    model=MODEL, system=SYSTEM, messages=messages
)
print(count.input_tokens)
```

**Longer context costs more and is slower.** Every token in the request is processed, so a 20,000-token document costs more and usually takes longer than a 500-token question. In a chat app, the history grows with every turn (L01). Common fixes are: send only the parts of a document that matter, keep the last few turns of a long chat, and keep max_tokens close to what you really need.

**Different languages, different token counts.** A tokenizer splits text into pieces that it saw often during training. The same meaning can therefore need a different number of tokens in different languages and scripts. Measure this with the token counter for your own languages instead of guessing. [VERIFY]

**Analogy:** Tokens are like the words a taxi meter counts instead of kilometres. The meter runs while you speak (input) and faster while the driver speaks (output). Reading a long letter aloud at the start of every ride makes every ride expensive, even if your question is short.

## Worked Example
Farida runs a language-learning app in Cairo, Egypt. Learners ask grammar questions in English or Arabic. She adds a helper that logs every call:

```python
import csv, time

# Prices per million tokens: copy from the pricing page [VERSION]
PRICE_IN = 0.0
PRICE_OUT = 0.0

def log_call(response, feature, path="usage_log.csv"):
    u = response.usage
    cost = (u.input_tokens * PRICE_IN + u.output_tokens * PRICE_OUT) / 1_000_000
    with open(path, "a", newline="") as f:
        csv.writer(f).writerow([time.strftime("%Y-%m-%d %H:%M:%S"), feature,
                                response.model, u.input_tokens,
                                u.output_tokens, round(cost, 6)])
    return cost
```

She sends the same grammar question in English and in Arabic, with the same system prompt and max_tokens. Example output from her log:

```text
2026-09-01 10:02:11, grammar, <model>, 212, 180, 0.00xxxx
2026-09-01 10:02:15, grammar, <model>, 241, 205, 0.00xxxx
```

In her test, the Arabic version used more tokens for the same meaning (example numbers). She decides to measure a sample of real questions in each language before she sets prices for her premium plan. She also notices that her 600-token system prompt is sent with every call, and she makes a note to try prompt caching in L13.

## Common Mistake
Many developers estimate cost from the length of the user's question only. In a real app, most input tokens often come from the parts the user never sees: the system prompt, examples, the chat history and any documents. Always read `usage` from real responses, log it, and calculate cost from the logged numbers, not from guesses.

## Key Takeaways
1. Cost per call = input tokens × input price + output tokens × output price, with prices per million tokens taken from the live pricing page.
2. Longer context means higher cost and slower replies, so send only what the model needs and keep max_tokens realistic.
3. Token counts for the same meaning can differ between languages, so measure your own languages with the token counter.

## Hands-on Exercise
**Task:** Write a helper that logs tokens and estimated cost for every call, and compare the cost of the same request in English and one other language.
**Tools:** Your L02 setup; the pricing page; a CSV file or spreadsheet.
**Steps:**
1. Copy the current input and output prices for your development model from the pricing page into two constants. [VERSION]
2. Write a `log_call()` helper like the worked example, and call it after every request.
3. Write one request in English, for example "Explain in 3 sentences how to save energy at home."
4. Translate it into one other language you know (or use a translation tool). Do not include personal data.
5. Use the token counter to count input tokens for both versions before sending. [VERSION]
6. Send both requests with the same system prompt and max_tokens, and log both.
7. Calculate the difference in input tokens, output tokens and cost, in numbers and as a percentage.
**What good looks like:** A working helper, a CSV file with at least two logged calls, the counted and actual input tokens for each language, and two or three sentences that explain the difference you found.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Prices per model, the token-counting endpoint, its SDK method and any limits or pricing for it must be checked against the current docs at recording time.
- [VERIFY] The claim that the same meaning can use different token counts in different languages must be checked with the current tokenizer; the numbers in the worked example are illustrative.
