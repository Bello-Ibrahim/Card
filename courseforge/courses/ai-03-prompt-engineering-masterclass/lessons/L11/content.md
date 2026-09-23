# L11 Checking Outputs: Accuracy, Bias and Confidentiality

Course: AI-03 · Module: M3 · Objectives: O5 · Video: 5 min

## Hook
When you send a document written with AI help, your name is on it, not the tool's. A two-minute check before you use an output protects you, your colleagues and your organisation.

## Explanation
Use this four-part checklist before you use any AI output at work.

**1. Facts and figures.** Check every number, date, name, percentage and quotation. AI tools can produce figures that look exact but are invented, and they may not know recent events. If you gave the tool the figures, check they were copied correctly. If you did not, find a reliable source yourself.

**2. Sources.** If the output mentions a study, a law, a report or a website, check that it exists and says what the output claims. A reference that looks real is not proof. If you cannot find it, remove it.

**3. Bias and one-sided wording.** Read the output as the people it describes would read it. Look for:
- one side of an issue presented as the only view,
- assumptions about gender, age, nationality or background, for example "the engineer... he",
- strong words, such as "obviously" or "failed", where a neutral word would be fairer.

**4. Confidentiality.** Confirm that you did not paste personal data, client details or internal secrets into the tool, and that the output does not contain any. Rules on personal data and workplace AI use differ between countries and employers. [REGION] Always check your own organisation's policy on which tools you may use and what you may share.

You can also **write prompts that make checking easier**:

```text
Mark any figure that did not come from my notes with [CHECK].
Do not include sources unless I provided them.
If you are not sure about something, say so.
```

These instructions often help, but they do not replace your own check.

**Analogy:** Checking an AI output is like checking a restaurant bill before you pay. Most of the time it is correct. But the bill has your name on the payment, so you look at each line and you do not pay for a dish you never ordered.

## Worked Example
Kwame is a policy analyst at a hypothetical farmers' cooperative in Kumasi. He asked an AI tool for a short briefing on drip irrigation for the cooperative's board. Here is part of the output:

```text
Drip irrigation reduces water use by 60% on every farm, according to
the 2021 West Africa Water Report. All modern farmers have already
switched, and any farmer who has not is clearly falling behind. The
cooperative could fund pilots using member data from our records:
Mr K. Boateng (plot 14) and Mrs A. Owusu (plot 22).
```

Kwame applies the checklist:

- **Facts:** "60% on every farm" is a precise figure with no basis in his notes. Savings depend on crop, soil and climate. Marked [CHECK].
- **Sources:** He cannot find a "2021 West Africa Water Report". Removed.
- **Bias:** "All modern farmers" and "clearly falling behind" are one-sided and unfair to members who cannot afford new equipment. Rewritten in neutral words.
- **Confidentiality:** Two members' names and plot numbers appear. Kwame realises he pasted them in his notes. Removed, and he replaces them with [MEMBER A] and [MEMBER B] in future prompts.

His improved prompt adds: "Use only the figures in my notes. Mark anything else with [CHECK]. Present benefits and costs in a balanced way. Do not name members."

## Common Mistake
Many learners check only the parts that look wrong. The most dangerous errors are the ones that look correct: a realistic figure, a report with a believable title, a confident sentence. Go through the whole checklist every time, even when the output reads well.

## Key Takeaways
1. Before using any AI output, check facts and figures, check sources, look for bias, and confirm confidentiality.
2. Prompts can make checking easier, for example by asking the tool to mark uncertain figures, but they do not replace your own check.
3. Rules on data and AI use differ between countries and employers, so always follow your own organisation's policy.

## Hands-on Exercise
**Task:** Check a provided AI-written briefing with the checklist, mark every issue you find, and rewrite the prompt so the next output is easier to verify.
**Tools:** A notes app or paper. Optional: Claude, ChatGPT or Gemini (free tier) [VERSION].
**Steps:**
1. Read this hypothetical AI-written briefing for a hospital's staff newsletter: "Remote meetings save every team 5 hours a week, as proven by the Global Workplace Study. Older staff usually struggle with video tools, so they should get extra help. Nurse Maria Silva on Ward 3 has already tested our new system."
2. Apply the four-part checklist and mark each issue as Facts, Sources, Bias or Confidentiality.
3. Write a one-line correction for each issue.
4. Rewrite the original prompt so that it asks the tool to mark uncertain figures, avoid invented sources, use balanced wording and use placeholders instead of names.
5. Check your own organisation's AI policy, or note that you need to ask for it.
**What good looks like:** At least four issues found (an unsupported figure, an unverified study, an age assumption, a named staff member), a correction for each, and a rewritten prompt with at least three checking instructions.
**Time:** about 20 minutes

## Review Flags
- [REGION] Data protection and workplace AI rules differ by country. The lesson points learners to their own organisation's policy instead of naming laws.
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini must be checked before scripting.
