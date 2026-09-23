# L09 Spotting and Fixing Common Flaws

Course: AI-20 · Module: M3 · Objectives: O5 · Video: 5 min

## Hook
At first glance the image looks perfect. Then a customer points out that the waiter has six fingers and the menu says "Chiken". Small flaws like these can make a whole brand look careless. The good news is that most of them follow patterns, so you can learn to find them quickly.

## Explanation
AI generators learn what things usually look like, not how they work (L01). This is why some flaws appear again and again. Use this five-point **quality checklist** on every image before you publish it:

1. **Hands and faces.** Count fingers. Check that eyes look in the same direction, that teeth and ears look natural, and that hands hold objects in a believable way. Likely cause: hands and faces have many small parts and many possible positions.
2. **Text and logos.** Look for misspelled words, invented letters and shapes that look like a logo but are not. Likely cause: most models do not spell reliably. [VERSION]
3. **Reflections and shadows.** Check that shadows fall away from the light source, and that mirrors and windows reflect the right things. Likely cause: the model does not calculate real light; it imitates patterns.
4. **Repeated patterns and objects.** Look for identical faces in a crowd, copied tiles, or a chair leg that joins the floor twice. Likely cause: the model fills large areas with similar patterns, especially after expanding an image (L07).
5. **Style drift across a set.** Compare images side by side for background, palette, light direction and framing. Likely cause: changes in the style block, or no reference image (L06).

For each flaw, choose one of three fixes:

- **Regenerate** when the flaw is large or in the main subject, or when many things are wrong.
- **Edit the area** with generative fill when the flaw is small and the rest of the image is good.
- **Crop it out** when the flaw is near the edge and cropping does not harm the composition.

For text, there is a fourth fix: **remove the text and add it in Canva** (L08).

**Analogy:** Checking an AI image is like proofreading a letter before you send it. You read slowly, line by line, looking for the kinds of mistakes you know are common. A quick look at the whole page is not enough.

## Worked Example
Layla manages a family restaurant in Amman, Jordan. She generated an image of a table with mezze dishes and a printed menu card for her new lunch offer. She checks it with the checklist:

- **Hands and faces:** a waiter's hand at the edge has four fingers and a thumb that bends the wrong way. Fix: crop it out, because it is at the edge and not needed.
- **Text:** the menu card has warped letters and the word "Lunch" is spelled "Lucnh". Fix: use generative fill to replace the lettering with a plain cream card, then add the real menu text in Canva.
- **Reflections and shadows:** the shadows of the bowls fall to the left, but the window light also comes from the left. Fix: this is a large, noticeable error, so she regenerates with "soft window light from the left, shadows falling to the right" in the prompt.
- **Repeated patterns:** two olive dishes are identical in shape and position. Fix: generative fill on one dish with the prompt "small bowl of pickled vegetables".
- **Style drift:** she compares it with her other two menu images. The new one is cooler in colour. She adds her palette line from her style block and regenerates.

After these fixes, the image is ready for Canva.

## Common Mistake
Many learners check images only on a small phone preview. Flaws such as extra fingers or broken letters are easy to miss at that size. Always view each image at full size and zoom into hands, text and edges. Another mistake is to fix every small flaw by regenerating the whole image. This can create new flaws and waste credits. Choose the smallest fix that solves the problem.

## Key Takeaways
1. Check every image for five common flaws: hands and faces, text and logos, reflections and shadows, repeated patterns, and style drift.
2. Each flaw has a likely cause, and knowing the cause helps you choose the right fix.
3. Use the smallest fix that works: crop, edit the area, or regenerate, and add real text in a design tool.

## Hands-on Exercise
**Task:** Review a set of 6 sample images with the checklist, name each flaw and its likely cause, and choose a fix.
**Tools:** The 6 sample images on the course page, or 6 images from your own earlier exercises; a notes app or spreadsheet.
**Steps:**
1. Open each image at full size.
2. Go through the five checklist points for every image. Zoom into hands, text and edges.
3. Make a table with the columns: image number, flaw, checklist category, likely cause, chosen fix (regenerate, edit, crop, or add text in Canva).
4. Write at least one row for each image. If an image has no flaw, write "none found" and what you checked.
5. Compare all 6 images side by side and add any style drift you notice.
6. Optional: apply your fix to one image and save the before and after versions.
**What good looks like:** A complete table covering all 6 images, with each flaw placed in the correct category, a likely cause that matches the lesson, and a sensible, small fix for each one.
**Time:** about 20 minutes

## Review Flags
- [VERSION] How reliably current models spell text in images changes between model versions and should be checked before recording.
