# HeyGen Batch Pack: AI-19 M4 (Building a Vision App: Capstone)

Course: Computer Vision Essentials. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L13 Counting and Tracking Objects in Video

- **Filename:** `ai-19-computer-vision-essentials_M4_L13_presenter.mp4`
- **Expected length:** about 5.0 minutes (695 words). The quality gate accepts ±10%.

```text
A bus takes three seconds to cross a junction. At twenty-five frames per second, a detector sees it in about seventy-five frames. If you count detections, you count one bus seventy-five times. So how do you count it once?

Welcome to the final week, where you build your capstone app. We start with counting. Detection works on single frames. It says there is a bus here, but it does not know that it saw the same bus one frame earlier.

Tracking links detections across frames, and gives each object a track ID that stays the same while it is visible. Most trackers use two clues. Motion, to predict where each object should be next. And overlap, often with IoU, to match new boxes to those predictions. Some also compare how objects look.

The Ultralytics package includes trackers. You call track instead of predict, and each box then has an ID. With IDs, counting is simple. Draw a counting line across the road. When a box centre moves from one side of the line to the other, count that ID once, and never again.

Tracking fails in predictable ways. In an ID switch, two objects pass close and swap IDs. In a lost track, an object is hidden, maybe behind a bus, and gets a new ID when it reappears. Near the line, it may be counted twice. And if the detector misses a small or dark object, the tracker cannot follow it.

So where should the line go? Place it where objects are large, clearly separated and rarely hidden. Then compare your automatic count with a manual count on a sample clip.

Tracking is like a teacher counting children back from a school trip. The teacher does not count every head every second. Each child has a name, and the teacher ticks each name once at the gate. If two children swap coats, the wrong name may be ticked.

Camila Restrepo works for a transport planning office in Bogotá, Colombia. She wants to count cars and buses entering a junction from one direction. She uses a public traffic clip filmed from a height, where faces cannot be seen.

In Colab, she loads the model and plays the first seconds of the clip. Her cell tracks only cars, buses and trucks. For each tracked vehicle, it remembers the box centre from the last frame, and counts the ID once when the centre moves down across the line.

She runs it. You'll see something like forty-one cars, six buses and three trucks. Then she saves the annotated video and opens it. Every vehicle has an ID above its box. The IDs make it easy to see where tracking works, and where it breaks.

She draws the counting line on one frame, so everyone can see where it is. Then she compares the result with her own count by hand. In her case, the hand count found forty-four cars, six buses and three trucks. Three cars are missing.

She checks the three missed cars. Two were hidden behind a bus while crossing the line. One was a dark car in shadow. So she moves the line eighty pixels lower, where vehicles are more separated, and runs the test again.

A common mistake is to count unique IDs across the whole video. That counts parked cars and vehicles at the edge, and every lost track adds a new ID. Count only line crossings in the right direction, and check against a manual count.

Let's recap. First, detection works frame by frame, while tracking gives each object a stable ID across frames. Second, to count, record when each tracked object crosses a line, and count each ID only once. Third, ID switches, lost tracks and missed detections cause counting errors, so always compare with a manual count.

Now it is your turn. In the exercise below this video, you will add tracking and a counting line to your YOLO pipeline, count vehicles in a short public clip, and compare with your own count. This is a core part of your capstone app. It takes about forty minutes. In the next lesson, Responsible Vision: Privacy, Bias and Licences. See you there.
```

## L14 Responsible Vision: Privacy, Bias and Licences

- **Filename:** `ai-19-computer-vision-essentials_M4_L14_presenter.mp4`
- **Expected length:** about 5.0 minutes (696 words). The quality gate accepts ±10%.

```text
Your vehicle counter works. Then someone asks. Who is visible in your videos, and did they agree? Does it work at night? Are you allowed to sell it? If you cannot answer, the project is not ready, however good the mAP is.

In the last lesson, you counted vehicles in video. Before you deploy a system like that, check four areas. Privacy, bias, licences, and fitness for use.

Privacy first. Cameras record people, even when you only want cars or shelves. Good practice has four parts. Collect less, and prefer counts over stored video. Blur people before you store or share frames. Limit who can access video, and when it is deleted. And inform people, with clear notices and consent where the law requires it.

Laws on cameras, consent and storage differ by country, and sometimes by city. This is general guidance, not legal advice, so check the rules where you deploy. And never upload real footage of people to online AI tools for testing.

Bias. A model works best on data like its training data. A detector trained mostly on daytime images from one country may miss vehicle types, shop layouts or lighting it rarely saw. So test in the real place, at different times and in different weather, and report each condition separately.

Licences. Check every model, dataset and library before commercial use. The Ultralytics YOLO licence must be checked before any commercial use, and Hugging Face models and datasets each have their own licence. Some allow research use only. Finally, fitness for use. Are the errors acceptable for this decision? Is the speed enough? And what happens when the system is wrong?

A fitness check is like a safety inspection before a new bus goes into service. The engine may be excellent, but the inspector also checks the brakes, the doors and the insurance. A bus that fails any check stays in the depot.

Oluwaseun Adeyemi builds a system to count delivery vans at a logistics depot in Lagos, Nigeria. The camera also records workers walking across the yard. So he adds a step that blurs every detected person before any frame is saved.

He adds a small blur function to his notebook from the last lesson. It takes a frame and a list of boxes, keeps each box inside the image, and applies a strong blur inside it. In the tracking loop, he selects the person boxes and blurs them before each frame is written.

He plays the output and pauses on a frame with workers in the yard. Each person is blurred from head to foot. He blurs the whole person box, not only the face, because face detectors miss small, turned or shadowed faces, and clothes can also identify people.

He also checks sample frames by eye, because one missed detection means one unblurred person. Then he writes his fitness check in a text cell, with five headings. Accuracy, speed, privacy, licence, and decision.

His example results. The van count is within five percent of a manual count on ten daytime clips, but night is untested. A one-minute clip takes about forty seconds, and hourly batches are enough. People are blurred, and raw video is deleted after twenty-four hours. The licence needs legal review before other depots use it. His decision? Fit for a daytime internal pilot only.

A common mistake is to treat privacy and licences as paperwork for later. By then, the video is already stored, and the model may be inside a product its licence does not allow. Check licences before you choose a model.

Let's recap. First, collect less, blur people, limit storage and follow local rules. Second, test for bias by measuring results separately for different conditions, places and times. Third, a fitness check covers accuracy, speed, privacy and licences, and ends with a clear decision.

Now it is your turn. In the exercise below this video, you will add person blurring to your video output, list the licences of everything you use, and write a half-page fitness check. It takes about thirty-five minutes, and it becomes part of your capstone. In the next lesson, Capstone Part 1: Build Your Detection App. See you there.
```

## L15 Capstone Part 1: Build Your Detection App

- **Filename:** `ai-19-computer-vision-essentials_M4_L15_presenter.mp4`
- **Expected length:** about 5.0 minutes (698 words). The quality gate accepts ±10%.

```text
A notebook that only you can run is an experiment. An app where a shop manager uploads a photo and sees fourteen cartons is a product. Today, you start building that app. And every choice you make today should serve that one number.

This is the first of two capstone lessons. Your capstone is an object detection and counting app for one real use case. Choose one that is narrow, and that counts objects, not people. For example, stock on shop shelves in Casablanca, or vehicles on a road in Manila.

Build it in four steps. First, define the target. Count juice cartons on the drinks shelf is a good target. Count everything in any shop is not. Second, choose the model. If a pre-trained class fits, use it with a tested threshold. If not, fine-tune on your own images, and check every licence.

Third, write one counting function that returns an annotated image and the total. For video, reuse the line counting from lesson thirteen. Fourth, add a simple interface with Gradio, which builds a web page from a Python function. It runs in Colab with a temporary link, or on a free Hugging Face Space.

Watch the colour order. Gradio gives your function red, green, blue. But the Ultralytics package treats arrays as blue, green, red, like OpenCV. So convert on the way in, and convert the annotated result back on the way out.

Over this lesson and the next, you deliver five things. The working app, a test table on at least twenty new images or clips, one measured improvement, a fitness check, and a three-minute demo. The rubric scores each of these, so keep them in mind as you build.

Think of the model as the engine, and the interface as the dashboard. The driver does not need to see the engine. They need a clear speed reading and a warning light.

Karim El Amrani manages three grocery shops in Casablanca. He fine-tuned a detector on eighty labelled shelf photos, using the steps from lesson eleven. Now he wraps it in an app.

In Colab, he installs Ultralytics and Gradio, and uploads his trained model file. His counting function flips the colour order, runs the model, counts the juice cartons, and flips the annotated picture back. The interface has an image input, a confidence slider, the annotated picture and the count.

He runs the cell and opens the temporary link. He uploads a shelf photo with fourteen cartons, and moves the slider. You'll see something like count thirteen. A carton behind a price label is missed, just as in training. He notes it for the next lesson.

To keep the app running, he creates a new Space on Hugging Face, with Gradio and free CPU hardware. He uploads three files. The app code, the model file, and a requirements file that lists Ultralytics and Gradio. Free Space hardware has no GPU and has limits, so he uses the smallest model and keeps any videos short.

When the build finishes, he tests the Space with a new photo. Before he makes it public, he checks two things. The app shows no people, and the detector's licence allows public use. Remember, the Ultralytics YOLO licence must be checked before commercial use.

A common mistake is to spend capstone time on colours and extra buttons. The rubric rewards a correct count, honest evaluation and a clear fitness judgement. So get a plain interface working first. And do not forget the colour conversion.

Let's recap. First, choose one narrow use case, with a clear target object and a number the user needs. Second, wrap one counting function in a Gradio interface, and convert between the two colour orders at the edges. Third, deploy on a free Hugging Face Space with a small model, and check licences before you go public.

Now it is your turn. In the exercise below this video, you complete capstone step one. Build an app that takes an image or a short video, detects and counts your target objects, and shows boxes and a total. It takes about an hour. In the next lesson, Capstone Part 2: Evaluate, Improve and Present. See you there.
```

## L16 Capstone Part 2: Evaluate, Improve and Present

- **Filename:** `ai-19-computer-vision-essentials_M4_L16_presenter.mp4`
- **Expected length:** about 4.9 minutes (686 words). The quality gate accepts ±10%.

```text
Your app counted correctly on the photos you tried. But you chose those photos, and you knew they would work. Today, you test it on images it has never seen, fix one thing, and decide honestly whether anyone should rely on it.

This is the final lesson, and the second part of your capstone. It has four steps. First, build a fair test set. Collect at least twenty new images or clips that were never used for training, validation or choosing a threshold.

Cover the conditions of real use. Different times of day, angles and distances, crowded and empty scenes. Write the condition next to each item, and count the true number of objects by hand.

Second, measure the errors. For a counting app, the main number is the count error, the difference between the app's count and the true count. Report the mean absolute error, which is the average size of the error, overall and for each condition. Where you have labelled boxes, add precision and recall, or mAP.

Third, make one improvement. Group the worst cases by cause, then choose one change for the biggest group. More training images, a better threshold chosen on separate images, or preprocessing with OpenCV. Change one thing at a time, rerun the same test set, and report the result, even if it did not help.

Fourth, judge fitness and present. Update your fitness check with the new numbers, and end with a clear decision. Then record a three-minute demo. The problem, the app working, results and failures, and your decision.

Evaluation is like a driving test on roads the learner has not practised. Driving well on your own street proves little. The examiner chooses the route, includes a busy junction and a hill start, and writes down every mistake.

Aigerim Seitkali, a developer in Almaty, Kazakhstan, built an app that counts parked vehicles from a fixed camera. She tests it on twenty-four new photos. Eight by day, eight in the evening and eight in rain, all taken from far away.

Her first results show large errors in rain and in the evening, where dark cars are missed. So she adds a contrast correction step with OpenCV, and runs the same test set again. She keeps everything in a spreadsheet, with the image, the condition, the true count, and the counts before and after.

In Colab, she uploads the file and runs a short cell. The mean error falls from zero point seven five to zero point four six vehicles per photo.

The breakdown tells the real story. Evening improves from zero point six two to zero point two five. Rain improves from one point five zero to zero point eight eight. But daytime gets slightly worse, from zero point one two to zero point two five, because the correction makes some reflections look like cars. She opens two rain images to see why.

She reports this honestly, in her updated fitness check. Her decision. Fit for hourly occupancy estimates, where an error of one vehicle is acceptable. Not fit for billing individual drivers. And rain still needs more training images. Finally, she shows the outline of her three-minute demo.

A common mistake is to tune the threshold while looking at the test results. Then the test score is too optimistic. Choose changes on separate images. And never hide failures in your demo. Showing where the app fails, and why, is part of the grade.

Let's recap. First, evaluate on at least twenty new images or clips that cover real conditions, and report errors for each condition. Second, make one targeted improvement, rerun the same test set, and report the result, even when it is mixed. Third, end with a clear fitness decision that says where the app can and cannot be used.

Congratulations on finishing Computer Vision Essentials. You have gone from pixels to a working, tested app. Now complete capstone step two in the exercise below. Test your app, make one improvement, update your fitness check, and record your demo. Remember to check the Ultralytics YOLO licence before any commercial use. Then submit your capstone. Well done.
```
