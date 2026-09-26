# Screen Demo Pack: AI-19 L10 Running YOLO on Images and Video

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L10_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. In a new Colab notebook, run !pip install ultralytics and wait for it to finish
2. Upload port_road.jpg
3. Run the first cell: YOLO('yolo11n.pt'), model('port_road.jpg', conf=0.25), print name, score and box, r.save

**Narration over this clip (for pacing)**

> In a new Colab notebook, he installs the package and waits for it to finish. Then he uploads the road photo and runs the first cell. It loads the nano model, detects objects at a threshold of zero point two five, prints each one, and saves a copy with the boxes drawn.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L10_screen_2.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Open port_road_boxes.jpg from the file panel
2. Point to the printed line for the truck and its box

**Narration over this clip (for pacing)**

> He opens the saved image. You'll see something like a truck with a score of zero point eight eight, inside a clear box. Each printed line shows the class name, the score, and the four corner values of the box in pixels, the same corner format as in the last lesson.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L10_screen_3.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Run the loop over conf 0.1, 0.25 and 0.5
2. Show the three detection counts
3. Display the 0.1 result and point out the two false alarms
4. Display the 0.5 result and point out the missed distant car

**Narration over this clip (for pacing)**

> Now the thresholds. You'll see something like eleven detections at zero point one, six at zero point two five, and four at zero point five. At the lowest value, he finds two false alarms. A container stack is called a truck, and a road sign is called a stop sign. At the highest, one distant car is missed.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L10_screen_4.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Upload port_road.mp4
2. Run model.predict('port_road.mp4', conf=0.25, stream=True, save=True) in a loop
3. Open the saved video from runs/detect/ and play it

**Narration over this clip (for pacing)**

> He chooses zero point two five for now, and notes that he must test it on more images. For video, he runs predict on the clip in streaming mode, which returns one result per frame and keeps memory low. With saving switched on, an annotated video appears in the output folder, and he plays it.

## Production notes for this lesson

- [VERIFY] Ultralytics licence. content.md states AGPL-3.0 with a separate paid enterprise licence for closed commercial use [VERIFY]. The voiceover does not name the licence or make any legal claim; it says only that the Ultralytics YOLO licence must be checked before commercial use, because 'free to download' does not mean 'free for any commercial use'. General guidance, not legal advice.
- [VERIFY] That the default pre-trained detection models are trained on COCO with 80 classes. The voiceover does not state the dataset or the number of classes; it says the models already know many common objects, such as cars, buses and bottles.
- [VERSION] ultralytics package interface (YOLO(), predict, stream, save, Results.save(filename=...), boxes.xyxy), the model name yolo11n.pt and the runs/detect/ output folder change between releases. Code was checked for syntax only.
- Run outputs: content.md gives the detections only as example output (truck 0.88; 11, 6 and 4 detections at conf 0.1, 0.25 and 0.5). The voiceover says 'you'll see something like' before these numbers. Show the real counts on screen; the false alarms named (container stack as truck, road sign as stop sign) and the missed distant car are what happened in Lars's test, so re-record that scene if the recorded run differs.
- Footage: port_road.jpg and port_road.mp4 show vehicles and road only, with no people in close view and no readable number plates.
- Lars Eriksson and the Gothenburg port are fictional; no real company names or logos on containers in footage.
- Screen recording: clean browser profile, no account names or other tabs visible.
