# L08 Thinking Tasks: Analysis, Planning and Decisions

Course: AI-03 · Module: M2 · Objectives: O3, O4 · Video: 5 min

## Hook
"Which option should I choose?" is a question AI tools are happy to answer, often with great confidence. But a confident answer is only as good as the reasoning and the information behind it.

## Explanation
For writing tasks, you mostly check the wording. For thinking tasks, such as analysis, planning and decisions, you need to see the reasoning. Four prompt techniques often help.

**1. Ask it to work step by step.** "Work through this step by step before you give a recommendation." Asking for the steps makes the reasoning visible, so you can check each step. With many tools this often improves the result, but it does not guarantee a correct answer. [VERIFY]

**2. Ask it to list its assumptions.** "List the assumptions you are making." AI tools fill gaps with assumptions, just as they do in writing. Seeing them lets you correct the wrong ones.

**3. Name the criteria.** Instead of "which is best?", say "compare these options on cost, reliability and ease of use, and show the result in a table". Your criteria reflect your priorities, which the tool cannot know.

**4. Ask it to ask you questions first.** "Before you answer, ask me up to five questions about anything you need to know." This is useful when you are not sure what context matters.

After the analysis, one more request is very useful: **"What is the weakest assumption in your analysis?"** This asks the tool to question its own answer and often shows where you need to check facts yourself.

Remember that the tool does not know current prices, local conditions or your finances unless you tell it. The decision remains yours.

**Analogy:** Using AI for a decision is like asking a well-read friend to help you compare three flats to rent. They can organise your thinking and point out things you forgot. But they have not visited the flats, so you still check the facts before you sign.

## Worked Example
Ravi runs a small hypothetical café in Chennai. He wants to start delivery and is comparing three hypothetical delivery partners. He has their offers written down.

Before:

```text
Which delivery partner is best for my café?
```

The answer is a general list of things to consider, with no clear recommendation.

After:

```text
I run a small café. I want to offer delivery within 5 km, about
30 orders a day, mostly at lunchtime.
Compare these three delivery partners on: cost per order, delivery
time at lunch, and how much control I have over customer service.

Partner A: [FEES AND TERMS]
Partner B: [FEES AND TERMS]
Partner C: [FEES AND TERMS]

Work step by step. First list your assumptions. Then show a table
comparing the three on my criteria. Then give a recommendation in
two sentences.
```

The tool lists assumptions, including "average order value of about [AMOUNT]" and "lunchtime delivery times are similar for all three". Ravi corrects the first assumption with his real figure. Then he asks: "What is the weakest assumption in your analysis?" The tool answers that it had no information about lunchtime delivery times and assumed they were equal. Ravi decides to test all three partners for one week before choosing.

The AI did not make the decision. It organised the information and showed Ravi what he still needed to find out.

## Common Mistake
Many learners ask "What should I do?" and follow the recommendation without reading the reasoning. A recommendation can sound certain even when it rests on a guessed number. Always read the assumptions, correct any that are wrong, and ask for the weakest assumption before you act.

## Key Takeaways
1. For thinking tasks, ask the tool to work step by step, list its assumptions and compare options on criteria you name.
2. Asking "What is the weakest assumption in your analysis?" often shows what you need to check.
3. Step-by-step prompts often help, but they do not guarantee a correct answer. The decision and the fact-checking stay with you.

## Hands-on Exercise
**Task:** Use a step-by-step prompt to compare two or three options for a real decision at work, then ask the AI to list the weakest assumption in its own analysis.
**Tools:** Claude, ChatGPT or Gemini (free tier) [VERSION]; a notes app.
**Steps:**
1. Choose a real, non-confidential decision, for example two software tools, three training providers or two ways to organise a team rota.
2. Write the situation in 2 or 3 lines and describe each option. Use placeholders for supplier names and prices if they are confidential.
3. Name three criteria that matter to you.
4. Ask the tool to work step by step, list its assumptions, compare the options in a table and give a short recommendation.
5. Correct any wrong assumptions in a follow-up message.
6. Ask: "What is the weakest assumption in your analysis?"
7. Write two lines: what you learned, and what you still need to check yourself.
**What good looks like:** A comparison table based on your own criteria, at least one corrected assumption, the tool's weakest assumption, and a clear note of what you will check before deciding.
**Time:** about 25 minutes

## Review Flags
- [VERIFY] The claim that asking for step-by-step reasoning improves results varies between models. The script must present it as "often helps", not as a guarantee.
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini must be checked before scripting.
