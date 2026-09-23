# L13 Critiquing AI Output: Usability, Accessibility and Originality

Course: AI-23 · Module: M3 · Objectives: O5, O6 · Video: 5 min

## Hook
Your brand and flow are finished. Or are they? Before anything reaches a client, one question matters: can you defend every asset, and do you know where each one came from?

## Explanation
AI-assisted work needs the same critique as any design work, plus a few extra checks. Use one checklist with five areas:

**1. Usability.** Can a person complete the key task without help? Are labels clear, is the next step obvious, and do error and empty states tell the user what to do? Use your test notes from L12.

**2. Accessibility.** Do all text pairs meet the WCAG contrast guidance you used in L09? [VERIFY] Are touch targets large enough for your design system's rule? Is information shown only by colour? Does the reading order make sense? Does text still work when it is larger or in another script?

**3. Consistency with the design system.** Does every screen use your components, styles and variables? AI drafts often leave loose layers, extra colours and odd spacing. Figma features that show detached instances or unused styles can help you find them. [VERSION]

**4. Originality.** Does any asset look close to an existing brand, logo or illustration? Do moodboard or image prompts name artists or brands? Is the logo redrawn, not traced?

**5. Rights.** For each asset: which tool made or helped make it, what do its current terms allow for commercial use [VERSION], and are trademark or ownership checks still needed? [REGION]

**Use Claude as a second reviewer.** You can export screenshots of screens (with no confidential content) and ask Claude: "Review this screen against this checklist. List the 5 most serious problems with a reason for each." Claude often notices unclear labels, missing states or inconsistent spacing. But it can also miss problems, misread colours from an image and give contrast values without measuring. Treat its review as a list of things to check, and keep the final judgement.

**Keep an asset log.** A simple table records every asset in the deliverable: name, source (human, AI-assisted, AI-generated, stock, font licence), tool, what you changed, risk checks done and status (clear, needs check, do not use). The log protects you and your client, and it is the basis of your case study.

**Analogy:** An asset log is like the ingredient list on food packaging. Most people will never read it, but when someone has an allergy or a question, it must be complete and correct.

## Worked Example
Aroha Wiremu is a product designer in Wellington, New Zealand. Her hypothetical client is a plant nursery with an app for ordering plants and booking garden advice.

She runs the checklist on her brand and flow. She also asks Claude to review 3 screenshots. Claude lists 6 issues. Aroha checks each one: 4 are real, 1 is wrong (Claude says a button label is "too small", but it meets her type scale) and 1 is not relevant.

Her top 3 fixes:

1. **Accessibility:** the green "In stock" label on a light green card fails the contrast check. She darkens the text colour.
2. **Consistency:** two screens still use a detached card from the AI draft. She replaces them with her card component.
3. **Originality:** one illustration from an image generator looks very similar to the style of a well-known garden brand's packaging. She removes it and draws a simple illustration herself.

Part of her asset log:

| Asset | Source | Tool | Changes | Checks | Status |
|---|---|---|---|---|---|
| Logo | AI-assisted concept, redrawn | Image generator, Figma | Full vector redraw | Reverse image search; trademark search recommended | Needs check |
| Hero illustration | Human | Figma | Not applicable | Originality review | Clear |
| Onboarding copy | AI-assisted | Claude | Edited all lines | Tone and accuracy review | Clear |
| Leaf illustration | AI-generated | Image generator | None | Similar to existing packaging | Do not use |

## Common Mistake
Many designers ask Claude "Is this design good?" and accept a general, positive answer. Ask for specific problems against a checklist, then verify each one. Another mistake is to create the asset log at the end from memory. Sources are easy to forget; keep the log as you work.

## Key Takeaways
1. Critique AI-assisted work for usability, accessibility, design-system consistency, originality and rights.
2. Claude can act as a second reviewer that lists specific problems, but you verify each point and keep the final judgement.
3. An asset log records the source, tool, changes, checks and status of every asset, and supports decisions about what can be delivered.

## Hands-on Exercise
**Task:** Capstone step 4: run the checklist on your brand and flow, fix the top 3 issues, and complete an asset log with the source and risk status of each asset.
**Tools:** Figma (free plan) with a contrast plugin [VERSION]; Claude (free plan); a table in Figma or a spreadsheet.
**Steps:**
1. Copy the five-area checklist into your Figma file.
2. Review your guidelines page and every screen against it, and write each problem you find.
3. Export 2 or 3 screenshots with no confidential content and ask Claude for the 5 most serious problems against the checklist.
4. Check each Claude point and mark it "real", "wrong" or "not relevant".
5. Choose the top 3 issues from all sources and fix them.
6. Build an asset log with a row for every logo, image, illustration, font, icon set and major piece of copy.
7. Give each asset a status: clear, needs check or do not use.
**What good looks like:** A completed checklist, 3 fixes with before-and-after screenshots, Claude's points marked with your verdict, and a complete asset log with an honest status for every asset.
**Time:** about 45 minutes

## Review Flags
- [VERIFY] The WCAG contrast guidance referred to from L09 must be confirmed against the current WCAG version.
- [VERSION] Figma features for finding detached instances or unused styles, contrast plugins, and image generator commercial-use terms change; check them against the live tools.
- [REGION] Trademark and ownership checks for AI-assisted assets differ by country; the lesson gives no legal conclusion.
