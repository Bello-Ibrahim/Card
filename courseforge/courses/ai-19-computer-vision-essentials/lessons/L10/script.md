# L10 Running YOLO on Images and Video | Presenter Script

Course: AI-19 · Video: 5 min · Words: 694

## Hook
With one install command and a few lines of Python, you can find cars, buses and bottles in any photo or video. The code is short. The real decisions are the confidence threshold, and the licence. Let us make both decisions well.

## Explain
In the last lesson, you learned how to score boxes with IoU. Today, we produce those boxes with a real detector, on photos and on video.

YOLO stands for you only look once. It is a family of fast object detectors that predict all boxes, classes and scores in one pass over the image, which makes them popular for video. We use the open-source Ultralytics Python package, which runs several YOLO versions with the same simple interface.

The pre-trained models already know many common objects, such as cars, buses and bottles. They come in sizes, and the nano size is the smallest and fastest. Model names change with each new release, so check the current name before you start.

The key setting is the confidence threshold. Detections with a lower score are dropped. A low threshold keeps more real objects, but adds false alarms. A high threshold gives fewer false alarms, but misses small, distant or hidden objects. In other words, lowering it usually raises recall and lowers precision.

It works like the sensitivity setting on a metal detector at the beach. Very sensitive, and it beeps for every coin and every bottle cap. Less sensitive, and it ignores the bottle caps, but also misses small coins buried deep.

And one more decision before you build anything real. Free to download does not mean free for any commercial use. You must check the Ultralytics YOLO licence before commercial use, and ask a legal adviser if you are unsure.

## Demonstrate
Lars Eriksson plans lorry traffic at a container port in Gothenburg, Sweden. He tests whether a pre-trained model detects trucks and cars in photos from a public road camera, with no people in close view.

In a new Colab notebook, he installs the package and waits for it to finish. Then he uploads the road photo and runs the first cell. It loads the nano model, detects objects at a threshold of zero point two five, prints each one, and saves a copy with the boxes drawn.

He opens the saved image. You'll see something like a truck with a score of zero point eight eight, inside a clear box. Each printed line shows the class name, the score, and the four corner values of the box in pixels, the same corner format as in the last lesson.

Now the thresholds. You'll see something like eleven detections at zero point one, six at zero point two five, and four at zero point five. At the lowest value, he finds two false alarms. A container stack is called a truck, and a road sign is called a stop sign. At the highest, one distant car is missed.

He chooses zero point two five for now, and notes that he must test it on more images. For video, he runs predict on the clip in streaming mode, which returns one result per frame and keeps memory low. With saving switched on, an annotated video appears in the output folder, and he plays it.

A common mistake is to pick a threshold on one image and use it everywhere. A value that works on a clear daytime photo may miss most objects at night or in rain. Test on varied images.

## Recap
Let's recap. First, the Ultralytics package runs pre-trained YOLO models on images and video in a few lines, and returns boxes, classes and scores. Second, the confidence threshold trades false alarms against missed objects, so choose it by testing on varied images. Third, check the licence before any commercial use, because terms can change.

## CTA
Now it is your turn. In the exercise below this video, you will run a pre-trained YOLO model on five images and one short video, try three thresholds, and record what changes. Choose scenes with objects and vehicles. It takes about thirty-five minutes. In the next lesson, Training YOLO on a Custom Dataset. See you there.

## Thumbnail
Headline: YOLO in Five Lines
Image: Navy background, a road photo near a container port with teal boxes around trucks and cars, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Ultralytics licence. content.md states AGPL-3.0 with a separate paid enterprise licence for closed commercial use [VERIFY]. The voiceover does not name the licence or make any legal claim; it says only that the Ultralytics YOLO licence must be checked before commercial use, because 'free to download' does not mean 'free for any commercial use'. General guidance, not legal advice.
- [VERIFY] That the default pre-trained detection models are trained on COCO with 80 classes. The voiceover does not state the dataset or the number of classes; it says the models already know many common objects, such as cars, buses and bottles.
- [VERSION] ultralytics package interface (YOLO(), predict, stream, save, Results.save(filename=...), boxes.xyxy), the model name yolo11n.pt and the runs/detect/ output folder change between releases. Code was checked for syntax only.
- Run outputs: content.md gives the detections only as example output (truck 0.88; 11, 6 and 4 detections at conf 0.1, 0.25 and 0.5). The voiceover says 'you'll see something like' before these numbers. Show the real counts on screen; the false alarms named (container stack as truck, road sign as stop sign) and the missed distant car are what happened in Lars's test, so re-record that scene if the recorded run differs.
- Footage: port_road.jpg and port_road.mp4 show vehicles and road only, with no people in close view and no readable number plates.
- Lars Eriksson and the Gothenburg port are fictional; no real company names or logos on containers in footage.
- Screen recording: clean browser profile, no account names or other tabs visible.
