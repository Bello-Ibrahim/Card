# L14 Responsible Vision: Privacy, Bias and Licences | Presenter Script

Course: AI-19 · Video: 5 min · Words: 700

## Hook
Your vehicle counter works. Then someone asks. Who is visible in your videos, and did they agree? Does it work at night? Are you allowed to sell it? If you cannot answer, the project is not ready, however good the mAP is.

## Explain
In the last lesson, you counted vehicles in video. Before you deploy a system like that, check four areas. Privacy, bias, licences, and fitness for use.

Privacy first. Cameras record people, even when you only want cars or shelves. Good practice has four parts. Collect less, and prefer counts over stored video. Blur people before you store or share frames. Limit who can access video, and when it is deleted. And inform people, with clear notices and consent where the law requires it.

Laws on cameras, consent and storage differ by country, and sometimes by city. This is general guidance, not legal advice, so check the rules where you deploy. And never upload real footage of people to online AI tools for testing.

Bias. A model works best on data like its training data. A detector trained mostly on daytime images from one country may miss vehicle types, shop layouts or lighting it rarely saw. So test in the real place, at different times and in different weather, and report each condition separately.

Licences. Check every model, dataset and library before commercial use. The Ultralytics YOLO licence must be checked before any commercial use, and Hugging Face models and datasets each have their own licence. Some allow research use only. Finally, fitness for use. Are the errors acceptable for this decision? Is the speed enough? And what happens when the system is wrong?

A fitness check is like a safety inspection before a new bus goes into service. The engine may be excellent, but the inspector also checks the brakes, the doors and the insurance. A bus that fails any check stays in the depot.

## Demonstrate
Oluwaseun Adeyemi builds a system to count delivery vans at a logistics depot in Lagos, Nigeria. The camera also records workers walking across the yard. So he adds a step that blurs every detected person before any frame is saved.

He adds a small blur function to his notebook from the last lesson. It takes a frame and a list of boxes, keeps each box inside the image, and applies a strong blur inside it. In the tracking loop, he selects the person boxes and blurs them before each frame is written.

He plays the output and pauses on a frame with workers in the yard. Each person is blurred from head to foot. He blurs the whole person box, not only the face, because face detectors miss small, turned or shadowed faces, and clothes can also identify people.

He also checks sample frames by eye, because one missed detection means one unblurred person. Then he writes his fitness check in a text cell, with five headings. Accuracy, speed, privacy, licence, and decision.

His example results. The van count is within five percent of a manual count on ten daytime clips, but night is untested. A one-minute clip takes about forty seconds, and hourly batches are enough. People are blurred, and raw video is deleted after twenty-four hours. The licence needs legal review before other depots use it. His decision? Fit for a daytime internal pilot only.

A common mistake is to treat privacy and licences as paperwork for later. By then, the video is already stored, and the model may be inside a product its licence does not allow. Check licences before you choose a model.

## Recap
Let's recap. First, collect less, blur people, limit storage and follow local rules. Second, test for bias by measuring results separately for different conditions, places and times. Third, a fitness check covers accuracy, speed, privacy and licences, and ends with a clear decision.

## CTA
Now it is your turn. In the exercise below this video, you will add person blurring to your video output, list the licences of everything you use, and write a half-page fitness check. It takes about thirty-five minutes, and it becomes part of your capstone. In the next lesson, Capstone Part 1: Build Your Detection App. See you there.

## Thumbnail
Headline: Is It Ready to Deploy?
Image: Navy background, a depot yard with delivery vans in teal boxes and walking figures fully blurred, a checklist card with four ticks beside it, headline in teal Inter Bold.

## Production Notes
- [REGION] Laws on cameras, face data, consent, notices and video storage periods differ by country and sometimes by city. The voiceover gives general guidance and says it is not legal advice.
- [VERIFY] Ultralytics licence (content.md: AGPL-3.0 with a separate commercial licence [VERIFY]). The voiceover does not name the licence or make legal claims; it says the Ultralytics YOLO licence must be checked before commercial use, and that Oluwaseun needs a legal review before offering the system to other depots.
- [VERSION] OpenCV bundled face detection models (Haar cascade files via cv2.data.haarcascades) and the ultralytics result attributes (boxes.cls, orig_img). The blur_boxes function was run with opencv-python-headless on a synthetic frame.
- No face recognition anywhere in this lesson. The demo blurs whole person boxes from the detector; it does not identify anyone. Face detectors are mentioned only as the weaker option.
- Footage: the depot clip must be staged or rights-cleared, filmed from a distance, with consenting workers. In every frame shown on screen, whole people must be blurred; check sample frames by eye before export. No readable number plates or company names on vans.
- Fitness-check figures (within 5% on 10 daytime clips, about 40 seconds per 1-minute clip, deletion after 24 hours) are example values from content.md, not benchmarks; the voiceover calls them his example results.
- Oluwaseun Adeyemi and the Lagos depot are fictional.
- Screen recording: clean browser profile, no account names or other tabs visible.
