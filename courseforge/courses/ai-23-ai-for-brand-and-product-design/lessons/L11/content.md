# L11 Generating UI Drafts in Figma

Course: AI-23 · Module: M3 · Objectives: O4, O5 · Video: 5 min (screen demo)

## Hook
Type one sentence, and Figma gives you a full screen with a header, buttons and text. It looks like a design. But is it your design, in your brand, with your components?

## Explanation
Figma now includes AI features that can generate a first draft of a screen from a text prompt, rename layers, fill in realistic content and suggest variations. Community plugins add more options, such as generating realistic text, placeholder images or data. [VERSION] Names, features and plan availability change often, so this lesson teaches a workflow, not a specific button. [VERSION]

**What AI drafts are good for:**

- **Speed:** a first layout for a screen in minutes, so you can think about flow instead of pushing boxes.
- **Realistic content:** real-looking names, prices and messages instead of "Lorem ipsum", which helps you find layout problems early.
- **Variations:** alternative layouts to compare.

**What AI drafts are not:**

- **Not your brand.** Drafts use generic colours, fonts and spacing.
- **Not your design system.** They are often built from loose frames and text layers, not from your components, so they break consistency.
- **Not checked.** Contrast, touch-target sizes, reading order and content may be wrong.

So the workflow is: **generate, review, rebuild.** Generate a draft from a clear prompt. Review it for structure: which elements does this screen need, and in what order? Then rebuild the screen using your own brand styles, variables and components from L10. Keep what is useful (structure, content ideas) and replace everything else.

A good UI prompt includes the user, the goal of the screen, the key content and the platform: "Mobile onboarding screen for a language-learning app. Goal: the user picks the language they want to learn. Show 6 language options with flags, a short headline, and a 'Continue' button. iOS size."

Do not put confidential client data into prompts or plugins. Check each plugin's data terms, as in L05. [VERSION]

**Analogy:** An AI UI draft is like a builder's temporary scaffolding. It shows the shape of the building quickly, but nobody lives in scaffolding. You replace it with the real, strong materials: your components.

## Worked Example
Camila Souza is a product designer in São Paulo, Brazil. Her hypothetical client is a language-learning app for adults. She needs an onboarding screen where users choose a language to learn.

The presenter follows these steps on screen. Feature and menu names may differ in the live tool. [VERSION]

1. Open the Figma file that contains the brand guidelines page, with styles and components.
2. Create a new page called "Onboarding: AI drafts".
3. Open Figma's AI features (for example, from the Actions or AI menu) and choose the option to generate a design from a prompt. [VERSION]
4. Type the prompt: "Mobile onboarding screen for a language-learning app for adults in Brazil. Goal: choose a language to learn. Headline in Portuguese, 6 language options as cards, a progress indicator showing step 1 of 3, and a 'Continuar' button."
5. Generate the draft, then generate one alternative. Place them side by side. [VERSION]
6. Review both drafts and write sticky notes: "Keep: card grid, progress indicator. Change: flags only (some languages are spoken in many countries), button too low."
7. Create a new frame at the same size on a page called "Onboarding: final".
8. Rebuild the screen with the brand components: the Button component, the Card component and the Progress component. Apply text styles and colour variables. [VERSION]
9. Replace flags with language names and a small icon, because a flag represents a country, not a language.
10. Run a community plugin to fill realistic content, such as learner names in the progress messages, and check the text. [VERSION]
11. Check contrast of text on cards with a contrast plugin, and check that buttons meet the touch-target size in her design system.

The final screen uses only her components, and the draft stays on a separate page as a record for her case study.

## Common Mistake
The most common mistake is to polish the AI draft directly: recolouring its layers and changing its fonts one by one. The screen looks right, but it is not connected to the design system, so the next change breaks consistency. Rebuild with components instead. Another mistake is to accept AI content without reading it; generated text can be wrong, culturally unsuitable or not what the product does.

## Key Takeaways
1. Figma AI features and plugins give fast drafts, realistic content and variations, but their names and availability change often.
2. Treat drafts as starting points: generate, review the structure, then rebuild with your own brand styles, variables and components.
3. Check every draft for contrast, touch targets, content accuracy and cultural fit before it goes into the flow.

## Hands-on Exercise
**Task:** Capstone step 2: generate draft screens for your key flow, then rebuild them with your brand styles and components.
**Tools:** Figma with its AI features (plan availability varies) [VERSION]; a free community content plugin [VERSION]; your brand guidelines page from L10.
**Steps:**
1. Choose your key flow of 4 to 6 screens, such as sign-up, booking or checkout.
2. Build any missing core components (button, input, card) with your brand styles.
3. For each screen, write a prompt with user, goal, key content and platform.
4. Generate a draft and one alternative on a "drafts" page. [VERSION]
5. Write notes on what to keep and what to change.
6. Rebuild each screen on a "final" page using only your components, styles and variables.
7. Check contrast, touch-target size and every piece of content.
8. Keep the drafts page for your case study.
**What good looks like:** 4 to 6 rebuilt screens that use your components and brand styles throughout, with a drafts page and notes that show what AI suggested and what you changed.
**Time:** about 50 minutes

## Review Flags
- [VERSION] Figma AI feature names, menus (such as an Actions or AI menu), draft generation, alternatives, plan availability and usage limits must be checked against the live tool before scripting.
- [VERSION] Community plugins for realistic content and contrast checking, and their data terms, change often; the reviewer should choose the plugins shown in the demo.
