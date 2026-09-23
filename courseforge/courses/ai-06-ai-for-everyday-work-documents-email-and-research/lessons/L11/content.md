# L11 Build Reusable Prompts and a Personal Prompt Library

Course: AI-06 · Module: M3 · Objectives: O3, O7 · Video: 5 min

## Hook
Last month you wrote a prompt that gave you a perfect weekly report. This week you cannot remember how you wrote it, so you start again from zero. A small personal prompt library solves this problem.

## Explanation
A **reusable prompt** is a prompt you save and use again, with spaces to fill in for the details that change each time. It follows the four parts from L02: task, context, format and examples.

Here is a simple template:

```text
Task: [what you want: write / rewrite / summarise / list]
Reader: [who will read it and what they need]
Context: [the key facts for this week, no personal data]
Format: [length, structure, tone]
Example: [paste a past version you liked, with names removed]
```

The parts in square brackets change each week. Everything else stays the same. You fill in the gaps, paste it into your AI assistant and get a consistent result.

**Improving a prompt.** The first version of a prompt rarely gives the best result. Test it, look at what went wrong, and change the prompt, not just the output. For example:

- The answer was too long: add "maximum 150 words".
- The tone was too formal: add "friendly, like a message to a colleague".
- It invented details: add "Use only the facts I give you. If something is missing, write [MISSING] instead of guessing."
- It forgot a section: add the section heading to the format line.

Each fix makes the next result better. After two or three rounds, the prompt is usually reliable for that task.

**Where to keep your library.** A simple document or notes file is enough. Give each prompt a clear name, such as "Weekly status update" or "Supplier reminder". Keep the library **free of confidential data**: store only the template with empty spaces, never a filled-in version with names, figures or client details. Keep it where your employer allows work files to be stored, and follow your employer's AI policy. [REGION] Some AI tools also let you save instructions or projects inside the tool; check what your plan offers and what your employer allows. [VERSION]

**Analogy:** A prompt library is like a folder of email templates or a recipe book. You do not invent a new recipe every time you cook the same dish. You follow the version that worked, change the ingredients for today and note any improvement in the margin.

## Worked Example
Sione is a hypothetical front office supervisor at a hotel in Suva, Fiji. Every Monday he writes a short update for the hotel manager about the previous week.

His first prompt:

```text
Write a weekly update for my manager about the front office.
```

The result is generic and invents figures. He builds a reusable prompt:

```text
Task: Write a weekly front office update.
Reader: The hotel manager, who wants a quick overview.
Context: [3 to 5 bullet points of this week's facts]
Format: 3 headings (Highlights, Problems, Next week), maximum 150 words, plain and direct.
Use only the facts I give you. Do not add numbers.
```

He tests it with last week's notes (guest names removed). The result is good, but the "Problems" section sounds too negative. He adds "neutral tone, focus on solutions" to the format line. The second result is right.

He saves the template in his work notes file under "Weekly manager update", with the context line left empty.

## Common Mistake
Many people save prompts that already contain the details of one week, such as client names, prices or colleague information. The library then becomes a store of confidential data, and the prompt does not work well for the next week anyway. The correction: save only templates with empty spaces, and add the facts fresh each time, without personal or confidential data.

## Key Takeaways
1. A reusable prompt keeps the task, reader and format fixed and leaves spaces for the facts that change.
2. Improve a prompt by fixing the prompt itself after each test, for example by adding length limits or "do not guess".
3. Keep your prompt library in an approved place and free of confidential data: save templates, not filled-in versions.

## Hands-on Exercise
**Task:** Capstone step 2: write and test a reusable prompt for each of your 3 tasks from L10, and improve each prompt at least once based on what the first result got wrong.
**Tools:** Claude or ChatGPT (free tier), or your employer's approved AI tool; a document or notes app for your library.
**Steps:**
1. Open your task map from L10. For each task, look at the steps marked "AI can draft" or "AI can check".
2. Write a reusable prompt for each task using the template: Task, Reader, Context, Format, and Example if you have one.
3. Test each prompt with this week's facts, with names and confidential details removed.
4. Check each result with the 4-step checklist from L04 and note what went wrong.
5. Change the prompt to fix the problem, test again and note whether it improved.
6. Save the 3 final templates in your prompt library, with clear names and empty spaces for the facts.
**What good looks like:** A prompt library with 3 named templates. Each has a first version, a note on what went wrong, and an improved version that gives a better result. No template contains confidential or personal data.
**Time:** about 35 minutes

## Review Flags
- [VERSION] Features for saving instructions or projects inside AI tools, and which plans include them, must be checked before scripting.
- [REGION] Employer rules on where work files and prompt libraries may be stored differ by organisation and country; learners follow their own policy.
- Sione and his hotel are hypothetical.
