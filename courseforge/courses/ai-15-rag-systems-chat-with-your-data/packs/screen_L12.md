# Screen Demo Pack: AI-15 L12 Measuring Answer Quality: Faithfulness and Relevance

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L12_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show the agreement function.
2. Show the judge and human label lists for five answers.
3. Run print(rate, diffs) and show the exact output 0.8 [(1, 'yes', 'partly')].

**Narration over this clip (for pacing)**

> So a judge must be checked. This small function compares the judge's labels with yours. In the example with five answers, agreement is zero point eight, and there is one difference, on the second answer. The judge said yes, and the human said partly. Read every disagreement like this one.

## Clip 2: scene 8

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L12_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run the pipeline over 25 test questions.
2. Open answers.jsonl and show one saved line with question, chunks and answer.

**Narration over this clip (for pacing)**

> Now a real evaluation. Kwame is a developer for an agricultural advice service in Kumasi, Ghana. Extension officers ask about crop guidance. He runs twenty-five test questions, twenty answerable and five unanswerable, and saves the question, chunks and answer for each one to a file.

## Clip 3: scene 9

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L12_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Show JUDGE_RUBRIC and the judge call with a structured verdict.
2. Run it over the 20 answerable answers and save the verdicts.
3. Show his own labels for 10 answers in a separate file, created before opening the verdicts.

**Narration over this clip (for pacing)**

> For the twenty answerable ones, he calls the judge with his rubric, and saves the verdicts. You'll see something like a list of verdicts, each with a faithfulness label and any unsupported claims. Before he opens that file, he labels ten answers himself.

## Clip 4: scene 10

- **Filename:** `ai-15-rag-systems-chat-with-your-data_L12_screen_4.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run agreement and show 8 of 10 with two disagreements.
2. Open one disagreement and highlight the planting month missing from the chunks.
3. Edit the rubric to 'list every claim first, then check each claim', re-judge, and show 9 of 10.

**Narration over this clip (for pacing)**

> Agreement is eight of ten. In both differences, the judge said yes, but the answer added a planting month that was not in the chunks. He changes the rubric: list every claim first, then check each one. He judges again, and agreement rises to nine of ten.

## Production notes for this lesson

- [VERSION] Claude API batch processing option (interface, discount and delivery time), structured output for the judge, and model choice (check the current models page). The voiceover mentions batch processing for larger runs but states no price, discount or delivery time.
- RESOLVED 2026-09-26: content.md now uses structured output (output_config JSON Schema) instead of a forced tool call.
- [VERSION] Optional open-source RAG evaluation libraries and their metric definitions; none is named in the voiceover.
- The agreement function is tested plain Python: the screen must show exactly 0.8 [(1, 'yes', 'partly')].
- Kwame's results (8 then 9 of 10 agreement; 16 faithful, 3 partly, 1 no; 4 of 5 correct refusals) are hypothetical; the voiceover calls them example results. Judge verdicts on screen come from a real run.
- Kwame and the Kumasi agricultural advice service are hypothetical.
