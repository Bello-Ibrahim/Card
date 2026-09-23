# L06 Validation, Errors and Retries

Course: AI-14 · Module: M2 · Objectives: O3, O5 · Video: 5 min (screen demo)

## Hook
Your extractor worked perfectly on five test invoices. On its first real day it met a 40-page invoice, a network timeout and an expired key. Code that talks to an API over the internet must expect failure and handle each kind in the right way.

## Explanation
Failures come from three places: the **response** is incomplete, the **request** fails, or the **output** does not pass your checks.

**1. Check the stop reason first.** A response with HTTP status 200 can still be unusable.

- `end_turn`: the model finished normally.
- `max_tokens`: the output was cut off at your limit. Structured output may be incomplete. Raise max_tokens, or shorten the task.
- `refusal`: the model declined the request. Show a clear message; do not retry the same input again and again.

Read the content only after you have checked `response.stop_reason`.

**2. Handle API errors by type.** The Python SDK raises a different exception class for each kind of error. Catch the specific classes first and the general ones last. [VERSION]

```python
import anthropic

try:
    response = client.messages.create(model=MODEL, max_tokens=500,
                                      messages=messages)
except anthropic.AuthenticationError:
    print("Invalid API key. Check ANTHROPIC_API_KEY.")      # do not retry
except anthropic.BadRequestError as e:
    print("Bad request:", e.message)                       # fix the request
except anthropic.RateLimitError:
    print("Rate limited. Try again later.")                # retry later
except anthropic.APIStatusError as e:
    print("API error", e.status_code)                      # 5xx: retry later
except anthropic.APIConnectionError:
    print("Network problem.")                              # retry later
```

**3. Use the SDK's automatic retries.** The SDK already retries connection errors, rate limits (429) and server errors (5xx) a small number of times, with growing waits between tries. You can change this with the `max_retries` client setting. Check the current default in the docs. [VERSION] Do not write your own retry loop around these errors unless you need different behaviour. Never retry authentication or bad-request errors: the same request will fail again and waste time.

**4. Retry a failed validation with the error included.** If the output fails your Pydantic or business checks, send one more request that includes the error message, so the model can correct itself. Limit this to one or two tries, then send the item to a human.

**Analogy:** Error handling is like a courier company's rules for failed deliveries. Nobody home: try again tomorrow (rate limit, server error). Wrong address: do not try again, send it back and ask for the right one (bad request, invalid key). Parcel damaged: repack it once and send again, then report it (validation retry).

## Worked Example
Sofia Petrova runs the invoice extractor for a logistics company in Sofia, Bulgaria. She wraps the L05 call in a function:

```python
from pydantic import ValidationError

def extract(text, attempts=2):
    content = f"<invoice>{text}</invoice>"
    for _ in range(attempts):
        r = client.messages.create(
            model=MODEL, max_tokens=500, system=SYSTEM,
            messages=[{"role": "user", "content": content}],
            output_config={"format": {"type": "json_schema",
                                      "schema": INVOICE_SCHEMA}},  # [VERSION]
        )
        if r.stop_reason == "max_tokens":
            raise RuntimeError("Output cut off. Raise max_tokens.")
        if r.stop_reason == "refusal":
            raise RuntimeError("Request declined by the model.")
        raw = next(b.text for b in r.content if b.type == "text")
        try:
            inv = Invoice.model_validate_json(raw)
            check_business_rules(inv)   # raises ValueError on a bad value
            return inv
        except (ValidationError, ValueError) as err:
            content += f"\nYour last answer failed a check: {err}. Fix it."
    return None   # send to human review
```

She tests three failures on screen:

1. **max_tokens = 10.** The stop reason is `max_tokens`, and the function stops with a clear message instead of saving half a record.
2. **An invalid key** (she sets the environment variable to a wrong value in one terminal). The SDK raises `AuthenticationError`, and her handler prints the key message. There are no retries.
3. **A malformed input**: a shopping list instead of an invoice. The total fails her "total greater than 0" check; the retry also fails, so the function returns `None` and the item goes to review.

## Common Mistake
Many developers wrap every call in `except Exception:` and retry three times. This hides the real problem: an invalid key is retried, a cut-off output is saved, and a model refusal is sent again and again. Check the stop reason, catch errors by class, let the SDK retry the temporary errors, and send permanent failures to a person.

## Key Takeaways
1. Always check `stop_reason` before reading content: `max_tokens` means cut-off output and `refusal` means the request was declined.
2. Catch API errors by class; let the SDK retry rate limits, server errors and connection errors, and never retry invalid keys or bad requests.
3. If validation fails, retry once or twice with the error message included, then send the item to human review.

## Hands-on Exercise
**Task:** Add error handling to your extractor and test it with a too-small max_tokens value, an invalid key and a malformed input.
**Tools:** Your L05 extractor; a terminal; the current SDK error-handling docs. [VERSION]
**Steps:**
1. Add a stop-reason check before you read the content.
2. Add an error handler with at least four exception classes, most specific first.
3. Add a validation retry that includes the error message, with a limit of 2 attempts.
4. Test 1: set max_tokens to 10 and run one invoice. Record what happens.
5. Test 2: in one terminal only, set `ANTHROPIC_API_KEY` to a wrong value and run again. Record the error class. Then restore the real key.
6. Test 3: send text that is not an invoice. Record whether it is rejected or sent to review.
7. Write a 3-row table: test, what happened, whether the behaviour is correct.
**What good looks like:** No test crashes with an unhandled error or saves a bad record. Each failure produces a clear message or goes to human review, and the table explains each result.
**Time:** about 35 minutes

## Review Flags
- [VERSION] SDK error class names, the default `max_retries` value, which status codes are retried automatically, and the structured-output parameter names must be checked against the current SDK docs.
- The test results in the worked example are hypothetical.
