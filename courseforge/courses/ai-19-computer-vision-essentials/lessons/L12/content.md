# L12 Reading Text in Images with OCR

Course: AI-19 · Module: M3 · Objectives: O3, O5 · Video: 5 min (screen demo)

## Hook
A program cannot search or add up a photo of a receipt. OCR turns the picture of text into real text. On a clean scan it can work well. On a creased receipt photographed in a dim café it can fail badly, and preprocessing makes much of the difference.

## Explanation
**Optical character recognition (OCR)** usually has two steps: **text detection** finds areas that contain text, and **text recognition** reads the characters in each area.

In this course we use **Tesseract**, a free, open-source OCR engine, through the `pytesseract` Python wrapper. In Colab you install the engine and one language pack per language, then the wrapper. [VERSION] Language codes are `fra` for French, `por` for Portuguese and `ara` for Arabic. You can combine them, for example `lang="fra+ara"`. Other open-source engines, such as EasyOCR and PaddleOCR, may handle photos better; compare them if Tesseract fails. [VERSION]

Quality depends strongly on the image. Useful preprocessing steps from L03:

- **Greyscale and resize:** small text becomes easier to read when you enlarge the image, for example by 2×.
- **Threshold:** Otsu or adaptive thresholding makes text black on white and removes shadows.
- **Crop:** remove the table, hands and background, so the engine only sees the document.
- **Deskew:** straighten tilted text; strongly tilted lines are often misread.

Scripts also matter. Arabic is written right to left, and letters change shape depending on their position in a word. OCR quality for Arabic can differ a lot between engines, language models and fonts, so test it on your own images before you rely on it. [VERIFY]

To measure OCR, type the true text by hand and compare. The **character error rate (CER)** is the number of character edits (insertions, deletions and substitutions) needed to turn the OCR output into the true text, divided by the length of the true text. A CER of 0 is perfect.

Receipts can contain personal data, such as names or card numbers. Use your own receipts or public signs, and do not upload other people's documents to online OCR services.

**Analogy:** OCR is like a person reading a handwritten note through a dirty window. They may know the language well, but they will still misread letters. Cleaning the window (preprocessing) often helps more than finding a better reader.

## Worked Example
Amira Ben Salem manages expenses for a design studio in Tunis, Tunisia, with receipts in French and Arabic. She tests OCR on one of her own receipts, card number covered, before and after preprocessing.

**On screen (presenter steps):**
1. In a Colab cell, run `!apt-get install -y tesseract-ocr tesseract-ocr-fra tesseract-ocr-ara tesseract-ocr-por` and `!pip install pytesseract`. [VERSION]
2. Upload `receipt.jpg` and run the cell below.
3. Show the raw and cleaned images and both OCR outputs side by side.
4. Type the true total line and calculate the CER for both outputs.

```python
import cv2
import pytesseract

img = cv2.imread("receipt.jpg")
raw = pytesseract.image_to_string(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
                                  lang="fra+ara")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
clean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                              cv2.THRESH_BINARY, 31, 15)
cleaned = pytesseract.image_to_string(clean, lang="fra+ara")
print(raw, "-----", cleaned, sep="\n")
```

A short function calculates the CER:

```python
def cer(truth, pred):
    """Character error rate: edit distance / length of the truth."""
    prev = list(range(len(pred) + 1))
    for i, t in enumerate(truth, 1):
        cur = [i]
        for j, p in enumerate(pred, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (t != p)))
        prev = cur
    return prev[-1] / max(len(truth), 1)

print(round(cer("TOTAL 12,500 DT", "T0TAL 12.500 DT"), 3))   # 0.133
```

In this hypothetical case, the raw image gives `T0TAL 12.500 DT`, with two wrong characters in 15, so the CER is about 0.13. After preprocessing, the French lines are read correctly. The Arabic shop name is still partly wrong, so Amira decides to check the Arabic results by hand and to compare a second engine.

## Common Mistake
Many developers test OCR on clean, printed screenshots and expect the same quality on phone photos. Real inputs have shadows, folds, tilt, glare and mixed languages. Test on real photos, measure CER for each language separately, and always set the language explicitly. Without the correct language pack, the engine reads Arabic or accented Portuguese characters as nonsense, and it does not warn you.

## Key Takeaways
1. OCR finds and reads text in images; Tesseract needs a language pack for each language, such as `fra`, `por` and `ara`.
2. Preprocessing with OpenCV, such as resizing, thresholding, cropping and deskewing, often improves OCR more than changing settings.
3. Measure quality with the character error rate on real images, separately for each language and script.

## Hands-on Exercise
**Task:** Run OCR on 5 receipt or sign images in at least 2 languages, before and after OpenCV preprocessing, and compare the character errors.
**Tools:** Google Colab; Tesseract with language packs and `pytesseract` [VERSION]; OpenCV; 5 photos of your own receipts (cover card numbers and names) or public signs.
**Steps:**
1. Install Tesseract, the language packs you need and `pytesseract`.
2. Photograph or choose 5 images in at least 2 languages, for example French and Arabic, or Portuguese and English.
3. For each image, type the true text of 2 or 3 important lines by hand.
4. Run OCR on the raw image with the correct language code.
5. Preprocess (greyscale, resize, threshold, crop) and run OCR again.
6. Calculate the CER for each image before and after, and put the results in a table.
7. Write 2 sentences on which language or script had the most errors and why.
**What good looks like:** A table of 5 images with CER before and after preprocessing, the language of each image, and a short note on the hardest cases.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Curriculum flag: OCR engine choice and installation. Tesseract `apt-get` package names, language codes (`fra`, `por`, `ara`), the `pytesseract.image_to_string` interface, and the alternative engines EasyOCR and PaddleOCR must be checked at recording time. OCR code was checked for syntax only; OCR text is example output. The `cer` function was run and checked.
- [VERIFY] Curriculum flag: quality of Arabic OCR support in the chosen engine must be tested on real Arabic receipts before the lesson describes it.
