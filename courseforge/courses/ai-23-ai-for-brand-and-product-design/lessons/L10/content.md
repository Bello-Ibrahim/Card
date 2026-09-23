# L10 Building Brand Guidelines in Figma

Course: AI-23 · Module: M2 · Objectives: O3, O4 · Video: 5 min

## Hook
A brand is only as consistent as the people who use it after you leave the project. What will they open when they need the right blue, or the correct space around the logo?

## Explanation
Brand guidelines turn your decisions into rules other people can follow. For many projects, one clear Figma page is enough to start, and it is the first deliverable of your capstone. It should include:

- **Logo usage:** the main mark and any versions (horizontal, stacked, icon), minimum size, clear space around the mark, and 3 to 4 examples of incorrect use.
- **Colour:** each colour with its name, role and hex code, plus the tested text pairs from L09.
- **Type:** heading and body fonts, a size scale and line heights, and examples in every script the brand uses.
- **Applications:** 2 or more examples, such as a social post, a packaging label, an app icon or a sign.

**Make the rules live in Figma.** Instead of drawing swatches only, set up your colours and type as reusable **styles** or **variables**, and turn the logo versions into **components**. Then every example application uses the real values. If you change a colour later, every example updates. Variables also let you create modes, such as light and dark, if the brand needs them. [VERSION]

**Use AI for draft usage notes.** Writing rules is slow. Claude can draft short usage notes from your decisions. Give it the facts: "Logo minimum size is 24 pixels on screen. Clear space equals the height of the bean shape. Never place the logo on the saffron colour." Ask for short, direct rules in plain language. Then edit: remove anything you did not decide, check every number and make the tone match the brand. The AI drafts; you set the rules.

Keep the page easy to scan. Use headings, short rules and visual examples. A person should find the right answer in under a minute.

**Analogy:** Brand guidelines are like the rules of a sport. Players do not need the history of the game, but they need to know the size of the field, the lines they cannot cross and what counts as a foul. Clear examples of "allowed" and "not allowed" work better than long explanations.

## Worked Example
Sanne de Vries is a freelance designer in Utrecht, the Netherlands. Her hypothetical client is a cycling café, where people can have coffee while their bike is repaired. She has the logo, palette and type from earlier steps.

1. In Figma, she creates a page called "Brand Guidelines" and a frame of 1440 pixels wide.
2. She creates colour styles (or variables) for her 5 colours, named by role, such as "Brand/Primary" and "Text/Default". [VERSION]
3. She creates text styles for H1, H2, Body and Caption.
4. She turns the logo versions into components: full logo, icon only, and a one-colour version.
5. She builds the logo section with a clear-space diagram and 4 examples of incorrect use: stretched, recoloured, rotated, and placed on a busy photo.
6. She asks Claude to draft usage notes from her facts. Claude writes: "Always use the logo on a plain background. Never add effects such as shadows." It also adds, "Use the logo in black and white for newspapers." She did not decide this, so she deletes it.
7. She builds 2 applications, a coffee cup sleeve and a repair-ticket screen, using only her styles and components.
8. She changes the primary colour slightly to test the system. Both applications update.

The client's staff can now use the page without asking Sanne every time.

## Common Mistake
Many designers build guidelines as a picture: colours drawn as rectangles and text typed with manual settings. The page looks correct, but nothing is connected, so later changes create inconsistency. Use styles, variables and components. Another mistake is pasting AI-drafted rules without checking them. The draft may include rules you never made.

## Key Takeaways
1. A one-page brand guidelines frame covers logo usage, colour, type and example applications, and it should be easy to scan.
2. Set up colours and type as styles or variables and the logo as components, so applications use real values and update together.
3. Let Claude draft usage notes from your decisions, then check every rule and number and remove anything you did not decide.

## Hands-on Exercise
**Task:** Capstone step 1: build a one-page brand guidelines frame in Figma with logo, colours, type and 2 example applications.
**Tools:** Figma (free plan); Claude (free plan); your logo, palette and type from L08 and L09.
**Steps:**
1. Create a "Brand Guidelines" page and one large frame.
2. Create colour styles or variables with role names. [VERSION]
3. Create text styles for at least 4 levels.
4. Turn your logo versions into components, and add clear space, minimum size and 3 examples of incorrect use.
5. Write your rules as short facts and ask Claude to draft usage notes. Edit them and delete anything you did not decide.
6. Build 2 example applications using only your styles and components.
7. Change one colour to test that the applications update, then change it back.
**What good looks like:** A clean, scannable page where every colour and text element uses a style or variable, the logo is a component, all rules are yours, and the 2 applications look consistent.
**Time:** about 45 minutes

## Review Flags
- [VERSION] Figma styles, variables, variable modes and their availability on the free plan change; confirm the current names and plan limits before scripting.
