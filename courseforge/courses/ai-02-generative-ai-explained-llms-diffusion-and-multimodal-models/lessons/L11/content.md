# L11 Running the Comparison

Course: AI-02 · Module: M3 · Objectives: O4, O7 · Video: 5 min (screen demo)

## Hook
Your task, input, prompt and rubric are ready. Now comes the part that feels easy: running the tests. But small mistakes here, such as a changed word in the prompt or a lost output, can make the whole comparison unfair. This lesson shows a careful way to run it.

## Explanation
Running a comparison well is about **discipline and records**. Follow the same routine for every tool.

**Before you start**

- Open your capstone document from L10 with the fixed prompt, the input and the rubric.
- Create a results folder with one sub-folder per tool.
- Create a log table with the columns: Tool, Version or model shown, Date and time, Settings changed, Output file, Scores, Notes.

**For each tool**

1. Start a **new, empty chat or project**, so earlier conversations do not affect the result.
2. Check which model or version the tool shows and write it in the log. If the tool does not show it, write "not shown". [VERSION]
3. Note any settings you change, such as temperature in Google AI Studio or the aspect ratio in an image generator. Keep settings as similar as possible between tools. [VERSION]
4. Paste the **exact** prompt and input. Do not correct or improve anything.
5. Save the **complete** output: copy text into a file, or download the image. Take a screenshot showing the tool and the output.
6. **Score the result straight away** against your rubric, before you open the next tool. This stops you from judging one tool by comparing it with another, instead of with your criteria.
7. Write notes on anything surprising: a failure, a refusal, a very long wait or an error message.

Which three tools? For a text task, you might use Claude or ChatGPT (free tier), Google AI Studio, and a third free chatbot. For an image task, use three free image generators. For a task with photos or audio, choose tools that accept uploads. Where the task needs both text and images, test each part with suitable tools and record them separately. [VERSION]

**Analogy:** Running the comparison is like a science experiment in a school laboratory. You follow the method exactly, write down every measurement when you take it and label every sample. If you change the method halfway, or try to remember the results the next day, nobody can trust the conclusion.

## Worked Example
Sione is a tourism officer at a hypothetical visitor centre in Suva, Fiji. His task: turn a public one-page information sheet about a nature park into a short list of "Frequently asked questions" for the centre's website. A presenter can follow these steps on screen. [VERSION]

1. Open the capstone document and show the fixed prompt: "Using only the text below, write 6 frequently asked questions and short answers for first-time visitors. If information is missing, do not invent it."
2. Open the first tool, a free chatbot such as Claude or ChatGPT, and start a new chat. [VERSION]
3. Read the model name shown in the interface, if any, and type it into the log with today's date. [VERSION]
4. Paste the prompt and the information sheet. Run it.
5. Copy the full answer into a file called "tool1_output". Take a screenshot.
6. Score it with the rubric: accuracy 4, clarity 5, follows structure 5, effort to fix 4. Note: "One answer adds a parking fee not in the sheet."
7. Open Google AI Studio, start a new prompt and check that the temperature is at its default value. Record it in the log. [VERSION]
8. Repeat steps 4–6 and save "tool2_output".
9. Repeat the same process with the third tool and save "tool3_output".
10. Show the completed log table with three rows.

The scores differ, but Sione does not choose a winner yet. First he checks that each row has a date, a version entry, the saved output and all scores. The analysis comes in L12.

## Common Mistake
Many learners run all three tools first and score them later from memory, or while looking at all three outputs side by side. Then the second-best output looks worse than it really is, because it is next to the best one, and details are forgotten. The correction is to score each output against the rubric straight away, then compare the scores at the end.

## Key Takeaways
1. Use a new chat for each tool, paste the exact same prompt and input, and record any settings you change.
2. Save every complete output with the tool name, the version shown and the date.
3. Score each result against your rubric straight away, before you look at the next tool.

## Hands-on Exercise
**Task:** Capstone step 2: run your task in three generative AI tools, save the outputs with the date and tool version, and score each one with your rubric.
**Tools:** Three free tools that suit your task, for example Claude or ChatGPT (free tier), Google AI Studio and a free image generator of your choice [VERSION]; your capstone document from L10; a folder for outputs.
**Steps:**
1. Create the results folder and the log table.
2. Check again that your input contains no personal or confidential data.
3. For each tool: start a new chat, record the version and date, paste the exact prompt and input, save the full output and a screenshot, and score it straight away.
4. Write at least one note per tool about a strength or a failure you noticed.
5. Check that the log is complete before you close the tools.
**What good looks like:** A results folder with three saved outputs and screenshots, and a complete log table with three rows showing tool, version (or "not shown"), date, settings, scores and notes. The prompt is the same in all three tests.
**Time:** about 45 minutes

## Review Flags
- [VERSION] A reviewer should choose the specific free tools for the demo, including a free image generator for image tasks, and check their current free limits and licence terms for generated images.
- [VERSION] Confirm where Claude, ChatGPT and Google AI Studio show the model name or version, and that Google AI Studio still shows a temperature control with a default value, before recording the screen demo.
