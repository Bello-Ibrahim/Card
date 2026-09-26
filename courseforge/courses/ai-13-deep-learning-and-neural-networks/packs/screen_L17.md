# Screen Demo Pack: AI-13 L17 Tracking Experiments and Reproducibility

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L17_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Run: from google.colab import drive; drive.mount("/content/drive") and approve access
2. Run: out_dir = "/content/drive/MyDrive/ai13"; os.makedirs(out_dir, exist_ok=True)
3. Run the set_seed cell: random.seed, np.random.seed, torch.manual_seed, torch.cuda.manual_seed_all

**Narration over this clip (for pacing)**

> First, she mounts Google Drive, approves access, and creates a project folder called ai thirteen. Then she defines a seed function that seeds Python, NumPy and PyTorch, including the GPU.

## Clip 2: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L17_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run the config cell: config = {"run": "cnn_dropout03", "lr": 1e-3, "batch_size": 64, "epochs": 10, "dropout": 0.3, "weight_decay": 1e-2, "seed": 0}; set_seed(config["seed"])
2. Run the training cell that reads only from config

**Narration over this clip (for pacing)**

> Next, the config dictionary, with the run name, learning rate, batch size, epochs, dropout, weight decay and seed. She sets the seed from the config, and trains using only values from the config.

## Clip 3: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L17_screen_3.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Run: torch.save({"model": model.state_dict(), "config": config}, ckpt)
2. Run: pd.DataFrame([{**config, "val_acc": best_val_acc}]).to_csv(table, mode="a", header=not os.path.exists(table), index=False)
3. Open results.csv in the Drive folder and show the new row

**Narration over this clip (for pacing)**

> After training, she saves the model's weights and the config together in one checkpoint file on Drive. Then she appends one row to the results table, with the config and the best validation accuracy. The file only gets a header the first time, so each new run simply adds a row.

## Clip 4: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L17_screen_4.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Runtime > Restart session
2. Re-run imports, drive mount and model definition; run: state = torch.load(ckpt, map_location="cpu"); model.load_state_dict(state["model"])
3. Evaluate on the validation split and compare with val_acc in results.csv

**Narration over this clip (for pacing)**

> Now the real test. She restarts the runtime, loads the checkpoint back into the model, and evaluates it on the validation split. The score matches the table. This proves the checkpoint, the preprocessing and the code still fit together.

## Production notes for this lesson

- [VERSION] Check at recording time: Google Colab Drive mounting (google.colab.drive), Google Drive free storage limits, TensorBoard integration, the Trainer report_to option, and the features and free plans of hosted experiment-tracking tools. The voiceover names no hosted tracking service.
- Screen recording: use a clean Google account; the Drive authorisation pop-up must not show personal account details. The folder is MyDrive/ai13.
- best_val_acc and the trained model come from Zanele's own training cell; pre-run it. The reloaded score must match the table row on screen.
- Zanele and the Stellenbosch wine producer are hypothetical; stock footage must not show a real winery name or logo.
