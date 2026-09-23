# L13 Gradients and the Chain Rule, Intuitively

Course: AI-05 · Module: M3 · Objectives: O4 · Video: 5 min

## Hook
A real model has many weights, not one. If the loss is too high, which weight should you change, in which direction and by how much? The gradient answers all three questions at once, and the chain rule shows you how to calculate it.

## Explanation
In L11, a function had one input and the derivative gave one slope. A loss usually depends on several weights. For a simple model `y_pred = w*x + b`, the loss depends on the weight `w` and the bias `b`.

A **partial derivative** is the slope in one direction only. In words: change one weight a tiny amount, keep every other weight fixed, and see how fast the loss changes. We write it as `∂L/∂w`, read "the partial derivative of L with respect to w". The curly ∂ just means "partial".

The **gradient** collects the partial derivatives for every weight into one vector. For our model, the gradient is `[∂L/∂w, ∂L/∂b]`. It points in the direction in which the loss **increases** fastest. So to reduce the loss, we move the weights in the **opposite** direction. That is the whole idea behind L14.

Each component tells you two things:

- its **sign**: positive means "increasing this weight increases the loss", negative means "increasing this weight decreases the loss";
- its **size**: how strongly the loss reacts to that weight right now.

**The chain rule.** A loss is often built in steps. First the model makes a prediction, then we calculate the error, then we square it. The chain rule says: to find how the final result reacts to the first input, **multiply the rates of change of each step**. If the error changes 2 units for each unit of `w`, and the loss changes −8 units for each unit of error, then the loss changes 2 × (−8) = −16 units for each unit of `w`.

**Analogy:** The chain rule is like a set of connected gears. Turn the first gear once and the second turns twice; each turn of the second turns the third three times. So one turn of the first gear turns the third 2 × 3 = 6 times. Each step's rate multiplies the next.

## Worked Example
Chloé is a hypothetical researcher at a plant nursery in Montréal, Canada. She has one invented training example: with x = 2 litres of a new fertiliser, a plant grew y = 7 cm. Her model is `y_pred = w*x + b`, with starting values w = 1 and b = 1. The loss is the squared error for this example.

**Step by step (hand calculation):**

1. Prediction: 1 × 2 + 1 = 3.
2. Error: prediction − truth = 3 − 7 = −4.
3. Loss: (−4)² = 16.

**Now the chain rule:**

- Loss = error², so the loss changes by `2 × error` for each unit of error: 2 × (−4) = −8.
- Error = w × x + b − y, so the error changes by `x` = 2 for each unit of `w`, and by 1 for each unit of `b`.
- Multiply along the chain: `∂L/∂w` = −8 × 2 = −16, and `∂L/∂b` = −8 × 1 = −8.

The gradient is `[−16, −8]`. Both parts are negative, so increasing `w` and `b` should reduce the loss. This makes sense: the prediction of 3 is too low, and bigger weights raise it. The `w` part is larger because `w` is multiplied by x = 2, so it has more influence.

**Code check by nudging:** change one weight a tiny amount up and down, and divide the change in loss by the total nudge. This is called a **numerical gradient**.

```python
x, y = 2.0, 7.0
def loss(w, b):
    return (w * x + b - y) ** 2

h = 0.0001
print(round((loss(1 + h, 1) - loss(1 - h, 1)) / (2 * h), 4))  # -16.0
print(round((loss(1, 1 + h) - loss(1, 1 - h)) / (2 * h), 4))  # -8.0
```

Both agree with the hand calculation. As a final test, Chloé takes a small step against the gradient: w = 1 + 0.01 × 16 = 1.16 and b = 1 + 0.01 × 8 = 1.08. The loss falls from 16 to 12.96. The gradient pointed the right way.

## Common Mistake
Learners often forget the sign and move **with** the gradient instead of against it. The gradient points uphill, towards a larger loss. To learn, you subtract it. A second mistake is to stop the chain too early: writing `∂L/∂w = 2 × error` and forgetting to multiply by `x`. When your numerical check disagrees with your formula, a missing link in the chain is the usual reason.

## Key Takeaways
1. A partial derivative is the slope for one weight with all other weights fixed, and the gradient collects them into one vector.
2. The gradient points in the direction where the loss increases fastest, so learning moves the weights in the opposite direction.
3. The chain rule multiplies the rates of change of each step; you can always check the result numerically by nudging each weight.

## Hands-on Exercise
**Task:** Calculate by hand the gradient of a simple two-weight loss at one point, then check it numerically in NumPy by nudging each weight a little.
**Tools:** Pen and paper; Google Colab with Python.
**Steps:**
1. Use the hypothetical loss `L(w1, w2) = w1² + 3 × w2²`.
2. Using the rules from L11, write `∂L/∂w1` (treat w2 as a fixed number) and `∂L/∂w2` (treat w1 as fixed).
3. Calculate the gradient at w1 = 1, w2 = 2.
4. In Colab, define the loss as a Python function and estimate each partial derivative with the nudge method, using h = 0.0001.
5. Compare the results. Then say which weight the loss is more sensitive to at this point, and why.
6. Optional: repeat Chloé's example with starting values w = 3, b = 2, and explain the signs.
**What good looks like:** `∂L/∂w1 = 2 × w1` and `∂L/∂w2 = 6 × w2`, so the gradient at (1, 2) is `[2, 12]`. Your numerical check gives values very close to 2 and 12, and you explain that w2 has more influence here because of its larger slope.
**Time:** about 25 minutes

## Review Flags
- None. The examples are hypothetical, and every gradient and code output shown was recalculated with Python.
