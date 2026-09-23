# L13 Cost Control in Practice | Presenter Script

Course: AI-14 · Video: 5 min · Words: 686

## Hook
Your app sends the same three-thousand-token system prompt with every question. A thousand questions a day means paying to send the same instructions a thousand times. Cost control starts with noticing what you pay for again and again.

## Explain
In the last lesson, you built an evaluation set. Now you will use it to cut costs safely. There are five main levers. Your usage log from lesson four shows which one matters most for your app.

The first lever is prompt caching. If the start of your request is the same every time, such as the tools, the system prompt or a long document, you can mark it for caching. The first request writes it to a cache. Later requests, within a short time, read it from the cache at a much lower price.

The cached part must match exactly, from the start of the request. So put stable content first, and the user's question last. There is a minimum length, a limited cache lifetime, and a small extra charge for writing. Check the current rules on the pricing page.

Second, batch processing for jobs that can wait. The batch API takes many requests at once and returns results later, at a discount. It suits nightly reports and bulk extraction, not live chat. Third, send easy tasks, like classification or routing, to a smaller model. Fourth, set output limits per feature. Fifth, set per-user quotas, so one user or a bot cannot spend your whole budget.

Think of a restaurant kitchen. You prepare the base sauce once in the morning, instead of for every plate. That is caching. You give simple dishes to the junior cook, and you serve sensible portions. And you still taste every dish before it goes out.

That last part matters. A cheaper setup that fails more cases is not really cheaper. Run your evaluation set after every change, and compare pass rate and cost together.

## Demonstrate
Aroha Ngata builds a study helper for a tutoring company in Wellington, New Zealand. Every request includes a long system prompt with course rules and examples. Hundreds of students use it every day, so that prompt is sent again and again. Her usage log shows that it is most of her input tokens.

First, she sends the same question twice without caching, and logs the usage. Both calls send the full system prompt as normal input tokens.

Then she adds the cache marker to the system prompt block, and sends two different questions within a minute. You'll see something like this. The first call writes the system prompt to the cache. The second call reads it from the cache, and only the new question counts as normal input.

She adds the current prices for cache writes and cache reads to her cost helper, and compares the cost of each call. Then she runs her evaluation set with caching on. The pass rate is unchanged, because caching does not change what the model sees.

She also moves her nightly summary report to the batch API, and sends simple topic classification to a smaller model, after checking it on twenty cases.

A common mistake is to put something that changes, like the current time or the user's name, at the start of the system prompt. Then every call writes to the cache and never reads from it. Check that cache reads are above zero on repeated calls.

## Recap
Let's recap. First, use prompt caching for long, stable context at the start of the request, and confirm cache reads in the usage fields. Second, use batch processing for work that can wait, a smaller model for easy tasks, and output limits and per-user quotas everywhere. Third, measure quality with your evaluation set before and after each change.

## CTA
Now it is your turn. In the exercise, you will apply prompt caching to a request with a long system prompt, and compare the cached and uncached usage and cost over six calls. Your capstone starts next. In the next lesson, Capstone Step One: Build the Core Feature, you will choose your use case and build it. See you there.

## Thumbnail
Headline: Stop Paying Twice
Image: Navy background, a long system prompt block stamped with a teal cache icon and a falling cost line, headline in teal Inter Bold.

## Production Notes
- [VERSION] Prompt caching syntax (cache_control), minimum cacheable length, cache lifetime, cache write and read prices, the usage field names (cache_creation_input_tokens, cache_read_input_tokens), and the Batch API discount (about 50% in content.md) and rules must be checked against the current docs. The voiceover states no discount percentage and no prices; it says 'check the current pricing page'.
- The token numbers in Aroha's usage table (3620, 3500 and so on) are illustrative: label them 'example output' on screen. Show costs as formulas or placeholders, not real prices.
- Aroha Ngata and the Wellington tutoring company are fictional.
