# L07 Build, Buy or Use an API?

Course: AI-27 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
A feature that costs almost nothing in a demo can become one of your largest monthly bills at scale. The way to avoid that surprise is a simple calculation you can do in a spreadsheet before you commit.

## Explanation
There are four common ways to get the AI part of a feature:

1. **Foundation model API.** You send requests to a general model, such as Claude, and pay per use. Fastest to start and good quality for language tasks. You depend on one supplier and must check its data terms.
2. **Vendor product.** You buy a finished tool, such as a ready-made support assistant. Fast to launch, but less control over behaviour, evaluation and your user experience.
3. **Fine-tuning.** You adapt an existing model with your own examples. It can improve style or narrow tasks, but it needs good labelled data and ongoing maintenance.
4. **In-house model.** Your team trains its own model. Most control, often cheaper per request at very high volume, but it needs specialist skills, data and time.

Compare options on five trade-offs: **cost per request, speed (response time), quality on your test set, data terms** (where data goes, whether it is stored or used for training), and **supplier dependence** (how hard it is to switch). Many teams start with an API to learn quickly, then revisit the choice when volume and evaluation results are known.

**Estimating API cost.** Model APIs usually charge per token. A token is a small piece of text, often part of a word. Prices are usually different for input tokens (what you send, including instructions and context) and output tokens (what the model writes). The method is:

- Requests per month = users × requests per user per month
- Input cost = requests × input tokens per request × input price per token
- Output cost = requests × output tokens per request × output price per token
- Monthly cost = input cost + output cost

All prices below are placeholders for teaching. Real prices differ by model and change over time, so check the provider's pricing page on the day you plan [VERSION].

**Analogy:** Choosing between an API and your own model is like choosing between a taxi and buying a car. The taxi costs more per trip but nothing to start, and you can change companies. The car costs a lot at the start and needs maintenance, but may be cheaper if you drive every day. You decide based on how much you will travel, and you check the prices before you choose.

## Worked Example
Lena Fischer is a PM at a hypothetical accounting software company in Germany. She plans a feature that explains each invoice error in plain language. She estimates the cost with placeholder prices:

- Users: 10,000; requests per user per month: 20
- Input tokens per request: 1,500 (instructions, invoice data and rules); output tokens: 300
- Placeholder prices: 1.50 US dollars per million input tokens, 6.00 US dollars per million output tokens [VERSION]

| Item | Calculation | Result |
|---|---|---|
| Requests per month | 10,000 × 20 | 200,000 |
| Input tokens | 200,000 × 1,500 | 300,000,000 |
| Output tokens | 200,000 × 300 | 60,000,000 |
| Input cost | 300 million × 1.50 per million | 450 dollars |
| Output cost | 60 million × 6.00 per million | 360 dollars |
| Monthly total | 450 + 360 | 810 dollars |

That is about 0.08 dollars per user per month, or about 0.004 dollars per request. If usage doubles to 40 requests per user, the cost doubles to 1,620 dollars, because the cost grows in a straight line with requests.

Lena notices that input tokens are most of the volume. Shorter instructions or sending only the relevant invoice lines would lower cost. She also adds costs that are not model costs: engineering time, evaluation work and monitoring. Her data question for the provider: "Is invoice data stored, and is it used for training?" Invoices contain personal and business data, so legal must approve the data terms before any real data is sent.

## Common Mistake
Many PMs estimate cost from a demo with short prompts and a few users. Real requests often include long instructions, retrieved documents and conversation history, so input tokens grow quickly. Estimate with realistic request sizes, test the cost at double and triple usage, and include the non-model costs.

## Key Takeaways
1. The four options are a foundation model API, a vendor product, fine-tuning and an in-house model, compared on cost, speed, quality, data terms and supplier dependence.
2. API cost = requests × tokens per request × price per token, calculated separately for input and output tokens.
3. Always use current prices from the provider [VERSION], test higher usage, and check data terms before sending real data.

## Hands-on Exercise
**Task:** In Google Sheets, estimate the monthly running cost of your feature for 10,000 users using the provided placeholder prices, then test how the cost changes if usage doubles.
**Tools:** Google Sheets [VERSION].
**Steps:**
1. Create input cells: users (10,000), requests per user per month, input tokens per request, output tokens per request, input price per million tokens (placeholder 1.50) and output price per million tokens (placeholder 6.00).
2. Add formulas: requests = users × requests per user; input cost = requests × input tokens ÷ 1,000,000 × input price; output cost likewise; total = input cost + output cost.
3. Add cost per user and cost per request.
4. Copy the column and double the requests per user. Record the new total.
5. Add a third column where you halve the input tokens. Compare.
6. Write two sentences: what drives your cost most, and one way to reduce it.
**What good looks like:** Clearly labelled input cells, correct formulas that update when inputs change, three scenarios, and a short conclusion about the main cost driver. Prices are marked as placeholders.
**Time:** about 25 minutes

## Review Flags
- [VERSION] All model API prices are placeholders only; any real price must be checked on the provider's pricing page on the day of scripting.
- [VERSION] Google Sheets formula features used in the exercise must be checked before recording.
