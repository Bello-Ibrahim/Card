# L18 Capstone Step 2: Report to Stakeholders

Course: AI-12 · Module: M4 · Objectives: O6, O7 · Video: 5 min

## Hook
"ROC AUC 0.75, recall 0.67 at a threshold of 0.15." To a data scientist, this is a clear result. To a sales director, it means nothing, and a model that nobody understands will not be used. Your last task is to explain your model in the language of the business.

## Explanation
A **stakeholder report** is one page for people who make decisions, not for people who build models. It should answer six questions, in this order:

1. **The problem:** What decision does the model support, and why does it matter?
2. **What the model does:** In one or two sentences, with no algorithm names unless asked. "It gives each customer a score for how likely they are to open a term deposit."
3. **Performance in business terms:** Turn metrics into counts that people can picture. Precision becomes "of every 100 customers we call, about N subscribe". Recall becomes "we reach about N out of every 10 customers who would subscribe". MAE becomes "on average, the forecast is N bikes per hour away from the real number". Always compare with the current way of working or a simple baseline.
4. **Limits:** What the model cannot do. For example: it was tested on past data only; it has not seen a period of very different interest rates; it shows patterns, not causes.
5. **Risks:** Your subgroup check and risk note from L16, in short form: which groups are served less well, and what happens when the model is wrong.
6. **Recommendation:** A clear next step, such as "Use the score to order the call list in one region for one month, and compare results with the current method."

Write for a busy reader. Use short sentences and plain words. Replace technical terms with their meaning, or explain them once. Put the most important numbers in one small table. Add an **executive summary** of 3 sentences at the top: what the model does, how much it helps, and what you recommend.

Be honest about uncertainty. Round numbers ("about 29 in 100", not "29.2%") and say what they are based on ("tested on 500 past customers the model had not seen").

If you use an AI assistant to improve your wording, share only the summary numbers and your own text. Do not paste customer data or confidential company information into AI tools.

**Analogy:** A good stakeholder report is like a weather forecast on the evening news. The forecaster does not explain the physics of air pressure. She says, "70% chance of rain tomorrow afternoon, take an umbrella." The audience gets the result, how sure it is, and what to do about it.

## Worked Example
Kwame Mensah is a data analyst at a hypothetical bank in Accra, Ghana. His model is the term-deposit pipeline from this course, with the 0.15 threshold from L09. On the test set of 500 past customers, 60 had subscribed. At the chosen threshold, the model selected 137 customers to call, and 40 of them had subscribed. It missed the other 20 subscribers.

Kwame turns these counts into business statements:

- "If we call the customers the model selects, about 29 of every 100 calls lead to a subscription. If we call customers at random, about 12 of every 100 do."
- "The model's list reaches about 2 out of every 3 customers who would subscribe, while calling only about a quarter of all customers."
- "The model works less well for customers aged 31 to 50: it reaches about half of the subscribers in that group."

His executive summary for the head of retail, Isabel Duarte:

"We built a score that ranks customers by how likely they are to open a term deposit. In a test on 500 past customers, calling the top-ranked quarter reached two thirds of the subscribers, with more than twice as many subscriptions per call as random calling. We recommend a one-month trial in one region, with a monthly check of results by age group."

Kwame's limits section notes that the test used past data only, that some age groups had few subscribers in the test, and that call outcomes may change with interest rates.

## Common Mistake
Learners often copy the classification report into the stakeholder report, or describe the method in detail ("we used a logistic regression pipeline with one-hot encoding..."). Readers stop at the first unknown term. Another common mistake is to hide the limits to make the model look better. Stakeholders who later discover an unmentioned weakness stop trusting both the model and its author. Lead with the business result and state limits clearly.

## Key Takeaways
1. A one-page report covers the problem, what the model does, performance in business terms, limits, risks and a recommendation.
2. Turn metrics into counts people can picture, such as "of every 100 calls, about 29 lead to a subscription", and compare with a baseline.
3. Start with a 3-sentence executive summary, avoid jargon, and state limits and risks honestly.

## Hands-on Exercise
**Task:** Capstone step 2: write the one-page stakeholder report and a 3-sentence summary for an executive.
**Tools:** A document editor (Google Docs, LibreOffice Writer or Word); your L17 notebook results. Optional: a free AI assistant to check clarity, using only your own text and summary numbers.
**Steps:**
1. Collect your key numbers from L17: test-set counts, the baseline, and your subgroup results.
2. Convert each metric into a business sentence with counts, as in the example.
3. Write the six sections: problem, what the model does, performance, limits, risks and recommendation.
4. Add one small table with at most 4 numbers.
5. Write the 3-sentence executive summary and place it at the top.
6. Ask someone without a data background to read it, and replace any word they do not understand.
**What good looks like:** One page, no unexplained technical terms, performance stated as counts with a baseline comparison, at least 2 honest limits, a risk from your subgroup check, and a specific, testable recommendation.
**Time:** about 60 minutes

## Review Flags
- None. The bank and all numbers are hypothetical or come from the course's synthetic data, which was run and checked in L09 and L16; the lesson has no code, tool steps or external facts to verify.
