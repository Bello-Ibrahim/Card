# L11 Build Your Own Image Classifier

Course: AI-01 · Module: M3 · Objectives: O4, O2 · Video: 5 min (screen demo)

## Hook
You have learned how machines learn from examples. Today you will teach one yourself, in your web browser, with no code and no maths. You will build a model that recognises objects you chose, and see where it succeeds and where it fails.

## Explanation
Google Teachable Machine is a free, browser-based tool for training simple models. We use an **image project**: a model that looks at a picture and predicts its class. This is supervised classification, from L05.

Every step in the tool matches a term you already know:

- **Classes are your labels**, such as "banana" or "orange".
- **Example images are your data**, from your webcam or uploaded files.
- **Features are found by the model.** You do not tell it "look for yellow". During training it finds its own patterns, such as shapes, colours and textures (L07).
- **Training** adjusts the model's internal dials to match your images to your labels.
- **Testing and prediction** happen in the preview area. You show new images, and the model gives a confidence for each class.

The interface may change, so treat these steps as a general guide. [VERSION]

1. Open Teachable Machine, start a new project and choose a standard image project. [VERSION]
2. Rename the empty default classes, for example "banana" and "orange". Add a third class if you want. [VERSION]
3. Add images to each class with the **Webcam** option (record frames of the object) or the **Upload** option (choose image files). [VERSION]
4. Click **Train** and keep the browser tab open until it finishes. [VERSION]
5. In the **Preview** area, show new objects or upload new images, and read the confidence bars. [VERSION]

You do not need the advanced or export options for the capstone. [VERSION]

**Privacy note:** Use objects, such as types of fruit or pens vs. cups. Do not use photos of other people without their clear consent. Check the tool's privacy information about where images are stored. [VERIFY]

**Analogy:** Training a classifier is like teaching a young child to name fruit by showing them real examples. If you only show yellow bananas on a white table, a green banana on a wooden table may confuse them. Varied examples help the child, and the model, handle new cases.

## Worked Example
Chiamaka runs a small recycling project at a community centre in Enugu, Nigeria. She wants a simple demonstration that tells "plastic bottle" from "metal can".

Using her laptop webcam, she records about 30 images per class: different sizes and colours, different angles, some crushed and some whole. The background is always the same plain wall.

She trains the model and tests it with 10 new items. It gets 8 right. It fails on a clear bottle held in front of a window and on a very shiny can. Her training images all had dull indoor light, so the model may have learned "bright and shiny" as a sign of "can".

She adds images taken near the window, trains again and tests with new items. The results improve. This is the full cycle: data, labels, training, testing and better data.

## Common Mistake
Many learners test with the same objects, angles and light they used for training. The results look perfect but tell you almost nothing. As L08 explained, a fair test uses examples the model has never seen. Test with new objects, backgrounds or lighting, and record the failures honestly. They are the most useful part of your capstone.

## Key Takeaways
1. In Teachable Machine, classes are labels, your images are the data, the Train button runs training, and the preview is where the model makes predictions.
2. Varied examples (angles, backgrounds, lighting) help the model handle new cases. Narrow examples can teach it the wrong pattern.
3. Test with new images the model has never seen, and record every result, including the mistakes.

## Hands-on Exercise
**Task:** Capstone step 1: train a classifier with at least 2 classes and 20+ images per class, then test it on 10 new images and record the results.
**Tools:** Google Teachable Machine (free, in a browser); a webcam or phone camera; everyday objects; a notes app or paper.
**Steps:**
1. Choose 2 or 3 classes of objects that are easy to find, such as apples vs. oranges, or pens vs. cups. Do not use photos of other people without their consent.
2. Create an image project and rename the classes. [VERSION]
3. Add at least 20 images to each class. Vary the angle, distance, background and lighting.
4. Train the model and keep the tab open until training finishes.
5. Test 10 new images or objects not used in training, including at least 2 difficult cases, such as a busy background.
6. Record in a table: the item, the true class, the predicted class, the confidence, and "correct" or "wrong".
7. Screenshot your classes and one test result. Keep your table for L12.
**What good looks like:** A trained model with at least 2 named classes and 20+ varied images each, a table of 10 test results with honest notes on mistakes, and screenshots as evidence.
**Time:** about 35 minutes

## Review Flags
- [VERSION] Teachable Machine interface details must be checked against the live tool before scripting: project type names, default class names, the Webcam and Upload options, the Train button, the Preview area, advanced settings and export options.
- [VERIFY] Where Teachable Machine stores images during and after training (in the browser only, or saved with a project) must be confirmed from the tool's current privacy information before the privacy note is recorded.
