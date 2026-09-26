# Screen Demo Pack: AI-19 L12 Reading Text in Images with OCR

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L12_screen_1.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Run !apt-get install -y tesseract-ocr tesseract-ocr-fra tesseract-ocr-ara tesseract-ocr-por
2. Run !pip install pytesseract
3. Upload receipt.jpg

**Narration over this clip (for pacing)**

> In Colab, she installs the Tesseract engine with its French, Arabic and Portuguese packs, and then the Python wrapper. She uploads the receipt photo.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L12_screen_2.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Run the OCR cell: raw image_to_string with lang='fra+ara', then greyscale, resize fx=2, adaptiveThreshold, and image_to_string on the clean image
2. Show the raw and cleaned images side by side
3. Show both OCR outputs side by side

**Narration over this clip (for pacing)**

> The cell reads the raw photo in French and Arabic. Then it cleans a copy. It turns it grey, doubles its size, and applies an adaptive threshold. The threshold makes the text black on white and removes the shadow of the fold. And it reads the clean version too. She shows both images and both outputs side by side.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L12_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Point to the raw total line: T0TAL 12.500 DT
2. Type the true total line: TOTAL 12,500 DT
3. Run the cer function and show 0.133

**Narration over this clip (for pacing)**

> On the raw photo, you'll see something like this for the total line. The letter O is read as a zero, and the comma is read as a full stop. That is two wrong characters out of fifteen. The error function gives zero point one three three.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L12_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Calculate the CER for the cleaned total line
2. Scroll to the Arabic lines in both outputs and compare them with the receipt

**Narration over this clip (for pacing)**

> In her test, the French lines are read correctly after preprocessing. She checks the Arabic lines separately, by hand, and plans to compare a second engine, because support for each script must be tested on real receipts.

## Production notes for this lesson

- [VERSION] OCR engine choice and installation: Tesseract apt-get package names, language codes (fra, por, ara), the pytesseract.image_to_string interface, and the alternative engines EasyOCR and PaddleOCR must be checked at recording time.
- [VERIFY] Quality of Arabic OCR support in the chosen engine must be tested on real Arabic receipts before the lesson describes it. The voiceover makes no claim about Arabic OCR quality. It says only that Amira checks the Arabic lines separately and plans to compare a second engine, and that learners should test each script on their own images. content.md's hypothetical detail that 'the Arabic shop name is still partly wrong' is left out of the voiceover.
- Run outputs: the CER value 0.133 for 'TOTAL 12,500 DT' vs 'T0TAL 12.500 DT' was run and checked, and the voiceover states it as about zero point one three. The OCR text itself is example output from a hypothetical case, so the voiceover says 'you'll see something like' for the raw result and 'in her test' for the cleaned result. Show the real OCR output on screen.
- Privacy: use a receipt with the card number and any names covered. Do not upload other people's documents to online OCR services. No people or hands with jewellery in the receipt shots.
- Amira Ben Salem and the Tunis design studio are fictional; the receipt must show no real shop name or logo.
- Screen recording: clean browser profile, no account names or other tabs visible.
