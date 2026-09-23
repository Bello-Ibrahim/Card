# L14 Responsible Vision: Privacy, Bias and Licences

Course: AI-19 · Module: M4 · Objectives: O6 · Video: 5 min (screen demo)

## Hook
Your vehicle counter works. Then someone asks: "Who is visible in your videos, and did they agree?", "Does it work at night?" and "Are you allowed to sell it?" If you cannot answer, the project is not ready, however good the mAP is.

## Explanation
Before you deploy a vision system, check four areas: privacy, bias, licences and fitness for use.

**Privacy.** Cameras record people, even when you only want cars or shelves, and faces, number plates and clothes can identify a person. Good practice: **collect less** (point the camera only where needed and prefer counts over stored video), **blur people** before you store or share frames, **limit storage** (who can access video and when it is deleted), and **inform and ask** (clear notices, and consent where the law requires it).

Laws on cameras, face data, consent and data storage differ by country and sometimes by city. This lesson gives general guidance, not legal advice; check the rules where you deploy. [REGION] Never upload real camera footage of people to online AI tools for testing.

**Bias.** A model works best on data like its training data. A detector trained mostly on daytime images from one country may miss vehicle types, shop layouts or lighting it rarely saw. Test in the real place, at different times and in different weather, and report each condition separately.

**Licences.** Check every model, dataset and code library before commercial use. The `ultralytics` package is AGPL-3.0, with a separate commercial licence. [VERIFY] Hugging Face models and datasets each have their own licence, and some allow only research use.

**Fitness for use.** Accuracy alone does not decide. Ask: are the errors acceptable for this decision, is the speed enough for real time or is batch processing fine, and what happens when the system is wrong?

**Analogy:** A fitness check is like a safety inspection before a new bus goes into service. The engine may be excellent, but the inspector also checks the brakes, the doors and the insurance. A bus that fails any check stays in the depot.

## Worked Example
Oluwaseun Adeyemi builds a system to count delivery vans at a logistics depot in Lagos, Nigeria. The camera also records workers walking across the yard. He adds a step that blurs every detected person before any frame is saved.

```python
import cv2

def blur_boxes(frame, boxes, k=51):
    """Blur each (x1, y1, x2, y2) box in place. k must be odd."""
    h, w = frame.shape[:2]
    for x1, y1, x2, y2 in boxes:
        x1, y1 = max(0, int(x1)), max(0, int(y1))
        x2, y2 = min(w, int(x2)), min(h, int(y2))
        if x2 > x1 and y2 > y1:
            frame[y1:y2, x1:x2] = cv2.GaussianBlur(
                frame[y1:y2, x1:x2], (k, k), 0)
    return frame

# inside the YOLO loop from L13 (class 0 is "person" in COCO):
# people = r.boxes.xyxy[r.boxes.cls == 0].tolist()
# frame = blur_boxes(r.orig_img.copy(), people)
```

He blurs the whole person box, not only the face. A face detector, such as OpenCV's bundled Haar cascade files, misses faces that are small, turned away or in shadow, and clothes can also identify people. [VERSION] He also checks sample frames by eye, because a missed detection means an unblurred person.

His half-page fitness check:

- **Accuracy:** van count within 5% of the manual count on 10 daytime clips; not yet tested at night.
- **Speed:** processes a 1-minute clip in about 40 seconds on a Colab GPU; batch processing every hour is enough.
- **Privacy:** people blurred before storage, raw video deleted after 24 hours, notices at the gate; local rules to be confirmed with the company lawyer. [REGION]
- **Licence:** AGPL-3.0 detector used internally; legal review needed before offering it to other depots. [VERIFY]
- **Decision:** fit for an internal pilot during daytime; not yet fit for night use or for sale.

These figures are his example results, not benchmarks.

**On screen (presenter steps):**
1. Add `blur_boxes` to the L13 notebook and call it on person boxes before each frame is written.
2. Play the output and pause on a frame with blurred people.
3. Show the fitness check as a text cell with the five headings.

## Common Mistake
Many developers treat privacy and licences as paperwork for after the app is built. By then the video is already stored, and the model may be in a product the licence does not allow. Build blurring and storage limits into the first version, and check licences before you choose a model.

## Key Takeaways
1. Collect less, blur people, limit storage and follow local rules on cameras and consent.
2. Test for bias by measuring results separately for different conditions, places and times.
3. A fitness check covers accuracy, speed, privacy and licences, and ends with a clear decision.

## Hands-on Exercise
**Task:** Add a step that blurs faces or people in your video output with OpenCV, then write a half-page fitness check for your use case: accuracy, speed, privacy and licence.
**Tools:** Google Colab; OpenCV; the `ultralytics` package [VERSION]; your L13 notebook and clip.
**Steps:**
1. Add the `blur_boxes` function to your notebook.
2. Detect people with the class filter for "person" and blur each box before the frame is saved.
3. Watch the output and note any frame where a person is not blurred.
4. List every model, dataset and library you use, with its licence and a link to its licence page.
5. Write a half-page fitness check with the headings Accuracy, Speed, Privacy, Licence and Decision.
6. Name one condition you have not tested, such as night or rain.
**What good looks like:** An output video where people are blurred, a component list with licences, and a fitness check that uses your own measured numbers and ends with a clear, limited decision.
**Time:** about 35 minutes

## Review Flags
- [REGION] Curriculum flag: laws on cameras, face data, consent, notices and video storage periods differ by country; the lesson gives general guidance, not legal advice.
- [VERIFY] Curriculum flag: Ultralytics licence (AGPL-3.0 with a separate commercial licence) must be confirmed before scripting; learners must check terms before commercial use.
- [VERSION] Curriculum flag: OpenCV bundled face detection models (Haar cascade files via `cv2.data.haarcascades`) and the `ultralytics` result attributes (`boxes.cls`, `orig_img`). The `blur_boxes` function was run with opencv-python-headless on a synthetic frame; fitness-check figures are example values.
