# Screen Demo Pack: AI-19 L08 Measuring Classification Quality

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L08_screen_1.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run the worked-example cell with the labels list, y_true and y_pred
2. Show the printed confusion matrix and classification report
3. Highlight accuracy 0.86 and recall 0.40 for glass and metal

**Narration over this clip (for pacing)**

> In Colab, he prints the confusion matrix and the classification report. Accuracy is zero point eight six. But look at recall. For glass and metal, it is only zero point four zero.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L08_screen_2.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Plot the matrix with ConfusionMatrixDisplay.from_predictions
2. Point to the plastic column: 9 glass and 3 metal items

**Narration over this clip (for pacing)**

> He plots the matrix, and the reason is clear. Nine glass items and three metal items were predicted as plastic. The model has learned to say plastic when it is unsure, because plastic dominates the training data.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L08_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Filter the test images where the true and predicted class differ
2. Show 8 of them in a grid with both labels

**Narration over this clip (for pacing)**

> Numbers tell you which classes fail. To learn why, you look at the images. He filters the wrong predictions and shows eight of them in a grid, with the true and the predicted label on each.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L08_screen_4.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Group the wrong images by likely cause: lighting, angle, blur, hidden, background, label error
2. Count each group and show that 7 of 9 glass errors are strong top lighting

**Narration over this clip (for pacing)**

> Then he groups the wrong images by likely cause and counts each group. Of the nine wrong glass images, seven show clear bottles under strong top lighting, where glass looks shiny, like plastic. So he plans two fixes. More glass images under the belt's real lighting, and class weights, so mistakes on small classes cost more.

## Production notes for this lesson

- [VERSION] scikit-learn functions (confusion_matrix, classification_report, ConfusionMatrixDisplay.from_predictions) and their availability in Colab must be checked at recording time.
- Run outputs: the voiceover states the numbers exactly as content.md reports them from the hand-made example labels: accuracy 0.86, glass recall 0.40, metal recall 0.40, 9 glass and 3 metal items predicted as plastic, 7 of the 9 wrong glass images under strong top lighting. The code cell was run with scikit-learn on these labels; confirm the recorded run prints the same report. These numbers are an illustration, not a benchmark.
- content.md's on-screen steps start by loading the L07 model; for Sipho's example, the demo runs the worked-example cell with the hand-made labels so the printed numbers match. Prepare a set of example item images (plastic, glass, metal, no people, no brand labels) for the grid of wrong predictions.
- Sipho Dlamini and the Durban waste company are fictional; no real company names, logos or bottle brands in footage.
- Screen recording: clean browser profile, no account names or other tabs visible.
