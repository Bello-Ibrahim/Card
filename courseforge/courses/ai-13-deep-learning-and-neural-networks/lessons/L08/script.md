# L08 Reading Learning Curves | Presenter Script

Course: AI-13 · Video: 5 min · Words: 675

## Hook
Your model finished training, and you do not like the score. You could change ten settings at random. Or you could look at one chart for thirty seconds, and know which setting to change first. That chart is the learning curve.

## Explain
In the scikit-learn course, your learning curves had training-set size on the x-axis. Here, the x-axis is epochs. A learning curve plots the training loss and the validation loss after every epoch, on the same axes. Plot loss before accuracy, because loss changes smoothly and shows problems earlier.

Four patterns cover most cases. In a healthy run, both losses fall and then flatten, with a small gap. More epochs will not help much. A larger model or better data might.

In overfitting, training loss keeps falling, but validation loss reaches a low point and then rises. The curves separate, because the model is memorising the training set. Fixes include more data or augmentation, regularisation, a smaller model, or stopping earlier.

In underfitting, both losses stay high and close together. The model cannot fit even the training data. Try a larger model, more epochs, a higher learning rate, or better inputs.

When the learning rate is too high, the loss jumps up and down, grows, or becomes not a number. Lower the learning rate, often by three to ten times.

Two more signals. If the training loss is flat from the start, check the loop itself. Is zero grad there? Does the optimiser have the right parameters? Is the model frozen? And if validation loss is lower than training loss, that is often normal when dropout or strong augmentation runs during training only.

Learning curves are like a patient's temperature chart. One reading tells you little. The shape over several days tells the doctor whether the treatment is working, whether the patient is getting worse, or whether the thermometer is broken.

## Demonstrate
Svetlana is an engineer at an agricultural insurer in Almaty, Kazakhstan. She trained the CNN from lesson seven on ten thousand Fashion-MNIST images for twenty epochs, and saved the losses from each epoch in two lists.

In Colab, she writes a small plotting function. It draws both losses with a legend, finds the epoch with the lowest validation loss, and marks it with a dashed grey line.

She calls it with her saved history. The training loss falls steadily to a low value. The validation loss falls until about epoch six, then rises slowly, while validation accuracy stays almost flat.

Her diagnosis is overfitting after epoch six, made more likely by the small training set. The model at epoch six is better than the final one, even though its training loss is higher.

She makes one change first. She adds augmentation to the training transform, keeps the old curve, trains again, and compares. Note what she does not do. She does not touch the learning rate, because nothing in the curves pointed to it.

A common mistake is looking only at the final accuracy, or only at training loss. The final epoch is often not the best one, and a falling training loss says nothing about new data. Another mistake is reading one noisy epoch as a trend. Look at the direction over several epochs.

And never draw learning curves on the test set. Every decision you make from it uses up its value as a fair check.

## Recap
Let's recap. First, plot training and validation loss per epoch on one chart. Second, separating curves mean overfitting, two high curves mean underfitting, and jumping or growing loss usually means the learning rate is too high. Third, diagnose first, then change one thing at a time after each diagnosis, and keep the old curve for comparison.

## CTA
Now it is your turn. In the exercise below this video, you will diagnose four learning curves, labelled A to D, then plot your own CNN's curves and write a one-paragraph diagnosis. It takes about thirty minutes. In the next lesson, we fight overfitting with dropout, weight decay and early stopping. See you there.

## Thumbnail
Headline: Read the Curve First
Image: Navy background, two loss curves on one chart, a teal training line falling and a white validation line rising after an early low point marked with a dashed line, headline in teal Inter Bold.

## Production Notes
- Review flags: none. Use the course team's images assets/L08_curve_A.png to assets/L08_curve_D.png for the four patterns, matching the exercise answer key: A overfitting, B underfitting, C learning rate too high, D healthy.
- The four curve slides show the pattern name only in the voiceover and caption; the exercise uses the same images without labels, so the course page must show them unlabelled.
- Svetlana's demo needs a saved history dictionary from a 20-epoch CNN run on a 10,000-image Fashion-MNIST subset. Record a run whose validation loss has its minimum near epoch 6, as content.md describes, or change the voiceover to the actual best epoch.
- Svetlana and the Almaty insurer are hypothetical; stock footage must not show a real company name or logo.
