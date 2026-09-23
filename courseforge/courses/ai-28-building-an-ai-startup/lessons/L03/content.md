# L03 Customer Discovery Interviews

Course: AI-28 · Module: M1 · Objectives: O3 · Video: 5 min

## Hook
Ask a friend, "Would you use an app that does this?" and they will almost always say yes. That answer feels good, but it tells you almost nothing. In this lesson you will learn to ask questions that people cannot answer just to be polite.

## Explanation
**Customer discovery** means talking to potential customers to learn about their problem before you build. The goal is not to sell your idea. The goal is to learn the truth about their situation.

The most important rule: **ask about past behaviour, not opinions about your idea.** Opinions about the future ("Would you pay for this?") are cheap and often wrong. Facts about the past ("What did you do last time?") are much more reliable.

Good questions sound like this:

- When did this problem last happen? Tell me about that day.
- What did you do about it?
- What did it cost you, in time, money or lost customers?
- What have you tried to solve it? What did you like or dislike about that?
- Who else is involved when this happens?

Weak questions, such as "Would you use an AI tool for this?", invite kindness, not facts.

**A validation-interview script (about 20 minutes)**

1. **Thank and explain (1 min):** "I am researching how [group] handle [task]. I am not selling anything. There are no wrong answers."
2. **Consent (1 min):** "May I take notes? I will not use your name, and I will delete anything you do not want recorded."
3. **Context (3 min):** "Tell me about your role and a normal week."
4. **The last time (6 min):** "When did [problem] last happen? Walk me through it step by step. What did you do next?"
5. **Cost (3 min):** "What did that cost you? How often does it happen?"
6. **Current solutions (4 min):** "What have you tried? What do you pay for it today, in money or staff time?"
7. **Close (2 min):** "Is there anything I should have asked? Who else should I talk to? May I contact you again when I have something to show?"

Listen more than you talk. When you hear something important, ask "Can you tell me more?"

After the interviews, remove names and identifying details from your notes. Then you can use Claude to look for **patterns**: problems, costs or workarounds that appear in several interviews. But AI tools can invent patterns or exaggerate weak ones. So check every pattern against your notes and count how many interviews really support it.

**Analogy:** A detective does not ask a suspect, "Would you ever commit a crime?" She asks, "Where were you on Tuesday at 8 p.m.?" Specific questions about real past events are much harder to answer with a comfortable story.

## Worked Example
Elif is a hypothetical founder in Izmir, Türkiye. She believes small shop owners lose money because they run out of popular products and order too much of slow ones. She plans an AI tool that suggests what to order.

She interviews five owners: two grocery shops, a stationery shop, a pharmacy and a phone-accessories shop. She does not mention AI. With the grocer, the conversation goes like this:

- Elif: "When did you last run out of something a customer asked for?"
- Grocer: "Last Friday. Bread flour, before a holiday weekend."
- Elif: "What did you do?"
- Grocer: "Sent my nephew to a wholesaler. We lost about half a day."
- Elif: "How do you decide what to order now?"
- Grocer: "I look at the shelves and write a list in a notebook."

After five interviews, Elif labels her notes Shop A to Shop E, with no names, and asks Claude to list common patterns with the number of shops that support each. Claude suggests three:

1. Ordering is done from memory or a notebook (supported by 4 of 5).
2. Stock problems cluster before holidays (3 of 5).
3. Owners want an app to predict demand (Claude says 3 of 5).

Elif checks her notes. Patterns 1 and 2 are correct. Pattern 3 is not supported: no owner asked for an app. One owner only said, "It would be nice to know earlier." Claude turned a wish into a request. Elif deletes pattern 3 and plans more interviews about holiday ordering.

## Common Mistake
The most common mistake is pitching during the interview. The founder describes the idea for ten minutes, the person politely agrees, and the founder leaves feeling validated. Nothing was learned. Keep your idea out of the conversation until the end, if you mention it at all. A second mistake is accepting AI-generated summaries without checking. Every pattern should point back to real notes.

## Key Takeaways
1. Ask about specific past events, actions and costs, not opinions about your idea.
2. Use a short, structured script, ask for consent, and listen more than you talk.
3. Remove names before using AI to find patterns, and check every pattern against your own notes.

## Hands-on Exercise
**Task:** Interview 3 to 5 potential customers. Remove names from your notes, then use Claude to find common patterns, and check each pattern against the notes.
**Tools:** The interview script above; a notes app or paper; Claude (free plan).
**Steps:**
1. Adapt the script to the problem you chose in L02.
2. Book 3 to 5 interviews of about 20 minutes, in person, by phone or by video call.
3. Ask for consent before taking notes. Do not record audio unless the person agrees.
4. Write notes as close to the person's own words as you can.
5. Replace names and identifying details with labels such as "Person A". Do not paste personal or confidential data into any AI tool.
6. Paste the cleaned notes into Claude and ask: "List the patterns that appear in more than one interview. For each, say which interviews support it and quote the evidence."
7. Check each pattern against your notes. Mark it "confirmed", "weak" or "not supported".
**What good looks like:** At least 3 interviews with notes about real past events. A pattern list where each pattern has a count, a quote and your own check. At least one AI-suggested pattern is corrected or rejected if the evidence is weak.
**Time:** about 90 minutes, including interviews

## Review Flags
- None. The founder and interviews are hypothetical, and no facts, statistics or tool details need checking.
