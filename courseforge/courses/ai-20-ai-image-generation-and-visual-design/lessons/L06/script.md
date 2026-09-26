# L06 Keeping Images Consistent | Presenter Script

Course: AI-20 · Video: 5 min · Words: 736

## Hook
One good AI image is easy. Four images that look like they come from the same photo shoot are much harder. Every new generation starts from new random noise, so things drift. Today, you get the tools to keep a set together.

## Explain
Style drift is when images that should belong together slowly become different. The light changes direction, the palette shifts, or the background moves from a studio to a kitchen. There are four main ways to control it.

The first and most important is a fixed style block. This is a paragraph that describes style, lighting, colour and framing. You paste it, word for word, into every prompt in the set. Only the subject line changes. It works in every tool.

The second is a reference image. You upload an image, often your best result so far, and ask the tool to match its look. In Gemini, you can attach an image to your message and describe what to keep. The third is Firefly's reference settings, where an image guides the style, or the layout and shapes.

The fourth is the seed. Where a tool lets you see and reuse a seed, it can keep a similar starting point. But many consumer tools hide seeds, so do not depend on this method.

A style block is like a uniform for a sports team. Each player is different, but the same colours and badge make everyone look like one team. The reference image is the photo of the uniform you show to a new player.

One safety note. Upload only images you own or have permission to use as references. No client files, and no photos of people without consent.

## Demonstrate
Let's help Min-seo. She runs a skincare start-up in Seoul, South Korea, and needs four product images for her website. Her style block is on screen. A pale peach background, one soft light from the upper left, a close-up at eye level, a peach, white and sage green palette, and a calm, clean mood.

I open Gemini and start a new chat. I paste the first subject, a frosted glass serum bottle with a white dropper, then the style block, and send. I download the best result. This is our hero image.

For the next image, I stay in the same chat and attach the hero image as a reference. I ask for a new image in exactly the same style, background and lighting, with a new subject, a white cream jar with a wooden lid. And I paste the style block again.

I repeat this for a tall sage green toner bottle, and a small tube of lip balm. Each time, only the subject changes.

Now the same idea in Adobe Firefly. I choose text to image and paste the subject line and the style block. Then I find the style reference setting and upload the hero image.

If there is a strength control, I move it. Watch how a stronger reference pulls the result closer to the hero image. I generate, then repeat with the next subject, keeping the reference and the style block the same.

Finally, the review. I place the four images in a row and check the background colour, the light direction, the shadow position and the framing. The lip balm image has a stronger shadow than the others.

So I add very soft, faint shadow to that prompt only, and regenerate that one image.

The most common mistake is to rewrite the style block a little each time, like soft light for one image and gentle daylight for the next. Small word changes create visible drift. Copy and paste the block exactly, and check each new image as you go.

## Recap
Let's recap. First, a fixed style block, pasted word for word into every prompt, is the most reliable way to keep a set consistent. Second, reference images and reference settings help you match a chosen hero image. Third, check each new image against the hero for background, light, palette and framing, and fix drift one image at a time.

## CTA
Now it is your turn. In the exercise below, you will build your own style block and use it to create four images that look like one set. Save the block, because you will use it in the capstone. It takes about twenty-five minutes. Next, we look at editing with generative fill and expand. See you there.

## Thumbnail
Headline: Four Images, One Look
Image: Navy background, four generated skincare product images in a row on the same pale peach background, with a thin teal line joining them; headline in teal Inter Bold.

## Production Notes
- [VERSION] Record the screen demo only after checking the live tools: the Gemini image attach or upload option, Adobe Firefly style reference and structure or composition reference settings, the reference strength control, seed visibility in each tool, and free-tier limits all change often. Update the screen_steps if menu names differ.
- [VERSION] Seeds: the voiceover says only that many consumer tools hide seeds and that learners should not depend on them. Do not show a seed control unless the live tool has one.
- Scenes 14 and 15 (Review): the demo shows the lip balm image with a stronger shadow than the others. If the recorded result has a different drift, name the real drift on screen and adjust the one fix line, keeping the method the same.
- Use a demo Google account and a demo Adobe account with no personal data visible. Blur account names, email addresses and credit balances.
- Only the team's own generated hero image is uploaded as a reference. No client files, real product packaging, logos or photos of people.
- Min-seo and her Seoul skincare start-up are fictional; no real brand names or marks on the products.
