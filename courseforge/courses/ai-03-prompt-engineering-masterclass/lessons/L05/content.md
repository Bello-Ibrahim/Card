# L05 Showing Examples: Few-Shot Prompting

Course: AI-03 · Module: M1 · Objectives: O3 · Video: 5 min

## Hook
Sometimes you know exactly what you want but find it hard to describe. In those cases, showing is often easier than explaining.

## Explanation
**Few-shot prompting** means you include a few examples of the output you want inside your prompt. "Few" usually means two or three. A prompt with no examples is sometimes called "zero-shot".

Examples help because they show the tool several things at once: the format, the length, the tone and the way you make decisions. A description such as "label each comment by type" leaves questions open. What are the types? What do you do with a comment that is both praise and a question? Two or three examples answer these questions without long explanations.

Few-shot prompting often helps with:

- **Sorting and labelling**, such as customer comments, support tickets or survey answers.
- **Repeated writing patterns**, such as product descriptions or short social media posts in your brand voice.
- **Extracting information in a fixed shape**, such as a name, a date and an amount from each line.

A few rules make examples work well:

1. **Show the input and the output** for each example, in the same layout every time.
2. **Cover the different cases.** If there are three labels, show at least one example of each.
3. **Keep examples realistic but invented.** Do not paste real customer comments that contain names or personal details.
4. **Check the results.** The tool may copy your examples too closely, or label a difficult case wrongly.

**Analogy:** Showing examples is like bringing a shirt you already like to a tailor. You could try to describe the collar, the fit and the sleeve length in words, but the tailor understands much faster when they can see and measure a real shirt.

## Worked Example
Youssef is the guest relations manager at a hypothetical hotel in Marrakesh. Every week he receives many short guest comments and wants to sort them into "praise", "complaint" or "question".

Before:

```text
Sort these guest comments into categories.
```

The tool invents its own categories, such as "Food", "Staff" and "Other", and some comments get two labels. This is not what Youssef needs.

After:

```text
Label each guest comment as exactly one of: praise, complaint, question.
If a comment contains a complaint and something else, label it complaint.

Examples:
Comment: "The rooftop breakfast was wonderful, thank you!"
Label: praise

Comment: "Our room was not cleaned on the second day."
Label: complaint

Comment: "Can we book an airport transfer for Sunday morning?"
Label: question

Now label these comments in the same format:
[PASTE COMMENTS]
```

Youssef pastes ten invented test comments. Nine labels are correct. One comment, "Lovely staff, but is the pool heated?", is labelled "praise". He checks his rule. It only covers complaints, not questions. He adds a line: "If a comment contains a question and praise, label it question." He runs the prompt again and the label is now correct.

Notice what Youssef did. The examples set the pattern, and the extra rule handled the difficult case. He also checked every label himself, because examples improve results but do not make them perfect.

## Common Mistake
Many learners give examples that are all the same type, for example three positive comments. The tool then learns a narrow pattern and may label too many new items as positive. Make your examples cover every category, and include at least one difficult or mixed case if you can.

## Key Takeaways
1. Few-shot prompting means including two or three examples of input and output in your prompt.
2. Good examples use the same layout every time, cover every category and are invented rather than copied from real, personal data.
3. Examples often improve consistency, but you must still check each result and add a rule for difficult cases.

## Hands-on Exercise
**Task:** Write a prompt with three labelled example comments, then use it to sort ten new hypothetical customer comments, and check every label yourself.
**Tools:** Claude, ChatGPT or Gemini (free tier) [VERSION]; a notes app or spreadsheet.
**Steps:**
1. Choose a business you know, for example a bakery, a bank branch or a bus company. Choose three labels, such as praise, complaint and question.
2. Write one invented example comment for each label, with the label underneath, in the same format as Youssef's prompt.
3. Add a rule for mixed comments.
4. Write ten new invented comments. Include at least two that are difficult or mixed.
5. Run the prompt and copy the labels into a table with columns: Comment, AI label, My label, Match (yes or no).
6. If any label is wrong, add or change one rule and run the prompt again.
**What good looks like:** A complete table of ten comments, your own label next to each AI label, an honest count of matches, and one improved rule if there were errors.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini must be checked before scripting.
