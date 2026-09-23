# L01 What Is Computer Vision? | Presenter Script

Course: AI-19 · Video: 5 min · Words: 720

## Hook
A farmer takes a photo of a leaf and learns which disease it has. A machine reads an address and sends a parcel down the right belt. None of these systems see like we do. But all of them turn pixels into useful information.

## Explain
Hi, and welcome to Computer Vision Essentials. In this first lesson, we answer a simple question. What is computer vision?

Computer vision is the part of AI that extracts information from images and video. The input is always a grid of pixel values. The output depends on the question you ask. Most real projects use one of four main tasks.

The first task is image classification. It answers the question, what is in this image? The model returns one label for the whole image, such as healthy leaf, or leaf rust. It does not say where the problem is. Picture an app that helps farmers in India check a photo of a crop leaf.

The second task is object detection. It answers, what is in this image, and where? Each object gets a class, a confidence score and a bounding box, which is a rectangle in pixel coordinates. Because each object has its own box, detection lets you count. Picture a traffic system in Nairobi that counts buses and cars in every frame.

The third task is segmentation. Instead of a rectangle, the model labels every pixel. This helps when the exact shape or area matters, for example how much of a leaf is damaged. It needs more detailed labels and more computing power, so this course covers it only here.

The fourth task is optical character recognition, or OCR. It answers, which text is in this image? It turns text into characters you can search and edit. Picture a parcel sorting centre in Germany that reads postcodes on labels.

Here is a simple way to remember them. Imagine four assistants looking at the same photo of a market stall. The first says, fruit stall. The second puts a sticky note on every mango and every orange. The third cuts out the exact shape of each fruit with scissors. The fourth reads the price labels aloud. Same photo, four questions, four amounts of work.

## Demonstrate
Let's use this in a real situation. Ana Lucía Ramírez leads a small logistics start-up in Lima, Peru. Her team has four ideas, and for each one they must choose the right vision task.

The first idea is to flag photos of damaged boxes. One answer per photo is enough, damaged or not damaged, so that is classification. The second idea is to count pallets in a loading bay. Counting needs one box per pallet, so that is detection. A classifier would only say that pallets are present.

The third idea is to measure how full a truck is. The team needs the area covered by goods, not a rough rectangle, so that is segmentation. The fourth idea is to read tracking numbers on labels. The output must be text, so that is OCR, usually after detection finds the label first.

So which idea does Ana Lucía build first? The classification idea, because it needs the least labelling work. She keeps the pallet idea for later. To choose a task, ask two questions. Do I need to know where things are? And do I need boxes, exact shapes or text?

A common mistake is to choose the most powerful task because it sounds better. Segmentation needs more detailed labels, more computing and more time. The opposite mistake happens too. A classifier can say cars, but it cannot say seven cars.

## Recap
Let's recap. First, computer vision turns pixel values into information: a label, a set of boxes, a pixel mask or text. Second, classification answers what, detection answers what and where, segmentation answers which exact pixels, and OCR answers which text. Third, choose the simplest task that supports the real decision, and combine tasks when one is not enough.

## CTA
Now it is your turn. In the exercise below this video, you will match eight real applications to the right task, from counting boats in a harbour to reading an electricity meter. It takes about fifteen minutes. In the next lesson, we open an image in code and look at the numbers inside. Images as Numbers: Pixels, Channels and Colour. See you there.

## Thumbnail
Headline: Four Ways Machines See
Image: Navy background, one photo of a market stall repeated four times as small tiles: a label, boxes, cut-out shapes and price text, headline in teal Inter Bold.

## Production Notes
- No facts to verify: all examples are hypothetical and describe general task types (content.md Review Flags: None).
- Ana Lucía Ramírez and her Lima logistics start-up are fictional. Stock footage must not show a real company name, logo or readable tracking numbers.
- Stock footage policy for this course: show objects, vehicles and scenes, not identifiable people. Traffic and warehouse clips must be wide shots with no readable number plates and no recognisable faces.
- This lesson has no screen demo (not in screen_demo_lessons). Segmentation is covered in this lesson only; the voiceover says so.
