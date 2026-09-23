# L06 Data Needs: What Your Feature Learns From

Course: AI-27 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
Your team can choose the best model available and still ship a poor feature. If the data behind it is old, incomplete or collected without permission, the model will faithfully repeat those problems to your users.

## Explanation
Every AI feature depends on data in up to three ways:

- **Training or tuning data:** examples a model learns from, if you train or adapt a model.
- **Context data:** information given to the model at the moment of use, such as a product catalogue, help articles or the user's order history.
- **Evaluation data:** examples with known good answers that you use to test quality (L09).

Even if you use a ready-made model through an API, you still need context and evaluation data. As a PM, you own the questions about all three. Check each source against six points:

1. **Source and owner.** Where does it come from, and who inside the company can approve its use?
2. **Labels.** Do the examples include the correct answer, such as "this substitution was accepted"? Who created the labels, and how consistent are they?
3. **Quality.** Is it accurate, complete and current? Old prices or deleted products create wrong answers.
4. **Coverage.** Does it represent all your users: regions, languages, device types, new and old customers? Gaps in coverage become quality gaps for those users.
5. **Consent and privacy.** Did users agree to this use? Does it contain personal data, and is that data necessary? Rules differ by country, so involve your privacy or legal team early.
6. **Access and cost.** Can the team get the data in a usable format, and how long will it take?

**The cold-start problem.** A new product, or a new market, often has no usage data yet. Common ways to fill the gap are: start with a rule-based version and collect data from it; use a general model with good context data instead of training; create a small set of labelled examples by hand; or run a human-in-the-loop version first, so that human decisions become labels.

**Analogy:** A recipe is only as good as its ingredients. A skilled chef with old vegetables still serves a poor meal. And if the kitchen only stocks ingredients for one type of dish, guests who want something else go hungry. Data quality is the freshness of your ingredients, and coverage is the range of dishes your kitchen can make.

## Worked Example
Mateo Fuentes is a PM at a hypothetical online grocery service in Chile. When an item is out of stock, pickers in the store choose a substitute. Mateo wants an AI feature that suggests the best substitute to the picker, who confirms it.

He fills in a data requirements table:

| Source | Owner | Quality risks | Privacy questions | How to fill gaps |
|---|---|---|---|---|
| Product catalogue (name, brand, size, price, category) | Catalogue team | Missing sizes; categories used inconsistently | None: no personal data | Clean the top 500 products first |
| Past substitutions and whether customers accepted or refunded them | Operations | Accept or refund is recorded, but not the reason | Linked to customer accounts; remove identity before use | Use only the item pair and the outcome |
| Customer dietary preferences (such as "no pork") | Customer team | Few customers fill them in | Sensitive personal data; needs clear consent and a legal review | Do not use in the MVP; ask legal before any later use |
| New store in the south, opened recently | Operations | Almost no substitution history | Same as above | Start with catalogue similarity rules and collect picker choices as labels |

The table leads to two decisions. First, the MVP will not use dietary preferences, because the privacy questions need more time and the feature works without them. Second, the new store has a cold-start problem, so it will begin with a simpler rule-based version and use picker confirmations to build labelled data.

## Common Mistake
Many PMs assume that "we have lots of data" means "we have the right data". A large data set can still lack labels, miss whole user groups or contain personal data you are not allowed to use. Ask specific questions about labels, coverage and consent, not only about volume. Never paste real customer data into an AI tool to "check it quickly". Use invented or anonymised examples.

## Key Takeaways
1. An AI feature needs context data and evaluation data even when you use a ready-made model, and sometimes training data as well.
2. Check every source for owner, labels, quality, coverage, consent and access, because each gap becomes a product problem.
3. Plan for cold start with rules, hand-labelled examples or a human-in-the-loop version whose decisions become labels.

## Hands-on Exercise
**Task:** Complete a data requirements table for your feature: sources, owner, quality risks, privacy questions and how you would fill any gaps.
**Tools:** Google Sheets or a document; optional: Claude (free plan) to suggest missing questions [VERSION].
**Steps:**
1. List every data source your feature needs. Mark each as training, context or evaluation data.
2. For each source, fill in the columns: source, owner, labels, quality risks, coverage gaps, privacy questions and how to fill gaps.
3. Mark any source that contains personal or sensitive data. Write the question you would ask your privacy or legal team.
4. Identify one cold-start or coverage gap and describe how you would fill it.
5. Optional: describe your feature to Claude in general terms, without any real data, and ask which data risks you may have missed.
**What good looks like:** A table with at least 3 sources, a named owner for each, specific quality and coverage risks, clear privacy questions, and a realistic plan for at least one gap.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Claude free-plan limits and data-use terms must be checked before recording.
- Data protection rules are described only as general principles; no country's law is named in this lesson.
