# HeyGen Batch Pack: AI-16 M2 (Adding AI to Workflows)

Course: AI Agents and Automation Workflows. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L05 Calling the Claude API from n8n

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M2_L05_presenter.mp4`
- **Expected length:** about 4.9 minutes (681 words). The quality gate accepts ±10%.

```text
Your workflow can already read and write a sheet. Now it gets a new ability: understanding language. One extra node lets it summarise, classify, or pull out information from every row.

A quick reminder. An API request is a message to a server, with a method, an address, some headers and a body. The server sends back a response, usually in JSON.

To call Claude, you send a POST request to the Messages address. It has three headers: your secret API key, the API version from the documentation, and the content type.

The body names the model, sets a limit on output length, adds an optional system prompt, and holds the messages. For the model, check the current models page in the Claude documentation. Smaller, faster models are often enough for summaries.

The response gives you the text, the reason it stopped, and a usage section with input and output tokens. Tokens are what you pay for.

Here is a picture. Calling the API is like posting a form to a translation office. The envelope has an address, and stamps that prove who you are and which form version you use. Inside is the form itself. The office sends back the translation, with an invoice for how much work it did.

In n8n, you have two ways to make this call. The HTTP Request node lets you set the method, address, headers and body yourself. It shows exactly what is sent, so we use it today. There are also built-in Anthropic model nodes that hide these details. We use one with the AI Agent node later in the course.

The Claude API is a paid, usage-based service. So before you start, set a spending limit in the Claude Console. Keep test runs to a few rows, and always limit output length. Store your key in an n8n credential, never in a node. And use sample data, not personal or confidential data.

Let's build it. Mei-Lin Chen runs a tea shop in Taipei. Her reviews sheet has five invented reviews, with empty summary and tokens columns. First, she creates an API key in the Claude Console, and sets a monthly spending limit.

In n8n, she creates a header credential called Claude API, with the key as its value. Then she builds a manual trigger, and a Sheets node that gets rows from reviews.

Next, an HTTP Request node. She sets the method to POST, pastes the Messages address, and picks her Claude API credential. She adds the other two headers, and the body with her system prompt.

She runs it with a single row first. In the output, you'll see something like: the customer liked the oolong, but found the delivery slow. You also see the token usage.

Then she adds a Set node. It takes the summary text, adds the input and output tokens together, and keeps the review ID. Finally, a Sheets node updates the rows, matching on review ID. She removes the one-row limit and runs all five. Her sheet now has five summaries, and a token count for each row.

A common mistake is to test on the whole sheet first. If the prompt has an error, every row gets the wrong prompt, and you pay for every call. Test with one item, check it, then run the full set.

Let's recap. First, a Claude API call is a POST request to the Messages address, with three headers and a body that holds the model, the output limit, the system prompt and the messages. Second, store the key in an n8n credential, and read the usage from the response. Third, the API is paid per use. Set a spending limit, limit output length, and test with one row first.

Now it is your turn. In the exercise below this video, you will send five customer reviews to the Claude API, write a one-sentence summary of each back to your sheet, and record the tokens the run used. It takes about forty minutes. In the next lesson, we cover Structured Output: Getting JSON You Can Trust. See you there.
```

## L06 Structured Output: Getting JSON You Can Trust

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M2_L06_presenter.mp4`
- **Expected length:** about 4.8 minutes (677 words). The quality gate accepts ±10%.

```text
A summary is nice to read, but a workflow cannot make decisions from a paragraph. It needs fields: category, urgency, language. Today, you make the model return data the next node can use, and you check it before anything depends on it.

Last time, the model gave us one sentence per review. Now we want structured output. That means asking the model for a fixed shape, usually JSON, instead of free text. You describe the shape in the system prompt, and give one example.

Three habits help. Use a short, closed list of allowed values for each field. Include an other or not sure value, so the model is not forced to guess. And ask for JSON only, with no explanation around it. The Claude API also offers stronger methods, so check the current documentation for the recommended one.

But even with a good prompt, never trust the output without checking it.

The model can add text before the JSON, use a value outside your list, or leave out a field. So you add a validation step in a Code node, before any other node uses the result. It tries to read the JSON safely. It checks each field against your allowed values. And it marks the item as valid or not valid.

Then an IF node sends valid items forward, and invalid items to a needs review tab. A simple rule for invalid output: retry once, then send it to review. Do not retry many times. Each retry costs money, and if the model fails twice on the same email, a person should look at it.

Think of the receiving desk in a warehouse. Every delivery is checked against the order form. A box that does not match goes to a separate shelf, for a person to inspect. It never goes straight onto the shop floor.

Let's build it. Beatriz Carvalho manages guest services at a hotel in Lisbon, Portugal. Guests write in Portuguese, English, French and Spanish. She wants each email sorted by category, urgency and language, so the right person sees it first. She uses ten invented emails. Her sheet has three tabs: emails, classified, and needs review.

In n8n, she builds a manual trigger, a Sheets node that reads the emails, and an HTTP Request to Claude, with the system prompt and a small output limit.

Next, she adds the validation Code node. For one email, you'll see something like: category complaint, urgency high, language French, and valid set to true.

She adds an IF node on valid. Valid items go to the classified tab. Invalid items get one retry, with a note that says the last answer was not valid JSON. If the second check fails too, the item goes to needs review, with its original text.

Now she tests the edges. An email that says only question marks comes back as category other, which is valid. A very long email that mixes three languages lands in needs review, which is exactly where it should go.

A common mistake is to read the JSON in the next node with no error handling. Then, when the model adds a line like here is the JSON, the whole workflow stops, and the other items are never processed. Always read the JSON safely, mark the item as invalid, and route it. One bad item should never stop the batch.

Let's recap. First, ask for a fixed JSON shape, with closed lists of allowed values and an other or not sure option. Second, validate every result in a Code node before other nodes use it. Third, for invalid output, retry once, then send the item to a needs review list for a person.

Now it is your turn. In the exercise below this video, you will classify ten sample emails as JSON, validate each one, and send invalid results to a separate tab. You will also break the prompt on purpose, and check that the workflow keeps running. It takes about forty-five minutes. In the next lesson, we look at Routing and Decisions. See you there.
```

## L07 Routing and Decisions

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M2_L07_presenter.mp4`
- **Expected length:** about 4.9 minutes (682 words). The quality gate accepts ±10%.

```text
Your workflow can now label every message. But a label is only useful if something happens next. Who sees the urgent complaint? Who answers the simple question? And what happens when the model is not sure?

Last time, we made the model return fields we can trust. Now we use them. Routing means sending each item down a different path, based on its data. n8n has two main nodes for this.

The IF node checks one condition, and has two outputs, true and false. The Switch node has several rules, and several outputs. For example, one output each for complaint, question and booking, plus a fallback for anything else.

Remember the key idea from lesson one. The model produces the label. Your workflow makes the decision. That keeps the path predictable, and easy to test.

Before you ask the model, ask yourself: can a simple rule decide this? An email from a known internal address can be routed by sender. A policy number in a fixed format can be found with a pattern. An amount above a limit is just a comparison. Rules are free, instant, and always give the same answer. So put them first, and send only the rest to the model.

Next, plan for uncertainty. Give the model a way to say it is not sure. Add a not sure category, or a confidence field, and route low confidence to a person. But a model's own confidence is only a rough signal, so check it against your test results.

Think of the triage desk in a hospital. Clear cases go straight to the right team. A patient who cannot be assessed quickly is not sent to a random ward. A senior nurse sees them. And some checks follow a fixed rule, and need no discussion.

Let's build it. Andrea Santos leads customer care at an insurance company in Manila, the Philippines. Claim messages arrive in English and Filipino. She uses twenty invented messages, and starts from the classification workflow from the last lesson.

First, a rule. Before the model call, she adds an IF node. If a message has a claim number in the standard format and the word status, it goes to an automatic status reply. No AI is needed.

The other messages go to Claude, with five categories: new claim, claim status, complaint, document question, and not sure, plus an urgency field. Then she adds a Switch node on the category, with one output per value, and a fallback.

She connects the outputs. High-urgency complaints go to an urgent complaints tab. Document questions go to a second Claude call that drafts a reply into a drafts tab. Nothing is sent. Not sure items and the fallback both go to review.

She runs all twenty, and checks the count in each tab. One message says: my car was hit, the other driver's insurer says you pay, and I also want to cancel my policy. You'll see something like not sure, so it goes to review. Andrea agrees. It needs a person.

A common mistake is to route on a free-text label, like complaint, urgent, in brackets. A small change in wording breaks the rules, and items fall into no path at all. Route only on values from a closed list, and always connect the fallback to a review tab, so no item is lost.

Let's recap. First, use IF for one condition and Switch for several. The model labels the item, and the workflow decides the path. Second, use a plain rule before the model whenever a rule can decide. Third, give the model a not sure option, and send those items, plus any fallback items, to a person.

Now it is your turn. In the exercise below this video, you will extend your email workflow so that urgent complaints, simple questions and unclear messages each go to the right place. Then list the decisions a rule could make without AI, and move one of them before the model. It takes about forty-five minutes. In the next lesson, we cover Batches, Loops and Rate Limits. See you there.
```

## L08 Batches, Loops and Rate Limits

- **Filename:** `ai-16-ai-agents-and-automation-workflows_M2_L08_presenter.mp4`
- **Expected length:** about 4.9 minutes (678 words). The quality gate accepts ±10%.

```text
Your workflow works on ten rows. Then someone asks you to run it on five thousand. Will it finish? Will the API refuse some requests? And how much will it cost? You should know the answers before you press the button.

Last time, we routed each message to the right place. Now we scale up. The Claude API limits how many requests and tokens you can use per minute. The limits depend on your account and change over time, so check them in the Claude Console. If you go over a limit, the API returns an error instead of an answer. It can also return temporary errors when it is busy.

n8n sends requests quickly when many items arrive at once, so a large sheet can hit a limit in seconds. Three tools help. Batching passes items on in small groups, for example ten at a time. Waiting pauses for a few seconds after each batch. And retrying tries a failed request again, after a short wait.

Here is a picture. Think of a bank with one counter and a long queue. If everyone rushes in at once, the guard closes the door. If people come in groups of ten, with a short pause, the queue moves steadily and everyone is served.

Next, estimate before you run. Cost depends on tokens. Run ten to twenty typical rows, and record the tokens per row. Take the average. Then multiply by the number of rows, and add a safety margin for longer rows and retries. Compare that with the current price list for your model. Prices change, so always look them up.

Also estimate time: time per batch, multiplied by the number of batches. If a run will take hours, use a schedule trigger, and a processed column, so a stopped run can continue where it ended, instead of starting again.

Let's see it. Omar Haddad runs data operations for an online electronics shop in Amman, Jordan. He must classify five hundred product reviews. He does not start with five hundred. He runs twenty rows, and reads the usage fields. You'll see something like four hundred input tokens and forty output tokens per row.

He calculates. Five hundred rows times four hundred and forty tokens is two hundred and twenty thousand tokens. He adds a twenty percent margin, so about two hundred and sixty-four thousand. He looks up the current price for his model, and checks that the cost is below his spending limit.

Now he adds a Loop Over Items node, with a batch size of ten, after the Sheets read node. Inside the loop, the call to Claude has retry on fail turned on. Then come the validation node, the sheet update, and a Wait node of a few seconds, connected back to the loop.

He adds a processed column, and filters on it at the start, so only unprocessed rows are read. Then he runs fifty rows, notes the run time, and multiplies by ten to estimate the time for all five hundred.

A common mistake is to estimate from one short test row, or to forget output tokens and retries. The real run is then much larger than expected. Measure a typical sample, add a margin, and keep a spending limit as a final safety net. And when you share an estimate, include the date of the price list you used.

Let's recap. First, rate limits depend on your account. Batches, waits and retries keep a large run within them. Second, estimate usage before a big run, from a real sample, plus a margin. Third, use a processed column, so a long run can stop and continue safely, without repeating paid work.

Now it is your turn. In the exercise below this video, you will process fifty rows in batches of ten, with a wait between batches. Record the run time and token usage, then estimate the usage for five thousand rows. It takes about forty minutes. In the next lesson, we move to agents, with Tool Use: Letting the Model Call Functions. See you there.
```
