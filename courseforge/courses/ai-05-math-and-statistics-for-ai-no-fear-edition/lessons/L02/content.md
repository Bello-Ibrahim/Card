# L02 Vectors: Data as Lists of Numbers

Course: AI-05 · Module: M1 · Objectives: O1, O2 · Video: 5 min (screen demo)

## Hook
How does a computer "see" a flat for rent, a customer or a song? It cannot see them at all. It sees a short list of numbers. Once you understand that list, you understand how almost all machine learning data is stored.

## Explanation
A **vector** is an ordered list of numbers that describes one thing. "Ordered" means the position of each number matters. We write a vector in square brackets, for example `[75, 3, 20]`.

Imagine a flat in Lisbon described by three numbers: size in square metres, number of rooms and age in years. The vector `[75, 3, 20]` means 75 m², 3 rooms and 20 years old. If you swapped the numbers to `[3, 75, 20]`, it would describe a very strange flat. Each position is called a **component**, and each component is one **feature** of the thing we describe. The number of components is the vector's **dimension**. This flat vector has dimension 3.

A vector with two components, such as `[3, 1]`, can be drawn as an **arrow** on a graph. It starts at the origin (0, 0) and ends at the point 3 steps right and 1 step up. Pictures only work in 2 or 3 dimensions, but the rules are the same for 100 components.

There are three operations you need.

**1. Adding vectors.** Add the matching components. In words: first plus first, second plus second. So `[3, 1] + [1, 2] = [4, 3]`. As arrows, you place the second arrow at the end of the first; the sum is the arrow from the start to the new end point. Both vectors must have the same dimension.

**2. Multiplying by a number.** Multiply every component by that number. So `2 × [3, 1] = [6, 2]`. The arrow points in the same direction but is twice as long. A single number like this is called a **scalar**, because it "scales" the vector.

**3. Length.** The length (also called the **norm**) of a vector is how long its arrow is. For 2D vectors you use the Pythagorean theorem from school: square each component, add them and take the square root. For `[3, 4]`: 3² + 4² = 9 + 16 = 25, and the square root of 25 is 5. In NumPy, `np.linalg.norm` does this for any dimension. Later, length helps us measure how far apart two data points are.

**Analogy:** A vector is like a row on a recipe card: "2 eggs, 300 g flour, 1 cup milk". The order matters, because the card only makes sense if everyone agrees which number means eggs. Doubling the recipe multiplies every amount by 2, which is exactly how a scalar multiplies a vector.

## Worked Example
Inês is a hypothetical data analyst at an estate agency in Lisbon, Portugal. She describes flats as `[size, rooms, age]`. Flat A is `[75, 3, 20]`.

A client asks, "What would twice this flat look like?" That is scalar multiplication: `2 × [75, 3, 20] = [150, 6, 40]`. Inês notices that this answer is silly for age, because a larger flat is not older. This is a useful lesson: the maths always works, but you must check that the result makes sense for the real thing.

Next she shows the idea in 2D on screen. A presenter can follow these steps:

1. Open the Desmos graphing calculator in a browser. [VERSION]
2. In the first line, type `a=(3,1)` and in the second `b=(1,2)`. Desmos shows two points. [VERSION]
3. To draw arrows from the origin, type `vector((0,0),a)` and `vector((0,0),b)`. [VERSION]
4. Type `vector(a,a+b)` to place arrow b at the end of arrow a, then `vector((0,0),a+b)`. The last arrow ends at (4, 3), the sum.
5. Type `2a` to see the point (6, 2): the same direction as a, but twice as far.

Then she checks the results in Colab:

```python
import numpy as np
a = np.array([3, 1])
b = np.array([1, 2])
print(a + b)                            # [4 3]
print(2 * a)                            # [6 2]
print(np.linalg.norm(np.array([3, 4])))  # 5.0
```

## Common Mistake
Learners often add vectors whose components mean different things, for example a flat `[size, rooms, age]` and another flat stored as `[rooms, size, age]`. NumPy will add them without any warning, and the result is nonsense. Always keep the same order of features for every example, and write the order down as a comment in your notebook.

## Key Takeaways
1. A vector is an ordered list of numbers that describes one thing; each position is one feature.
2. You add vectors component by component, and multiplying by a scalar multiplies every component.
3. The length (norm) of a vector is the square root of the sum of its squared components, and `np.linalg.norm` calculates it.

## Hands-on Exercise
**Task:** Draw two 2D vectors in Desmos, add them, and check your answer with NumPy; then describe three items from your own work as vectors.
**Tools:** Desmos graphing calculator (free, in a browser) [VERSION]; Google Colab with NumPy; pen and paper.
**Steps:**
1. Choose two 2D vectors with small whole numbers, for example `[2, 3]` and `[4, -1]`.
2. On paper, add them and multiply the first one by 3.
3. In Desmos, draw both as arrows from the origin, then draw their sum. [VERSION]
4. In Colab, create both vectors with `np.array` and print the sum, the scaled vector and the length of each.
5. Think of three items from your work or daily life, such as a product, a delivery or a lesson. Describe each as a vector of three features, and write the feature order in words. Use made-up values, not confidential data.
**What good looks like:** Your hand answers, Desmos picture and NumPy output all agree. Your three vectors use the same feature order, and each feature is a number with a clear unit.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Desmos: confirm that typing a point such as `a=(3,1)`, the `vector()` function and expressions such as `a+b` and `2a` still work as described in the current graphing calculator before scripting the screen demo.
