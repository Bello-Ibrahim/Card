# Screen Demo Pack: AI-14 L05 Structured Outputs with JSON Schemas

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L05_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open extract.py in VS Code
2. Highlight the Invoice Pydantic class
3. Highlight the system prompt: 'Extract invoice fields. Convert all dates to YYYY-MM-DD. Use the ISO 4217 currency code.'
4. Highlight the user content wrapped in <invoice> tags

**Narration over this clip (for pacing)**

> She opens her extractor. At the top is the Invoice class. The system prompt tells the model to convert all dates to one standard format, and to use standard currency codes. The invoice text goes inside tags, as you learned in lesson three.

## Clip 2: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L05_screen_2.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Highlight client.messages.parse(...) with output_format=Invoice and max_tokens=500
2. Highlight response.parsed_output
3. Run python extract.py invoices/mexico.txt
4. Show the parsed object: supplier 'Papelería del Centro', invoice_date 2026-03-12, total 18450.0, currency MXN (labelled 'example output')

**Narration over this clip (for pacing)**

> The call uses the parse helper, with the Invoice class as the output format. The result is an Invoice object, not a string. She runs it on the Mexican invoice. You'll see something like the supplier name, the date in standard format, the total as a number, and the Mexican peso code.

## Clip 3: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L05_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Show the line that saves the Invoice object to the database
2. Run the extractor on invoices/germany.txt with the total '1.234,50 EUR'
3. Show the result total 1.2345 and circle it in red (example output)

**Narration over this clip (for pacing)**

> She saves the object straight to the database. No string searching, and no regular expressions. Then she tests a German invoice, where the total uses a comma for decimals. The first result is wrong. The schema was valid, but the value was not.

## Clip 4: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L05_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Add to the system prompt: 'Numbers may use a comma as the decimal separator.'
2. Add a business check that prints REVIEW for totals below 5
3. Run the German invoice again and show total 1234.5

**Narration over this clip (for pacing)**

> So she adds a rule to the system prompt about comma decimals, and a business check that flags very small totals for human review. She runs it again, and the total is now correct.

## Production notes for this lesson

- [VERSION] Structured-output parameters (output_config, output_format), the messages.parse() helper and parsed_output must be checked against the current SDK and docs before recording. If names have changed, update the on-screen code; the voiceover describes the feature without naming parameters.
- [VERSION] Confirm that the tool-based alternative (a tool whose input_schema is the schema) is still supported as described.
- The example outputs (the Mexican invoice JSON and the first German result 1.2345) are illustrative: label them 'example output' on screen.
- Priya, the Bengaluru accounting tool and the supplier 'Papelería del Centro' are invented; all invoices on screen are invented text with no real personal data.
