# Screen Demo Pack: AI-16 L06 Structured Output: Getting JSON You Can Trust

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L06_screen_1.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Show the Google Sheet with tabs 'emails' (email_id, text), 'classified' and 'needs_review'
2. Scroll through 10 invented emails in four languages

**Narration over this clip (for pacing)**

> Let's build it. Beatriz Carvalho manages guest services at a hotel in Lisbon, Portugal. Guests write in Portuguese, English, French and Spanish. She wants each email sorted by category, urgency and language, so the right person sees it first. She uses ten invented emails. Her sheet has three tabs: emails, classified, and needs review.

## Clip 2: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L06_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Manual Trigger → Google Sheets (get rows from 'emails')
2. HTTP Request to the Claude Messages endpoint with the JSON-shape system prompt
3. Set max_tokens to a small value

**Narration over this clip (for pacing)**

> In n8n, she builds a manual trigger, a Sheets node that reads the emails, and an HTTP Request to Claude, with the system prompt and a small output limit.

## Clip 3: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L06_screen_3.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Add a Code node and paste the validation script from content.md
2. Run on one email
3. Show output for E07: category complaint, urgency high, language fr, valid true (example output)

**Narration over this clip (for pacing)**

> Next, she adds the validation Code node. For one email, you'll see something like: category complaint, urgency high, language French, and valid set to true.

## Clip 4: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L06_screen_4.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Add an IF node: valid is true
2. True branch: Google Sheets (append to 'classified')
3. False branch: second HTTP Request with the extra line 'Your previous answer was not valid JSON. Return only the JSON.'
4. Second Code check, then Google Sheets (append to 'needs_review' with the original text)

**Narration over this clip (for pacing)**

> She adds an IF node on valid. Valid items go to the classified tab. Invalid items get one retry, with a note that says the last answer was not valid JSON. If the second check fails too, the item goes to needs review, with its original text.

## Clip 5: scene 12

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L06_screen_5.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Run with the email '????': result category 'other', valid true
2. Run with the long three-language email: item lands in 'needs_review'
3. Open both tabs to show where each item ended up

**Narration over this clip (for pacing)**

> Now she tests the edges. An email that says only question marks comes back as category other, which is valid. A very long email that mixes three languages lands in needs review, which is exactly where it should go.

## Production notes for this lesson

- [VERSION] Claude API structured output: the recommended method for JSON output (prompting, tool input schemas or a dedicated structured output option) and the response path content[0].text must be checked against current documentation. The voiceover says only that stronger options exist and learners should check the documentation.
- [VERSION] n8n HTTP Request, Code ($input.all()) and IF node options must be checked against the current release.
- Screen recording: the validation JavaScript and the JSON shape come from content.md and are shown on screen; the voiceover describes them and does not read them. The JSON result for email E07 is an example output.
- Beatriz Carvalho and her Lisbon hotel are fictional; all 10 emails are invented, with no real guest names.
