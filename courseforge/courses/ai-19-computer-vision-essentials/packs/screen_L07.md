# Screen Demo Pack: AI-19 L07 Transfer Learning: Fine-Tuning on Your Own Images

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L07_screen_1.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open Runtime, then Change runtime type
2. Select a GPU if one is available and save

**Narration over this clip (for pacing)**

> First, in Colab, she opens the runtime settings and chooses a GPU, if one is available. Training is much faster on a GPU. If none is free today, the same code still runs on the processor, only more slowly.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L07_screen_2.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Scroll through the cell: load_dataset, class names, AutoImageProcessor, AutoModelForImageClassification with num_labels
2. Highlight the loop that sets requires_grad = False on model.base_model.parameters()

**Narration over this clip (for pacing)**

> Then she walks through the cell. It loads the dataset and the class names, loads a pre-trained vision model with a new head for three classes, and prepares each image the way the model expects. Here is the key line. A short loop freezes every backbone parameter, so only the new head will learn.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L07_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run the cell
2. Point to the printed 'before' accuracy
3. Show the training loss decreasing over the 3 epochs

**Narration over this clip (for pacing)**

> She runs it. Before training, the new head is untrained, so the test accuracy is close to guessing, about one in three. You'll see something like zero point three four. Then the training starts, and the loss goes down, epoch by epoch.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L07_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Point to the printed 'after' accuracy
2. Run trainer.save_model() and show the saved folder in the file panel

**Narration over this clip (for pacing)**

> After three epochs, the test accuracy is a clearly higher number. Your numbers will differ, and they are not a benchmark. Finally, she saves the model, because she will measure it properly in the next lesson.

## Production notes for this lesson

- [VERIFY] The bean leaf dataset: Hub ID AI-Lab-Makerere/beans, its licence, column names image and labels, and that it was collected in Uganda. The voiceover says only 'a public bean leaf photo dataset' and does not state where it was collected or where it is hosted.
- [VERIFY] The recommended way to save a model from Colab (Google Drive mount or push to the Hub). The voiceover only says 'saves the model', matching the trainer.save_model() screen step.
- [VERSION] Google Colab GPU availability, session limits and the Runtime menu path change and are not guaranteed. The voiceover says 'a GPU, if one is available'.
- [VERSION] Hugging Face transformers and datasets APIs (TrainingArguments arguments, with_transform, base_model) and the checkpoint ID google/vit-base-patch16-224-in21k. Code was checked for syntax only.
- Run outputs: content.md gives 'before: 0.34' only as example output and no exact 'after' value. The voiceover says 'you'll see something like zero point three four' and 'a clearly higher number'. Do not add an on-screen caption with a specific after value.
- Grace Namukasa and the Mbale advice service are fictional. Stock footage of bean plants must show no identifiable farmers.
- Screen recording: clean browser profile, no account names or other tabs visible.
