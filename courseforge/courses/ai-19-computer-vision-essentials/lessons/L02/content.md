# L02 Images as Numbers: Pixels, Channels and Colour

Course: AI-19 · Module: M1 · Objectives: O1, O3 · Video: 5 min (screen demo)

## Hook
You paint a square red in your code, display the image, and the square is blue. Nothing is broken. You have just met one of the most common surprises in computer vision, and after this lesson you will know exactly why it happens.

## Explanation
For a computer, an image is a grid of numbers. Each cell in the grid is a **pixel**. In Python, OpenCV loads an image as a NumPy array, so everything you already know about arrays applies.

The array has a **shape** of `(height, width, channels)`:

- **Height** is the number of rows of pixels.
- **Width** is the number of columns.
- **Channels** hold the colour. A colour image has 3 channels; a greyscale image has only height and width.

Each value is usually an 8-bit integer (`uint8`) from 0 to 255. 0 means none of that colour and 255 means the maximum. A pixel with values (0, 0, 0) is black, and (255, 255, 255) is white.

Pay attention to the order of the channels. OpenCV stores colour as **BGR** (blue, green, red), while most other libraries, including Matplotlib, Pillow and most deep learning models, expect **RGB**. If you pass a BGR array to a function that expects RGB, red and blue swap places. Convert with `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` whenever you move an image from OpenCV to another library.

Indexing follows the array: `img[y, x]` is the pixel in row `y` and column `x`. The row comes first. The origin (0, 0) is the **top-left** corner, and `y` grows downwards.

A **video** is the same idea over time: a sequence of these arrays, called frames. You will work with frames in L04.

We use Google Colab because it is free and needs no installation. Colab's interface, session limits and free resources change, so treat the menu names here as a guide. [VERSION]

**Analogy:** Think of an image as a large egg box with three layers. Each small cup holds a number that says how strong one colour is at that spot. OpenCV stacks the layers blue, green, red from top to bottom; most other tools expect red on top. If you hand the box to someone who expects a different order, the colours come out wrong, even though every number is correct.

## Worked Example
Hiroshi Tanaka checks photos of ceramic tiles at a small factory in Osaka, Japan. Before he trains any model, he wants to understand the data. He uploads one tile photo to Colab and runs this code:

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("tile.jpg")          # BGR, uint8
print(img.shape, img.dtype)           # e.g. (480, 640, 3) uint8
print(img[0, 0])                      # top-left pixel: [B G R]

img[50:150, 100:200] = (0, 0, 255)    # red block in BGR order

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
```

Example output: `(480, 640, 3) uint8` and a top-left pixel such as `[182 190 201]`. The image shows a red square. If Hiroshi removes the `cvtColor` call, the square appears blue, because Matplotlib reads the first channel as red.

Note two details. `cv2.imread` does not raise an error when the file is missing; it returns `None`, so check the result before you use it. And the slice `[50:150, 100:200]` selects rows 50 to 149 and columns 100 to 199.

**On screen (presenter steps):**
1. Open colab.research.google.com and create a new notebook. [VERSION]
2. Click the folder icon in the left panel and upload `tile.jpg`. [VERSION]
3. Paste the code into a cell and run it with Shift+Enter.
4. Point to the printed shape and name each number: height, width, channels.
5. Delete the `cvtColor` call, run again and show the blue square. Put the call back.

## Common Mistake
Many learners read the shape as `(width, height)`, because that is how we say screen sizes, such as 640 × 480. NumPy arrays are rows first, so the shape is `(height, width, channels)`, and a pixel is `img[y, x]`. When you crop or draw, mixing up the order gives wrong results with no error. Also, `cv2.resize` takes the size as `(width, height)`, the opposite order, so always check the shape after resizing.

## Key Takeaways
1. An image is a NumPy array with shape `(height, width, channels)` and, usually, `uint8` values from 0 to 255.
2. OpenCV uses BGR order; convert to RGB before you display the image with Matplotlib or pass it to most models.
3. Index pixels as `img[y, x]`: row first, from the top-left corner, and check that `cv2.imread` did not return `None`.

## Hands-on Exercise
**Task:** In a Colab notebook, load a photo with OpenCV, print its shape, change a block of pixels to red, and display it correctly in RGB order.
**Tools:** Google Colab (free); OpenCV and Matplotlib (already installed in Colab [VERSION]); one photo of an object or scene with no people in it.
**Steps:**
1. Open a new Colab notebook and upload your photo with the folder icon. [VERSION]
2. Load it with `cv2.imread` and stop with a clear message if the result is `None`.
3. Print the shape and data type, and write down which number is the height and which is the width.
4. Print the values of the pixel at the centre of the image: `img[h // 2, w // 2]`.
5. Set a 100 × 100 block of pixels to red using BGR order.
6. Display the image with Matplotlib, first without conversion and then with `cv2.COLOR_BGR2RGB`.
7. Convert the image to greyscale with `cv2.COLOR_BGR2GRAY` and print its new shape.
**What good looks like:** The notebook prints a 3-value shape for the colour image and a 2-value shape for greyscale. The red block appears red only in the converted display, and a short note explains why.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Google Colab interface: the new-notebook flow, the folder icon for uploads, and the pre-installed OpenCV and Matplotlib packages. Free resources and session limits change and are not guaranteed.
- [VERSION] OpenCV function names (`imread`, `cvtColor`, colour conversion codes) should be checked against the OpenCV version installed in Colab at recording time. Code was tested with opencv-python-headless on a synthetic image.
