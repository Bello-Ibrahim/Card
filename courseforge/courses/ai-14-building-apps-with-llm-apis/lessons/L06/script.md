# L06 Validation, Errors and Retries | Presenter Script

Course: AI-14 · Video: 5 min · Words: 696

## Hook
Your extractor worked perfectly on five test invoices. On its first real day, it met a forty-page invoice, a network timeout and an expired key. Code that talks to an API must expect failure, and handle each kind in the right way.

## Explain
In the last lesson, you built an invoice extractor. Now let's make it robust. Failures come from three places. The response is incomplete, the request fails, or the output does not pass your checks.

First, check the stop reason before you read anything. A successful response can still be unusable. End turn means the model finished. Max tokens means the output was cut off, so structured data may be incomplete. Refusal means the model declined. Show a clear message, and do not retry the same input again and again.

Second, handle API errors by type. The Python SDK raises a different exception for each kind of error. Catch the specific ones first and the general ones last. An invalid key or a bad request needs a fix, not a retry. A rate limit, a server error or a network problem is temporary.

Third, let the SDK retry temporary errors for you. It already retries rate limits, server errors and connection problems a few times, with growing waits. You can change this with a client setting. Check the current default in the docs. Fourth, if the output fails your checks, send one more request that includes the error message, then give the item to a human.

Think of a courier's rules for failed deliveries. Nobody home? Try again tomorrow. Wrong address? Do not try again, ask for the right one. Parcel damaged? Repack it once, send again, then report it.

## Demonstrate
Sofia Petrova runs the invoice extractor for a logistics company in Sofia, Bulgaria. Hundreds of invoices pass through it every week, so failures are normal. She wraps the call in one function.

Look at the order of the checks. After the call, the function checks the stop reason first. Only then does it read the text and validate it against the schema and her business rules. If a check fails, it adds the error to the request and tries once more. After two attempts, it returns nothing, so the item goes to human review.

Around the call, the error handler catches each class separately, from the most specific to the most general. Each handler prints a clear message that says what to do next, such as check the key, fix the request, or try again later. Now she tests three failures on screen.

Test one. She sets max tokens to ten. The stop reason is max tokens, and the function stops with a clear message, instead of saving half a record.

Test two. In one terminal only, she sets the key variable to a wrong value. The SDK raises an authentication error, and her handler prints a clear key message. There are no retries.

A common mistake is to catch every exception and retry three times. That hides the real problem. It retries invalid keys, saves cut-off output, and sends refusals again and again. Check the stop reason, catch by class, let the SDK retry temporary errors, and send permanent failures to a person.

A common mistake is to catch every exception and retry three times. That retries invalid keys, saves cut-off output, and sends refusals again and again. Check the stop reason, catch by class, and send permanent failures to a person.

## Recap
Let's recap. First, always check the stop reason before reading content. Max tokens means cut-off output, and refusal means the request was declined. Second, catch API errors by class. Let the SDK retry temporary errors, and never retry invalid keys or bad requests. Third, if validation fails, retry once or twice with the error message, then send the item to human review.

## CTA
Now it is your turn. In the exercise, you will add error handling to your extractor and test it with a tiny max tokens value, an invalid key and a malformed input. Record each result in a short table. In the next lesson, Streaming Responses, you will make your app feel much faster. See you there.

## Thumbnail
Headline: Expect Failure, Handle It
Image: Navy background, three coloured parcels with labels retry, stop and repack, headline in teal Inter Bold.

## Production Notes
- [VERSION] SDK error class names (AuthenticationError, BadRequestError, RateLimitError, APIStatusError, APIConnectionError), the default max_retries value, which status codes are retried automatically, and the output_config structured-output parameter must be checked against the current SDK docs before recording. The voiceover names no default retry count.
- The three test results in the demo are hypothetical; record them live and adjust the voiceover only if the behaviour differs.
- For the invalid-key test, set a clearly fake value in one terminal only; never show the real key. Restore it off camera.
- Sofia Petrova and the Sofia logistics company are fictional; invoices are invented text.
