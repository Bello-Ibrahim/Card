# L09 Object Detection: Boxes, Classes and IoU | Presenter Script

Course: AI-19 · Video: 5 min · Words: 725

## Hook
A detector draws a box around a car, but cuts off the back of it. Is that correct, or a mistake? Without a clear rule, two people will score the same model differently. That rule is called IoU.

## Explain
Welcome to week three. So far, our models said what is in an image. Now we also ask where. An object detector returns a list of detections, and each one has three parts.

First, a bounding box, usually the top left and bottom right corners in pixels. Some tools use the centre, width and height instead, so always check the format. Second, a class, such as car or bus. Third, a confidence score from zero to one.

Detectors often draw several overlapping boxes for one object. Non-maximum suppression keeps the box with the highest score and removes boxes that overlap it strongly. Libraries usually do this for you.

Intersection over union, or IoU, measures how well a predicted box matches the true box that a person drew. It is the area of overlap divided by the area of the union, which is everything either box covers. IoU is one for a perfect match, and zero when the boxes do not touch.

To score a detector, you pick an IoU threshold, often zero point five. A prediction with the right class and enough overlap is a true positive. Otherwise it is a false positive. And every true box with no match is a false negative. From these counts, you get precision and recall, like last week.

Average precision summarises precision and recall for one class, and mAP averages it over all classes. There are two common versions. mAP fifty uses a threshold of zero point five. mAP fifty to ninety-five averages stricter thresholds, so it is always lower or equal for the same model.

Picture laying a transparent sheet with your box over the true box on a light table. Measure where they overlap, and divide by the total area they cover. A box that is too big and a box that is too small both lose points.

## Demonstrate
Nadia Rahman evaluates a parking detector for a shopping centre in Dhaka, Bangladesh. For one car, the true box runs from one hundred, fifty to three hundred, one hundred and fifty. The predicted box runs from one hundred and fifty, seventy to three hundred and thirty, one hundred and seventy.

The true box is two hundred by one hundred, so its area is twenty thousand. The predicted box is one hundred and eighty by one hundred, so eighteen thousand. The overlap is one hundred and fifty wide and eighty high, which is twelve thousand.

The union is twenty thousand plus eighteen thousand, minus the overlap, so twenty-six thousand. Twelve thousand divided by twenty-six thousand gives an IoU of about zero point four six.

At a threshold of zero point five, this prediction is a false positive, and the car counts as a false negative, even though the box is clearly on the car. Nadia notices that the boxes often shift towards the car's shadow, something to fix with more training images.

She checks her answer with a short function. It finds the corners of the overlap, multiplies width by height, and divides by the union. It prints zero point four six two. Note the parts that stop the width or height going below zero. Without them, two boxes that do not touch could show a false overlap.

A common mistake is to compare mAP numbers from different sources. Only compare the same version, on the same test set. And never mix box formats, because the wrong format gives wrong IoU values without any error.

## Recap
Let's recap. First, a detector returns a box, a class and a confidence score for each object, and non-maximum suppression removes duplicate boxes. Second, IoU is overlap divided by union, and a threshold such as zero point five decides whether a prediction counts. Third, compare mAP values only with the same version and the same test set.

## CTA
Now it is your turn. In the exercise below this video, you will calculate IoU by hand for three pairs of boxes, then check your answers with a short Python function. It takes about twenty minutes. In the next lesson, we run a real detector. Running YOLO on Images and Video. See you there.

## Thumbnail
Headline: Is This Box Correct?
Image: Navy background, a top-down car park photo with two overlapping boxes on one car, one green and one teal, the overlap shaded, headline in teal Inter Bold.

## Production Notes
- No facts to verify: this is a concept lesson with a hypothetical example (content.md Review Flags: None). The IoU function and all worked numbers (20,000; 18,000; 12,000; 26,000; IoU 0.46, printed as 0.462) were run and checked in Python.
- Not a screen demo lesson: the code check is shown as a code slide, not a live notebook.
- Nadia Rahman and the Dhaka shopping centre are fictional. Car park stock footage should be top-down or distant, with no readable number plates and no identifiable people.
