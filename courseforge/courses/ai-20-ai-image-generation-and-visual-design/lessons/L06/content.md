# L06 Keeping Images Consistent

Course: AI-20 · Module: M2 · Objectives: O3, O5 · Video: 5 min (screen demo)

## Hook
One good AI image is easy. Four images that look like they come from the same photo shoot are much harder. Every new generation starts from new random noise, so colours, light and mood tend to drift. This lesson gives you the tools to keep a set together.

## Explanation
**Style drift** is when images that should belong together slowly become different: the light changes direction, the palette shifts, or the background changes from studio to kitchen. There are four main ways to control it.

1. **A fixed style block.** A style block is a paragraph that describes style, lighting, colour and framing. You paste it, word for word, into every prompt in the set. Only the subject line changes. This is the most important method, and it works in every tool.
2. **Reference images.** You upload an image, often your best result so far, and ask the tool to match its look. In Gemini you can attach an image to your message and describe what to keep. [VERSION]
3. **Style or structure reference settings.** Adobe Firefly offers settings where you upload an image to guide the style, or to guide the layout and shapes. The names and positions of these settings change. [VERSION]
4. **Seeds.** Where a tool lets you see and reuse a seed, reusing it with a similar prompt can keep a similar starting point. Many consumer tools hide seeds, so do not depend on this method. [VERSION]

**Analogy:** A style block is like a uniform for a sports team. Each player is different, but the same colours, cut and badge make everyone look like one team. The reference image is the photo of the uniform you show to a new player.

**Safety note:** Upload only images you own or have permission to use as references. Do not upload client files or photos of people without consent.

## Worked Example
Min-seo runs a skincare start-up in Seoul, South Korea. She needs 4 product images for her website that look like one set. The presenter follows these steps on screen. Check each menu name in the live tools before recording. [VERSION]

First she writes a style block:

```text
Style block: product photograph on a seamless pale peach background,
single soft light from the upper left with a gentle shadow to the lower right,
close-up at eye level, product centred with generous empty space around it,
limited palette of pale peach, white and soft sage green,
calm, clean and fresh mood
```

**Part A: Gemini with a style block and reference**
1. Open Gemini and start a new chat. [VERSION]
2. Paste: "A frosted glass serum bottle with a white dropper." Then paste the style block. Send.
3. Download the best result. This is the "hero" image.
4. Start the next image in the same chat: attach the hero image as a reference using the attach or upload option. [VERSION]
5. Write: "Create a new image in exactly the same style, background and lighting as this reference. Subject: a white cream jar with a wooden lid." Paste the style block again. Send.
6. Repeat step 5 for "a tall sage-green toner bottle" and "a small tube of lip balm".

**Part B: Adobe Firefly with a style reference**
1. Open Adobe Firefly and choose text to image. [VERSION]
2. Paste the subject line and the style block.
3. Find the style reference setting and upload the hero image. [VERSION]
4. Adjust the strength of the reference, if the setting exists, and point out how the result changes. [VERSION]
5. Generate, then repeat with the next subject, keeping the reference and style block the same.

**Part C: Review.** Place the 4 images in a row. Check the background colour, light direction, shadow position and framing. In this demonstration, the lip balm image has a stronger shadow than the others. Min-seo adds "very soft, faint shadow" to that prompt only and regenerates it.

## Common Mistake
The most common mistake is to rewrite the style block a little for each image: "soft light" for one, "gentle daylight" for the next. Small word changes create visible drift. Copy and paste the block exactly. A second mistake is to generate all images first and check consistency only at the end. Check each new image against the hero image as you go, so you fix drift early.

## Key Takeaways
1. A fixed style block, pasted word for word into every prompt, is the most reliable way to keep a set consistent.
2. Reference images and style or structure reference settings help match the look of a chosen "hero" image.
3. Check each new image against the hero image for background, light direction, palette and framing, and fix drift one image at a time.

## Hands-on Exercise
**Task:** Build a reusable "style block" and use it to generate 4 images of different subjects that look like one set.
**Tools:** Gemini (free) or Google AI Studio; Adobe Firefly free tier for the style reference option; a notes app. [VERSION]
**Steps:**
1. Choose a small real or fictional business and 4 different subjects it could show, such as 4 products or 4 scenes.
2. Write a style block with background, lighting, framing, palette and mood. Save it in your notes.
3. Generate the first subject with the style block and choose your best result as the hero image.
4. Generate the other 3 subjects with the exact same style block. Use the hero image as a reference in Gemini, or as a style reference in Firefly, if the option is available. [VERSION]
5. Place all 4 images in a row and check background, light direction, palette and framing.
6. Regenerate any image that drifts, changing only the words needed to fix it.
7. Save your style block for the capstone in L11.
**What good looks like:** Four images of different subjects that clearly belong to one set, a saved style block, and a short note of any image you regenerated and which words fixed the drift.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Gemini image-attachment options, Adobe Firefly style reference and structure or composition reference settings, reference strength controls, seed visibility in each tool, and free-tier limits change often and must be checked against the live tools before scripting.
