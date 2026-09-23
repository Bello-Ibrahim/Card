# L04 Tokens, Context and Cost | Presenter Script

Course: AI-14 · Video: 5 min · Words: 684

## Hook
Two apps use the same model and answer the same number of questions each day. One costs ten times more than the other. The difference is not the model. It is how many tokens each app sends and receives.

## Explain
In lesson two, you printed token counts. Now let's turn them into money. Every response includes a usage object. Input tokens are everything you sent, including the system prompt, the messages and any tool definitions. Output tokens are what the model wrote.

Prices are listed per million tokens, and output tokens usually cost more than input tokens. So the cost of one call is input tokens times the input price, plus output tokens times the output price, divided by one million. Prices differ by model and change, so check the current pricing page, and keep them in one place in your code.

You can also count tokens before you send. The API has a token-counting endpoint. You pass the same model, system prompt and messages, and it returns the input token count without writing a reply. Use it to check that a long document fits, or to warn a user before an expensive request.

Longer context costs more, and is usually slower. In a chat app, the history grows with every turn. So send only the parts of a document that matter, keep the last few turns of a long chat, and keep max tokens close to what you really need.

Think of a taxi meter that counts words instead of kilometres. It runs while you speak, and faster while the driver speaks. If you read a long letter aloud at the start of every ride, every ride is expensive, even when your question is short.

Languages matter too. A tokenizer splits text into pieces it saw often in training. So do not assume the same meaning costs the same in every language or script. Measure it for your own languages with the token counter.

## Demonstrate
Farida runs a language-learning app in Cairo, Egypt. Learners ask grammar questions in English or Arabic. She wants to know what each call costs, and how the two languages compare.

She writes a small helper. At the top are two price constants, copied from the pricing page. The helper reads the usage from each response, calculates the cost, and adds one row to a CSV file with the time, the feature, the model, both token counts and the cost.

Before sending, she counts the input tokens for the same grammar question, once in English and once in Arabic, with the same system prompt.

Then she sends both requests with the same max tokens, and logs them. You'll see something like two rows in the CSV file. She compares the token counts in the two rows. But one test is not enough, so she will measure a sample of real questions in each language before she sets prices for her premium plan.

She also notices something bigger. Her system prompt is six hundred tokens long, and it is sent with every call. She makes a note to try prompt caching in lesson thirteen.

A common mistake is to estimate cost from the user's question only. In a real app, most input tokens often come from things the user never sees. The system prompt, examples, the chat history and documents. Always log real usage, and calculate from that.

## Recap
Let's recap. First, the cost of a call is input tokens times the input price, plus output tokens times the output price, using prices per million tokens from the live pricing page. Second, longer context means higher cost and slower replies, so send only what the model needs. Third, measure token counts for your own languages with the token counter.

## CTA
Now it is your turn. In the exercise, you will write a helper that logs tokens and estimated cost for every call, then compare the same request in English and one other language. This logging will grow into your capstone cost dashboard. In the next lesson, Structured Outputs with JSON Schemas, your code will get data it can trust. See you there.

## Thumbnail
Headline: Where Your Tokens Go
Image: Navy background, a taxi-meter style counter beside a stacked bar of system prompt, history and question, headline in teal Inter Bold.

## Production Notes
- [VERSION] Prices per model, the token-counting endpoint and its SDK method (count_tokens), and any limits or pricing for it must be checked against the current docs at recording time. The voiceover names no prices; the PRICE_IN and PRICE_OUT constants stay at 0.0 placeholders on screen, and cost values in the log are shown as 0.00xxxx.
- [VERIFY] The claim that the same meaning can use different token counts in different languages is NOT stated as fact in the voiceover; the script only tells learners to measure their own languages. The Arabic and English numbers in Farida's log (212/180 and 241/205) are illustrative: label them 'example numbers' on screen.
- Farida and the Cairo language-learning app are fictional. Use an invented grammar question; no learner data on screen.
