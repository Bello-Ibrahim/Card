# L08 Query Rewriting and Conversational Retrieval

Course: AI-15 · Module: M2 · Objectives: O3, O6 · Video: 5 min (screen demo)

## Hook
A user asks, "How many days of parental leave do employees get?" Your assistant answers well. Then the user asks, "And for contractors?" If you embed "And for contractors?" and search, you get random passages about contractors. The question only makes sense together with the conversation.

## Explanation
Retrieval works one query at a time and has no memory. In a chat, many questions depend on earlier turns: "And in 2022?", "What about the second option?", "Does that apply to Kenya too?" These are **follow-up questions**. Before retrieval, we rewrite them into **standalone queries**, such as "How many days of parental leave do contractors get?"

The LLM is good at this, and you already know from AI-14 how to get a **structured output** that your code can trust. Here we use a tool definition with a forced tool choice, so the model must return JSON that matches a schema. You may use your API's native structured-output option instead. [VERSION]

```python
REWRITE_TOOL = {
    "name": "search_queries",
    "description": "Search queries for the user's latest question.",
    "input_schema": {
        "type": "object",
        "properties": {
            "standalone": {"type": "string"},
            "variants": {"type": "array", "items": {"type": "string"}},
        },
        "required": ["standalone", "variants"],
    },
}

def rewrite(history, question):
    convo = "\n".join(f"{role}: {text}" for role, text in history[-6:])
    msg = client.messages.create(
        model=MODEL, max_tokens=300,  # MODEL: check the current models page
        tools=[REWRITE_TOOL],
        tool_choice={"type": "tool", "name": "search_queries"},
        messages=[{"role": "user", "content":
            f"Conversation:\n{convo}\n\nLatest question: {question}\n"
            "Rewrite the latest question as one complete search query. "
            "Add up to 3 other phrasings that use different words."}])
    return next(b.input for b in msg.content if b.type == "tool_use")
```

Example output:

```
{"standalone": "How many days of parental leave do contractors get?",
 "variants": ["contractor parental leave entitlement",
              "parental leave policy for non-employees"]}
```

Two techniques are shown here:

- **Standalone rewriting** resolves words like "that", "it" and "and for", using the last few turns. Keep the history short (for example the last 6 messages) to control cost and avoid confusion.
- **Multi-query retrieval** searches with the standalone query and each variant, then fuses the lists with `rrf` from L07. Different phrasings reach different chunks, which improves recall when users write vaguely.

Two rules keep this safe. First, if the question is already complete, the rewrite should return it almost unchanged; test this. Second, keep the user's original question for the final answer step. The rewritten query is for search only, so the model should still answer what the user actually asked.

Rewriting adds one LLM call per turn, so it adds cost and latency. You can skip it for the first message in a conversation, and use a smaller model for rewriting.

**Analogy:** Query rewriting is like a good receptionist who takes phone messages. The caller says, "Tell her it's about the same thing as yesterday." The receptionist writes: "Mr Sato called about the delayed invoice for order 552." The person reading the note later does not know the conversation, so the note must stand alone.

## Worked Example
Aigerim builds an internal HR policy assistant for a hypothetical logistics company in Almaty, Kazakhstan. Policies are in Russian and English, and employees ask in both languages.

On screen, follow her test of one short conversation:

1. Question 1: "What is the travel allowance for Astana?" Retrieval works, and the answer cites the travel policy.
2. Question 2: "And for drivers?" Without rewriting, the top chunks are about vehicle maintenance for drivers. The answer is wrong.
3. She adds `rewrite()`. The standalone query becomes "What is the travel allowance for drivers travelling to Astana?", with variants such as "driver per diem Astana trip".
4. She retrieves with all three queries, fuses them with `rrf`, and the drivers' section of the travel policy is now the top chunk.
5. She prints the rewritten query in a debug panel, so testers can see what was searched.

She also tests a complete first question. The rewrite returns the same question with small word changes, which is acceptable.

## Common Mistake
Developers often send the whole chat history to the embedding model as the search query. Long histories mix several topics, so the vector points to the average of them and retrieval becomes vague. Rewrite into one focused query instead. Another mistake is to answer the rewritten query and not the user's words; if the rewrite was wrong, the user gets an answer to a question they did not ask.

## Key Takeaways
1. Follow-up questions depend on earlier turns and must be rewritten into standalone queries before retrieval.
2. A structured output (such as a forced tool call) gives your code a reliable standalone query and extra phrasings for multi-query retrieval.
3. Use the rewrite only for search, keep the user's original question for the answer, and test that complete questions stay unchanged.

## Hands-on Exercise
**Task:** Add query rewriting for follow-up questions, and test it on 5 short conversations.
**Tools:** Python 3, the anthropic SDK with a Claude API key (paid, use a smaller model), your Chroma collection and the `rrf` function from L07. [VERSION]
**Steps:**
1. Write 5 conversations of 2–3 turns each about your collection. Each must contain at least one follow-up question. Use invented data, not personal details.
2. Add `rewrite()` and print the standalone query and variants for every turn.
3. For each follow-up, retrieve the top 5 with the raw question and with rewriting plus multi-query fusion.
4. Mark whether the expected chunk is in the top 5 in each case.
5. Check that the first, complete questions were not changed in meaning.
**What good looks like:** A table of follow-up questions with raw and rewritten queries and hit/miss results, showing clear improvement, and a note on any rewrite that changed the meaning.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Claude API tool use with forced `tool_choice`, the response content block format, native structured-output options, and model choice (MODEL constant; check the current models page).
