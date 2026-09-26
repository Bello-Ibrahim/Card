# Screen Demo Pack: AI-19 L13 Counting and Tracking Objects in Video

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L13_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Load the model and play the first seconds of junction.mp4 in the notebook
2. Scroll through the cell: LINE_Y, the VEHICLES class filter, model.track with stream and persist
3. Highlight the if line that counts each ID once when it crosses the line

**Narration over this clip (for pacing)**

> In Colab, she loads the model and plays the first seconds of the clip. Her cell tracks only cars, buses and trucks. For each tracked vehicle, it remembers the box centre from the last frame, and counts the ID once when the centre moves down across the line.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L13_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run the cell and show the printed counts
2. Add save=True to model.track() and run again
3. Open the saved video and show the IDs above each box

**Narration over this clip (for pacing)**

> She runs it. You'll see something like forty-one cars, six buses and three trucks. Then she saves the annotated video and opens it. Every vehicle has an ID above its box. The IDs make it easy to see where tracking works, and where it breaks.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L13_screen_3.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Draw the counting line on one frame with cv2.line and display it
2. Show a small table comparing automatic and manual counts per class

**Narration over this clip (for pacing)**

> She draws the counting line on one frame, so everyone can see where it is. Then she compares the result with her own count by hand. In her case, the hand count found forty-four cars, six buses and three trucks. Three cars are missing.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L13_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Step through the saved video to the frames where the three cars were missed
2. Change LINE_Y to 80 pixels lower and run the cell again

**Narration over this clip (for pacing)**

> She checks the three missed cars. Two were hidden behind a bus while crossing the line. One was a dark car in shadow. So she moves the line eighty pixels lower, where vehicles are more separated, and runs the test again.

## Production notes for this lesson

- [VERSION] ultralytics tracking interface (model.track, persist, classes, boxes.id), the included trackers (BoT-SORT, ByteTrack), the model name yolo11n.pt and the COCO class IDs used (2 car, 5 bus, 7 truck) must be checked at recording time. The counting logic was run on synthetic tracks; the YOLO calls were checked for syntax only.
- Run outputs: content.md gives {'car': 41, 'bus': 6, 'truck': 3} only as example output. The voiceover says 'you'll see something like' before these counts. Camila's manual count (44 cars, 6 buses, 3 trucks) and the cause of the three missed cars are described as her results; if the recorded run differs, show the real counts and keep the 'something like' wording, and re-record the comparison scene.
- Footage: junction.mp4 must be a public traffic clip, filmed from a height, showing vehicles only, with no visible faces and no readable number plates. Check that its licence allows reuse.
- Camila Restrepo and the Bogotá transport office are fictional; no real agency names or logos.
- Screen recording: clean browser profile, no account names or other tabs visible.
