# L10 Fixing Weak Outputs | Presenter Script

Course: AI-03 · Video: 5 min · Words: 680

## Hook
When an AI output is disappointing, most people delete everything and start again. But often, a small change to one part of the prompt is faster, and gives a better result. Today, you will learn how to find that part.

## Explain
In the last lesson, you built results through conversation. Now, what do you do when a result is weak? Before you fix a prompt, find the cause. Four questions cover most weak outputs.

Question one: was the task unclear? The output does something different from what you wanted. The fix is a precise verb, such as review, compare, or list the risks in. Question two: was context missing? The output is correct, but generic, or makes wrong guesses about the audience. The fix is to add audience, purpose, background or material.

Question three: was the format specified? The content is fine, but it is too long, or has no structure. The fix is to name the format and give a number for length. Question four: did instructions conflict? For example, be detailed and under fifty words in the same prompt. The fix is to remove one instruction, or say which one matters more.

After you name the cause, make one targeted change, and run the prompt again. If you change five things at once, you will not know which change helped.

If the cause is harder to see, two more techniques can help. Add an example of the output you want. Or ask the tool which parts of your prompt were unclear. That answer is not always reliable, but it can give you useful ideas.

Think of a mechanic who hears a strange noise in a car. A good mechanic does not replace the whole engine. They check a short list of likely causes, change one part, and test the car again.

## Demonstrate
Let's look at three cases. Ingrid is an office manager at an architecture firm in Stockholm. Here are three weak outputs she received, and how she diagnosed each one.

Case one. She asked the tool to look at a supplier contract summary, and got a shorter summary of the same text. But she wanted to know which terms were risky. The cause is an unclear task. Her fix asks for the three terms with the most risk for a small office, each explained in one sentence.

Case two. She asked for a welcome message for a new employee, and got a friendly message about our exciting company, with no useful information. The cause is missing context. Her fix names the role and start day, the arrival time, who to ask for, and what to bring, with a warm tone and under one hundred words.

Case three. She asked for a detailed, complete report on office energy use, in under fifty words. She got fifty words that said almost nothing. The cause is conflicting instructions. Her fix chooses one goal: three bullet points for the team newsletter, focused on the biggest change since last month.

In each case, Ingrid changed one part of the prompt, not all of it. This habit will matter when you build your prompt library in module three.

A common mistake is to blame the tool, and try a different one immediately. Sometimes another tool does help. But if the prompt has a clear weakness, the same weakness usually gives a weak result in any tool. Diagnose first, fix the prompt, and only then compare tools.

## Recap
Let's recap. First, four questions diagnose most weak outputs: an unclear task, missing context, a missing format, or conflicting instructions. Second, name the cause, then make one targeted change and test again. Third, starting again or changing tools is rarely the fastest fix when the prompt itself has a clear weakness.

## CTA
Now it is your turn. In the exercise below this video, you will diagnose three weak outputs, name the cause of each one, and write an improved prompt with one targeted change. It takes about twenty minutes. That completes week two. In the next lesson, we look at checking outputs for accuracy, bias and confidentiality. See you there.

## Thumbnail
Headline: Diagnose, Don't Delete
Image: Navy background, a four-point diagnosis checklist beside a wrench icon on a prompt card, headline in teal Inter Bold.

## Production Notes
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini must be checked before recording (content.md Review Flags).
- Ingrid and her architecture firm in Stockholm are hypothetical. Do not show a real firm name or logo in stock footage.
- Each case's weak prompt and fixed prompt appear side by side on comparison or code slides, using the exact text from content.md, including [OFFICE MANAGER] and [PASTE FIGURES]. The voiceover summarises the fixes.
- Asking the tool to explain what was unclear is presented as 'not always reliable'.
