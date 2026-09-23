# L16 Tuning Hyperparameters and Learning-Rate Schedules | Presenter Script

Course: AI-13 · Video: 5 min · Words: 707

## Hook
A deep network has dozens of settings you could tune, and your free GPU time is limited. If you can afford only eight training runs, which settings deserve them? For most networks, the answer starts with one number. The learning rate.

## Explain
Welcome to the last module, where we tune, track and build the capstone. In practice, there is a rough order of importance. First, the learning rate, because it decides whether training works at all. Search it on a log scale, such as one times ten to the minus four, then three times, then ten times, not in equal steps.

Second, batch size and epochs. Batch size is often set by GPU memory, and if you change it a lot, re-check the learning rate. Choose epochs with early stopping, rather than tuning them. Third, regularisation strength. Fourth, model size. Change one group at a time, starting from a known good recipe, such as your run from lesson ten or thirteen.

A learning-rate schedule changes the rate during training. Large steps early make fast progress, and small steps late settle into a good minimum. Step decay divides the rate by ten at fixed epochs. Cosine decay lowers it smoothly to near zero. And warm-up starts small and increases it over the first few percent of steps.

Warm-up avoids large, unstable updates while the new layers are still random, and it is standard when fine-tuning transformers. Most schedulers step once per batch, or once per epoch, depending on how you set their length. Be consistent. The Trainer has its own scheduler settings, and their names differ between versions.

Tuning is like adjusting a new bicycle. First, the saddle height, because nothing else matters if it is wrong. Then the handlebars and gears. A schedule is like changing gear. A strong gear on the flat road at the start, and a gentle one on the steep final hill.

Free sessions can end, and usage limits change. So plan small. Use a data subset and fewer epochs for the sweep, then retrain only the best setting on the full data. And save results after every run.

## Demonstrate
Lars is an engineer at a salmon-farming company in Bergen, Norway. He classifies fish-health images with the ResNet from lesson ten, and has time for eight short runs.

In Colab, he writes a function that builds a warm-up plus cosine schedule. Warm-up takes the first ten percent of all steps, starting at one tenth of the rate. Cosine decay takes the rest. The scheduler steps after every batch, right after the optimiser.

Then the sweep. Four learning rates, each with and without the schedule. That is eight runs, each for five epochs on a subset, with the same seed. Each run returns its best validation accuracy.

He prints the results as a table, sorted by validation accuracy. Then he plots the learning rate at every step for one scheduled run, to check that the warm-up and the decay look right.

He picks the best setting on validation accuracy. But a difference smaller than the seed variation he measured in lesson fourteen is not a real difference. So he runs the best two settings with two more seeds before he decides.

A common mistake is a huge grid that runs out of GPU time halfway. Another is stepping a scheduler once per epoch when its length was set in batches. The rate hardly changes, and the schedule does nothing. One plot catches it.

## Recap
Let's recap. First, tune the learning rate first, on a log scale. Then batch size and epochs with early stopping, then regularisation and model size. Second, schedules such as warm-up plus cosine use large steps early and small steps late. Step them consistently, and plot the result. Third, plan small sweeps on subsets, and treat differences smaller than seed variation as ties.

## CTA
Now it is your turn. In the exercise below this video, you will run a small learning-rate sweep with and without a scheduler, and choose the best setting from validation scores. It takes about forty-five minutes. You will use this in your capstone soon. In the next lesson, we track experiments and make them reproducible. See you there.

## Thumbnail
Headline: Tune the Learning Rate First
Image: Navy background, a teal learning-rate curve that ramps up briefly then falls along a smooth cosine, beside a small dial labelled lr, headline in teal Inter Bold.

## Production Notes
- [VERSION] Hugging Face TrainingArguments scheduler and warm-up option names (for example, warmup_ratio is not accepted in some newer versions, while warmup_steps is) must be checked at recording time. The voiceover says only that the names differ between versions.
- [VERSION] Colab free GPU usage limits and session length change; the voiceover says only that sessions can end and limits change.
- run(lr, use_schedule, epochs, seed) is Lars's own helper built from the L10 loop; define it in a cell above the demo before recording and pre-run the 8 runs. No accuracy values are stated (content.md gives none); show the real table.
- Lars and the Bergen salmon-farming company are hypothetical; stock footage must not show a real company name or logo.
