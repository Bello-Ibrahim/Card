# L05 Calling the Claude API from n8n

Course: AI-16 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Your workflow can already read and write a sheet. Now it gets a new ability: understanding language. One extra node lets it summarise, classify or extract information from every row.

## Explanation
Quick recap: an API request is a message to a server with a method, an address, headers and a body. The server sends back a response, usually JSON.

To call Claude you send a POST request to the Messages endpoint, `https://api.anthropic.com/v1/messages`, with three headers:

- `x-api-key`: your secret API key.
- `anthropic-version`: the API version string from the documentation. [VERSION]
- `content-type`: `application/json`.

The body contains the model, a limit on output length, an optional system prompt and the messages:

```json
{
  "model": "MODEL",
  "max_tokens": 150,
  "system": "You summarise customer reviews in one neutral sentence.",
  "messages": [
    {"role": "user", "content": "Review: {{ $json.review }}"}
  ]
}
```

Replace `MODEL` with a current model ID: check the current models page in the Claude documentation. [VERSION] Smaller, faster models are usually cheaper and are often enough for summaries.

The response contains a `content` list (the text is in `content[0].text`), a `stop_reason` and a `usage` object with `input_tokens` and `output_tokens`. Tokens are what you pay for.

In n8n you have two options:

- **HTTP Request node:** you set the method, URL, headers and JSON body yourself. It shows exactly what is sent, so we use it in this lesson. [VERSION]
- **Anthropic chat model nodes:** built-in nodes that hide the request details. We use one with the AI Agent node in L10. [VERSION]

If you prefer code outside n8n, the official `anthropic` SDK does the same:

```python
import anthropic
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
msg = client.messages.create(model="MODEL", max_tokens=150,
    messages=[{"role": "user", "content": "Summarise: ..."}])
print(msg.content[0].text, msg.usage)
```

**Cost and safety.** The Claude API is a paid, usage-based service; do not assume a free tier. [VERSION] Before you start, set a spending limit in the Claude Console, keep test runs to a few rows, and set `max_tokens` so a reply cannot grow without limit. Never paste your API key into a node's body or a shared workflow: store it in an n8n credential. Do not send personal or confidential data to the API during the course; use sample data.

**Analogy:** Calling the API is like sending a form to a translation office by post. The envelope has an address (the URL) and stamps that prove who you are and which form version you use (the headers). Inside is the form itself (the body). The office sends back the translation with an invoice that shows how many words it handled (the usage).

## Worked Example
Mei-Lin Chen runs a hypothetical tea shop in Taipei. She has a sheet "reviews" with columns `review_id`, `review`, `summary` and `tokens`, filled with 5 invented reviews. On screen, she:

1. Creates an API key in the Claude Console and sets a monthly spending limit. [VERSION]
2. In n8n, creates a **Header Auth** credential named "Claude API" with the name `x-api-key` and her key as the value. [VERSION]
3. Builds: Manual Trigger, then Google Sheets (get rows) from "reviews".
4. Adds an **HTTP Request** node: method POST, the Messages URL, authentication set to the "Claude API" credential, two more headers (`anthropic-version`, `content-type`), and the JSON body above. [VERSION]
5. Runs the node with a single row first. The output shows `content[0].text`: "The customer liked the oolong but found the delivery slow." (example output)
6. Adds an **Edit Fields (Set)** node that creates `summary` = `{{ $json.content[0].text }}` and `tokens` = input plus output tokens. She also keeps `review_id` from the sheet node so she can match rows. [VERSION]
7. Adds Google Sheets (update rows, match on `review_id`) and runs all 5 rows.

Her sheet now has 5 summaries and a token count for each row.

## Common Mistake
Learners often test with the whole sheet on the first run. If the prompt has a mistake, every row is processed with the wrong prompt and every call is paid for. Test with one item first (n8n can limit items, or you can use a sheet with a few rows), check the output, and only then run the full set.

## Key Takeaways
1. A Claude API call is a POST to /v1/messages with the x-api-key, anthropic-version and content-type headers and a body with model, max_tokens, system and messages.
2. Store the API key in an n8n credential, use a MODEL placeholder that you fill from the current models page, and read usage from the response.
3. The API is paid per use: set a spending limit, limit output length and test with one row first.

## Hands-on Exercise
**Task:** Send 5 customer reviews from a sheet to the Claude API, write a one-sentence summary of each back to the sheet, and record the token usage.
**Tools:** n8n self-hosted; Google Sheets; a Claude API key with a spending limit (paid, usage-based).
**Steps:**
1. Create a "reviews" sheet with 5 invented reviews and empty `summary` and `tokens` columns.
2. Create an API key and set a spending limit in the Claude Console. [VERSION]
3. Store the key in an n8n Header Auth credential. [VERSION]
4. Build the workflow from the worked example and run it on one row.
5. Check the summary, then run all 5 rows.
6. Add the token counts and write the total at the bottom of your notes.
**What good looks like:** Five accurate, one-sentence summaries in the sheet, a token count for each row, no API key visible in any node, and a note of the total tokens for the run.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Claude API: the `anthropic-version` header value, the request and response fields (`content[0].text`, `stop_reason`, `usage`), the current model IDs for the MODEL placeholder, the `anthropic` SDK call, and the Claude Console steps for API keys and spending limits must be checked against current documentation. No free tier is assumed and no prices are named.
- [VERSION] n8n: HTTP Request node options, Header Auth credential, Anthropic chat model node names and Edit Fields (Set) expressions must be checked against the current release.
