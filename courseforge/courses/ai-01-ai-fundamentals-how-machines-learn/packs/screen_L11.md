# Screen Demo Pack: AI-01 L11 Build Your Own Image Classifier

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_L11_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open Google Teachable Machine in a clean browser window
2. Click the button to get started
3. Choose Image Project
4. Choose the standard image model option
5. Show the empty project with two default classes and the Train and Preview panels

**Narration over this clip (for pacing)**

> First, open Teachable Machine in your browser. Start a new project, and choose a standard image project. The interface may look a little different when you try it, so follow the ideas, not the exact screen.

## Clip 2: scene 8

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_L11_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Click the name of the first default class and type 'plastic bottle'
2. Click the name of the second default class and type 'metal can'
3. Point to the option to add a class, without clicking it

**Narration over this clip (for pacing)**

> Next, rename the two empty classes. Chiamaka calls them plastic bottle, and metal can. These are the labels. You can add a third class if you want.

## Clip 3: scene 9

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_L11_screen_3.mp4`
- **Target length:** about 19 seconds

**Steps**

1. In the 'plastic bottle' class, click Webcam and allow camera access
2. Hold to record while turning several unbranded bottles of different sizes and colours, some crushed, until about 30 images appear
3. Repeat in the 'metal can' class with several cans, some crushed, until about 30 images appear
4. Briefly show the Upload option as the alternative
5. Scroll through the thumbnails to show the variety

**Narration over this clip (for pacing)**

> Now add the data. Use the Webcam option to record frames of each object, or the Upload option to choose image files. Chiamaka records about thirty images per class. She uses different sizes and colours, different angles, and some crushed and some whole items.

## Clip 4: scene 10

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_L11_screen_4.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Click Train
2. Show the training progress message
3. Speed up the wait if needed
4. Show that training is complete

**Narration over this clip (for pacing)**

> Then click Train, and keep the browser tab open until it finishes. This is the training phase. The model is nudging its dials to match the images to the labels.

## Clip 5: scene 11

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_L11_screen_5.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Turn on the webcam in the Preview area
2. Hold up new bottles and cans not used in training, one at a time
3. Pause on the confidence bars for a correct bottle and a correct can
4. Show a simple tally on a sticky note: 8 of 10 correct

**Narration over this clip (for pacing)**

> Now test it in the preview area, with ten new items it has never seen. For each one, read the confidence bars. Chiamaka's model gets eight out of ten right.

## Clip 6: scene 12

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_L11_screen_6.mp4`
- **Target length:** about 24 seconds

**Steps**

1. In Preview, hold a clear plastic bottle in front of a bright window: the bar leans to 'metal can'
2. Hold a very shiny can: show the wrong or uncertain result
3. Go back to the 'plastic bottle' class and record extra images near the window
4. Click Train again and wait
5. Test again with new items near the window and show the improved result

**Narration over this clip (for pacing)**

> It fails on a clear bottle held in front of a window, and on a very shiny can. Her training images all had dull indoor light. So the model may have learned that bright and shiny means can. She adds images taken near the window, trains again, and tests with new items. The results improve.

## Clip 7: scene 13

- **Filename:** `ai-01-ai-fundamentals-how-machines-learn_L11_screen_7.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Point to the advanced settings and export area without opening them
2. Take a screenshot of both classes with their image thumbnails
3. Take a screenshot of the Preview area showing one test result with its confidence bars

**Narration over this clip (for pacing)**

> You do not need the advanced settings or the export options for your capstone. But before you close the tab, take two screenshots. One of your classes, and one of a test result. You will need them as evidence.

## Production notes for this lesson

- [VERSION] Record the screen demo in Google Teachable Machine only after checking the live tool: project type names, the default class names, the Webcam and Upload options, the Train button, the Preview area, advanced settings and export options. Adjust the screen_steps to the live labels; the voiceover avoids exact button names except Train, Webcam, Upload and Preview, so change those words too if the live tool uses different ones.
- [VERSION] The voiceover says learners do not need the advanced or export options. Keep this if it still holds for the live tool.
- [VERIFY] Where Teachable Machine stores images during and after training is NOT stated in the voiceover. It only tells learners to check the tool's privacy information. Confirm from the tool's current privacy information before adding any claim.
- Screen recording: record with the OBS Screen Demo Pack in a clean browser profile with no bookmarks, extensions, account names or other tabs visible. Use a plain wall background, and do not show any person on the webcam; only hands holding objects.
- Chiamaka's recycling project in Enugu is fictional; the demo recreates her bottle-and-can example. Use unbranded bottles and cans, or turn labels away from the camera.
- Scenes 7 to 13 are screen scenes. Where the real training time is longer than the scene, speed up the recording or cut the progress bar.
