# HeyGen Batch Pack: AI-19 M3 (Object Detection and OCR)

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

## L09 Object Detection: Boxes, Classes and IoU

- **Filename:** `ai-19-computer-vision-essentials_M3_L09_presenter.mp4`
- **Expected length:** about 5.2 minutes (720 words). The quality gate accepts ±10%.

```text
A detector draws a box around a car, but cuts off the back of it. Is that correct, or a mistake? Without a clear rule, two people will score the same model differently. That rule is called IoU.

Welcome to week three. So far, our models said what is in an image. Now we also ask where. An object detector returns a list of detections, and each one has three parts.

First, a bounding box, usually the top left and bottom right corners in pixels. Some tools use the centre, width and height instead, so always check the format. Second, a class, such as car or bus. Third, a confidence score from zero to one.

Detectors often draw several overlapping boxes for one object. Non-maximum suppression keeps the box with the highest score and removes boxes that overlap it strongly. Libraries usually do this for you.

Intersection over union, or IoU, measures how well a predicted box matches the true box that a person drew. It is the area of overlap divided by the area of the union, which is everything either box covers. IoU is one for a perfect match, and zero when the boxes do not touch.

To score a detector, you pick an IoU threshold, often zero point five. A prediction with the right class and enough overlap is a true positive. Otherwise it is a false positive. And every true box with no match is a false negative. From these counts, you get precision and recall, like last week.

Average precision summarises precision and recall for one class, and mAP averages it over all classes. There are two common versions. mAP fifty uses a threshold of zero point five. mAP fifty to ninety-five averages stricter thresholds, so it is always lower or equal for the same model.

Picture laying a transparent sheet with your box over the true box on a light table. Measure where they overlap, and divide by the total area they cover. A box that is too big and a box that is too small both lose points.

Nadia Rahman evaluates a parking detector for a shopping centre in Dhaka, Bangladesh. For one car, the true box runs from one hundred, fifty to three hundred, one hundred and fifty. The predicted box runs from one hundred and fifty, seventy to three hundred and thirty, one hundred and seventy.

The true box is two hundred by one hundred, so its area is twenty thousand. The predicted box is one hundred and eighty by one hundred, so eighteen thousand. The overlap is one hundred and fifty wide and eighty high, which is twelve thousand.

The union is twenty thousand plus eighteen thousand, minus the overlap, so twenty-six thousand. Twelve thousand divided by twenty-six thousand gives an IoU of about zero point four six.

At a threshold of zero point five, this prediction is a false positive, and the car counts as a false negative, even though the box is clearly on the car. Nadia notices that the boxes often shift towards the car's shadow, something to fix with more training images.

She checks her answer with a short function. It finds the corners of the overlap, multiplies width by height, and divides by the union. It prints zero point four six two. Note the parts that stop the width or height going below zero. Without them, two boxes that do not touch could show a false overlap.

A common mistake is to compare mAP numbers from different sources. Only compare the same version, on the same test set. And never mix box formats, because the wrong format gives wrong IoU values without any error.

Let's recap. First, a detector returns a box, a class and a confidence score for each object, and non-maximum suppression removes duplicate boxes. Second, IoU is overlap divided by union, and a threshold such as zero point five decides whether a prediction counts. Third, compare mAP values only with the same version and the same test set.

Now it is your turn. In the exercise below this video, you will calculate IoU by hand for three pairs of boxes, then check your answers with a short Python function. It takes about twenty minutes. In the next lesson, we run a real detector. Running YOLO on Images and Video. See you there.
```

## L10 Running YOLO on Images and Video

- **Filename:** `ai-19-computer-vision-essentials_M3_L10_presenter.mp4`
- **Expected length:** about 5.0 minutes (688 words). The quality gate accepts ±10%.

```text
With one install command and a few lines of Python, you can find cars, buses and bottles in any photo or video. The code is short. The real decisions are the confidence threshold, and the licence. Let us make both decisions well.

In the last lesson, you learned how to score boxes with IoU. Today, we produce those boxes with a real detector, on photos and on video.

YOLO stands for you only look once. It is a family of fast object detectors that predict all boxes, classes and scores in one pass over the image, which makes them popular for video. We use the open-source Ultralytics Python package, which runs several YOLO versions with the same simple interface.

The pre-trained models already know many common objects, such as cars, buses and bottles. They come in sizes, and the nano size is the smallest and fastest. Model names change with each new release, so check the current name before you start.

The key setting is the confidence threshold. Detections with a lower score are dropped. A low threshold keeps more real objects, but adds false alarms. A high threshold gives fewer false alarms, but misses small, distant or hidden objects. In other words, lowering it usually raises recall and lowers precision.

It works like the sensitivity setting on a metal detector at the beach. Very sensitive, and it beeps for every coin and every bottle cap. Less sensitive, and it ignores the bottle caps, but also misses small coins buried deep.

And one more decision before you build anything real. Free to download does not mean free for any commercial use. You must check the Ultralytics YOLO licence before commercial use, and ask a legal adviser if you are unsure.

Lars Eriksson plans lorry traffic at a container port in Gothenburg, Sweden. He tests whether a pre-trained model detects trucks and cars in photos from a public road camera, with no people in close view.

In a new Colab notebook, he installs the package and waits for it to finish. Then he uploads the road photo and runs the first cell. It loads the nano model, detects objects at a threshold of zero point two five, prints each one, and saves a copy with the boxes drawn.

He opens the saved image. You'll see something like a truck with a score of zero point eight eight, inside a clear box. Each printed line shows the class name, the score, and the four corner values of the box in pixels, the same corner format as in the last lesson.

Now the thresholds. You'll see something like eleven detections at zero point one, six at zero point two five, and four at zero point five. At the lowest value, he finds two false alarms. A container stack is called a truck, and a road sign is called a stop sign. At the highest, one distant car is missed.

He chooses zero point two five for now, and notes that he must test it on more images. For video, he runs predict on the clip in streaming mode, which returns one result per frame and keeps memory low. With saving switched on, an annotated video appears in the output folder, and he plays it.

A common mistake is to pick a threshold on one image and use it everywhere. A value that works on a clear daytime photo may miss most objects at night or in rain. Test on varied images.

Let's recap. First, the Ultralytics package runs pre-trained YOLO models on images and video in a few lines, and returns boxes, classes and scores. Second, the confidence threshold trades false alarms against missed objects, so choose it by testing on varied images. Third, check the licence before any commercial use, because terms can change.

Now it is your turn. In the exercise below this video, you will run a pre-trained YOLO model on five images and one short video, try three thresholds, and record what changes. Choose scenes with objects and vehicles. It takes about thirty-five minutes. In the next lesson, Training YOLO on a Custom Dataset. See you there.
```

## L11 Training YOLO on a Custom Dataset

- **Filename:** `ai-19-computer-vision-essentials_M3_L11_presenter.mp4`
- **Expected length:** about 5.0 minutes (679 words). The quality gate accepts ±10%.

```text
The pre-trained model knows bottle, but not your brand of mango juice. To detect your own objects, you draw boxes on your own images and fine-tune a detector. About fifty labelled images can be enough to start.

In the last lesson, YOLO found common objects straight away. Today, we teach it new ones. Training a custom detector has four stages. Collect, label, export, and fine-tune.

First, collect images in the real conditions of your use case, with variety. Full and half-empty shelves, different angles, some blur. Keep customers and staff out of the photos, or ask for their consent. Second, label them. In a free annotation tool, draw a tight box around every visible object, even partly hidden ones.

This point matters a lot. An object that you do not label teaches the model that it is background. So label every one.

Third, export in YOLO format. Each image gets a text file, with one line per object. The line holds the class number, then the box centre, width and height, all scaled from zero to one. A small settings file tells YOLO where the images are and what the classes are called.

Put about eighty percent of the images in training and twenty percent in validation, and never the same photo in both. Fourth, fine-tune from a pre-trained model, as in lesson seven. Then read mAP fifty, mAP fifty to ninety-five, and the results for each class. Free Colab GPUs are not guaranteed, so save your trained weights to Google Drive when training ends.

Labelling is like preparing the answer key for an exam. If the key has missing answers, or careless ones, even a clever student learns the wrong things. So careful labels come first.

Mei Ling Chen runs convenience shops in Kuala Lumpur, Malaysia. She wants to detect two products, juice cartons and rice bags. She takes sixty shelf photos, with no customers in view.

In Label Studio, she creates a project with two labels, juice carton and rice bag. She imports her images and draws boxes on one of them, including a carton that is half hidden behind another.

She exports in YOLO format and downloads the zip file. In Colab, she unzips it into folders for training and validation, and writes the small settings file with her two class names. She also checks a few exported label files against their images, because export options change.

Then she runs the training cell. It starts from the pre-trained nano model and trains for fifty epochs. When it finishes, she validates. You'll see something like zero point eight one for mAP fifty, and zero point five two for mAP fifty to ninety-five. With only twelve validation images, these are a rough guide.

She opens the training curves and a validation image. Three failures stand out. Rice bags on the bottom shelf, seen from above, are missed. Two cartons side by side get one big box. And a carton behind a price label is not found. So she will add twenty bottom-shelf photos, and check her labels.

A common mistake is to trust a high score from validation photos taken seconds after the training photos. Near-identical photos make the model look much better than it is. Split by shooting session or by shelf. And before any commercial use of your trained model, check the Ultralytics YOLO licence.

Let's recap. First, a custom detector needs real-condition images, tight boxes around every object, a YOLO-format export and a settings file with the class names. Second, fine-tuning starts from a pre-trained model, so a small dataset can give useful first results. Third, read mAP with per-class results and failure images, and keep training and validation photos truly separate.

Now it is your turn. In the exercise below this video, you will label about fifty images of your own objects, fine-tune a small YOLO model, and report its mAP and three failures. Save your best weights, because you will use them in the capstone. It takes about an hour. In the next lesson, Reading Text in Images with OCR. See you there.
```

## L12 Reading Text in Images with OCR

- **Filename:** `ai-19-computer-vision-essentials_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (690 words). The quality gate accepts ±10%.

```text
A program cannot search or add up a photo of a receipt. OCR turns the picture of text into real text. On a clean scan it can work well. On a creased receipt in a dim café, it can fail badly. Preprocessing makes much of the difference.

In the last two lessons, we detected objects. Today, the objects are letters. Optical character recognition, or OCR, usually has two steps. Text detection finds the areas that contain text, and text recognition reads the characters in each area.

We use Tesseract, a free, open-source OCR engine, through a small Python wrapper. You install the engine and one language pack for each language. The codes are f r a for French, p o r for Portuguese and a r a for Arabic, and you can combine them. Other open-source engines, such as EasyOCR and PaddleOCR, may handle photos better, so compare them if Tesseract fails.

Quality depends strongly on the image, and the steps from lesson three help. Enlarge small text, for example to twice the size. Threshold it to black on white, which also removes shadows. Crop away the table and background. And straighten tilted lines, because tilted text is often misread.

Scripts matter too. Arabic is written right to left, and letters change shape by position, so test each script on your own images before you rely on it. To measure OCR, type the true text by hand. The character error rate counts the character edits needed to fix the output, divided by the length of the true text. Zero is perfect.

OCR is like a person reading a note through a dirty window. They may know the language well, but they still misread letters. Cleaning the window often helps more than finding a better reader.

One more thing. Receipts can contain personal data, such as names or card numbers. Use your own receipts or public signs, and never upload other people's documents to online OCR services.

Amira Ben Salem manages expenses for a design studio in Tunis, Tunisia. Her receipts are in French and Arabic. She tests OCR on one of her own receipts, with the card number covered, before and after preprocessing.

In Colab, she installs the Tesseract engine with its French, Arabic and Portuguese packs, and then the Python wrapper. She uploads the receipt photo.

The cell reads the raw photo in French and Arabic. Then it cleans a copy. It turns it grey, doubles its size, and applies an adaptive threshold. The threshold makes the text black on white and removes the shadow of the fold. And it reads the clean version too. She shows both images and both outputs side by side.

On the raw photo, you'll see something like this for the total line. The letter O is read as a zero, and the comma is read as a full stop. That is two wrong characters out of fifteen. The error function gives zero point one three three.

In her test, the French lines are read correctly after preprocessing. She checks the Arabic lines separately, by hand, and plans to compare a second engine, because support for each script must be tested on real receipts.

A common mistake is to test OCR on clean screenshots, and expect the same on phone photos. Real inputs have shadows, folds, tilt and glare. And always set the language. Without the right pack, the engine reads Arabic or accented Portuguese as nonsense, and it does not warn you.

Let's recap. First, OCR finds and reads text in images, and Tesseract needs a language pack for each language. Second, preprocessing with OpenCV, like resizing, thresholding, cropping and straightening, often helps more than changing settings. Third, measure quality with the character error rate on real images, separately for each language and script.

Now it is your turn. In the exercise below this video, you will run OCR on five receipts or signs in at least two languages, before and after preprocessing, and compare the errors. It takes about forty minutes. Next week is capstone week, and we start by counting moving objects. Counting and Tracking Objects in Video. See you there.
```
