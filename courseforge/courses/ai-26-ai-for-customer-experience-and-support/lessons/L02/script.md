# L02 How AI Assistants Answer Questions | Presenter Script

Course: AI-26 · Video: 5 min · Words: 700

## Hook
A customer asks a chatbot, can I get a refund after forty-five days? The chatbot replies at once, politely and with confidence: yes, you have sixty days. The real policy says thirty. So where did sixty come from? Let's find out.

## Explain
In the last lesson, we saw where AI helps in support. Today we look inside an AI assistant. It has two main parts.

The first part is the language model. This is the part that reads and writes text, like the model behind Claude or ChatGPT. It learned from a huge amount of text, so it is good at language. But it does not know your company. It has never seen your refund policy, your prices or your delivery times.

The second part is your own content: help articles, policies, product guides and approved answers. When a customer asks a question, a well-built assistant first searches your content for the most relevant parts. Then it gives them to the model with an instruction: answer using only this text. This is often called grounding.

Problems happen when this process fails. If the content is missing, the model may fill the gap with something that sounds likely. A guessed answer sounds just as confident as a correct one. This invented answer is often called a hallucination.

There are three other problems. The content can be out of date, so an old article that says sixty days is repeated faithfully, but it is still wrong. The search can find the wrong article, for another country or product. And weak instructions can push the assistant to answer anyway, instead of saying, I don't know.

Here is a simple way to picture it. Imagine a new support agent on their first day. They write well and are very polite. With a correct handbook, they give good answers. With an old handbook, they give old answers.

And if the page they need is missing, a nervous new agent may guess, instead of admitting they do not know. An AI assistant is similar. It is only as good as its handbook, and it needs clear permission to say, I will ask a colleague.

## Demonstrate
Let's see this in practice. Ingrid works in support for a hypothetical furniture retailer in Norway. She is testing an AI assistant before it goes live.

She asks, do you deliver to the islands in the north? The assistant answers: yes, we deliver everywhere in Norway within five working days, at no extra cost. But the delivery article only covers mainland cities. The assistant invented a delivery time and a free delivery promise that nobody approved.

Ingrid makes two changes. First, she asks the delivery team for the correct island delivery rules, and adds a short article. Second, she adds an instruction: if the answer is not in the knowledge base, say you are not sure, and offer to connect the customer with a person.

She tests again. For island delivery, the assistant now gives the approved answer. For a question about delivery to Sweden, which is still not covered, it says it is not sure, and offers a person. That is exactly what she wants.

One common mistake is to believe that a confident, well-written answer is probably correct. With language models, tone tells you nothing about accuracy. A model writes a wrong answer with the same calm confidence as a right one. So always check answers against your source content, and make, I don't know, an acceptable answer.

## Recap
Let's recap. First, an AI support assistant combines a language model, which is good at language, with your own content, which holds the facts. Second, when content is missing, out of date or hard to find, the assistant may invent a confident answer. Third, good content and clear instructions, including permission to say I don't know, reduce invented answers.

## CTA
Now try it yourself. In the exercise, you will ask Claude or ChatGPT about the refund policy of a made-up company, first without the policy, then with the policy pasted in. You will compare the two answers and note every invented detail. In the next lesson, we look at writing a knowledge base that AI can use. See you there.

## Thumbnail
Headline: Why Did It Say 60?
Image: Navy background, a chat bubble saying '60 days' with a red question mark beside a policy card showing '30 days', headline in teal Inter Bold.

## Production Notes
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT: check what the free plans currently offer and how they use chat content before recording (the exercise names both tools).
- Ingrid and the Norwegian furniture retailer are fictional; stock footage must show no real shop names or logos.
- Lumora Home (exercise) is a made-up company; learners must not paste real customer or company data into free tools.
- The 60-day and 30-day refund figures in the hook are part of the made-up example, not a real policy.
