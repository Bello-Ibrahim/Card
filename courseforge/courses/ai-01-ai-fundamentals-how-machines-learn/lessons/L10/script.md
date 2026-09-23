# L10 Bias, Data and the Limits of AI | Presenter Script

Course: AI-01 · Video: 5 min · Words: 687

## Hook
Imagine a job application system that rejects people from one region more often than people from another. Nobody told it to do that. So where did the unfairness come from? Usually, from the examples it learned from.

## Explain
In lesson three, you learned that the quantity, variety and quality of examples matter. Today we look at what happens when the examples are not a fair picture of the world.

Bias in AI means that a system's outputs are unfair, or less accurate, for some groups of people or some situations, again and again. The most common cause is unrepresentative data.

This can happen in three main ways. Missing groups: some people appear rarely in the training data, so the model makes more mistakes for them. Unfair past decisions: if the labels come from past human decisions that were unfair, the model learns the unfairness as if it were correct.

And proxy features. A feature can quietly stand in for something sensitive. For example, a home postcode can be linked to income or background, even when those are not in the data. Remember, a model does not know what is fair. It only finds patterns that match its labels.

Bias is not the only limit. Privacy: training data often contains information about real people. Using it without clear permission can harm them, and personal details can sometimes appear in outputs. No real-world understanding: a model finds patterns, but it does not understand causes, context or common sense.

And changing conditions. A model learns from the past. When the world changes, with new customer habits, new products or a new season, the old patterns can stop working. The model does not warn you. Its accuracy just quietly falls.

Think of a cook who learned every recipe in one small village. Give them spices they have never seen, or guests with different tastes, and the results are poor. A model trained on narrow data is the same. Skilled inside its experience, and unreliable outside it.

## Demonstrate
Here is a hypothetical case. A mid-sized bank in Malaysia wants to speed up small business loan decisions. Its data team, led by Nurul, trains a model on ten years of past loan applications.

Each example has features such as business type, years open, monthly income and location. The label is approved or rejected, taken from past decisions by loan officers. The model scores well overall. But when the team checks results by group, they find three problems.

First, missing groups. Few past applicants ran online-only businesses, so the model often rejects them, even when their income is strong. Second, unfair past decisions. In some rural branches, officers approved fewer loans for reasons that had little to do with risk, and the model copied that pattern.

Third, proxy features. The location feature lets the model treat whole districts as higher risk. That affects applicants who are, individually, reliable.

Nurul's team keeps the model, but they collect more online-only examples, review the old labels, test each group separately, and keep a human officer in charge of every rejection.

A common mistake is to think that a computer decision must be neutral. A model reflects the data and labels people chose to give it. So ask, whose examples did it learn from, and who is missing? And check accuracy for each group, not only overall. As you saw in lesson eight, a high overall score can hide poor results for a smaller group.

## Recap
Let's recap. First, bias usually comes from unrepresentative data: missing groups, unfair past decisions used as labels, or proxy features. Second, other limits include privacy, no real-world understanding, and changing conditions. Third, check results separately for different groups, and keep a person responsible for important decisions.

## CTA
Now it is your turn. In the exercise below this video, choose a hypothetical hiring or loan model, and list three ways its training data could be unrepresentative. For each one, name who could be treated unfairly, and one action that helps. Your capstone project starts in the next lesson, Build Your Own Image Classifier, where you train a model yourself. See you there.

## Thumbnail
Headline: Who Is Missing?
Image: Navy background, a crowd of simple person icons with a few faded-out gaps, a teal magnifying glass over one gap, headline in teal Inter Bold.

## Production Notes
- The bank case is hypothetical by design, as approved in the curriculum. Keep the caption 'Hypothetical example' on scenes 10 to 14. Do not name or suggest any real bank, company or incident; real, sourced cases may be added later only after a separate [VERIFY] fact-check.
- Nurul's bank in Malaysia is fictional; stock footage must not show a real bank's name, logo or branch signs.
- Show a diverse range of people in stock footage, and avoid showing any group as the 'problem'.
