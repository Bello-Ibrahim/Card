# L05 Keyframes: From Still Image to Motion

Course: AI-21 · Module: M1 · Objectives: O3 · Video: 5 min

## Hook
You generate a beautiful clip, and then the next clip has different colours, a different room and a different person. Many creators solve this before they generate any motion at all. They start with still images.

## Explanation
A **keyframe** is a still image that shows exactly how a shot should look. You create it with an image generator, check it, and only then add motion with an image-to-video tool.

Why start from a still?

- **Control:** you can fix the composition, colours and characters before motion is added.
- **Cost:** images are usually quicker and cheaper to generate than video [VERSION], so you can try many versions.
- **Consistency:** when all keyframes share one look, the clips made from them usually share it too.

**The style block.** The key to consistent keyframes is a **style block**: a fixed piece of text that you paste, unchanged, at the end of every image prompt. It describes the look, not the content. For example:

```text
Style: warm cinematic photography, golden hour light, terracotta and teal colour palette, shallow depth of field, soft film grain, 16:9.
```

The first part of each prompt changes (the subject, action and setting). The style block never changes.

**Characters.** If a person appears in more than one shot, write a fixed **character description** and reuse it word for word: age range, hair, clothing and one or two clear details. Do not describe the same person in different words each time. Use fictional characters only; do not create keyframes of real, identifiable people.

**Aspect ratio.** Generate keyframes in the aspect ratio of your final video, usually 16:9 for horizontal or 9:16 for vertical. Changing it later means cropping.

Use any image generator you know from the previous course. Many have free tiers [VERSION].

**Analogy:** Keyframes are like the costume and set photos a film team takes before shooting. Everyone agrees on the look from the photos, so on the day of filming nobody needs to guess what the room or the actor should look like.

## Worked Example
Youssef is a marketing assistant at a hypothetical riad hotel in Marrakech, Morocco. He needs 3 shots that feel like one place.

His style block:

```text
Style: warm editorial travel photography, late afternoon sun, terracotta, cream and deep green palette, soft shadows, gentle film grain, 16:9.
```

His character description, used in keyframe 3:

```text
A woman in her thirties with curly black hair tied back, wearing a loose white linen shirt and a thin gold bracelet.
```

His three prompts:

```text
Keyframe 1: Wide view of a tiled courtyard with a small fountain in the centre, orange trees in pots and carved wooden doors. [style block]
Keyframe 2: Close-up of mint tea being poured from a silver teapot into a small decorated glass on a brass tray. [style block]
Keyframe 3: Medium shot of [character description] reading a book on a rooftop terrace with low cushions, the city in soft focus behind her. [style block]
```

He generates 4 versions of each keyframe and chooses the best one. Keyframe 2 has a warped teapot handle, so he regenerates it. He puts the 3 chosen images side by side. The colours and light match, so they are ready for Kling in L07.

## Common Mistake
Many learners change the style words a little each time: "warm light" in one prompt, "sunset glow" in the next, "golden tones" in the third. Each change moves the look. Copy and paste the exact same style block every time. If you want to change the style, change it for every keyframe together.

## Key Takeaways
1. A keyframe is a still image that fixes the look of a shot before motion is added.
2. A style block pasted unchanged into every prompt, and a fixed character description, are the main tools for consistency.
3. Generate keyframes in your final aspect ratio, check them side by side, and use fictional people only.

## Hands-on Exercise
**Task:** Generate 3 keyframe images for your shot list that share the same style, colour palette and characters.
**Tools:** Any free image generator you used in the previous course [VERSION]; your shot list and prompts.
**Steps:**
1. Choose 3 shots from your shot list that you plan to animate.
2. Write one style block with lighting, colour palette, texture and aspect ratio.
3. If a character appears, write one fixed character description.
4. Write 3 prompts: content first, then the style block pasted unchanged.
5. Generate 2 to 4 versions of each and choose the best.
6. Place the 3 chosen images side by side and check colours, light and the character.
7. Regenerate any image that does not match. Save the final images and prompts.
**What good looks like:** 3 images in the same aspect ratio that clearly belong to the same video, with the same palette and light, and the same character where one appears.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Relative cost and speed of image versus video generation, and free-tier availability of image generators, must be checked against current tools before scripting.
