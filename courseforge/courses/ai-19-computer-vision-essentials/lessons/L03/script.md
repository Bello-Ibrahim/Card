# L03 Image Processing with OpenCV | Presenter Script

Course: AI-19 · Video: 5 min · Words: 692

## Hook
Not every vision problem needs a neural network. Some can be solved with a few lines of OpenCV that run in milliseconds on any laptop. And when you do use a model, those same few lines often decide whether it succeeds or fails.

## Explain
In the last lesson, we saw that an image is just an array of numbers. OpenCV gives you fast, predictable operations on those arrays. Let's meet the core ones you will use throughout this course.

Resize changes the size, because models expect a fixed input size, and smaller images are faster. Remember that resize takes width first. Crop needs no function at all. It is plain array slicing. Greyscale reduces three channels to one, and many later steps work on one channel.

Blur averages each pixel with its neighbours. It removes small noise, like paper texture or camera grain. The kernel size must be an odd number, such as five by five. Threshold turns a greyscale image into pure black and white. With the Otsu option, OpenCV chooses the cut-off value for you. When the lighting is uneven, adaptive threshold chooses a different value for each small area.

Edge detection, with the Canny function, marks pixels where brightness changes sharply. It takes a low and a high threshold. Raise them to keep only strong edges. Then find contours joins edge pixels into outlines. From an outline, you can get its area or a bounding rectangle.

Think of image processing like preparing vegetables before cooking. You wash them, which is the blur. You cut them to size, which is resize and crop. And you sort them, which is the threshold. A good cook can still manage with bad preparation, but the result is better when the preparation is done well.

You use these steps in two ways. First, as preprocessing before a model, so your inputs look more like the training data. Second, as a complete solution, when the scene is simple and controlled, like a document on a plain desk.

## Demonstrate
Here is a real case. Fatou Diop works for a microfinance office in Dakar, Senegal. Field staff photograph paper forms on their desks. She needs a clean black-and-white image of each form. She tests with a sample form that holds no real customer data.

In Colab, she uploads the photo and runs the first three lines. They load the image, turn it grey, and apply a five by five blur. Showing the blurred image next to the original, you can see the paper texture fade away.

Next, she runs edge detection and finds the contours. She keeps the largest outline, because the paper is lighter than the desk, so it forms the biggest shape. She draws its rectangle on a copy of the photo to check it.

Then she crops to that rectangle and applies Otsu's threshold. The desk is gone, and the text is black on white. The output line shows nine hundred, twelve hundred, three, turning into seven hundred and sixty, five hundred and forty.

Now watch what happens when she lowers the edge thresholds to ten and thirty. Many more edges appear, from the wood grain and small shadows. The thresholds really matter.

This is also the common mistake. Learners copy values from a tutorial and expect them to work on every photo. A blur that suits a large photo may remove the text from a small one. Display every step, and test on photos with different lighting.

## Recap
Let's recap. First, the core OpenCV steps are resize, crop, greyscale, blur, threshold, edges and contours, and each one returns a new array you can inspect. Second, use them to prepare images for a model, or on their own when the scene is simple and controlled. Third, the right values depend on the image, so check every result.

## CTA
Now it is your turn. In the exercise below this video, you will turn a phone photo of a document into a clean black-and-white image, with greyscale, blur, threshold and crop. It takes about thirty minutes. In the next lesson, we move from single images to moving pictures. Working with Video Frames. See you there.

## Thumbnail
Headline: Six Lines, Clean Image
Image: Navy background, a tilted phone photo of a paper form on a wooden desk on the left, a crisp black-and-white scan on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] OpenCV function names and signatures (findContours return values, THRESH_OTSU, Canny) must be checked against the OpenCV version in Colab at recording time. Code in content.md was tested with opencv-python-headless on a synthetic image.
- Run outputs: the voiceover states the output '(900, 1200, 3) -> (760, 540)' exactly as content.md reports. Prepare form.jpg at 1200 × 900 pixels and confirm that the recorded run prints exactly this line. If the crop size differs, change the sample photo, not the voiceover, or re-record the scene with 'something like'.
- The number of extra edges with Canny thresholds of 10 and 30 is not given in content.md; the voiceover only says 'many more edges'.
- Fatou Diop and the Dakar microfinance office are fictional. The sample form must contain no real customer data, names or signatures, and no people appear in the photo.
- Screen recording: clean browser profile, no account names or other tabs visible.
