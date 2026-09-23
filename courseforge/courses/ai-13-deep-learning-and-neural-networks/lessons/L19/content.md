# L19 Capstone Step 2: Fine-Tune and Compare

Course: AI-13 · Module: M4 · Objectives: O4, O6, O7 · Video: 5 min (screen demo)

## Hook
You now have a baseline and a plan. This week you will train several models, and one of them will look best. The hard part is not training them. It is being able to say, honestly, that the winner really is better, and then measuring it on the test set exactly once.

## Explanation
**Run the plan, in order.** Start with the experiment most likely to give a large gain, usually a pretrained model: a ResNet from torchvision for images (L10), or a small encoder from the Hub for text (L13). Then add regularisation (L09) and tuning (L16) one change at a time. After each run, log a row to your results table (L17) and write one line in your plan: was the hypothesis supported?

**Compare fairly.** Every run in the comparison must use:

- the **same validation split** and the same preprocessing for evaluation;
- the **same main metric**, computed the same way;
- a comparable **budget**, or a note when one run had more epochs or a larger model;
- more than one **seed** for the leading candidates (L14).

**Choose the final model on validation data,** and justify it. The best score is not the only reason: if two models are within seed variation, prefer the smaller, faster or simpler one. Write down the reason in one or two sentences.

**Test once.** Only after the choice is final, evaluate the chosen model **once** on the test split and report that number. If you then change the model because of the test result, the test score is no longer an honest estimate, and you must say so in your report.

Pretrained checkpoints have their own licences and training data; record the checkpoint name and licence for each one you use. [VERIFY]

**Analogy:** Comparing models is like judging a cooking competition. Every chef must cook the same dish, with the same ingredients and time limit, for the same judges. The final, public tasting happens once. If a chef could taste the judges' plate and then cook again, the result would not be fair.

## Worked Example
Diego is an ML engineer at a hypothetical avocado exporter in Uruapan, Mexico. His capstone classifies leaf photos into four classes from a public dataset with a confirmed licence. His baseline is a small CNN trained from scratch.

**Screen demo steps:**

1. Show the results table with the baseline row.
2. Run the planned experiments and show new rows appearing.
3. Rerun the top two with 2 more seeds and show the mean and spread.
4. Write the choice and its justification, then run the test evaluation once.

```python
import pandas as pd

runs = pd.read_csv("/content/drive/MyDrive/ai13/results.csv")
summary = (runs.groupby("run")["val_f1"]
               .agg(["mean", "std", "count"])
               .sort_values("mean", ascending=False))
print(summary)

# only after the final choice is written down:
final = load_checkpoint("resnet18_ft_layer4")          # your L17 reload code
test_f1 = evaluate(final, test_dl)                     # run exactly once
print("TEST macro F1:", round(test_f1, 3))
```

Diego's table shows four runs: the baseline CNN, a frozen ResNet-18 with a new head, the same with `layer4` fine-tuned, and the fine-tuned model with a learning-rate schedule. The two fine-tuned runs are within seed variation of each other. Diego chooses the version **without** the schedule, because it is simpler and equally good, and writes this reason next to the table. He then runs the test evaluation once and copies the number into his report without changing the model.

## Common Mistake
Many learners evaluate every candidate on the test set "just to see", and then pick the best test score. This makes the test set a second validation set, and the reported score is too optimistic. Another mistake is comparing runs that used different validation splits, for example because the split was created without a fixed seed. Check that the validation split is identical across all runs before you compare scores.

## Key Takeaways
1. Run planned experiments one change at a time, starting with a pretrained model, and log every run with its config.
2. Compare on the same validation split and metric, use extra seeds for the leaders, and prefer the simpler model when results are within seed variation.
3. Evaluate the chosen model once on the test set, and report that number without further changes.

## Hands-on Exercise
**Task:** Capstone step 2: run at least 3 tracked experiments, choose the final model, and evaluate it once on the test set.
**Tools:** Google Colab with a GPU runtime (free; optional); PyTorch and torchvision, or Hugging Face `transformers`; your results table from L17. CPU fallback: use a data subset, a frozen backbone or a small encoder, and fewer epochs.
**Steps:**
1. Run at least 3 experiments from your L18 plan, including at least one pretrained model, and log each to the results table.
2. Mark each hypothesis as supported, not supported or unclear, with one line of evidence.
3. Rerun your top 2 settings with 2 more seeds and report the mean and spread.
4. Write down the final choice and a 2–3 sentence justification.
5. Evaluate the chosen model once on the test set and record the result with the date.
6. Record the name and licence of every pretrained checkpoint you used. [VERIFY]
**What good looks like:** At least 3 comparable logged runs plus the baseline, seed results for the leaders, a written justification made before the test run, and one test score reported honestly.
**Time:** about 90 minutes

## Review Flags
- [VERIFY] Licences and intended uses of all pretrained checkpoints used by learners (for example, ImageNet-pretrained torchvision weights and Hub encoders) must be recorded; the course page should link to where to find them.
