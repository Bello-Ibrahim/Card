# Screen Demo Pack: AI-11 L20 Capstone Step 2: Clean, Explore and Document

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-11-python-for-ai_L20_screen_1.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Run the L14, L16, L17 and L18 cells so ml exists
2. Add a new code cell
3. Type: assert ml.isna().sum().sum() == 0, "missing values remain"
4. Type: assert ml.select_dtypes("number").shape[1] == ml.shape[1], "non-numeric column"
5. Type: print("Checks passed:", ml.shape)
6. Press Shift + Enter
7. Output: Checks passed: (8, 11)

**Narration over this clip (for pacing)**

> First, her final checks. To keep the demo short, we run them on the order table from lesson eighteen. One assert checks that no values are missing. Another checks that every column is numeric. Both pass, and we see eight rows and eleven columns.

## Clip 2: scene 9

- **Filename:** `ai-11-python-for-ai_L20_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Open the example notebook (hypothetical data)
2. Scroll through: Question · Source (licence, download date) · Load · Audit with problem list
3. Stop at the Cleaning section and highlight the log row: Negative readings (14 rows): removed, because a pollution level cannot be below 0.

**Narration over this clip (for pacing)**

> Now her notebook's structure. It starts with the question and the source, with the licence and download date. Then loading and the audit, ending with a problem list. Then cleaning, one decision per cell, and the log. For example, negative readings were removed, because pollution cannot be below zero.

## Clip 3: scene 10

- **Filename:** `ai-11-python-for-ai_L20_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Scroll to Exploration: three labelled charts, each with one insight sentence
2. Scroll to ML-ready table: target, features, removed columns with reasons, saved CSV
3. Scroll to Limits and highlight the example sentence about the missing month

**Narration over this clip (for pacing)**

> Next, three labelled charts, each with a sentence of insight. Then the ML-ready table, with the removed columns and their reasons, and the saved file. And finally, a short Limits section. For example, one station is missing a full month, so that month's pattern is uncertain.

## Clip 4: scene 11

- **Filename:** `ai-11-python-for-ai_L20_screen_4.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Choose the Colab menu option that restarts the session and runs all cells (check its current name and menu)
2. Wait for all cells to finish
3. Scroll from top to bottom to show every cell ran without errors

**Narration over this clip (for pacing)**

> Last, we restart the session and run all cells. Then we scroll from top to bottom. Every cell has run, and there are no errors. The notebook is ready to share.

## Production notes for this lesson

- [VERSION] The Colab menu option that restarts the session and runs all cells, the Share button options, and the File menu option to save a copy to GitHub must be checked against the live interface before recording.
- Camila's air-quality dataset and findings are hypothetical. The notebook walkthrough scene shows a mock notebook built by the team with the template headings and the example log line from content.md, labelled on screen 'Example notebook, hypothetical data'. No real station or city data is shown.
- The assert demo runs on the synthetic order table ml from L18. Printed output must match content.md: 'Checks passed: (8, 11)'.
- Last lesson: the CTA congratulates learners and points to the capstone submission and rubric.
- Before the demo, run the L14, L16, L17 and L18 cells on screen (or show them already run) so ml exists.
