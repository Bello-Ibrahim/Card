# L15 Common Training Problems and Fixes

Course: AI-13 · Module: M3 · Objectives: O5 · Video: 6 min (screen demo)

## Hook
Your loss prints `nan` at step 8. Or the loss never moves. Or the GPU runs out of memory after ten minutes. Each looks like a disaster, but most have a small number of causes, and you can check them in a fixed order.

## Explanation
**NaN or exploding loss.** The loss grows quickly, becomes `inf`, then `nan`. Usual causes: a learning rate that is too high, unnormalised inputs with large values, or an invalid operation such as `log(0)`. Fixes: normalise inputs, lower the learning rate, and add **gradient clipping**, which scales the gradients down when their total norm is above a limit: `torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)` between `backward()` and `step()`.

**Vanishing gradients.** The loss hardly moves, and the early layers' gradients are close to zero. In deep stacks, gradients are multiplied layer by layer on the way back (L04); saturating activations such as sigmoid make each factor small. Fixes: ReLU-family activations, normalisation layers (`BatchNorm`, `LayerNorm`), residual connections, or a shallower model. **Diagnose by printing the gradient norm of each layer.**

**Wrong loss for the label shape.** `CrossEntropyLoss` wants logits `(N, C)` and integer labels `(N,)`. `BCEWithLogitsLoss` wants logits and float labels of the same shape. Mismatches give an error, or worse, silent broadcasting.

**GPU out-of-memory (OOM).** Fixes: a smaller batch size; **mixed precision**, which runs most operations in 16-bit floats; and not keeping graphs alive by accident. [VERSION]

```python
scaler = torch.amp.GradScaler("cuda")
with torch.autocast(device_type="cuda", dtype=torch.float16):
    loss = loss_fn(model(xb), yb)
scaler.scale(loss).backward(); scaler.step(opt); scaler.update()
```

**Debugging checklist:** (1) Read the full error and print shapes, dtypes and devices. (2) Overfit one small batch: a correct model and loop can reach near-zero loss on 32 examples. (3) Check the loss and label format. (4) Lower the learning rate by 10. (5) Print gradient norms. (6) Check memory use per step.

**Analogy:** Debugging training is like a mechanic diagnosing a car that will not start. A good mechanic does not replace the engine first. They check the fuel, then the battery, then the spark plugs, in a fixed order, from the cheapest check to the most expensive.

## Worked Example
Nguyen Thi Hoa is an ML engineer at a hypothetical logistics firm in Da Nang, Vietnam. She inherits four broken notebooks. Each has a symptom, a cause and a fix.

**Screen demo steps:** run each broken cell, show the symptom, apply the fix, run again.

**Notebook A: loss becomes NaN.**
```python
X = torch.rand(512, 5) * 5000                   # raw values in the thousands
y = X @ torch.tensor([0.2, 0.1, 0.05, 0.3, 0.1])
model = nn.Linear(5, 1); opt = torch.optim.SGD(model.parameters(), lr=0.01)
```
Cause: unscaled inputs make gradients huge, so each step overshoots. Fix: standardise `X` and `y`, then clip gradients. In our CPU test, the broken version reached `inf` within 5 steps.

**Notebook B: error about sizes.**
```python
model = nn.Sequential(nn.Linear(10, 16), nn.ReLU(), nn.Linear(16, 1))
loss = nn.BCEWithLogitsLoss()(model(xb), yb)      # yb: int64, shape (32,)
```
Symptom: "Target size (torch.Size([32])) must be the same as input size (torch.Size([32, 1]))". Fix: `model(xb).squeeze(1)` and `yb.float()`.

**Notebook C: loss does not move.**
```python
layers = []
for _ in range(20): layers += [nn.Linear(64, 64), nn.Sigmoid()]
model = nn.Sequential(*layers, nn.Linear(64, 10))
```
Cause: vanishing gradients; the first layer's gradient norm is almost zero. Fix: ReLU with `BatchNorm1d` after each linear layer (or far fewer layers), then confirm with gradient norms.

**Notebook D: GPU out of memory after many steps.**
```python
losses = []
for xb, yb in train_dl:
    ...
    losses.append(loss)                          # keeps every graph alive
```
Cause: storing the loss tensor keeps each step's computation graph in memory, so use grows every step. Fix: `losses.append(loss.item())`, then reduce the batch size or add mixed precision if memory is still short. On CPU, the same bug shows as growing RAM in the Colab resource panel.

## Common Mistake
Many learners respond to every problem by changing the learning rate or the architecture, without first reading the error or checking shapes. Several bugs, such as a missing `zero_grad` or a stored loss tensor, produce symptoms that look like tuning problems. Follow the checklist in order, and change one thing at a time.

## Key Takeaways
1. NaN or exploding loss usually means a high learning rate or unscaled inputs; normalise, lower the rate and clip gradients.
2. Vanishing gradients show as a flat loss and near-zero early-layer gradients; use ReLU, normalisation or fewer layers.
3. For OOM errors, stop storing graphs, reduce the batch size and use mixed precision; for any problem, follow a fixed debugging checklist.

## Hands-on Exercise
**Task:** Debug 4 provided broken training notebooks and record the symptom, the cause and the fix for each one.
**Tools:** Google Colab (free; all four notebooks run on CPU, and Notebook D can also be tried on a GPU runtime); PyTorch.
**Steps:**
1. Open notebooks A to D from the course page and run each one unchanged.
2. For each, write the symptom in one line before you change anything.
3. Use the checklist: shapes, one-batch overfit, loss format, learning rate, gradient norms, memory.
4. Apply one fix at a time until the notebook trains correctly.
5. Fill a table with four rows: notebook, symptom, cause, fix, evidence that it worked.
**What good looks like:** A complete table matching the answer key (A: unscaled inputs, fixed with standardisation and clipping; B: logits and label shape or dtype mismatch, fixed with `squeeze(1)` and `float()`; C: vanishing gradients from deep sigmoid layers, fixed with ReLU and BatchNorm; D: stored loss tensors, fixed with `.item()`), with printed evidence for each fix.
**Time:** about 40 minutes

## Review Flags
- [VERSION] PyTorch mixed-precision API (`torch.amp.GradScaler("cuda")` and `torch.autocast`); older code uses `torch.cuda.amp`. Check against the Colab PyTorch version at recording time.
- The course team must package notebooks A to D from the inline code above, with setup lines (imports, `xb`, `yb`, `train_dl`) added, and confirm each shows its symptom before recording.
