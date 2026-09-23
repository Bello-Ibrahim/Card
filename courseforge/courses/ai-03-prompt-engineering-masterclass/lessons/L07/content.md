# L07 Summarising and Extracting Information

Course: AI-03 · Module: M2 · Objectives: O3, O5 · Video: 5 min

## Hook
An AI tool can turn two pages of meeting notes into a neat table in a few seconds. It can also, in the same few seconds, leave out a deadline or invent an owner who was never named. Both results look equally professional.

## Explanation
Summarising and extracting are two of the most useful work tasks for AI tools, and they need slightly different prompts.

**Summarising** means making a text shorter while keeping what matters. A good summary prompt says:

- **The purpose**: "so my manager can decide whether to approve the budget", or "for a colleague who missed the meeting".
- **The length and format**: "5 bullet points", "one paragraph under 80 words".
- **The focus**: "focus on risks and costs", "ignore the technical details".

**Extracting** means pulling specific items out of a text into a fixed shape. It works well with a table:

```text
From the notes below, extract every decision and action item into a
table with columns: Item, Type (decision or action), Owner, Deadline.
If the owner or deadline is not stated, write "not stated".
Do not guess. Use only information from the notes.
```

The last two lines are important. When information is missing, AI tools sometimes fill the gap with a likely-sounding answer. Telling the tool to write "not stated" makes gaps visible.

**Always check a summary against the source.** This is not optional. Mark each item as:

- **Correct**: it matches the notes.
- **Missing**: something important in the notes is not in the output.
- **Invented**: something in the output is not in the notes.

Only you can do this check, because only you have the original and know what matters. Also remember the rule from L03: do not paste confidential or personal information. Replace names with roles or placeholders before you paste notes.

**Analogy:** An AI summary is like a colleague's quick notes from a meeting you could not attend. They are very useful, but before you act on a deadline in those notes, you check it with the person who set it.

## Worked Example
Aroha is a project officer at a hypothetical city council in Wellington. She has notes from a meeting about a new cycle lane. She replaces names with roles and pastes the notes:

```text
Meeting notes: Cycle lane, Stage 2.
- Engineer: design drawings 90% done, final version end of month.
- Agreed: public consultation will run for 4 weeks.
- Comms lead to prepare the consultation web page.
- Budget: finance team to confirm extra lighting cost, date not set.
- Agreed: no work on the main street during the market weekend.
```

She uses the extraction prompt above. The table has five rows. She checks each one against her notes:

| Item | AI output | Check |
|---|---|---|
| Final drawings | Owner: Engineer, end of month | Correct |
| Consultation 4 weeks | Decision | Correct |
| Consultation web page | Owner: Comms lead, deadline: 2 weeks | Invented deadline |
| Lighting cost | Owner: Finance team, not stated | Correct |
| Market weekend | Missing | Missing |

The tool invented a deadline for the web page and missed one decision. Aroha fixes both in the table and adds a line to her prompt: "List every line that starts with 'Agreed' as a decision."

## Common Mistake
Many learners check only whether a summary "sounds right". Invented details are dangerous because they sound right. The fix is a line-by-line check: go through the source and tick each point in the output, then go through the output and find each point in the source. Checking in both directions finds both missing and invented items.

## Key Takeaways
1. A good summary prompt states the purpose, the length and format, and the focus.
2. For extraction, use a table with named columns and tell the tool to write "not stated" instead of guessing.
3. Always check the output against the source in both directions and mark each item as correct, missing or invented.

## Hands-on Exercise
**Task:** Summarise a set of hypothetical meeting notes into a table of decisions, owners and deadlines, then mark every item against the original notes as correct, missing or invented.
**Tools:** Claude, ChatGPT or Gemini (free tier) [VERSION]; a notes app or spreadsheet.
**Steps:**
1. Use Aroha's notes above, or write 6 to 8 lines of hypothetical meeting notes from your own field. Use roles, not names.
2. Include at least one item with no owner and one with no deadline.
3. Run the extraction prompt from this lesson.
4. Add a column called Check to the output table.
5. Mark every row as correct, missing or invented. Then read your notes again and add any missing items.
6. Write one line you would add to the prompt to prevent the biggest error.
**What good looks like:** A complete table where every item is marked, missing items are added, invented details are highlighted, and one specific prompt improvement is written.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Free-tier availability of Claude, ChatGPT and Gemini must be checked before scripting.
