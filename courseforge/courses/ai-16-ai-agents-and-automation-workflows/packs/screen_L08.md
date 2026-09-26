# Screen Demo Pack: AI-16 L08 Batches, Loops and Rate Limits

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L08_screen_1.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Run the classification workflow on 20 rows
2. Open the HTTP Request output and point to usage.input_tokens and usage.output_tokens
3. Show the averages in a sheet: about 400 input and 40 output tokens per row (example output)

**Narration over this clip (for pacing)**

> Let's see it. Omar Haddad runs data operations for an online electronics shop in Amman, Jordan. He must classify five hundred product reviews. He does not start with five hundred. He runs twenty rows, and reads the usage fields. You'll see something like four hundred input tokens and forty output tokens per row.

## Clip 2: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L08_screen_2.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Add Loop Over Items after Google Sheets (get rows), batch size 10
2. Inside the loop: HTTP Request to Claude → Settings → Retry On Fail on, a few tries with a wait
3. Validation Code node → Google Sheets update
4. Wait node, a few seconds → connect back to Loop Over Items

**Narration over this clip (for pacing)**

> Now he adds a Loop Over Items node, with a batch size of ten, after the Sheets read node. Inside the loop, the call to Claude has retry on fail turned on. Then come the validation node, the sheet update, and a Wait node of a few seconds, connected back to the loop.

## Clip 3: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L08_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Add a 'processed' column to the sheet
2. Filter the Google Sheets read to rows where processed is empty
3. Set processed to 'yes' in the update node
4. Run 50 rows and show the start and end time in the Executions list

**Narration over this clip (for pacing)**

> He adds a processed column, and filters on it at the start, so only unprocessed rows are read. Then he runs fifty rows, notes the run time, and multiplies by ten to estimate the time for all five hundred.

## Production notes for this lesson

- [VERSION] Claude API rate limits depend on the account and change over time; the lesson states no specific limits. The voiceover says only that the API 'returns an error'; confirm the rate-limit status code (429) and where limits are shown in the Claude Console before it appears on any slide.
- [VERSION] No prices are named in the voiceover or on screen; learners look up the current price list. The token figures in the worked example (about 400 input and 40 output tokens per row) are invented example output and are introduced with 'you'll see something like'.
- [VERSION] n8n Loop Over Items (Split in Batches), HTTP Request batching, Wait node and Retry On Fail settings must be checked against the current release.
- Screen recording: when Omar looks up the price, show the pricing page only briefly and blurred, or cut to the calculation; no figures on screen.
- Omar Haddad and his Amman electronics shop are fictional; the 500 reviews are invented.
