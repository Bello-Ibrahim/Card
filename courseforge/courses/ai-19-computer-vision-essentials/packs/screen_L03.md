# Screen Demo Pack: AI-19 L03 Image Processing with OpenCV

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L03_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Upload form.jpg to a Colab notebook
2. Run the first three lines: cv2.imread, cv2.cvtColor to greyscale, cv2.GaussianBlur with (5, 5)
3. Display blur next to the original image

**Narration over this clip (for pacing)**

> In Colab, she uploads the photo and runs the first three lines. They load the image, turn it grey, and apply a five by five blur. Showing the blurred image next to the original, you can see the paper texture fade away.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L03_screen_2.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run the Canny and findContours lines
2. Run the line that keeps the largest contour with cv2.contourArea and gets cv2.boundingRect
3. Draw the rectangle on a copy of the image with cv2.rectangle and display it

**Narration over this clip (for pacing)**

> Next, she runs edge detection and finds the contours. She keeps the largest outline, because the paper is lighter than the desk, so it forms the biggest shape. She draws its rectangle on a copy of the photo to check it.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L03_screen_3.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Run the crop and threshold lines and the cv2.imwrite line
2. Show the final clean black-and-white image
3. Point to the printed output (900, 1200, 3) -> (760, 540)

**Narration over this clip (for pacing)**

> Then she crops to that rectangle and applies Otsu's threshold. The desk is gone, and the text is black on white. The output line shows nine hundred, twelve hundred, three, turning into seven hundred and sixty, five hundred and forty.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L03_screen_4.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Change the Canny thresholds to (10, 30)
2. Run the cell again and display the edge image
3. Show how many extra edges appear compared with (50, 150)

**Narration over this clip (for pacing)**

> Now watch what happens when she lowers the edge thresholds to ten and thirty. Many more edges appear, from the wood grain and small shadows. The thresholds really matter.

## Production notes for this lesson

- [VERSION] OpenCV function names and signatures (findContours return values, THRESH_OTSU, Canny) must be checked against the OpenCV version in Colab at recording time. Code in content.md was tested with opencv-python-headless on a synthetic image.
- Run outputs: the voiceover states the output '(900, 1200, 3) -> (760, 540)' exactly as content.md reports. Prepare form.jpg at 1200 × 900 pixels and confirm that the recorded run prints exactly this line. If the crop size differs, change the sample photo, not the voiceover, or re-record the scene with 'something like'.
- The number of extra edges with Canny thresholds of 10 and 30 is not given in content.md; the voiceover only says 'many more edges'.
- Fatou Diop and the Dakar microfinance office are fictional. The sample form must contain no real customer data, names or signatures, and no people appear in the photo.
- Screen recording: clean browser profile, no account names or other tabs visible.
