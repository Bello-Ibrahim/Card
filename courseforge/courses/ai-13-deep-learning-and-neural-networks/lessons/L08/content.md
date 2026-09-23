# L08 Reading Learning Curves

Course: AI-13 · Module: M2 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
Your model finished training with a validation accuracy you do not like. You could change ten settings at random, or you could look at one chart for thirty seconds and know which setting to change first. That chart is the learning curve.

## Explanation
A **learning curve** plots the training loss and the validation loss after every epoch, on the same axes. In AI-12 you used learning curves with training-set size on the x-axis; here the x-axis is epochs. Plot loss rather than accuracy first, because loss changes smoothly and shows problems earlier.

Four patterns cover most cases:

- **Healthy:** both losses fall and then flatten, with a small gap. More epochs will not help much; a larger model or better data might.
- **Overfitting:** training loss keeps falling, but validation loss reaches a minimum and then rises. The curves separate. The model is memorising the training set. Fixes: more data or augmentation, regularisation (L09), a smaller model, or stopping earlier.
- **Underfitting:** both losses stay high and close together. The model cannot fit even the training data. Fixes: a larger model, more epochs, a higher learning rate, or better features and inputs.
- **Learning rate too high:** the loss jumps up and down, grows, or becomes NaN. Fix: lower the learning rate, often by a factor of 3 to 10 (L15, L16).

Two more signals are useful. If the training loss is **flat from the start**, check the loop: zero_grad, the optimiser's parameter list, and whether the model is frozen. If the validation loss is **lower than the training loss**, this is often normal when dropout or strong augmentation is active during training only.

Always change **one thing at a time** after a diagnosis, and keep the old curve for comparison.

**Analogy:** Learning curves are like a patient's temperature chart in a hospital. One reading tells you little. The shape over several days tells the doctor whether the treatment is working, whether the patient is getting worse, or whether the thermometer is broken.

## Worked Example
Svetlana is an ML engineer at a hypothetical agricultural insurer in Almaty, Kazakhstan. She trained the CNN from L07 on a 10,000-image subset of Fashion-MNIST for 20 epochs and saved the per-epoch losses in two lists.

**Screen demo steps:**

1. Plot both losses on one chart with a legend.
2. Mark the epoch with the lowest validation loss.
3. Read the pattern and write a diagnosis.

```python
import matplotlib.pyplot as plt

def plot_curves(train_loss, val_loss, title=""):
    epochs = range(1, len(train_loss) + 1)
    best = min(range(len(val_loss)), key=val_loss.__getitem__)
    plt.plot(epochs, train_loss, label="train")
    plt.plot(epochs, val_loss, label="validation")
    plt.axvline(best + 1, linestyle="--", color="grey")
    plt.xlabel("epoch"); plt.ylabel("loss"); plt.title(title); plt.legend(); plt.show()
    return best + 1

best_epoch = plot_curves(history["train_loss"], history["val_loss"], "CNN, 10k images")
```

Svetlana's curves show the training loss falling steadily to a low value. The validation loss falls until about epoch 6 and then rises slowly, while validation accuracy stays almost flat. Her diagnosis: overfitting after epoch 6. The small training subset makes this more likely. The model at epoch 6 is better than the final one, even though its training loss is higher.

She decides on one change first: add augmentation to the training transform. She keeps the old curve, trains again, and compares. Adding dropout, weight decay and early stopping comes in L09.

Note what she did not do: she did not change the learning rate, because nothing in the curves suggested it was a problem.

## Common Mistake
Many learners look only at the final validation accuracy, or only at the training loss. The final epoch is often not the best one, and a falling training loss says nothing about new data. Another mistake is reading one noisy epoch as a trend. Small validation sets make the curve jumpy; look at the direction over several epochs, and consider a larger validation set before reacting. Finally, do not use the test set to draw learning curves. Every decision you make from a curve uses up that data's value as an unbiased check (L14).

## Key Takeaways
1. Plot training and validation loss per epoch on one chart; loss shows problems earlier and more smoothly than accuracy.
2. Separating curves mean overfitting, two high curves mean underfitting, and jumping or growing loss usually means the learning rate is too high.
3. Diagnose first, then change one thing at a time, and keep the old curve for comparison.

## Hands-on Exercise
**Task:** Diagnose 4 provided learning curves, then plot your own CNN's curves and write a one-paragraph diagnosis.
**Tools:** Google Colab (free); matplotlib; your saved histories from L05 and L07. The 4 curves are provided as images on the course page.
**Steps:**
1. Look at curves A to D on the course page. For each, write the pattern name and one fix.
2. Check your answers with the key: A is overfitting (validation loss rises after an early minimum), B is underfitting (both losses flat and high), C is a learning rate that is too high (loss jumps and then grows), D is healthy (both fall and flatten with a small gap).
3. Plot your own CNN's training and validation loss from L07 with the `plot_curves` function and mark the best epoch.
4. Write one paragraph: the pattern you see, the evidence for it, the best epoch, and the single change you would try next.
5. Optional: make the change, train again, and plot the two validation curves together.
**What good looks like:** Correct labels for A to D, a clear chart with a legend and the best epoch marked, and a diagnosis that points to specific evidence in the curve and proposes one targeted change.
**Time:** about 30 minutes

## Review Flags
- None. The lesson teaches general diagnostic patterns with a hypothetical example and no specific facts or version-sensitive APIs; the 4 provided curve images must be produced by the course team to match the answer key.
