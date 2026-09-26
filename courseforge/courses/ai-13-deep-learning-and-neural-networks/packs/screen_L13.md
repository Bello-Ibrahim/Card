# Screen Demo Pack: AI-13 L13 Fine-Tuning a Transformer for Text Classification

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L13_screen_1.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Show the AG News and distilbert-base-uncased Hub pages (licence sections)
2. Run: ds = load_dataset("fancyzhx/ag_news")
3. Run: train = ds["train"].shuffle(seed=42).select(range(4000)).train_test_split(0.2, seed=42); test = ds["test"].shuffle(seed=42).select(range(2000))

**Narration over this clip (for pacing)**

> In Colab, he loads the dataset and takes small subsets, so training fits in free GPU time. Four thousand training examples, with twenty percent split off for validation, and two thousand test examples.

## Clip 2: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L13_screen_2.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Run: tok = AutoTokenizer.from_pretrained(name); enc = lambda b: tok(b["text"], truncation=True, max_length=128)
2. Run: train, test = train.map(enc, batched=True), test.map(enc, batched=True)
3. Run: model = AutoModelForSequenceClassification.from_pretrained(name, num_labels=4); point to the 'newly initialized' warning

**Narration over this clip (for pacing)**

> He loads the DistilBERT tokenizer, tokenises both splits with map, truncating at one hundred and twenty-eight tokens, and creates the model with four labels.

## Clip 3: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L13_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run the metrics cell: accuracy_score and f1_score(average="macro")
2. Run the TrainingArguments cell: learning_rate=3e-5, num_train_epochs=2, per_device_train_batch_size=32, weight_decay=0.01, eval_strategy="epoch", save_strategy="epoch", load_best_model_at_end=True, seed=42, report_to="none"
3. Highlight eval_strategy

**Narration over this clip (for pacing)**

> Next, a metrics function for accuracy and macro F1. Then the training arguments. A learning rate of three times ten to the minus five, two epochs, batches of thirty-two, evaluation and saving every epoch, and keep the best model at the end.

## Clip 4: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L13_screen_4.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Run: trainer = Trainer(model=model, args=args, train_dataset=train["train"], eval_dataset=train["test"], data_collator=DataCollatorWithPadding(tok), compute_metrics=metrics)
2. Run: trainer.train() and show the per-epoch validation metrics
3. Run once: print(trainer.evaluate(test))

**Narration over this clip (for pacing)**

> He builds the Trainer with the validation split as the evaluation set, and a data collator for padding. He trains, and then evaluates the test subset only once, at the end. He reports the accuracy and F1 he measured, and notes the subset sizes, because results on four thousand examples are not comparable with published results on the full dataset.

## Production notes for this lesson

- [VERSION] Check TrainingArguments and Trainer parameter names (eval_strategy compared with the older evaluation_strategy, and other renamed options) and datasets loading and train_test_split behaviour against the Colab versions at recording time.
- [VERIFY] AG News Hub dataset ID (fancyzhx/ag_news in content.md), source and licence, and the licence and intended use of distilbert-base-uncased, must be confirmed before recording. Show both Hub pages briefly on screen.
- Results: content.md gives no numbers. The voiceover says learners report their own accuracy and macro F1; do not add numbers in captions. Results on the 4,000-example subset are not comparable with published full-dataset results.
- The Trainer needs accelerate; if missing, install with pip install transformers[torch] in a hidden cell before recording. Speed up the training segment in the edit.
- Joaquín and the Rosario news aggregator are hypothetical; stock footage must not show real news brands or logos.
