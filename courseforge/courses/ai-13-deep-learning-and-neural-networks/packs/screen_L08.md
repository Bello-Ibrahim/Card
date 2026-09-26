# Screen Demo Pack: AI-13 L08 Reading Learning Curves

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L08_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Run the plot_curves cell from content.md: plot train_loss and val_loss against epochs, best = epoch with lowest val_loss, plt.axvline(best + 1, linestyle="--", color="grey"), legend, return best + 1
2. Highlight the axvline line

**Narration over this clip (for pacing)**

> In Colab, she writes a small plotting function. It draws both losses with a legend, finds the epoch with the lowest validation loss, and marks it with a dashed grey line.

## Clip 2: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L08_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run: best_epoch = plot_curves(history["train_loss"], history["val_loss"], "CNN, 10k images")
2. Point to the training line falling, the validation minimum near epoch 6 and the dashed marker

**Narration over this clip (for pacing)**

> She calls it with her saved history. The training loss falls steadily to a low value. The validation loss falls until about epoch six, then rises slowly, while validation accuracy stays almost flat.

## Clip 3: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L08_screen_3.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Add a text cell under the chart: Diagnosis: overfitting after epoch 6; small subset; epoch-6 model is the best
2. Print best_epoch

**Narration over this clip (for pacing)**

> Her diagnosis is overfitting after epoch six, made more likely by the small training set. The model at epoch six is better than the final one, even though its training loss is higher.

## Clip 4: scene 13

- **Filename:** `ai-13-deep-learning-and-neural-networks_L08_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Add RandomHorizontalFlip and RandomCrop(28, padding=2) to the training transform (from L06)
2. Retrain and plot the old and new validation curves on one chart

**Narration over this clip (for pacing)**

> She makes one change first. She adds augmentation to the training transform, keeps the old curve, trains again, and compares. Note what she does not do. She does not touch the learning rate, because nothing in the curves pointed to it.

## Production notes for this lesson

- Review flags: none. Use the course team's images assets/L08_curve_A.png to assets/L08_curve_D.png for the four patterns, matching the exercise answer key: A overfitting, B underfitting, C learning rate too high, D healthy.
- The four curve slides show the pattern name only in the voiceover and caption; the exercise uses the same images without labels, so the course page must show them unlabelled.
- Svetlana's demo needs a saved history dictionary from a 20-epoch CNN run on a 10,000-image Fashion-MNIST subset. Record a run whose validation loss has its minimum near epoch 6, as content.md describes, or change the voiceover to the actual best epoch.
- Svetlana and the Almaty insurer are hypothetical; stock footage must not show a real company name or logo.
