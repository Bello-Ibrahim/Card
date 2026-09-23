# L13 Fine-Tuning a Transformer for Text Classification

Course: AI-13 · Module: M3 · Objectives: O4 · Video: 6 min (screen demo)

## Hook
In L10 you gave a pretrained image network a new head and taught it bean diseases. The same idea works for text, and with Hugging Face the whole process, from raw dataset to evaluated model, fits in about thirty lines.

## Explanation
Fine-tuning a transformer for classification has five parts.

1. **Dataset.** The `datasets` library loads public datasets from the Hub into a `DatasetDict` with splits such as `train` and `test`. Use `.shuffle(seed).select(range(n))` to take a subset, and `train_test_split` to create a validation split from the training data. [VERSION]
2. **Tokenisation in batches.** `dataset.map(fn, batched=True)` applies the tokenizer to many rows at once and caches the result. Truncate to a `max_length` that fits most texts; padding can be done later, per batch, by a **data collator**, which is faster than padding everything to the same length.
3. **Model.** `AutoModelForSequenceClassification.from_pretrained(name, num_labels=k)` loads the pretrained encoder and adds a new, randomly initialised classification head. A warning that some weights are "newly initialized" is expected.
4. **Training setup.** `TrainingArguments` holds the settings: learning rate, batch size, epochs, weight decay, and when to evaluate and save. Parameter names change between versions; for example, older code uses `evaluation_strategy`, and newer versions use `eval_strategy`. [VERSION]
5. **Trainer.** `Trainer` runs the loop from L05 for you, including device placement, mixed precision if enabled, evaluation and checkpoints. A `compute_metrics` function turns predictions into accuracy and F1.

Unlike L10, you usually fine-tune **all** layers of a small transformer, with a small learning rate (around `2e-5` to `5e-5` is a common starting range) for a few epochs.

**Analogy:** An experienced translator who moves to a new publishing house does not relearn the language. They spend a few days learning the house style and the kinds of documents it handles. Fine-tuning is those few days: small, careful adjustments to skills that are already there.

## Worked Example
Joaquín is a data scientist at a hypothetical news aggregator in Rosario, Argentina. He wants to sort incoming English headlines and summaries into four topics: World, Sports, Business and Sci/Tech. He prototypes with AG News, a public topic-classification dataset. [VERIFY] Dataset and model licences must be checked on their Hub pages.

**Screen demo steps:**

1. Load the dataset and take small subsets so that training fits in free GPU time (or on CPU).
2. Tokenise with `map` and create the model.
3. Set the training arguments and metrics, then train and evaluate on the test subset.

```python
import numpy as np
from datasets import load_dataset
from sklearn.metrics import accuracy_score, f1_score
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                          TrainingArguments, Trainer, DataCollatorWithPadding)

name = "distilbert-base-uncased"                               # [VERIFY] licence
ds = load_dataset("fancyzhx/ag_news")                          # [VERIFY] ID and licence
train = ds["train"].shuffle(seed=42).select(range(4000)).train_test_split(0.2, seed=42)
test = ds["test"].shuffle(seed=42).select(range(2000))

tok = AutoTokenizer.from_pretrained(name)
enc = lambda b: tok(b["text"], truncation=True, max_length=128)
train, test = train.map(enc, batched=True), test.map(enc, batched=True)

model = AutoModelForSequenceClassification.from_pretrained(name, num_labels=4)

def metrics(p):
    preds = np.argmax(p.predictions, axis=1)
    return {"accuracy": accuracy_score(p.label_ids, preds),
            "f1_macro": f1_score(p.label_ids, preds, average="macro")}

args = TrainingArguments("agnews-run", learning_rate=3e-5, num_train_epochs=2,
                         per_device_train_batch_size=32, weight_decay=0.01,
                         eval_strategy="epoch", save_strategy="epoch",    # [VERSION]
                         load_best_model_at_end=True, seed=42, report_to="none")
trainer = Trainer(model=model, args=args, train_dataset=train["train"],
                  eval_dataset=train["test"], data_collator=DataCollatorWithPadding(tok),
                  compute_metrics=metrics)
trainer.train()
print(trainer.evaluate(test))
```

Joaquín chooses the best epoch on the **validation** split and evaluates the test subset only once, at the end. He reports the accuracy and macro F1 he measured, and notes the subset sizes, because results on 4,000 examples are not comparable with published results on the full dataset. On CPU, he uses 1,000 training examples and `max_length=64` so that the run finishes in reasonable time.

## Common Mistake
Many learners pass the test split as `eval_dataset` and use it with `load_best_model_at_end=True`. The Trainer then selects the checkpoint that is best on the test set, and the final test score is too optimistic. Use a validation split for evaluation during training, and touch the test split once. A second common mistake is copying `TrainingArguments` from an old tutorial and getting an "unexpected keyword argument" error; check the parameter names for your installed version. [VERSION]

## Key Takeaways
1. Load data with `datasets`, tokenise with `map(batched=True)`, and pad per batch with a data collator.
2. `AutoModelForSequenceClassification` adds a new head to a pretrained encoder; fine-tune all layers with a small learning rate for a few epochs.
3. Choose checkpoints on a validation split, evaluate the test split once, and check `TrainingArguments` names against your installed version.

## Hands-on Exercise
**Task:** Fine-tune a small pretrained model on a subset of AG News on the free GPU and report accuracy and F1 on the test split.
**Tools:** Google Colab with a GPU runtime (free; optional); Hugging Face `transformers`, `datasets` and `accelerate` (the Trainer needs it; install with `pip install transformers[torch]` if it is missing); scikit-learn. CPU fallback: 1,000 training examples and `max_length=64`.
**Steps:**
1. Check the Hub pages of the dataset and the model for licence and intended use. [VERIFY]
2. Create train, validation and test subsets with a fixed seed.
3. Tokenise with `map`, create the model with `num_labels=4`, and set `TrainingArguments` for your installed version. [VERSION]
4. Train for 2 epochs with evaluation on the validation split each epoch.
5. Evaluate the best checkpoint once on the test subset and record accuracy and macro F1.
6. Save the per-epoch validation results for L14.
**What good looks like:** A run that completes without errors, a clean split between validation and test, both metrics reported with subset sizes, and settings recorded so the run can be repeated.
**Time:** about 45 minutes

## Review Flags
- [VERSION] Hugging Face `TrainingArguments` and `Trainer` parameter names (`eval_strategy` compared with the older `evaluation_strategy`, and other renamed options) and `datasets` loading and `train_test_split` behaviour must be checked against the Colab versions at recording time.
- [VERIFY] AG News: Hub dataset ID, source and licence; `distilbert-base-uncased`: licence and intended use.
