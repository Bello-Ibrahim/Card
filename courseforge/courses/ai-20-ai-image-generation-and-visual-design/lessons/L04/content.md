# L04 Composition, Lighting and Colour Words

Course: AI-20 · Module: M1 · Objectives: O2, O3 · Video: 5 min

## Hook
Photographers can make the same street look calm, exciting or mysterious without moving a single object. They do it with the camera angle, the light and the colours. You can do the same with a few well-chosen words.

## Explanation
In L02 you met the prompt formula. This lesson focuses on three of its parts: **composition**, **lighting** and **colour**. The best words for these come from photography and design, because image models learned from many photos and pictures described with this language.

**Composition words** control framing and viewpoint:

- **Close-up:** the subject fills most of the frame. Good for products and details.
- **Medium shot:** the subject with some surroundings.
- **Wide shot:** the whole scene, with the subject small in the frame. Good for places.
- **Eye level:** the camera is at the height of a person's eyes. It feels natural.
- **Low angle:** the camera looks up. The subject feels large and strong.
- **Top-down (flat lay):** the camera looks straight down. Popular for food and products.
- **Empty space on the left/right:** leaves room for text you will add later.

**Lighting words** control mood:

- **Soft window light:** gentle, natural, few hard shadows.
- **Golden hour:** warm, low sunlight just after sunrise or before sunset.
- **Overcast daylight:** even and cool, with very soft shadows.
- **High contrast:** strong difference between bright and dark areas. Dramatic.
- **Backlit:** light behind the subject, often with a bright outline.

**Colour words** control the palette:

- **Limited colour palette of** two or three named colours keeps an image simple and on brand.
- **Muted** or **pastel** colours feel calm; **saturated** colours feel energetic.
- **Warm** tones (orange, red, yellow) and **cool** tones (blue, green) change the feeling of the whole image.

**Using brand colours:** most generators do not follow hex codes such as #0B5C8A reliably. [VERSION] Describe the colour in words instead: "deep ocean blue", "soft sand beige". Then correct exact colours later in a design tool, as you will do in L08.

**Analogy:** Composition, lighting and colour are like the camera, the lamps and the paint in a small film studio. The actors and the set can stay the same, but moving the camera, changing the lamps or repainting the wall creates a different scene each time.

## Worked Example
Haruto works for a small travel agency in Kyoto, Japan. He needs images of a quiet garden path for three different tour packages. He keeps the subject and setting fixed and changes only the lighting:

```text
A narrow stone path through a quiet garden with maple trees and a small wooden gate,
wide shot at eye level, empty space on the right,
[LIGHTING], limited colour palette of green, stone grey and deep red
```

He replaces `[LIGHTING]` three times:

1. **"soft overcast morning light"** gives a calm, even image for a "relaxing mornings" tour.
2. **"golden hour sunlight through the leaves"** gives warm light and long shadows for an "evening walks" tour.
3. **"lantern light at night, high contrast"** gives a dark, dramatic image for a "night lanterns" tour.

Because only one part changed, Haruto can see exactly what each lighting phrase does. The three images also look related, because the subject, composition and palette stayed the same. He notices that the empty space on the right is useful for the tour name and price.

## Common Mistake
Many learners mix contradictory terms, such as "top-down view, low angle" or "golden hour, overcast". The model cannot show both, so it picks one or produces a confused image. Choose one term per category. Another mistake is to trust that a hex code in the prompt gives an exact brand colour. Describe colours in words and check them afterwards.

## Key Takeaways
1. Words from photography, such as close-up, top-down, golden hour and high contrast, give precise control over composition and lighting.
2. Changing only one part of a prompt at a time shows you what each word does.
3. Describe brand colours in words and a limited palette; fix exact colour values later in a design tool.

## Hands-on Exercise
**Task:** Generate one scene in 3 variations that change only camera angle, lighting or colour, and label what each word changed.
**Tools:** Gemini (free) or Google AI Studio, or Adobe Firefly free tier; a notes app or slide. [VERSION]
**Steps:**
1. Choose a scene for a small business, for example a market stall, a hotel room or a bicycle repair shop.
2. Write a base prompt with subject, setting, style, composition, lighting and colour.
3. Choose one category to change: camera angle, lighting or colour.
4. Create 3 versions of the prompt that change only that category. Keep every other word the same.
5. Generate all 3 versions in the same tool.
6. Place the results side by side and label each one with the words you changed.
7. Write one sentence per image about how the change affects the mood or usefulness of the image.
**What good looks like:** Three images of the same scene with a clear, visible difference in one category only, labels showing the exact words used, and short notes linking each change to a business purpose.
**Time:** about 20 minutes

## Review Flags
- [VERSION] Whether current Gemini, Google AI Studio and Adobe Firefly models follow hex colour codes in prompts must be tested before recording; free-tier limits must also be checked.
