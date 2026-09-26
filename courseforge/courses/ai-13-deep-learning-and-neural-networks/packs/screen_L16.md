# Screen Demo Pack: AI-13 L16 Tuning Hyperparameters and Learning-Rate Schedules

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L16_screen_1.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run the make_scheduler cell from content.md: SequentialLR(opt, [LinearLR(opt, start_factor=0.1, total_iters=warm), CosineAnnealingLR(opt, T_max=steps - warm)], milestones=[warm])
2. Show the loop line after opt.step(): if sched: sched.step()

**Narration over this clip (for pacing)**

> In Colab, he writes a function that builds a warm-up plus cosine schedule. Warm-up takes the first ten percent of all steps, starting at one tenth of the rate. Cosine decay takes the rest. The scheduler steps after every batch, right after the optimiser.

## Clip 2: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L16_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run the sweep cell: for lr in [1e-4, 3e-4, 1e-3, 3e-3]: for use_schedule in [False, True]: acc = run(lr=lr, use_schedule=use_schedule, epochs=5, seed=0); results.append(...)
2. Show the progress as each of the 8 runs finishes

**Narration over this clip (for pacing)**

> Then the sweep. Four learning rates, each with and without the schedule. That is eight runs, each for five epochs on a subset, with the same seed. Each run returns its best validation accuracy.

## Clip 3: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L16_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run: pd.DataFrame(results).sort_values("val_acc", ascending=False)
2. Plot the learning rate per step for one scheduled run; point to the ramp up and the cosine decay

**Narration over this clip (for pacing)**

> He prints the results as a table, sorted by validation accuracy. Then he plots the learning rate at every step for one scheduled run, to check that the warm-up and the decay look right.

## Clip 4: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L16_screen_4.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Highlight the top two rows of the table
2. Run the top two settings with seeds 1 and 2 and add the rows to the table

**Narration over this clip (for pacing)**

> He picks the best setting on validation accuracy. But a difference smaller than the seed variation he measured in lesson fourteen is not a real difference. So he runs the best two settings with two more seeds before he decides.

## Production notes for this lesson

- [VERSION] Hugging Face TrainingArguments scheduler and warm-up option names (for example, warmup_ratio is not accepted in some newer versions, while warmup_steps is) must be checked at recording time. The voiceover says only that the names differ between versions.
- [VERSION] Colab free GPU usage limits and session length change; the voiceover says only that sessions can end and limits change.
- run(lr, use_schedule, epochs, seed) is Lars's own helper built from the L10 loop; define it in a cell above the demo before recording and pre-run the 8 runs. No accuracy values are stated (content.md gives none); show the real table.
- Lars and the Bergen salmon-farming company are hypothetical; stock footage must not show a real company name or logo.
