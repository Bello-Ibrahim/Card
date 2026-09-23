# L05 Showing Examples: Few-Shot Prompting | Presenter Script

Course: AI-03 · Video: 5 min · Words: 695

## Hook
Sometimes you know exactly what you want, but you find it hard to describe. In those cases, showing is often easier than explaining. Today, you will learn how to show the AI what you mean.

## Explain
In the last lesson, you controlled format and tone with clear instructions. Now we add the sixth part of the structured prompt: examples. This is called few-shot prompting.

Few-shot prompting means you include a few examples of the output you want inside your prompt. Few usually means two or three. A prompt with no examples is sometimes called zero-shot. Most of the prompts you have written so far in this course were zero-shot.

Examples help because they show several things at once: the format, the length, the tone and the way you make decisions. A description like label each comment by type leaves questions open. What are the types? And what about a comment that is both praise and a question? Two or three examples answer this without long explanations.

Few-shot prompting often helps with sorting and labelling, like customer comments or survey answers. It helps with repeated writing patterns, like short posts in your brand voice. And it helps with extracting information in a fixed shape, like a name, a date and an amount from each line.

A few rules make examples work well. Show the input and the output for each example, in the same layout every time. Cover the different cases, so if there are three labels, show at least one of each. Keep examples realistic, but invented. And check the results, because the tool may copy your examples too closely.

Think of a tailor. You could describe the collar, the fit and the sleeves in words. But the tailor understands much faster when you bring a shirt you already like. Examples work the same way for an AI tool.

## Demonstrate
Let's try it. Youssef is the guest relations manager at a hotel in Marrakesh. Every week, he receives many short guest comments. He wants to sort each one into praise, complaint or question.

His first prompt simply asks the tool to sort the comments into categories. The tool invents its own categories, such as food, staff and other, and some comments get two labels. This is not what he needs.

His new prompt names the three labels and says each comment gets exactly one. It adds a rule: if a comment contains a complaint, label it complaint. Then it shows three short example comments, one for each label, each followed by its label. Finally, it asks the tool to label new comments in the same format.

Youssef tests it with ten invented comments. Nine labels are correct. But one comment, lovely staff, but is the pool heated, is labelled praise. His rule covers complaints, not questions. So he adds one more line: if a comment contains a question and praise, label it question. He runs it again, and the label is now correct.

Notice what Youssef did. The examples set the pattern, and the extra rule handled the difficult case. He still checked every label himself, because examples improve results, but do not make them perfect.

A common mistake is to give examples that are all the same type, such as three positive comments. The tool then learns a narrow pattern, and may label too many new items as positive. Cover every category, and include a mixed case if you can.

## Recap
Let's recap. First, few-shot prompting means including two or three examples of input and output in your prompt. Second, good examples use the same layout, cover every category, and are invented rather than copied from real, personal data. Third, examples often improve consistency, but you must still check each result, and add a rule for difficult cases.

## CTA
Now it is your turn. In the exercise below this video, you will write a prompt with three labelled example comments, use it to sort ten new invented comments, and check every label yourself. It takes about twenty minutes. That completes week one. In the next lesson, we start on everyday work with writing and rewriting emails, reports and messages. See you there.

## Thumbnail
Headline: Show, Don't Describe
Image: Navy background, three small labelled example cards feeding into a prompt window, headline in teal Inter Bold.

## Production Notes
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini must be checked before recording (content.md Review Flags).
- Youssef and his hotel in Marrakesh are hypothetical, and all guest comments are invented. Do not show a real hotel name or logo in stock footage.
- The full few-shot prompt appears on a code slide with the exact text from content.md; the voiceover summarises it. The placeholder [PASTE COMMENTS] is shown on screen only.
- Examples are presented as often improving consistency, not as making results perfect.
