# L07 Editing with Generative Fill and Expand

Course: AI-20 · Module: M2 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
You have an almost perfect image. The light is right, the colours are right, but there is a coffee cup in the corner that should not be there, and the image is square when your website needs a wide banner. Do you start again? No. You edit only the part that needs to change.

## Explanation
Two editing features save a great deal of time.

**Generative fill** changes a selected area of an image. You paint or draw over part of the picture (this is called a **selection** or **mask**), then either:

- **remove** what is there, and the tool fills the space with background that matches the rest of the image, or
- **add or replace** something by writing a short prompt, such as "a green potted plant", and the tool creates it only inside the selection.

This technique is also called **inpainting**: the tool "paints in" new pixels inside an area while keeping everything outside the area the same.

**Generative expand** makes the canvas larger and fills the new space so that it continues the original image. This is also called **outpainting**. It is the best way to change a square image into a wide 16:9 banner or a tall 9:16 story without stretching or cutting the subject.

In Adobe Firefly, these features appear under names such as Generative Fill and Generative Expand. They use generative credits, and the free tier has a monthly limit. [VERSION]

Tips for good results:

- Select a little more than the object, including its shadow, so no outline is left behind.
- Keep fill prompts short and concrete: "empty wooden shelf" works better than a long description.
- Expanding a lot at once can create repeated or strange details. Check the new edges carefully.

**Analogy:** Generative fill is like a skilled wall painter who repairs one damaged patch and matches the colour so well that you cannot see the repair. Generative expand is like adding a new section to a mural, painted to continue the original scene.

**Safety note:** Only edit images you have the right to use. Do not upload photos of people without their consent, or confidential client material.

## Worked Example
Nino owns a bicycle repair shop in Tbilisi, Georgia. She has a square AI image of her workshop counter, but there is a plastic bottle on the left that looks untidy, and her website needs a 16:9 banner. The presenter follows these steps on screen. Check each name and position in the live tool before recording. [VERSION]

**Part A: Remove an object**
1. Open Adobe Firefly and sign in. [VERSION]
2. Choose the Generative Fill option and upload the square workshop image. [VERSION]
3. Choose the remove tool or brush and paint over the bottle and its shadow. [VERSION]
4. Click the remove or generate button. [VERSION]
5. Compare the results offered, choose the one with the cleanest counter surface, and keep it.

**Part B: Add an object**
1. Select a small empty area on the right of the counter with the insert or add brush. [VERSION]
2. Type a short prompt:

```text
a small green potted plant in a metal pot
```

3. Generate and choose the result that matches the light direction of the image.

**Part C: Expand to 16:9**
1. Open the Generative Expand option with the edited image. [VERSION]
2. Choose the 16:9 aspect ratio from the size or ratio menu. [VERSION]
3. Move the original image inside the new frame. Place it on the right so the new empty area appears on the left, where the website headline will go.
4. Leave the prompt empty so the tool continues the scene, or add "plain workshop wall" for a calmer background. [VERSION]
5. Generate, check the new edges for repeated tools or bent lines, and download the best result. [VERSION]

The final banner shows Nino's tidy counter on the right and a quiet wall on the left, ready for text in Canva.

## Common Mistake
Beginners often select only the object itself, not its shadow or reflection. The object disappears, but a shadow of nothing remains, and the image looks wrong. Another mistake is to regenerate the whole image because of one small problem. This wastes credits and can lose the parts you liked. Edit the area first; regenerate the whole image only when many things are wrong.

## Key Takeaways
1. Generative fill (inpainting) removes, adds or replaces objects inside a selected area while keeping the rest of the image the same.
2. Generative expand (outpainting) extends the canvas to a new aspect ratio, such as square to 16:9, without stretching the subject.
3. Select objects together with their shadows, keep fill prompts short, and check new edges carefully.

## Hands-on Exercise
**Task:** In Adobe Firefly, remove one unwanted object from an image and expand it from square to 16:9.
**Tools:** Adobe Firefly free tier (Generative Fill and Generative Expand); one square image you created earlier in this course. [VERSION]
**Steps:**
1. Choose a square image from your earlier exercises that contains at least one unwanted object.
2. Open it with Generative Fill in Firefly. [VERSION]
3. Select the object and its shadow, then remove it. Choose the cleanest result.
4. Open the edited image with Generative Expand and choose 16:9. [VERSION]
5. Place the original image to one side so there is space for a headline.
6. Generate, choose the best result and check the new edges.
7. Save the before image and the after image side by side.
**What good looks like:** The object is gone with no leftover shadow or outline, the 16:9 image continues the original scene naturally, and there is a clear empty area for text. No repeated or distorted details appear in the expanded area.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Adobe Firefly feature names (Generative Fill, Generative Expand), remove and insert brushes, button labels, aspect-ratio menus, whether the expand prompt can be left empty, and free-tier generative credits must be checked against the live tool before scripting.
