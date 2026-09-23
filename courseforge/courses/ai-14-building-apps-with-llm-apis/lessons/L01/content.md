# L01 How LLM APIs Work

Course: AI-14 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
You chat with an AI assistant for ten minutes, and it remembers everything you said. Then you call the same model through its API, ask a follow-up question, and it has no idea what you are talking about. Nothing is broken. This lesson explains why, and what your app must do about it.

## Explanation
An LLM API works like other web APIs: your code sends an HTTP request and gets a response. What is new is the shape of the request and the response.

**The request.** The main part of a request is a list of **messages**. Each message has a **role** and some **content**:

- `user`: text from the person using your app (or text your app writes on their behalf).
- `assistant`: earlier replies from the model.

The list must start with a `user` message, and the roles normally take turns. You can also send a **system prompt**. This is a separate field, not a message. It sets the model's role, rules and style for the whole conversation.

You also send settings. The two you will use in every call are the **model** (which model to run) and **max_tokens** (the maximum length of the reply).

**Tokens.** Models do not read words or letters. They read **tokens**, which are small pieces of text: often a whole short word, sometimes part of a longer word or a punctuation mark. Everything is measured in tokens: the length of your input, the length of the reply, the price and the limits.

**The context window.** Each model can read only a limited number of tokens in one request. This limit is the **context window**. It includes the system prompt, every message in the list and the reply. The size depends on the model, so check the models page. [VERSION]

**The response.** The API sends back:

- **content**: a list of blocks. For now, you only need the `text` block that holds the reply.
- **stop_reason**: why the model stopped. `end_turn` means it finished normally. `max_tokens` means it hit your length limit and the reply is cut off. You will meet other values, such as `tool_use`, later in the course.
- **usage**: how many input tokens you sent and how many output tokens the model wrote. This is what you pay for.

**Stateless.** The API does not remember earlier requests. Each call starts from nothing. If you want a conversation, your app must store the history and send the whole list again every time, with the new user message added at the end.

**Analogy:** Imagine a very knowledgeable assistant who answers the phone but forgets every call as soon as it ends. To continue yesterday's discussion, you must first read your notes aloud: "Yesterday I asked X, and you said Y. Now my question is Z." The notes are your messages list. Longer notes mean longer, more expensive calls.

## Worked Example
Tomás builds a help chat for a chain of bakeries in Montevideo, Uruguay. A customer writes: "Do you have gluten-free bread?" His app sends this request:

```python
system = "You are the assistant for a bakery chain. Be brief and friendly."
messages = [
    {"role": "user", "content": "Do you have gluten-free bread?"},
]
```

The model replies (example output): "Yes, we bake gluten-free loaves every morning." The response shows `stop_reason` = `end_turn` and usage of 31 input tokens and 12 output tokens (example numbers).

The customer then asks: "Which shops have it?" Tomás's first version sent only this question, and the model asked: "Which product do you mean?"

In the fixed version, his app appends the model's reply and the new question, then sends the full list:

```python
messages = [
    {"role": "user", "content": "Do you have gluten-free bread?"},
    {"role": "assistant", "content": "Yes, we bake gluten-free loaves every morning."},
    {"role": "user", "content": "Which shops have it?"},
]
```

Now the model understands "it". Tomás also notices that input tokens grow with every turn, because the whole history is sent again each time.

## Common Mistake
Many developers assume the API "remembers" the user because they send the same API key each time. The API key identifies your account for billing. It does not create a memory. Keep the system prompt in its own field, and keep the conversation history in your app (in memory, a session or a database) and send it with every request.

## Key Takeaways
1. A request contains a list of messages with `user` and `assistant` roles, an optional system prompt in its own field, a model and a max_tokens limit.
2. A response contains content blocks, a stop reason and token usage. Check the stop reason to know if the reply is complete.
3. The API is stateless: your app must send the full conversation history with every request, so input tokens and cost grow as the conversation grows.

## Hands-on Exercise
**Task:** Turn a 4-turn chat conversation into a messages list on paper, and mark which parts are sent again on the next request.
**Tools:** Pen and paper, or any text editor. No API account is needed for this exercise.
**Steps:**
1. Write a short invented conversation between a customer and a support assistant for a business of your choice: user, assistant, user, assistant (4 turns). Do not use real customer data.
2. Write one system prompt for this assistant in one or two sentences.
3. Write the conversation as a messages list, in the same format as the worked example, with the system prompt kept separate.
4. Add a fifth message: a new user question that only makes sense with the history (for example, it uses "it" or "that one").
5. Mark with a highlighter or a symbol every part that is sent again in the fifth request.
6. Write one sentence: what would the model reply if your app sent only the fifth message?
**What good looks like:** A correct list that starts with `user`, has alternating roles and keeps the system prompt outside the list. All earlier turns are marked as sent again, and your sentence explains that the model would lack context without them.
**Time:** about 15 minutes

## Review Flags
- [VERSION] Context window sizes differ by model and change over time; the lesson points learners to the live models page instead of giving numbers.
- Token counts in the worked example are labelled as example numbers and are not real measurements.
