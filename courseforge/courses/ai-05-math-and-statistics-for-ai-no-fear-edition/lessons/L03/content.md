# L03 The Dot Product: Weighted Sums and Similarity

Course: AI-05 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
If a courier needs 2 minutes for every kilometre and 5 minutes for every stop, how long will a trip take? You can answer that in your head. Without noticing, you have just done the single most common calculation in machine learning.

## Explanation
The **dot product** takes two vectors of the same dimension and gives back one number. In words: multiply the matching components, then add the results.

For `a = [2, 5]` and `b = [8, 3]`:

- first components: 2 × 8 = 16
- second components: 5 × 3 = 15
- add them: 16 + 15 = 31

So `a · b = 31`. The dot symbol "·" is where the name comes from. In NumPy you write `np.dot(a, b)`. [VERSION]

**Why it matters for prediction.** Many models predict with a **weighted sum**. Each feature has a **weight** that says how much that feature matters. The prediction is weight times feature, for every feature, all added together. That is exactly a dot product of a weight vector and a feature vector. In later lessons we also add a starting value called the **bias**, written `b`, so a one-feature model looks like `y = w*x + b`: "the prediction is the weight times the input, plus a starting value".

**Why it matters for similarity.** The dot product also tells you whether two vectors point in a similar direction. Imagine hypothetical taste profiles as `[spicy, sweet, sour]`, scored from 0 to 4:

- Customer A: `[1, 2, 0]`
- Customer B: `[2, 4, 0]`
- Customer C: `[0, 0, 3]`

A · B = 1×2 + 2×4 + 0×0 = 2 + 8 + 0 = 10. A · C = 1×0 + 2×0 + 0×3 = 0. A and B like the same things, so their dot product is large. A and C share nothing, so it is 0. Recommendation systems use this idea to find similar users or products. Because long vectors give bigger dot products, practitioners often divide by both lengths. This is called **cosine similarity**, and it is always between −1 and 1. For A and B it is exactly 1, because B is just A doubled.

**Analogy:** A dot product is like a shopping bill. The feature vector is the quantities in your basket (3 apples, 2 loaves), and the weight vector is the price of each item. Multiply each quantity by its price and add everything up, and you get one total. A model's prediction is the "bill" for one example.

## Worked Example
Dewi is a hypothetical operations planner for a delivery start-up in Jakarta, Indonesia. From past trips, her team estimates that each kilometre adds about 2 minutes and each stop adds about 5 minutes. These numbers are invented for the example.

Her weight vector is `w = [2, 5]` (minutes per kilometre, minutes per stop). Tomorrow's first trip is 8 kilometres with 3 stops, so the feature vector is `x = [8, 3]`.

**Picture:** two bars stacked on each other, one for distance time and one for stop time.

**Hand calculation:** 2 × 8 = 16 minutes for distance, 5 × 3 = 15 minutes for stops, total 31 minutes.

**Code:**

```python
import numpy as np
w = np.array([2, 5])   # minutes per km, minutes per stop
x = np.array([8, 3])   # km, stops
print(np.dot(w, x))    # 31
```

Dewi also sees how to read the weights. If the trip had one more stop, the prediction would rise by 5 minutes, the weight for stops. Each weight tells you how much the prediction changes when its feature grows by 1. You will use this same reading in the capstone.

## Common Mistake
Learners often multiply the matching components and forget to add them. In NumPy, `w * x` gives `[16, 15]`, which is still a vector. `np.dot(w, x)` gives `31`, which is one number. If your "prediction" has several numbers when you expected one, check whether you used `*` instead of `np.dot`. A second mistake is to use vectors of different lengths. NumPy stops with an error, and that error is helpful: every feature needs exactly one weight.

## Key Takeaways
1. The dot product multiplies matching components and adds the results, giving one number.
2. A model's prediction is often a weighted sum of features, which is a dot product of weights and features.
3. A large dot product (or cosine similarity close to 1) means two vectors point in a similar direction; 0 means they share nothing.

## Hands-on Exercise
**Task:** Calculate three dot products by hand, repeat them with `np.dot`, and use one to make a price prediction for a hypothetical product.
**Tools:** Pen and paper; Google Colab with NumPy.
**Steps:**
1. By hand, calculate `[1, 2, 3] · [4, 5, 6]`, `[2, 0, -1] · [3, 7, 4]` and `[0.5, 2] · [10, 3]`. Write each multiplication before you add.
2. In Colab, check each answer with `np.dot`.
3. Invent a small product, such as a phone case. Choose two features, for example material cost 3 and labour minutes 10, and two weights, for example 2 and 0.5.
4. Calculate the predicted price by hand and with `np.dot`.
5. Write one sentence for each weight that explains what it means, for example "each extra minute of labour adds 0.5 to the price".
**What good looks like:** Your answers are 32, 2 and 11, and NumPy agrees. Your price prediction (11 with the example numbers) matches in both methods, and each weight has a clear plain-language meaning.
**Time:** about 20 minutes

## Review Flags
- [VERSION] NumPy: `np.dot` is a stable function, but confirm its behaviour and any warnings against the current NumPy version before recording. The code outputs shown were checked with NumPy 2.4.
- All numbers (delivery weights, taste scores, product price) are hypothetical and must not be presented as real data.
