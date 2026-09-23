# L01 How LLM APIs Work | Presenter Script

Course: AI-14 · Video: 5 min · Words: 739

## Hook
You chat with an AI assistant for ten minutes, and it remembers everything you said. Then you call the same model through its API, ask a follow-up question, and it has no idea what you mean. Nothing is broken. Let's see why.

## Explain
Hi, and welcome to Building Apps with LLM APIs. Over four weeks, you will build real features on a large language model API, using the Claude API as our main example. We start with the basics of a request and a response.

An LLM API works like other web APIs. Your code sends an HTTP request and gets a response back. What is new is the shape of that request. Its main part is a list of messages. Each message has a role and some content.

The user role is text from the person using your app. The assistant role holds earlier replies from the model. The list starts with a user message, and the roles take turns. The system prompt is a separate field, not a message. It sets the model's role, rules and style.

You also send settings. The two you will use in every call are the model, which chooses the model to run, and max tokens, the longest reply you allow. And what is a token? Models do not read words. They read tokens, small pieces of text, often a short word or part of a longer one.

Everything is measured in tokens. Input length, reply length, price and limits. Each model can read only a limited number of tokens in one request. This limit is the context window. It includes the system prompt, every message and the reply. The size depends on the model, so check the current models page.

The response gives you three things. First, content, a list of blocks. For now, you only need the text block. Second, the stop reason. End turn means the model finished normally. Max tokens means it hit your limit, and the reply is cut off. Third, usage, the input and output tokens you pay for.

Now the most important idea. The API is stateless. It does not remember earlier requests. Picture a very knowledgeable assistant who answers the phone, but forgets every call as soon as it ends.

To continue yesterday's discussion, you must read your notes aloud first. Yesterday I asked this, you said that, and now my question is this. The notes are your messages list. And longer notes mean longer, more expensive calls.

## Demonstrate
Let's see this in practice. Tomás builds a help chat for a chain of bakeries in Montevideo, Uruguay. A customer writes, do you have gluten-free bread?

His app sends a short system prompt that says be brief and friendly, and one user message with the question. You'll see something like this. Yes, we bake gluten-free loaves every morning. The stop reason is end turn, and usage shows a few input and output tokens.

Then the customer asks, which shops have it? Tomás's first version sent only this new question. The model replied, which product do you mean? It had no idea what it referred to, because nobody sent the history.

In the fixed version, his app adds the model's earlier reply and the new question to the list, and sends the full list. Now the model understands what it means. Tomás also notices something. Input tokens grow with every turn, because the whole history is sent again each time.

A common mistake is to think the API remembers the user because you send the same API key each time. The key only identifies your account for billing. Your app must keep the history, in memory, a session or a database, and send it every time.

## Recap
Let's recap. First, a request has a list of messages with user and assistant roles, a system prompt in its own field, a model and a max tokens limit. Second, a response has content blocks, a stop reason and token usage. Third, the API is stateless. Your app sends the full history every time, so cost grows as the conversation grows.

## CTA
Now it is your turn. In the exercise, you will turn a four-turn chat into a messages list on paper, and mark every part that is sent again. No API account is needed yet. In the next lesson, Setup: API Keys, SDKs and a Low-Cost Budget, you will make your first real call. See you there.

## Thumbnail
Headline: Why the API Forgets
Image: Navy background, a code-style message list on the left and a phone handset with a faded memory bubble on the right, headline in teal Inter Bold.

## Production Notes
- L01 is not a screen-demo lesson: code appears only on code slides. Keep the code on slides short and readable at video size.
- [VERSION] Context window sizes differ by model and change over time. The voiceover says 'check the models page' and gives no numbers; do not add numbers on slides.
- Token counts on the worked-example slides (31 input, 12 output) are example numbers, not real measurements: label them 'example' on screen.
- Tomás and the Montevideo bakery chain are fictional; stock footage must not show a real shop name or logo.
