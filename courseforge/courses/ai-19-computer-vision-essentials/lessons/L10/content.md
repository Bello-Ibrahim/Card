# L10 Running YOLO on Images and Video

Course: AI-19 · Module: M3 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
With one install command and a few lines of Python, you can find cars, buses, people and bottles in any photo or video. The code is short. The important decisions are which confidence threshold to use and which licence applies to your project.

## Explanation
**YOLO** ("You Only Look Once") is a family of fast object detectors. They look at the whole image in one pass and predict all boxes, classes and scores together. This makes them popular for video. In this course we use the open-source `ultralytics` Python package, which runs several YOLO versions with the same simple interface. [VERSION]

The pre-trained detection models are trained on the COCO dataset, which has 80 common object classes, such as person, car, bus, truck, bicycle, bottle and chair. [VERIFY] Model files come in sizes: "n" (nano) is the smallest and fastest, and larger sizes are slower but usually more accurate. Model names such as `yolo11n.pt` change with each new release. [VERSION]

The key setting is the **confidence threshold** (`conf`). The model drops every detection with a lower score.

- A **low** threshold (for example 0.1) keeps more real objects, but adds false alarms: shadows called "car", signs called "person".
- A **high** threshold (for example 0.7) gives fewer false alarms but misses small, distant or partly hidden objects.

In L08 terms, lowering the threshold usually raises recall and lowers precision. There is no universal best value; you choose it by testing on your own images.

**Licence.** The `ultralytics` package and its models are released under the AGPL-3.0 licence, with a separate paid enterprise licence from Ultralytics for closed-source commercial use. [VERIFY] AGPL-3.0 is a copyleft licence: if you use the code in a product, including one that people use over a network, you may have to publish your own source code under the same licence. Learning and open projects are usually fine, but check the current terms, or ask a legal adviser, before any commercial use.

**Analogy:** The confidence threshold works like the sensitivity setting on a metal detector at the beach. Turn it up and it beeps for every coin, and also for every bottle cap. Turn it down and it stays quiet for bottle caps, but it also misses small coins buried deep. You adjust it for what you are searching for.

## Worked Example
Lars Eriksson plans lorry traffic at a container port in Gothenburg, Sweden. He wants to know if a pre-trained model can detect trucks and cars in photos from a public road camera near the port, with no people in close view.

First, in a Colab cell, he installs the package: `!pip install ultralytics`. [VERSION]

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")               # downloads on first use
r = model("port_road.jpg", conf=0.25)[0]
for box in r.boxes:
    name = r.names[int(box.cls)]
    print(name, round(float(box.conf), 2), box.xyxy[0].int().tolist())
r.save(filename="port_road_boxes.jpg")

for conf in (0.1, 0.25, 0.5):
    n = len(model("port_road.jpg", conf=conf, verbose=False)[0].boxes)
    print(f"conf={conf}: {n} detections")
```

Example output:

```text
truck 0.88 [412, 190, 640, 355]
car 0.74 [120, 230, 215, 290]
conf=0.1: 11 detections
conf=0.25: 6 detections
conf=0.5: 4 detections
```

At 0.1 Lars finds two false alarms: a container stack called "truck" and a road sign called "stop sign". At 0.5 one distant car is missed. He chooses 0.25 for now and notes that he must test it on more images.

For video, he streams the results frame by frame so the notebook does not run out of memory:

```python
counts = []
for r in model.predict("port_road.mp4", conf=0.25, stream=True, save=True):
    counts.append(len(r.boxes))
print("frames:", len(counts), "max objects in one frame:", max(counts))
```

`save=True` writes an annotated video into a `runs/detect/` folder. [VERSION]

**On screen (presenter steps):**
1. In a new Colab notebook, run `!pip install ultralytics` and wait for it to finish.
2. Upload `port_road.jpg` and run the first cell. Show the printed detections.
3. Open `port_road_boxes.jpg` from the file panel and point to each box and its label.
4. Show the three threshold counts, and display the 0.1 result to point out false alarms.
5. Run the video cell and open the saved video from the `runs/detect/` folder.

## Common Mistake
Many learners pick one threshold on one image and use it everywhere. A threshold that works on a clear daytime photo may miss most objects at night or in rain. Test thresholds on a varied set of images and record false alarms and missed objects for each one. A second mistake is ignoring the licence because the package installs for free. "Free to download" does not mean "free for any commercial use".

## Key Takeaways
1. The `ultralytics` package runs pre-trained YOLO models on images and video in a few lines, and returns boxes, classes and scores.
2. The confidence threshold trades false alarms against missed objects; choose it by testing on varied images.
3. Check the licence before commercial use: the package is AGPL-3.0, with a separate commercial licence, and terms can change.

## Hands-on Exercise
**Task:** Run a pre-trained YOLO model on 5 images and one short video, try 3 confidence thresholds, and record how the number of detections and false alarms changes.
**Tools:** Google Colab; the `ultralytics` package [VERSION]; 5 photos of streets, car parks, shelves or kitchens, and one short clip (10 to 20 seconds) with a licence that allows reuse. Prefer scenes with objects and vehicles, and avoid close views of people.
**Steps:**
1. Install `ultralytics` and load the smallest pre-trained detection model.
2. Run the model on each image at `conf` 0.1, 0.25 and 0.5 and save the annotated images.
3. For each image and threshold, count the detections, the false alarms and the missed objects you can see.
4. Run the model on the video at your preferred threshold with `stream=True` and `save=True`.
5. Watch the saved video and note two moments where the model fails.
6. Record in a table which threshold you would choose and why.
**What good looks like:** A table with 15 rows (5 images × 3 thresholds) showing detections, false alarms and misses, an annotated video, and a short justification for one threshold that mentions the trade-off.
**Time:** about 35 minutes

## Review Flags
- [VERIFY] Curriculum flag: Ultralytics licence terms. The lesson states AGPL-3.0 with a separate paid enterprise licence for closed commercial use; a reviewer must confirm current terms before scripting L10, L11, L14 and the capstone. The lesson gives general guidance, not legal advice.
- [VERIFY] Confirm that the default pre-trained detection models are trained on COCO with 80 classes, including the class names used in the example.
- [VERSION] `ultralytics` package interface (`YOLO()`, `predict`, `stream`, `save`, `Results.save(filename=...)`, `boxes.xyxy`), the model name `yolo11n.pt`, and the `runs/detect/` output folder change between releases. Code was checked for syntax only; detections are example output.
