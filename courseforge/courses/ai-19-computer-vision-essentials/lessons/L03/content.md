# L03 Image Processing with OpenCV

Course: AI-19 · Module: M1 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Not every vision problem needs a neural network. Some problems can be solved with six lines of OpenCV that run in milliseconds on any laptop. And when you do use a model, the same six lines often decide whether it succeeds or fails.

## Explanation
OpenCV gives you fast, predictable operations on image arrays. These are the core ones you will use throughout the course:

- **Resize** (`cv2.resize`) changes the size. Models expect a fixed input size, and smaller images process faster. Remember that the size argument is `(width, height)`.
- **Crop** is plain NumPy slicing: `img[y1:y2, x1:x2]`. No function is needed.
- **Greyscale** (`cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`) reduces 3 channels to 1. Many steps, such as thresholding and edge detection, work on one channel.
- **Blur** (`cv2.GaussianBlur`) averages each pixel with its neighbours. It removes small noise, such as paper texture or camera grain, so later steps react to real structure. The kernel size must be odd, for example `(5, 5)`.
- **Threshold** turns a greyscale image into pure black and white. `cv2.threshold` with the `THRESH_OTSU` flag chooses the cut-off value for you from the image histogram. `cv2.adaptiveThreshold` chooses a different value for each small area, which helps when the lighting is uneven.
- **Edge detection** (`cv2.Canny`) marks pixels where brightness changes sharply. Its two numbers are a low and a high threshold: raise them to keep only strong edges.
- **Contours** (`cv2.findContours`) join edge pixels into outlines. From a contour you can get its area or a bounding rectangle.

These steps are used in two ways. First, as **preprocessing** before a model: resizing, correcting colour and removing noise make inputs more like the training data. Second, as a **complete solution** for simple, controlled scenes, such as a document on a plain desk or a part on a conveyor belt with fixed lighting.

**Analogy:** Image processing is like preparing vegetables before cooking. You wash them (blur away noise), cut them to size (resize and crop) and sort them (threshold). A good cook can still make a meal from badly prepared vegetables, but the result is better and more predictable when the preparation is done well.

## Worked Example
Fatou Diop works for a microfinance office in Dakar, Senegal. Field staff photograph paper forms on their desks, and she needs a clean black-and-white image of each form for archiving. She uses a sample form with no real customer data.

```python
import cv2

img = cv2.imread("form.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blur, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)
page = max(contours, key=cv2.contourArea)     # largest outline
x, y, w, h = cv2.boundingRect(page)

crop = blur[y:y + h, x:x + w]
_, clean = cv2.threshold(crop, 0, 255,
                         cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite("form_clean.png", clean)
print(img.shape, "->", clean.shape)
```

Example output: `(900, 1200, 3) -> (760, 540)`. The paper is lighter than the desk, so its outline is the largest contour. The crop removes the desk, and Otsu's threshold makes the text black on white.

This simple version has limits. It uses an upright rectangle, so a form photographed at an angle keeps some desk in the corners. A later improvement would find the four corners and correct the perspective with `cv2.getPerspectiveTransform`.

**On screen (presenter steps):**
1. Upload `form.jpg` to a Colab notebook.
2. Run the first three lines and display `blur` next to the original.
3. Run the Canny and contour lines. Draw the rectangle on a copy with `cv2.rectangle` and display it.
4. Run the crop and threshold lines and show the final image.
5. Change the Canny thresholds to `(10, 30)` and show how many extra edges appear.

## Common Mistake
Many learners copy threshold and kernel values from a tutorial and expect them to work on every photo. These values depend on image size, lighting and noise. A `(5, 5)` blur that suits a 1,200-pixel photo may remove the text from a 300-pixel photo. Display the image after every step, and test your pipeline on several photos with different lighting before you trust it. When lighting varies a lot, try `adaptiveThreshold` instead of one global value.

## Key Takeaways
1. The core OpenCV steps are resize, crop, greyscale, blur, threshold, edge detection and contours, and each one returns a new array you can inspect.
2. Use these steps to prepare images for a model, or on their own when the scene is simple and controlled.
3. Parameter values depend on the image, so display every intermediate result and test on varied photos.

## Hands-on Exercise
**Task:** Build a small pipeline that turns a phone photo of a document into a clean black-and-white image: greyscale, blur, threshold and crop.
**Tools:** Google Colab; OpenCV and Matplotlib; a phone photo of a printed page with no personal or confidential information (for example, a page from a public brochure).
**Steps:**
1. Photograph the page on a plain, darker surface and upload the photo to Colab.
2. Load it, convert it to greyscale and apply a `(5, 5)` Gaussian blur.
3. Find edges with Canny, find the largest contour and crop to its bounding rectangle.
4. Apply Otsu's threshold to the crop and save the result.
5. Display the original, the edges and the final image side by side with Matplotlib subplots.
6. Try `cv2.adaptiveThreshold` on the same crop and compare the two results.
7. Test the pipeline on a second photo taken in weaker light and write one sentence on what changed.
**What good looks like:** The final image shows only the page, with dark text on a white background. The notebook shows each step, and the note explains which threshold method worked better and why.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Curriculum flag for L02-L05: OpenCV function names and signatures (`findContours` return values, `THRESH_OTSU`, `Canny`) should be checked against the OpenCV version in Colab at recording time. Code was tested with opencv-python-headless on a synthetic image.
