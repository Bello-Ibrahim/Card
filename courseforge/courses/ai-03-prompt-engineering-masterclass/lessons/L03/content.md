# L03 Giving Context That Matters

Course: AI-03 · Module: M1 · Objectives: O1, O2 · Video: 5 min

## Hook
Context is the part of a prompt that turns a general answer into your answer. But some context should never go into an AI tool. How do you give enough without giving too much?

## Explanation
In L01 you saw that an AI tool fills gaps with safe, average choices. Context closes those gaps. Useful context answers four questions:

1. **Audience**: Who will read or use the output? A board member, a new employee, a customer who is angry, a supplier who reads English as a second language?
2. **Purpose**: What should the output achieve? Inform, persuade, apologise, get a decision, get a reply by a date?
3. **Background**: What does the AI need to know about the situation? What happened, what was agreed before, what the limits are.
4. **Material**: What do you already have? Notes, a draft, figures, a previous version. Pasting your own rough notes is often better than describing them.

Four short lines, one for each question, are often enough. You do not need to write a story.

Now the other side: **what not to share**. Many AI tools may store your conversations, and your employer may have rules about which tools you can use. Before you paste anything, remove:

- **Personal data**: names, phone numbers, addresses, ID numbers, health details, salaries of real people.
- **Confidential client data**: client names, contract values, account details.
- **Internal secrets**: unreleased products, prices, strategy, passwords, access codes.

Replace them with neutral **placeholders** in square brackets, such as [CLIENT], [PRODUCT], [EMPLOYEE], [AMOUNT] or [DATE]. The AI can still write a good output, and you add the real details yourself afterwards, outside the tool. Always follow your organisation's policy on AI tools; it is the rule that applies to you.

**Analogy:** Giving context is like briefing a taxi driver in a city you know well. "The airport" is not enough if there are two terminals and you have a flight in 40 minutes. You tell them the terminal and the time, but you do not hand them your passport.

## Worked Example
Nguyen Thi Lan is a marketing coordinator at a hypothetical cosmetics company in Hanoi. A large retail client has complained that a product launch campaign started late in their stores.

Before:

```text
Write a reply to the client about the campaign delay. The client is
Ms Tran Minh Chau at SunMart, and her email is minh.chau@... She says
the Glow Serum launch started 5 days late in 40 stores.
```

This prompt has useful facts, but it also contains a real person's name, email address, the client name and an unreleased product name.

After:

```text
Audience: the marketing lead at [CLIENT], a large retail chain. She is
unhappy and busy.
Purpose: apologise, explain briefly, and keep the relationship strong.
Background: our campaign for [PRODUCT] started 5 days late in 40 of
their stores because printed displays arrived late from our supplier.
New displays are now in all stores.
Material: my notes: "sorry, supplier issue, fixed now, offer extra
week of promotion at no cost".
Task: write a reply email under 150 words in a polite, direct tone.
```

The reply is clear and specific. Lan copies it into her email program and replaces [CLIENT] and [PRODUCT] with the real names there. The AI tool never saw them.

## Common Mistake
Some learners remove so much detail that the prompt becomes vague again. "Write to a client about a problem" is safe, but not useful. The goal is to remove identities and secrets, not the situation. "A retail client, a 5-day delay in 40 stores, caused by a supplier" contains no personal or confidential data, but it still gives the AI what it needs.

## Key Takeaways
1. Useful context answers four questions: who is the audience, what is the purpose, what background is needed, and what material you already have.
2. Never paste personal data, confidential client data or internal secrets into an AI tool. Replace them with placeholders such as [CLIENT] or [PRODUCT].
3. Keep the situation and remove the identities, so the output stays specific and safe.

## Hands-on Exercise
**Task:** Write the context for a real work task in four short lines, using placeholders for anything sensitive.
**Tools:** A notes app or paper. Optional: Claude, ChatGPT or Gemini (free tier) to test the prompt.
**Steps:**
1. Choose a real task from your job that you do often, for example a reply to a customer, a note to your team or a short report.
2. Write one line each for audience, purpose, background and material.
3. Underline every name, number, email address or detail that is personal or confidential.
4. Replace each underlined item with a placeholder in square brackets, such as [CLIENT], [COLLEAGUE] or [AMOUNT].
5. Add a one-line task at the end. Optional: run the prompt and check that the output is still specific.
**What good looks like:** Four clear lines of context plus a task. A colleague could understand the situation, but could not identify any real person, client or secret from the text.
**Time:** about 15 minutes

## Review Flags
- None. The lesson gives general data-protection advice and points learners to their own organisation's policy instead of describing how any specific tool stores data.
