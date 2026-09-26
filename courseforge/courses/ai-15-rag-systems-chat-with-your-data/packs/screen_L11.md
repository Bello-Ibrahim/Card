# Screen Demo Pack: AI-15 L11 Measuring Retrieval Quality

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 6

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L11_screen_1.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Show the retrieval_metrics function.
2. Show the three example runs.
3. Run the print line with k=3 and show the exact output {'hit@k': 0.667, 'recall@k': 0.5, 'mrr': 0.444}.

**Narration over this clip (for pacing)**

> Here is the metrics function in plain Python. We test it on three questions. The first finds its chunk at rank one. The second finds one of its two relevant chunks, at rank three. The third finds nothing. The result: hit rate zero point six six seven, recall zero point five, and MRR zero point four four four.

## Clip 2: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L11_screen_2.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Show the two pipeline versions: A vector only, B hybrid with RRF, both with 800-character chunks.
2. Run both over the test set and save runs_A.json and runs_B.json with the top 10 IDs per question.

**Narration over this clip (for pacing)**

> Now a real comparison. Hana is an engineer at an insurance company in Prague, Czech Republic. Her assistant answers questions about claims procedures. Version A uses vector search only. Version B uses the same chunks, with hybrid search. She runs both over thirty-two answerable test questions, and saves the top ten IDs for each.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L11_screen_3.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Print the five failed questions from version B.
2. For each, show the retrieved chunks next to the relevant chunk.
3. Fill a small table: chunking ×2 (split table), embeddings ×1 (Czech legal term), vague question ×1 ('what about the form?'), parsing ×1 (scanned appendix).

**Narration over this clip (for pacing)**

> But numbers do not say why. So she lists the five questions that B still fails, and opens the retrieved chunks and the relevant chunk for each one. Two are chunking problems, where a table was split. One is embeddings, with a Czech legal term. One is a vague question. One is parsing, a scanned appendix.

## Production notes for this lesson

- Content.md Review Flags: None. The metrics code is plain Python and was tested: the screen must show exactly {'hit@k': 0.667, 'recall@k': 0.5, 'mrr': 0.444}.
- Hana's results (A: hit@5 0.72, MRR 0.51; B: hit@5 0.84, MRR 0.63) and her five classified failures are hypothetical; the voiceover calls them example results and the slide carries a 'hypothetical results' label.
- This lesson makes no API calls; no model names or costs appear.
- Hana and the Prague insurance company are hypothetical; the Czech legal term shown on screen should be an invented or generic example.
