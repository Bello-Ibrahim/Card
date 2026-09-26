# Screen Demo Pack: AI-26 L10 Adding the Hand-off Flow

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L10_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open the test bot in Botpress and go to the human hand-off (HITL) settings
2. Add trigger phrases and topics: 'person', 'agent', 'change my booking', 'injured', 'medical'
3. Show the list of triggers saved

**Narration over this clip (for pacing)**

> In the chatbot builder, I open the hand-off settings. I add the triggers from lesson seven: person, agent, change my booking, injured and medical. So a request for a person, a booking change, or a safety or medical issue will hand off.

## Clip 2: scene 10

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L10_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. In the hand-off step, add the question: 'May I have your email address so a colleague can reply? I will share a summary of our chat with them.'
2. Add the summary fields: Need, Trigger, Details, Assistant said, Mood, Urgency

**Narration over this clip (for pacing)**

> Next, collect. The assistant asks: may I have your email address, so a colleague can reply? I will share a summary of our chat with them. Then I set the summary fields from the template: need, trigger, details, what the assistant said, mood and urgency.

## Clip 3: scene 11

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L10_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Option A (record): choose the builder's email notification and enter the test support inbox address
2. Option B (optional insert, only if confirmed): send the hand-off to a Zapier or n8n automation that emails the team and adds a row to a 'Hand-offs' sheet

**Narration over this clip (for pacing)**

> Now, send. The simplest option is the builder's own email notification, going to a test support inbox. If your builder can send data out, you could instead pass the hand-off to Zapier or n8n, to email the team and log it in a hand-offs sheet.

## Clip 4: scene 12

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L10_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open the out-of-hours message setting
2. Type: 'Our team is offline now. A person will read your message and reply by email when the office opens. For an emergency during your trip, use the emergency number in your travel documents.'

**Narration over this clip (for pacing)**

> Then, tell. For out of hours, I write: our team is offline now. A person will read your message and reply by email when the office opens. For an emergency during your trip, use the emergency number in your travel documents.

## Clip 5: scene 13

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L10_screen_5.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open the 'Emulator' test chat and type a made-up request: 'I want to change my booking, can I talk to a person?'
2. Switch to the test inbox and open the summary; highlight the missing email field in red
3. Back in the builder, move the Collect step before the Send step
4. Retest and show the complete summary in the inbox

**Narration over this clip (for pacing)**

> Finally, I test with a made-up conversation, and check the inbox. The summary arrived, but without the customer's email. The assistant handed off before asking. So Wanjiru moves collect before send, and the retest is complete.

## Production notes for this lesson

- Screen demo lesson: record scenes 9 to 13 live in Botpress (free plan), continuing the test bot style from L09 but configured as Wanjiru's safari assistant. The screen_steps are content.md's step list adapted to Botpress.
- [VERSION] Botpress hand-off features and names in the screen_steps (the human hand-off or 'HITL' / human-in-the-loop integration, email notification option, trigger settings, 'Emulator' test chat) and whether they are available on the free plan must be checked in the live tool before recording; update the steps if they differ.
- [VERIFY] That Botpress can send hand-off data to Zapier or n8n on a free plan. The demo records Option A (the builder's own email notification) as the main path; Option B (Zapier or n8n webhook to email and a 'Hand-offs' sheet) is only named in the voiceover and shown in scene 11 as an optional insert if it is confirmed. If not confirmed, cut the Option B steps and keep the voiceover as it is.
- [VERSION] n8n and Zapier free-tier limits and triggers for receiving a hand-off.
- Use a test support inbox and made-up test email addresses only; blur real account addresses. The emergency number in the out-of-hours message stays generic ('the emergency number in your travel documents'); do not add a real number.
- 'Within one working day' in the strong customer message is an example; the voiceover tells learners to promise only times their team can meet.
- Wanjiru and the Nairobi safari company are fictional. Pronunciation: Wanjiru (wahn-JEE-roo).
