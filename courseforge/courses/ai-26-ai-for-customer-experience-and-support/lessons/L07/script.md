# L07 Designing the Hand-off to a Human | Presenter Script

Course: AI-26 · Video: 5 min · Words: 692

## Hook
After ten minutes with a chatbot, you finally reach a person. And the first thing they ask is, how can I help you today? You have to tell your whole story again. Today we design a hand-off that never does that.

## Explain
In the last lesson, you marked the points where a case must move to a person. That moment is the hand-off, also called escalation. It is the most important moment in an AI support conversation. A good hand-off has two parts: clear triggers, and a clear summary.

There are six triggers. First, the customer asks for a person. Words like real agent or human should always work, in every language you support. Never make the customer ask three times. Second, the assistant is unsure, because the question is not covered, or there is no clear answer.

Third, the customer is very upset: strong anger, repeated complaints, capital letters or threats to leave. Fourth, the topic is sensitive, such as bereavement, fraud, health, safety, legal threats or discrimination. Fifth, a money or policy limit is reached. And sixth, the same question fails twice. Then stop trying, and hand off.

The second part is the hand-off summary. When the conversation moves, the assistant sends the person a short summary, so the customer does not repeat anything. A simple template has six fields.

The customer's need, in one sentence. The trigger, meaning why the hand-off happened. The details collected, only what is needed. What the assistant already said or tried. The customer's mood. And the urgency, with the reason.

The customer should also know what happens next. For example: I am passing you to a colleague. They will see our conversation, so you will not need to repeat it.

Think of the baton pass in a relay race. The first runner does not stop suddenly. They run beside the next runner and place the baton in their hand. A fast chatbot and a skilled agent still give a poor experience if the baton is dropped.

## Demonstrate
Let's see it in practice. Priya runs support for a hypothetical online pharmacy in Pune, India. Her chatbot answers questions about delivery, opening hours and uploading a prescription. She designs clear hand-off rules for everything else.

Her rules: a request for a person, in English, Hindi or Marathi, means hand off at once. Any question about doses or side effects goes to a pharmacist, because the chatbot must never give medical advice. Emergency words show the local emergency number and alert a person. Large refunds, and two failed tries, also hand off.

A customer writes: my order has not arrived, and my mother needs this medicine tonight. She is very unwell. The chatbot sees two triggers, urgency and health. It replies: I am sorry to hear your mother is unwell. I am connecting you with a colleague now, who will see this conversation.

The agent receives the summary. Missing delivery of medicine needed tonight. Trigger, health and urgency. Order number provided. Mood, worried. Urgency, high. The agent starts helping in the very first message. The customer does not have to explain anything again.

A common mistake is to hide the way to reach a person, so the chatbot handles more conversations. Customers give up, or come back angrier. The chatbot's numbers look good, while the customer experience gets worse. Make asking for a person easy, and treat hand-offs as a normal part of good service.

## Recap
Let's recap. First, hand off when the customer asks for a person, the assistant is unsure, the customer is very upset, the topic is sensitive, a limit is reached, or a question fails twice. Second, a short summary means the customer does not repeat their story. Third, tell the customer what happens next, and never make it hard to reach a person.

## CTA
Now it is your turn. In the exercise, you will write five hand-off rules and a summary template. Then you will test the template on two made-up conversations. Keep them, because they are the heart of your capstone. In the next lesson, we automate simple tasks with n8n or Zapier. See you there.

## Thumbnail
Headline: Don't Drop the Baton
Image: Navy background, two hands passing a teal relay baton, one hand drawn as a chat bubble and one as a person, headline in teal Inter Bold.

## Production Notes
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording (optional tool in the exercise).
- Safety: the pharmacy chatbot never gives medical advice and shows the local emergency number; no specific number is given on screen, so no [REGION] tag is needed. Do not add a real emergency number to the slide.
- Priya and the Pune online pharmacy are fictional; stock footage must show no real pharmacy names, logos or medicine brands.
- content.md lists six triggers (the curriculum summary lists five; content.md adds 'money or policy limits'). The script follows content.md.
- Hand-off is a central theme of the course and the capstone: keep the trigger slide (scene 4) and the summary template slide (scene 6) on screen long enough to read.
