# L16 Capstone Part 2: Evaluate, Improve and Present

Course: AI-19 · Module: M4 · Objectives: O5, O6, O7 · Video: 5 min (screen demo)

## Hook
Your app counted correctly on the photos you tried yesterday. But you chose those photos, and you knew they would work. Today you test it on images it has never seen, find where it fails, fix one thing, and decide honestly whether anyone should rely on it.

## Explanation
The second part of the capstone has four steps.

**1. Build a fair test set.** Collect at least 20 new images or short clips that were not used for training, validation or threshold choice. Cover the conditions of real use: different times of day, angles, distances, crowded and empty scenes. Write the condition next to each item, and count the true number of target objects by hand.

**2. Measure errors.** For a counting app, the main number is the **count error**: the difference between the app's count and the true count for each image. Report the **mean absolute error** (the average size of the error) and the error for each condition. Where you have labelled boxes, also report precision and recall (L08) or mAP (L09), so you can see whether errors come from missed objects or from false alarms.

**3. Make one improvement and measure it again.** Look at the worst cases and group them by cause, as in L08. Then choose one change that targets the biggest group:

- **More training images** of the failing condition, such as evening light or the bottom shelf.
- **A better threshold,** chosen on a separate set of images, not on your test set.
- **Preprocessing,** such as resizing or contrast correction with OpenCV (L03).

Change one thing at a time and rerun the same test set, so you know what caused the difference. Report the result even if it did not help.

**4. Judge fitness and present.** Update your fitness check from L14 with the new numbers: accuracy, speed, privacy and licence, and a clear decision. Then record a 3-minute demo: the problem (30 seconds), the app working (60 seconds), results and failures (60 seconds), and your decision (30 seconds).

**Analogy:** Evaluation is like a driving test on roads the learner has not practised. Driving well around your own street proves little. The examiner chooses the route, includes a busy junction and a hill start, and writes down every mistake.

## Worked Example
Aigerim Seitkali, a developer in Almaty, Kazakhstan, built an app that counts parked vehicles in a car park from a fixed camera. She tests it on 24 new photos: 8 by day, 8 in the evening and 8 in rain. The photos are taken from far enough away that people cannot be identified, and number plates are not readable. Her first results show large errors in rain and in the evening, where dark cars are missed. She adds a contrast correction step with OpenCV and runs the same test set again.

```python
import pandas as pd

df = pd.read_csv("test_results.csv")   # image, condition, true, before, after
for col in ["before", "after"]:
    df[col + "_err"] = (df[col] - df["true"]).abs()

print(df[["before_err", "after_err"]].mean().round(2))
print(df.groupby("condition")[["before_err", "after_err"]].mean().round(2))
```

Output (shortened; from her example data):

```text
before_err    0.75
after_err     0.46
           before_err  after_err
day              0.12       0.25
evening          0.62       0.25
rain             1.50       0.88
```

The mean error falls from 0.75 to 0.46 vehicles per photo. Evening and rain improve, but daytime becomes slightly worse, because the correction makes some reflections look like cars. Aigerim reports this honestly. Her decision: fit for hourly occupancy estimates, where an error of one vehicle is acceptable; not fit for billing individual drivers; rain still needs more training images.

**On screen (presenter steps):**
1. Open a spreadsheet with the columns image, condition, true, before and after, and fill a few rows.
2. Upload it to Colab as `test_results.csv` and run the cell.
3. Point to the condition with the largest error and open two of its images.
4. Show the updated fitness check with the new numbers.
5. Show the outline of the 3-minute demo on one slide.

## Common Mistake
Many learners tune the threshold or preprocessing while looking at the test results, then report the improved test score. The test set has then been used for training decisions, so the score is too optimistic. Choose changes using separate images, and use the test set only to measure before and after. Another mistake is hiding failures in the demo. Showing where the app fails, and why, is part of the grade.

## Key Takeaways
1. Evaluate on at least 20 new images or clips that cover real conditions, and report errors for each condition.
2. Make one targeted improvement, rerun the same test set, and report the result even when it is mixed.
3. End with a clear fitness decision that states where the app can and cannot be used.

## Hands-on Exercise
**Task:** Capstone step 2: evaluate your app on at least 20 new test images or clips, make one improvement, and record a 3-minute demo with your fitness check.
**Tools:** Google Colab; your L15 app; a spreadsheet; pandas; any free screen recorder. Show objects and scenes, not identifiable people.
**Steps:**
1. Collect at least 20 new test images or clips and record the condition of each.
2. Count the true number of target objects by hand.
3. Run your app and record its count for each item.
4. Calculate the mean absolute error overall and for each condition.
5. Group the worst cases by cause and choose one improvement.
6. Apply it, rerun the same test set, and compare before and after.
7. Update your fitness check and record the 3-minute demo.
**What good looks like:** A test table with at least 20 rows, before-and-after errors by condition, one improvement with an honest result, an updated fitness check with a clear decision, and a demo that shows at least one failure.
**Time:** about 90 minutes

## Review Flags
- None. The lesson uses a hypothetical example and general evaluation methods; the pandas code was run on example data, and its numbers are illustrations, not benchmarks. Licence and privacy points refer back to the flagged content in L14 and L15.
