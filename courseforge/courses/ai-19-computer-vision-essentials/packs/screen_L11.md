# Screen Demo Pack: AI-19 L11 Training YOLO on a Custom Dataset

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L11_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. In Label Studio, create a project with the labels juice_carton and rice_bag
2. Import the images
3. Draw boxes on one image, including a half-hidden carton

**Narration over this clip (for pacing)**

> In Label Studio, she creates a project with two labels, juice carton and rice bag. She imports her images and draws boxes on one of them, including a carton that is half hidden behind another.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L11_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Export in YOLO format and download the zip file
2. Open two exported .txt label files and compare them with their images
3. In Colab, unzip into /content/shelf with images/ and labels/ split into train and val
4. Create shelf.yaml

**Narration over this clip (for pacing)**

> She exports in YOLO format and downloads the zip file. In Colab, she unzips it into folders for training and validation, and writes the small settings file with her two class names. She also checks a few exported label files against their images, because export options change.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L11_screen_3.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Run the training cell: YOLO('yolo11n.pt'), model.train(data='shelf.yaml', epochs=50, imgsz=640)
2. Run model.val() and show the printed mAP50 and mAP50-95

**Narration over this clip (for pacing)**

> Then she runs the training cell. It starts from the pre-trained nano model and trains for fifty epochs. When it finishes, she validates. You'll see something like zero point eight one for mAP fifty, and zero point five two for mAP fifty to ninety-five. With only twelve validation images, these are a rough guide.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L11_screen_4.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Open results.png from the results folder
2. Open one validation image with boxes
3. Point to the missed bottom-shelf rice bags, the merged carton box and the carton behind the price label

**Narration over this clip (for pacing)**

> She opens the training curves and a validation image. Three failures stand out. Rice bags on the bottom shelf, seen from above, are missed. Two cartons side by side get one big box. And a carton behind a price label is not found. So she will add twenty bottom-shelf photos, and check her labels.

## Production notes for this lesson

- [VERSION] Free annotation tools (Label Studio, CVAT) and their project setup and export formats change; neither tool is in the brief's tool list. The demo uses Label Studio, as in content.md.
- [VERSION] ultralytics training interface (train, val, metrics.box.map50, metrics.box.map), the model name yolo11n.pt and the results folder contents (results.png, confusion matrix, weights/best.pt). Code was checked for syntax only.
- [VERSION] Google Colab free GPUs and session limits are not guaranteed.
- [VERIFY] Ultralytics licence (content.md: AGPL-3.0 with a separate commercial licence [VERIFY]). The voiceover makes no legal claim and does not name the licence; it only says to check the Ultralytics YOLO licence before any commercial use of a trained model. General guidance, not legal advice.
- [REGION] Rules on photographing customers or staff in shops, and on consent, differ by country. The shelf photos must show no customers or staff.
- Run outputs: content.md gives mAP50 0.81 and mAP50-95 0.52 only as example output from 12 validation images. The voiceover says 'you'll see something like' and calls them a rough guide. The three failure cases are described as what Mei Ling found; re-record that scene if the recorded run shows different failures.
- Products on the shelf must be plain or unbranded; no real brand names or logos. Mei Ling Chen and her Kuala Lumpur shops are fictional.
- Screen recording: clean browser profile, no account names or other tabs visible.
