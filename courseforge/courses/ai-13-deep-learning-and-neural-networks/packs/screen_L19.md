# Screen Demo Pack: AI-13 L19 Capstone Step 2: Fine-Tune and Compare

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-13-deep-learning-and-neural-networks_L19_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Run: runs = pd.read_csv("/content/drive/MyDrive/ai13/results.csv")
2. Show the four runs: baseline CNN, frozen ResNet-18, resnet18_ft_layer4, fine-tuned + schedule

**Narration over this clip (for pacing)**

> In Colab, he loads his results table from Drive, so nothing is lost when a session ends. It has four runs. The baseline CNN, a frozen ResNet eighteen with a new head, the same with its last block fine-tuned, and the fine-tuned model with a learning-rate schedule.

## Clip 2: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L19_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run the top two settings with 2 more seeds each; new rows appear in results.csv
2. Run: summary = runs.groupby("run")["val_f1"].agg(["mean", "std", "count"]).sort_values("mean", ascending=False); print(summary)

**Narration over this clip (for pacing)**

> He reruns the top two with two more seeds. Then he groups the table by run, and shows the mean, the spread and the count of validation F1, sorted from best to worst. Two extra seeds per run is a small cost for an honest comparison.

## Clip 3: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L19_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Highlight the two fine-tuned rows and their overlapping ranges
2. Add a text cell: Final choice: resnet18_ft_layer4 (no schedule). Reason: within seed variation of the scheduled run, and simpler.

**Narration over this clip (for pacing)**

> The two fine-tuned runs are within seed variation of each other. So Diego chooses the version without the schedule, because it is simpler and equally good. He writes that reason next to the table, before he touches the test set.

## Clip 4: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L19_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Run once: final = load_checkpoint("resnet18_ft_layer4"); test_f1 = evaluate(final, test_dl); print("TEST macro F1:", round(test_f1, 3))
2. Copy the printed test score into the report draft

**Narration over this clip (for pacing)**

> Now he reloads the chosen checkpoint, and evaluates it on the test set, exactly once. He copies the number into his report, and does not change the model afterwards. If he changed it now, the test score would no longer be an honest estimate.

## Production notes for this lesson

- [VERIFY] Licences and intended uses of all pretrained checkpoints used (for example ImageNet-pretrained torchvision weights and Hub encoders) must be recorded; the course page should link to where to find them. Diego's leaf dataset must be one of the course team's confirmed-licence examples; show its card.
- No scores are stated in the voiceover (content.md gives none). Show the real summary table and the single test result; do not add numbers in captions.
- load_checkpoint and evaluate are Diego's own helpers from L17 and L05; define them above the demo cell. Record the test cell being run exactly once.
- Diego and the Uruapan avocado exporter are hypothetical; stock footage must not show a real company name or logo.
