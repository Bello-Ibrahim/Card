# L02 How AI Assistants Answer Questions

Course: AI-26 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
A customer asks a chatbot, "Can I get a refund after 45 days?" The chatbot replies at once, politely and with confidence: "Yes, you have 60 days." The real policy says 30 days. Where did the chatbot get "60 days"? This lesson explains how AI assistants find their answers, and why they sometimes invent them.

## Explanation
An AI support assistant has two main parts.

**The language model.** This is the part that reads and writes text, such as the model behind Claude or ChatGPT. It learned from a very large amount of public text, so it is good at language: understanding questions, writing clear sentences and changing tone. But it does not know your company. It has never seen your refund policy, your prices or your delivery times.

**Your own content.** This is your knowledge base: help articles, policies, product guides and approved answers. When a customer asks a question, a well-built assistant first searches your content for the most relevant parts. Then it gives those parts to the language model with an instruction such as: "Answer the customer's question using only this text." The model writes the answer from your content.

This combination is sometimes called "retrieval" or "grounding", because the answer is grounded in (based on) your own documents.

Problems happen when this process fails:

- **The content is missing.** If there is no article about refunds after 45 days, the model may fill the gap with something that sounds likely. Language models are built to produce fluent text, so a guessed answer can sound just as confident as a correct one. This is often called a **hallucination**: an invented answer that sounds real.
- **The content is wrong or out of date.** If an old article still says "60 days", the assistant will repeat it correctly, but the answer is still wrong.
- **The search finds the wrong article.** If two articles have similar titles, the assistant may use the one for another country or another product.
- **The instructions are weak.** If the assistant is not told to say "I don't know" or to pass the question to a person, it may try to answer anyway.

**Analogy:** Imagine a new support agent on their first day. They write well and are very polite. If you give them a well-organised, correct handbook, they give good answers. If the handbook is old, they give old answers. If the page they need is missing, a nervous new agent may guess rather than admit they do not know. An AI assistant behaves in a similar way: its answers are only as good as the handbook it has, and it needs clear permission to say "I will ask a colleague".

## Worked Example
Ingrid works in customer support for a hypothetical furniture retailer in Norway. She is testing an AI assistant before it goes live.

She asks: "Do you deliver to the islands in the north?" The assistant answers: "Yes, we deliver everywhere in Norway within 5 working days at no extra cost." It sounds helpful. But the company's delivery article only covers mainland cities. The assistant filled the gap with a likely-sounding answer, including a delivery time and a free-delivery promise that nobody approved.

Ingrid makes two changes. First, she asks the delivery team for the correct island delivery rules and adds a short article. Second, she adds an instruction: "If the answer is not in the knowledge base, say you are not sure and offer to connect the customer with a person." She tests again. For island delivery, the assistant now gives the approved answer. For a question about delivery to Sweden, which is still not covered, it says it is not sure and offers a person.

## Common Mistake
Many people believe that a confident, well-written answer is probably a correct answer. With language models, tone tells you nothing about accuracy. A model writes a wrong answer with the same calm confidence as a right one. The correction is to always check answers against your source content, and to design the assistant so that "I don't know, let me connect you with a colleague" is an acceptable answer.

## Key Takeaways
1. An AI support assistant combines a language model, which is good at language, with your own content, which holds the facts about your company.
2. When content is missing, out of date or hard to find, the assistant may invent a confident answer (a hallucination).
3. Good content and clear instructions, including permission to say "I don't know" and pass to a person, reduce invented answers.

## Hands-on Exercise
**Task:** Ask Claude or ChatGPT a question about a made-up company's refund policy, first without and then with the policy text pasted in. Compare the two answers and note any invented details.
**Tools:** Claude or ChatGPT (free plan) [VERSION]; a notes app.
**Steps:**
1. Open a new chat. Ask: "What is the refund policy of Lumora Home, and can I return a lamp after 40 days?" Lumora Home is a made-up company, so the assistant cannot know the answer.
2. Copy the answer into your notes. Underline every specific detail, such as a number of days, a fee or a condition.
3. Open a new chat. Paste this short policy: "Lumora Home refund policy: Customers can return items within 30 days of delivery for a full refund. Items must be unused. Lighting products have a 14-day return period. Refunds are paid to the original payment method within 10 working days."
4. Below the policy, write: "Using only the policy above, answer: can I return a lamp after 40 days? If the policy does not say, tell me."
5. Compare the two answers. For each underlined detail from step 2, write "invented", "correct" or "not covered".
6. Write two sentences about what changed when the assistant had the policy text.
**What good looks like:** A short comparison table showing which details in the first answer were invented or vague (or whether the assistant said it could not know), and whether the second answer correctly used the 14-day rule for lighting. Only the made-up company and made-up policy are used; no real customer or company data is pasted into the tool.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT: check what the free plans currently offer and how they use chat content before recording.
- Judgement call (from curriculum): exercises use a made-up company; learners are told not to paste real customer or company data into free tools.
