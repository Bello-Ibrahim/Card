# L12 Should I Trust This AI? A Practical Checklist

Course: AI-01 · Module: M3 · Objectives: O6, O7 · Video: 5 min

## Hook
An app says a photo of your plant shows a disease. A chatbot gives you a clear summary of a new law. A website says an AI chose these products "just for you". Should you act on any of them? You do not need to be an engineer to decide. You need five good questions.

## Explanation
In this course you have learned how models learn from data (L03), how they are trained and used (L04), how they are tested (L08), why chatbots hallucinate (L09) and how biased data leads to unfair results (L10). You also trained your own model (L11). This lesson brings all of that together into a checklist you can use with any AI system.

**The 5-question trust checklist**

1. **What data did it learn from?** Were the examples varied and representative of the people and situations it will meet? If you cannot find out, treat that as a warning sign.
2. **How was it tested?** Was it tested on new examples it never saw? Were results checked for different groups, not only as one overall score? Remember overfitting from L08.
3. **Who could it fail?** Think about the groups or situations that were rare in the data. These are the cases where mistakes are most likely.
4. **Can I verify the output?** Can you check the answer against a reliable source, a second opinion or your own knowledge? A fluent answer is not a verified answer.
5. **What happens if it is wrong?** A wrong song recommendation costs you a few minutes. A wrong medical, legal or financial answer can cause real harm. The higher the cost of a mistake, the more checking and human review you need.

You rarely get a perfect answer to every question. The aim is not to reject AI. The aim is to match your level of trust to the evidence and to the risk.

**Analogy:** Think of using the checklist like checking a used car before you buy it. You ask where it has been driven, whether it passed an inspection, what problems it is known for, whether you can take it for a test drive, and what it would cost you if it broke down on a long journey. You would not refuse to buy every used car. You would simply decide carefully, based on what you found out.

## Worked Example
Sofía works for a farming cooperative in Mendoza, Argentina. Members want to use a free phone app that identifies grape-leaf diseases from a photo. She uses the checklist:

1. **Data:** The app's website says it learned from leaf photos, but does not say which regions or grape varieties. Sofía notes this as unknown.
2. **Testing:** No test results are published. Sofía runs a small test herself: she photographs 15 leaves that an expert has already checked. The app is correct on most healthy leaves but misses some early-stage disease.
3. **Who could it fail:** Local grape varieties and leaves photographed in strong midday sun seem to cause more mistakes.
4. **Verify:** Members can send unclear cases to the cooperative's plant expert.
5. **If wrong:** A missed disease could spread across a field, so the cost is high.

Her decision: members may use the app as a first check, but any "healthy" result on a leaf that looks unusual must still be shown to the expert.

## Common Mistake
Many people think trust is a yes-or-no decision: either "AI is reliable" or "AI cannot be trusted". In practice, the same system can be trustworthy for one task and not for another. The correction is to use the checklist for each specific use, and to decide *how* to use the output (as a draft, a first check, or a final decision) rather than simply whether to use it.

## Key Takeaways
1. Ask five questions: What data did it learn from? How was it tested? Who could it fail? Can I verify the output? What happens if it is wrong?
2. Match your trust to the evidence and to the cost of a mistake. High-risk decisions need verification and a responsible person.
3. The same checklist helps you explain your own model's strengths and weaknesses in your capstone.

## Hands-on Exercise
**Task:** Capstone step 2: write a one-page explanation of how your classifier learned, where it failed, and why.
**Tools:** The model, test table and screenshots from L11; any word processor or notes app (free options such as Google Docs work well). Optional: ChatGPT or Claude (free tier) to give feedback on clarity, but the thinking and writing must be your own.
**Steps:**
1. **How it learned (about one paragraph).** Describe your classes, how many images you added and how you varied them. Use the terms data, features, labels, training and prediction correctly.
2. **How you tested it.** Explain that you used 10 new images, and summarise the results from your table (for example, "8 of 10 correct").
3. **Where it failed and why.** Describe at least 2 mistakes. Give a likely reason for each, such as a background that was missing from the training data, similar-looking objects, or overfitting to one lighting condition.
4. **Trust checklist.** Answer the 5 checklist questions for your own model in one or two sentences each.
5. **Improvement.** Suggest one specific change to the data that could improve the model.
6. Keep it to one page. Attach your test table and screenshots. Check your work against the capstone rubric before you submit.
**What good looks like:** A clear, honest page that a friend with no technical background could understand. It uses the course terms correctly, links each failure to a reason in the data, applies all 5 checklist questions, and proposes a realistic improvement.
**Time:** about 40 minutes

## Review Flags
- None. The worked example is hypothetical, and the checklist and capstone steps follow the approved curriculum and rubric.
