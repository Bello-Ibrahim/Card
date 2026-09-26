# HeyGen Batch Pack: AI-13 M4 (Tuning, Experiments and the Capstone)

Course: Deep Learning and Neural Networks. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L16 Tuning Hyperparameters and Learning-Rate Schedules

- **Filename:** `ai-13-deep-learning-and-neural-networks_M4_L16_presenter.mp4`
- **Expected length:** about 5.0 minutes (694 words). The quality gate accepts ±10%.

```text
A deep network has dozens of settings you could tune, and your free GPU time is limited. If you can afford only eight training runs, which settings deserve them? For most networks, the answer starts with one number. The learning rate.

Welcome to the last module, where we tune, track and build the capstone. In practice, there is a rough order of importance. First, the learning rate, because it decides whether training works at all. Search it on a log scale, such as one times ten to the minus four, then three times, then ten times, not in equal steps.

Second, batch size and epochs. Batch size is often set by GPU memory, and if you change it a lot, re-check the learning rate. Choose epochs with early stopping, rather than tuning them. Third, regularisation strength. Fourth, model size. Change one group at a time, starting from a known good recipe, such as your run from lesson ten or thirteen.

A learning-rate schedule changes the rate during training. Large steps early make fast progress, and small steps late settle into a good minimum. Step decay divides the rate by ten at fixed epochs. Cosine decay lowers it smoothly to near zero. And warm-up starts small and increases it over the first few percent of steps.

Warm-up avoids large, unstable updates while the new layers are still random, and it is standard when fine-tuning transformers. Most schedulers step once per batch, or once per epoch, depending on how you set their length. Be consistent. The Trainer has its own scheduler settings, and their names differ between versions.

Tuning is like adjusting a new bicycle. First, the saddle height, because nothing else matters if it is wrong. Then the handlebars and gears. A schedule is like changing gear. A strong gear on the flat road at the start, and a gentle one on the steep final hill.

Free sessions can end, and usage limits change. So plan small. Use a data subset and fewer epochs for the sweep, then retrain only the best setting on the full data. And save results after every run.

Lars is an engineer at a salmon-farming company in Bergen, Norway. He classifies fish-health images with the ResNet from lesson ten, and has time for eight short runs.

In Colab, he writes a function that builds a warm-up plus cosine schedule. Warm-up takes the first ten percent of all steps, starting at one tenth of the rate. Cosine decay takes the rest. The scheduler steps after every batch, right after the optimiser.

Then the sweep. Four learning rates, each with and without the schedule. That is eight runs, each for five epochs on a subset, with the same seed. Each run returns its best validation accuracy.

He prints the results as a table, sorted by validation accuracy. Then he plots the learning rate at every step for one scheduled run, to check that the warm-up and the decay look right.

He picks the best setting on validation accuracy. But a difference smaller than the seed variation he measured in lesson fourteen is not a real difference. So he runs the best two settings with two more seeds before he decides.

A common mistake is a huge grid that runs out of GPU time halfway. Another is stepping a scheduler once per epoch when its length was set in batches. The rate hardly changes, and the schedule does nothing. One plot catches it.

Let's recap. First, tune the learning rate first, on a log scale. Then batch size and epochs with early stopping, then regularisation and model size. Second, schedules such as warm-up plus cosine use large steps early and small steps late. Step them consistently, and plot the result. Third, plan small sweeps on subsets, and treat differences smaller than seed variation as ties.

Now it is your turn. In the exercise below this video, you will run a small learning-rate sweep with and without a scheduler, and choose the best setting from validation scores. It takes about forty-five minutes. You will use this in your capstone soon. In the next lesson, we track experiments and make them reproducible. See you there.
```

## L17 Tracking Experiments and Reproducibility

- **Filename:** `ai-13-deep-learning-and-neural-networks_M4_L17_presenter.mp4`
- **Expected length:** about 4.9 minutes (688 words). The quality gate accepts ±10%.

```text
Two weeks ago, you had a great validation score. Today, you cannot remember the learning rate, the notebook has changed, and the Colab session has ended. The model is gone. Let's make sure that never happens to your capstone.

An experiment is only useful if you can find it, compare it and repeat it. Four habits cover most of this. The first is to fix the seeds, for Python, NumPy and PyTorch, at the start of every run. Some GPU operations are not fully deterministic, so tiny differences can remain. And you still run several seeds to measure variation.

The second habit is to put every setting in one config dictionary. Learning rate, batch size, epochs, model name, data subset, dropout, weight decay and seed. The training code reads only from the config, so the config is a complete description of the run.

The third habit is to log every run to a results table. One row per run, with the run name, all config values, the best validation score, the best epoch and the date. A CSV file is enough. Log failed and poor runs too. They are evidence for your report.

The fourth habit is to save checkpoints outside the session. Colab's local disk is deleted when the session ends. Mount Google Drive, and save the best checkpoint there with its config. Check the file size first, because free storage is limited.

Tools like TensorBoard can plot curves for many runs side by side, and hosted tracking services exist too. Check their free plans before you depend on them. For this course, a CSV table and saved plots are enough. And never log personal data or secret keys.

A results table is like a chemist's laboratory notebook. Every attempt is written down, with quantities, temperature and time, including the failures, so anyone can repeat the result. A saved checkpoint is the labelled sample in the fridge.

Zanele is a data scientist at a wine producer in Stellenbosch, South Africa. She classifies grape-leaf photos, and she keeps losing work when her Colab session ends. So she adds tracking to her notebook.

First, she mounts Google Drive, approves access, and creates a project folder called ai thirteen. Then she defines a seed function that seeds Python, NumPy and PyTorch, including the GPU.

Next, the config dictionary, with the run name, learning rate, batch size, epochs, dropout, weight decay and seed. She sets the seed from the config, and trains using only values from the config.

After training, she saves the model's weights and the config together in one checkpoint file on Drive. Then she appends one row to the results table, with the config and the best validation accuracy. The file only gets a header the first time, so each new run simply adds a row.

Now the real test. She restarts the runtime, loads the checkpoint back into the model, and evaluates it on the validation split. The score matches the table. This proves the checkpoint, the preprocessing and the code still fit together.

A common mistake is saving only the weights. Without the config, you do not know which transforms, class order or tokenizer the model expects. Save the config, including the class names and preprocessing, with the weights, and test reloading in a fresh session before you trust it. And save only the best checkpoint, or you will fill your storage.

Let's recap. First, fix seeds, and keep every setting in one config dictionary, so each run is fully described and repeatable. Second, log every run, including poor ones, to a results table with its config, best score and best epoch. Third, save the best checkpoint with its config to Google Drive, and test reloading it in a fresh session.

Now it is your turn. In the exercise below this video, you will log three runs to a results table, save the best checkpoint to Drive, and reload it in a fresh session. It takes about thirty minutes. These habits are the base of your capstone, which starts in the next lesson. Capstone step one, choose a task and build a baseline. See you there.
```

## L18 Capstone Step 1: Choose a Task and Build a Baseline

- **Filename:** `ai-13-deep-learning-and-neural-networks_M4_L18_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
The most common reason capstone projects fail is not a bad model. It is a dataset you cannot use, a task with no clear measure of success, or no simple result to compare with. This week, you fix all three.

Your capstone has three steps. Choose and baseline, today. Experiment and choose, in the next lesson. And document, in the final lesson. Today's step has four parts.

First, choose a task. It must be image or text classification, with a clear set of labels. Plant diseases, product categories, support-ticket topics or review sentiment. Keep it small enough for free GPU time. A few thousand examples is plenty, and you can use a subset.

Second, choose a public dataset with a clear licence. Read the dataset card. Check the licence and whether it allows your use, the source, and how the labels were made. Avoid personal data, such as faces, names, health records or private messages. And if there is no validation split, create one with a fixed seed.

Third, build a baseline. That is the simplest reasonable model, trained quickly, that gives you a score to beat. For text, TF-IDF with logistic regression from the scikit-learn course is strong. For images, a small CNN, or a frozen pretrained backbone with a new head. Log it in your results table.

Fourth, write an experiment plan with at least three experiments. Each has a hypothesis, the one change you will make, and the metric that decides. Use macro F1 when classes are unbalanced, and accuracy when they are balanced and all errors cost the same.

A baseline is like the time a runner records on the first day of training. Without it, a later time of fifty-two minutes means nothing. With it, the runner knows whether the new plan actually helped.

Fatima is a data scientist at a telecoms company in Dakar, Senegal. For her capstone, she chooses public English customer reviews with three sentiment labels. She does not use her employer's customer messages.

She starts on the dataset card. She reads the licence, which allows educational use, and the label description, and writes both into a text cell in her notebook, before any code.

Then she loads the data, and splits off twenty percent of the training set for validation, with a fixed seed. She prints the label names and counts to check the class balance.

Now the baseline. A TF-IDF vectoriser with single words and word pairs, and a balanced logistic regression. She fits it on the training text, and scores macro F1 on the validation split. It takes seconds on a CPU.

She adds the baseline row to her results table, with its config. Then she writes her plan. One, fine-tune a small pretrained encoder with default settings. Two, the same with a learning-rate sweep and warm-up. Three, the best setting with a longer maximum length, because some reviews are long. The test split is not touched.

A common mistake is skipping the baseline, because it will obviously lose. Sometimes it does not. On short texts, TF-IDF can come close to a transformer, at a tiny fraction of the cost. Without a baseline, you cannot show that your deep model is worth it.

Another mistake is choosing a dataset first, and checking the licence later, when changing is expensive. Check it before you write any code.

Let's recap. First, choose an image or text classification task, with a public dataset whose licence, source and content you have checked, and no personal data. Second, build a fast baseline and log it. It is the score every later experiment must beat. Third, write a plan with at least three experiments, each with a hypothesis, one change and a decision metric.

Now it is your turn. This is capstone step one. In the exercise below this video, you will choose your dataset, train a baseline, and write an experiment plan with at least three experiments. The capstone rubric is on the course page. It takes about an hour. In the next lesson, capstone step two, fine-tune and compare. See you there.
```

## L19 Capstone Step 2: Fine-Tune and Compare

- **Filename:** `ai-13-deep-learning-and-neural-networks_M4_L19_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
You have a baseline and a plan. This week, you train several models, and one will look best. The hard part is not training them. It is saying honestly that the winner really is better, and then testing it exactly once.

Run your plan in order. Start with the experiment most likely to give a large gain, usually a pretrained model. A ResNet for images, or a small encoder from the Hub for text. Then add regularisation and tuning, one change at a time.

After each run, log a row to your results table, and write one line in your plan. Was the hypothesis supported? Keep failed runs too. They are evidence for your report. Also record the name and licence of every pretrained checkpoint you use.

Compare fairly. Every run must use the same validation split and preprocessing, and the same main metric, computed the same way. Budgets must be comparable, or noted. And the leading candidates need more than one seed.

Choose the final model on validation data, and justify it. The best score is not the only reason. If two models are within seed variation, prefer the smaller, faster or simpler one. Then, and only then, evaluate it once on the test split. If you change the model after seeing the test result, the test score is no longer honest, and you must say so.

It is like judging a cooking competition. Every chef cooks the same dish, with the same ingredients and time, for the same judges. The final public tasting happens once. If a chef could taste the judges' plate and then cook again, it would not be fair.

Diego is an engineer at an avocado exporter in Uruapan, Mexico. His capstone classifies leaf photos into four classes, from a public dataset with a confirmed licence. His baseline is a small CNN trained from scratch.

In Colab, he loads his results table from Drive, so nothing is lost when a session ends. It has four runs. The baseline CNN, a frozen ResNet eighteen with a new head, the same with its last block fine-tuned, and the fine-tuned model with a learning-rate schedule.

He reruns the top two with two more seeds. Then he groups the table by run, and shows the mean, the spread and the count of validation F1, sorted from best to worst. Two extra seeds per run is a small cost for an honest comparison.

The two fine-tuned runs are within seed variation of each other. So Diego chooses the version without the schedule, because it is simpler and equally good. He writes that reason next to the table, before he touches the test set.

Now he reloads the chosen checkpoint, and evaluates it on the test set, exactly once. He copies the number into his report, and does not change the model afterwards. If he changed it now, the test score would no longer be an honest estimate.

A common mistake is evaluating every candidate on the test set, just to see, and then picking the best test score. This makes the test set a second validation set, and the reported score is too optimistic. Another is comparing runs with different validation splits, for example because the split was made without a fixed seed. Check the split is identical across all runs.

Let's recap. First, run planned experiments one change at a time, starting with a pretrained model, and log every run with its config. Second, compare on the same validation split and metric, use extra seeds for the leaders, and prefer the simpler model when results are within seed variation. Third, evaluate the chosen model once on the test set, and report that number without further changes.

Now it is your turn. This is capstone step two. In the exercise below this video, you will run at least three tracked experiments, choose your final model, and evaluate it once on the test set. Check your work against the capstone rubric. It takes about ninety minutes. In the final lesson, capstone step three, you document your experiments. See you there.
```

## L20 Capstone Step 3: Document Your Experiments

- **Filename:** `ai-13-deep-learning-and-neural-networks_M4_L20_presenter.mp4`
- **Expected length:** about 5.0 minutes (694 words). The quality gate accepts ±10%.

```text
Imagine a colleague opens your capstone notebook six months from now. Can they tell what the model is for, what data it learned from, how you chose it, and where it fails? If not, it is much less useful than its score suggests.

This final step turns your experiments into something other people can trust and repeat. Your report follows the style of a model card, a short, structured document that travels with a model. It has eight sections, in this order.

First, the summary and intended use. The task, the classes, and who might use it for what. Also state what it is not for, such as medical or legal decisions. Second, the data. Its name, source, licence, split sizes, class balance, how labels were made, and known gaps, such as one region or one camera type.

Third, the method. The baseline and the final architecture, the pretrained checkpoint and its licence, and the full training setup. Fourth, the experiments table, with one row per run, the validation metric with mean and spread, and whether the hypothesis was supported. Fifth, the results. The final validation score, the single test score, and a confusion matrix.

Sixth, error analysis, with the main error patterns and two or three short, non-personal examples. Seventh, limitations and risks. Where the model is likely to fail, possible bias, and what to check before real use. Eighth, reproducibility. Library versions, how to run the notebook from the start, where the checkpoint is, and the expected runtime.

A model card is like the leaflet inside a medicine box. It says what the medicine is for, how it was tested, the dose, the side effects, and who should not take it. Nobody would trust a medicine without one.

Elif is an engineer at a carpet manufacturer in Gaziantep, Türkiye. Her capstone classifies weaving defects from public textile images with a confirmed licence. Her first draft has a strong results section, but only one sentence on data, and nothing on limits.

She revises it section by section. In the data section, she adds that all images come from one type of camera and lighting, and that one defect class has far fewer examples.

In the experiments section, she pastes her results table. The baseline CNN, the frozen ResNet, the fine-tuned ResNet, and the fine-tuned model with a schedule, each with validation macro F1 over three seeds.

Her error analysis shows that most errors are between two defect types that look similar at low resolution. And under limitations, she writes that the model has not been tested on photos from factory cameras, and should not reject products without human review.

Before sharing, she restarts the runtime and runs every cell from the top. There are no secret keys in the code. A colleague then runs it on a CPU with the small subset, and gets a validation score within the seed range in her table.

Optionally, you can share your model and its card on the Hugging Face Hub. Upload steps change, so follow the current Hub documentation, and upload only models trained on data whose licence allows it.

A common mistake is writing the report as a success story, with only the final score, no failed runs and no limits. That makes the work less credible, not more. Reviewers trust a report that shows what did not work, and why the final choice was made. And always test your shared notebook with restart and run all.

Let's recap. First, structure the report like a model card, with intended use, data, method, experiments, results, error analysis, limitations and reproducibility. Second, take every number from your results table or notebook outputs, and include failed runs and known limits. Third, share a notebook that runs from the start with no secrets in the code, and check licences before any public upload.

Congratulations. You have gone from tensors to a fine-tuned, documented neural network. For capstone step three, write your experiment report and share your notebook so someone else can run it from the start. It takes about an hour. Then check the rubric, and submit your capstone on the course page. Well done, and good luck.
```
