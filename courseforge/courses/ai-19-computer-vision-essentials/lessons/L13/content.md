# L13 Counting and Tracking Objects in Video

Course: AI-19 · Module: M4 · Objectives: O3, O5 · Video: 5 min (screen demo)

## Hook
A bus takes three seconds to cross a junction. At 25 frames per second, a detector sees it in about 75 frames. If you count detections, you count one bus 75 times. To count objects in video, you must know that the bus in frame 10 is the same bus as in frame 11.

## Explanation
**Detection** works on single frames. It says "there is a bus at this position" but does not know that it saw the same bus in the previous frame. **Tracking** links detections across frames and gives each object a **track ID** that stays the same while the object is visible.

Most trackers use two clues to link detections:

- **Motion:** they predict where each object should be in the next frame, based on its recent speed and direction.
- **Overlap or appearance:** they match new boxes to predicted positions, often with IoU from L09, and some also compare how the objects look.

The `ultralytics` package includes trackers such as BoT-SORT and ByteTrack. You call `model.track()` instead of `model.predict()`, and each box then has an `id`. [VERSION]

With IDs, counting is simple and reliable. Draw a **counting line** across the road. For each track, remember the position of its box centre in the previous frame. When the centre moves from one side of the line to the other, count that ID once, and never count it again.

Tracking can fail in predictable ways:

- **ID switch:** two objects pass close to each other and swap IDs.
- **Lost track:** an object is hidden, for example behind a bus, and gets a new ID when it appears again. If this happens near the line, it can be counted twice.
- **Missed detection:** if the detector does not see a small or dark object, the tracker cannot follow it.

Place the line where objects are large, clearly separated and rarely hidden, and compare your count with a manual count on a sample clip.

**Analogy:** Tracking is like a teacher counting children as they come back from a school trip. The teacher does not count every head in every second. The teacher gives each child a name, watches them walk through the gate, and ticks each name once. If two children swap coats, the teacher may tick the wrong name.

## Worked Example
Camila Restrepo works for a transport planning office in Bogotá, Colombia. She wants to count cars and buses entering a junction from one direction. She uses a public traffic camera clip filmed from a height, where faces cannot be seen.

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
LINE_Y = 400                                   # counting line, pixels from top
VEHICLES = {2: "car", 5: "bus", 7: "truck"}    # COCO class IDs
last_y, counted = {}, {}

for r in model.track("junction.mp4", stream=True, persist=True,
                     classes=list(VEHICLES), conf=0.3):
    if r.boxes.id is None:                     # no tracked objects
        continue
    for tid, cls, box in zip(r.boxes.id.int().tolist(),
                             r.boxes.cls.int().tolist(),
                             r.boxes.xyxy.tolist()):
        cy = (box[1] + box[3]) / 2              # centre y of the box
        if last_y.get(tid, cy) < LINE_Y <= cy and tid not in counted:
            counted[tid] = VEHICLES[cls]
        last_y[tid] = cy

names = list(counted.values())
print({v: names.count(v) for v in VEHICLES.values()})
```

Example output: `{'car': 41, 'bus': 6, 'truck': 3}`. Camila counts the same 2-minute clip by hand and finds 44 cars, 6 buses and 3 trucks. She checks the three missed cars: two were hidden behind a bus while crossing the line, and one was a dark car in shadow. She moves the line 80 pixels lower, where vehicles are more separated, and runs the test again.

**On screen (presenter steps):**
1. Load the model and play the first seconds of `junction.mp4` in the notebook.
2. Run the cell above and show the printed counts.
3. Add `save=True` to `model.track()` and open the saved video to show IDs above each box.
4. Draw the counting line on one frame with `cv2.line` and show where it is.
5. Compare the counts with a manual count in a small table.

## Common Mistake
Many learners count unique track IDs across the whole video instead of counting line crossings. This counts parked cars and vehicles that only appear at the edge, and every lost track adds a new ID. Count only objects that cross the line in the correct direction, and check the result against a manual count before you trust it.

## Key Takeaways
1. Detection works frame by frame; tracking gives each object a stable ID across frames.
2. To count, record when each tracked object crosses a line, and count each ID only once.
3. ID switches, lost tracks and missed detections cause counting errors, so always compare with a manual count.

## Hands-on Exercise
**Task:** Add tracking and a counting line to your YOLO video pipeline, count vehicles or people in a short public clip, and compare the result with a manual count.
**Tools:** Google Colab; the `ultralytics` package [VERSION]; a 1 to 2 minute traffic clip with a licence that allows reuse, filmed from a distance. Prefer vehicles to people, and avoid clips where faces are visible.
**Steps:**
1. Watch the clip and choose where to place the counting line.
2. Count the target objects that cross the line by hand and write the numbers down.
3. Run the tracking and counting code with your line position and target classes.
4. Save the annotated video and watch where IDs change or disappear.
5. Compare the automatic and manual counts in a table, and calculate the difference for each class.
6. Move the line or change the confidence threshold once, run again and record the new counts.
**What good looks like:** A table with manual and automatic counts for two line or threshold settings, an annotated video, and 2 or 3 sentences explaining the main source of counting errors.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Curriculum flag: `ultralytics` tracking interface (`model.track`, `persist`, `classes`, `boxes.id`), the included trackers (BoT-SORT, ByteTrack), the model name `yolo11n.pt` and the COCO class IDs used (2 car, 5 bus, 7 truck). The counting logic was run on synthetic tracks; the YOLO calls were checked for syntax only and the counts are example output.
