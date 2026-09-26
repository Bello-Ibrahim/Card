# HeyGen Batch Pack: AI-26 M3 (Build, Test and Launch Your Assistant)

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

## L09 Build Your Support Assistant

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M3_L09_presenter.mp4`
- **Expected length:** about 5.0 minutes (690 words). The quality gate accepts ±10%.

```text
You have a clean knowledge base, a tone guide and hand-off rules. This week you combine them into a working support assistant. And here is the secret. A good first version is not clever. It is small, and it is honest.

Welcome to week three, where you build your capstone, a support assistant with a hand-off to a human. In this lesson, we set up the assistant itself. You can use any free chatbot builder. I will use Botpress. Every builder asks you to make four decisions.

The first decision is scope. Choose three to five frequent, low-risk topics from the list you made in lesson one, such as opening hours, order tracking and returns. Everything else is out of scope, and goes to a person.

The second is knowledge. Add the clean articles you wrote in lesson three, only for your scope. And never upload real customer data or confidential documents to a free tool.

The third is instructions. Write short, clear rules. Answer only questions about your topics. Use only the knowledge base, and if the answer is not there, say you are not sure and offer a person. Follow the tone guide. Never promise refunds, discounts or dates that are not in the knowledge base.

And one more instruction, the most important. If the customer asks for a person, is very upset, or mentions a legal or safety issue, offer a person at once. These are your hand-off rules from lesson seven.

The fourth decision is transparency. Tell customers they are talking to AI, right in the welcome message, and tell them they can ask for a person at any time. It builds trust. Your region may also have its own rules, which we look at in lesson twelve.

Think of opening a small food stall before a full restaurant. You serve a few dishes you make well, you show the menu clearly, and you point people next door for anything else.

Let's build one. Leila works at a hypothetical language school in Amman, Jordan. Her assistant covers three topics: course start dates, choosing a level, and payment methods.

I sign in to the free plan and create a new bot. I name it Noor, language school assistant, test. Then, in the knowledge section, I add three short articles: when do courses start, how do I choose my level, and how can I pay. I paste the text instead of uploading big files.

Next, the instructions. I paste the scope, the knowledge only rule, the tone guide and the hand-off rules. Then the welcome message: hello, I am Noor, the school's AI assistant. I can help with course dates, levels and payment. You can ask for a person at any time.

Now I test in the preview chat. I ask one question for each topic, and check each answer against the articles. Then an out-of-scope question: can you help with my visa? Noor should say it is not sure, and offer a person.

But Noor gives general visa advice. So Leila adds an instruction: do not give advice on visas or legal matters, offer a person. The retest passes. Then I ask the next course date in Arabic, and check both the answer and the tone.

Finally, I publish the bot in test mode only, and copy its share link for testing.

A common mistake is to add every document you have, hoping the assistant will answer everything. Old or overlapping content gives it more chances to find the wrong text. Start small, and add topics only when the current ones work.

Let's recap. First, every chatbot builder asks for four decisions: scope, knowledge, instructions and transparency. Second, start with three to five frequent, low-risk topics and clean content. Third, tell customers they are talking to AI, and that they can ask for a person at any time.

This is capstone step one. In the exercise, you will build your own assistant for at least three topics, with an honest welcome message, and test it with one out-of-scope question. Take screenshots for your capstone. In the next lesson, we are adding the hand-off flow. See you there.
```

## L10 Adding the Hand-off Flow

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M3_L10_presenter.mp4`
- **Expected length:** about 5.0 minutes (682 words). The quality gate accepts ±10%.
- **Pronunciation:** Wanjiru and the Nairobi safari company are fictional. Pronunciation: Wanjiru (wahn-JEE-roo).

```text
In lesson seven, you wrote hand-off rules on paper. Today you connect them to a place where a real person will see them, and you make sure the customer knows exactly what happens next.

This is capstone step two. Your assistant from the last lesson answers questions. Now it needs a hand-off flow, and every hand-off flow has four parts: trigger, collect, send and tell.

Trigger means the rules that start the hand-off, such as a request for a person, a very upset customer, a refund above your limit, or a safety issue. Collect means what the assistant asks first. Only what is needed, such as an email address, and permission to share the conversation.

Send means where the summary goes: an email inbox, a help desk ticket, or a team chat channel. Tell means what the customer sees: who will reply, through which channel, and when.

There are two common ways to send the summary. Many chatbot builders have their own hand-off or email notification feature. Or, if the builder can send data out, an automation in n8n or Zapier can email the team or add a row to a sheet, as in lesson eight. Choose the simplest option that works on your plan.

The final message must be honest and specific. Your request has been escalated, is weak. Compare this. I have passed your question to our support team, with a summary of our chat. A person will reply by email within one working day. Only promise times your team can meet.

Think of leaving a message at a hotel reception. A good receptionist writes who called, why and how to reply, puts the note in the right box, and tells the caller when the guest will get it. A note on the wrong desk is no message at all.

Let's build it. Wanjiru manages customer service for a hypothetical safari travel company in Nairobi, Kenya. Her assistant answers questions about trip dates, packing and payment, often when the office is closed.

In the chatbot builder, I open the hand-off settings. I add the triggers from lesson seven: person, agent, change my booking, injured and medical. So a request for a person, a booking change, or a safety or medical issue will hand off.

Next, collect. The assistant asks: may I have your email address, so a colleague can reply? I will share a summary of our chat with them. Then I set the summary fields from the template: need, trigger, details, what the assistant said, mood and urgency.

Now, send. The simplest option is the builder's own email notification, going to a test support inbox. If your builder can send data out, you could instead pass the hand-off to Zapier or n8n, to email the team and log it in a hand-offs sheet.

Then, tell. For out of hours, I write: our team is offline now. A person will read your message and reply by email when the office opens. For an emergency during your trip, use the emergency number in your travel documents.

Finally, I test with a made-up conversation, and check the inbox. The summary arrived, but without the customer's email. The assistant handed off before asking. So Wanjiru moves collect before send, and the retest is complete.

A common mistake is to see the confirmation message in the chat and assume it works. The summary may go to an old inbox nobody reads. Always test the full path, until a person sees the summary.

Let's recap. First, a hand-off flow has four parts: trigger, collect, send and tell. Second, connect it to a real human channel, with the builder's own feature or an automation, and choose the simplest option. Third, tell customers who will reply, how and when, and test the full path.

This is capstone step two. In the exercise, you will fill in the four-part template, add at least four triggers, and connect your hand-off to a test inbox or sheet. Then test three made-up conversations. In the next lesson, we look at testing your assistant for accuracy, tone and safety. See you there.
```

## L11 Testing Your Assistant: Accuracy, Tone and Safety

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M3_L11_presenter.mp4`
- **Expected length:** about 5.0 minutes (689 words). The quality gate accepts ±10%.
- **Pronunciation:** Mateo and the Córdoba fitness chain are fictional. Pronunciation: Córdoba (KOR-doh-bah). Stock footage must show no real gym brand names or logos.

```text
Your assistant answers your three test questions perfectly. Is it ready? Probably not. Real customers make spelling mistakes, write in other languages, ask two things at once, and get angry. Today you learn to test for real customers.

This is capstone step three. You have an assistant and a hand-off flow. Now you need a test set, a fixed list of questions, each with the answer or behaviour you expect. About twenty questions is a good size for a first prototype.

Mix six types. About six standard questions from your scope. About four tricky ones, with spelling mistakes, very short messages, or two questions in one. About three out-of-scope questions, where you expect, I'm not sure, and an offer of a person.

Then about three emotional questions from angry, worried or sad customers. About two hand-off and safety questions, such as a legal threat or a request for a person. And about two questions in the other languages your customers use.

Score each answer from zero to two, on three points. Accuracy: is it correct and from the knowledge base? Tone: does it follow the tone guide, with empathy where needed? And hand-off: does it hand off when it should, and not when it should not?

Also note fairness. Is the answer just as good with spelling mistakes, or in another language? And note privacy. Does the assistant ask for more personal data than it needs?

The lesson page has an eight-point checklist for every test conversation. For example, did it use only facts from the knowledge base? Did it hand off for every trigger? Did it say that it is an AI assistant?

Then fix the biggest problems first. An invented answer or a missed safety hand-off matters more than a reply that is a little too long. And run the full test set again, because one fix can break something else.

Think of a driving test. A fair test does not only use an empty car park. It includes busy junctions, bad weather and a sudden stop. An assistant that only passes easy questions is not ready for real customers.

Let's look at an example. Mateo is testing an assistant for a hypothetical chain of fitness centres in Córdoba, Argentina. It covers opening hours, membership types, and how to freeze a membership. He runs twenty questions and scores them in a sheet. Most standard questions score well. But three problems stand out.

First, an invented answer. Asked, can I bring my dog, the assistant said yes, in the outdoor area. There is no such policy. Accuracy, zero. Second, a missed hand-off. A customer wrote: I hurt my back on your machine yesterday, and I want compensation. The assistant explained how to freeze a membership. Hand-off, zero.

Third, the answers in Spanish were shorter, and left out a step about freezing a membership. That is a fairness problem.

Mateo fixes them in order of risk. He adds injury, hurt and compensation, and the Spanish words, to the hand-off triggers. He strengthens the rule: if the answer is not in the knowledge base, do not guess. He adds the full Spanish article. Then he runs all twenty questions again, and records the new scores in a second column.

A common mistake is to write test questions that match your articles word for word. Real customers do not write like help articles. Ask a colleague who did not build the assistant to write some of your questions. Include the messy, emotional and unexpected messages you see in real work, without personal details.

Let's recap. First, a test set of about twenty questions should mix standard, tricky, out-of-scope, emotional, hand-off and non-English questions. Second, score each answer for accuracy, tone and hand-off, and check fairness and privacy. Third, fix the highest-risk problems first, then run the full test set again.

This is capstone step three. In the exercise, you will write twenty made-up test questions, score every answer in a sheet, fix the three biggest problems, and test again. Your capstone is almost complete. In the final lesson, we look at measuring success and keeping the human touch. See you there.
```

## L12 Measuring Success and Keeping the Human Touch

- **Filename:** `ai-26-ai-for-customer-experience-and-support_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (678 words). The quality gate accepts ±10%.

```text
Imagine your new assistant handles almost every conversation without a person. It looks like a great result. But what if many of those customers simply gave up and closed the chat? The numbers you choose decide what you see.

In the last lesson, you tested your assistant before launch. In this final lesson, we look at how to measure it after launch, and how to keep the human touch. Four measures are useful for most support assistants.

First response time is how long a customer waits for the first useful reply. But a fast wrong answer is not a success. Resolution rate is the share of conversations where the problem was actually solved. You can ask, did this answer your question, or check if the customer contacted you again soon.

Hand-off rate is the share of conversations passed to a person. A hand-off is not a failure. The question is whether the right conversations are handed off. And customer satisfaction is a short rating at the end, for both AI-only and handed-off conversations.

This course gives no target numbers. Good values depend on your industry, customers and channels. Compare with your own team's results before launch, and follow the trend. And keep checking the points from lesson eleven: accuracy, tone, fairness across languages, and privacy.

Always read the measures together. The rate of conversations that never reach a person is sometimes called containment. If customers leave without an answer, containment goes up, while satisfaction and resolution go down. Watch for warning signs: chats that end suddenly, repeat contacts by email or phone, and low ratings after AI-only chats.

Privacy and transparency are principles, not extras. Tell customers they are talking to AI, and how to reach a person. Collect only the data you need, follow the data protection rules where your customers live, and ask your legal team before any real launch. And keep real customer data out of free test tools.

Think of a doctor checking a patient. A normal temperature with a very high heart rate still means something is wrong. In the same way, high containment with low satisfaction means customers are not being helped.

Let's see a launch note. Sofie runs support for a hypothetical bicycle rental company in Ghent, Belgium. Customers write in Dutch, French and English. She prepares a one-page note for a two-month pilot.

Her scope is bike availability, prices and opening hours. Everything else goes to a person. Her measures are the four you just saw, compared with the two months before launch. Her warning signs include chats that end after one message, repeat contacts within two days, and any complaint that the assistant was hard to leave.

For quality, a team member reads twenty random conversations each week, in all three languages. The welcome message says it is an AI assistant, and the data protection officer approves what data is collected. She reviews quality weekly, the measures monthly, and after two months decides to continue, change or stop.

After the first month, containment is high, but satisfaction for French conversations is lower. Sofie reads those conversations and finds two French articles are missing. She adds them, and watches the next month's results.

A common mistake is to report only one number, the conversations the assistant handled. That rewards keeping customers away from people. Report containment with resolution and satisfaction, and treat a well-timed hand-off as good service.

Let's recap. First, track response time, resolution, hand-off rate and satisfaction together, compared with your own results. Second, high containment is not always good, because customers who give up also count. Third, tell customers they are talking to AI, make a person easy to reach, and collect only the data you need.

Congratulations, you have finished the course! You designed a working assistant with a real hand-off to a human. For capstone step four, make your final fixes and write your one-page launch note. Then check the rubric checklist and submit your capstone: your assistant, your hand-off flow, your test sheet and your launch note. Well done, and keep the human touch.
```
