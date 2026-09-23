# L07 Image-to-Video and Motion Control in Kling

Course: AI-21 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Your keyframe already looks right. Now you only need it to move. With image-to-video, your prompt becomes much shorter, because the picture already answers most of the questions.

## Explanation
In image-to-video, you upload a still image and describe **only the motion**. The subject, setting, lighting and style are already in the image. If you describe them again, the model may try to change the image to match your words.

A good image-to-video prompt answers two questions:

- **What moves in the scene?** Steam rises, leaves move in the wind, a person turns their head.
- **What does the camera do?** A slow dolly-in, a gentle pan, or static.

Kling offers settings that help control motion [VERSION]. Names and options change, but they usually include:

- **Camera movement controls:** preset or adjustable moves, such as zoom, pan or tilt [VERSION].
- **A creativity or relevance setting:** how closely the result follows your prompt and image [VERSION].
- **Duration and quality mode:** longer or higher-quality clips often cost more credits [VERSION].
- **Negative prompt:** things to avoid, such as "distortion, extra fingers, text" [VERSION].

Free credits, daily limits, watermarks and export options in Kling change often [VERSION]. Check what your account has before you start, and plan the shots that matter most first.

**Motion strength.** Small motion is safer. Large movements, such as a person walking across the frame, give the model more chances to distort faces, hands or objects. For product and place shots, a slow camera move is often enough to make a still image feel alive.

**Analogy:** An image-to-video prompt is like instructions to a puppeteer. The puppet is already built and painted. You do not describe its face or clothes again. You only say how it should move: "raise the left arm slowly and turn the head towards the window".

## Worked Example
Pim runs a small street-food tour company in Bangkok, Thailand. She has a keyframe of a market stall at night: coloured lamps, a cook behind a wok and steam in the air. She wants a slow dolly-in. The presenter follows these on-screen steps [VERSION]:

1. Open Kling in a web browser and sign in. Check the credit balance shown on the screen [VERSION].
2. Choose **AI Video**, then the **image-to-video** option [VERSION].
3. Upload the keyframe. Check that it is not cropped in the preview.
4. Write a motion-only prompt:

```text
Slow dolly-in towards the cook. Steam rises gently from the wok. Lamps sway slightly. The cook stirs the wok with steady movements.
```

5. Add a negative prompt: "distorted hands, flicker, text" [VERSION].
6. Choose the duration and mode, and note the credit cost [VERSION].
7. Leave camera controls on default for the first attempt, because the prompt already describes the camera [VERSION].
8. Click **Generate** and wait.
9. Review: the camera moves smoothly, but the cook's hands blur. Pim writes this down.
10. Second attempt: she removes "stirs the wok" and keeps only steam and lamps moving. The hands stay still, and the shot is clean.
11. She downloads the clip, checks the resolution and any watermark [VERSION], and names it "S05_stall_dolly_v2.mp4".

Pim's lesson: less subject movement gave a cleaner result, and the camera movement alone made the shot feel alive.

## Common Mistake
Many learners paste their full text-to-video prompt into image-to-video, including the setting, lighting and style. The model then tries to follow both the image and the text, and the look shifts or the image changes. Describe only what moves and what the camera does.

## Key Takeaways
1. In image-to-video, the image fixes the look, so the prompt describes only subject motion and camera motion.
2. Motion controls, creativity settings, duration and negative prompts help, but their names and costs change, so check the live tool.
3. Small, slow motion is safer than large movement, especially for hands and faces.

## Hands-on Exercise
**Task:** Animate 2 of your keyframes in Kling, one with a camera movement and one with subject movement only.
**Tools:** Kling (free credits) [VERSION]; your keyframes from L05; a log table.
**Steps:**
1. Sign in to Kling and check your credit balance [VERSION].
2. Open image-to-video and upload keyframe A [VERSION].
3. Write a prompt with a camera movement only, such as "slow pan left", and a static subject. Generate.
4. Upload keyframe B. Write a prompt with subject movement only, such as "steam rises, curtains move", and "static camera". Generate.
5. Review each clip twice and log problems.
6. If needed, change one element and generate again. Reduce motion if something distorts.
7. Download both clips, name them by shot number and save the prompts.
**What good looks like:** 2 clips that keep the look of the keyframes, one with clear camera movement and one with only subject movement, plus a short log that explains any changes.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Kling interface details must be checked against the live tool before scripting: menu names, the image-to-video option, camera movement controls, the creativity or relevance setting, negative prompt field, duration and quality modes, free credits and daily limits, watermarks, and export options.
