# L08 Query Rewriting and Conversational Retrieval | Presenter Script

Course: AI-15 · Video: 5 min · Words: 690

## Hook
A user asks how many days of parental leave employees get. Your assistant answers well. Then the user asks: and for contractors? Search for those three words alone, and you get random passages. The question only makes sense inside the conversation.

## Explain
In the last lesson, we improved retrieval with hybrid search and reranking. Today we fix the question itself, before it ever reaches retrieval.

Retrieval works one query at a time, and it has no memory. In a chat, many questions depend on earlier turns. And in twenty twenty-two? What about the second option? These are follow-up questions. Before retrieval, we rewrite them into standalone queries, such as: how many days of parental leave do contractors get?

The language model is good at this. From the previous course, you know how to ask for a structured output that your code can trust. Here, the request includes a small schema with two fields: one standalone query, and a list of up to three other phrasings. A schema in the request is the safest way to get this, because the reply must match it.

This gives us two techniques. Standalone rewriting resolves words like that, it, and and for, using only the last few turns. Multi-query retrieval searches with every phrasing, then fuses the lists with rank fusion from the last lesson. Different words reach different chunks. This improves recall when users write vaguely.

Think of a good receptionist taking a phone message. The caller says: tell her it's about the same thing as yesterday. The receptionist writes a note that names the person, the invoice and the order. The reader was not on the call, so the note must stand alone.

## Demonstrate
Let's follow Aigerim. She builds an HR policy assistant for a logistics company in Almaty, Kazakhstan. Policies are in Russian and English. First question: what is the travel allowance for Astana? Retrieval works, and the answer cites the travel policy.

Second question: and for drivers? Without rewriting, the top chunks are about vehicle maintenance for drivers. The answer is wrong, and it is easy to see why when we print the retrieved chunks. The search engine saw only the word drivers, so it found drivers, but the wrong topic.

Now she adds the rewrite function. It sends the last six messages and the new question, with the schema, and reads back the JSON. You'll see something like a standalone query about the travel allowance for drivers going to Astana, plus a short variant about a driver's daily allowance.

She searches with all three queries, fuses them, and the drivers' section of the travel policy is now the top chunk. She also shows the rewritten query in a debug panel, so testers can see exactly what was searched. That makes problems much easier to find later.

Two rules keep this safe. First, a complete question should come back almost unchanged, so she tests one, and gets only small word changes. Second, the rewrite is for search only. The final answer step still receives the user's original words.

A common mistake is to send the whole chat history to the embedding model as the query. Long histories mix topics, so retrieval becomes vague. Rewrite into one focused query instead. And remember, rewriting adds one model call per turn, so you can skip it for the first message, and use a smaller model for it.

## Recap
Let's recap. First, follow-up questions depend on earlier turns, so rewrite them into standalone queries before retrieval. Second, a structured output gives your code a reliable standalone query, plus extra phrasings for multi-query retrieval. Third, use the rewrite only for search, keep the user's original question for the answer, and test that complete questions stay the same.

## CTA
Now it is your turn. In the exercise below, write five short conversations with follow-up questions, add rewriting, and compare retrieval with and without it. For each follow-up, mark whether the expected chunk is in the top five. Note any rewrite that changed the meaning. That completes week two. In the next lesson, Grounded Answers with Citations, we make every answer show its sources.

## Thumbnail
Headline: And for Drivers?
Image: Navy background, a short chat bubble 'And for drivers?' transforming into a longer, complete search query with a teal arrow, headline in teal Inter Bold.

## Production Notes
- [VERSION] Claude API structured outputs (output_config with a JSON Schema; a forced tool_choice is rejected by some current models), the response content block format, and model choice (MODEL read from the environment; check the current models page). Never say a model ID or price.
- The rewrite output on screen comes from a real API run; the voiceover says 'you'll see something like' and the wording will differ from content.md.
- Aigerim and the Almaty logistics company are hypothetical; HR policies and conversations are invented, with no personal data.
- Russian-language policy text, if shown on screen, should be checked by a Russian speaker before release.
