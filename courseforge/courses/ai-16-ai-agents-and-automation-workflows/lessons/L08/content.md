# L08 Batches, Loops and Rate Limits

Course: AI-16 · Module: M2 · Objectives: O3, O5 · Video: 5 min (screen demo)

## Hook
Your workflow works on 10 rows. Then someone asks you to run it on 5,000. Will it finish? Will the API refuse some requests? And how much will it cost? You should know the answers before you press the button.

## Explanation
**Rate limits.** The Claude API limits how many requests and tokens you can use per minute. The limits depend on your account and change over time, so check them in the Claude Console and documentation. [VERSION] If you go above a limit, the API returns an error (HTTP status 429) instead of an answer. The API can also return temporary errors when it is busy.

n8n sends requests quickly when many items arrive at once, so a large sheet can reach a limit in seconds. Three tools help:

1. **Batching.** The **Loop Over Items** node (previously called Split in Batches) passes items to the next nodes in groups, for example 10 at a time. [VERSION] The HTTP Request node also has its own batching option. [VERSION]
2. **Waiting.** A **Wait** node after each batch pauses for a few seconds, which spreads requests over time.
3. **Retrying.** In the node settings, turn on **Retry On Fail** with a few tries and a wait between them. A temporary error then often succeeds on the next try. [VERSION] Error workflows come in L13.

**Estimate before you run.** Cost depends on tokens. Measure a small sample, then multiply:

- Run 10 to 20 representative rows and record input and output tokens per row.
- Average them: average tokens per row.
- Expected tokens = rows × average tokens per row, plus a safety margin for longer rows and retries.

Then compare the result with the current price list for your model to get a cost estimate. Prices change, so always look them up; do not copy them from an old note. [VERSION]

Also estimate time: time per batch × number of batches. If a run will take hours, use a schedule trigger and a "processed" column so a stopped run can continue where it ended instead of starting again.

**Analogy:** Batching is like a bank that opens one counter at a time for a long queue. If everyone rushes to the counter, the guard closes the door (the rate limit). If people come in groups of ten with a short pause, the queue moves steadily and everyone is served.

## Worked Example
Omar Haddad runs data operations for a hypothetical online electronics shop in Amman, Jordan. He must classify 500 product reviews. He does not start with 500. On screen, he:

1. Runs the classification workflow on 20 rows and reads the `usage` fields. He finds an average of about 400 input tokens and 40 output tokens per row (example output).
2. Calculates: 500 rows × 440 tokens = 220,000 tokens, plus a 20% margin for retries and long reviews = about 264,000 tokens.
3. Looks up the current price for his chosen model and multiplies to get an expected cost. He checks that it is below his spending limit. [VERSION]
4. Adds a **Loop Over Items** node with a batch size of 10 after the Google Sheets read node. [VERSION]
5. Inside the loop: HTTP Request to Claude (with Retry On Fail turned on), the validation Code node, Google Sheets update, then a **Wait** node of a few seconds, connected back to the loop. [VERSION]
6. Adds a `processed` column and filters it at the start, so only unprocessed rows are read.
7. Runs 50 rows, records the run time, and multiplies by 10 to estimate the time for 500.

## Common Mistake
Learners often estimate cost from a single, short test row, or forget output tokens and retries. The real run is then much larger than expected. Always measure a representative sample, include output tokens, add a margin, and set a spending limit in the console as a final safety net. Never state an expected cost to a manager without the date of the price list you used.

## Key Takeaways
1. Rate limits depend on your account; batches, waits and retries keep a large run within them.
2. Estimate usage before a big run: rows × average tokens per row from a real sample, plus a margin.
3. Use a "processed" column so a long run can stop and continue safely without repeating paid work.

## Hands-on Exercise
**Task:** Process 50 rows in batches of 10 with a wait between batches, record run time and token usage, then estimate the usage for 5,000 rows.
**Tools:** n8n self-hosted; Google Sheets; Claude API (keep within your spending limit).
**Steps:**
1. Create or copy 50 invented rows (reviews or emails). Do not use real customer data.
2. Add a `processed` column and a `tokens` column.
3. Build: trigger, Google Sheets (only unprocessed rows), Loop Over Items (batch size 10), HTTP Request (Retry On Fail on), validation, Google Sheets update, Wait, back to the loop. [VERSION]
4. Run it and write down the start and end time.
5. Sum the tokens and calculate the average per row.
6. Estimate the tokens and the time for 5,000 rows, with a margin, and write one sentence on how you would schedule that run.
**What good looks like:** All 50 rows are processed once, no rate-limit errors stop the run, and your estimate shows the calculation (rows × average, plus margin) instead of a guess.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Claude API rate limits depend on the account and change over time; the lesson states no specific limits. Confirm the rate-limit status code (429) and where limits are shown in the Claude Console.
- [VERSION] No prices are named; learners look up the current price list. The token figures in the worked example are invented example output.
- [VERSION] n8n Loop Over Items (Split in Batches), HTTP Request batching, Wait node and Retry On Fail settings must be checked against the current release.
