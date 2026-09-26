# Screen Demo Pack: AI-16 L04 Your First Workflow: Sheets In, Sheets Out

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L04_screen_1.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Open Google Sheets in a test account
2. Create a sheet named 'orders' with columns order_id, customer, item, amount, flag
3. Show 15 rows of invented sample orders (no phone numbers)

**Narration over this clip (for pacing)**

> Let's build it. Wanjiru Kamau runs a bakery in Nairobi, Kenya. She wants to phone every customer who orders more than five thousand Kenyan shillings, to confirm before baking. She uses sample data only. First, she creates a sheet called orders, with fifteen invented rows.

## Clip 2: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L04_screen_2.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open Credentials and create a Google Sheets credential following the current n8n OAuth steps (blur client ID and secret)
2. Click to test the connection
3. New workflow: add a Manual Trigger
4. Add a Google Sheets node, operation get rows, select the 'orders' document and sheet
5. Run the node: output shows 15 items

**Narration over this clip (for pacing)**

> In n8n, she creates a Google Sheets credential using the current steps, and tests that it connects. Then she adds a manual trigger, and a Sheets node that gets rows from the orders sheet. When she runs it, the output shows fifteen items.

## Clip 3: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L04_screen_3.mp4`
- **Target length:** about 29 seconds

**Steps**

1. Add a Code node after the Sheets node
2. Paste the JavaScript from content.md (LIMIT = 5000; flag = 'check' or 'ok')
3. Run the node
4. Show the output: flag 'check' on 4 items, 'ok' on the rest

**Narration over this clip (for pacing)**

> Next, she adds a Code node. For a simple rule like this, a few lines of code are short and clear. The code sets a limit of five thousand at the top. Then, for every item, it sets the flag to check if the amount is above the limit, and to ok if not. You'll see something like four items marked check, and the rest marked ok.

## Clip 4: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L04_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Add a second Google Sheets node, operation update row
2. Set 'column to match on' to order_id
3. Map the flag field
4. Run the whole workflow
5. Switch to the sheet: the flag column is filled

**Narration over this clip (for pacing)**

> To write back, she adds a second Sheets node, with the update operation. She sets the column to match on to the order ID, and maps the flag field. She runs the whole workflow, opens the sheet, and the flag column is filled.

## Clip 5: scene 12

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L04_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Point to the row where amount is '6,200' as text and the flag is wrong
2. Edit the Code node to clean the value: Number(String(item.json.amount).replace(/,/g, ''))
3. Run again: that row is now flagged 'check'

**Narration over this clip (for pacing)**

> Then she notices a problem. One amount was typed as text, with a comma, so the comparison failed. She adds a small step to remove the comma and turn it into a number. Real data is always less tidy than you expect.

## Production notes for this lesson

- [VERSION] Google Cloud OAuth client setup, the APIs to enable, and the n8n Google Sheets node operations ('get rows', 'update row', 'column to match on') change often and must be checked before recording.
- [VERSION] n8n node names (Edit Fields (Set), IF, Code) and the Code node's $input.all() syntax must be confirmed for the current release.
- [REGION] Use invented sample data only; storing real customer names or phone numbers in a sheet may be restricted by local data protection law. The demo sheet contains only invented names and no phone numbers.
- Screen recording: use a test Google account. Blur the OAuth client ID and secret. The Code node shows the JavaScript from content.md; the voiceover describes it and does not read it.
- Wanjiru Kamau and her Nairobi bakery are fictional.
