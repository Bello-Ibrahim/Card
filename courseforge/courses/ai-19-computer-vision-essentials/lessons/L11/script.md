# L11 Training YOLO on a Custom Dataset | Presenter Script

Course: AI-19 · Video: 5 min · Words: 696

## Hook
The pre-trained model knows bottle, but not your brand of mango juice. To detect your own objects, you draw boxes on your own images and fine-tune a detector. About fifty labelled images can be enough to start.

## Explain
In the last lesson, YOLO found common objects straight away. Today, we teach it new ones. Training a custom detector has four stages. Collect, label, export, and fine-tune.

First, collect images in the real conditions of your use case, with variety. Full and half-empty shelves, different angles, some blur. Keep customers and staff out of the photos, or ask for their consent. Second, label them. In a free annotation tool, draw a tight box around every visible object, even partly hidden ones.

This point matters a lot. An object that you do not label teaches the model that it is background. So label every one.

Third, export in YOLO format. Each image gets a text file, with one line per object. The line holds the class number, then the box centre, width and height, all scaled from zero to one. A small settings file tells YOLO where the images are and what the classes are called.

Put about eighty percent of the images in training and twenty percent in validation, and never the same photo in both. Fourth, fine-tune from a pre-trained model, as in lesson seven. Then read mAP fifty, mAP fifty to ninety-five, and the results for each class. Free Colab GPUs are not guaranteed, so save your trained weights to Google Drive when training ends.

Labelling is like preparing the answer key for an exam. If the key has missing answers, or careless ones, even a clever student learns the wrong things. So careful labels come first.

## Demonstrate
Mei Ling Chen runs convenience shops in Kuala Lumpur, Malaysia. She wants to detect two products, juice cartons and rice bags. She takes sixty shelf photos, with no customers in view.

In Label Studio, she creates a project with two labels, juice carton and rice bag. She imports her images and draws boxes on one of them, including a carton that is half hidden behind another.

She exports in YOLO format and downloads the zip file. In Colab, she unzips it into folders for training and validation, and writes the small settings file with her two class names. She also checks a few exported label files against their images, because export options change.

Then she runs the training cell. It starts from the pre-trained nano model and trains for fifty epochs. When it finishes, she validates. You'll see something like zero point eight one for mAP fifty, and zero point five two for mAP fifty to ninety-five. With only twelve validation images, these are a rough guide.

She opens the training curves and a validation image. Three failures stand out. Rice bags on the bottom shelf, seen from above, are missed. Two cartons side by side get one big box. And a carton behind a price label is not found. So she will add twenty bottom-shelf photos, and check her labels.

A common mistake is to trust a high score from validation photos taken seconds after the training photos. Near-identical photos make the model look much better than it is. Split by shooting session or by shelf. And before any commercial use of your trained model, check the Ultralytics YOLO licence.

## Recap
Let's recap. First, a custom detector needs real-condition images, tight boxes around every object, a YOLO-format export and a settings file with the class names. Second, fine-tuning starts from a pre-trained model, so a small dataset can give useful first results. Third, read mAP with per-class results and failure images, and keep training and validation photos truly separate.

## CTA
Now it is your turn. In the exercise below this video, you will label about fifty images of your own objects, fine-tune a small YOLO model, and report its mAP and three failures. Save your best weights, because you will use them in the capstone. It takes about an hour. In the next lesson, Reading Text in Images with OCR. See you there.

## Thumbnail
Headline: Teach YOLO Your Products
Image: Navy background, a shop shelf with juice cartons and rice bags in tight teal boxes, headline in teal Inter Bold.

## Production Notes
- [VERSION] Free annotation tools (Label Studio, CVAT) and their project setup and export formats change; neither tool is in the brief's tool list. The demo uses Label Studio, as in content.md.
- [VERSION] ultralytics training interface (train, val, metrics.box.map50, metrics.box.map), the model name yolo11n.pt and the results folder contents (results.png, confusion matrix, weights/best.pt). Code was checked for syntax only.
- [VERSION] Google Colab free GPUs and session limits are not guaranteed.
- [VERIFY] Ultralytics licence (content.md: AGPL-3.0 with a separate commercial licence [VERIFY]). The voiceover makes no legal claim and does not name the licence; it only says to check the Ultralytics YOLO licence before any commercial use of a trained model. General guidance, not legal advice.
- [REGION] Rules on photographing customers or staff in shops, and on consent, differ by country. The shelf photos must show no customers or staff.
- Run outputs: content.md gives mAP50 0.81 and mAP50-95 0.52 only as example output from 12 validation images. The voiceover says 'you'll see something like' and calls them a rough guide. The three failure cases are described as what Mei Ling found; re-record that scene if the recorded run shows different failures.
- Products on the shelf must be plain or unbranded; no real brand names or logos. Mei Ling Chen and her Kuala Lumpur shops are fictional.
- Screen recording: clean browser profile, no account names or other tabs visible.
