# Screen Demo Pack: AI-19 L14 Responsible Vision: Privacy, Bias and Licences

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L14_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Add the blur_boxes function to the L13 notebook
2. In the YOLO loop, select person boxes with the class filter and call blur_boxes on a copy of the frame
3. Run the cell so each frame is blurred before it is written

**Narration over this clip (for pacing)**

> He adds a small blur function to his notebook from the last lesson. It takes a frame and a list of boxes, keeps each box inside the image, and applies a strong blur inside it. In the tracking loop, he selects the person boxes and blurs them before each frame is written.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L14_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Play the output video
2. Pause on a frame with blurred people and point to the whole-body blur

**Narration over this clip (for pacing)**

> He plays the output and pauses on a frame with workers in the yard. Each person is blurred from head to foot. He blurs the whole person box, not only the face, because face detectors miss small, turned or shadowed faces, and clothes can also identify people.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L14_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Step through sample frames and check every person is blurred
2. Show the fitness check text cell with the headings Accuracy, Speed, Privacy, Licence, Decision

**Narration over this clip (for pacing)**

> He also checks sample frames by eye, because one missed detection means one unblurred person. Then he writes his fitness check in a text cell, with five headings. Accuracy, speed, privacy, licence, and decision.

## Production notes for this lesson

- [REGION] Laws on cameras, face data, consent, notices and video storage periods differ by country and sometimes by city. The voiceover gives general guidance and says it is not legal advice.
- [VERIFY] Ultralytics licence (content.md: AGPL-3.0 with a separate commercial licence [VERIFY]). The voiceover does not name the licence or make legal claims; it says the Ultralytics YOLO licence must be checked before commercial use, and that Oluwaseun needs a legal review before offering the system to other depots.
- [VERSION] OpenCV bundled face detection models (Haar cascade files via cv2.data.haarcascades) and the ultralytics result attributes (boxes.cls, orig_img). The blur_boxes function was run with opencv-python-headless on a synthetic frame.
- No face recognition anywhere in this lesson. The demo blurs whole person boxes from the detector; it does not identify anyone. Face detectors are mentioned only as the weaker option.
- Footage: the depot clip must be staged or rights-cleared, filmed from a distance, with consenting workers. In every frame shown on screen, whole people must be blurred; check sample frames by eye before export. No readable number plates or company names on vans.
- Fitness-check figures (within 5% on 10 daytime clips, about 40 seconds per 1-minute clip, deletion after 24 hours) are example values from content.md, not benchmarks; the voiceover calls them his example results.
- Oluwaseun Adeyemi and the Lagos depot are fictional.
- Screen recording: clean browser profile, no account names or other tabs visible.
