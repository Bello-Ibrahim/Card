# Screen Demo Pack: AI-15 L10 Building a RAG Test Set

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L10_screen_1.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Show the drafting cell: loop over 25 selected chunks, one API call per chunk asking for 2 questions with answer and evidence.
2. Open drafts.jsonl and show that it holds 50 drafts.

**Narration over this clip (for pacing)**

> Let's follow Thandiwe. She runs a research library service at a university in Cape Town, South Africa. Her assistant covers sixty public policy reports in English, and a few summaries in isiZulu and Afrikaans. She gives the model one chunk at a time, and asks it to draft two questions, a short answer and an evidence phrase for each.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L10_screen_2.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Open the drafts in a spreadsheet.
2. Highlight a draft that copies a sentence from its chunk and delete it.
3. Rewrite a draft into a student's words: 'what did that report say about youth jobs?'

**Narration over this clip (for pacing)**

> You'll see something like fifty drafts. Many copy the chunk's exact words, which makes retrieval look better than it is. So she reviews every one in a spreadsheet. She deletes fourteen that simply repeat a sentence, and rewrites ten to sound like students, like: what did that report say about youth jobs?

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L10_screen_3.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Add six rows with answerable set to false and no source.
2. Add four rows with language 'zu' and 'af', marked 'checked by colleague'.

**Narration over this clip (for pacing)**

> Then she writes six unanswerable questions herself, on topics close to the collection but not in it. She adds four questions in isiZulu and Afrikaans, checked by colleagues who speak those languages. A machine check does not replace a native speaker. These questions show whether the multilingual model really works for her users.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L10_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Show the check_testset function: duplicate id check, source and evidence check, Counter of types and languages.
2. Run check_testset('testset.jsonl') and show: 40 items, unanswerable: 6, four types, three languages.

**Narration over this clip (for pacing)**

> Before using the file, she validates it with a short script. It checks for duplicate IDs, makes sure every answerable item has a source and evidence, and counts the mix. The result: forty items, six unanswerable, four types and three languages.

## Clip 5: scene 11

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L10_screen_5.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Commit testset.jsonl and tag it v1 in the terminal.
2. Show a short team note: 'Freeze the test set before comparing.'

**Narration over this clip (for pacing)**

> Finally, she saves the file in version control, and agrees a rule with her team. Nobody tunes the system and edits the test set at the same time. Otherwise, the before and after scores are measured on different questions, and the comparison means nothing.

## Production notes for this lesson

- [VERSION] Claude API use for drafting candidate questions (model choice read from the environment; check the current models page). Never say a model ID or price.
- Drafted questions shown on screen come from a real API run; the voiceover says 'you'll see something like'.
- Thandiwe's check_testset summary must match content.md: 40 items, 6 unanswerable (34 answerable), 4 types, 3 languages. Prepare testset.jsonl so that the real run prints exactly these counts.
- The isiZulu and Afrikaans questions shown on screen need a native-speaker check before release (course-wide human review item).
- Thandiwe and the Cape Town university library service are hypothetical; the 60 policy reports must be public documents. Do not show personal data.
