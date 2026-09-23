# L03 Storyboards and Shot Lists

Course: AI-21 · Module: M1 · Objectives: O2 · Video: 5 min

## Hook
You have a script. Now imagine sending it to a video model line by line. What should the first shot look like? How long should it last? Where is the camera? If you cannot answer these questions, the model will answer them for you, and you may not like its answers.

## Explanation
A **storyboard** is a row of rough pictures that shows the video shot by shot. A **shot list** is the same plan as a table. For AI video, the shot list is the more useful of the two, because every row becomes a prompt later.

A simple shot list has these columns:

| # | Time | Duration | Shot type | What the viewer sees | Narration at the same time | Source |
|---|---|---|---|---|---|---|

- **Time:** where the shot starts in the video, for example 0:08.
- **Duration:** how long the shot stays on screen. For short-form video, 3 to 8 seconds is common. Generated clips are often short [VERSION], so a shot longer than one clip needs a plan, such as two clips or a slower edit.
- **Shot type:** wide, medium or close-up. You learn these in L04.
- **What the viewer sees:** one line, specific enough to become a prompt.
- **Narration:** the words from your script that play during this shot.
- **Source:** text-to-video, image-to-video, avatar, your own footage, or a simple graphic.

**How to build it.** Take your two-column script. Split it where the picture should change, which is usually every one or two sentences. Give each piece a duration by reading it aloud. Check that the durations add up to your target length.

**Rhythm.** Vary shot types. Three wide shots in a row feel slow; a wide shot followed by a close-up feels like the story is moving. Put your strongest image in the hook.

**Storyboards still help.** Quick stick-figure sketches, or a few rough images, help you see whether the shots work together before you spend credits.

**Analogy:** A shot list is like a recipe card. The script tells you what dish you are cooking. The shot list tells you each step, in order, with the time each step takes. A cook who works without a recipe can still make something, but it is hard to make it the same way twice or to find out what went wrong.

## Worked Example
Valeria is a freelance creator in Oaxaca, Mexico. A small coffee brand has asked her for a 45-second video. Here are her first 8 shots:

| # | Time | Dur. | Shot type | Viewer sees | Narration | Source |
|---|---|---|---|---|---|---|
| 1 | 0:00 | 4 s | Wide | Misty mountain slopes with coffee plants at sunrise | "Our coffee starts in the clouds." | Text-to-video |
| 2 | 0:04 | 5 s | Close-up | Hands picking red coffee cherries | "Every cherry is picked by hand." | Text-to-video |
| 3 | 0:09 | 6 s | Medium | Beans drying on a patio, a rake moving through them | "Then dried slowly in the sun." | Text-to-video |
| 4 | 0:15 | 5 s | Close-up | Beans turning brown in a roaster | "We roast in small batches." | Image-to-video |
| 5 | 0:20 | 6 s | Medium | The brand's bag on a kitchen table, morning light | "So it arrives fresh at your door." | Image-to-video from product photo |
| 6 | 0:26 | 7 s | Close-up | Coffee pouring into a clay cup | "Rich, smooth and full of flavour." | Image-to-video |
| 7 | 0:33 | 4 s | Medium | Two friends smiling over coffee | "Made to share." | Text-to-video |
| 8 | 0:37 | 8 s | Graphic | Logo and website address | "Order today at our website." | Editor text |

The total is 45 seconds. Notice that each "Viewer sees" line names a subject, an action and a setting. That makes L04 much easier. Notice also that shot 8 needs no AI at all. Text generated inside video is often unreadable, so logos and web addresses are added in the editor.

## Common Mistake
Many learners write vague rows such as "nice coffee shot" or "happy people". These rows give you nothing to prompt with, and you end up generating many random clips and hoping one fits. Make every row specific: who or what, doing what, where. If you cannot picture the shot, the model cannot either.

## Key Takeaways
1. A shot list turns your script into rows with time, duration, shot type, what the viewer sees, narration and source.
2. Durations must add up to your target length, and most short-form shots last about 3 to 8 seconds.
3. Specific rows become good prompts later, and text such as logos is best added in the editor.

## Hands-on Exercise
**Task:** Turn your script into a shot list of 8 to 12 shots with duration, shot type and a one-line description for each.
**Tools:** A spreadsheet, a document table or paper; your script from L02; a phone timer.
**Steps:**
1. Create a table with the seven columns from this lesson.
2. Split your script where the picture should change. Put each piece of narration in its own row.
3. Read each row aloud and write its duration.
4. Write one specific line for "What the viewer sees": subject, action and setting.
5. Choose a shot type and a source for each row.
6. Add up the durations. Adjust until they match your script length.
7. Check the rhythm: do not use the same shot type more than twice in a row.
**What good looks like:** 8 to 12 rows, each with a specific description that someone else could picture, durations that add up to your target, varied shot types, and text-heavy shots marked for the editor.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Typical maximum clip lengths of video models must be checked against the live tools before scripting.
