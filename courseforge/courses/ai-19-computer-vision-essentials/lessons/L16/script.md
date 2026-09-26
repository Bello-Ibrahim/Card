# L16 Capstone Part 2: Evaluate, Improve and Present | Presenter Script

Course: AI-19 · Video: 5 min · Words: 689

## Hook
Your app counted correctly on the photos you tried. But you chose those photos, and you knew they would work. Today, you test it on images it has never seen, fix one thing, and decide honestly whether anyone should rely on it.

## Explain
This is the final lesson, and the second part of your capstone. It has four steps. First, build a fair test set. Collect at least twenty new images or clips that were never used for training, validation or choosing a threshold.

Cover the conditions of real use. Different times of day, angles and distances, crowded and empty scenes. Write the condition next to each item, and count the true number of objects by hand.

Second, measure the errors. For a counting app, the main number is the count error, the difference between the app's count and the true count. Report the mean absolute error, which is the average size of the error, overall and for each condition. Where you have labelled boxes, add precision and recall, or mAP.

Third, make one improvement. Group the worst cases by cause, then choose one change for the biggest group. More training images, a better threshold chosen on separate images, or preprocessing with OpenCV. Change one thing at a time, rerun the same test set, and report the result, even if it did not help.

Fourth, judge fitness and present. Update your fitness check with the new numbers, and end with a clear decision. Then record a three-minute demo. The problem, the app working, results and failures, and your decision.

Evaluation is like a driving test on roads the learner has not practised. Driving well on your own street proves little. The examiner chooses the route, includes a busy junction and a hill start, and writes down every mistake.

## Demonstrate
Aigerim Seitkali, a developer in Almaty, Kazakhstan, built an app that counts parked vehicles from a fixed camera. She tests it on twenty-four new photos. Eight by day, eight in the evening and eight in rain, all taken from far away.

Her first results show large errors in rain and in the evening, where dark cars are missed. So she adds a contrast correction step with OpenCV, and runs the same test set again. She keeps everything in a spreadsheet, with the image, the condition, the true count, and the counts before and after.

In Colab, she uploads the file and runs a short cell. The mean error falls from zero point seven five to zero point four six vehicles per photo.

The breakdown tells the real story. Evening improves from zero point six two to zero point two five. Rain improves from one point five zero to zero point eight eight. But daytime gets slightly worse, from zero point one two to zero point two five, because the correction makes some reflections look like cars. She opens two rain images to see why.

She reports this honestly, in her updated fitness check. Her decision. Fit for hourly occupancy estimates, where an error of one vehicle is acceptable. Not fit for billing individual drivers. And rain still needs more training images. Finally, she shows the outline of her three-minute demo.

A common mistake is to tune the threshold while looking at the test results. Then the test score is too optimistic. Choose changes on separate images. And never hide failures in your demo. Showing where the app fails, and why, is part of the grade.

## Recap
Let's recap. First, evaluate on at least twenty new images or clips that cover real conditions, and report errors for each condition. Second, make one targeted improvement, rerun the same test set, and report the result, even when it is mixed. Third, end with a clear fitness decision that says where the app can and cannot be used.

## CTA
Congratulations on finishing Computer Vision Essentials. You have gone from pixels to a working, tested app. Now complete capstone step two in the exercise below. Test your app, make one improvement, update your fitness check, and record your demo. Remember to check the Ultralytics YOLO licence before any commercial use. Then submit your capstone. Well done.

## Thumbnail
Headline: Test It Honestly
Image: Navy background, a car park photo in rain beside a small before-and-after bar chart of count errors, headline in teal Inter Bold.

## Production Notes
- No new facts to verify (content.md Review Flags: None). The pandas code was run on example data; the voiceover states its numbers exactly as content.md reports them: mean error 0.75 before and 0.46 after; day 0.12 to 0.25; evening 0.62 to 0.25; rain 1.50 to 0.88. These are illustrations, not benchmarks. Prepare test_results.csv from the same example data so the recorded run prints exactly these values.
- Licence and privacy points refer back to L14 and L15 flags: the voiceover repeats only that the Ultralytics YOLO licence must be checked before commercial use, with no legal claims.
- Footage: car park photos are taken from far enough away that people cannot be identified and number plates are not readable. Aigerim Seitkali and the Almaty car park are fictional.
- Screen recording: clean browser profile, no account names or other tabs visible. The spreadsheet can be any free spreadsheet tool; do not show a brand name.
