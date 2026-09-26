# Screen Demo Pack: AI-28 L07 Building with No-Code Tools

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-28-building-an-ai-startup_L07_screen_1.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Open Claude in the browser and start a new chat.
2. Type: 'Help me write instructions for an AI step that turns a plumber's short job notes into a clear, polite price quote. Use only the prices the plumber enters. Never invent prices. If information is missing, list what is missing.'
3. Highlight the two rules in the reply: only entered prices; list what is missing.
4. Copy the reply into a blank document and title it 'Prompt v1'.

**Narration over this clip (for pacing)**

> First, we draft the prompt with Claude. We ask for instructions that turn a plumber's short notes into a polite quote. Two rules matter most. Use only the prices the plumber enters, and never invent prices. If something is missing, list what is missing.

## Clip 2: scene 8

- **Filename:** `ai-28-building-an-ai-startup_L07_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open Glide and sign in with a free account.
2. Click New app and choose to start from a blank Glide Table [VERSION].
3. Name the app 'Quick Quotes'.

**Narration over this clip (for pacing)**

> Next, in Glide, the builder we use here, we create a new blank app. Any no-code builder with a table, a form and an AI step will work. The buttons may simply have different names.

## Clip 3: scene 9

- **Filename:** `ai-28-building-an-ai-startup_L07_screen_3.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Open the Data editor and rename the table 'Quotes'.
2. Add columns: Job description, Materials and prices, Labour hours, Hourly rate, Quote text, Status.
3. Set Labour hours and Hourly rate to number columns.

**Narration over this clip (for pacing)**

> We add a table called Quotes. It has fields for the job description, materials and prices, labour hours, hourly rate, the quote text, and a status.

## Clip 4: scene 10

- **Filename:** `ai-28-building-an-ai-startup_L07_screen_4.mp4`
- **Target length:** about 11 seconds

**Steps**

1. In the Layout editor, add a Form (or Form button) linked to the Quotes table [VERSION].
2. Add fields for Job description, Materials and prices, Labour hours and Hourly rate.
3. Toggle Required on for all four fields.

**Narration over this clip (for pacing)**

> Then we add a form linked to the table, with the first four fields. All four are required, so a plumber cannot send an empty request.

## Clip 5: scene 11

- **Filename:** `ai-28-building-an-ai-startup_L07_screen_5.mp4`
- **Target length:** about 20 seconds

**Steps**

1. In the Quotes table, add a new AI column that generates text (for example 'Generate text') [VERSION].
2. Paste Prompt v1 as the instructions.
3. Insert the four form fields into the prompt as inputs, for example 'Job notes: {Job description}'.
4. Map the AI result to Quote text, and set Status to 'draft' when the form is submitted (via an Action or default value) [VERSION].

**Narration over this clip (for pacing)**

> Now the AI step. We add an AI column that generates text from each new row. We paste Prompt version one and insert the form fields where the builder allows. The answer is saved into the quote text field, and the status is set to draft.

## Clip 6: scene 12

- **Filename:** `ai-28-building-an-ai-startup_L07_screen_6.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Add a Details screen for a Quotes row that shows Quote text and Status.
2. Add a button with a Copy to clipboard action for Quote text [VERSION].
3. Open Preview to show the whole flow: form, submit, quote.

**Narration over this clip (for pacing)**

> Next, an output page shows the quote text, with a button to copy it. The core flow now runs from start to finish. It looks plain, and that is fine.

## Clip 7: scene 13

- **Filename:** `ai-28-building-an-ai-startup_L07_screen_7.mp4`
- **Target length:** about 14 seconds

**Steps**

1. In Preview, fill the form: 'Replace kitchen tap'; materials 'tap 450'; labour hours 1; hourly rate 350.
2. Submit and open the new quote.
3. Zoom in on the prices in the quote and compare them with the inputs.

**Narration over this clip (for pacing)**

> Time to test, with fake data only. Replace kitchen tap, tap four hundred and fifty, labour one hour at three hundred and fifty. We check that the quote uses only these numbers.

## Clip 8: scene 14

- **Filename:** `ai-28-building-an-ai-startup_L07_screen_8.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Highlight the invented 'call-out fee' line in the quote.
2. Open the AI column settings and add: 'Do not add any fee that is not listed.'
3. Save the new text in the prompt document as 'Prompt v2'.
4. Submit the same test again and show the quote now has only the tap and labour.

**Narration over this clip (for pacing)**

> And here is a problem. The AI added a call out fee that Sipho never entered. So we add a rule to the prompt: do not add any fee that is not listed. We save it as Prompt version two and test again.

## Clip 9: scene 15

- **Filename:** `ai-28-building-an-ai-startup_L07_screen_9.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Remove the hourly rate from the prompt input for one test row and run it.
2. Show the output listing 'Hourly rate is missing' instead of a made-up number.
3. Click Share or Publish and copy the preview link [VERSION].

**Narration over this clip (for pacing)**

> We also test a missing field. Without the hourly rate, the quote should ask for it, not invent it. Finally, we share the preview link with one test user and watch them finish the task without help.

## Production notes for this lesson

- Screen demo tool: Glide (free plan), per DECISIONS.md. content.md says 'a no-code builder of your choice'; the voiceover keeps that wording and names Glide only as the tool shown. Backup if Glide's free plan cannot run the AI step: Lovable (free credits), or the manual Wizard of Oz route described in scene 16.
- [VERSION] All Glide steps are adapted from content.md's generic steps 2 to 10 and must be checked against the live tool on the day of recording: the names 'New app', 'Glide Table', 'Data editor', 'Form' component, AI or 'Generate text' column, 'Actions', 'Preview' and 'Share' may differ or move.
- [VERSION] Check whether Glide's free plan includes its AI features (DECISIONS.md: VERIFY), and whether connecting Claude instead needs a paid API key. Never show a real API key on screen; blur it if one appears.
- [VERSION] Claude free-plan limits and data-use terms should be checked before recording.
- Test data is fake only (kitchen tap 450, labour 1 hour at 350). No real customer names or addresses on screen. Prices are placeholders in no named currency.
- Sipho (Durban, South Africa) is fictional. Record the screen at 1080p, zoom to 150% on the prompt and AI-column settings so text is readable.
