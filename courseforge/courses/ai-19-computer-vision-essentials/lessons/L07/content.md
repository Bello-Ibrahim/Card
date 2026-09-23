# L07 Transfer Learning: Fine-Tuning on Your Own Images

Course: AI-19 · Module: M2 · Objectives: O2, O4 · Video: 5 min (screen demo)

## Hook
In L06 the general model did not know your categories. Training a new model from zero needs a very large labelled dataset. With transfer learning, around a thousand labelled images and a short Colab session can be enough to teach a pre-trained model a new task.

## Explanation
Recall from L05 that image models learn general features in their early and middle layers: edges, textures, shapes and parts. Only the last layer, the **classification head**, is specific to the original labels.

**Transfer learning** keeps the pre-trained layers, called the **backbone**, and replaces the head with a new one that has your classes. There are two common levels:

- **Feature extraction:** freeze the backbone and train only the new head. This is fast and needs little data.
- **Full fine-tuning:** also update backbone layers with a small learning rate. This can fit your data better, but needs more data and time, and can overfit small datasets.

Start with feature extraction.

This works with little data because the backbone already knows what an edge or a leaf vein looks like. Your data only teaches the head which combination of features means "rust" or "healthy".

Keep **train**, **validation** and **test** splits separate, and check the test split once, at the end.

Free Colab GPUs are useful here but are not guaranteed, and session length is limited. [VERSION] Save your model to Google Drive or the Hub when training ends. [VERIFY]

**Analogy:** Transfer learning is like hiring an experienced photographer to sort plant photos. They already know light, shapes and colours. You only show them a few hundred examples of each plant disease. A beginner would need years; the photographer needs an afternoon.

## Worked Example
Grace Namukasa works for an agricultural advice service in Mbale, Uganda. She wants a model that classifies bean leaf photos as healthy or as one of two diseases. She uses a public bean leaf dataset collected in Uganda and hosted on the Hugging Face Hub. [VERIFY]

```python
import torch
from datasets import load_dataset
from transformers import (AutoImageProcessor, AutoModelForImageClassification,
                          TrainingArguments, Trainer)

ds = load_dataset("AI-Lab-Makerere/beans")          # [VERIFY] id and licence
names = ds["train"].features["labels"].names
ckpt = "google/vit-base-patch16-224-in21k"
proc = AutoImageProcessor.from_pretrained(ckpt)

def transform(batch):
    out = proc([im.convert("RGB") for im in batch["image"]], return_tensors="pt")
    out["labels"] = batch["labels"]
    return out

def collate(items):
    return {"pixel_values": torch.stack([x["pixel_values"] for x in items]),
            "labels": torch.tensor([x["labels"] for x in items])}

ds = ds.with_transform(transform)
model = AutoModelForImageClassification.from_pretrained(
    ckpt, num_labels=len(names), id2label=dict(enumerate(names)))
for p in model.base_model.parameters():
    p.requires_grad = False                        # train only the new head

args = TrainingArguments("beans-vit", num_train_epochs=3, learning_rate=1e-3,
                         per_device_train_batch_size=32,
                         remove_unused_columns=False, report_to="none")
trainer = Trainer(model=model, args=args, train_dataset=ds["train"],
                  data_collator=collate)

def accuracy(split):
    p = trainer.predict(ds[split])
    return (p.predictions.argmax(-1) == p.label_ids).mean()

print("before:", accuracy("test"))
trainer.train()
print("after: ", accuracy("test"))
```

The "before" score uses the untrained head, so it is close to guessing (about one in three). Example output: `before: 0.34`, followed by a clearly higher "after" value. Your numbers will differ, and they are not a benchmark.

**On screen (presenter steps):**
1. In Colab, choose Runtime, then Change runtime type, and select a GPU if one is available. [VERSION]
2. Run the cell and point to the line that freezes the backbone.
3. Show the "before" accuracy and the training loss going down.
4. Show the "after" accuracy and save the model with `trainer.save_model()`.

## Common Mistake
Many learners report accuracy on the training images. That only shows the model remembers what it saw; report the test split instead. Another mistake is unfreezing the whole backbone with a high learning rate on a small dataset, which can destroy the pre-trained features. Use a small learning rate when you unfreeze.

## Key Takeaways
1. Transfer learning reuses a pre-trained backbone and trains a new head for your classes, so it needs much less data and time.
2. Start by freezing the backbone and training only the head; unfreeze layers later only if you have enough data.
3. Keep train, validation and test splits separate, and report results on the test split.

## Hands-on Exercise
**Task:** Fine-tune a small pre-trained model on a public dataset of 3 to 5 classes in Colab, and compare its accuracy on test images with the model before fine-tuning.
**Tools:** Google Colab (GPU if available [VERSION]); `transformers` and `datasets` [VERSION]; the bean leaf dataset or another public dataset of 3 to 5 classes with a licence that allows your use. [VERIFY]
**Steps:**
1. Enable a GPU runtime if one is available.
2. Load the dataset and print the class names and the size of each split.
3. Load the pre-trained model with a new head and freeze the backbone.
4. Record test accuracy before training.
5. Train for 3 epochs and record test accuracy after training.
6. Unfreeze the backbone, set the learning rate to `2e-5`, train again for 2 epochs and record the result.
7. Save the best model, because you will use it in L08.
**What good looks like:** A notebook that runs from top to bottom, with a small table of test accuracy before training, after head-only training and after fine-tuning, plus one sentence on which approach worked best on this dataset.
**Time:** about 40 minutes

## Review Flags
- [VERIFY] Curriculum flag: confirm the licence and current location of the bean leaf disease dataset (Hub ID `AI-Lab-Makerere/beans`, column names `image` and `labels`, and that it was collected in Uganda) before scripting.
- [VERIFY] Confirm the recommended way to save a model from Colab (Google Drive mount or push to the Hub) and whether free GPU sessions are available.
- [VERSION] Google Colab GPU availability, session limits and the Runtime menu path change and are not guaranteed.
- [VERSION] Hugging Face `transformers` and `datasets` APIs (`TrainingArguments` arguments, `with_transform`, `base_model`) and the checkpoint ID `google/vit-base-patch16-224-in21k`. Code was checked for syntax only; accuracy values are example output, not benchmarks.
