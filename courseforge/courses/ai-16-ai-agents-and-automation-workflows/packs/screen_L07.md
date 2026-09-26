# Screen Demo Pack: AI-16 L07 Routing and Decisions

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L07_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open the L06 classification workflow (duplicated and renamed)
2. Show the sheet with 20 invented claim messages in English and Filipino

**Narration over this clip (for pacing)**

> Let's build it. Andrea Santos leads customer care at an insurance company in Manila, the Philippines. Claim messages arrive in English and Filipino. She uses twenty invented messages, and starts from the classification workflow from the last lesson.

## Clip 2: scene 9

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L07_screen_2.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Add an IF node before the HTTP Request to Claude
2. Condition 1: text matches the regular expression CL-\d{6}
3. Condition 2: text contains 'status'
4. True branch → 'auto status reply' path; false branch → Claude

**Narration over this clip (for pacing)**

> First, a rule. Before the model call, she adds an IF node. If a message has a claim number in the standard format and the word status, it goes to an automatic status reply. No AI is needed.

## Clip 3: scene 10

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L07_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Update the system prompt: categories claim_new, claim_status, complaint, document_question, not_sure; plus urgency
2. Update the validation Code node with the new allowed values
3. Add a Switch node on category, one output per value, fallback output turned on

**Narration over this clip (for pacing)**

> The other messages go to Claude, with five categories: new claim, claim status, complaint, document question, and not sure, plus an urgency field. Then she adds a Switch node on the category, with one output per value, and a fallback.

## Clip 4: scene 11

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L07_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. complaint + urgency high → Google Sheets append to 'urgent_complaints'
2. document_question → second HTTP Request that drafts a reply → append to 'drafts' (not sent)
3. not_sure and fallback → append to 'review'

**Narration over this clip (for pacing)**

> She connects the outputs. High-urgency complaints go to an urgent complaints tab. Document questions go to a second Claude call that drafts a reply into a drafts tab. Nothing is sent. Not sure items and the fallback both go to review.

## Clip 5: scene 12

- **Filename:** `ai-16-ai-agents-and-automation-workflows_L07_screen_5.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Run the workflow on all 20 messages
2. Open each tab and show the item counts
3. Open 'review' and point to the mixed car accident and cancellation message with category not_sure (example output)

**Narration over this clip (for pacing)**

> She runs all twenty, and checks the count in each tab. One message says: my car was hit, the other driver's insurer says you pay, and I also want to cancel my policy. You'll see something like not sure, so it goes to review. Andrea agrees. It needs a person.

## Production notes for this lesson

- [VERSION] n8n IF and Switch node options (rules mode, fallback output, regular expression conditions) must be checked against the current release.
- Screen recording: the regular expression CL-\d{6} is shown on screen only; the voiceover describes it as 'a claim number in a fixed format'. The not_sure result for the mixed message is an example output.
- Drafted replies are stored in the 'drafts' tab and never sent in this lesson; keep that visible on screen.
- Andrea Santos and her Manila insurance company are fictional; all 20 claim messages are invented.
