# L08 Batches, Loops and Rate Limits | Presenter Script

Course: AI-16 · Video: 5 min · Words: 679

## Hook
Your workflow works on ten rows. Then someone asks you to run it on five thousand. Will it finish? Will the API refuse some requests? And how much will it cost? You should know the answers before you press the button.

## Explain
Last time, we routed each message to the right place. Now we scale up. The Claude API limits how many requests and tokens you can use per minute. The limits depend on your account and change over time, so check them in the Claude Console. If you go over a limit, the API returns an error instead of an answer. It can also return temporary errors when it is busy.

n8n sends requests quickly when many items arrive at once, so a large sheet can hit a limit in seconds. Three tools help. Batching passes items on in small groups, for example ten at a time. Waiting pauses for a few seconds after each batch. And retrying tries a failed request again, after a short wait.

Here is a picture. Think of a bank with one counter and a long queue. If everyone rushes in at once, the guard closes the door. If people come in groups of ten, with a short pause, the queue moves steadily and everyone is served.

Next, estimate before you run. Cost depends on tokens. Run ten to twenty typical rows, and record the tokens per row. Take the average. Then multiply by the number of rows, and add a safety margin for longer rows and retries. Compare that with the current price list for your model. Prices change, so always look them up.

Also estimate time: time per batch, multiplied by the number of batches. If a run will take hours, use a schedule trigger, and a processed column, so a stopped run can continue where it ended, instead of starting again.

## Demonstrate
Let's see it. Omar Haddad runs data operations for an online electronics shop in Amman, Jordan. He must classify five hundred product reviews. He does not start with five hundred. He runs twenty rows, and reads the usage fields. You'll see something like four hundred input tokens and forty output tokens per row.

He calculates. Five hundred rows times four hundred and forty tokens is two hundred and twenty thousand tokens. He adds a twenty percent margin, so about two hundred and sixty-four thousand. He looks up the current price for his model, and checks that the cost is below his spending limit.

Now he adds a Loop Over Items node, with a batch size of ten, after the Sheets read node. Inside the loop, the call to Claude has retry on fail turned on. Then come the validation node, the sheet update, and a Wait node of a few seconds, connected back to the loop.

He adds a processed column, and filters on it at the start, so only unprocessed rows are read. Then he runs fifty rows, notes the run time, and multiplies by ten to estimate the time for all five hundred.

A common mistake is to estimate from one short test row, or to forget output tokens and retries. The real run is then much larger than expected. Measure a typical sample, add a margin, and keep a spending limit as a final safety net. And when you share an estimate, include the date of the price list you used.

## Recap
Let's recap. First, rate limits depend on your account. Batches, waits and retries keep a large run within them. Second, estimate usage before a big run, from a real sample, plus a margin. Third, use a processed column, so a long run can stop and continue safely, without repeating paid work.

## CTA
Now it is your turn. In the exercise below this video, you will process fifty rows in batches of ten, with a wait between batches. Record the run time and token usage, then estimate the usage for five thousand rows. It takes about forty minutes. In the next lesson, we move to agents, with Tool Use: Letting the Model Call Functions. See you there.

## Thumbnail
Headline: Ready for 5,000 Rows?
Image: Navy background, a long stack of spreadsheet rows split into neat teal groups of ten with small pause icons between them, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API rate limits depend on the account and change over time; the lesson states no specific limits. The voiceover says only that the API 'returns an error'; confirm the rate-limit status code (429) and where limits are shown in the Claude Console before it appears on any slide.
- [VERSION] No prices are named in the voiceover or on screen; learners look up the current price list. The token figures in the worked example (about 400 input and 40 output tokens per row) are invented example output and are introduced with 'you'll see something like'.
- [VERSION] n8n Loop Over Items (Split in Batches), HTTP Request batching, Wait node and Retry On Fail settings must be checked against the current release.
- Screen recording: when Omar looks up the price, show the pricing page only briefly and blurred, or cut to the calculation; no figures on screen.
- Omar Haddad and his Amman electronics shop are fictional; the 500 reviews are invented.
