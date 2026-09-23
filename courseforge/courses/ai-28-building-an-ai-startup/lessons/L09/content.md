# L09 Unit Economics of an AI Product

Course: AI-28 · Module: M2 · Objectives: O5 · Video: 5 min

## Hook
A traditional app costs almost nothing extra when one more customer uses it. An AI product is different: every time a customer presses the button, you pay the model supplier. That means one very active customer on a cheap plan can cost you more than they pay. Do you know which of your customers are making you money?

## Explanation
**Unit economics** means looking at the money for one "unit" of your business, usually one customer per month. Two questions matter: how much does one customer bring in, and how much does it cost to serve them?

**Revenue per customer** is what the customer pays you, for example a monthly plan price.

**Cost to serve** is everything you spend because that customer uses the product. For an AI product it usually includes:

- **Model usage**: the fee you pay the model supplier. Suppliers usually charge by the amount of text processed, so more requests and longer requests cost more [VERSION].
- **Hosting and tools**: your share of the no-code builder, database and other subscriptions.
- **Support**: time spent helping the customer.
- **Payment fees**: the percentage a payment provider keeps from each payment [VERSION].

**Gross profit** is revenue minus cost to serve. **Gross margin** is gross profit as a percentage of revenue. It tells you how much of each unit of money you keep to pay for everything else, such as salaries, marketing and rent.

Two more terms help you see the full picture:

- **CAC (customer acquisition cost)**: what you spend on marketing and sales to win one new customer.
- **Payback period**: how many months of gross profit it takes to earn back the CAC.

All prices in this lesson are **placeholders** in US dollars, not real prices. Model and tool prices change often, so always check the current prices on the day you do your own calculation [VERSION].

**Analogy:** Think of an all-you-can-eat restaurant. The price is fixed, but the cost depends on how much each guest eats. Most guests are profitable. A few very hungry guests cost more than they pay. The owner must know the average guest and the hungriest guest before setting the price.

## Worked Example
Karim is a hypothetical founder in Marrakech, Morocco. His product drafts replies to guest messages for small guesthouses. He charges **$20 per month** [VERSION]. He estimates the cost to serve an average customer, using placeholder prices:

| Item | Calculation | Monthly cost |
|---|---|---|
| Model usage | 600 requests × $0.004 per request [VERSION] | $2.40 |
| Hosting and tools share | Estimate | $1.50 |
| Support | About 10 minutes per customer | $2.00 |
| Payment fee | 3% of $20 [VERSION] | $0.60 |
| **Total cost to serve** | | **$6.50** |

- Gross profit = $20.00 − $6.50 = **$13.50** per month.
- Gross margin = $13.50 ÷ $20.00 = **67.5%**.

Now the **heavy user**. One large guesthouse sends 5,000 requests a month. Model usage becomes 5,000 × $0.004 = $20.00. The total cost to serve becomes $20.00 + $1.50 + $2.00 + $0.60 = **$24.10**. Karim **loses $4.10** every month on this customer.

Finally, **CAC and payback**. Karim spent $300 on local advertising and won 10 customers, so CAC = $300 ÷ 10 = **$30**. Payback period = $30 ÷ $13.50 gross profit per month = about **2.2 months**. An average customer must stay for more than two months before Karim earns back what he spent to win them.

Karim's decisions: add a usage limit to the $20 plan (for example, 1,500 requests), create a higher-priced plan for large guesthouses, and shorten prompts to reduce model usage per request.

## Common Mistake
Many founders calculate the cost of the **average** user and stop. With AI products, usage can vary a lot between customers, and a small number of heavy users can remove your profit. Always calculate at least two cases: average and heavy. A second mistake is forgetting costs that are not the model, such as support and payment fees. These are often larger than founders expect.

## Key Takeaways
1. Unit economics compares what one customer pays with what it costs to serve them, including model usage, hosting, support and payment fees.
2. Gross margin is gross profit divided by revenue; heavy AI usage can make a cheap plan lose money.
3. CAC and payback period show how long a customer must stay before you earn back the cost of winning them.

## Hands-on Exercise
**Task:** In a free spreadsheet, estimate the monthly cost and revenue per customer for your MVP, then ask Claude to check your formulas and assumptions.
**Tools:** A free spreadsheet; Claude (free plan); your model supplier's and tools' current price pages [VERSION].
**Steps:**
1. Create rows for price, model usage, hosting and tools, support, and payment fees.
2. For model usage, write your assumption: requests per customer per month × cost per request. Check current prices, or use clearly marked placeholders.
3. Use formulas, not typed totals, for total cost, gross profit and gross margin.
4. Copy the column and create a "heavy user" case with five to ten times more requests.
5. Add a CAC estimate and a payback period formula: CAC ÷ monthly gross profit.
6. Paste your sheet as text into Claude (with no confidential data) and ask: "Check my formulas and tell me which assumptions look unrealistic."
7. Recalculate one example by hand to confirm the sheet is correct.
**What good looks like:** A sheet with formulas for average and heavy users, a clear gross margin for each, a CAC and payback estimate, placeholder prices clearly labelled, and one change you would make to your pricing or product.
**Time:** about 40 minutes

## Review Flags
- [VERSION] All model, tool, support and payment-fee figures ($20 plan, $0.004 per request, $1.50 hosting, $2.00 support, 3% payment fee, $300 advertising) are placeholders. The worked numbers (cost to serve $6.50, gross margin 67.5%, heavy-user loss $4.10, CAC $30, payback about 2.2 months) were checked by calculation; if placeholders change, recalculate them.
- [VERSION] How model suppliers charge (by amount of text processed) should be confirmed against current pricing pages.
