# L09 Object Detection: Boxes, Classes and IoU

Course: AI-19 · Module: M3 · Objectives: O1, O5 · Video: 5 min

## Hook
A detector draws a box around a car, but cuts off the back of the car. Is that correct or a mistake? Without a clear rule, two people will score the same model differently. That rule is IoU.

## Explanation
An object detector returns a list of detections. Each detection has three parts:

- A **bounding box**, usually as `(x1, y1, x2, y2)`: the top-left and bottom-right corners in pixels. Some formats use the centre, width and height instead, and YOLO label files use values scaled from 0 to 1. Always check which format a tool uses.
- A **class**, such as "car" or "bus".
- A **confidence score** from 0 to 1.

Detectors often produce several overlapping boxes for one object. **Non-maximum suppression (NMS)** keeps the highest-scoring box and removes boxes that overlap it strongly. Libraries usually run it for you.

**Intersection over Union (IoU)** measures how well a predicted box matches the true box (the **ground truth**) that a person drew:

IoU = area of overlap ÷ area of union

The union is the area covered by either box: area A + area B − overlap. IoU is 1.0 for a perfect match and 0 when the boxes do not touch.

To score a detector, you choose an **IoU threshold**, often 0.5. A prediction counts as a **true positive** if it has the right class and IoU of at least 0.5 with a ground-truth box that no other prediction has already matched. Otherwise it is a **false positive**. Every ground-truth box with no match is a **false negative**. From these counts you get precision and recall, as in L08.

**Average precision (AP)** summarises precision and recall across all confidence thresholds for one class. **mAP** (mean average precision) is the average of AP over all classes. You will see two common versions: **mAP50**, which uses an IoU threshold of 0.5, and **mAP50-95**, which averages over thresholds from 0.5 to 0.95 and rewards very accurate boxes. mAP50-95 is always lower than or equal to mAP50 for the same model, so compare the same version.

**Analogy:** IoU is like laying a transparent sheet with your drawn box over the true box on a light table. You measure the area where both shapes overlap and divide it by the total area either shape covers. A box that is too large and a box that is too small both lose points, because both make the union larger than the overlap.

## Worked Example
Nadia Rahman evaluates a parking-lot detector for a shopping centre in Dhaka, Bangladesh. For one car, the ground-truth box is A = (100, 50, 300, 150) and the predicted box is B = (150, 70, 330, 170).

**By hand:**

1. Area A = (300 − 100) × (150 − 50) = 200 × 100 = 20,000.
2. Area B = (330 − 150) × (170 − 70) = 180 × 100 = 18,000.
3. Overlap: x from max(100, 150) = 150 to min(300, 330) = 300, so width 150. y from max(50, 70) = 70 to min(150, 170) = 150, so height 80. Overlap = 150 × 80 = 12,000.
4. Union = 20,000 + 18,000 − 12,000 = 26,000.
5. IoU = 12,000 ÷ 26,000 ≈ 0.46.

At a threshold of 0.5, this prediction is a false positive, and the car is a false negative, even though the box is clearly on the car. Nadia sees that the model's boxes often shift towards the car's shadow, a pattern to fix with more training images.

She checks her calculation with a short function:

```python
def iou(a, b):
    """Boxes as (x1, y1, x2, y2) in pixels."""
    ix1, iy1 = max(a[0], b[0]), max(a[1], b[1])
    ix2, iy2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)

print(round(iou((100, 50, 300, 150), (150, 70, 330, 170)), 3))  # 0.462
```

The `max(0, ...)` parts matter: when boxes do not overlap, the width or height would be negative, and without them two negative numbers could multiply into a positive overlap that does not exist.

## Common Mistake
Many learners compare mAP numbers from different sources as if they meant the same thing. A model with "mAP 0.70" at IoU 0.5 may be worse than one with "mAP 0.50" at IoU 0.5-0.95. Only compare mAP values that use the same version and the same test set. Another mistake is mixing box formats, such as passing `(x, y, width, height)` to a function that expects corners, which gives wrong IoU values with no error.

## Key Takeaways
1. A detector returns a box, a class and a confidence score for each object, and NMS removes duplicate boxes.
2. IoU is the overlap area divided by the union area; a threshold such as 0.5 decides whether a prediction counts as correct.
3. mAP summarises precision and recall across classes; compare only mAP values with the same IoU version and the same test set.

## Hands-on Exercise
**Task:** Calculate IoU by hand for 3 pairs of boxes, then check your answers with a short Python function.
**Tools:** Pen and paper; Google Colab or any Python environment.
**Steps:**
1. Draw each pair on squared paper. Pair 1: (0, 0, 100, 100) and (50, 0, 150, 100). Pair 2: (0, 0, 100, 100) and (20, 20, 80, 80). Pair 3: (0, 0, 40, 40) and (50, 50, 90, 90).
2. For each pair, write the two areas, the overlap, the union and the IoU.
3. Decide for each pair whether it counts as a match at an IoU threshold of 0.5.
4. Type the `iou` function into a notebook and check your three answers.
5. Remove both `max(0, ...)` calls, run Pair 3 again, and explain the wrong result.
**What good looks like:** Correct values of about 0.33, 0.36 and 0 (none of them is a match at 0.5), and one sentence explaining why the function needs `max(0, ...)` for boxes that do not overlap.
**Time:** about 20 minutes

## Review Flags
- None. This is a concept lesson with a hypothetical example; the IoU function and all worked answers were run and checked in Python.
