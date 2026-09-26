# Screen Demo Pack: AI-14 L14 Capstone Step 1: Build the Core Feature

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-14-building-apps-with-llm-apis_L14_screen_1.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Open spec.md in VS Code
2. Scroll through the six headings: User and problem, Input and output, Prompt plan, Tool (optional), Limits, Success
3. Highlight the Limits section: small model placeholder, low max_tokens, spend limit set, no personal data
4. Highlight the Success line: 5 invented test adverts return correct fields

**Narration over this clip (for pacing)**

> Before any code, she writes her one-page spec. The users are recruiters. The input is one advert, and the output is a schema. Her limits are a small model, a low max tokens value and a spend limit, and she excludes any personal data. Success means five test adverts give correct fields.

## Clip 2: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L14_screen_2.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Open schema.py in VS Code
2. Highlight the JobAnalysis Pydantic class
3. Point to the optional salary_min, salary_max and currency fields
4. Point to red_flags with the comment e.g. 'no salary given'

**Narration over this clip (for pacing)**

> Her schema has the job title, the seniority level, a list of required skills, an optional salary range and currency, and a list of red flags, such as no salary given.

## Clip 3: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L14_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open core.py and highlight analyse()
2. Highlight the <advert> tags and output_format=JobAnalysis
3. Highlight the stop_reason check that raises 'Stopped early'
4. Run python core.py adverts/advert_01.txt and show the printed object

**Narration over this clip (for pacing)**

> Her core function sends the advert inside tags with the structured-output helper. It checks the stop reason, and returns a validated object. She tests it in the terminal first, before any page exists.

## Clip 4: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L14_screen_4.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Open app.py and highlight st.json(analysis.model_dump())
2. Highlight st.write_stream() for the comment
3. Run streamlit run app.py, paste an invented advert and show the fields, then the streamed comment

**Narration over this clip (for pacing)**

> Then the page. The Streamlit app shows the structured fields, and then streams a short, plain-language comment built from that object, just like in lesson eight.

## Clip 5: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L14_screen_5.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Paste the Polish advert and show the parsed fields
2. Paste the advert with no salary and show salary_min empty and 'no salary given' in red_flags (example output)
3. Show the spec line: 'Tool (optional): read-only salary table, after core tests pass'

**Narration over this clip (for pacing)**

> She tests five invented adverts, including one in Polish and one with no salary. For that one, you'll see something like an empty salary field, and no salary given in the red flags. A salary lookup tool stays optional. She adds it only after these tests pass, read-only, with the loop limits from lesson ten.

## Production notes for this lesson

- [VERSION] The structured-output helper (messages.parse, output_format, parsed_output) and Streamlit functions (st.json, st.write_stream) must be checked against the current docs before recording.
- The result for the advert with no salary (empty salary_min, 'no salary given' in red_flags) is example output; label it on screen.
- Agnieszka Nowak, the Kraków recruitment agency and all job adverts are invented. The Polish advert should be checked by a Polish speaker for natural wording before recording.
- Scope: retrieval over documents is AI-15 and multi-step agents are AI-16; the voiceover mentions both once.
