# Screen Demo Pack: AI-13 L18 Capstone Step 1: Choose a Task and Build a Baseline

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L18_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Open the chosen dataset's card on the Hugging Face Hub; scroll to the licence and the label description
2. Add a text cell: dataset name, licence, source, label meanings

**Narration over this clip (for pacing)**

> She starts on the dataset card. She reads the licence, which allows educational use, and the label description, and writes both into a text cell in her notebook, before any code.

## Clip 2: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L18_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run: ds = load_dataset("<chosen dataset ID>"); split = ds["train"].train_test_split(test_size=0.2, seed=0); train, val = split["train"], split["test"]
2. Run: print(train.features["label"], train.to_pandas()["label"].value_counts())
3. Point to the class counts

**Narration over this clip (for pacing)**

> Then she loads the data, and splits off twenty percent of the training set for validation, with a fixed seed. She prints the label names and counts to check the class balance.

## Clip 3: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L18_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Run: vec = TfidfVectorizer(ngram_range=(1, 2), min_df=2); clf = LogisticRegression(max_iter=1000, class_weight="balanced")
2. Run: clf.fit(vec.fit_transform(train["text"]), train["label"]); preds = clf.predict(vec.transform(val["text"]))
3. Run: print("baseline macro F1:", f1_score(val["label"], preds, average="macro"))

**Narration over this clip (for pacing)**

> Now the baseline. A TF-IDF vectoriser with single words and word pairs, and a balanced logistic regression. She fits it on the training text, and scores macro F1 on the validation split. It takes seconds on a CPU.

## Clip 4: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L18_screen_4.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Append the baseline row to results.csv with its config (L17 code)
2. Add a text cell 'Experiment plan' with 3 numbered experiments, each with a hypothesis, one change and the metric validation macro F1

**Narration over this clip (for pacing)**

> She adds the baseline row to her results table, with its config. Then she writes her plan. One, fine-tune a small pretrained encoder with default settings. Two, the same with a learning-rate sweep and warm-up. Three, the best setting with a longer maximum length, because some reviews are long. The test split is not touched.

## Production notes for this lesson

- [VERIFY] The dataset ID in content.md is a placeholder (your-chosen/dataset). The course team must provide 3 example datasets with confirmed licences and IDs; record the demo with one of them, a three-label English review-sentiment dataset whose card states a licence that allows educational use, and show its card on screen. The voiceover names no dataset.
- The baseline score is not stated (content.md gives none). Show the real printed macro F1; do not add numbers in captions.
- The capstone rubric (capstone_rubric.md) should be linked from the course page under this video.
- Fatima and the Dakar telecoms company are hypothetical; she uses public review text only, never employer data. Stock footage must not show a real operator's name or logo.
