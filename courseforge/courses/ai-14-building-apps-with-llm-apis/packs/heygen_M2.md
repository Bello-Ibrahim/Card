# HeyGen Batch Pack: AI-14 M2 (Structured Outputs and Streaming)

Course: Building Apps with LLM APIs. Make one HeyGen video per lesson below, using these settings for every video.

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

## L05 Structured Outputs with JSON Schemas

- **Filename:** `ai-14-building-apps-with-llm-apis_M2_L05_presenter.mp4`
- **Expected length:** about 5.0 minutes (692 words). The quality gate accepts ±10%.

```text
Your code asks the model for an invoice total. The model replies, sure, the total appears to be around four thousand five hundred rupees. But your code needs a number and a currency code. A friendly sentence is useless to a database.

In the last lesson, you learned to measure what each call costs. Now let's make the output useful to code. Free text is good for people and bad for programs. When another part of your program reads the result, you need structured output. That means data with fixed fields and types that your code can trust.

There are three steps. Step one, define a schema. It lists the fields, their types, and which ones are required. In Python, the usual tool is Pydantic. You write a small class, and Pydantic turns it into a JSON schema and checks data against it. In TypeScript, Zod does the same job.

Step two, ask the API for output that matches the schema. The Claude API has a structured-output feature. The Python SDK has a helper that takes your Pydantic class and gives you back a parsed object. Names of these settings change between versions, so check the current docs.

There is also an older, widely used option. You define a tool whose input schema is your schema, and read the tool's input. Lesson nine explains tools.

Step three, still validate in your code. The schema controls the shape, not the truth. The model can read the wrong number from a blurred invoice. So add business checks. Is the total positive? Is the date not in the future? And say clearly what to do with missing values, for example use null, and make that field optional.

Asking for free text is like asking a colleague to tell you about an invoice by phone. Structured output is like handing them a printed form with labelled boxes. It is easy to file, but you still check the numbers in the boxes.

Priya works on an accounting tool in Bengaluru, India. It reads supplier invoices from India, Mexico and Germany, each with a different layout and date format.

She opens her extractor. At the top is the Invoice class. The system prompt tells the model to convert all dates to one standard format, and to use standard currency codes. The invoice text goes inside tags, as you learned in lesson three.

The call uses the parse helper, with the Invoice class as the output format. The result is an Invoice object, not a string. She runs it on the Mexican invoice. You'll see something like the supplier name, the date in standard format, the total as a number, and the Mexican peso code.

She saves the object straight to the database. No string searching, and no regular expressions. Then she tests a German invoice, where the total uses a comma for decimals. The first result is wrong. The schema was valid, but the value was not.

So she adds a rule to the system prompt about comma decimals, and a business check that flags very small totals for human review. She runs it again, and the total is now correct.

A common mistake is to write reply only with JSON in the prompt, parse the text, and hope. Usually it works. Sometimes there is extra text or a missing field, and the app crashes. Use the structured-output feature, and never pull out fields with string matching.

Let's recap. First, define your output as a schema, with Pydantic in Python or Zod in TypeScript, so your code receives fixed fields and types. Second, use the API's structured-output feature, or a tool with an input schema, and parse the result into an object. Third, a valid schema does not mean correct values, so add business checks and a clear rule for missing data.

Now it is your turn. In the exercise, you will build an invoice extractor that returns validated objects for five invented invoices in different formats, with two business checks. You will reuse this schema idea in your capstone. In the next lesson, Validation, Errors and Retries, you will make it survive real failures. See you there.
```

## L06 Validation, Errors and Retries

- **Filename:** `ai-14-building-apps-with-llm-apis_M2_L06_presenter.mp4`
- **Expected length:** about 5.0 minutes (692 words). The quality gate accepts ±10%.

```text
Your extractor worked perfectly on five test invoices. On its first real day, it met a forty-page invoice, a network timeout and an expired key. Code that talks to an API must expect failure, and handle each kind in the right way.

In the last lesson, you built an invoice extractor. Now let's make it robust. Failures come from three places. The response is incomplete, the request fails, or the output does not pass your checks.

First, check the stop reason before you read anything. A successful response can still be unusable. End turn means the model finished. Max tokens means the output was cut off, so structured data may be incomplete. Refusal means the model declined. Show a clear message, and do not retry the same input again and again.

Second, handle API errors by type. The Python SDK raises a different exception for each kind of error. Catch the specific ones first and the general ones last. An invalid key or a bad request needs a fix, not a retry. A rate limit, a server error or a network problem is temporary.

Third, let the SDK retry temporary errors for you. It already retries rate limits, server errors and connection problems a few times, with growing waits. You can change this with a client setting. Check the current default in the docs. Fourth, if the output fails your checks, send one more request that includes the error message, then give the item to a human.

Think of a courier's rules for failed deliveries. Nobody home? Try again tomorrow. Wrong address? Do not try again, ask for the right one. Parcel damaged? Repack it once, send again, then report it.

Sofia Petrova runs the invoice extractor for a logistics company in Sofia, Bulgaria. Hundreds of invoices pass through it every week, so failures are normal. She wraps the call in one function.

Look at the order of the checks. After the call, the function checks the stop reason first. Only then does it read the text and validate it against the schema and her business rules. If a check fails, it adds the error to the request and tries once more. After two attempts, it returns nothing, so the item goes to human review.

Around the call, the error handler catches each class separately, from the most specific to the most general. Each handler prints a clear message that says what to do next, such as check the key, fix the request, or try again later. Now she tests three failures on screen.

Test one. She sets max tokens to ten. The stop reason is max tokens, and the function stops with a clear message, instead of saving half a record.

Test two. In one terminal only, she sets the key variable to a wrong value. The SDK raises an authentication error, and her handler prints a clear key message. There are no retries.

A common mistake is to catch every exception and retry three times. That hides the real problem. It retries invalid keys, saves cut-off output, and sends refusals again and again. Check the stop reason, catch by class, let the SDK retry temporary errors, and send permanent failures to a person.

A common mistake is to catch every exception and retry three times. That retries invalid keys, saves cut-off output, and sends refusals again and again. Check the stop reason, catch by class, and send permanent failures to a person.

Let's recap. First, always check the stop reason before reading content. Max tokens means cut-off output, and refusal means the request was declined. Second, catch API errors by class. Let the SDK retry temporary errors, and never retry invalid keys or bad requests. Third, if validation fails, retry once or twice with the error message, then send the item to human review.

Now it is your turn. In the exercise, you will add error handling to your extractor and test it with a tiny max tokens value, an invalid key and a malformed input. Record each result in a short table. In the next lesson, Streaming Responses, you will make your app feel much faster. See you there.
```

## L07 Streaming Responses

- **Filename:** `ai-14-building-apps-with-llm-apis_M2_L07_presenter.mp4`
- **Expected length:** about 4.9 minutes (688 words). The quality gate accepts ±10%.

```text
Two apps take exactly twelve seconds to write the same answer. In the first, the user stares at a spinner for twelve seconds. In the second, words start to appear after about one second. The second app feels faster, although it is not.

In the last lesson, you made your extractor survive failures. Now let's make your app feel fast. Without streaming, the API waits until the whole reply is finished, and sends it in one piece. With streaming, the server sends small pieces while the model writes. Your app can show each piece immediately.

Two times matter to users. Time to first token is how long until the first text appears. Streaming makes this short. Total time is how long until the reply is complete. Streaming does not change that. And it does not change the cost either. You pay for the same tokens.

The Python SDK has a streaming helper that handles the low-level events for you. You open a stream, and loop over the text pieces as they arrive. After the loop, you ask for the final message. It looks like a normal response, with content, a stop reason and usage.

Under the helper, the API sends a series of named events. The message starts, text arrives in small deltas, and the message stops with the final usage. You only need these events for advanced cases, and they are listed in the streaming docs.

So when should you stream? Stream anything a person reads while waiting, such as chat replies, drafts and summaries. Streaming also helps with very long outputs, which can hit timeouts otherwise. For short background jobs, like extracting fields from a batch of invoices, a normal request is simpler.

Streaming is like live radio commentary of a football match, compared with a report in tomorrow's newspaper. The match lasts the same time either way. With the radio, you follow it as it happens. With the newspaper, you wait, and then you get everything at once.

Kenji Watanabe builds a legal research helper for a small law firm in Osaka, Japan. Lawyers ask for plain-language explanations of contract terms, and replies are often four to six hundred words long. Without streaming, they said the tool freezes.

He adds timing to the streaming loop. He notes the start time. When the first piece of text arrives, he records the time to first token. After the loop, he gets the final message and records the total time. Nothing else in his code changes. Same model, same system prompt, same messages.

He runs it with a long contract question. Watch the terminal. Text starts almost at once, and keeps flowing. At the end, you'll see something like a time to first token under one second, a total of about eleven seconds, and the output token count.

The total time is still long, but lawyers start reading almost at once. Kenji also passes the final message to his logging helper from lesson four, so every streamed call has its tokens, cost, and both times in the log. Later, he can see if a model or prompt change makes the tool feel slower.

A common mistake is to stream to the screen and forget the end of the stream. Without the final message, you have no stop reason and no usage. Your cost log is empty, and cut-off replies look complete. Always get the final message, check it, and log it.

Let's recap. First, streaming shows text as it is generated. It shortens the time to first token, but not the total time or the cost. Second, use the SDK's streaming helper, and loop over the text pieces. Third, after the loop, get the final message to check the stop reason, log usage, and save the reply to the history.

Now it is your turn. In the exercise, you will stream a long answer to the terminal, record the time to first token and the total time, then compare it with a normal request. In the next lesson, A Web Front End with Streamlit or Next.js, you will put this streaming chat on the web. See you there.
```

## L08 A Web Front End with Streamlit or Next.js

- **Filename:** `ai-14-building-apps-with-llm-apis_M2_L08_presenter.mp4`
- **Expected length:** about 4.8 minutes (670 words). The quality gate accepts ±10%.

```text
A script in your terminal is a prototype. A link that a colleague can open on their phone is a product. With about thirty lines of Python, you can turn your streaming code into a chat app on the web.

In the last lesson, you streamed replies to the terminal. Now let's put them on a web page. Streamlit is a free, open-source Python library for small web apps. You write a normal Python script, and Streamlit turns it into a page. The same pattern in Next.js is in the course resources as extra code.

One idea explains most of Streamlit. The whole script runs again from the top every time the user does something, such as sending a message. Normal variables are reset on every run. To keep data between runs, you store it in session state, which lasts for the user's session.

Think of a waiter who forgets everything each time they walk back to the kitchen. Session state is the order pad in the waiter's pocket. Whatever is written there is still there on the next trip.

A chat app needs four features. Session state keeps the messages list, because the API is stateless. Chat message shows a bubble for the user or the assistant. Chat input shows a text box at the bottom. And write stream shows streamed text as it arrives, then returns the full reply.

On your computer, the key lives in an environment variable or a local secrets file. On a host, it goes into the host's secrets settings, never into the repository. Streamlit Community Cloud and Vercel both have free plans with limits, so check the current rules.

And a public link means anyone can use your API credit. So keep max tokens low, keep your spend limit set, and consider a simple password or a per-session message limit.

Amara Diallo runs a small tour company in Dakar, Senegal. She wants a chat assistant that answers visitors' questions about her tours.

Here is her app file. It sets the model in one constant and a short system prompt. The client reads the key from Streamlit secrets. If there is no history in session state yet, it creates an empty list. Then it shows every earlier message as a bubble.

When the visitor sends a message, the app adds it to the history and shows it. Then it streams the reply with the full history and a low max tokens value, shows it with write stream, and saves the reply back into the history.

She puts the key in a local secrets file, and adds the folder to git ignore. She installs Streamlit and runs the app. In the browser, she asks about a tour, then asks a follow-up. The assistant remembers.

A common mistake is to keep the chat history in a normal list at the top of the script. Streamlit reruns the script on every message, so the list is empty each time, and the assistant forgets everything. A second mistake is committing the secrets file. Always check git status before you push.

A common mistake is to keep the chat history in a normal list at the top of the script. Streamlit reruns the script on every message, so the list is empty each time, and the assistant forgets everything.

Let's recap. First, Streamlit reruns the whole script on every user action, so keep the chat history in session state. Second, a chat app needs a chat input, message bubbles, streamed output, and the history sent with each request. Third, keep keys in the host's secrets settings, not in the repository, and protect your budget when the link is public.

Now it is your turn. In the exercise, you will build and deploy a small streaming chat app with your own system prompt, and share the link with a classmate. Your capstone will use this same front end. In the next lesson, Tool Use: Letting the Model Call Your Functions, your app starts to take real actions. See you there.
```
