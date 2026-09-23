# L08 Logo Exploration: AI as Sketchbook, Not Final Art

Course: AI-23 · Module: M2 · Objectives: O3, O6 · Video: 5 min

## Hook
An image generator gives you a logo that looks finished. It has clean edges, nice colours and a clever shape. Why would a professional designer still redraw it from the beginning?

## Explanation
Image generators are useful in the early part of logo design: exploring many shapes, metaphors and compositions quickly. They are a poor choice for the final mark. Treat them as a **sketchbook**, not as final art.

**How to explore.** Prompt with the idea and the form, not with existing logos:

- **Concept:** "a coffee bean that is also a sun rising over hills".
- **Form:** "simple flat vector symbol, two colours, thick even lines, no text, white background".
- **Variation:** change one variable at a time: geometric or organic, open or closed shape, symmetric or not.

Generate many concepts, then choose one direction based on the brief, not on which image looks most polished.

**Why raw AI logos are risky.**

1. **Similarity to existing marks.** Generators learn from very large image collections that include many logos. A result can look close to an existing mark without you knowing. Do a reverse image search and a visual search of logo collections, and get official trademark checks before launch, as with names in L06. [REGION]
2. **Weak scalability.** Generated images are pixels, not vectors. Edges are often uneven, details disappear at small sizes and shapes do not follow a grid. A logo must work at favicon size and on a building.
3. **Uncertain copyright protection.** In many places, copyright law is unclear about works made mostly by AI, and some authorities have said that work without enough human authorship may not be protected. [VERIFY] Rules differ by country and are still developing. [REGION] If the client cannot own their logo, a competitor might be able to use something very similar.

**The redraw practice.** Choose the direction, then redraw it yourself in Figma as a clean vector: build it on a grid, make your own decisions about proportions, curves and weight, and simplify it until it works at small sizes. The result is better design, and it is clearly your own creative work. But redrawing is good practice, not a legal guarantee. It does not replace trademark checks or legal advice about ownership. [VERIFY]

**Analogy:** An AI logo concept is like a photo reference for a painter. The photo helps you see the idea, but the painting is made by your own decisions with the brush. Copying the photo line by line is tracing; interpreting it is design.

## Worked Example
Selam Tesfaye is a brand designer in Addis Ababa, Ethiopia. Her hypothetical client is a small coffee roaster that sells to cafés. The brief asks for a mark that suggests origin, warmth and care.

She generates 10 concepts with prompts such as: "simple flat vector symbol, a coffee cherry combined with a rising sun, two colours, thick even lines, no text, white background." She varies geometric and organic forms.

She puts the 10 concepts in Figma and scores each against the brief: meaning, simplicity and difference from typical coffee logos. She picks a direction where the sun's rays become the lines of a coffee bean.

A reverse image search finds no close matches, but she notes: "Visual search is not a trademark clearance." She then redraws the mark in Figma:

1. She sets up a 48-unit grid and draws the bean with the Ellipse and Pen tools.
2. She makes the rays equal width, with the same gaps, so they stay clear at small sizes.
3. She removes one ray that disappears at 16 pixels.
4. She converts the outlines into one clean vector shape and tests it at 16, 64 and 512 pixels.

Her logo file includes a note: "Concept explored with an image generator; final mark redrawn by hand. Trademark search and ownership advice recommended before launch." [VERIFY]

## Common Mistake
Many designers use an auto-trace or auto-vectorise function on an AI image and call it redrawn. That keeps the AI's uneven shapes and does not add real design decisions. A second mistake is to believe that redrawing makes the logo legally safe. It improves quality and shows authorship, but ownership and similarity questions still need proper checks.

## Key Takeaways
1. Use image generators as a sketchbook for fast logo exploration, prompting with concept and form, not existing logos.
2. Raw AI logos are risky: they may resemble existing marks, they scale poorly, and their copyright protection is uncertain and differs by country.
3. Redraw the chosen direction by hand as a clean vector in Figma as good practice, but still recommend trademark and legal checks.

## Hands-on Exercise
**Task:** Generate 10 logo concepts, pick one direction, and redraw it as a vector mark in Figma at 3 sizes.
**Tools:** A free image generator [VERSION]; Figma (free plan); a free reverse image search.
**Steps:**
1. Write a concept and form prompt from your brief. Do not mention any existing logo or brand.
2. Generate 10 concepts, varying one variable at a time.
3. Place them in Figma and score each for meaning, simplicity and difference.
4. Pick one direction and run a reverse image search. Note the result.
5. Redraw the mark on a grid with Figma's vector tools. Do not auto-trace the image.
6. Test the mark at 3 sizes, such as 16, 64 and 512 pixels, and simplify anything that breaks.
7. Add a note with the AI source and "trademark and ownership checks recommended".
**What good looks like:** A clean vector mark that is clearly redrawn (not traced), readable at all 3 sizes, with the 10 concepts, the search result and a risk note saved for your case study.
**Time:** about 40 minutes

## Review Flags
- [VERIFY] Copyright protection for AI-assisted logos is unsettled; confirm the general statement that some authorities have said works without enough human authorship may not be protected, and that redrawing is presented as good practice, not a legal guarantee.
- [REGION] Copyright and trademark rules for AI-assisted work differ by country and are still developing; the lesson gives no legal conclusion.
- [VERSION] The free image generator (to be chosen by a reviewer for the L07 and L08 demos) and its commercial-use terms must be checked against the live tool.
