# L10 Fixing Weak Outputs

Course: AI-03 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
When an AI output is disappointing, most people delete everything and start again. Often a small change to one part of the prompt is faster and gives a better result.

## Explanation
Before you fix a prompt, find the cause. Four questions cover most weak outputs.

**1. Was the task unclear?** The output does something different from what you wanted. For example, you asked to "look at" a report and got a summary, but you wanted feedback. Fix: use a precise verb. "Review", "summarise", "compare", "list the risks in".

**2. Was context missing?** The output is correct but generic, or makes wrong assumptions about the audience or situation. Fix: add the audience, purpose, background or material (L03).

**3. Was the format specified?** The content is fine, but it is too long, in paragraphs instead of a table, or has no structure. Fix: name the format and give numbers for length (L04).

**4. Did instructions conflict?** The output seems confused or ignores part of the prompt. For example, "be detailed" and "under 50 words" in the same prompt, or "formal" in one line and "chatty" in another. Fix: remove one instruction, or say which one is more important.

After you name the cause, make **one targeted change** and run the prompt again. If you change five things at once, you will not know which change helped. This habit matters for the prompt library you will build in Module 3.

Two more techniques can help when the cause is harder to see:

- **Add an example** of the output you want (L05).
- **Ask the tool to explain.** "Which parts of my prompt were unclear to you?" The answer is not always reliable, but it can give useful ideas.

**Analogy:** Fixing a prompt is like a mechanic finding the cause of a noise in a car. A good mechanic does not replace the whole engine. They check a short list of likely causes, change one part and test the car again.

## Worked Example
Ingrid is an office manager at a hypothetical architecture firm in Stockholm. Here are three weak outputs she received, with her diagnosis.

**Case 1.** Prompt: "Look at this supplier contract summary." Output: a shorter summary of the same text. Ingrid wanted to know which terms were risky.
Cause: unclear task. Fix:

```text
List the three terms in this contract summary that carry the most
risk for a small office, and explain each in one sentence.
```

**Case 2.** Prompt: "Write a welcome message for a new employee." Output: a friendly message about "our exciting company" with no useful information.
Cause: missing context. Fix:

```text
Write a welcome message for a new receptionist starting Monday. Tell
them to arrive at 08:30, ask for [OFFICE MANAGER], and bring ID for
their building pass. Warm tone, under 100 words.
```

**Case 3.** Prompt: "Write a detailed, complete report on our office energy use in under 50 words." Output: 50 words that say almost nothing.
Cause: conflicting instructions. Fix:

```text
Summarise our office energy use in 3 bullet points for the monthly
team newsletter. Focus on the biggest change since last month.
[PASTE FIGURES]
```

In each case, Ingrid changed one part of the prompt, not all of it.

## Common Mistake
Many learners blame the tool and try a different tool immediately. Sometimes another tool does help, but if the prompt has a clear weakness, the same weakness usually gives a weak result in any tool. Diagnose first, fix the prompt, and only then compare tools, as you will do in L12.

## Key Takeaways
1. Four questions diagnose most weak outputs: unclear task, missing context, missing format, or conflicting instructions.
2. Name the cause, then make one targeted change and test again.
3. Starting again or changing tools is rarely the fastest fix when the prompt itself has a clear weakness.

## Hands-on Exercise
**Task:** Diagnose three weak AI outputs, name the cause of each, and write an improved prompt that fixes it.
**Tools:** A notes app or paper. Optional: Claude, ChatGPT or Gemini (free tier) [VERSION] to test your fixes.
**Steps:**
1. Read these three weak prompts and outputs:
   - A: Prompt "Help with the training day." Output: general tips about adult learning. The learner wanted an agenda for a 6-hour day.
   - B: Prompt "Write a friendly but strictly formal reminder about unpaid invoices." Output: a message that sounds unsure and mixed.
   - C: Prompt "Explain our new expense policy to staff." Output: a long explanation that invents rules the company does not have.
2. For each, name the cause using the four questions.
3. Write an improved prompt with one targeted change. Use placeholders for any company details.
4. Optional: run your improved prompts and check whether the cause is fixed.
**What good looks like:** A: unclear task (fix: "Create an agenda for a 6-hour training day..."). B: conflicting instructions (fix: choose one tone). C: missing context (fix: paste the policy points and say "use only these rules"). Each fix changes one main part.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini must be checked before scripting.
