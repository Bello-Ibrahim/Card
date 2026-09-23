# L02 Research Synthesis with Claude

Course: AI-23 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
You have 12 interview notes, a deadline tomorrow and a wall of sticky notes that is still empty. Claude can suggest themes in under a minute. But can you trust a theme if you have not checked where it came from?

## Explanation
Research synthesis means turning raw material, such as interview notes, app store reviews or open survey answers, into a small number of clear patterns. It is slow work, and it is a good fit for a language model like Claude, because the task is about reading a lot of text and grouping similar ideas.

A reliable synthesis prompt has four parts:

1. **Context:** who the research is about and what decision it supports.
2. **Material:** the anonymised notes, clearly separated, with an ID for each participant (P01, P02 and so on).
3. **Task:** "Find up to 5 themes. For each theme, give a short name, a one-sentence description, the participant IDs that support it and 2 exact quotes."
4. **Rules:** "Only use quotes that appear word for word in the notes. If a theme is supported by fewer than 3 participants, say so. Do not add information that is not in the notes."

Asking for participant IDs and exact quotes makes the output checkable. It also makes weak themes visible, because a theme supported by one person looks very different from a theme supported by nine.

**Why checking matters.** Language models produce text that sounds right. They can merge two different complaints into one theme, turn "some people" into "most users", or slightly reword a quote so it supports a theme better. Sometimes they invent a quote that no participant said. None of this is deliberate, but the result is the same: a false insight in your deck. So you verify every theme against the source before you use it.

**Protect the data first.** Before you paste anything, remove names, phone numbers, email addresses, exact locations, employer names and any detail that could identify a person. Replace them with IDs or general terms ("a market trader in a large city"). Only use research data in an AI tool if participants agreed to this kind of processing or the data is properly anonymised, and your client has approved it. Lesson L05 covers this in more detail.

**Analogy:** Claude is like a colleague who read all the notes very quickly and now tells you what they remember. Their summary is useful, but you would still ask, "Who said that? Show me the page." Asking for IDs and quotes is how you ask Claude to show you the page.

## Worked Example
Wanjiru Kamau is a UX researcher at a hypothetical start-up building a group savings app for users in Kenya and Ghana. She has 12 anonymised interview notes, labelled P01 to P12.

She writes this prompt in Claude:

```text
Context: interviews with 12 people in Kenya and Ghana about saving money in groups. The goal is to decide the first features of a savings app.
Task: find up to 5 themes. For each: name, one-sentence description, supporting participant IDs, and 2 exact quotes.
Rules: quotes must appear word for word in the notes. Mark any theme with fewer than 3 participants as "weak". Do not add facts that are not in the notes.
Notes: [P01] ... [P12] ...
```

Claude returns five themes, including "Trust in the group treasurer" (P02, P05, P07, P09, P11) and "Fear of hidden fees" (P03, P06, P10).

Wanjiru checks each quote with a text search in her original notes. Four themes are correct. In "Fear of hidden fees", one quote is slightly changed: the note says "I think there might be charges", but Claude wrote "I know there are hidden charges". The meaning is stronger than the original. She also finds that P06 talked about bank fees, not app fees. She corrects the quote, removes P06 and relabels the theme as "weak: 2 participants". In her report, it becomes a question for the next round of research, not a finding.

## Common Mistake
The most common mistake is to copy Claude's themes straight into a research deck because they "sound right". A theme is only a finding when you can point to the evidence. A second mistake is to paste raw notes with real names and phone numbers because "it is only a summary task". The task does not change the data you shared.

## Key Takeaways
1. Ask Claude for themes with participant IDs and exact quotes, so every claim can be checked against the source.
2. Verify every quote and every supporting participant before you use a theme; models can reword, merge or invent evidence.
3. Anonymise research data and only use it in AI tools with consent and client approval.

## Hands-on Exercise
**Task:** Give Claude a set of sample interview notes, ask for 5 themes with quotes, and verify each quote against the original text.
**Tools:** Claude (free plan); the sample interview notes from the course page, or your own notes after full anonymisation; a text editor with search.
**Steps:**
1. Open the sample notes, or anonymise your own: replace names and identifying details with IDs and general terms.
2. Write a prompt with context, material, task and rules, using the structure in this lesson.
3. Ask Claude for 5 themes, each with participant IDs and 2 exact quotes.
4. Search for every quote in the original notes. Mark each as "exact", "changed" or "not found".
5. Check that each listed participant really supports the theme.
6. Correct or remove any theme with problems, and mark themes with fewer than 3 participants as "weak".
**What good looks like:** A table of 5 themes where every quote is marked, at least one correction is recorded (if needed), and weak themes are clearly separated from strong ones.
**Time:** about 30 minutes

## Review Flags
- None. The lesson uses hypothetical data and general prompting practice. Consent and privacy rules are covered, with their tags, in L05.
