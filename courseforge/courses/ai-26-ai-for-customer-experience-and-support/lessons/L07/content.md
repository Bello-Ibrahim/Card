# L07 Designing the Hand-off to a Human

Course: AI-26 · Module: M2 · Objectives: O4, O5 · Video: 5 min

## Hook
Most people have had this experience: after ten minutes with a chatbot, you finally reach a person, and the first thing they ask is "How can I help you today?" You have to tell your whole story again. A hand-off to a human is the most important moment in an AI support conversation. This lesson shows how to design it well.

## Explanation
A **hand-off** (also called escalation) is the moment when an AI assistant passes the conversation to a person. A good hand-off has two parts: clear **triggers** that decide when to hand off, and a clear **summary** that the person receives.

**Hand-off triggers.** Your assistant should pass the conversation to a person when:

1. **The customer asks for a person.** Words such as "talk to a person", "real agent" or "human" should always work, in every language you support. Never make the customer ask three times.
2. **The assistant is unsure.** The question is not covered by the knowledge base, or the assistant cannot find a clear answer.
3. **The customer is very upset.** Strong anger, repeated complaints, capital letters or threats to leave are signs to bring in a person.
4. **The topic is sensitive.** For example bereavement (a customer's family member has died), fraud, health, safety, legal threats or complaints about discrimination.
5. **Money or policy limits are reached.** For example, a refund above a limit your company sets, or any request for an exception to the policy.
6. **The same question fails twice.** If the customer repeats or rephrases a question and still does not get a useful answer, stop trying and hand off.

**The hand-off summary.** When the conversation moves to a person, the assistant should send a short summary so that the customer does not have to repeat anything. A simple template:

- **Customer need:** one sentence.
- **Trigger:** why the hand-off happened.
- **Details collected:** for example order number or product (only what is needed).
- **What the assistant already said or tried.**
- **Customer mood:** calm, worried, upset.
- **Urgency:** normal or high, and why.

The customer should also know what happens next: "I am passing you to a colleague. They will see our conversation, so you will not need to repeat it."

**Analogy:** A hand-off is like the baton pass in a relay race. The first runner does not stop suddenly and drop the baton; they run alongside the next runner and place it in their hand. If the baton falls, the team loses time, even if both runners are fast. A fast chatbot and a skilled agent still give a poor experience if the hand-off between them is dropped.

## Worked Example
Priya runs support for a hypothetical online pharmacy in Pune, India. Her chatbot answers questions about delivery, opening hours and how to upload a prescription. She designs these hand-off rules:

- A customer asks for a person, in English, Hindi or Marathi → hand off at once.
- Any question about doses, side effects or whether two medicines can be taken together → hand off to a pharmacist. The chatbot must never give medical advice.
- Words linked to an emergency, such as "overdose" or "can't breathe" → show the local emergency number at once and alert a person.
- Refund request above the limit set by finance → hand off.
- No clear answer after two tries → hand off.

A customer writes: "My order has not arrived and my mother needs this medicine tonight, she is very unwell." The chatbot sees two triggers: urgency and health. It replies: "I am sorry to hear your mother is unwell. I am connecting you with a colleague now, who will see this conversation."

The agent receives: "Need: missing delivery of medicine needed tonight. Trigger: health and urgency. Details: order number provided. Assistant said: connecting to a colleague. Mood: worried. Urgency: high – medicine needed today." The agent starts helping in the first message.

## Common Mistake
Many teams hide the option to reach a person, because they want the chatbot to "handle" more conversations. Customers who cannot reach a person often give up or come back angrier through another channel. This makes the chatbot's numbers look good while the customer experience gets worse. The correction: make asking for a person easy and respected, and measure hand-offs as a normal part of good service.

## Key Takeaways
1. Hand off when the customer asks for a person, the assistant is unsure, the customer is very upset, the topic is sensitive, a money or policy limit is reached, or the same question fails twice.
2. A short hand-off summary means the customer does not have to repeat their story.
3. Tell the customer what happens next, and never make it hard to reach a person.

## Hands-on Exercise
**Task:** Write 5 hand-off rules and a hand-off summary template, then test the template on 2 sample conversations.
**Tools:** A document or notes app. Optional: Claude or ChatGPT (free plan) [VERSION] to draft summaries from the sample conversations.
**Steps:**
1. Choose the made-up company or process you mapped in L06.
2. Write 5 hand-off rules. Include at least: "customer asks for a person", "angry customer", "refund above a limit" (choose your own limit), and "legal or safety issue".
3. Write a hand-off summary template with 5 or 6 fields, using the list in this lesson.
4. Write 2 short made-up conversations (6 to 10 lines each) between a customer and a chatbot. In each one, at least one of your triggers should happen.
5. For each conversation, fill in the summary template by hand. Optional: ask an AI assistant to fill it in and compare its summary with yours.
6. Check: could an agent start helping from the summary alone, without reading the whole conversation?
**What good looks like:** Five clear rules that a colleague could apply without asking you questions, a short template, and two filled summaries that give an agent everything needed in a few lines. The rules make it easy to reach a person.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
- Judgement call (from curriculum): sample conversations are made up; no real customer data.
- Safety note for reviewer: the pharmacy example tells the chatbot never to give medical advice and to show a local emergency number; no specific number is given, so no region tag is needed.
