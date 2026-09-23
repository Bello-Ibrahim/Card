# L15 Documenting and Sharing Your Library

Course: AI-03 · Module: M3 · Objectives: O6 · Video: 5 min

## Hook
Six months from now, will you remember why a template says "do not make promises"? Will a new colleague know which placeholder to fill? Good documentation turns your prompts into a tool other people can trust.

## Explanation
Each prompt in your library gets one **prompt card** with the same fields. You started these cards in L13:

- **Name**: short and clear, such as "Supplier delay reply".
- **Version**: v1, v2, v3. Raise it every time you change the template.
- **Purpose**: one line on what the prompt is for and when to use it.
- **Pattern**: draft, rewrite, summarise or extract, classify, analyse, or interview first.
- **Prompt template**: the full text with placeholders.
- **Inputs**: what to put in each placeholder, and what must never go in.
- **Example input** and **example output**: a short, non-confidential example.
- **Test notes**: the inputs tested, scores, problems and changes.
- **Tool and date of last test.**

Keep the cards in one shared place that your team already uses, such as a shared document or a spreadsheet with one row per prompt.

**Keeping the library up to date.** AI tools change their features, limits and behaviour. [VERSION] A template that worked in one tool this month may give different results later. Three habits help:

1. **Retest important prompts** regularly, for example every three months, and when a tool announces a major update.
2. **Update the date and version** on the card after every test or change.
3. **Remove prompts** that nobody uses or that no longer work well.

Write a short **introduction** at the top of the library for colleagues: what the library is for, how to use a card, and three safety rules, such as "never paste personal or confidential data", "check every output with the four-part checklist" and "follow our organisation's AI policy".

**Analogy:** A documented prompt library is like a well-kept recipe book in a restaurant kitchen. Each recipe has the ingredients, the method, a photo of the finished dish and notes from the chef. A new cook can produce the same dish, and the chef updates the recipe when a supplier changes.

## Worked Example
Min-jun is a finance analyst at a hypothetical manufacturing company in Seoul. Here is one of his completed cards:

```text
Name: Monthly variance summary
Version: v3
Purpose: Explain the main budget differences to department heads.
Pattern: Summarise or extract
Prompt template: You are a finance analyst. Using only the figures
below, list the three largest differences between budget and actual
for [DEPARTMENT] in [MONTH]. Show a table (Item, Budget, Actual,
Difference), then 3 plain-language sentences for a non-finance
reader. Mark any figure you calculated with [CHECK].
Figures: [PASTE FIGURES - no salaries or personal data]
Inputs: DEPARTMENT and MONTH as text; figures copied from the monthly report.
Example input: Invented figures for "Maintenance", "June".
Example output: 3-row table and 3 sentences (see tab 2).
Test notes: v1 used finance words; v2 added "non-finance reader";
v3 added [CHECK] after one wrong subtraction. Scores 5/5/4.
Tool and date of last test: [TOOL], [DATE]
```

His introduction for colleagues is five sentences long and ends with the three safety rules.

**Presenting the capstone rubric.** Your library will be assessed on the quality of the prompts, how you improved them, how you tested and checked them, and how well they are documented. Read the rubric on the course page before you submit.

## Common Mistake
Many learners document only the final prompt and delete the test notes. Without test notes, nobody knows why the prompt looks the way it does, and a colleague might remove an important constraint. Keep the test notes short, but keep them.

## Key Takeaways
1. Each prompt card has the same fields: name, version, purpose, pattern, template, inputs, example input and output, test notes, and the tool and date of the last test.
2. Retest important prompts regularly and update the version and date, because tools change.
3. A short introduction with clear safety rules helps colleagues use the library correctly.

## Hands-on Exercise
**Task:** Capstone step 3: document all 15 prompts in the library format in a shared document or spreadsheet, and write a short introduction for a colleague who will use it.
**Tools:** A free document or spreadsheet tool, such as Google Docs, Google Sheets or LibreOffice [VERSION].
**Steps:**
1. Create one card, or one spreadsheet row, for each of your 15 prompts, using every field listed above.
2. Check that every example input and output is invented or non-confidential.
3. Make sure each card shows at least two tests and the current version.
4. Write an introduction of 5 to 8 sentences: purpose, how to use a card, and three safety rules.
5. Ask one colleague to try one card without your help, and note any question they ask.
6. Improve the card that caused the question.
**What good looks like:** 15 complete cards in one shared place, a clear introduction, and one improvement based on a colleague's feedback.
**Time:** about 45 minutes

## Review Flags
- [VERSION] How often AI tools change their features and limits, and the availability of the named free document tools, must be checked before scripting.
