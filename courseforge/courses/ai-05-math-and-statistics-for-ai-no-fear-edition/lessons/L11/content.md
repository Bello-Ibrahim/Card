# L11 Functions, Slopes and Derivatives

Course: AI-05 · Module: M3 · Objectives: O1, O4 · Video: 5 min (screen demo)

## Hook
The word "calculus" worries many people more than any other part of maths. Here is a secret: for machine learning, you need one main idea from calculus, and you already use it when you walk up a hill. Is the ground getting steeper or flatter? That feeling is a derivative.

## Explanation
A **function** is a rule that turns an input into an output. We often write it as `f(x)`, read "f of x". For example, `f(x) = x²` means "take the input and multiply it by itself", so `f(3) = 9`.

The **slope** of a straight line tells you how much the output changes when the input increases by 1. A slope of 2 means "up 2 for every 1 step right". A negative slope means the line goes down.

A curve such as `y = x²` does not have one slope. It is flat near 0 and gets steeper as x grows. So we ask a more precise question: **what is the slope at one particular point?** Imagine a straight line that just touches the curve at that point and goes in the same direction. This is the **tangent line**. Its slope is the slope of the curve at that point.

The **derivative** is a function that gives this slope at every point. In words: it tells you how fast the output changes when you change the input a little. For `f(x) = x²`, the derivative is `2x`, written `f'(x) = 2x` (read "f prime of x"). At x = 1 the slope is 2, at x = 2 it is 4 and at x = 3 it is 6.

You can also **estimate** a derivative with numbers: change the input by a tiny amount `h`, see how much the output changes, and divide. At x = 3 with h = 0.001: (3.001² − 3²) ÷ 0.001 = 6.001, which is very close to 6. This "nudge and measure" idea is how you will check your gradients in code.

You only need four rules in this course. No proofs.

1. **Constant rule:** a fixed number, such as 7, has derivative 0, because it never changes.
2. **Power rule:** `xⁿ` has derivative `n × xⁿ⁻¹`. So `x²` becomes `2x`, and `x` becomes 1.
3. **Constant multiple rule:** `5x²` has derivative `5 × 2x = 10x`.
4. **Sum rule:** the derivative of a sum is the sum of the derivatives. So `x² + 3x` becomes `2x + 3`.

Why does machine learning care? The derivative tells a model which way is "downhill" for its error, and how steep the hill is. That is the core of learning, as you will see in L14.

**Analogy:** A derivative is like the speedometer in a car. Your trip record shows the distance you have travelled. The speedometer shows how fast that distance is changing at this exact moment. The derivative is the speedometer reading of any function.

## Worked Example
Youssef runs a hypothetical tile workshop in Fez, Morocco. A square tile with side x centimetres has area `x²` square centimetres. He wants to know: if he makes the side a little longer, how fast does the area grow?

**Picture:** a presenter can follow these steps in Desmos on screen.

1. Open the Desmos graphing calculator. [VERSION]
2. Type `f(x)=x^2`. The curve appears.
3. Type `a=1`. Desmos offers to create a **slider** for `a`; accept it. [VERSION]
4. Type `y=2a(x-a)+f(a)`. This is the tangent line at x = a, using the slope 2a.
5. Move the slider to 1, 2 and 3. The line touches the curve at each point and becomes steeper.
6. Optional: type `f'(x)` to see Desmos draw the derivative, the straight line y = 2x. [VERSION]

**Hand calculation:** at side 3 cm, the derivative is 2 × 3 = 6. So a tiny increase in side, such as 0.001 cm, adds about 6 × 0.001 = 0.006 cm² of area.

**Code check:**

```python
def f(x):
    return x**2
h = 0.001
print((f(3 + h) - f(3)) / h)   # 6.000999999999479
```

The result is about 6.001, as expected. The long tail of digits is a small rounding effect of how computers store decimals, not a mistake.

## Common Mistake
Learners often confuse the value of a function with its slope. At x = 3, `f(3) = 9` but `f'(3) = 6`. The first says "how high", the second says "how steep". A second mistake is thinking a derivative must be a difficult symbolic calculation. For machine learning, the meaning matters most: a positive derivative means "increasing the input increases the output", a negative one means the opposite, and zero means "flat here".

## Key Takeaways
1. The derivative gives the slope of a function at each point: how fast the output changes when the input changes a little.
2. For `x²` the derivative is `2x`; the constant, power, constant multiple and sum rules cover this course.
3. You can check any derivative numerically by nudging the input by a tiny amount and dividing the change in output by the nudge.

## Hands-on Exercise
**Task:** In Desmos, plot `y = x²` and a tangent line at three points, estimate each slope, and compare with the derivative `2x`.
**Tools:** Desmos graphing calculator (free) [VERSION]; pen and paper; optional Google Colab.
**Steps:**
1. Plot `f(x)=x^2` and the tangent line `y=2a(x-a)+f(a)` with a slider for `a`, as in the worked example.
2. Choose three points, for example x = −1, 0.5 and 2.
3. For each point, read two points on the tangent line and estimate its slope as "rise ÷ run".
4. Calculate `2x` at each point and compare.
5. Optional: check one slope in Colab with the nudge method.
6. Using the rules, write the derivative of `3x² + 4x + 1` and check it at x = 1 with the nudge method.
**What good looks like:** Your slopes are close to −2, 1 and 4. You explain that the negative slope at x = −1 means the curve goes down there. The derivative of `3x² + 4x + 1` is `6x + 4`, which is 10 at x = 1.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Desmos: confirm that function notation `f(x)=`, automatic slider creation, and the `f'(x)` derivative notation work as described in the current graphing calculator before scripting the screen demo (carried from the curriculum flags).
