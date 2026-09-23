# L17 Tracking Experiments and Reproducibility

Course: AI-13 · Module: M4 · Objectives: O6, O7 · Video: 5 min (screen demo)

## Hook
Two weeks ago you had a model with a great validation score. Today you cannot remember the learning rate, the notebook has changed, and the Colab session that trained it has ended. The model is gone. This lesson makes sure that never happens to your capstone.

## Explanation
An experiment is only useful if you can **find it, compare it and repeat it**. Four habits cover most of this.

**1. Fix the seeds.** Set the seed for Python, NumPy and PyTorch at the start of every run. This makes runs repeatable enough to compare, although some GPU operations are not fully deterministic, so tiny differences can remain. Seeds are for repeatability; you still run several seeds to measure variation (L14).

**2. Put every setting in one config dictionary.** Learning rate, batch size, epochs, model name, data subset, augmentation, dropout, weight decay, seed. The training code reads only from the config. Then the config is a complete description of the run, and you can save it next to the results.

**3. Log every run to a results table.** One row per run: the run name, all config values, the best validation score, the best epoch, and the date. A CSV file is enough. Log failed and poor runs too; they are evidence for your report.

**4. Save checkpoints outside the session.** Colab's local disk is deleted when the session ends. Mount Google Drive and save the best checkpoint there, together with its config. [VERSION] Check the size first, because Drive storage on a free plan is limited. [VERSION]

**Optional tools.** TensorBoard (`torch.utils.tensorboard.SummaryWriter`) plots curves for many runs side by side, and the Hugging Face Trainer can log to it with `report_to`. Hosted experiment-tracking services also exist; check what their free plans include before depending on them. [VERSION] A CSV table and saved plots are enough for this course.

Never log personal or confidential data, or secret keys, into tables, notebooks or tracking services.

**Analogy:** A results table is like a laboratory notebook in chemistry. A chemist writes down the quantities, temperature and time for every attempt, including the failures, so that any result can be repeated by someone else. A saved checkpoint is the labelled sample in the fridge.

## Worked Example
Zanele is a data scientist at a hypothetical wine producer in Stellenbosch, South Africa. She is classifying grape-leaf photos and loses work when her Colab session ends. She adds tracking to her notebook.

**Screen demo steps:**

1. Mount Google Drive and create a project folder.
2. Define the seed function and config.
3. After training, save the checkpoint and append a row to the results table.
4. Restart the runtime, reload the checkpoint and check the validation score again.

```python
import os, random, numpy as np, pandas as pd, torch
from google.colab import drive                                   # [VERSION]
drive.mount("/content/drive")
out_dir = "/content/drive/MyDrive/ai13"; os.makedirs(out_dir, exist_ok=True)

def set_seed(seed):
    random.seed(seed); np.random.seed(seed); torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

config = {"run": "cnn_dropout03", "lr": 1e-3, "batch_size": 64, "epochs": 10,
          "dropout": 0.3, "weight_decay": 1e-2, "seed": 0}
set_seed(config["seed"])
# ... build model and train using only values from config ...

ckpt = f"{out_dir}/{config['run']}.pt"
torch.save({"model": model.state_dict(), "config": config}, ckpt)
table = f"{out_dir}/results.csv"
pd.DataFrame([{**config, "val_acc": best_val_acc}]).to_csv(
    table, mode="a", header=not os.path.exists(table), index=False)

state = torch.load(ckpt, map_location="cpu")
model.load_state_dict(state["model"])
```

After reloading, Zanele evaluates the model on the validation split and confirms that the score matches the one in the table. This check proves that the checkpoint, the preprocessing and the code all still fit together.

## Common Mistake
Many learners save only the weights and keep the settings in their head, or in notebook cells they later edit. A checkpoint without its config and preprocessing details is hard to use: you do not know which transforms, class order or tokenizer it expects. Save the config, including the class names and preprocessing, with the weights, and test reloading in a fresh session before you trust it. Another mistake is saving every epoch's checkpoint to Drive and filling the storage; save the best one only.

## Key Takeaways
1. Fix seeds and keep every setting in one config dictionary, so each run is fully described and repeatable.
2. Log every run, including poor ones, to a results table with its config, best score and best epoch.
3. Save the best checkpoint with its config to Google Drive, and test reloading it in a fresh session.

## Hands-on Exercise
**Task:** Log 3 runs to a results table with their settings and scores, save the best checkpoint to Drive, and reload it.
**Tools:** Google Colab (free); Google Drive (free storage); PyTorch; pandas. Optional: TensorBoard. CPU fallback: use short runs on a data subset; if Drive is not available, save to a local folder and download the file.
**Steps:**
1. Add a `set_seed` function and a `config` dictionary to your L16 notebook.
2. Mount Drive and create a project folder. [VERSION]
3. Run 3 experiments that differ in one setting, and append one row per run to `results.csv`.
4. Save only the best run's checkpoint with its config.
5. Restart the runtime, reload the checkpoint, and confirm the validation score matches the table.
6. Optional: log the three runs to TensorBoard and compare the curves.
**What good looks like:** A CSV with 3 complete rows, a checkpoint that includes its config, a successful reload in a fresh session with a matching score, and no personal data or keys in any log.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Google Colab Drive mounting (`google.colab.drive`), Google Drive free storage limits, TensorBoard integration, the Trainer `report_to` option, and the features and free plans of hosted experiment-tracking tools must be checked at recording time.
