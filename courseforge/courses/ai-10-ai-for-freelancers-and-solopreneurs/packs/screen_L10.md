# Screen Demo Pack: AI-10 L10 Your First Automation with Zapier or n8n

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_L10_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Sign in to Zapier and click to create a new automation (a 'Zap').
2. In the trigger step, search for and select the form app.
3. Choose the event 'new form response' and connect the form account (blur the account email).

**Narration over this clip (for pacing)**

> He signs in to Zapier and creates a new automation. For the trigger, he chooses his form app and the event for a new form response, then connects his account.

## Clip 2: scene 10

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_L10_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. In a second tab, open the form and submit: name 'Test Client One', own email address, project type 'Wedding video'.
2. Back in Zapier, click to test the trigger.
3. Show the test entry's fields appearing in the trigger result.

**Narration over this clip (for pacing)**

> He submits a test entry in his form, called Test Client One, with his own email address. Then he tests the trigger, and checks that the test entry appears.

## Clip 3: scene 11

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_L10_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Add an action step, select the spreadsheet app and the event 'create row'.
2. Choose the spreadsheet and worksheet.
3. Map the Name, Email and Project type columns to the matching form fields.
4. Test the action, then open the spreadsheet and highlight the new 'Test Client One' row.

**Narration over this clip (for pacing)**

> Now the first action. He chooses his spreadsheet app and the event to create a row. He picks his spreadsheet and matches each column to a form field. He tests it, and opens the spreadsheet to see the new row.

## Clip 4: scene 12

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_L10_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Add a second action step, select the email app and the event 'send email'.
2. Put the form's Email field in 'To'.
3. Paste the welcome text and insert the Name field after 'Dear'.
4. Test the action and open the test inbox to show the welcome email.

**Narration over this clip (for pacing)**

> Then the second action. He chooses his email app, puts the form's email field in the To box, and inserts the name field into his welcome text. He tests it, and checks his own inbox.

## Clip 5: scene 13

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_L10_screen_5.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Turn the automation on.
2. Submit 'Test Client Two' with a long name and an accented character; check the spreadsheet and inbox.
3. Submit a third entry with the name left blank; show the email reading 'Dear ,'.
4. Open the form settings and mark the Name field as required.

**Narration over this clip (for pacing)**

> He turns the automation on, and submits two more test entries. On the third test, the email says Dear, with no name, because he left the name field empty. So he makes the name field required in his form.

## Clip 6: scene 14

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_L10_screen_6.mp4`
- **Target length:** about 18 seconds

**Steps**

1. In n8n, create a new workflow.
2. Add a trigger node for the form, or a webhook.
3. Add a spreadsheet node and an email node, connected in a line.
4. Run the workflow with example data and click each node to inspect its output.

**Narration over this clip (for pacing)**

> If you choose n8n, the idea is the same. You create a new workflow with a trigger for your form, then a spreadsheet step and an email step in a line. You run it with example data, and inspect each step's output.

## Production notes for this lesson

- [VERSION] Zapier and n8n interfaces, menu names ('Zap', 'workflow', 'node', 'test', 'execute'), trigger and action names, and app connections must be checked against the live tools before the screen demo is recorded. Adjust screen_steps wording to match the live interface; keep the voiceover general.
- [VERSION] Free-tier task limits, steps per automation and available apps for Zapier and n8n change often. The voiceover makes no claim about limits or prices and tells learners to check current plans.
- [VERIFY] Whether a two-action (multi-step) automation is available on Zapier's free tier must be confirmed before recording. If it is not, record the demo in n8n with the same three nodes, or reduce the Zapier demo to one action and re-record scenes 12 and 13.
- [VERIFY] Whether n8n can be used free only by self-hosting, and whether its online version offers a free tier or a trial, must be confirmed. The voiceover deliberately does not state this; the lesson page carries the flagged text.
- Screen recording data: use only 'Test Client One', 'Test Client Two' and 'Test Client Three' with an email inbox owned by the production team. Blur account emails and any connected-account names. Use generic form, spreadsheet and email apps as available in the tool.
- Sipho is fictional.
