# L02 Research Synthesis with Claude | Presenter Script

Course: AI-23 · Video: 5 min · Words: 715

## Hook
You have twelve interview notes, a deadline tomorrow and a wall of sticky notes that is still empty. Claude can suggest themes in under a minute. But can you trust a theme if you have not checked where it came from?

## Explain
In the last lesson, we mapped where AI fits. Now we start at the beginning, with research. This lesson is about research synthesis with Claude.

Research synthesis means turning raw material, such as interview notes, app store reviews or open survey answers, into a few clear patterns. It is slow work. And it suits a language model like Claude, because the task is about reading a lot of text and grouping similar ideas.

A reliable synthesis prompt has four parts. Context: who the research is about, and what decision it supports. Material: the anonymised notes, with an ID for each participant, like P zero one. Task: find up to five themes, each with a name, a description, the supporting participant IDs and two exact quotes. And finally, rules.

The rules say: only use quotes that appear word for word in the notes. Mark any theme with fewer than three participants. And do not add information that is not in the notes. IDs and exact quotes make the output checkable, and they make weak themes easy to see.

Why does checking matter? Language models produce text that sounds right. They can merge two complaints into one theme, turn some people into most users, or slightly reword a quote. Sometimes they invent a quote that nobody said. It is not deliberate, but the result is a false insight in your deck.

So protect the data first. Before you paste anything, remove names, phone numbers, email addresses, exact locations and employer names. Replace them with IDs or general terms. And only use research data with participant consent and client approval. Lesson five covers this in more detail.

Here is a way to think about it. Claude is like a colleague who read all the notes very quickly, and now tells you what they remember. That is useful. But you would still ask, who said that? Show me the page. Asking for IDs and quotes is how you ask Claude to show you the page.

## Demonstrate
Let's try it. Wanjiru Kamau is a UX researcher at a start-up building a group savings app for users in Kenya and Ghana. She has twelve anonymised interview notes, labelled P zero one to P twelve.

She writes a prompt in Claude with the context, the task and the rules, and then pastes the notes. Claude returns five themes. For example, trust in the group treasurer, supported by five participants, and fear of hidden fees, supported by three.

Now Wanjiru checks each quote with a text search in her original notes. Four themes are correct. But in fear of hidden fees, one quote has changed. The note says, I think there might be charges. Claude wrote, I know there are hidden charges. The meaning is stronger than the original.

She also finds that participant six talked about bank fees, not app fees. So she corrects the quote, removes that participant and relabels the theme as weak, with two participants. In her report, it becomes a question for the next round of research, not a finding.

The most common mistake is to copy Claude's themes straight into a deck because they sound right. A theme is only a finding when you can point to the evidence. Another mistake is pasting raw notes with real names, because it is only a summary. The task does not change the data you shared.

## Recap
Let's recap. First, ask Claude for themes with participant IDs and exact quotes, so every claim can be checked. Second, verify every quote and every participant before you use a theme, because models can reword, merge or invent evidence. Third, anonymise research data, and only use it in AI tools with consent and client approval.

## CTA
Now it is your turn. In the exercise below this video, you will give Claude a set of sample interview notes, ask for five themes with quotes, and check every quote against the original text. It takes about thirty minutes. In the next lesson, we go from insights to personas and jobs to be done. See you there.

## Thumbnail
Headline: Trust, but Check Themes
Image: Navy background, a column of sticky-note themes on the left linked by teal lines to highlighted quotes on the right, one link marked with a small warning icon, headline in teal Inter Bold.

## Production Notes
- No facts to verify: hypothetical data and general prompting practice (content.md Review Flags: None).
- Wanjiru Kamau and the savings start-up are fictional; stock footage must not show a real app, bank or brand.
- Participant IDs are spoken as 'P zero one' and 'P twelve'; slides show P01 to P12.
- Scene 10 code slide shows the prompt from content.md (Context, Task, Rules, Notes); the presenter describes it and does not read it.
