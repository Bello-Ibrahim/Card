# HeyGen Batch Pack: AI-26 M2 (Designing AI-Assisted Workflows)

Course: AI for Customer Experience and Support. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L05 Ticket Triage: Sorting and Routing with AI

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M2_L05_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.
- **Pronunciation:** Pronunciation: Katarzyna (kah-tah-ZHIH-nah).

```text
A customer writes: my card was used in another country, and I did not make these payments. If that message waits behind fifty password questions, the customer may lose more money. Sorting tickets well is not only about speed. Sometimes it is about safety.

Welcome to week two. This week we design AI-assisted workflows, and we start with ticket triage. Triage means reading each new message, deciding what kind it is, and sending it to the right place.

AI can do the first step by adding labels. The common ones are topic, such as billing or delivery. Urgency, such as high, normal or low. Language, so the right agent can read it. And sentiment, the customer's mood. Then a routing rule sends the ticket on. For example, card fraud goes to the fraud team with high priority.

How does AI choose a label? A language model compares the meaning of the message with the category names and descriptions you give it. It does not only look for keywords, so it understands that the courier never came is a delivery problem. But it is still a prediction, and predictions can be wrong, even when they sound confident.

A wrong label has a real cost. A fraud report labelled as a billing question may wait for days. A calm message from a vulnerable customer may be marked low urgency.

So two things matter. First, clear categories. Each one needs a short description and one or two examples, and categories must not overlap. If payments and billing both exist, and nobody can explain the difference, the AI will not know either. Second, checking the results. Compare AI labels with labels from experienced agents, and keep checking a sample after launch.

A useful extra rule is an unsure category. Tell the AI: if the message does not clearly fit one category, label it needs review. A person sorts these by hand. That is better than a confident wrong label.

Think of a sorting desk at a big post office. Most letters have clear addresses and go straight to the right van. A good sorter puts the hard-to-read ones in a box for a supervisor, instead of guessing.

Here is an example. Katarzyna leads support at a hypothetical digital bank in Poland. Customers write in Polish, English and Ukrainian. Her team uses five categories: card and fraud, payments and transfers, account access, loans, and other.

She writes a short description for each. Card and fraud means lost or stolen cards, payments the customer did not make, and suspicious messages that ask for codes. Every card and fraud ticket is high priority, and any ticket the AI is unsure about goes to needs review.

Before launch, she takes sixty old tickets, with all personal details removed. Two senior agents label them, and then the AI labels the same tickets. They agree on most, but not all.

Katarzyna studies the differences. The AI labelled, someone called me pretending to be from the bank, as account access, not fraud. So she adds phone calls from people pretending to be the bank to the fraud description. She tests again, and the results improve. A senior agent now checks a small sample every week.

A common mistake is to test once and stop checking. A new product, a new scam or an outage brings new kinds of messages. The categories that worked last month may not fit this month. Keep checking samples, and update your descriptions.

Let's recap. First, AI triage labels tickets by topic, urgency, language and sentiment, so routing rules can send them to the right team. Second, clear categories with short descriptions and a needs review option reduce wrong labels. Third, compare AI labels with human labels before launch, and check a sample regularly after launch.

Now it is your turn. In the exercise, you will define five categories, write fifteen made-up tickets, and label them yourself. Then an AI assistant labels them too, and you count the differences. In the next lesson, we map the workflow and decide what to automate, what to assist, and what stays human. See you there.
```

## L06 Mapping the Workflow: Automate, Assist or Human

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M2_L06_presenter.mp4`
- **Expected length:** about 5.0 minutes (698 words). The quality gate accepts ±10%.

```text
Should AI handle refunds? That is the wrong question. A refund is not one task. It is a chain of small steps. Some are perfect for AI, and others must stay with a person. Today you learn to tell them apart.

In the last lesson, we sorted tickets with AI. Now we look at the whole journey of a case. A workflow is the list of steps from the moment a customer contacts you until the case is closed.

First, write down the steps. Then give each step one of three labels. Automate means AI or a simple automation does the step, with no person involved each time, although people still check samples. Assist means AI prepares a draft, a summary or a suggestion, and a person checks and decides. Human means a person does the step.

To choose a label, ask four questions about each step. How risky is a mistake? How emotional is the situation? How complex is the case? And could the customer be vulnerable? If a wrong answer costs a lot of money, breaks a law or harms someone, the step needs a person, or at least a person's approval.

A vulnerable customer could be an older person who is confused, someone in financial difficulty, or someone who mentions illness. These customers need extra care, and they should reach a person easily.

Here is a simple rule of thumb. If all four answers are low, the step is a good candidate to automate. If one or two are medium, assist is often right. If any answer is high, the step usually stays human.

The labels are not fixed forever. You might start a step as assist, check the results for a while, and then move it to automate. It is safer to move slowly than to automate first and discover problems from customer complaints.

Think of an airport. Automatic gates check passports in simple cases. When a passport is damaged, or a case is unusual, the gate sends the traveller to an officer. The airport did not ask if machines should do border control. It asked which part a machine can do safely.

Let's map a real process. Farah manages customer service for a hypothetical electronics retailer in Kuala Lumpur, Malaysia. She maps the refund process for items returned within the return period.

Step one, the customer asks for a refund in chat. A chatbot collects the order number and reason, so she labels it automate. Step two, checking the order date against the return period, is a fixed rule, so that is automate too. Step three, classifying the reason as faulty, unwanted or damaged, is assist. AI suggests, and the agent confirms.

Step four, deciding on refunds above a set amount, involves money and exceptions, so it is human, and a supervisor approves. Step five, the reply, is assist, because a refusal can be emotional. And step six, a disputed decision, needs judgement and empathy, so it stays human.

Then Farah notices something. Step one can become emotional. If a customer writes that the product caught fire, it is a safety issue, not a normal refund. So she adds a rule: any mention of fire, injury or smoke goes straight to a person. She also sets the refund limit together with the finance team.

A common mistake is to label a whole process, such as refunds or complaints, as automated or human. That hides the details. Always label each step, and write the reason next to it, so others can question and improve it.

Let's recap. First, break each support process into steps, and label each one automate, assist or human. Second, choose the label with four questions: risk, emotion, complexity and vulnerability. Third, start carefully, write down your reasons, and move steps towards automation only after checking the results.

Your turn. In the exercise, choose one process from the list you made in lesson one. Write five to eight steps, answer the four questions for each, and give each step a label and a reason. Mark at least one point where a case must move to a person. In the next lesson, we design that hand-off to a human. See you there.
```

## L07 Designing the Hand-off to a Human

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M2_L07_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.

```text
After ten minutes with a chatbot, you finally reach a person. And the first thing they ask is, how can I help you today? You have to tell your whole story again. Today we design a hand-off that never does that.

In the last lesson, you marked the points where a case must move to a person. That moment is the hand-off, also called escalation. It is the most important moment in an AI support conversation. A good hand-off has two parts: clear triggers, and a clear summary.

There are six triggers. First, the customer asks for a person. Words like real agent or human should always work, in every language you support. Never make the customer ask three times. Second, the assistant is unsure, because the question is not covered, or there is no clear answer.

Third, the customer is very upset: strong anger, repeated complaints, capital letters or threats to leave. Fourth, the topic is sensitive, such as bereavement, fraud, health, safety, legal threats or discrimination. Fifth, a money or policy limit is reached. And sixth, the same question fails twice. Then stop trying, and hand off.

The second part is the hand-off summary. When the conversation moves, the assistant sends the person a short summary, so the customer does not repeat anything. A simple template has six fields.

The customer's need, in one sentence. The trigger, meaning why the hand-off happened. The details collected, only what is needed. What the assistant already said or tried. The customer's mood. And the urgency, with the reason.

The customer should also know what happens next. For example: I am passing you to a colleague. They will see our conversation, so you will not need to repeat it.

Think of the baton pass in a relay race. The first runner does not stop suddenly. They run beside the next runner and place the baton in their hand. A fast chatbot and a skilled agent still give a poor experience if the baton is dropped.

Let's see it in practice. Priya runs support for a hypothetical online pharmacy in Pune, India. Her chatbot answers questions about delivery, opening hours and uploading a prescription. She designs clear hand-off rules for everything else.

Her rules: a request for a person, in English, Hindi or Marathi, means hand off at once. Any question about doses or side effects goes to a pharmacist, because the chatbot must never give medical advice. Emergency words show the local emergency number and alert a person. Large refunds, and two failed tries, also hand off.

A customer writes: my order has not arrived, and my mother needs this medicine tonight. She is very unwell. The chatbot sees two triggers, urgency and health. It replies: I am sorry to hear your mother is unwell. I am connecting you with a colleague now, who will see this conversation.

The agent receives the summary. Missing delivery of medicine needed tonight. Trigger, health and urgency. Order number provided. Mood, worried. Urgency, high. The agent starts helping in the very first message. The customer does not have to explain anything again.

A common mistake is to hide the way to reach a person, so the chatbot handles more conversations. Customers give up, or come back angrier. The chatbot's numbers look good, while the customer experience gets worse. Make asking for a person easy, and treat hand-offs as a normal part of good service.

Let's recap. First, hand off when the customer asks for a person, the assistant is unsure, the customer is very upset, the topic is sensitive, a limit is reached, or a question fails twice. Second, a short summary means the customer does not repeat their story. Third, tell the customer what happens next, and never make it hard to reach a person.

Now it is your turn. In the exercise, you will write five hand-off rules and a summary template. Then you will test the template on two made-up conversations. Keep them, because they are the heart of your capstone. In the next lesson, we automate simple tasks with n8n or Zapier. See you there.
```

## L08 Automating Simple Tasks with n8n or Zapier

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M2_L08_presenter.mp4`
- **Expected length:** about 5.0 minutes (694 words). The quality gate accepts ±10%.
- **Pronunciation:** Aroha and the Wellington outdoor shop are fictional. Pronunciation: Aroha (ah-ROH-hah).

```text
On many support teams, someone reads every contact form message each morning, decides which team should handle it, and copies it into a spreadsheet. Today you build a small automation that does this for you, with no code at all.

In the last lesson, we designed the hand-off. Today we automate a simple, low-risk task. An automation tool connects apps and runs steps for you when something happens. Two popular tools are Zapier and n8n, and we use them in the browser, with no installation.

A simple AI automation has three parts. The trigger is the event that starts it, such as a new form response. The AI step reads the message and does something with it, such as adding one label from a fixed list. And the action does something with the result, such as adding a row to a spreadsheet.

This is the triage idea from lesson five, running on its own. Following your workflow map, labelling is a good step to automate. A wrong label in a log is low risk, and a person still reads each message. We do not send automatic replies to customers here.

Some practical points. Free plan limits change often, so check the current plan before you start. Some AI steps may need a separate account. And test with made-up data only. Never connect a real customer inbox to a trial account.

Think of a row of dominoes. When the first one falls, the trigger, it knocks the next one, the AI step, which knocks the last one, the action. If one domino is in the wrong place, the chain stops. So test the row before you rely on it.

Let's build it. Aroha runs support for a hypothetical outdoor equipment shop in Wellington, New Zealand. She wants each contact form message labelled order, product question, return or other, and logged in a sheet.

First, the test data. I create a form called contact us test, with name, email and message. I submit two made-up responses. Then I create a sheet called support log, with four columns: date, email, message and label.

Now I log in to Zapier and create a new automation. For the trigger, I choose Google Forms, and the event new form response. I connect my test account, choose the form, and test the trigger. A sample response loads.

Next, the AI step. I add the built-in AI option and write the instruction. Read the message. Reply with exactly one label from this list: order, product question, return, other. If unsure, reply other. I map the message field into the input, and test. The output is one label only.

Then the action. I choose Google Sheets and the event create spreadsheet row. I pick the support log sheet and map the date, email, message and AI label to the columns. I test the step, open the sheet, and there is the new row.

Finally, I turn the automation on, submit a new test message, and check the sheet again. In n8n cloud, the same flow uses a form trigger, an AI node and a Google Sheets node.

Aroha tests ten made-up messages. One asks, is the blue tent waterproof, and can I return it if not? It fits two labels. So she updates her instruction: label mixed messages by the first question.

A common mistake is to turn an automation on after one good test, and never look again. A field is renamed, a connection expires, or a run limit is reached, and it stops without warning.

Let's recap. First, a simple AI automation has three parts: a trigger, an AI step and an action. Second, start with low-risk steps like labelling and logging, and keep people responsible for replies. Third, plans and interfaces change often, so check the limits, test with made-up data, and check the run history, because automations can fail silently.

Now build your own. In the exercise, you will create the same three-step automation in Zapier or n8n, submit ten made-up messages, count the correct labels, and improve your instruction once. Next week, you build your capstone, starting with the next lesson: build your support assistant. See you there.
```
