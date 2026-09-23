# L14 Gradient Descent Step by Step

Course: AI-05 · Module: M3 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
You now know how to measure how wrong a model is (the loss) and which way is downhill (the gradient). Put those two ideas in a loop, and you have the engine that trains almost every modern machine learning model. It fits in about six lines of code.

## Explanation
**Gradient descent** is a method for finding the weights that make the loss small. In words: start somewhere, look at the slope, take a small step downhill, and repeat.

Each step does three things:

1. Calculate the gradient of the loss at the current weights.
2. Move each weight a little **against** the gradient.
3. Repeat until the loss stops falling.

The update rule is:

`w_new = w − learning_rate × gradient`

In words: the new weight is the old weight minus a small number times the slope. If the slope is positive, the weight goes down; if it is negative, the weight goes up. Either way, the loss falls. Near the bottom, the slope is close to zero, so the steps become smaller by themselves.

The **learning rate** sets the size of each step. It is a number you choose, often something like 0.1 or 0.01. Choosing it well is important:

- **Too small:** each step is tiny, so learning is very slow.
- **About right:** the loss falls quickly and settles near the minimum.
- **Too large:** each step jumps past the bottom to the other side of the valley, often higher than before. The loss can grow instead of falling, which is called **diverging**.

Plotting the loss against the step number gives a **loss curve**, the most important picture for checking that training works.

**Analogy:** Gradient descent is like walking downhill in thick fog. You cannot see the valley, but you can feel the slope under your feet. You take a step in the downhill direction, feel the slope again and take another step. Short steps are safe but slow. Very long steps might carry you across the valley and up the other side.

## Worked Example
Aroha is a hypothetical junior machine learning engineer in Wellington, New Zealand. Before trusting her training code on real data, she tests it on a toy loss where she already knows the answer: `L(w) = (w − 3)²`. The minimum is at w = 3, where the loss is 0.

**Picture:** a U-shaped curve with its lowest point at w = 3. She starts at w = 0, on the left side of the valley.

**Hand calculation:** the chain rule from L13 gives the derivative `2 × (w − 3)`. With a learning rate of 0.1:

- Step 1: gradient = 2 × (0 − 3) = −6. New w = 0 − 0.1 × (−6) = 0.6. Loss = (0.6 − 3)² = 5.76.
- Step 2: gradient = 2 × (0.6 − 3) = −4.8. New w = 0.6 + 0.48 = 1.08. Loss = 3.6864.
- Step 3: gradient = 2 × (1.08 − 3) = −3.84. New w = 1.08 + 0.384 = 1.464. Loss ≈ 2.36.

The loss falls from 9 to 5.76, 3.69 and 2.36, and the steps get smaller as w approaches 3.

**Code:** a presenter can follow these steps in Colab on screen.

1. Type the `descend` function and explain each line.
2. Run it for three learning rates and print the final weight for each.
3. Show the loss curves. The vertical axis uses a log scale, where each grid line is 10 times the one below, so that very large and very small losses fit on one plot.

```python
import matplotlib.pyplot as plt

def descend(lr, steps=30):
    w, losses = 0.0, []
    for step in range(steps):
        grad = 2 * (w - 3)      # derivative of (w - 3)**2
        w = w - lr * grad       # step against the gradient
        losses.append((w - 3) ** 2)
    return w, losses

for lr in [0.01, 0.1, 1.1]:
    w, losses = descend(lr)
    print(lr, round(w, 4))
    plt.plot(losses, label=f"lr={lr}")
plt.yscale("log"); plt.legend(); plt.show()
```

4. Read the output: `0.01 1.3635`, `0.1 2.9963` and `1.1 -709.1289`.

After 30 steps, the small learning rate has only reached about 1.36: too slow. The learning rate of 0.1 is very close to 3. The learning rate of 1.1 has jumped back and forth across the valley with bigger and bigger jumps, and its loss curve rises steeply. That is divergence.

## Common Mistake
When the loss grows or jumps up and down, learners often rewrite their gradient formula. Very often the formula is fine and the learning rate is simply too large. First, try a learning rate 10 times smaller. Second, always plot the loss curve. A curve that falls and then flattens means training is working; a curve that rises means the steps are too big.

## Key Takeaways
1. Gradient descent repeats one update, `w = w − learning_rate × gradient`, to move the weights downhill on the loss.
2. The learning rate sets the step size: too small is slow, too large overshoots and can diverge.
3. Always plot the loss curve: it should fall and then flatten out.

## Hands-on Exercise
**Task:** Write a loop in Colab that minimises `(w − 3)²` with gradient descent, then try three learning rates and plot the loss over time for each.
**Tools:** Google Colab with Matplotlib (available in Colab).
**Steps:**
1. Calculate the first two steps by hand with a learning rate of 0.1, starting at w = 0.
2. Type the `descend` function yourself rather than copying it, and check that the first two weights match your hand calculation (print `w` inside the loop).
3. Run it with learning rates 0.01, 0.1 and 1.1, and plot the three loss curves.
4. Try a learning rate of 1.0. Print the weights and describe what happens.
5. Change the starting point to w = 10 and check that the good learning rate still reaches 3.
6. Write three sentences comparing the learning rates.
**What good looks like:** Your hand steps give 0.6 and 1.08, matching the code. Your plot shows one slow curve, one fast curve that flattens near 0, and one that rises. With 1.0, the weight jumps between 0 and 6 forever and the loss stays at 9.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Google Colab and Matplotlib: confirm the current Colab interface and that `plt.yscale("log")` and `plt.legend()` behave as shown before scripting the screen demo. Outputs were checked with Python and NumPy 2.4.
