# L11 Build Your Own Image Classifier

Course: AI-01 · Module: M3 · Objectives: O4, O2 · Video: 5 min (screen demo)

## Hook
For ten lessons you have learned how machines learn from examples. Today you will teach one yourself, in your web browser, with no code and no maths. In about half an hour, you will have a working model that recognises objects you chose, and you will see exactly where it succeeds and where it fails.

## Explanation
Google Teachable Machine is a free, browser-based tool for training simple models. In this lesson we use an **image project**: a model that looks at a picture and predicts which class it belongs to. This is supervised classification, which you met in L05.

Every step in the tool matches a term you already know:

- **Classes are your labels.** Each class is a category, such as "banana" or "orange". You give each class a name.
- **Example images are your data.** You add pictures to each class, either from your webcam or by uploading files.
- **Features are found by the model.** You do not tell it "look for the colour yellow". During training it finds its own patterns, such as shapes, colours and textures, as you saw in L07.
- **Training** is the step where the model adjusts its internal dials to match your images to your labels.
- **Testing and prediction** happen in the preview area. You show the model new images it has never seen, and it gives a confidence for each class.

The basic workflow is below. The tool's interface may change, so the button names and layout here are a general guide. [VERSION]

1. Open Teachable Machine in your browser, start a new project and choose an image project with the standard image model. [VERSION]
2. You will see two empty classes with default names. Click each name and rename it, for example "banana" and "orange". Add a third class if you want. [VERSION]
3. For each class, add images using the **Webcam** option (hold the object in front of the camera and record a series of frames) or the **Upload** option (choose image files from your device). [VERSION]
4. Click the **Train** button and wait. Keep the browser tab open while it trains. [VERSION]
5. When training finishes, use the **Preview** area. Show the model new objects with the webcam, or upload new images, and read the confidence bars for each class. [VERSION]

Some versions offer advanced training settings and ways to export or save the project. You do not need these for the capstone. [VERSION]

**Privacy note:** Use objects, not people. Good choices are types of fruit, pens vs. cups, or different shoes. Do not use photos of other people without their clear consent. Check the tool's own privacy information about where your images are stored before you upload anything personal. [VERIFY]

**Analogy:** Training a classifier is like teaching a young child to name fruit by showing them real examples. If you only ever show bright yellow bananas on a white table, the child may be confused by a green banana on a wooden table. The more varied your examples, the better the child, or the model, can handle new cases.

## Worked Example
Chiamaka runs a small recycling project at a community centre in Enugu, Nigeria. She wants a simple demonstration that tells "plastic bottle" from "metal can".

She creates two classes with those names. Using her laptop webcam, she records about 30 images per class: bottles and cans of different sizes and colours, held at different angles, some crushed and some whole. She keeps the same plain wall in the background.

She trains the model and tests it with 10 new items she did not use in training. The model gets 8 right. It fails on a clear bottle held in front of a window, and on a can with a very shiny silver label. Chiamaka notes a pattern: her training images all had the same dull background and indoor light. The model may have learned "bright and shiny" as a sign of "can", and a very bright scene confused it.

She adds 10 more images per class taken near the window, trains again, and tests again with new items. The results improve. This is the full cycle: data, labels, training, testing, and improving the data.

## Common Mistake
Many learners test the model with the same objects, or even the same angle and light, that they used for training. The results look perfect, but this tells you almost nothing. As L08 explained, a fair test uses examples the model has never seen. Always test with new objects, new angles, new backgrounds or new lighting, and record the results honestly, including the failures. The failures are the most useful part of your capstone.

## Key Takeaways
1. In Teachable Machine, classes are labels, your images are the data, the Train button runs training, and the preview is where the model makes predictions.
2. Varied examples (angles, backgrounds, lighting) help the model handle new cases. Narrow examples can teach it the wrong pattern.
3. Test with new images the model has never seen, and record every result, including the mistakes.

## Hands-on Exercise
**Task:** Capstone step 1: train a classifier with at least 2 classes and 20+ images per class, then test it on 10 new images and record the results.
**Tools:** Google Teachable Machine (free, in a web browser); a webcam or a phone to take photos; everyday objects; a notes app or a simple table on paper.
**Steps:**
1. Choose 2 or 3 classes of objects that are easy to find, such as apples vs. oranges, or pens vs. cups. Do not use photos of other people without their consent.
2. Create an image project and rename the classes. [VERSION]
3. Add at least 20 images to each class. Vary the angle, distance, background and lighting.
4. Train the model and keep the tab open until training finishes.
5. Collect 10 new test images or objects that were not used in training. Include at least 2 difficult cases, such as an unusual colour or a busy background.
6. Test each one and record, in a table: the test item, the true class, the predicted class, the confidence shown, and "correct" or "wrong".
7. Take a screenshot of your classes and one of a test result. Keep your table for L12.
**What good looks like:** A trained model with at least 2 named classes and 20+ varied images each, a table of 10 test results with honest notes on mistakes, and screenshots as evidence.
**Time:** about 35 minutes

## Review Flags
- [VERSION] Teachable Machine interface details must be checked against the live tool before scripting: project type names, default class names, the Webcam and Upload options, the Train button, the Preview area, advanced settings and export options.
- [VERIFY] Where Teachable Machine stores images during and after training (in the browser only, or saved with a project) must be confirmed from the tool's current privacy information before the privacy note is recorded.
