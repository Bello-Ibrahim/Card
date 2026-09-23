# L04 Controlling Format, Length and Tone

Course: AI-03 · Module: M1 · Objectives: O1, O3 · Video: 5 min

## Hook
The same information can be a one-line message, a table or a polite email. If you do not say which one you want, the AI chooses for you, and it often chooses something longer than you need.

## Explanation
Three parts of the structured prompt control how the output looks and sounds: format, constraints and, for style, tone.

**Format** is the shape of the output. Be specific:

- "a table with columns Task, Owner, Status"
- "5 bullet points, one sentence each"
- "an email with a subject line"
- "a slide outline: a title and 3 bullet points per slide, for 4 slides"

**Length** is a constraint. Numbers work better than words like "short". "Under 100 words", "3 sentences" or "one line" are easier for the tool to follow than "brief". Word limits are not always exact, so check the result.

**Reading level** is also a constraint. "Use simple words for readers who speak English as a second language" or "explain for someone with no finance background" often helps.

**Tone** describes the voice: formal, friendly, neutral, firm, warm, direct. Two words together often work well, for example "polite but firm" or "warm and professional". If you have a sample of the tone you want, you can paste it in, which you will practise in L05.

A useful habit is to put format and length at the end of your prompt, on their own lines. This keeps them easy to see and easy to change.

**Analogy:** Asking an AI for content without a format is like asking a caterer for "food for a meeting". You might get a three-course lunch when you wanted coffee and biscuits for ten people. Say the shape and the quantity, and you get what the meeting needs.

## Worked Example
Kenji is a project manager at a hypothetical equipment manufacturer in Osaka. His project to install a new packaging line is one week late because a part is delayed. He needs to tell three different people.

First, his project notes go into the prompt:

```text
Project notes: packaging line install. Motor part delayed at supplier,
arrives 12 [MONTH]. Testing moves from week 3 to week 4. Budget not
affected. Team: Aiko (electrical), Ben (mechanical), Chen (testing).
Supplier must confirm delivery time by Friday.
```

For his director:

```text
Using the notes above, write ONE line (under 25 words) for my
director. Formal tone. Say the delay, the new week and that budget is
not affected.
```

For his team:

```text
Using the notes above, make a table with columns: Team member, What
changes, New date. Neutral tone. No extra text before or after the table.
```

For the supplier:

```text
Using the notes above, write an email to the supplier under 100 words.
Polite but firm. Ask them to confirm the delivery time by Friday.
Include a subject line.
```

The results are three very different outputs from the same facts. Kenji notices that the tool added a sentence before the table even though he asked for "no extra text". He deletes it. Small failures like this are normal, and noticing them is part of the skill.

## Common Mistake
Many people write "keep it short" or "make it professional" and are surprised when the result is still long or too stiff. These words mean different things to different readers. Replace them with measurable instructions: a number of words or bullet points, a named format, and two tone words. If the tool still ignores an instruction, repeat it at the end of the prompt, or ask for a fix in a follow-up message: "Shorten this to 50 words."

## Key Takeaways
1. Name the format exactly: table with named columns, number of bullet points, email with subject line, or slide outline.
2. Use numbers for length and plain descriptions for reading level. Words like "short" are too vague.
3. Describe tone with one or two clear words, and check the output, because tools do not always follow every instruction.

## Hands-on Exercise
**Task:** Ask for the same content in three formats, each with a length limit, and note which instruction the tool followed least well.
**Tools:** Claude, ChatGPT or Gemini (free tier) [VERSION]; a notes app.
**Steps:**
1. Write 4 to 6 lines of non-confidential notes about a real or hypothetical work update. Use placeholders for names.
2. Ask for a one-line message under 25 words for a senior manager.
3. In the same chat, ask for a table with three named columns for your team.
4. Ask for an email under 100 words with a subject line, in a tone you name.
5. Check each output: count the words, check the columns and check the tone.
6. Write one sentence about which instruction the tool followed least well, and one follow-up prompt that could fix it.
**What good looks like:** Three outputs that match their formats, a word count for each, and a clear note such as "The email was 128 words, not under 100. Fix: 'Shorten this email to under 100 words and keep the subject line.'"
**Time:** about 20 minutes

## Review Flags
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini must be checked before scripting.
