# L08 Measuring Classification Quality | Presenter Script

Course: AI-19 · Video: 5 min · Words: 689

## Hook
A model reports eighty-six percent accuracy. That sounds good, until you learn that it misses most of the glass bottles it was built to find. One number can hide the most important failure. Today, you learn to see what that number hides.

## Explain
In the last lesson, you fine-tuned a model and saw one accuracy number. Accuracy is the share of all predictions that are correct. It is a useful first number, but it treats every image the same.

When one class is much larger than the others, we call the data unbalanced. Then a model can reach high accuracy by doing well on the large class and badly on the small ones.

A confusion matrix shows every combination of true class and predicted class. The rows are the true classes, and the columns are the predictions. The diagonal holds the correct answers. Every cell off the diagonal is a specific kind of mistake, like glass predicted as plastic.

From it, you get two numbers per class. Precision asks, of all the images the model called this class, how many really were? Low precision means false alarms. Recall asks, of all the images that really were this class, how many did the model find? Low recall means missed cases.

Which matters more depends on the cost of each mistake. If a missed diseased leaf can spread to a whole field, focus on recall. If a false alarm stops a production line, focus on precision. The F1 score combines both, and the macro average gives every class the same weight.

Think of a school's overall exam pass rate. A school with ninety percent passes may still fail almost every student in one small class. The confusion matrix is the report for each class, and looking at the wrong images is like talking to the students who failed.

## Demonstrate
Sipho Dlamini builds a recycling sorter for a waste company in Durban, South Africa. His model classifies items on a belt as plastic, glass or metal. His test set has eighty plastic, fifteen glass and five metal items, just like the real belt.

In Colab, he prints the confusion matrix and the classification report. Accuracy is zero point eight six. But look at recall. For glass and metal, it is only zero point four zero.

He plots the matrix, and the reason is clear. Nine glass items and three metal items were predicted as plastic. The model has learned to say plastic when it is unsure, because plastic dominates the training data.

Numbers tell you which classes fail. To learn why, you look at the images. He filters the wrong predictions and shows eight of them in a grid, with the true and the predicted label on each.

Then he groups the wrong images by likely cause and counts each group. Of the nine wrong glass images, seven show clear bottles under strong top lighting, where glass looks shiny, like plastic. So he plans two fixes. More glass images under the belt's real lighting, and class weights, so mistakes on small classes cost more.

A common mistake is to balance the test set by removing images from the large class. The test set should reflect the real data, or your numbers promise results you will not get. Keep a realistic test set, and report precision and recall for each class, plus the macro average. If the small classes matter, balance the training data, or use class weights.

## Recap
Let's recap. First, accuracy can hide poor results on small classes when data is unbalanced, so always check per-class results. Second, the confusion matrix shows which classes are mixed up, precision counts false alarms, and recall counts missed cases. Third, look at the wrong images and group them by cause, to decide what to fix first.

## CTA
Now it is your turn. In the exercise below this video, you will build a confusion matrix for your fine-tuned model, calculate precision and recall, and explain its most common mistake. It takes about thirty minutes. Next week, we find where objects are, not just what they are. Object Detection: Boxes, Classes and IoU. See you there.

## Thumbnail
Headline: What Accuracy Hides
Image: Navy background, a large '86%' in white with a small red-highlighted row of a confusion matrix below it, headline in teal Inter Bold.

## Production Notes
- [VERSION] scikit-learn functions (confusion_matrix, classification_report, ConfusionMatrixDisplay.from_predictions) and their availability in Colab must be checked at recording time.
- Run outputs: the voiceover states the numbers exactly as content.md reports them from the hand-made example labels: accuracy 0.86, glass recall 0.40, metal recall 0.40, 9 glass and 3 metal items predicted as plastic, 7 of the 9 wrong glass images under strong top lighting. The code cell was run with scikit-learn on these labels; confirm the recorded run prints the same report. These numbers are an illustration, not a benchmark.
- content.md's on-screen steps start by loading the L07 model; for Sipho's example, the demo runs the worked-example cell with the hand-made labels so the printed numbers match. Prepare a set of example item images (plastic, glass, metal, no people, no brand labels) for the grid of wrong predictions.
- Sipho Dlamini and the Durban waste company are fictional; no real company names, logos or bottle brands in footage.
- Screen recording: clean browser profile, no account names or other tabs visible.
