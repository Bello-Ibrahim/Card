# L10 Bias, Data and the Limits of AI

Course: AI-01 · Module: M3 · Objectives: O6 · Video: 5 min

## Hook
Imagine a job-application system that rejects people from one region more often than people from another. Nobody told it to do that. So where did the unfairness come from? Usually, from the examples it learned from.

## Explanation
In L03 you learned that the quantity, variety and quality of examples matter. This lesson looks at what happens when the examples are not a fair picture of the world.

**Bias** in AI means that a system's outputs are systematically unfair or less accurate for some groups of people or some situations. The most common cause is **unrepresentative data**. This can happen in several ways:

- **Missing groups.** Some people or situations appear rarely or not at all in the training data. The model then has few patterns for them and makes more mistakes.
- **Unfair past decisions.** If the labels come from past human decisions, and those decisions were unfair, the model learns the unfairness as if it were a correct pattern.
- **Proxy features.** A feature can quietly stand in for something sensitive. For example, a home postcode can be linked to income or background, even when those are not in the data.

A model does not know what is fair. It only finds patterns that help it match the labels it was given.

Bias is not the only limit. Three others are important:

- **Privacy.** Training data often contains information about real people. Using it without clear permission can harm them, and personal details can sometimes appear in outputs.
- **No real-world understanding.** As you saw in L01 and L09, a model finds patterns. It does not understand causes, context or common sense.
- **Changing conditions.** A model learns from the past. When the world changes, such as new customer habits, new products or a new season, the old patterns can stop working. The model does not warn you. Its accuracy just quietly falls.

**Analogy:** Think of a cook who learned every recipe in one small village. Give them spices they have never seen, or guests with different tastes, and the results are poor. A model trained on narrow data is the same: skilled inside its experience, and unreliable outside it.

## Worked Example
This is a hypothetical case. A mid-sized bank in Malaysia wants to speed up small-business loan decisions. Its data team, led by Nurul, trains a model on ten years of past loan applications. Each example has features such as business type, years open, monthly income and location. The label is "approved" or "rejected", taken from past decisions by loan officers.

The model scores well overall, but results by group show three problems:

1. **Missing groups.** Few past applicants ran online-only businesses, so the model often rejects them, even when their income is strong.
2. **Unfair past decisions.** In some rural branches, officers in the past approved fewer loans for reasons that had little to do with risk. The model copied that pattern.
3. **Proxy features.** The "location" feature lets the model treat whole districts as higher risk, which affects applicants who are individually reliable.

Nurul's team keeps the model but collects more online-only examples, reviews the old labels, tests each group separately, and keeps a human officer in charge of every rejection.

## Common Mistake
Many people think that because a computer makes the decision, the decision must be neutral. A model reflects the data and labels people chose to give it. The correction is to ask "Whose examples did it learn from, and who is missing?" and to check accuracy for each group, not only overall. A high overall score, as you saw in L08, can hide poor results for a smaller group.

## Key Takeaways
1. Bias usually comes from unrepresentative data: missing groups, unfair past decisions used as labels, or features that act as proxies for sensitive information.
2. Other limits include privacy risks, no real-world understanding, and changing conditions that make old patterns out of date.
3. Check results separately for different groups and keep a person responsible for important decisions.

## Hands-on Exercise
**Task:** For a hypothetical hiring or loan model, list 3 ways the training data could be unrepresentative.
**Tools:** Pen and paper or any notes app. Optional: ChatGPT or Claude (free tier) to compare ideas after you finish your own list.
**Steps:**
1. Choose one scenario: (a) a company that screens job applications using its past hiring decisions, or (b) a lender that decides on personal loans using its past loan records.
2. Write down the features the model might use (for example, education, work history, location, income) and the label it learns (for example, "hired" or "not hired").
3. List 3 ways the data could be unrepresentative. Use the ideas from this lesson: missing groups, unfair past decisions, proxy features, or old data in a changed world.
4. For each problem, name one group of people who could be treated unfairly, and one action that could reduce the problem.
5. Optional: ask a chatbot the same question and note one idea it gave that you did not think of.
**What good looks like:** Three clearly different problems, each linked to a specific feature or label, a group that could be affected, and a practical action. For example: "Past hiring favoured graduates of a few universities, so applicants from other universities are under-represented. Action: test results separately for each group of universities."
**Time:** about 15 minutes

## Review Flags
- None. All cases are hypothetical by design, as approved in the curriculum. No real companies, statistics or incidents are named. Real, sourced cases may be added later after a separate fact-check.
