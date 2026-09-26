# L07 Build, Buy or Use an API? | Presenter Script

Course: AI-27 · Video: 5 min · Words: 692

## Hook
A feature that costs almost nothing in a demo can become one of your largest monthly bills at scale. The way to avoid that surprise is a simple calculation you can do in a spreadsheet, before you commit.

## Explain
Last time, we looked at the data your feature needs. Now, where does the AI part come from? There are four common ways.

A foundation model API: you send requests to a general model, such as Claude, and pay per use. It is the fastest start, but you depend on one supplier.

A vendor product: you buy a finished tool. It is fast to launch, with less control. Fine tuning: you adapt a model with your own examples, which needs good labelled data. And an in house model: the most control, but it needs specialist skills, data and time.

Compare the options on five trade offs: cost per request, speed, quality on your test set, data terms, and how hard it is to switch supplier. Many teams start with an API to learn quickly, then revisit the choice when volume and evaluation results are known.

Model APIs usually charge per token. A token is a small piece of text, often part of a word. Input tokens are what you send, including instructions and context. Output tokens are what the model writes. They usually have different prices. So monthly cost is requests, times tokens per request, times price per token, worked out for input and output separately.

One important note. All the prices in this lesson are placeholders for teaching. Real prices differ by model and change over time, so always check the provider's pricing page on the day you plan.

Choosing between an API and your own model is like choosing between a taxi and buying a car. The taxi costs more per trip, but nothing to start, and you can change companies. The car costs a lot at the start and needs maintenance, but may be cheaper if you drive every day.

## Demonstrate
Let's calculate. Lena Fischer is a PM at a hypothetical accounting software company in Germany. She plans a feature that explains each invoice error in plain language.

She has ten thousand users, each making twenty requests a month. That is two hundred thousand requests. Each request sends fifteen hundred input tokens and gets three hundred output tokens back. Her placeholder prices are one dollar fifty per million input tokens, and six dollars per million output tokens.

Input is three hundred million tokens, so four hundred and fifty dollars. Output is sixty million tokens, so three hundred and sixty dollars. The monthly total is eight hundred and ten dollars, with placeholder prices. That is about eight cents per user per month.

What if usage doubles to forty requests per user? The cost doubles to one thousand six hundred and twenty dollars a month, because cost grows in a straight line with requests.

Lena notices that input tokens are most of the volume. Shorter instructions, or sending only the relevant invoice lines, would lower the cost. She also adds costs that are not model costs: engineering time, evaluation work and monitoring. And she asks the provider whether invoice data is stored or used for training. Legal must approve the data terms before any real data is sent.

A common mistake is estimating cost from a demo with short prompts and a few users. Real requests carry long instructions and documents. Test at double and triple usage.

## Recap
Let's recap. First, the four options are an API, a vendor product, fine tuning and an in house model, compared on cost, speed, quality, data terms and supplier dependence. Second, API cost is requests times tokens times price, for input and output separately. Third, always use current prices, test higher usage, and check data terms before sending real data.

## CTA
Now it is your turn. In the exercise below, estimate the monthly cost of your feature for ten thousand users in Google Sheets, using the placeholder prices provided. Then see what happens when usage doubles. It takes about twenty five minutes. In the next lesson, we look at designing evaluation, and the metrics that matter. See you there.

## Thumbnail
Headline: Taxi or Buy a Car?
Image: Navy background, a taxi icon and a car-with-keys icon on either side of a simple cost chart, headline in teal Inter Bold.

## Production Notes
- [VERSION] All model API prices are placeholders for teaching only (1.50 US dollars per million input tokens, 6.00 US dollars per million output tokens). The voiceover calls them placeholders; every cost slide must carry the label 'Placeholder prices, check the provider's pricing page'. Do not replace them with real prices without checking on the day of recording.
- [VERSION] Google Sheets formula features used in the exercise must be checked before recording.
- The figures must be spoken and shown exactly as in content.md: 450 dollars input, 360 dollars output, 810 dollars a month, 1,620 dollars a month when usage doubles, about 0.08 dollars per user and 0.004 dollars per request.
- Claude is named only as an example of a foundation model API, as in content.md. Lena Fischer and the accounting software company in Germany are hypothetical.
