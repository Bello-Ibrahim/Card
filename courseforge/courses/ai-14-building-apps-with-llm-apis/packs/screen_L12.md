# Screen Demo Pack: AI-14 L12 Testing Prompts with a Small Evaluation Set

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L12_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open evals/cases.json in VS Code
2. Highlight case se-07 with its file path and expected currency SEK, total 12500.0 and invoice_date 2026-02-28

**Narration over this clip (for pacing)**

> Here is one case in his cases file. It has an ID, the invoice file, and the expected currency, total and date. His set mixes normal Swedish invoices, hard formats from other countries, and a few bad inputs.

## Clip 2: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L12_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Open run_eval.py
2. Highlight the loop over cases and the call extract(text, prompt_version)
3. Highlight the all(...) check that compares each expected field
4. Highlight cost += call_cost and the FAIL print
5. Highlight the final summary print

**Narration over this clip (for pacing)**

> His runner loads every case and calls the extractor with a chosen prompt version. It checks that each expected field matches, adds up the cost from his logger, and prints any failing case. At the end, it prints the pass rate and total cost.

## Clip 3: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L12_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run python run_eval.py v1 and show 'v1: 18/20 passed' with FAIL se-07 and FAIL de-03
2. Run python run_eval.py v2 and show 'v2: 19/20 passed' with FAIL mx-02
3. Circle mx-02 in red and add the label 'regression' (example output)

**Narration over this clip (for pacing)**

> He runs version one and version two. You'll see something like this. Version one passes eighteen of twenty. Version two passes nineteen. It looks better. But look closer. Version two fixed two cases, and broke one that passed before, a Mexican invoice. That is a regression.

## Clip 4: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L12_screen_4.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open prompts/extract_v2.txt and highlight the decimal-comma rule
2. Save an edited copy as prompts/extract_v3.txt
3. Run python run_eval.py v3 and show no regressions against v1 (example output)

**Narration over this clip (for pacing)**

> So Johan does not ship version two. He finds that his new rule about decimal commas confused Mexican number formats. He fixes the rule in version three, and ships only when it passes every case that version one passed.

## Production notes for this lesson

- content.md Review Flags: none. All cases are invented and all outputs are example output.
- The eval results (v1 18 of 20, v2 19 of 20 with the mx-02 regression) are example output; label them on screen. Costs on screen stay as 0.0xx placeholders; do not show real prices.
- Johan Lindqvist and the Gothenburg accounting firm are fictional; test invoices are invented text.
