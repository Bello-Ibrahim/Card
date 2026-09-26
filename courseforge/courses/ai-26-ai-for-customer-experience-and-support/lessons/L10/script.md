# L10 Adding the Hand-off Flow | Presenter Script

Course: AI-26 · Video: 5 min · Words: 695

## Hook
In lesson seven, you wrote hand-off rules on paper. Today you connect them to a place where a real person will see them, and you make sure the customer knows exactly what happens next.

## Explain
This is capstone step two. Your assistant from the last lesson answers questions. Now it needs a hand-off flow, and every hand-off flow has four parts: trigger, collect, send and tell.

Trigger means the rules that start the hand-off, such as a request for a person, a very upset customer, a refund above your limit, or a safety issue. Collect means what the assistant asks first. Only what is needed, such as an email address, and permission to share the conversation.

Send means where the summary goes: an email inbox, a help desk ticket, or a team chat channel. Tell means what the customer sees: who will reply, through which channel, and when.

There are two common ways to send the summary. Many chatbot builders have their own hand-off or email notification feature. Or, if the builder can send data out, an automation in n8n or Zapier can email the team or add a row to a sheet, as in lesson eight. Choose the simplest option that works on your plan.

The final message must be honest and specific. Your request has been escalated, is weak. Compare this. I have passed your question to our support team, with a summary of our chat. A person will reply by email within one working day. Only promise times your team can meet.

Think of leaving a message at a hotel reception. A good receptionist writes who called, why and how to reply, puts the note in the right box, and tells the caller when the guest will get it. A note on the wrong desk is no message at all.

## Demonstrate
Let's build it. Wanjiru manages customer service for a hypothetical safari travel company in Nairobi, Kenya. Her assistant answers questions about trip dates, packing and payment, often when the office is closed.

In the chatbot builder, I open the hand-off settings. I add the triggers from lesson seven: person, agent, change my booking, injured and medical. So a request for a person, a booking change, or a safety or medical issue will hand off.

Next, collect. The assistant asks: may I have your email address, so a colleague can reply? I will share a summary of our chat with them. Then I set the summary fields from the template: need, trigger, details, what the assistant said, mood and urgency.

Now, send. The simplest option is the builder's own email notification, going to a test support inbox. If your builder can send data out, you could instead pass the hand-off to Zapier or n8n, to email the team and log it in a hand-offs sheet.

Then, tell. For out of hours, I write: our team is offline now. A person will read your message and reply by email when the office opens. For an emergency during your trip, use the emergency number in your travel documents.

Finally, I test with a made-up conversation, and check the inbox. The summary arrived, but without the customer's email. The assistant handed off before asking. So Wanjiru moves collect before send, and the retest is complete.

A common mistake is to see the confirmation message in the chat and assume it works. The summary may go to an old inbox nobody reads. Always test the full path, until a person sees the summary.

## Recap
Let's recap. First, a hand-off flow has four parts: trigger, collect, send and tell. Second, connect it to a real human channel, with the builder's own feature or an automation, and choose the simplest option. Third, tell customers who will reply, how and when, and test the full path.

## CTA
This is capstone step two. In the exercise, you will fill in the four-part template, add at least four triggers, and connect your hand-off to a test inbox or sheet. Then test three made-up conversations. In the next lesson, we look at testing your assistant for accuracy, tone and safety. See you there.

## Thumbnail
Headline: Hand-off That Really Arrives
Image: Navy background, a chat bubble sending a folded note along a teal path into an inbox where a person is waiting, headline in teal Inter Bold.

## Production Notes
- Screen demo lesson: record scenes 9 to 13 live in Botpress (free plan), continuing the test bot style from L09 but configured as Wanjiru's safari assistant. The screen_steps are content.md's step list adapted to Botpress.
- [VERSION] Botpress hand-off features and names in the screen_steps (the human hand-off or 'HITL' / human-in-the-loop integration, email notification option, trigger settings, 'Emulator' test chat) and whether they are available on the free plan must be checked in the live tool before recording; update the steps if they differ.
- [VERIFY] That Botpress can send hand-off data to Zapier or n8n on a free plan. The demo records Option A (the builder's own email notification) as the main path; Option B (Zapier or n8n webhook to email and a 'Hand-offs' sheet) is only named in the voiceover and shown in scene 11 as an optional insert if it is confirmed. If not confirmed, cut the Option B steps and keep the voiceover as it is.
- [VERSION] n8n and Zapier free-tier limits and triggers for receiving a hand-off.
- Use a test support inbox and made-up test email addresses only; blur real account addresses. The emergency number in the out-of-hours message stays generic ('the emergency number in your travel documents'); do not add a real number.
- 'Within one working day' in the strong customer message is an example; the voiceover tells learners to promise only times their team can meet.
- Wanjiru and the Nairobi safari company are fictional. Pronunciation: Wanjiru (wahn-JEE-roo).
