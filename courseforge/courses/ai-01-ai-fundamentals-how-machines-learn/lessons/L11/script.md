# L11 Build Your Own Image Classifier | Presenter Script

Course: AI-01 · Video: 5 min · Words: 689

## Hook
You have learned how machines learn from examples. Today, you will teach one yourself, in your web browser, with no code and no maths. You will build a model that recognises objects you choose, and see where it succeeds, and where it fails.

## Explain
We will use Google Teachable Machine. It is a free tool that trains simple models in your browser. We will make an image project, a model that looks at a picture and predicts its class. That is supervised classification, from lesson five.

Every step in the tool matches a word you already know. The classes are your labels. The example images are your data. You do not choose the features. The model finds its own patterns, like shapes, colours and textures. Training adjusts the model's dials. And the preview is where you test it, with new images.

It is like teaching a young child to name fruit with real examples. If you only show yellow bananas on a white table, a green banana on a wooden table may confuse them. Varied examples help the child, and the model, handle new cases.

One privacy point before we start. Use objects, such as fruit, or pens and cups. Do not use photos of other people without their clear consent. And check the tool's privacy information before you begin.

## Demonstrate
Let's follow Chiamaka. She runs a small recycling project at a community centre in Enugu, Nigeria. She wants a simple demonstration that tells a plastic bottle from a metal can. Let's build it together.

First, open Teachable Machine in your browser. Start a new project, and choose a standard image project. The interface may look a little different when you try it, so follow the ideas, not the exact screen.

Next, rename the two empty classes. Chiamaka calls them plastic bottle, and metal can. These are the labels. You can add a third class if you want.

Now add the data. Use the Webcam option to record frames of each object, or the Upload option to choose image files. Chiamaka records about thirty images per class. She uses different sizes and colours, different angles, and some crushed and some whole items.

Then click Train, and keep the browser tab open until it finishes. This is the training phase. The model is nudging its dials to match the images to the labels.

Now test it in the preview area, with ten new items it has never seen. For each one, read the confidence bars. Chiamaka's model gets eight out of ten right.

It fails on a clear bottle held in front of a window, and on a very shiny can. Her training images all had dull indoor light. So the model may have learned that bright and shiny means can. She adds images taken near the window, trains again, and tests with new items. The results improve.

You do not need the advanced settings or the export options for your capstone. But before you close the tab, take two screenshots. One of your classes, and one of a test result. You will need them as evidence.

That is the full cycle. Data, labels, training, testing, and better data. And watch out for one mistake. If you test with the same objects, angles and light you trained on, the results look perfect, but they tell you almost nothing. Test with new objects, backgrounds and lighting, and record the failures honestly.

## Recap
Let's recap. First, in Teachable Machine, classes are labels, your images are the data, the Train button runs training, and the preview is where the model makes predictions. Second, varied examples help the model handle new cases. Third, test with new images the model has never seen, and record every result, including the mistakes.

## CTA
Now it is your turn. This is step one of your capstone. Train a classifier with at least two classes, and twenty or more varied images per class. Then test it on ten new images, and record the results in a table, with two screenshots. Keep them safe. In the last lesson, Should I Trust This AI? A Practical Checklist, you will explain your model. See you there.

## Thumbnail
Headline: Train Your Own Model
Image: Navy background, a laptop webcam view of a plastic bottle and a metal can, with two teal confidence bars beside them, headline in teal Inter Bold.

## Production Notes
- [VERSION] Record the screen demo in Google Teachable Machine only after checking the live tool: project type names, the default class names, the Webcam and Upload options, the Train button, the Preview area, advanced settings and export options. Adjust the screen_steps to the live labels; the voiceover avoids exact button names except Train, Webcam, Upload and Preview, so change those words too if the live tool uses different ones.
- [VERSION] The voiceover says learners do not need the advanced or export options. Keep this if it still holds for the live tool.
- [VERIFY] Where Teachable Machine stores images during and after training is NOT stated in the voiceover. It only tells learners to check the tool's privacy information. Confirm from the tool's current privacy information before adding any claim.
- Screen recording: record with the OBS Screen Demo Pack in a clean browser profile with no bookmarks, extensions, account names or other tabs visible. Use a plain wall background, and do not show any person on the webcam; only hands holding objects.
- Chiamaka's recycling project in Enugu is fictional; the demo recreates her bottle-and-can example. Use unbranded bottles and cans, or turn labels away from the camera.
- Scenes 7 to 13 are screen scenes. Where the real training time is longer than the scene, speed up the recording or cut the progress bar.
