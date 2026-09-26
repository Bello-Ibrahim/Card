# L12 Reading Text in Images with OCR | Presenter Script

Course: AI-19 · Video: 5 min · Words: 652

## Hook
A program cannot search or add up a photo of a receipt. OCR turns the picture of text into real text. On a clean scan it can work well. On a creased receipt in a dim café, it can fail badly.

## Explain
In the last two lessons, we detected objects. Today, the objects are letters. Optical character recognition, or OCR, usually has two steps. Text detection finds the areas that contain text, and text recognition reads the characters in each area.

We use Tesseract, a free, open-source OCR engine, through a small Python wrapper. You install the engine and one language pack for each language. The codes are f r a for French, p o r for Portuguese and a r a for Arabic, and you can combine them.

Quality depends strongly on the image, and the steps from lesson three help. Enlarge small text, for example to twice the size. Threshold it to black on white, which also removes shadows. Crop away the table and background. And straighten tilted lines, because tilted text is often misread.

Scripts matter too. Arabic is written right to left, and letters change shape by position, so test each script on your own images before you rely on it. To measure OCR, type the true text by hand. The character error rate counts the character edits needed to fix the output, divided by the length of the true text. Zero is perfect.

OCR is like a person reading a note through a dirty window. They may know the language well, but they still misread letters. Cleaning the window often helps more than finding a better reader.

One more thing. Receipts can contain personal data, such as names or card numbers. Use your own receipts or public signs, and never upload other people's documents to online OCR services.

## Demonstrate
Amira Ben Salem manages expenses for a design studio in Tunis, Tunisia. Her receipts are in French and Arabic. She tests OCR on one of her own receipts, with the card number covered, before and after preprocessing.

In Colab, she installs the Tesseract engine with its French, Arabic and Portuguese packs, and then the Python wrapper. She uploads the receipt photo.

The cell reads the raw photo in French and Arabic. Then it cleans a copy. It turns it grey, doubles its size, and applies an adaptive threshold. And it reads the clean version too. She shows both images and both outputs side by side.

On the raw photo, you'll see something like this for the total line. The letter O is read as a zero, and the comma is read as a full stop. That is two wrong characters out of fifteen. The error function gives zero point one three three.

In her test, the French lines are read correctly after preprocessing. She checks the Arabic lines separately, by hand, and plans to compare a second engine, because support for each script must be tested on real receipts.

A common mistake is to test OCR on clean screenshots, and expect the same on phone photos. Real inputs have shadows, folds, tilt and glare. And always set the language. Without the right pack, the engine reads Arabic or accented Portuguese as nonsense, and it does not warn you.

## Recap
Let's recap. First, OCR finds and reads text in images, and Tesseract needs a language pack for each language. Second, preprocessing with OpenCV, like resizing, thresholding, cropping and straightening, often helps more than changing settings. Third, measure quality with the character error rate on real images, separately for each language and script.

## CTA
Now it is your turn. In the exercise below this video, you will run OCR on five receipts or signs in at least two languages, before and after preprocessing, and compare the errors. It takes about forty minutes. Next week is capstone week, and we start by counting moving objects. Counting and Tracking Objects in Video. See you there.

## Thumbnail
Headline: From Photo to Text
Image: Navy background, a creased paper receipt on the left and clean typed text lines on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] OCR engine choice and installation: Tesseract apt-get package names, language codes (fra, por, ara), the pytesseract.image_to_string interface, and the alternative engines EasyOCR and PaddleOCR must be checked at recording time.
- [VERIFY] Quality of Arabic OCR support in the chosen engine must be tested on real Arabic receipts before the lesson describes it. The voiceover makes no claim about Arabic OCR quality. It says only that Amira checks the Arabic lines separately and plans to compare a second engine, and that learners should test each script on their own images. content.md's hypothetical detail that 'the Arabic shop name is still partly wrong' is left out of the voiceover.
- Run outputs: the CER value 0.133 for 'TOTAL 12,500 DT' vs 'T0TAL 12.500 DT' was run and checked, and the voiceover states it as about zero point one three. The OCR text itself is example output from a hypothetical case, so the voiceover says 'you'll see something like' for the raw result and 'in her test' for the cleaned result. Show the real OCR output on screen.
- Privacy: use a receipt with the card number and any names covered. Do not upload other people's documents to online OCR services. No people or hands with jewellery in the receipt shots.
- Amira Ben Salem and the Tunis design studio are fictional; the receipt must show no real shop name or logo.
- Screen recording: clean browser profile, no account names or other tabs visible.
