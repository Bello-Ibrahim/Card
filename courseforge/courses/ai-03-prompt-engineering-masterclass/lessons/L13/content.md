# L13 Turning Prompts into Reusable Templates

Course: AI-03 · Module: M3 · Objectives: O4, O6 · Video: 5 min

## Hook
If you write a good prompt once and never use it again, you lose most of its value. A template lets you, and your colleagues, get the same quality every time in a few seconds.

## Explanation
A **prompt template** is a prompt where the parts that change are replaced with clear placeholders. You already used placeholders to protect confidential data in L03. In a template, they also mark what the user must fill in.

To turn a prompt into a template:

1. **Start from a prompt that worked.** Use one you have tested and improved.
2. **Find the parts that change** each time: the audience, the document, the date, the topic.
3. **Replace them with placeholders** in capital letters and square brackets: [AUDIENCE], [DOCUMENT], [DEADLINE], [WORD LIMIT].
4. **Keep the parts that make it work**: the role, the format, the constraints, the examples and the checking instructions.
5. **Add a short instruction for the user** at the top if a placeholder is not obvious, for example "[TONE]: choose formal or friendly".

Most work tasks fit one of a few **prompt patterns** from this course:

- **Draft** from notes (L06)
- **Rewrite**: shorten, change tone or adapt (L06)
- **Summarise or extract** into a table (L07)
- **Classify** with examples (L05)
- **Analyse or compare** step by step (L08)
- **Interview first**, for tasks with unclear context (L09)

Choosing the pattern first makes each template faster to write.

**Introducing the capstone.** In the next three lessons you will build a **Personal Prompt Library**: 15 tested, documented templates for your own job role. To choose the 15 tasks, look for tasks that are **frequent** (weekly or more), **time-consuming**, and **safe** to do with AI, meaning they do not require personal or confidential data. Those tasks usually save the most time.

**Analogy:** A prompt template is like a form letter with blank lines. The structure, tone and important sentences are already written. Each time, you only fill in the name, the date and the details, and the quality stays the same.

## Worked Example
Ana is a pharmacy manager at a hypothetical chain of pharmacies in Lisbon. Every week she writes a short update for her staff. Here is a prompt she tested and improved:

```text
You are an experienced pharmacy manager. Write a weekly update for
pharmacy assistants about the new opening hours from 1 March and the
flu vaccine appointment system. Friendly, clear tone. 5 bullet points,
under 120 words. Do not add any facts that are not in my notes.
Notes: [...]
```

She turns it into a template:

```text
PATTERN: Draft from notes
You are an experienced [JOB ROLE]. Write a weekly update for [AUDIENCE]
about [TOPICS]. [TONE] tone. [NUMBER] bullet points, under [WORD LIMIT]
words. Do not add any facts that are not in my notes.
Notes: [PASTE NOTES - no personal or patient data]
```

The reminder "no personal or patient data" is part of the template, so every future user sees it. Ana tests the template with a different topic, stock changes, and the result has the same quality.

She then lists her 15 recurring tasks, such as "reply to supplier delay", "summarise head-office circular", "rota change message" and "classify customer feedback", and writes the pattern next to each.

## Common Mistake
Some learners replace too much with placeholders, including the format and constraints. A template like "Write [OUTPUT] for [AUDIENCE] in [FORMAT]" is too empty to help anyone. Keep fixed everything that made the original prompt work, and use placeholders only for what really changes.

## Key Takeaways
1. A template replaces the changing parts of a tested prompt with clear placeholders, such as [AUDIENCE] or [DOCUMENT].
2. Keep the role, format, constraints and checking instructions fixed, because they are what make the template reliable.
3. For the capstone, choose 15 tasks that are frequent, time-consuming and safe to do with AI.

## Hands-on Exercise
**Task:** Capstone step 1: list 15 recurring tasks from your job, choose the prompt pattern for each, and turn your first three prompts into templates with placeholders.
**Tools:** A spreadsheet or document (free options such as Google Sheets or LibreOffice work); Claude, ChatGPT or Gemini (free tier) [VERSION].
**Steps:**
1. List 15 tasks you do at least monthly. Mark any that need confidential data and replace them with safer tasks.
2. Next to each task, write its pattern: draft, rewrite, summarise or extract, classify, analyse, or interview first.
3. Choose three tasks and write a full prompt for each, using the six parts.
4. Test each prompt once and improve it.
5. Turn each into a template with placeholders.
6. Start a prompt card for each template with these fields:

```text
Name:
Version: v1
Purpose (one line):
Pattern:
Prompt template:
Inputs (what to put in each placeholder):
Example input:
Example output (short extract):
Test notes (tests, scores, changes):
Tool and date of last test:
```

**What good looks like:** A list of 15 tasks, each with a pattern, and three templates with placeholders only where content changes, each on a started prompt card.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini, and of the named free spreadsheet tools, must be checked before scripting.
