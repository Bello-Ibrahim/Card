# L10 Choosing a Business Model

Course: AI-28 · Module: M2 · Objectives: O2, O5 · Video: 5 min

## Hook
Two founders build the same product. One charges a monthly subscription; the other charges for each use. A year later, one business is healthy and the other is losing money. The product was the same. The difference was how they asked customers to pay.

## Explanation
A **business model** describes who pays you, for what, and how. Common models for AI products are:

- **Subscription**: a fixed price each month or year. Predictable for you and the customer. The risk: heavy users can cost more than they pay (see L09).
- **Pay per use**: the customer pays for each action, such as each page translated or each document processed. Your revenue rises with your costs. The risk: customers may use it less because they see a price every time, and income is harder to predict.
- **Pay per result**: the customer pays only when an outcome happens, such as a recovered unpaid invoice. Attractive to customers, but you carry the risk when results do not come.
- **Freemium**: a free basic version, with payment for more features or more use. It can attract many users, but free users still create model costs.

You also choose **who** pays:

- **B2B (business to business)**: you sell to companies. Prices can be higher and customers often stay longer, but sales take more time.
- **B2C (business to consumer)**: you sell to individuals. Sales are faster, but people are often more price sensitive and may stop paying quickly.

The model also affects defensibility (L05). A product paid per result or deeply built into a company's daily process is harder to replace than a low-cost subscription that anyone can cancel in one click.

**Local factors matter.** In many emerging markets, fewer people use credit cards, and **mobile money** (payments sent from a mobile phone account) or airtime top-ups may be more common. Small, frequent payments may feel safer to customers than a monthly commitment. Payment providers and their fees differ by country [REGION] [VERSION].

**Analogy:** A gym and a swimming pool can both sell exercise. The gym sells monthly memberships and hopes most members come only sometimes. The pool sells single tickets, so it earns more when people swim more. Neither is wrong, but each works for a different kind of customer.

## Worked Example
Awa is a hypothetical founder in Dakar, Senegal. Her tool helps small businesses translate documents between French, English and Wolof, with a human check for important texts. She compares two models, using placeholder prices in US dollars [VERSION]. Each translated page costs her $0.01 in model usage, each customer also costs $1.20 per month in hosting and support, and the mobile-money provider keeps 2% of each payment.

**Subscription: $8 per month for unlimited pages.**
**Pay per use: $0.05 per page.**

| Monthly use | Subscription: revenue, cost, profit | Pay per use: revenue, cost, profit |
|---|---|---|
| Light (20 pages) | $8.00, $1.56, **$6.44** (80.5% margin) | $1.00, $1.42, **−$0.42** (loss) |
| Typical (200 pages) | $8.00, $3.36, **$4.64** (58% margin) | $10.00, $3.40, **$6.60** (66% margin) |
| Heavy (1,000 pages) | $8.00, $11.36, **−$3.36** (loss) | $50.00, $12.20, **$37.80** (75.6% margin) |

How one cell is calculated: typical subscription cost = 200 × $0.01 + $1.20 + 2% of $8.00 = $2.00 + $1.20 + $0.16 = $3.36.

Each model has a risk. Subscription loses money on heavy users. Pay per use loses money on light users, because the fixed $1.20 cost is larger than the revenue. Awa's interviews showed that her customers prefer small mobile-money payments and that their use varies a lot from month to month. She chooses **pay per use with a minimum monthly charge of $2**, which covers the fixed cost for light users.

## Common Mistake
Many founders copy the business model of a famous software company, usually a low monthly subscription, without checking their own costs or their customers' payment habits. With AI products, the cost of each use is real, so a model that ignores usage can be dangerous. Always test your chosen model against light, typical and heavy customers, and against how your customers actually prefer to pay.

## Key Takeaways
1. Common models are subscription, pay per use, pay per result and freemium, sold to businesses (B2B) or consumers (B2C).
2. Test each model against light, typical and heavy users; each model loses money on a different kind of customer.
3. Local payment habits, such as mobile money and price sensitivity, can decide which model works.

## Hands-on Exercise
**Task:** Compare two business models for your idea in a table: price, cost to serve, margin, and the risk of each.
**Tools:** A free spreadsheet; your unit economics sheet from L09; optional Claude (free plan).
**Steps:**
1. Choose two business models that could fit your customers.
2. Set a placeholder price for each, and mark it as a placeholder.
3. Using your L09 costs, calculate revenue, cost to serve and gross margin for a light, typical and heavy customer under each model.
4. Write the main risk of each model in one sentence.
5. Add one row on payment habits: how your customers prefer to pay, based on your interviews.
6. Optional: ask Claude, "Which customer type would make each of these models lose money, and how could I protect against that?"
7. Choose one model and write two sentences explaining why.
**What good looks like:** A clear table with two models and three customer types, correct formulas, a named risk for each model, and a choice supported by your costs and your customers' payment habits.
**Time:** about 35 minutes

## Review Flags
- [VERSION] All prices and costs ($8 subscription, $0.05 per page, $0.01 model cost per page, $1.20 hosting and support, 2% payment fee, $2 minimum charge) are placeholders. The table figures were checked by calculation; if placeholders change, recalculate them.
- [REGION] Mobile-money availability, payment providers and their fees differ by country; the Senegal example is illustrative.
