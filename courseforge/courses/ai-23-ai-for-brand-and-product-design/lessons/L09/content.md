# L09 Colour, Type and Accessible Brand Systems

Course: AI-23 · Module: M2 · Objectives: O3, O5 · Video: 5 min

## Hook
Claude suggests a beautiful palette and writes, "These colours have good contrast." Do they? The only way to know is to measure.

## Explanation
Colour and type turn a logo into a brand system. Claude can help you here, because it can suggest options with reasons linked to your brief. For example: "Suggest 3 palettes of 5 colours each, with hex codes, for a brand that feels trustworthy and warm. For each colour, give its role (primary, secondary, background, text, accent) and one reason." For type: "Suggest 3 type pairings, one for headings and one for body text, that are free to use and support Latin and Arabic scripts."

Treat these suggestions as a starting point. Language models can give hex codes that do not match the colour they describe, claim contrast values without calculating them, or suggest fonts that do not exist or do not support the scripts you need. You test everything yourself.

**Test colour contrast.** WCAG (the Web Content Accessibility Guidelines) sets minimum contrast ratios between text and background. For example, level AA asks for at least 4.5:1 for normal body text and 3:1 for large text. [VERIFY] Test every text and background pair you plan to use with a contrast checker, such as a Figma plugin or a free web checker. [VERSION] If a pair fails, darken or lighten one colour until it passes, and keep the original as a decorative colour only.

**Test type in real conditions.** Set your body font at small sizes, such as 12 to 14 pixels on screen, and check that letters like "I", "l" and "1" are clear. If your brand works in other scripts, such as Arabic or Devanagari, test real words in those scripts, not only the Latin version. Check that the font family includes the script, that weights look balanced next to the Latin text, and that line height works for the taller shapes of some scripts. Ask a reader of that script to check the result.

**Analogy:** A palette from AI is like a paint chart from a shop. The colours look good on the card, but you still test them on your own wall, in your own light, before you paint the whole room.

## Worked Example
Omar Haddad is a product designer in Amman, Jordan. His hypothetical client is a money-transfer app for workers who send money between Jordan and Nepal. The brand must work in English, Arabic and Nepali, which uses the Devanagari script.

Claude suggests a palette: navy #1E3A5F, saffron #E07A3F, cream #F6F1E7, green #2E8B57 and warm grey #9A8F80. It says all colours "work well for text".

Omar tests each planned text pair with a contrast checker:

| Pair | Ratio | Result at AA for body text [VERIFY] |
|---|---|---|
| Navy on cream | 10.22:1 | Pass |
| Saffron on white | 2.99:1 | Fail |
| Green on white | 4.25:1 | Fail |
| Warm grey on cream | 2.82:1 | Fail |
| Saffron on navy | 3.85:1 | Fail for body text; large text only |

He fixes the failures. He darkens saffron to #B8561F (4.78:1 on white) for text and buttons, and keeps the brighter saffron for illustrations. He darkens green to #1F6B45 (6.47:1) and warm grey to #6B6154 (5.39:1 on cream).

For type, Claude suggested a pairing where one font had no Devanagari support. Omar chooses a free font family with Latin, Arabic and Devanagari versions, tests transfer amounts and short messages at 14 pixels in all three scripts, and asks two colleagues who read Arabic and Nepali to check the text.

## Common Mistake
The most common mistake is to accept an AI statement such as "this palette is accessible" without measuring. Another mistake is to test only the main brand colour on white and forget other pairs, such as grey helper text, text on buttons or text on coloured cards. List every pair you will use and test each one.

## Key Takeaways
1. Use Claude to suggest palettes and type pairings with roles and reasons, but treat every hex code, font and contrast claim as unverified.
2. Test every text and background pair against WCAG contrast guidance (for example, 4.5:1 for normal text at AA) and fix failures by adjusting the colour.
3. Test type at small sizes and in every script your brand needs, and ask real readers of those scripts to check it.

## Hands-on Exercise
**Task:** Build a palette of 5 colours and a type pairing for your brand, test all text colour pairs for contrast, and fix any that fail.
**Tools:** Claude (free plan); Figma (free plan) with a contrast-checker plugin, or a free web contrast checker [VERSION].
**Steps:**
1. Ask Claude for 3 palettes of 5 colours with roles and reasons, based on your brief and moodboard.
2. Choose one palette and place the colours as swatches in Figma.
3. List every text and background pair you will use, including buttons, helper text and cards.
4. Test each pair and record the ratio and the result.
5. Adjust any colour that fails and test again.
6. Ask Claude for type pairings that support your scripts; confirm script support on the font's own page.
7. Test the body font at 12 to 14 pixels and in every script your brand needs.
**What good looks like:** A palette with roles, a table of every text pair with its ratio and a clear pass or fail, fixed colours for all failures, and a type pairing tested at small sizes and in all required scripts.
**Time:** about 35 minutes

## Review Flags
- [VERIFY] Confirm the WCAG contrast figures (4.5:1 for normal text and 3:1 for large text at level AA) against the current WCAG version before scripting. The ratios in the worked example were calculated with the standard WCAG formula but should be re-checked with the contrast tool used in the video.
- [VERSION] Figma contrast-checker plugins and web contrast checkers change; confirm the tool shown in the video.
