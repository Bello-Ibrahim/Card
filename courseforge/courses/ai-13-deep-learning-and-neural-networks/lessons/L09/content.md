# L09 Regularisation: Dropout, Weight Decay and Early Stopping

Course: AI-13 · Module: M2 · Objectives: O5, O6 · Video: 5 min (screen demo)

## Hook
In L08, the validation loss started to rise while the training loss kept falling. Your model was learning the training set too well. Today you add three tools that make it learn less about the details and more about the pattern, and you check whether each one really helps.

## Explanation
**Regularisation** is any change that makes a model generalise better to new data, usually at some cost to its training score. In AI-12 you met L2 penalties for linear models. Deep networks use the same idea plus a few of their own.

**Dropout** (`nn.Dropout(p)`) randomly sets a fraction `p` of activations to zero in each training step and scales the rest up, so the expected value stays the same. The network cannot rely on any single unit, so it learns more robust, spread-out features. Dropout is active only in `model.train()` mode; in `model.eval()` mode it does nothing (L05). Typical values are 0.1 to 0.5, usually placed before fully connected layers.

**Weight decay** shrinks every weight a little at each step, which keeps weights small and the function smoother. It is the deep-learning version of an L2 penalty. With Adam, use `torch.optim.AdamW(params, lr, weight_decay=...)`, which applies decay separately from the adaptive step. Common starting values are around `1e-4` to `1e-2`; tune them on validation data.

**Early stopping** watches the validation loss after every epoch, saves a copy of the weights whenever it improves, and stops when it has not improved for `patience` epochs. You then reload the best copy. It is simple, and it also saves GPU time.

**Data augmentation** (L06) is also a regulariser, and often the strongest one for images.

**Analogy:** A student who practises with one set of past exam questions can memorise the answers and still fail a new exam. A student who practises with different question sets, sometimes with parts of the question hidden, has to learn the method. Dropout hides parts of the input, weight decay stops the student from building very complicated rules, and early stopping is the teacher saying "stop now, you are starting to memorise".

## Worked Example
Hamid is an ML engineer at a hypothetical argan-oil cooperative in Agadir, Morocco. His quality-check CNN overfits after a few epochs. He adds dropout and weight decay, and wraps the loop from L05 with early stopping.

**Screen demo steps:**

1. Add a dropout layer before the classifier.
2. Switch the optimiser to AdamW with weight decay.
3. Add the early-stopping block after the validation pass and reload the best weights at the end.

```python
import copy, torch
from torch import nn

model = nn.Sequential(
    nn.Conv2d(1, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
    nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
    nn.Flatten(), nn.Dropout(0.3), nn.Linear(64 * 7 * 7, 10),
)
opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)

best_loss, best_state, patience, bad_epochs = float("inf"), None, 3, 0
for epoch in range(30):
    train_one_epoch(model, opt)            # your loop from L05
    val_loss = evaluate(model)             # mean validation loss, eval() + no_grad()
    if val_loss < best_loss:
        best_loss, bad_epochs = val_loss, 0
        best_state = copy.deepcopy(model.state_dict())
    else:
        bad_epochs += 1
        if bad_epochs >= patience:
            print("stopping at epoch", epoch); break
model.load_state_dict(best_state)
```

Hamid runs two experiments with the same data, seed and learning rate: the original model, and the regularised model. He plots both validation curves on one chart. The expected result is that the regularised model's validation loss stays lower for longer and the gap between training and validation loss becomes smaller. He compares the best validation scores, not the final ones, and records both runs in a small table.

## Common Mistake
Many learners save the best model with `best_state = model.state_dict()`. This does not copy the weights; it stores references to the live tensors, which keep changing as training continues. At the end, "best" is simply the last model. Use `copy.deepcopy(model.state_dict())`, or save to a file with `torch.save`. A second mistake is adding every regulariser at once with strong settings. The model may then underfit, and you cannot tell which change helped. Add them one at a time and compare the curves.

## Key Takeaways
1. Dropout randomly switches off units during training only; weight decay keeps weights small; both reduce overfitting at some cost to training fit.
2. Early stopping keeps the checkpoint with the best validation loss and stops after a set number of epochs without improvement; save a real copy of the weights.
3. Judge regularisation by comparing validation curves and best validation scores across runs that change one thing at a time.

## Hands-on Exercise
**Task:** Add dropout and weight decay to your CNN, use early stopping, and compare validation curves before and after.
**Tools:** Google Colab with a GPU runtime (free; optional), or CPU with a 10,000-image subset; PyTorch; your CNN and loop from L07.
**Steps:**
1. Fix the random seed with `torch.manual_seed(0)` so that both runs start the same way.
2. Run the original CNN for 15 epochs and save its training and validation losses.
3. Add `nn.Dropout(0.3)` before the final linear layer, switch to `AdamW` with `weight_decay=1e-2`, and add early stopping with a patience of 3.
4. Train again and reload the best checkpoint at the end.
5. Plot both validation curves on one chart and fill a table: run, best epoch, best validation loss, best validation accuracy.
6. Write three sentences: did regularisation help, by how much, and what would you try next?
**What good looks like:** Two comparable runs with the same seed and data, a correct deep copy of the best weights, a clear comparison chart, and a conclusion based on the numbers you measured.
**Time:** about 40 minutes

## Review Flags
- None. The lesson uses stable, core PyTorch features and a hypothetical example; the suggested hyperparameter ranges are starting points for tuning, not claims about results.
