# L04 Context Windows, Knowledge Cut-offs and Hallucinations

Course: AI-02 · Module: M1 · Objectives: O2, O5 · Video: 5 min

## Hook
You paste a long document into a chatbot and ask about page one. The answer is strange, as if the chatbot never read it. Later, it tells you about a "company rule" that does not exist. What went wrong? Three ideas explain most of these problems.

## Explanation
**1. The context window.** When you chat with a language model, it does not remember the conversation the way a person does. Each time it answers, it looks at a block of text: your instructions, the conversation so far and any documents you added. This block is the **context window**, and it has a maximum size, measured in tokens (L02). If the conversation or document is longer than the window, the tool must leave something out. Depending on the tool, it may drop or shorten the oldest part of the conversation, or refuse a document that is too long. The model cannot use what is no longer in the window. Even inside the window, very long inputs can make it easier for the model to miss details. Window sizes differ between models and change often, so this course does not give numbers.

**2. The knowledge cut-off.** A model learns from text collected up to a certain date (L03). Events after that date are unknown to it. The model may still answer questions about recent events by guessing from older patterns. Some tools solve part of this problem by searching the web or reading files and placing the results in the context window. In that case the model answers from the new text, but it can still misread it.

**3. Hallucinations.** Because a model generates likely text rather than looking up checked facts, it can produce answers that are fluent and confident but false. This is called a **hallucination**. Common examples are invented quotes, wrong numbers, non-existent sources or policy rules that sound real. Hallucinations are more likely when:

- the answer is not in the context window and not common in the training data;
- the question assumes something false ("Why does our policy allow ten days of leave?");
- the prompt asks for very specific details such as dates, names or references.

You can reduce hallucinations. Give the model the source text, ask it to answer **only** from that text, and ask it to say "not stated" when the answer is missing. But you cannot remove them completely, so important answers must always be checked.

**Analogy:** The context window is like the space on a desk. The model can only work with the papers on the desk. When the desk is full, older papers fall off the edge, and the model cannot see them anymore. The knowledge cut-off is like the date the library stopped buying new books. A hallucination is like a student who does not know the answer but writes a confident paragraph anyway, because a blank answer earns no marks.

## Worked Example
Kwame is an HR officer at a hypothetical logistics company in Accra, Ghana. He gives a chatbot the company's two-page travel policy, with all staff names removed, and asks four questions.

- "How many days before a trip must staff submit a request?" The policy says five working days, and the chatbot answers correctly.
- "What is the daily meal allowance?" Correct, and it quotes the right paragraph.
- "Can staff book business class for flights over six hours?" The policy says nothing about this. The chatbot replies, "Yes, for flights over six hours business class is allowed with manager approval." This is a **hallucination**: it sounds like a normal company rule, but it is not in the text.
- Kwame asks again with a new instruction: "Answer only from the policy. If the policy does not say, reply 'not stated'." This time the chatbot says "not stated".

Kwame also notices that after a very long conversation, the chatbot forgets an instruction he gave at the start. He starts a new chat and repeats the key instruction, so it is back in the context window.

## Common Mistake
Many learners think a hallucination is a rare bug that will soon disappear. It is a direct result of how language models work: they generate likely text. Better models and search tools reduce the problem, but a fluent answer is never proof of a correct answer. The correction is a habit: give the source, ask for "not stated" when information is missing, and check every important fact.

## Key Takeaways
1. The context window is the amount of text a model can consider at one time; text outside it cannot be used.
2. A knowledge cut-off means the model does not know about later events unless a tool gives it new information.
3. Hallucinations are confident but false answers that come from predicting likely text, so important answers must be checked against a source.

## Hands-on Exercise
**Task:** Give a free chatbot a two-page hypothetical company policy, ask five questions about it (including one that the policy does not answer), and record which answers were correct, invented or honestly uncertain.
**Tools:** Claude, ChatGPT or Google AI Studio (free) [VERSION]; the sample policy on the course page, or a short policy you write yourself; a table in a notes app or spreadsheet.
**Steps:**
1. Use the hypothetical sample policy or write your own. Do not use a real company's confidential documents or any personal data.
2. Paste the policy into the chatbot.
3. Write five questions. Four should have answers in the policy. One should ask about something the policy does not cover.
4. Ask the questions one by one and copy each answer.
5. Check each answer against the policy and label it "correct", "invented" or "honestly uncertain".
6. Ask the unanswered question again with the instruction "Answer only from the policy; say 'not stated' if it is missing", and record what changes.
**What good looks like:** A five-row table with question, answer, label and the policy line used to check it, plus one sentence on whether the "answer only from the policy" instruction changed the result.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Free chatbot options (Claude, ChatGPT, Google AI Studio) and their limits on pasted text length must be checked before recording.
- Note for reviewer: no context window sizes or cut-off dates are given on purpose, because they change with each model version.
