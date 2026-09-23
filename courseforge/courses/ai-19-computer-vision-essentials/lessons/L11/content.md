# L11 Training YOLO on a Custom Dataset

Course: AI-19 · Module: M3 · Objectives: O4, O5 · Video: 5 min (screen demo)

## Hook
The pre-trained model knows "bottle", but it does not know your brand of mango juice or the difference between two sizes of rice bag. To detect your own objects, you draw boxes on your own images and fine-tune a detector. About 50 labelled images can be enough to start.

## Explanation
Training a custom detector has four stages.

**1. Collect images.** Take photos in the real conditions of your use case: the same shelves, the same lighting, the same camera height. Include variety: full and half-empty shelves, different angles, some blur. Avoid customers and staff in the photos, or ask for their consent. [REGION]

**2. Label (annotate) them.** Use a free annotation tool, such as Label Studio or CVAT, to draw a tight box around every visible object of each class. [VERSION] Label *every* object, including partly hidden ones. An object you leave unlabelled teaches the model that it is background.

**3. Export in YOLO format.** Each image gets a `.txt` file with one line per object:

```text
0 0.412 0.530 0.110 0.240
```

The numbers are: class ID, box centre x, centre y, width and height, all scaled from 0 to 1 by the image size. Export options and folder layouts change between tool versions, so check the export on a few images. [VERSION] A small YAML file tells YOLO where the images are and what the classes are called:

```yaml
path: /content/shelf
train: images/train
val: images/val
names:
  0: juice_carton
  1: rice_bag
```

Split the images so that about 80% are for training and 20% for validation, and never put the same photo in both.

**4. Fine-tune and read the results.** Training starts from a pre-trained model, as in L07, so it already knows general features. The results folder contains training curves, a confusion matrix and validation images with predicted boxes. [VERSION] Focus on **mAP50** and **mAP50-95** from L09, and on precision and recall for each class. Then look at the validation images where boxes are missing or wrong.

Colab's free GPUs are not guaranteed, and sessions end after a limit. [VERSION] Save your trained weights to Google Drive when training ends. The same licence rules as in L10 apply to models you train with the `ultralytics` package. [VERIFY]

**Analogy:** Labelling is like preparing an answer key for an exam. If the key is missing answers, or has boxes drawn carelessly, the student learns the wrong lessons, no matter how intelligent the student is.

## Worked Example
Mei Ling Chen runs a small chain of convenience shops in Kuala Lumpur, Malaysia. She wants to know when two products run low: juice cartons and rice bags. She photographs 60 shelf images, with no customers in view, and labels them in Label Studio.

**On screen (presenter steps):**
1. In the annotation tool, create a project with the labels `juice_carton` and `rice_bag`. [VERSION]
2. Import the images and draw boxes on one image, including a carton that is half hidden.
3. Export in YOLO format and download the zip file. [VERSION]
4. In Colab, upload and unzip it into `/content/shelf` with `images/` and `labels/` folders split into `train` and `val`, and create `shelf.yaml`.
5. Run the training cell below and show the progress lines.
6. Open `results.png`, the confusion matrix and one validation image from the results folder.

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")                 # pre-trained starting point
model.train(data="shelf.yaml", epochs=50, imgsz=640)

metrics = model.val()
print("mAP50:", round(metrics.box.map50, 3))
print("mAP50-95:", round(metrics.box.map, 3))
```

Example output: `mAP50: 0.81` and `mAP50-95: 0.52`. These values come from Mei Ling's small validation set of 12 images, so they are only a rough guide.

She looks at the failures. Three stand out: rice bags on the bottom shelf, photographed from above, are missed; two juice cartons placed side by side get one large box; and a carton behind a price label is not found. Her next step is to add 20 bottom-shelf photos and check that neighbouring cartons have separate boxes in her labels.

## Common Mistake
Many learners trust a high mAP from a very small validation set, or from validation images taken seconds after the training images. Near-identical photos in both splits make the model look much better than it is. Split by shooting session or by shelf, not by random photo, and test later on completely new photos. Also check your labels before training: missing or loose boxes are the most common cause of poor results.

## Key Takeaways
1. A custom detector needs images from real conditions, tight boxes around every object, a YOLO-format export and a YAML file with the class names.
2. Fine-tuning starts from a pre-trained model, so a small labelled dataset can give useful first results.
3. Read mAP together with per-class results and failure images, and keep training and validation photos truly separate.

## Hands-on Exercise
**Task:** Label about 50 images of one or two custom objects (for example products on a shop shelf), fine-tune a small YOLO model in Colab, and report its mAP and 3 failure cases.
**Tools:** A free annotation tool, such as Label Studio or CVAT [VERSION]; Google Colab with a GPU if available [VERSION]; the `ultralytics` package [VERSION]; your own photos of objects, with no people or private information in view.
**Steps:**
1. Photograph about 50 images of one or two object types in varied positions and lighting.
2. Create an annotation project, label every visible object and export in YOLO format.
3. Open 3 label files and check that the lines match the objects in the images.
4. Split the images by photo session into train (about 80%) and val (about 20%), and write the YAML file.
5. Fine-tune `yolo11n.pt` for 50 epochs and record mAP50 and mAP50-95.
6. Open the validation images and describe 3 failure cases with a likely cause for each.
7. Save `best.pt` from the weights folder to Google Drive for L13 and L15.
**What good looks like:** A labelled dataset in YOLO format, a completed training run, the two mAP values, and 3 failure cases, each linked to a cause such as angle, overlap, lighting or labelling errors.
**Time:** about 60 minutes

## Review Flags
- [VERSION] Curriculum flag: free annotation tools (Label Studio, CVAT) and their project setup and export formats change; neither tool is in the brief's tool list.
- [VERSION] `ultralytics` training interface (`train`, `val`, `metrics.box.map50`, `metrics.box.map`), the model name `yolo11n.pt`, and the results folder contents (`results.png`, confusion matrix, `weights/best.pt`). Code was checked for syntax only; mAP values are example output, not benchmarks.
- [VERSION] Google Colab free GPU availability and session limits are not guaranteed.
- [VERIFY] Curriculum flag: Ultralytics licence (AGPL-3.0 with a separate commercial licence) must be confirmed before scripting; learners must check terms before commercial use of trained models.
- [REGION] Rules on photographing customers or staff in shops, and on consent, differ by country.
