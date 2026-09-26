# Screen Demo Pack: AI-13 L14 Evaluating Deep Models Properly

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L14_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Show the run_experiment(seed) cell built from the L13 code; highlight seed=seed in TrainingArguments and in .shuffle(seed=seed)
2. Highlight the return line: preds, labels as NumPy arrays

**Narration over this clip (for pacing)**

> In Colab, she has wrapped her training code in a function that takes a seed and returns the validation predictions and labels. The function sets the seed everywhere, so each run can be repeated. The same seed always gives the same result.

## Clip 2: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L14_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run: results = []; for seed in [0, 1, 2]: preds, labels = run_experiment(seed=seed); results.append(f1_score(labels, preds, average="macro"))
2. Run the print line: macro F1 mean, std, min, max
3. Point to the spread between min and max

**Narration over this clip (for pacing)**

> She runs it with seeds zero, one and two, computes macro F1 for each, and prints the mean, standard deviation, minimum and maximum. This is the number she reports, not the best single run.

## Clip 3: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L14_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run: ConfusionMatrixDisplay.from_predictions(labels, preds, display_labels=["World", "Sports", "Business", "Sci/Tech"])
2. Run: wrong = np.where(preds != labels)[0]; for i in wrong[:10]: print(labels[i], "->", preds[i], "|", val_texts[i][:120])

**Narration over this clip (for pacing)**

> Next, a confusion matrix for one run, with the four topic names. Then she lists the first ten misclassified validation examples, with the true label, the predicted label, and the start of the text.

## Clip 4: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L14_screen_4.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Point to the largest off-diagonal cells: Business ↔ Sci/Tech
2. Scroll the printed errors and highlight two tech-earnings summaries and one likely mislabel

**Narration over this clip (for pacing)**

> She reads them and groups them. Most errors are between Business and Science and Technology. Summaries about technology companies' earnings could fit either label. A few look mislabelled.

## Production notes for this lesson

- [VERIFY] AG News dataset licence and source (carried from L13) must be confirmed before the dataset is used in the recording.
- run_experiment is the learner's own L13 code wrapped in a function; define it in a cell above the demo before recording. It must set the seed in TrainingArguments and in any subset shuffling.
- No scores are stated in the voiceover (content.md gives none). Show the real mean, std, min and max printed by the notebook; do not add numbers in captions.
- Three seeded runs take time on the free GPU; pre-run them and speed up the training segment in the edit.
- Ayesha and the Dhaka non-profit are hypothetical; stock footage must not show a real organisation's name or logo.
