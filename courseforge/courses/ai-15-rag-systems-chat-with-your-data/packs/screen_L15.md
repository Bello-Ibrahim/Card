# Screen Demo Pack: AI-15 L15 Capstone Step 1: Build Your RAG Assistant

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L15_screen_1.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Show the folder of 45 guidance PDFs and the CSV with URL and licence columns.
2. Run python ingest.py and show the log ending with 2 scanned files skipped.

**Narration over this clip (for pacing)**

> Let's follow Wanjiru, a developer volunteering for a network of community clinics near Kisumu, Kenya. Clinic staff need quick answers from public health guidance, such as vaccination schedules and referral steps. She collects forty-five public guidance PDFs, records each link and licence, and runs her ingestion script. The log shows two scanned files skipped.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L15_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show config.py with the chosen chunk size and k.
2. Run the collection count and show 2,900 chunks.
3. Print one chunk with its metadata: title, page, year, url, access.

**Narration over this clip (for pacing)**

> After a quick hit at five check, she chooses sentence chunks of about eight hundred characters, with section titles. She stores two thousand nine hundred chunks in Chroma, with metadata that includes the year, so answers prefer current guidance. She checks a few chunks by eye before moving on.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L15_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Scroll through rag.py: hybrid retrieval with RRF, reranker, grounded SYSTEM prompt, structured answer with citations and found, check_citations.
2. Show app.py with st.title, the notice caption and the chat input.
3. Run streamlit run app.py and show the app with the notice at the top.

**Narration over this clip (for pacing)**

> In the answering file, she connects hybrid retrieval, reranking and the grounded prompt, with a structured output for the answer, citations and the found flag. Then she builds the Streamlit app, with a notice at the top: the assistant supports, but does not replace, professional judgement.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L15_screen_4.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Ask a vaccination schedule question and show the answer with title and page source links.
2. Ask a question in Kiswahili and show the cited answer.
3. Ask about a drug not in the guidance and show the exact refusal sentence.

**Narration over this clip (for pacing)**

> She asks five realistic questions, including one in Kiswahili. You'll see something like short answers, each with clickable sources that show the title and page. Then she asks about a drug that is not in the guidance. The reply is exactly: I don't know. The documents do not contain this information.

## Clip 5: scene 11

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L15_screen_5.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open NOTES.md and show two open issues: split dosage tables, overlapping guidance versions.

**Narration over this clip (for pacing)**

> Finally, she writes her open issues in a notes file. Tables in dosage charts are sometimes split, and two guidance versions overlap. These become her first candidates for improvement in step two. Writing issues down now saves time later, because the evaluation will show which one matters most.

## Production notes for this lesson

- [VERIFY] Licence and reuse terms of the public health guidance used in Wanjiru's demo, and of the open-source documentation example. Confirm before recording, or use another collection whose licence is confirmed.
- [VERSION] Streamlit chat API (chat_input, chat_message) and all libraries used in the pipeline; Claude model choice read from config (check the current models page). Never say a model ID or price.
- RESOLVED 2026-09-26: content.md now uses structured output (output_config JSON Schema) instead of a forced tool call.
- Health example: the Streamlit app on screen must show the notice that the assistant supports but does not replace professional judgement.
- The Kiswahili question shown on screen needs a native-speaker check before release.
- Wanjiru and the clinic network near Kisumu are hypothetical; the counts (45 PDFs, 2 skipped, 2,900 chunks) describe her example build. Answers on screen come from a real run and are introduced with 'you'll see something like'. The refusal sentence must match exactly: 'I don't know. The documents do not contain this information.'
- Stock footage of clinic staff must not show a real clinic name, logo or identifiable patients.
