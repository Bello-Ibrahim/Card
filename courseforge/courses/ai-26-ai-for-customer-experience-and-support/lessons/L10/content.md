# L10 Adding the Hand-off Flow

Course: AI-26 · Module: M3 · Objectives: O4, O6 · Video: 5 min (screen demo)

## Hook
In L07 you wrote hand-off rules on paper. A rule on paper does not help a customer at 11 at night. Today you connect those rules to a real place where a person will see them, and you make sure the customer knows exactly what happens next.

## Explanation
A hand-off flow has four parts. You can use this **flow template** for your capstone:

| Part | Question | Your answer |
|---|---|---|
| 1. Trigger | Which rules start the hand-off? | For example: asks for a person, very upset, refund above your limit, legal or safety issue, sensitive topic, question fails twice. |
| 2. Collect | What does the assistant ask before handing off? | Only what is needed, such as a contact email and order number. Ask for permission to share the conversation. |
| 3. Send | Where does the summary go? | An email inbox, a ticket in a help desk, or a message in a team chat channel. |
| 4. Tell | What does the customer see? | Who will reply, through which channel, and when. |

**Sending the summary.** There are two common ways to connect the hand-off to a human channel:

- **The builder's own feature.** Many chatbot builders have a "human hand-off", "live chat", "escalation" or "email notification" feature [VERSION]. It may send an email to your team or open a live chat for an agent.
- **An automation.** If the builder can send data to another tool (often through a "webhook" or a built-in connection), you can use n8n or Zapier, as in L08. Trigger: hand-off event from the builder. Action: send an email, create a ticket or add a row to a sheet [VERSION] [VERIFY].

Choose the simplest option that works on your free plan.

**Telling the customer.** The final message must be honest and specific. Compare:

- Weak: "Your request has been escalated."
- Strong: "I have passed your question to our support team, with a summary of our chat. A person will reply by email within one working day. If it is urgent, you can call us during opening hours."

Only promise times your team can really meet. Outside working hours, say so clearly.

**Analogy:** A hand-off flow is like leaving a message with a hotel reception for a guest. A good receptionist writes down who called, what it is about and how to reply, puts the note in the right box, and tells the caller when the guest will get it. A note with no name, left on the wrong desk, is the same as no message at all.

## Worked Example
Wanjiru manages customer service for a hypothetical safari travel company in Nairobi, Kenya. Customers write from many time zones, often when the office is closed. Her assistant answers questions about trip dates, what to pack and payment options.

Her hand-off rule: if a customer asks for a person, wants to change a booked trip, or mentions a safety or medical issue, the assistant hands off. Outside office hours, no person is online.

The presenter follows these steps on screen. Names depend on the builder and automation tool chosen [VERSION].

1. In the chatbot builder, open the hand-off or escalation settings for the test assistant.
2. Add the trigger phrases and topics from the L07 rules: "person", "agent", "change my booking", "injured", "medical".
3. Set the assistant to ask: "May I have your email address so a colleague can reply? I will share a summary of our chat with them."
4. Choose where the hand-off goes. Option A: the builder's email notification, sent to a test support inbox. Option B: send the hand-off to a Zapier or n8n automation that emails the team and adds a row to a "Hand-offs" sheet.
5. Set the summary fields from the L07 template: need, trigger, details, what the assistant said, mood, urgency.
6. Write the out-of-hours message: "Our team is offline now. A person will read your message and reply by email when the office opens. For an emergency during your trip, use the emergency number in your travel documents."
7. Test the flow in the preview with a made-up conversation and a test email address.
8. Open the test inbox or sheet and check that the summary arrived and is complete.

In the test, the summary arrives but the customer's email field is empty. Wanjiru finds that the assistant handed off before asking for the email. She moves the "Collect" step before "Send" and tests again.

## Common Mistake
Many teams build the hand-off, see the confirmation message in the chat, and assume it works. The customer sees "A person will reply soon", but the email goes to an old inbox nobody reads. Always test the full path, from the customer's message to the moment a person sees the summary, and test again after any change.

## Key Takeaways
1. A hand-off flow has four parts: trigger, collect, send and tell.
2. Connect the hand-off to a real human channel, using the builder's own feature or an automation tool, and choose the simplest option that works.
3. Tell customers who will reply, how and when, and test the full path until a person sees the summary.

## Hands-on Exercise
**Task:** Capstone step 2: add a hand-off flow that sends the conversation summary to a human channel, using the builder's own feature or n8n or Zapier.
**Tools:** Your assistant from L09; the chatbot builder's hand-off feature, or Zapier (free plan) or n8n (cloud trial) [VERSION]; a test email inbox or Google Sheet.
**Steps:**
1. Fill in the four-part flow template (trigger, collect, send, tell) for your assistant.
2. Add at least 4 triggers from your L07 rules, including "customer asks for a person" and "refund above a limit" or "legal or safety issue".
3. Set up what the assistant collects before handing off, and ask permission to share the chat.
4. Connect the hand-off to a test inbox, ticket or sheet using the builder or an automation.
5. Write the customer message for working hours and for out-of-hours.
6. Test 3 made-up conversations that each start a different trigger. Use only test email addresses.
7. Check that each summary arrives and that an agent could act on it without reading the full chat.
**What good looks like:** A completed flow template, a working hand-off that delivers a complete summary to a human channel for all 3 test conversations, and clear customer messages that say what happens next. Screenshots of the settings and a received summary are saved.
**Time:** about 45 minutes

## Review Flags
- [VERSION] The chosen chatbot builder's hand-off, live chat, email notification and webhook features, and whether they are available on the free plan, must be checked before recording.
- [VERSION] n8n and Zapier free-tier limits, triggers and interfaces for receiving a hand-off from a chatbot builder.
- [VERIFY] That the chosen builder can send hand-off data to Zapier or n8n on a free plan; if not, the demo should use only Option A.
- Judgement call (from curriculum): tests use made-up conversations and test email addresses only.
