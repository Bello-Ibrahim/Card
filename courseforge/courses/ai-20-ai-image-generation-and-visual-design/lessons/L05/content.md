# L05 Describing a Style Without Copying Artists

Course: AI-20 · Module: M2 · Objectives: O2, O6 · Video: 5 min

## Hook
Many people get a strong look by adding "in the style of" and the name of a famous living artist. It seems quick. But it borrows someone else's life's work without asking. There is a better way, and it also gives you more control.

## Explanation
A **style** is the set of visual qualities that make images look like they belong together. You can describe almost any style with five attributes:

1. **Medium:** what the image seems to be made with. "Gouache painting", "linocut print", "3D clay render", "35mm film photograph", "flat vector illustration".
2. **Texture and line:** the surface and edges. "Rough paper grain", "clean thin outlines", "visible brush strokes", "smooth gradients".
3. **Era or influence:** a period or general tradition, not a person. "1970s travel poster", "mid-century modern", "early digital pixel art".
4. **Colour:** the palette and its strength. "Limited palette of coral, teal and off-white, slightly faded".
5. **Mood:** the feeling. "Energetic and playful", "calm and quiet", "bold and confident".

Add composition and lighting words from L04 and you have a complete, reusable style description.

**Why not name living artists?** There are three reasons. First, an artist's style is linked to their income and reputation, and many artists have not agreed to have their work imitated by AI tools. Second, the legal position on imitating a named artist's style is unclear and differs between countries, so it can create risk for your business or client. [VERIFY] [REGION] Third, some tools block or change prompts that include artists' names. [VERSION] In this course we never name living artists in prompts. Describing attributes is also more useful: you understand exactly why the style works, and you can adjust each part.

**Analogy:** Describing a style by its attributes is like describing a dish by its ingredients and flavours instead of naming a famous chef. "Slow-cooked beans with smoked meat, garlic and orange" tells a cook what to make. "Cook it like Chef X" only works if you copy that chef, and it does not teach you anything about the dish.

## Worked Example
Renata runs a small, fictional sportswear brand in Recife, Brazil. She wants her campaign images to feel active, warm and local. Instead of naming an artist, she writes a five-attribute style description:

```text
Style: flat vector illustration with bold geometric shapes (medium),
clean edges and a light paper grain (texture),
inspired by 1980s sports posters (era),
limited palette of sunset orange, deep teal and white (colour),
energetic and optimistic (mood)
```

She tests it on two different subjects by adding the style to each prompt:

```text
A runner on a beach path at sunrise, low angle, empty space at the top.
[Style description]
```

```text
A pair of running shoes on a boardwalk, close-up, seen from the side.
[Style description]
```

Both images share the orange-teal-white palette, the bold shapes and the poster feeling, even though one shows a person and the other shows a product. Renata now has a style that belongs to her brand, and she can explain every part of it to her team.

She notices one problem: in the shoe image the paper grain is almost invisible. She changes "a light paper grain" to "a clearly visible paper grain", generates again, and the two images match more closely.

## Common Mistake
Some learners replace a living artist's name with an art movement word and think the style is now fully described. "Pop art" or "impressionist" alone still leaves the model to guess medium, colour and mood. Use a movement or era only as one of the five attributes. Another mistake is to include a real brand's name or a character from a film or game to get a certain look. Avoid logos, brand names and copyrighted characters in your prompts.

## Key Takeaways
1. Describe a style with five attributes: medium, texture, era, colour and mood.
2. Do not name living artists in prompts; it raises ethical and legal questions, and attribute descriptions give you more control.
3. Test a style description on different subjects to check that it creates a consistent look.

## Hands-on Exercise
**Task:** Write a 5-attribute style description for a fictional sportswear brand from Brazil, and test it on 2 different subjects.
**Tools:** Gemini (free) or Google AI Studio, or Adobe Firefly free tier; a notes app. [VERSION]
**Steps:**
1. Invent a name and a short personality for the brand, for example "a running brand for city runners in Belo Horizonte".
2. Write one line for each attribute: medium, texture, era, colour and mood. Do not use the name of any artist, brand or character.
3. Join the five lines into one style description.
4. Write two prompts with different subjects, such as a person training and a product, each followed by the style description.
5. Generate both images in the same tool.
6. Compare them. Write which attributes appear in both, and change one word if any attribute is missing. Generate again.
**What good looks like:** A clear five-attribute style description with no names of artists, brands or characters, and two images of different subjects that share a visible palette, medium and mood. Notes explain one improvement made after the first test.
**Time:** about 20 minutes

## Review Flags
- [VERIFY] [REGION] The legal position on imitating a named artist's style is unclear and differs by country; the lesson states no legal conclusion and should be reviewed.
- [VERSION] Whether current tools block or change prompts that contain artists' names must be checked; free-tier limits must also be checked.
- Judgement call from the curriculum: style is taught through visual attributes only, and the course never names living artists to imitate.
