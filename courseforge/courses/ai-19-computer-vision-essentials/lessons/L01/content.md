# L01 What Is Computer Vision?

Course: AI-19 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
A farmer takes a photo of a leaf and learns which disease it has. A parcel machine reads an address and pushes the box onto the right belt. A city screen shows how many cars passed a junction in the last hour. None of these systems "see" like we do, but all of them turn pixels into useful information. This course shows you how to build systems like these.

## Explanation
**Computer vision** is the part of AI that extracts information from images and video. The input is always a grid of pixel values. The output depends on the question you ask. Most real projects use one of four main tasks.

**1. Image classification: "What is in this image?"** The model returns one label (or a ranked list of labels) for the whole image, such as "healthy leaf" or "leaf rust". It does not say where the object is. A hypothetical example: an app that helps farmers in India check a photo of a crop leaf for disease.

**2. Object detection: "What is in this image, and where?"** The model returns a list of objects. Each object has a class, a confidence score and a **bounding box**: a rectangle given as pixel coordinates. Detection lets you count things, because each object gets its own box. A hypothetical example: a traffic system in Nairobi that counts buses and cars in each frame of a camera feed.

**3. Segmentation: "Exactly which pixels belong to each object?"** Instead of a rectangle, the model labels every pixel. This is useful when the exact shape or area matters, for example measuring how much of a leaf is damaged, or separating a road from the pavement. Segmentation needs more detailed training labels and more computing power, so this course covers it only in this lesson.

**4. Optical character recognition (OCR): "Which text is in this image?"** OCR finds text and turns it into characters you can search and edit. A hypothetical example: a parcel sorting centre in Germany that reads postcodes on labels.

Real systems often combine tasks. A parcel system may first *detect* the label on the box, then run *OCR* only inside that box. A shop system may *detect* products and then *classify* each one as "correctly placed" or "wrong shelf".

To choose a task, ask two questions. First: do I need to know **where** things are, or only **what** is there? If only "what", classification is usually enough and is the cheapest to build. Second: do I need **boxes, exact shapes or text**? Boxes point to detection, exact shapes point to segmentation, and text points to OCR.

**Analogy:** Imagine four assistants looking at the same photo of a market stall. The first says "fruit stall". The second puts a sticky note on every mango and every orange. The third carefully cuts out the exact shape of each fruit with scissors. The fourth reads the price labels aloud. Same photo, four different questions, four different amounts of work.

## Worked Example
Ana Lucía Ramírez leads a small logistics start-up in Lima, Peru. Her team lists four ideas and decides which vision task each one needs.

| Idea | Task | Reason |
|---|---|---|
| Flag photos of damaged boxes | Classification | One answer per photo: "damaged" or "not damaged". Location is not needed. |
| Count pallets in a loading bay | Detection | Counting needs one box per pallet. Classification would only say "pallets present". |
| Measure how full a truck is | Segmentation | The team needs the area covered by goods, not a rough rectangle. |
| Read tracking numbers on labels | OCR (after detection) | The output must be text that matches the database. |

Ana Lucía starts with the classification idea, because it needs the least labelling work. She keeps the pallet idea for later, when the team has time to draw boxes on training images.

## Common Mistake
Many developers choose the most powerful task because it sounds better, for example using segmentation when a count is enough. More detailed tasks need more detailed labels, more computing and more time. Start from the decision the system must support, then choose the simplest task that gives the needed information. The opposite mistake also happens: using classification when you need to count. A classifier can say "cars", but not "seven cars".

## Key Takeaways
1. Computer vision turns pixel values into information: a label, a set of boxes, a pixel mask or text.
2. Classification answers "what", detection answers "what and where", segmentation answers "which exact pixels", and OCR answers "which text".
3. Choose the simplest task that supports the real decision, and combine tasks when one is not enough.

## Hands-on Exercise
**Task:** Match 8 applications to the correct task: classification, detection, segmentation or OCR. For two of them, explain why the other tasks would not be enough.
**Tools:** Pen and paper or any notes app.
**Steps:**
1. Read the list: (a) sorting photos of fruit as "ripe" or "unripe"; (b) counting boats in a harbour photo; (c) reading the numbers on an electricity meter; (d) measuring the area of a lake in a satellite image; (e) checking if a photo shows a cat or a dog; (f) finding every helmet on a building site; (g) turning printed menus into text for a website; (h) outlining the exact shape of each tumour region in a medical scan for a research study.
2. Write one task next to each application.
3. Choose two applications and write two or three sentences each on why the other three tasks would not be enough.
4. Compare your answers with the answer key on the course page.
**What good looks like:** (a) and (e) are classification, (b) and (f) are detection, (d) and (h) are segmentation, (c) and (g) are OCR. The two explanations mention location, counting, exact shape or text output, for example "classification can say 'boats' but cannot count them".
**Time:** about 15 minutes

## Review Flags
- None. All examples are hypothetical and describe general task types; no specific facts, tools or versions need checking.
