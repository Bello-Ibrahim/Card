# L13 Counting and Tracking Objects in Video | Presenter Script

Course: AI-19 · Video: 5 min · Words: 700

## Hook
A bus takes three seconds to cross a junction. At twenty-five frames per second, a detector sees it in about seventy-five frames. If you count detections, you count one bus seventy-five times. So how do you count it once?

## Explain
Welcome to the final week, where you build your capstone app. We start with counting. Detection works on single frames. It says there is a bus here, but it does not know that it saw the same bus one frame earlier.

Tracking links detections across frames, and gives each object a track ID that stays the same while it is visible. Most trackers use two clues. Motion, to predict where each object should be next. And overlap, often with IoU, to match new boxes to those predictions. Some also compare how objects look.

The Ultralytics package includes trackers. You call track instead of predict, and each box then has an ID. With IDs, counting is simple. Draw a counting line across the road. When a box centre moves from one side of the line to the other, count that ID once, and never again.

Tracking fails in predictable ways. In an ID switch, two objects pass close and swap IDs. In a lost track, an object is hidden, maybe behind a bus, and gets a new ID when it reappears. Near the line, it may be counted twice. And if the detector misses a small or dark object, the tracker cannot follow it.

So where should the line go? Place it where objects are large, clearly separated and rarely hidden. Then compare your automatic count with a manual count on a sample clip.

Tracking is like a teacher counting children back from a school trip. The teacher does not count every head every second. Each child has a name, and the teacher ticks each name once at the gate. If two children swap coats, the wrong name may be ticked.

## Demonstrate
Camila Restrepo works for a transport planning office in Bogotá, Colombia. She wants to count cars and buses entering a junction from one direction. She uses a public traffic clip filmed from a height, where faces cannot be seen.

In Colab, she loads the model and plays the first seconds of the clip. Her cell tracks only cars, buses and trucks. For each tracked vehicle, it remembers the box centre from the last frame, and counts the ID once when the centre moves down across the line.

She runs it. You'll see something like forty-one cars, six buses and three trucks. Then she saves the annotated video and opens it. Every vehicle has an ID above its box. The IDs make it easy to see where tracking works, and where it breaks.

She draws the counting line on one frame, so everyone can see where it is. Then she compares the result with her own count by hand. In her case, the hand count found forty-four cars, six buses and three trucks. Three cars are missing.

She checks the three missed cars. Two were hidden behind a bus while crossing the line. One was a dark car in shadow. So she moves the line eighty pixels lower, where vehicles are more separated, and runs the test again.

A common mistake is to count unique IDs across the whole video. That counts parked cars and vehicles at the edge, and every lost track adds a new ID. Count only line crossings in the right direction, and check against a manual count.

## Recap
Let's recap. First, detection works frame by frame, while tracking gives each object a stable ID across frames. Second, to count, record when each tracked object crosses a line, and count each ID only once. Third, ID switches, lost tracks and missed detections cause counting errors, so always compare with a manual count.

## CTA
Now it is your turn. In the exercise below this video, you will add tracking and a counting line to your YOLO pipeline, count vehicles in a short public clip, and compare with your own count. This is a core part of your capstone app. It takes about forty minutes. In the next lesson, Responsible Vision: Privacy, Bias and Licences. See you there.

## Thumbnail
Headline: Count Each Bus Once
Image: Navy background, a high-angle junction shot with vehicles in teal boxes carrying ID numbers and a bright counting line across the road, headline in teal Inter Bold.

## Production Notes
- [VERSION] ultralytics tracking interface (model.track, persist, classes, boxes.id), the included trackers (BoT-SORT, ByteTrack), the model name yolo11n.pt and the COCO class IDs used (2 car, 5 bus, 7 truck) must be checked at recording time. The counting logic was run on synthetic tracks; the YOLO calls were checked for syntax only.
- Run outputs: content.md gives {'car': 41, 'bus': 6, 'truck': 3} only as example output. The voiceover says 'you'll see something like' before these counts. Camila's manual count (44 cars, 6 buses, 3 trucks) and the cause of the three missed cars are described as her results; if the recorded run differs, show the real counts and keep the 'something like' wording, and re-record the comparison scene.
- Footage: junction.mp4 must be a public traffic clip, filmed from a height, showing vehicles only, with no visible faces and no readable number plates. Check that its licence allows reuse.
- Camila Restrepo and the Bogotá transport office are fictional; no real agency names or logos.
- Screen recording: clean browser profile, no account names or other tabs visible.
