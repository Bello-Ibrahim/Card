# Screen Demo Pack: AI-19 L16 Capstone Part 2: Evaluate, Improve and Present

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-19-computer-vision-essentials_L16_screen_1.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Open a spreadsheet with the columns image, condition, true, before and after
2. Fill in a few rows
3. Export it as test_results.csv

**Narration over this clip (for pacing)**

> Her first results show large errors in rain and in the evening, where dark cars are missed. So she adds a contrast correction step with OpenCV, and runs the same test set again. She keeps everything in a spreadsheet, with the image, the condition, the true count, and the counts before and after.

## Clip 2: scene 10

- **Filename:** `ai-19-computer-vision-essentials_L16_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Upload test_results.csv to Colab
2. Run the pandas cell
3. Point to the overall means: before_err 0.75, after_err 0.46

**Narration over this clip (for pacing)**

> In Colab, she uploads the file and runs a short cell. The mean error falls from zero point seven five to zero point four six vehicles per photo.

## Clip 3: scene 11

- **Filename:** `ai-19-computer-vision-essentials_L16_screen_3.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Point to the per-condition table: day 0.12 to 0.25, evening 0.62 to 0.25, rain 1.50 to 0.88
2. Open two images from the rain condition

**Narration over this clip (for pacing)**

> The breakdown tells the real story. Evening improves from zero point six two to zero point two five. Rain improves from one point five zero to zero point eight eight. But daytime gets slightly worse, from zero point one two to zero point two five, because the correction makes some reflections look like cars. She opens two rain images to see why.

## Clip 4: scene 12

- **Filename:** `ai-19-computer-vision-essentials_L16_screen_4.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Show the updated fitness check with the new numbers
2. Show the outline of the 3-minute demo on one slide

**Narration over this clip (for pacing)**

> She reports this honestly, in her updated fitness check. Her decision. Fit for hourly occupancy estimates, where an error of one vehicle is acceptable. Not fit for billing individual drivers. And rain still needs more training images. Finally, she shows the outline of her three-minute demo.

## Production notes for this lesson

- No new facts to verify (content.md Review Flags: None). The pandas code was run on example data; the voiceover states its numbers exactly as content.md reports them: mean error 0.75 before and 0.46 after; day 0.12 to 0.25; evening 0.62 to 0.25; rain 1.50 to 0.88. These are illustrations, not benchmarks. Prepare test_results.csv from the same example data so the recorded run prints exactly these values.
- Licence and privacy points refer back to L14 and L15 flags: the voiceover repeats only that the Ultralytics YOLO licence must be checked before commercial use, with no legal claims.
- Footage: car park photos are taken from far enough away that people cannot be identified and number plates are not readable. Aigerim Seitkali and the Almaty car park are fictional.
- Screen recording: clean browser profile, no account names or other tabs visible. The spreadsheet can be any free spreadsheet tool; do not show a brand name.
