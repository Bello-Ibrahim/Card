# L05 How CNNs Learn Visual Features

Course: AI-19 · Module: M2 · Objectives: O2 · Video: 5 min (screen demo)

## Hook
In L03 you chose the blur size and the edge thresholds yourself. That works for a document on a desk. But who could write the rules that separate a healthy leaf from a leaf with early rust, in every light and at every angle? A convolutional neural network does not need those rules. It learns its own filters from examples.

## Explanation
A **filter** (also called a **kernel**) is a small grid of numbers, for example 3 × 3. **Convolution** slides the filter across the image. At each position, it multiplies the filter values by the pixel values under it and adds the results. The output is a new image, called a **feature map**, that is bright where the image matches the filter's pattern.

The filter values decide what it detects. A filter with negative numbers on the left and positive numbers on the right responds to vertical edges, where dark changes to light. A filter of equal values averages its neighbours, which is a blur. You used such filters in L03 without seeing the numbers: Gaussian blur and Canny are built from them.

A **convolutional neural network (CNN)** stacks many layers of filters. You already know neural networks, weights and training from Python for AI; the difference here is that the weights *are* filter values.

- **Early layers** learn simple patterns: edges at different angles, colour changes and small textures.
- **Middle layers** combine these into shapes: corners, circles, stripes and repeated patterns.
- **Later layers** combine shapes into object parts, such as a wheel, an eye or the vein pattern of a leaf.
- A final **classification layer** turns the last feature maps into scores for each class.

**Pooling** layers, or filters with a larger step (**stride**), shrink the feature maps between layers. Each later filter therefore "sees" a larger area of the original image.

The most important idea: **nobody designs these filters by hand.** They start as random numbers. During training, the network adjusts them so that its predictions match the labels. If rust spots help separate the classes, some filters become rust-spot detectors. This is why a CNN trained on millions of general photos has already learned useful early and middle filters, which you will reuse in L07.

**Analogy:** Imagine a set of stencils, each cut with a small pattern: a line, a curve, a dot. You slide each stencil across a picture, and it lights up wherever the picture matches its pattern. A CNN starts with blank stencils and cuts its own patterns by looking at thousands of labelled pictures. Later layers use stencils made from combinations of earlier ones.

## Worked Example
Leila Haddad inspects printed fabric at a textile workshop in Tripoli, Lebanon. Before training a model, she wants to see what simple filters detect on a fabric photo.

```python
import cv2
import numpy as np

img = cv2.imread("fabric.jpg", cv2.IMREAD_GRAYSCALE)

kernels = {
    "vertical_edge": np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]], np.float32),
    "blur": np.ones((3, 3), np.float32) / 9,
    "sharpen": np.array([[0, -1, 0],
                         [-1, 5, -1],
                         [0, -1, 0]], np.float32),
}
for name, k in kernels.items():
    out = cv2.filter2D(img, cv2.CV_32F, k)
    out = cv2.convertScaleAbs(out)         # back to 0-255
    cv2.imwrite(f"fabric_{name}.png", out)
    print(name, out.mean().round(1))
```

The vertical edge map is bright along vertical threads and printed stripes, and dark on flat areas. The blur softens the weave texture. The sharpen filter makes small defects, such as a pulled thread, stand out. `CV_32F` keeps negative values during the calculation, and `convertScaleAbs` turns them into positive 0-255 values for display.

**On screen (presenter steps):**
1. Upload a fabric or texture photo to Colab and run the cell.
2. Display the original and the three outputs in a 2 × 2 Matplotlib grid.
3. Change the edge kernel to its transpose (`k.T`) and show that it now finds horizontal edges.
4. Show a prepared image of the first-layer filters of a pre-trained CNN, and point out edge-like and colour-blob filters that look similar to the hand-made ones.

## Common Mistake
Many learners believe each filter in a CNN detects one named thing, such as "the wheel filter". Early filters do match simple, clear patterns, but most deeper filters respond to mixtures of patterns that have no simple name. Treat visualisations as a rough guide, not as a full explanation of why a model made a decision. Also, a CNN learns whatever separates the labels in its training data, including shortcuts such as a background colour that appears in only one class.

## Key Takeaways
1. A filter is a small grid of numbers; convolution slides it over the image and produces a feature map that is bright where the pattern matches.
2. CNNs stack layers of filters: edges first, then shapes, then object parts, with a classification layer at the end.
3. CNN filters are learned from labelled data, not designed by hand, which is why pre-trained filters can be reused for new tasks.

## Hands-on Exercise
**Task:** Apply 3 hand-made filters (edge, blur, sharpen) to an image with OpenCV and describe what each one detects. Then compare them with the filters a CNN learns in its first layer.
**Tools:** Google Colab; OpenCV, NumPy and Matplotlib; a photo with clear textures and edges, such as a brick wall, fabric or a bookshelf, with no people in it; optionally PyTorch and torchvision, which are usually pre-installed in Colab. [VERSION]
**Steps:**
1. Run the three filters from the worked example on your own photo and display the results.
2. Write one sentence for each filter: what becomes bright, what becomes dark.
3. Make a horizontal edge filter by transposing the vertical one, and describe the difference.
4. Load a small pre-trained CNN, for example `torchvision.models.resnet18(weights="DEFAULT")`, and print the shape of `model.conv1.weight`. [VERSION]
5. Display the first 16 filters as small colour images (normalise each one to 0-1 first).
6. Find two learned filters that look like edge detectors and one that looks like a colour detector.
**What good looks like:** Three clear filter outputs with correct descriptions, and a short comparison stating that some learned filters look like edge detectors, but they were learned from data and include colour patterns that the hand-made filters do not have.
**Time:** about 30 minutes

## Review Flags
- [VERSION] torchvision model names and the `weights="DEFAULT"` argument, and whether PyTorch and torchvision are pre-installed in Colab, must be checked at recording time. Curriculum flag: OpenCV function names (`filter2D`, `convertScaleAbs`) for L02-L05. The OpenCV code was tested with opencv-python-headless on a synthetic image.
