# HeyGen Batch Pack: AI-26 M1 (AI in Support: The Basics)

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

## L01 Where AI Helps in Customer Support

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M1_L01_presenter.mp4`
- **Expected length:** about 5.2 minutes (734 words). The quality gate accepts ±10%.

```text
Think about the last busy day on your support team. How many questions were new? And how many had you already answered a hundred times? AI is useful for that second group. Today we see where it helps, and where people must stay in charge.

Hi, and welcome to AI for Customer Experience and Support. In this first lesson, we look at the five most common ways AI helps a support team.

AI in support is not one single tool. It is a group of uses. The first use is chatbots. A chatbot answers customer questions in a chat window, on a website, in an app or in a messaging service. Modern chatbots use a language model, so customers can write in their own words.

The second use is ticket triage. When a message arrives by email, form or chat, AI reads it and adds labels: the topic, the urgency, the language and the customer's mood. Then the ticket goes to the right team.

The third use is agent assistance. Here AI does not talk to the customer. It helps the agent. It can suggest a reply, summarise a long conversation, find the right help article, or translate a message. The agent reads, edits and decides what to send.

The fourth use is the knowledge base, your collection of help articles, policies and guides. AI can help write and update articles, find gaps, and search them to answer questions. A good knowledge base supports almost everything else.

The fifth use is support analytics. AI reads thousands of tickets, reviews and survey comments, and groups them by theme. For example, many complaints this month mention a new login page. Now managers can fix the cause.

All five uses share one goal: faster, more consistent answers, without losing the human touch. AI is good at repeated, predictable work. People are better at judgement, empathy and unusual cases. A good team uses both.

Here is a picture to keep in mind. Think of a busy hospital reception. A sign on the wall answers, where is the pharmacy? A receptionist sends patients to the right department. A nurse prepares notes for the doctor. And the doctor makes the important decisions.

AI in support can play the sign, the receptionist and the helpful nurse. But the difficult decisions still belong to a person.

Now let's meet three hypothetical companies. First, a telecom company in Morocco. Youssef leads a support team that receives many messages in Arabic, French and English, mostly about bills and mobile data.

The team adds AI triage. Each message is labelled by topic and language, and sent to the right queue. Agents now start each ticket already knowing both. But messages about a lost or stolen phone always go straight to a person, because they can involve fraud.

Second, an online shop in Vietnam that sells home appliances. Linh runs its support. Customers often ask, where is my order, and how do I return an item? Linh sets up a chatbot that answers these two questions from the help articles. When a customer wants to complain about a damaged product, the chatbot offers a person.

Third, a small airline in Mexico. Mariana manages its contact centre. Flight changes involve rules, fees and stressed travellers. So AI never answers customers directly. It suggests a reply and a summary, and the agent checks the fare rules and edits before sending.

Notice that each company chose a different use, based on its own questions and risks.

A common mistake is to start by asking, how can we replace agents with a chatbot? That leads to frustrated customers. A better question is, which of our questions are simple, frequent and low risk? Start there, and grow step by step.

Let's recap. First, the five main uses of AI in support are chatbots, ticket triage, agent assistance, knowledge bases and support analytics. Second, AI works best on frequent, predictable, low-risk questions. People handle judgement, empathy and unusual cases. Third, start from your own questions and risks, not from a tool.

Now it is your turn. In the exercise below this video, you will list the ten questions your team receives most often. You will mark each one: AI can answer, AI can help an agent, or a human must handle it. Keep your list for later. In the next lesson, we look at how AI assistants answer questions. See you there.
```

## L02 How AI Assistants Answer Questions

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M1_L02_presenter.mp4`
- **Expected length:** about 5.0 minutes (696 words). The quality gate accepts ±10%.

```text
A customer asks a chatbot, can I get a refund after forty-five days? The chatbot replies at once, politely and with confidence: yes, you have sixty days. The real policy says thirty. So where did sixty come from? Let's find out.

In the last lesson, we saw where AI helps in support. Today we look inside an AI assistant. It has two main parts.

The first part is the language model. This is the part that reads and writes text, like the model behind Claude or ChatGPT. It learned from a huge amount of text, so it is good at language. But it does not know your company. It has never seen your refund policy, your prices or your delivery times.

The second part is your own content: help articles, policies, product guides and approved answers. When a customer asks a question, a well-built assistant first searches your content for the most relevant parts. Then it gives them to the model with an instruction: answer using only this text. This is often called grounding.

Problems happen when this process fails. If the content is missing, the model may fill the gap with something that sounds likely. A guessed answer sounds just as confident as a correct one. This invented answer is often called a hallucination.

There are three other problems. The content can be out of date, so an old article that says sixty days is repeated faithfully, but it is still wrong. The search can find the wrong article, for another country or product. And weak instructions can push the assistant to answer anyway, instead of saying, I don't know.

Here is a simple way to picture it. Imagine a new support agent on their first day. They write well and are very polite. With a correct handbook, they give good answers. With an old handbook, they give old answers.

And if the page they need is missing, a nervous new agent may guess, instead of admitting they do not know. An AI assistant is similar. It is only as good as its handbook, and it needs clear permission to say, I will ask a colleague.

Let's see this in practice. Ingrid works in support for a hypothetical furniture retailer in Norway. She is testing an AI assistant before it goes live.

She asks, do you deliver to the islands in the north? The assistant answers: yes, we deliver everywhere in Norway within five working days, at no extra cost. But the delivery article only covers mainland cities. The assistant invented a delivery time and a free delivery promise that nobody approved.

Ingrid makes two changes. First, she asks the delivery team for the correct island delivery rules, and adds a short article. Second, she adds an instruction: if the answer is not in the knowledge base, say you are not sure, and offer to connect the customer with a person.

She tests again. For island delivery, the assistant now gives the approved answer. For a question about delivery to Sweden, which is still not covered, it says it is not sure, and offers a person. That is exactly what she wants.

One common mistake is to believe that a confident, well-written answer is probably correct. With language models, tone tells you nothing about accuracy. A model writes a wrong answer with the same calm confidence as a right one. So always check answers against your source content, and make, I don't know, an acceptable answer.

Let's recap. First, an AI support assistant combines a language model, which is good at language, with your own content, which holds the facts. Second, when content is missing, out of date or hard to find, the assistant may invent a confident answer. Third, good content and clear instructions, including permission to say I don't know, reduce invented answers.

Now try it yourself. In the exercise, you will ask Claude or ChatGPT about the refund policy of a made-up company, first without the policy, then with the policy pasted in. You will compare the two answers and note every invented detail. In the next lesson, we look at writing a knowledge base that AI can use. See you there.
```

## L03 Writing a Knowledge Base That AI Can Use

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M1_L03_presenter.mp4`
- **Expected length:** about 5.0 minutes (688 words). The quality gate accepts ±10%.

```text
Most support teams have plenty of content. But it lives in long emails, old documents and the heads of experienced colleagues. An AI assistant cannot use that. Today we turn it into short, clear articles that customers and AI can both use.

In the last lesson, we saw that an AI assistant is only as good as the content it can find. So how do we write that content? An article that works well for AI has the same features as one that works well for a busy customer. Five features matter most.

First, one topic per article. An article called delivery information that covers prices, times, tracking, damaged parcels and returns is hard to search. Split it into separate articles, such as how to track your order, and what to do if your parcel is damaged.

Second, a clear title in the customer's words. How do I change my delivery address, is better than address modification procedure.

Third, short steps and plain language. Use numbered steps, short sentences and one idea per sentence. Be careful with words like usually, or in most cases. AI may repeat a vague rule as if it were a firm promise.

Fourth, a review date, because old articles are a main reason for wrong answers. And fifth, an owner, such as the logistics team. When something changes, everybody knows who must update the article.

AI can help you write these articles. Paste an internal note into Claude or ChatGPT, and ask for a clean article with a set structure. But AI can also add details, drop an exception, or make a rule sound more certain than it is. So there is one firm rule. A person checks every fact against the source before publishing.

And before you paste anything, remove personal data, such as customer names, phone numbers and order numbers, and anything confidential. Follow your company's AI tool policy.

Think of a well-organised pharmacy shelf. Each medicine has its own box, a clear label and an expiry date. If all the medicines were mixed in one big bag, even an expert would make mistakes.

Let's see an example. Chukwuemeka leads support at a hypothetical online electronics shop in Lagos, Nigeria. The logistics manager sends a long email about delivery delays. It mixes several topics.

Heavy rain has slowed deliveries to some states. A courier partner has changed. Customers in affected areas should expect up to five extra working days. Old tracking links no longer work. And agents may offer free re-delivery if a parcel is returned by mistake.

He removes staff names and internal phone numbers. Then he asks the AI assistant for two customer articles, one on delivery delays, one on tracking after the courier change. He asks for question titles, short numbered steps, review and owner lines, and only facts from the note.

The drafts look good. But when he checks them against the email, he finds two problems. The first draft says all deliveries are delayed, but the email says some states. The second draft invents a new tracking website address.

He corrects both, adds the list of affected states, and publishes. The free re-delivery rule is for agents, not customers, so he keeps it in an internal article.

A common mistake is to paste a whole knowledge base into an AI tool and call it ready. Long, mixed, out-of-date articles give long, mixed, out-of-date answers. Cleaning the content is the most important part of the project.

Let's recap. First, good articles have one topic, a clear title in the customer's words, short steps, a review date and an owner. Second, AI can turn messy notes into clean drafts quickly, but it may add, remove or change facts. Third, a person checks every fact against the source, and personal data is removed before pasting.

Your turn. In the exercise, you will use an AI assistant to turn a messy note from a made-up bike shop into two clean articles. Then you will check every fact against the note, and list what you corrected. In the next lesson, we look at brand voice and reply drafting. See you there.
```

## L04 Brand Voice and Reply Drafting

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M1_L04_presenter.mp4`
- **Expected length:** about 5.0 minutes (690 words). The quality gate accepts ±10%.
- **Pronunciation:** Pronunciation: Ana Paula (AH-nah POW-lah), São Paulo (sow POW-loo).

```text
Two replies say the same thing: your refund will arrive in five working days. One makes the customer feel heard. The other makes them feel like a ticket number. The difference is tone. Today we help AI draft replies that sound like you.

In the last lesson, we built clean knowledge base articles. Now we use that content to reply to customers, in your own brand voice, with a person responsible for every message.

Brand voice is the way your company sounds when it writes. Some companies are formal and careful. Others are friendly and relaxed. Customers notice when replies sound completely different from one agent to the next.

Without guidance, AI tends to write in a general style that is often too long and too formal. A short tone guide fixes much of this. It is about five lines long, and it answers five questions. Who are we? How formal are we? How do we show empathy? How long are replies? And what do we never do?

For example: we speak to customers as neighbours. We use first names. We name the customer's problem before the solution. Replies stay under one hundred and twenty words. And we never promise dates or compensation that are not in the policy.

You give the AI the tone guide, the customer message and the relevant policy. It drafts a reply in your voice. The same guide works in several languages. But politeness rules differ, so a person who reads the language well should check important replies.

The order of importance is clear. Accuracy first, then empathy and clarity, then speed. A fast reply with a wrong promise creates a second, bigger problem. So an agent always checks facts, adjusts the tone and removes anything the company cannot promise.

Think of a recipe card in a restaurant chain. Cooks in different cities make a dish that tastes the same, because they follow the same card. But the cook still tastes the dish before it leaves the kitchen. The AI drafts from the recipe card. The agent tastes before serving.

Here is an example. Ana Paula leads support for a hypothetical meal-kit company in São Paulo, Brazil. Her tone guide says: warm and direct, first names, name the problem first, under one hundred words, and never promise credits that are not in the policy.

A customer writes: third time this month my box arrived without the vegetables. I'm paying for nothing. Cancel everything. Ana Paula removes the name and order number, then gives the AI the tone guide, the message and the policy. The policy gives a credit for missing items, and cancellation is possible any time in the account settings.

The first draft starts: we sincerely apologise for any inconvenience. It is too formal. It does not name the problem. And it offers a full refund for the month, which the policy does not allow.

Ana Paula edits it. Three incomplete boxes in one month is not acceptable, and I understand why you want to cancel. I have added a credit for the missing vegetables. You can cancel in your account settings, or I can ask our warehouse to check your next box personally.

A common mistake is to send AI drafts after a quick look, because they sound professional. A draft can sound perfect and still contain a wrong date, or a promise the company cannot keep. Read every draft as the customer would. Check every fact, and change at least the first sentence so it answers this person's real problem.

Let's recap. First, a short tone guide of about five lines helps AI draft replies that sound like your company, in several languages. Second, accuracy comes first, then empathy and clarity, then speed. Third, an agent always reviews, checks and edits an AI draft before it is sent.

Now it is your turn. In the exercise, you will write a five-line tone guide, then ask an AI assistant to draft replies to three upset, made-up customers. You will edit each draft and note what you changed and why. Next week begins with ticket triage, sorting and routing with AI. See you there.
```
