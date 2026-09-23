# L04 How Networks Learn: Loss and Backpropagation

Course: AI-13 · Module: M1 · Objectives: O2 · Video: 5 min (screen demo)

## Hook
The network from L03 has 235,146 parameters, all set to random values. Nobody will tune them by hand. So how does each one know which way to move? The answer is one line of code, `loss.backward()`, and this lesson shows what it does.

## Explanation
Training needs three parts.

**1. A loss function** gives one number that says how wrong the model is on a batch.

- `nn.CrossEntropyLoss` for classification. It takes raw logits of shape `(N, C)` and integer class labels of shape `(N,)`. It applies log-softmax inside.
- `nn.MSELoss` for regression. It takes predictions and targets of the same shape.
- `nn.BCEWithLogitsLoss` for binary or multi-label problems with one logit per label.

**2. Gradients.** Quick recap from AI-05: the gradient of the loss with respect to a parameter tells you how much the loss changes, and in which direction, if you move that parameter a little. **Backpropagation** is the chain rule applied layer by layer from the loss back to the inputs, reusing results so it stays fast. You never write it yourself. PyTorch's **autograd** records every operation on tensors that have `requires_grad=True`, and `loss.backward()` fills the `.grad` field of each parameter.

**3. Gradient descent** moves each parameter a small step against its gradient: `w = w - lr * w.grad`. The **learning rate** (`lr`) sets the step size. Too small, and training is slow. Too large, and the loss jumps around or grows.

Two details matter in code. First, gradients **accumulate**: each `backward()` adds to `.grad`, so you must reset it to zero before the next step. Second, the update itself must not be recorded by autograd, so you do it inside `torch.no_grad()`.

**Analogy:** Gradient descent is like walking downhill in thick fog. You cannot see the valley, but you can feel the slope under your feet. At each step you move a little in the steepest downhill direction. Short steps are safe but slow. Very long steps can take you past the valley and up the other side.

## Worked Example
Bilal is a data scientist at a hypothetical logistics company in Lahore, Pakistan. Before he trusts optimisers, he wants to see gradient descent work on a function he can check by hand: `f(w) = (w - 3)²`. The minimum is at `w = 3`, and the derivative is `2(w - 3)`, so at `w = 0` the gradient should be `-6`.

**Screen demo steps:**

1. Create `w` with `requires_grad=True` and check the gradient.
2. Run 10 manual steps and store the loss.
3. Plot the loss.

```python
import torch
import matplotlib.pyplot as plt

w = torch.tensor(0.0, requires_grad=True)
loss = (w - 3) ** 2
loss.backward()
print(w.grad)                         # tensor(-6.)

lr, history = 0.1, []
w.grad.zero_()
for step in range(10):
    loss = (w - 3) ** 2
    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad
    w.grad.zero_()
    history.append(loss.item())

print(round(w.item(), 3))             # 2.678
plt.plot(history); plt.xlabel("step"); plt.ylabel("loss"); plt.show()
```

Each step moves `w` 20% of the remaining distance towards 3, so the loss falls quickly at first and then more slowly. Bilal then tries `lr = 1.1`. Now each step overshoots, `w` moves further from 3 each time, and the loss grows. This is the same pattern you will see in real learning curves when the learning rate is too high (L08).

In real training, `torch.optim.SGD(model.parameters(), lr=0.1)` does the update, and `optimizer.zero_grad()` does the reset, for every parameter at once. Adam (`torch.optim.Adam`) adapts the step size for each parameter and is a common default.

## Common Mistake
The most common mistake is forgetting to zero the gradients. Because `.grad` accumulates, each step uses the sum of all previous gradients, and the steps become larger and larger. The loss may fall for a while and then jump or become NaN, which looks like a learning-rate problem. Always call `optimizer.zero_grad()` (or `.grad.zero_()`) once per step. A second mistake is passing one-hot labels or probabilities where `CrossEntropyLoss` expects integer class IDs; check the label shape and dtype first.

## Key Takeaways
1. The loss is one number for how wrong the model is; use cross-entropy with logits and integer labels for classes, and mean squared error for numbers.
2. `loss.backward()` uses autograd to compute every parameter's gradient by the chain rule; gradients accumulate, so reset them every step.
3. Gradient descent moves parameters against the gradient, and the learning rate controls the step size: too small is slow, too large diverges.

## Hands-on Exercise
**Task:** Use autograd to compute a gradient for a simple function, then take 10 manual gradient-descent steps and plot the loss.
**Tools:** Google Colab (free, CPU is enough); PyTorch; matplotlib.
**Steps:**
1. Choose a function with a known minimum, for example `f(w) = (w - 3)²` or `f(a, b) = (a - 1)² + 2(b + 2)²`.
2. Compute the gradient by hand at a start point, then with `backward()`, and confirm they match.
3. Run 10 manual gradient-descent steps with `lr = 0.1`, zeroing the gradient each time, and plot the loss.
4. Repeat with a very small learning rate and with one that is too large, and plot all three curves on one chart.
5. Remove the `zero_()` line, run again, and describe what changes.
**What good looks like:** Matching hand and autograd gradients, a plot with three clearly labelled curves (slow, good, diverging), and a short note explaining the effect of forgetting to zero gradients.
**Time:** about 25 minutes

## Review Flags
- None. The lesson uses a hand-checkable function and stable, core autograd features; the printed values must be confirmed by running the snippet before recording.
