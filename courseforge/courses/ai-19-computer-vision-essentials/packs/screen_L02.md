# Screen Demo Pack: AI-19 L02 Images as Numbers: Pixels, Channels and Colour

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L02_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open colab.research.google.com and create a new notebook
2. Click the folder icon in the left panel
3. Upload tile.jpg and show it in the file list

**Narration over this clip (for pacing)**

> He opens Google Colab and creates a new notebook. Then he clicks the folder icon on the left and uploads one photo, called tile dot j p g. Menus in Colab change, so follow the idea rather than the exact screen.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L02_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Paste the code from content.md into a cell: cv2.imread, print shape and dtype, print img[0, 0], set img[50:150, 100:200] = (0, 0, 255), plt.imshow with cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
2. Highlight the line that sets the block to (0, 0, 255)
3. Run the cell with Shift+Enter

**Narration over this clip (for pacing)**

> He pastes a short cell. It loads the photo with OpenCV, prints the shape and the data type, and prints the top-left pixel. Then it paints a block of pixels red, using blue, green, red order, and displays the image with Matplotlib after converting it to RGB.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L02_screen_3.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Point to the printed output (480, 640, 3) uint8
2. Name each number in turn: height, width, channels
3. Point to the printed top-left pixel values and label them B, G, R

**Narration over this clip (for pacing)**

> The output shows four hundred and eighty, six hundred and forty, three, and the type is u-int-eight. That is four hundred and eighty rows of height, six hundred and forty columns of width, and three colour channels. The top-left pixel shows three numbers, something like one hundred and eighty, in blue, green, red order.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L02_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Show the displayed image with the red square
2. Delete the cv2.cvtColor call so plt.imshow(img) receives BGR
3. Run again and show the blue square
4. Put the cvtColor call back and run once more

**Narration over this clip (for pacing)**

> The image shows a red square, as expected. Now he deletes the conversion call and runs the cell again. The square is blue. Matplotlib read the first channel, which is blue, as red. He puts the call back.

## Production notes for this lesson

- [VERSION] Google Colab interface: the new-notebook flow, the folder icon for uploads, and the pre-installed OpenCV and Matplotlib packages. Check against the live tool before recording and adjust screen_steps to the live labels. The voiceover avoids exact menu names except the folder icon.
- [VERSION] OpenCV function names (imread, cvtColor, colour conversion codes): check against the OpenCV version installed in Colab at recording time. Code in content.md was tested with opencv-python-headless on a synthetic image.
- Run outputs: the voiceover states the shape 480, 640, 3 and the type uint8 exactly as content.md reports. Prepare tile.jpg at exactly 640 × 480 pixels so the recorded output matches. The top-left pixel value is NOT read aloud: content.md gives it only as an example, so the voiceover says 'something like'.
- Hiroshi Tanaka and the Osaka tile factory are fictional. Use an unbranded photo of ceramic tiles with no people in it.
- Screen recording: clean browser profile, no account names, bookmarks or other tabs visible. Speed up any waiting time for the Colab runtime to connect.
