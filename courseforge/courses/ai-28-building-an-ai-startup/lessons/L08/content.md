# L08 Making the AI Part Work: Prompts and Quality Checks

Course: AI-28 · Module: M2 · Objectives: O4, O6 · Video: 5 min

## Hook
Your prototype works on the example you tried. But your users will not type your example. They will write in a hurry, make spelling mistakes, and ask for things you never imagined. How do you know the AI part will still work?

## Explanation
AI models do not give the same quality of answer every time, and they can be confidently wrong. A founder cannot remove this risk completely, but can reduce it and plan for it. Three tools help most.

**1. Clear instructions.** A good prompt for a product says:

- the **role** and the **task** ("You write replies to customer reviews for a small restaurant");
- the **rules** ("Never offer refunds or discounts. Never argue with the customer.");
- the **format** ("Three sentences at most. Friendly and professional.");
- what to do when **unsure** ("If the review mentions food poisoning, illness or a legal threat, do not write a reply. Output only: NEEDS HUMAN.").

**2. Good examples.** Show the model one or two examples of a good input and a good output. Examples often teach style and format better than long explanations.

**3. A small test set.** A **test set** is a list of inputs with a description of what a good answer looks like. Include normal cases, difficult cases and "should refuse" cases. Every time you change the prompt, run the whole test set again, because a change that fixes one case can break another.

Score each result simply: **pass**, **partial** or **fail**, with a short reason. Your **pass rate** is the number of passes divided by the number of cases.

You also need a **fallback plan**: what the product does when the AI is wrong or unsure. Common options are sending the case to a person, asking the user for more information, or showing the draft only after a human approves it. In high-stakes areas such as health, money or law, a human check is often necessary.

**Analogy:** In a busy restaurant, a new chef follows the recipe card exactly. That is your prompt. The head chef tastes each dish before it leaves the kitchen. That is your quality check. If a dish is wrong, it goes back to the kitchen instead of to the customer. That is your fallback plan.

## Worked Example
Putri is a hypothetical founder in Yogyakarta, Indonesia. Her MVP writes draft replies to online reviews for small restaurants, in Indonesian or English. She creates 15 test cases in a sheet, with made-up reviews (no real customer names):

| # | Type | Example input | Good answer |
|---|---|---|---|
| 1–6 | Normal | Positive or mildly negative reviews | Polite, specific, 3 sentences at most |
| 7–10 | Difficult | Mixed languages, spelling mistakes, sarcasm | Correct tone, reply in the reviewer's language |
| 11–13 | Should refuse | Food poisoning, legal threat, personal attack on a staff member | Only "NEEDS HUMAN" |
| 14–15 | Tricky | A review asking for a discount; a review about another restaurant | No discount offered; a polite note that it may be the wrong place |

**Prompt v1** passes 9 of 15. The failures: two replies offered a free dessert, two sarcastic reviews received cheerful thanks, and two "should refuse" cases received normal replies.

For **Prompt v2**, she adds the rule "Never offer anything for free", one example of a sarcastic review with a good reply, and a clearer list of topics that require "NEEDS HUMAN". Now 13 of 15 pass. Both "should refuse" failures are fixed. One sarcastic review still fails, and one reply is slightly too long.

Putri decides that 13 of 15 is good enough for a first test, **because** every draft is shown to the restaurant owner before it is posted. The human approval is her fallback plan. She keeps the two failures in her test set for the next round.

## Common Mistake
Founders often test a prompt on two or three easy examples, see good results and move on. Then real users bring the difficult cases. Another mistake is assuming that a newer or larger model will fix every problem. A better model can help, but you only know if it helps by running the same test set. Finally, do not use real customer data in test sets unless you have permission; made-up but realistic examples work well.

## Key Takeaways
1. Clear instructions, one or two good examples, and a small test set make AI output more reliable.
2. Run the whole test set after every prompt change and score each case as pass, partial or fail.
3. Plan what the product does when the AI is wrong or unsure, such as a human check or a request for more information.

## Hands-on Exercise
**Task:** Write 15 test cases for your MVP in a sheet, run them, score the results, and improve your instructions until most cases pass.
**Tools:** A free spreadsheet; your prototype from L07 or Claude (free plan) to run the prompt.
**Steps:**
1. Create a sheet with columns: number, type, input, good answer, result (v1), score (v1), result (v2), score (v2), notes.
2. Write 15 made-up cases: about 6 normal, 4 difficult, 3 that should be refused or sent to a human, and 2 tricky ones.
3. Run every case through your current prompt and paste each result.
4. Score each result as pass, partial or fail, with a one-line reason.
5. Change the prompt to fix the most common failure. Save it as a new version.
6. Run all 15 cases again, not only the failed ones, and compare pass rates.
7. Write your fallback plan in one or two sentences.
**What good looks like:** A complete sheet with 15 varied cases, two scored rounds, a higher pass rate in round two, all "should refuse" cases handled safely, and a written fallback plan.
**Time:** about 50 minutes

## Review Flags
- None. The founder and test cases are hypothetical, and the lesson names no specific model, price or tool feature.
