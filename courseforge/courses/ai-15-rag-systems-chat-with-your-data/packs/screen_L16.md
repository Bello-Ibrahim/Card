# Screen Demo Pack: AI-15 L16 Capstone Step 2: Evaluate, Improve and Report

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L16_screen_1.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Show the frozen test set file and its version tag.
2. Run the baseline evaluation and log it with log_run as v1.
3. Show the v1 line: hit@5 0.70, MRR 0.52, faithfulness 0.80, refusals 4 of 6.

**Narration over this clip (for pacing)**

> Let's follow Camila in Belo Horizonte, Brazil. She builds an assistant over a web framework's English documentation, for Brazilian developers who ask in Portuguese. Here are her example results. Her baseline, version one, has a hit rate at five of zero point seven zero, an MRR of zero point five two, faithfulness of zero point eight zero, and four of six correct refusals.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L16_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Show the classified failures: mostly function names, two Portuguese technical-term questions.
2. Switch retrieval to hybrid with RRF, re-run, and log v2.
3. Show hit@5 0.83 with faithfulness unchanged.

**Narration over this clip (for pacing)**

> Her diagnosis: most failures are code names, such as function names, plus two Portuguese questions with technical terms. So change one is hybrid search with rank fusion. The hit rate rises to zero point eight three, and faithfulness stays the same. Hybrid search targets exactly that cause.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L16_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Show the prompt change: 'reply exactly' refusal sentence and claim-by-claim citations.
2. Re-run and log v3.
3. Show refusals 6 of 6 and faithfulness 0.90.

**Narration over this clip (for pacing)**

> Change two is a stricter prompt, with reply exactly for refusals, and a citation for every claim. Correct refusals rise to six of six, and faithfulness to zero point nine zero. Every I don't know is now a real, correct answer.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L16_screen_4.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Show the rejected reranker run in the log with higher latency and no hit@5 gain.
2. Run compare('runs.jsonl') and show one line per version with hit@5, faithfulness and cost.
3. Show the deployed v3 answering a Portuguese question with sources.

**Narration over this clip (for pacing)**

> She also tried a reranker. It added time, with no gain on her test set, so she removed it, and she reports that too. Then she prints all runs side by side from her results file, deploys version three, and writes her report. Her report has one results table and five real failure examples.

## Production notes for this lesson

- [VERIFY] Licence of the example open-source documentation used in Camila's demo.
- [VERSION] Free hosting plans and their limits (no provider named in the voiceover); Claude model choice and prices for estimating cost per query, read from config. Never say a model ID or price.
- Camila's results (v1 hit@5 0.70, MRR 0.52, faithfulness 0.80, refusals 4 of 6; v2 hit@5 0.83; v3 refusals 6 of 6, faithfulness 0.90) are hypothetical; the voiceover calls them example results and the results slide carries a 'hypothetical results' label. The compare() output on screen must be generated from a runs file containing these example values.
- Portuguese questions shown on screen should be checked by a Portuguese speaker before release.
- Camila in Belo Horizonte is hypothetical; do not name or show the logo of a real web framework unless its documentation licence has been confirmed.
