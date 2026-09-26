# L09 Colour, Type and Accessible Brand Systems | Presenter Script

Course: AI-23 · Video: 5 min · Words: 715

## Hook
Claude suggests a beautiful palette, and writes: these colours have good contrast. Do they? The only way to know is to measure.

## Explain
Last time, we redrew a logo by hand. Now we turn it into a brand system. This lesson is about colour, type and accessible brand systems.

Claude can help here, because it can suggest options with reasons linked to your brief. For example, ask for three palettes of five colours, with hex codes, a role for each colour, and one reason. For type, ask for pairings that are free to use and support the scripts you need, such as Latin and Arabic.

Treat these suggestions as a starting point. Language models can give hex codes that do not match the colour they describe. They can claim contrast values without calculating them. And they can suggest fonts that do not exist, or that do not support your scripts. So you test everything yourself.

First, test colour contrast. The Web Content Accessibility Guidelines, or WCAG, set minimum contrast ratios between text and background, with a higher minimum for normal body text than for large text. Test every text and background pair you plan to use, with a contrast checker plugin in Figma or a free web checker.

If a pair fails, darken or lighten one colour until it passes. Then keep the original colour for decoration only.

Next, test type in real conditions. Set body text at small sizes, like twelve to fourteen pixels, and check that a capital I, a small l and the number one are clear. If your brand uses other scripts, such as Arabic or Devanagari, test real words in those scripts. Check the weights, the line height, and ask a reader of that script to review it.

Think of an AI palette as a paint chart from a shop. The colours look good on the card, but you still test them on your own wall, in your own light, before you paint the whole room.

## Demonstrate
Let's measure a real palette. Omar Haddad is a product designer in Amman, Jordan. His client is a money-transfer app for workers who send money between Jordan and Nepal. The brand must work in English, Arabic and Nepali, which uses the Devanagari script.

Claude suggests five colours: navy, saffron, cream, green and warm grey. It says that all of them work well for text. Omar does not accept that. He tests each text pair he plans to use.

Navy on cream measures ten point two two to one, and passes. But saffron on white measures only two point nine nine to one. Green on white and warm grey on cream also fail for body text. Saffron on navy works for large text only.

So he fixes the failures. He darkens saffron for text and buttons, and it now measures four point seven eight to one on white. He keeps the brighter saffron for illustrations. He also darkens the green and the warm grey until both pass.

For type, Claude suggested a pairing where one font had no Devanagari support. Omar chooses a free font family with Latin, Arabic and Devanagari versions. He tests transfer amounts and short messages at fourteen pixels in all three scripts, and asks two colleagues who read Arabic and Nepali to check the text.

A common mistake is to accept an AI statement like this palette is accessible, without measuring. Another is to test only the main brand colour on white, and forget grey helper text, button text or text on coloured cards. List every pair you will use, and test each one.

## Recap
Let's recap. First, use Claude to suggest palettes and type pairings with roles and reasons, but treat every hex code, font and contrast claim as unverified. Second, test every text and background pair against WCAG contrast guidance, and fix failures by adjusting the colour. Third, test type at small sizes and in every script your brand needs, with real readers.

## CTA
Now it is your turn. In the exercise below this video, you will build a palette of five colours and a type pairing for your brand, test all text colour pairs for contrast, and fix any that fail. It takes about thirty-five minutes. In the next lesson, we build brand guidelines in Figma. See you there.

## Thumbnail
Headline: Measure, Don't Trust
Image: Navy background, two colour swatches with a contrast checker readout between them, a red 'fail' chip and a teal 'pass' chip, headline in teal Inter Bold.

## Production Notes
- Contrast figures must be spoken exactly: 'two point nine nine to one' (saffron #E07A3F on white) and 'four point seven eight to one' (darkened saffron #B8561F on white). Navy on cream is 'ten point two two to one'. All ratios in content.md were re-checked with the standard WCAG relative-luminance formula for this script: 10.22, 2.99, 4.25, 2.82, 3.85, 4.78, 6.47 and 5.39 all match. Re-check them in the contrast tool shown on screen.
- [VERIFY] The WCAG AA thresholds (4.5:1 for normal text and 3:1 for large text) are not spoken as fact in the voiceover; the script says only that WCAG sets a higher minimum for body text than for large text, and that the checker reports pass or fail. After checking against the current WCAG version, the editor may show 'AA body text: 4.5:1' on the scene 5 and scene 11 slides.
- [VERIFY] The pass and fail results in the worked example depend on those thresholds; confirm them with the tool used in the video.
- [VERSION] Figma contrast-checker plugins and web contrast checkers change; confirm the plugin or checker shown on the slides.
- Omar Haddad and the money-transfer app are fictional; stock footage must not show a real payment app or brand.
- Arabic and Devanagari sample text on the scene 13 slide must be checked by readers of those scripts before rendering.
