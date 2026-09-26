# Screen Demo Pack: AI-26 L08 Automating Simple Tasks with n8n or Zapier

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L08_screen_1.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open Google Forms and create a form titled 'Contact us (test)'
2. Add three fields: Name, Email, Message
3. Submit two made-up test responses
4. Open Google Sheets and create a sheet called 'Support log'
5. Type column headers in row 1: Date, Email, Message, Label

**Narration over this clip (for pacing)**

> First, the test data. I create a form called contact us test, with name, email and message. I submit two made-up responses. Then I create a sheet called support log, with four columns: date, email, message and label.

## Clip 2: scene 9

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L08_screen_2.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Log in to Zapier and click 'Create', then 'Zap' (or the current button for a new automation)
2. Choose trigger app 'Google Forms' and event 'New Form Response'
3. Connect the test Google account and select the 'Contact us (test)' form
4. Click 'Test trigger' and show the sample response loading

**Narration over this clip (for pacing)**

> Now I log in to Zapier and create a new automation. For the trigger, I choose Google Forms, and the event new form response. I connect my test account, choose the form, and test the trigger. A sample response loads.

## Clip 3: scene 10

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L08_screen_3.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Add a second step and choose the built-in AI option (for example 'AI by Zapier')
2. Type the instruction: 'Read the message. Reply with exactly one label from this list: Order, Product question, Return, Other. If unsure, reply Other.'
3. Map the Message field from step 1 into the input
4. Click 'Test step' and zoom in on the output: a single label

**Narration over this clip (for pacing)**

> Next, the AI step. I add the built-in AI option and write the instruction. Read the message. Reply with exactly one label from this list: order, product question, return, other. If unsure, reply other. I map the message field into the input, and test. The output is one label only.

## Clip 4: scene 11

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L08_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Add a third step: app 'Google Sheets', event 'Create Spreadsheet Row'
2. Select the 'Support log' sheet
3. Map Date, Email, Message and the AI label to the four columns
4. Click 'Test step', then switch to the sheet and highlight the new row

**Narration over this clip (for pacing)**

> Then the action. I choose Google Sheets and the event create spreadsheet row. I pick the support log sheet and map the date, email, message and AI label to the columns. I test the step, open the sheet, and there is the new row.

## Clip 5: scene 12

- **Filename:** `ai-26-ai-for-customer-experience-and-support_L08_screen_5.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Turn the automation on (publish it)
2. Submit a new made-up form response
3. Refresh the 'Support log' sheet and show the new labelled row
4. Optional: show a still of the same three-node flow on the n8n canvas (only if node names are confirmed)

**Narration over this clip (for pacing)**

> Finally, I turn the automation on, submit a new test message, and check the sheet again. In n8n cloud, the same flow uses a form trigger, an AI node and a Google Sheets node.

## Production notes for this lesson

- Screen demo lesson: record scenes 8 to 12 live in Zapier, following content.md's step list. Button and menu names in the screen_steps ('Create' then 'Zap', 'Test trigger', 'Test step', 'AI by Zapier', 'Create Spreadsheet Row', 'Publish') are [VERSION]: check them in the live tool on the recording day and update the steps if they differ.
- [VERIFY] That Zapier's free plan currently allows a three-step automation with a built-in AI step (for example 'AI by Zapier'), and whether n8n cloud offers a free trial that includes AI nodes without a separate paid AI account. The voiceover does not claim either; it tells learners to check the current plan.
- [VERSION] [VERIFY] n8n cloud equivalent (Form Trigger, AI node, Google Sheets append row) is only mentioned in the voiceover; show a still of the n8n canvas in scene 12 only if the node names are confirmed.
- [VERSION] Whether AI steps need a separate AI provider account or key, and any cost.
- Use a fresh test Google account with only the 'Contact us (test)' form and 'Support log' sheet. All form responses are made up; blur the email address of the test account. Never connect a real customer inbox.
- Aroha and the Wellington outdoor shop are fictional. Pronunciation: Aroha (ah-ROH-hah).
- Judgement call carried from curriculum: no coding and no self-hosting of n8n.
