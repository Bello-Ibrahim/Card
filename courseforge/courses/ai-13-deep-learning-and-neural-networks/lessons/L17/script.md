# L17 Tracking Experiments and Reproducibility | Presenter Script

Course: AI-13 · Video: 5 min · Words: 689

## Hook
Two weeks ago, you had a great validation score. Today, you cannot remember the learning rate, the notebook has changed, and the Colab session has ended. The model is gone. Let's make sure that never happens to your capstone.

## Explain
An experiment is only useful if you can find it, compare it and repeat it. Four habits cover most of this. The first is to fix the seeds, for Python, NumPy and PyTorch, at the start of every run. Some GPU operations are not fully deterministic, so tiny differences can remain. And you still run several seeds to measure variation.

The second habit is to put every setting in one config dictionary. Learning rate, batch size, epochs, model name, data subset, dropout, weight decay and seed. The training code reads only from the config, so the config is a complete description of the run.

The third habit is to log every run to a results table. One row per run, with the run name, all config values, the best validation score, the best epoch and the date. A CSV file is enough. Log failed and poor runs too. They are evidence for your report.

The fourth habit is to save checkpoints outside the session. Colab's local disk is deleted when the session ends. Mount Google Drive, and save the best checkpoint there with its config. Check the file size first, because free storage is limited.

Tools like TensorBoard can plot curves for many runs side by side, and hosted tracking services exist too. Check their free plans before you depend on them. For this course, a CSV table and saved plots are enough. And never log personal data or secret keys.

A results table is like a chemist's laboratory notebook. Every attempt is written down, with quantities, temperature and time, including the failures, so anyone can repeat the result. A saved checkpoint is the labelled sample in the fridge.

## Demonstrate
Zanele is a data scientist at a wine producer in Stellenbosch, South Africa. She classifies grape-leaf photos, and she keeps losing work when her Colab session ends. So she adds tracking to her notebook.

First, she mounts Google Drive, approves access, and creates a project folder called ai thirteen. Then she defines a seed function that seeds Python, NumPy and PyTorch, including the GPU.

Next, the config dictionary, with the run name, learning rate, batch size, epochs, dropout, weight decay and seed. She sets the seed from the config, and trains using only values from the config.

After training, she saves the model's weights and the config together in one checkpoint file on Drive. Then she appends one row to the results table, with the config and the best validation accuracy. The file only gets a header the first time, so each new run simply adds a row.

Now the real test. She restarts the runtime, loads the checkpoint back into the model, and evaluates it on the validation split. The score matches the table. This proves the checkpoint, the preprocessing and the code still fit together.

A common mistake is saving only the weights. Without the config, you do not know which transforms, class order or tokenizer the model expects. Save the config, including the class names and preprocessing, with the weights, and test reloading in a fresh session before you trust it. And save only the best checkpoint, or you will fill your storage.

## Recap
Let's recap. First, fix seeds, and keep every setting in one config dictionary, so each run is fully described and repeatable. Second, log every run, including poor ones, to a results table with its config, best score and best epoch. Third, save the best checkpoint with its config to Google Drive, and test reloading it in a fresh session.

## CTA
Now it is your turn. In the exercise below this video, you will log three runs to a results table, save the best checkpoint to Drive, and reload it in a fresh session. It takes about thirty minutes. These habits are the base of your capstone, which starts in the next lesson. Capstone step one, choose a task and build a baseline. See you there.

## Thumbnail
Headline: Never Lose a Model Again
Image: Navy background, a results table with rows of runs, a checkpoint file icon and a cloud drive icon joined by a teal arrow, headline in teal Inter Bold.

## Production Notes
- [VERSION] Check at recording time: Google Colab Drive mounting (google.colab.drive), Google Drive free storage limits, TensorBoard integration, the Trainer report_to option, and the features and free plans of hosted experiment-tracking tools. The voiceover names no hosted tracking service.
- Screen recording: use a clean Google account; the Drive authorisation pop-up must not show personal account details. The folder is MyDrive/ai13.
- best_val_acc and the trained model come from Zanele's own training cell; pre-run it. The reloaded score must match the table row on screen.
- Zanele and the Stellenbosch wine producer are hypothetical; stock footage must not show a real winery name or logo.
