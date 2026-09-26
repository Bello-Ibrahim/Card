# Screen Demo Pack: AI-19 L04 Working with Video Frames

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L04_screen_1.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Upload belt.mp4 (a 10-second clip) to Colab
2. Run only the first four lines: cv2.VideoCapture, CAP_PROP_FPS, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT
3. Print fps, w and h

**Narration over this clip (for pacing)**

> He uploads a ten-second clip to Colab and runs only the first few lines. They open the video and read its frame rate, width and height, which he prints to check.

## Clip 2: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L04_screen_2.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Paste and run the full cell from content.md: VideoWriter with mp4v and isColor=False, the while loop with cap.read, cvtColor to grey, putText 'frame n', out.write
2. Highlight cap.release() and out.release()
3. Point to the printed summary: 250 frames at 25 FPS, size 640x360

**Narration over this clip (for pacing)**

> Then he runs the full cell. It creates a writer with colour switched off, and loops through the frames. Each frame is turned grey, gets its number written in white, and is saved. Finally, both objects are released. The summary reads two hundred and fifty frames at twenty-five frames per second, size six hundred and forty by three hundred and sixty.

## Clip 3: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L04_screen_3.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Open the file panel and download belt_gray.mp4
2. Play the video and pause on one frame to show the frame number

**Narration over this clip (for pacing)**

> He downloads the new file from the file panel and plays it. Every frame is grey, with its number in the corner.

## Clip 4: scene 13

- **Filename:** `ai-19-computer-vision-essentials_L04_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Change isColor=False to isColor=True
2. Run the cell again and show that no exception appears
3. Show that belt_gray.mp4 is broken or very small in the file panel
4. Change it back to isColor=False

**Narration over this clip (for pacing)**

> Now he breaks it on purpose. He switches colour on in the writer and runs the cell again. There is no error message, but the output file is broken or very small. He switches it back.

## Production notes for this lesson

- [VERSION] Video codec support (mp4v, .mp4) depends on the OpenCV build in Colab; check that the output plays at recording time. Colab file panel download steps also change. OpenCV function names for L02-L05 must be checked. Code in content.md was tested with opencv-python-headless on a synthetic clip.
- [VERIFY] Confirm that the stock video site the course recommends allows reuse of its clips for training exercises. The voiceover does not name a site.
- Demo footage: belt.mp4 must show only fruit on a sorting belt, with no identifiable people or hands with jewellery, tattoos or badges.
- Run outputs: the voiceover states '250 frames at 25 FPS, size 640x360' exactly as content.md reports. Prepare belt.mp4 as a 10-second clip at 25 FPS and 640 × 360 so the recorded run prints exactly this line.
- The size of the broken file when isColor is True is not given in content.md; the voiceover only says 'broken or very small'.
- Mateus Oliveira and the Petrolina packing plant are fictional; no company names or logos in footage.
