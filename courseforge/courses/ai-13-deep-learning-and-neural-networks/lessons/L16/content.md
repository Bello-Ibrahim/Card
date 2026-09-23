# L16 Tuning Hyperparameters and Learning-Rate Schedules

Course: AI-13 · Module: M4 · Objectives: O6 · Video: 5 min (screen demo)

## Hook
A deep network has dozens of settings you could tune, and your free GPU time is limited. If you can afford only eight training runs, which settings deserve them? For most networks the answer starts with one number: the learning rate.

## Explanation
**What matters most.** In practice, a rough order of importance is:

1. **Learning rate.** It has the largest effect on whether training works at all. Search it on a **log scale**, for example `1e-4, 3e-4, 1e-3, 3e-3`, not on a linear one.
2. **Batch size and number of epochs.** Batch size is often set by GPU memory; if you change it a lot, re-check the learning rate. Choose epochs with early stopping (L09) rather than tuning them separately.
3. **Regularisation strength:** weight decay, dropout, augmentation.
4. **Model size:** width, depth, or a larger pretrained checkpoint.

Change settings one group at a time, starting from a known good recipe, such as your L10 or L13 run.

**Learning-rate schedules** change the learning rate during training. Large steps early make fast progress; small steps late settle into a good minimum. Common choices:

- **Step decay:** divide the rate by 10 at fixed epochs.
- **Cosine decay:** lower the rate smoothly along a cosine curve to near zero.
- **Warm-up:** start with a small rate and increase it over the first few percent of steps. This avoids large, unstable updates while the new layers are still random, and is standard when fine-tuning transformers.

Most schedulers in PyTorch are stepped **once per batch** or **once per epoch**, depending on how you set their length. Be consistent. In the Hugging Face Trainer, you set `lr_scheduler_type` and a warm-up option in `TrainingArguments`; the warm-up option names differ between versions. [VERSION]

**Planning within free GPU time.** Free Colab sessions can end, and usage limits change. [VERSION] Plan small: use a data subset and fewer epochs for the sweep, then retrain only the best setting on the full data. Save results after every run (L17).

**Analogy:** Tuning is like adjusting a new bicycle. First you set the saddle height, because nothing else matters if it is wrong. Then you adjust the handlebars and the gears. A learning-rate schedule is like changing gear: a strong gear on the flat road at the start, a gentle one on the steep final hill.

## Worked Example
Lars is an ML engineer at a hypothetical salmon-farming company in Bergen, Norway. He classifies fish-health images with the ResNet from L10 and has time for 8 short runs.

**Screen demo steps:**

1. Define a `run(lr, use_schedule)` function that trains for 5 epochs on a subset and returns the best validation accuracy.
2. Add a warm-up plus cosine schedule, stepped after every batch.
3. Loop over 4 learning rates, with and without the schedule, and show the results table.

```python
from torch.optim.lr_scheduler import LinearLR, CosineAnnealingLR, SequentialLR

def make_scheduler(opt, epochs, steps_per_epoch):
    steps = epochs * steps_per_epoch
    warm = int(0.1 * steps)
    return SequentialLR(opt, [LinearLR(opt, start_factor=0.1, total_iters=warm),
                              CosineAnnealingLR(opt, T_max=steps - warm)], milestones=[warm])

# inside the training loop, after opt.step():
#     if sched: sched.step()

results = []
for lr in [1e-4, 3e-4, 1e-3, 3e-3]:
    for use_schedule in [False, True]:
        acc = run(lr=lr, use_schedule=use_schedule, epochs=5, seed=0)
        results.append({"lr": lr, "schedule": use_schedule, "val_acc": acc})
```

Lars prints `results` as a table, sorted by `val_acc`. He also plots the learning rate per step for one run with the schedule to check that the warm-up and decay look right. He chooses the best setting on validation accuracy, but he notes that a difference smaller than the seed variation he measured in L14 is not a real difference. He then runs the best two settings with two more seeds before deciding.

## Common Mistake
Many learners tune many settings at once with a large grid, run out of GPU time halfway, and cannot tell which setting mattered. Another common mistake is calling `scheduler.step()` once per epoch for a scheduler whose length was set in batches. The learning rate then hardly changes, and the "schedule" has no effect. Plot the learning rate you actually used; it takes one line and catches this bug immediately.

## Key Takeaways
1. Tune the learning rate first, on a log scale; then batch size and epochs (with early stopping), regularisation and model size.
2. Schedules such as warm-up plus cosine decay use large steps early and small steps late; step them consistently and plot the result.
3. Plan small sweeps on subsets within free GPU limits, and treat differences smaller than seed variation as ties.

## Hands-on Exercise
**Task:** Run a small learning-rate sweep with and without a scheduler and choose the best setting from validation scores.
**Tools:** Google Colab with a GPU runtime (free; optional); PyTorch; your model from L10 or L13. CPU fallback: use your L07 CNN on a 10,000-image Fashion-MNIST subset with 3 epochs per run.
**Steps:**
1. Write a `run(lr, use_schedule, epochs, seed)` function that returns the best validation score.
2. Choose 4 learning rates on a log scale around your current value.
3. Run each rate with and without warm-up plus cosine decay (8 runs in total), with the same seed and data.
4. Plot the learning rate per step for one scheduled run.
5. Show a results table sorted by validation score, and rerun the top 2 settings with 2 more seeds.
6. Write three sentences choosing a final setting and explaining your evidence.
**What good looks like:** Eight comparable runs, a correct learning-rate plot, a sorted table, extra seeds for the leading settings, and a choice that respects seed variation.
**Time:** about 45 minutes

## Review Flags
- [VERSION] Hugging Face `TrainingArguments` scheduler and warm-up option names (for example, `warmup_ratio` is not accepted in some newer versions, while `warmup_steps` is) and Colab free GPU usage limits and session length must be checked at recording time.
