# L12 Testing a Prompt Across Tools

Course: AI-03 · Module: M3 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
You have a prompt that works well in one tool. Will it work as well in another tool, or next month in the same tool? The only way to know is to test it.

## Explanation
Claude, ChatGPT and Gemini are built by different companies and trained in different ways. The same prompt can give different length, structure, tone and sometimes different facts in each one. Tools are also updated, so a result can change over time. [VERSION]

A fair test keeps everything the same except the tool:

1. **Same prompt.** Copy it exactly. Do not improve it between tools.
2. **Same input.** Use the same hypothetical or non-confidential material.
3. **New chat.** Start a fresh conversation in each tool, so earlier messages do not affect the result. Saved instructions can also affect results, so note if you use them.
4. **Simple scores.** Score each output from 1 (poor) to 5 (excellent) on three criteria:
   - **Accuracy**: facts are correct and nothing is invented or missing.
   - **Format**: it follows the requested format and length.
   - **Tone**: it suits the audience.
5. **Record the date and tool.** Write the tool name, the model if it is shown, and the date. [VERSION]

Scores are your judgement, not a scientific measurement. That is fine. The aim is to make a practical choice for one task, not to find the "best AI". A tool that scores well for summaries may score less well for creative writing. Free plans may also limit how many messages you can send in a day, so plan your tests. [VERSION]

**Analogy:** Testing a prompt across tools is like testing one recipe in three different ovens. Same ingredients, same steps, same time. If one cake is dry, you know it is the oven, not the recipe, and you write a note on the recipe card.

## Worked Example
Chloé is a communications officer at a hypothetical environmental charity in Montréal. She wants to test her prompt for turning event notes into a short social media post.

**Screen demo steps for the presenter** (check each step in the live tools first [VERSION]):

1. Open three browser tabs: Claude, ChatGPT and Gemini. Sign in to the free plan of each.
2. In a notes app, show the prompt and input:

```text
Write a post under 60 words for our charity's social media page about
the event below. Friendly and hopeful tone. End with one question for
readers. Do not add figures that are not in the notes.

Notes: river clean-up on Saturday, 45 volunteers, 120 kg of waste
collected, next clean-up in [MONTH].
```

3. Start a new chat in Claude. Paste the prompt exactly. Show the output.
4. Repeat in ChatGPT, then in Gemini, with the same prompt and a new chat.
5. Place the three outputs side by side on screen.
6. Open a simple spreadsheet with columns: Tool, Date, Accuracy, Format, Tone, Total, Notes.
7. Score each output aloud. For example: one tool counts 64 words (Format 3); one adds "our biggest event ever", which is not in the notes (Accuracy 2); one follows every instruction (Accuracy 5, Format 5, Tone 4).
8. Fill in the Notes column and show the final choice: "Use the highest-scoring tool for this task. Retest in 3 months."

Chloé now has evidence for her choice, not only a feeling.

## Common Mistake
Many learners change the prompt a little in each tool, or test in a chat that already contains earlier messages. Then the comparison is not fair. Another common mistake is testing once and deciding forever. Tools change, so record the date and retest important prompts from time to time.

## Key Takeaways
1. A fair test uses the same prompt, the same input and a new chat in each tool.
2. Score each output from 1 to 5 on accuracy, format and tone, and record the tool and the date.
3. The best tool depends on the task, and results can change when tools are updated, so retest important prompts.

## Hands-on Exercise
**Task:** Run one of your prompts in Claude, ChatGPT and Gemini, score each output from 1 to 5 on three criteria, and record which tool you would use for this task.
**Tools:** Claude, ChatGPT and Gemini (free tiers) [VERSION]; a spreadsheet or notes app.
**Steps:**
1. Choose one prompt you wrote in this course, with non-confidential input.
2. Create a table with columns: Tool, Date, Accuracy, Format, Tone, Total, Notes.
3. Run the prompt in a new chat in each tool, without changing it.
4. Score each output and write one note explaining the lowest score.
5. Write one sentence: which tool you would use for this task and why.
**What good looks like:** A complete table with three rows, a date, scores with reasons, and a clear choice such as "Tool B: correct figures and under the word limit; the others added details."
**Time:** about 25 minutes

## Review Flags
- [VERSION] Free-tier usage limits of Claude, ChatGPT and Gemini may restrict how many tests learners can run in one day; check current limits before scripting.
- [VERSION] Whether each tool shows the model name, how tools are updated, and whether a free account is needed must be checked before scripting.
- [VERSION] Every screen demo step, including sign-in and new-chat actions, must be checked in the live tools before recording.
