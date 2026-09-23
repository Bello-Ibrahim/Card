# L06 Guiding Image Generators

Course: AI-02 · Module: M2 · Objectives: O3, O4 · Video: 5 min (screen demo)

## Hook
You type "bread" into an image generator and get a plain loaf on a white table. It is not wrong, but it is not what you imagined. The model filled every gap with the most typical choice. How do you give it enough guidance to make the picture you actually need?

## Explanation
In L05 you learned that a diffusion model starts from random noise and that the text prompt steers every step. Anything you do not describe, the model fills in with typical patterns from training. So a better prompt does not use "magic words". It simply gives **clearer guidance** on the details that matter to you.

A useful checklist has six parts:

- **Subject:** what is in the image. Be specific: "round loaves and small rolls of brown bread", not "bread".
- **Setting:** where it is. "On a wooden table at an outdoor market stall."
- **Style:** how it should look. "Realistic photograph", "flat illustration" or "watercolour painting".
- **Composition:** how the image is arranged. "Close-up", "wide view", "subject in the centre", "empty space at the top for a title".
- **Lighting:** "soft morning sunlight", "bright studio light", "warm evening light".
- **Aspect ratio:** the shape of the image, such as square, tall (portrait) or wide (landscape). Many tools set this with a menu or button, not in the prompt. [VERSION]

Some generators also offer settings such as the number of images, a style preset or a "negative prompt" (things to avoid). Settings differ between tools. [VERSION]

Two further tips help. First, **change one or two things at a time**, so you can see which change caused which effect. Second, **do not ask for text inside the image** if you need exact words. Image models often produce wrong letters. It is usually better to add the text later in a design tool.

**Analogy:** Prompting an image generator is like briefing a photographer you cannot speak to again. If you only say "take a photo of bread", they will choose the place, the angle and the light themselves. If you give a clear brief with the subject, the place, the style and the light, the result is much closer to what you had in mind.

## Worked Example
Wanjiru runs a small bakery in Nairobi, Kenya. She wants a poster image of fresh bread on a market stall to advertise her weekend stall. This is a hypothetical case. A presenter can follow these steps on screen in a free image generator of their choice. [VERSION]

1. Open the image generator and choose a **portrait** (tall) aspect ratio, because the poster is tall. [VERSION]
2. Type the **first version**: "bread on a market stall". Generate it. The result shows a generic loaf on a grey table in a dark setting. It does not look fresh, local or inviting.
3. Write the **second version**, adding subject, setting and lighting: "Fresh round loaves and small brown bread rolls in woven baskets on a wooden market stall, soft morning sunlight." Generate it. The bread looks fresh and warm, but the image is full to the edges, with no space for the poster title.
4. Write the **third version**, adding style and composition: "Realistic photograph of fresh round loaves and small brown bread rolls in woven baskets on a wooden market stall, soft morning sunlight, close-up, baskets in the lower half, plain light sky in the upper half for a title." Generate it.
5. Compare the three results side by side and note what each change improved.

The third image has empty sky at the top. Wanjiru adds the bakery name and opening hours later in a free design tool, so the letters are correct. She checks the image carefully for strange details before printing, and she checks the tool's terms to confirm she may use the image in advertising. [VERSION]

## Common Mistake
Many learners write longer and longer prompts full of words like "amazing, ultra-detailed, masterpiece", hoping for better quality. These words rarely help much, and very long prompts can confuse the model about what matters most. The correction is to describe the six parts clearly, change one or two things at a time, and use the tool's settings (such as aspect ratio) instead of forcing everything into the text.

## Key Takeaways
1. A diffusion model fills every gap with typical patterns, so a clear prompt gives better guidance about the details that matter to you.
2. Describe subject, setting, style, composition and lighting, and choose the aspect ratio with the tool's settings when possible.
3. Improve a prompt in small steps and note what each change does; add exact text in a design tool, not in the image prompt.

## Hands-on Exercise
**Task:** Write a first, second and third version of an image prompt for a hypothetical business of your choice, generate each one, and note what each change improved.
**Tools:** A free image generator of your choice [VERSION]; a notes app. Check the course page for current suggestions and free limits.
**Steps:**
1. Choose a hypothetical business, such as a bicycle repair shop, a tea stall or a language school, and decide what the image is for (poster, website banner or social media post).
2. Choose the aspect ratio that suits that use. [VERSION]
3. Write version 1 in five words or fewer. Generate it and save the image.
4. Write version 2 by adding subject details, setting and lighting. Generate and save.
5. Write version 3 by adding style and composition. Generate and save.
6. Under each image, write one sentence about what the change improved and one thing that is still wrong.
7. Do not include real people's names, faces or logos of real brands in your prompts.
**What good looks like:** Three saved images with their exact prompts, clear differences between versions, and short notes that link each improvement to a part of the checklist (for example "adding 'close-up' made the product fill the frame").
**Time:** about 25 minutes

## Review Flags
- [VERSION] "Free image generator" is not named on purpose. A reviewer should choose specific free tools, check their current free limits, how aspect ratio, number of images, style presets and negative prompts are set, and the licence terms for using generated images in advertising.
- [VERSION] Confirm the screen-demo steps (choosing aspect ratio, generating, comparing results side by side) against the chosen tool before recording.
