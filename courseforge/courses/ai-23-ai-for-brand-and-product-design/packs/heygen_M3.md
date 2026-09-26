# HeyGen Batch Pack: AI-23 M3 (AI for UI, Prototyping and the Case Study)

Course: AI for Brand and Product Design. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L11 Generating UI Drafts in Figma

- **Filename:** `ai-23-ai-for-brand-and-product-design_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (684 words). The quality gate accepts ±10%.

```text
Type one sentence, and Figma gives you a full screen, with a header, buttons and text. It looks like a design. But is it your design, in your brand, with your components?

Welcome to module three. Your brand is ready, so now we design the product. This lesson is about generating UI drafts in Figma.

Figma includes AI features that can draft a screen from a text prompt, fill in realistic content and suggest variations. Community plugins add more options, such as realistic text, placeholder images or data. Names and features change often, so this lesson teaches a workflow, not a specific button.

AI drafts are good for speed, for realistic content instead of placeholder text, and for variations to compare. But a draft is not your brand. It uses generic colours and fonts. It is not your design system, because it is built from loose layers. And it is not checked for contrast, touch targets or content.

So the workflow is generate, review, rebuild. Generate a draft from a clear prompt. Review its structure. Which elements does this screen need, and in what order? Then rebuild it with your own styles, variables and components from lesson ten. Keep the useful ideas, and replace everything else.

A good UI prompt names the user, the goal of the screen, the key content and the platform. And, as in lesson five, keep confidential client data out of prompts and plugins.

Think of an AI draft as a builder's scaffolding. It shows the shape of the building quickly. But nobody lives in scaffolding. You replace it with the real, strong materials, which are your components.

Let's see it in Figma. Camila Souza is a product designer in São Paulo, Brazil. Her client is a language-learning app for adults. She needs an onboarding screen where users choose a language to learn.

Camila opens the Figma file with her brand guidelines, styles and components. She creates a new page for AI drafts, then opens Figma's AI features and chooses to generate a design from a prompt.

Her prompt asks for a mobile onboarding screen for adults in Brazil, with a headline in Portuguese, six language options as cards, a progress indicator for step one of three, and a continue button. She generates a draft and one alternative, and places them side by side.

Then she reviews both drafts, and writes sticky notes. Keep the card grid and the progress indicator. Change the flags, because some languages are spoken in many countries. And move the button, which sits too low.

Now she rebuilds. On a new page for the final screen, she creates a frame of the same size. She uses her own button, card and progress components, and applies her text styles and colour variables.

She replaces the flags with language names and a small icon, because a flag represents a country, not a language. Then she runs a community plugin to fill in realistic content, and reads every line it adds.

Finally, she checks the contrast of text on the cards with a contrast plugin, and checks that the buttons meet the touch-target size in her design system. The draft stays on its own page, as a record for her case study.

A common mistake is to polish the AI draft directly, recolouring its layers one by one. It looks right, but it is not connected to your system. Rebuild with components instead. And always read AI content. It can be wrong, or culturally unsuitable.

Let's recap. First, Figma's AI features and plugins give fast drafts, realistic content and variations, but their names and availability change often. Second, treat drafts as starting points. Generate, review the structure, then rebuild with your own styles, variables and components. Third, check every draft for contrast, touch targets, content accuracy and cultural fit.

Now it is your turn. This is step two of your capstone. You will generate draft screens for your key flow, then rebuild them with your brand styles and components. It takes about fifty minutes. In the next lesson, we go from draft to clickable prototype. See you there.
```

## L12 From Draft to Clickable Prototype

- **Filename:** `ai-23-ai-for-brand-and-product-design_M3_L12_presenter.mp4`
- **Expected length:** about 5.2 minutes (725 words). The quality gate accepts ±10%.

```text
Your screens look good in a row. But what happens when the user types the wrong phone number, or has no past orders yet? A prototype shows the answer before a developer writes any code.

In the last lesson, you rebuilt your draft screens with your own components. Now we connect them. This lesson is about going from draft to clickable prototype.

A clickable prototype connects your screens into a flow that a person can use. It has three layers. The first is the happy path. Connect the main screens in order, such as home, choose item, confirm and success. In prototype mode, you link each button to the next screen.

The second layer is states. Real products have more than one state per screen. Error states, like wrong input or a declined payment. Empty states, like no orders yet. Loading states, while the user waits. And component states, such as pressed, disabled or selected.

The third layer is microcopy, the small text on buttons, hints and messages. Claude can give you many options in your brand's tone. Give it the situation and the rules, such as a calm tone, a maximum length, and a clear fix with no blame. Then choose and edit.

Also ask Claude to list edge cases you may have missed. It often finds cases like the shop closing while the user is ordering.

When the flow works, test it with one person. Give them a task, not instructions. Watch without helping, and note where they hesitate. One test will not prove the design works, but it often finds the biggest problem. Ask for consent before you record, and keep recordings out of AI tools.

Think of a prototype as a rehearsal before a play. The set is not finished, but the actors walk through every scene, including the moment when something goes wrong. Problems found in rehearsal are cheap to fix.

Let's build one. Nguyen Minh Anh is a UI designer in Hanoi, Viet Nam. Her client is a street-food stall network with a pre-order app for office workers. Her key flow has five screens: menu, item detail, pickup time, confirm and success.

Minh Anh opens her final page with the five rebuilt screens, and switches to prototype mode. She links the order button to the pickup time screen, on tap, with a slide animation, and repeats this for the other screens.

She sets the menu as the starting point, and names the flow pre-order lunch. Then she asks Claude to list eight edge cases. She picks two. The chosen pickup time is now full, and no past orders.

She asks Claude for five error messages for the full time slot, with her tone and length rules. She edits one to say: twelve thirty is full. Choose twelve forty-five or later.

She duplicates the pickup time screen, adds the error message and a disabled twelve thirty option, and connects it. Then she creates the empty state for my orders, with an illustration and a button back to the menu.

She makes the time-slot component interactive, with selected and not selected states. Then she clicks present, and runs the whole flow once.

Finally, she tests it with a colleague who agreed to take part. The task is: order a bowl of noodles for twelve thirty. He taps the disabled slot twice before he reads the message. So Minh Anh moves the message above the time slots.

A common mistake is to prototype only the happy path. The demo looks smooth, but the first real user meets an error nobody designed. Add at least one error and one empty state. And never paste AI microcopy straight in. Check its tone, length and accuracy.

Let's recap. First, a clickable prototype connects the happy path, and adds error, empty, loading and component states. Second, use Claude to draft microcopy options and list edge cases, then choose and edit the text yourself. Third, a quick task-based test with one person, with their consent, often finds the biggest usability problem.

Now it is your turn. This is step three of your capstone. You will turn your key flow of four to six screens into a clickable prototype, and test it with one person. It takes about fifty minutes. In the next lesson, we learn to critique AI output for usability, accessibility and originality. See you there.
```

## L13 Critiquing AI Output: Usability, Accessibility and Originality

- **Filename:** `ai-23-ai-for-brand-and-product-design_M3_L13_presenter.mp4`
- **Expected length:** about 5.1 minutes (707 words). The quality gate accepts ±10%.

```text
Your brand and flow are finished. Or are they? Before anything reaches a client, one question matters. Can you defend every asset, and do you know where each one came from?

Last time, you built and tested a clickable prototype. Now we step back and review everything. This lesson is about critiquing AI output for usability, accessibility and originality.

AI-assisted work needs the same critique as any design work, plus a few extra checks. Use one checklist with five areas. First, usability. Can a person finish the key task without help? Second, accessibility. Do text pairs meet the contrast guidance from lesson nine, and are touch targets large enough? Third, consistency. Does every screen use your components, styles and variables?

Fourth, originality. Does any asset look close to an existing brand, logo or illustration? Is the logo redrawn, not traced? Fifth, rights. For each asset, which tool helped make it, what do its current terms allow, and are trademark or ownership checks still needed?

You can use Claude as a second reviewer. Share screenshots with no confidential content, and ask for the five most serious problems against your checklist, with a reason for each. Claude often notices unclear labels, missing states or uneven spacing.

But it can also miss problems, misread colours from an image, and give contrast values without measuring. Treat its review as a list of things to check. And keep the final judgement.

Finally, keep an asset log. It is a simple table that records every asset in the deliverable. Its name, its source, the tool, what you changed, the risk checks you did, and its status: clear, needs check, or do not use. The log protects you and your client, and it is the basis of your case study.

Think of an asset log as the ingredient list on food packaging. Most people never read it. But when someone has an allergy or a question, it must be complete and correct.

Let's run a review. Aroha Wiremu is a product designer in Wellington, New Zealand. Her client is a plant nursery, with an app for ordering plants and booking garden advice.

She runs the checklist on her brand and flow, and also asks Claude to review three screenshots. Claude lists six issues, and Aroha checks each one. Four are real. One is wrong. Claude says a button label is too small, but it meets her type scale. And one is not relevant.

Then she makes her top three fixes. For accessibility, the green in stock label on a light green card fails the contrast check, so she darkens the text. For consistency, two screens still use a detached card from the AI draft, so she replaces them with her card component.

For originality, one illustration from an image generator looks very similar to the packaging style of a well-known garden brand. She removes it, and draws a simple illustration herself.

Her asset log shows the result. The logo is an AI-assisted concept, fully redrawn, but a trademark search is still recommended, so its status is needs check. The onboarding copy was drafted with Claude and every line was edited, so it is clear. And the AI leaf illustration is marked do not use.

A common mistake is to ask Claude, is this design good, and accept a general, positive answer. Ask for specific problems against a checklist instead, then verify each one. Another mistake is to write the asset log at the end, from memory. Keep it as you work.

Let's recap. First, critique AI-assisted work for usability, accessibility, design-system consistency, originality and rights. Second, Claude can act as a second reviewer that lists specific problems, but you verify each point, and you keep the final judgement. Third, an asset log records the source, tool, changes, checks and status of every asset, and supports what you can deliver.

Now it is your turn. This is step four of your capstone. Run the checklist on your brand and flow, fix the top three issues, and complete an asset log with the source and risk status of each asset. It takes about forty-five minutes. In the final lesson, we bring it all together in the capstone: writing the AI-assisted design case study. See you there.
```

## L14 Capstone: Writing the AI-Assisted Design Case Study

- **Filename:** `ai-23-ai-for-brand-and-product-design_M3_L14_presenter.mp4`
- **Expected length:** about 5.0 minutes (691 words). The quality gate accepts ±10%.

```text
Two designers show the same polished app. One says, I used AI. The other shows exactly where AI helped, where she overruled it, and which risks she checked. Which one would you hire?

This is the final lesson. Last time, you critiqued your work and built an asset log. Now you tell the story, in the capstone: writing the AI-assisted design case study.

Your capstone is a brand identity and a key app screen flow, designed with an AI-assisted process, and documented as a case study. You have already built most of it. Guidelines in lesson ten. Screens in lesson eleven. The prototype in lesson twelve. And the checklist and asset log in lesson thirteen.

A case study is not a gallery. It shows how you think. Use five sections. Problem: the client, the audience, the goal and one success measure. Process: the main stages, with drafts and dead ends, not only the final result. And an AI use log: where you used AI, what you kept, and what you changed or rejected.

Include at least one case where you overruled AI, and why. Then Decisions: the three to five most important design and risk decisions, with reasons. And finally Outcomes: the final brand and flow, a link to the prototype, what your test found, and what you learned.

Be honest and specific about AI. A vague phrase like AI-powered design is not useful, and hiding AI use can damage trust. A specific sentence is useful. For example: Claude grouped anonymised interview notes into themes, I verified every quote, and I removed one theme.

And never claim a legal result you did not get. Write trademark search recommended, not trademark cleared. Protect data here too. Use anonymised research, and publish client details only with approval.

Think of a case study as a cooking programme, not a restaurant photo. The photo shows the dish. The programme shows the ingredients, the steps, the mistakes and the choices. So the viewer trusts that the cook can do it again.

Let's look at an example. Fatima Bello is a brand and product designer in Lagos, Nigeria. For her capstone, she creates a fictional drinking-water delivery brand for apartment buildings. She uses everything from this course.

Her AI use log is a clear table. In research, Claude found themes, and she removed one theme with a changed quote. In naming, she shortlisted Tidewell, and rejected two names with negative meanings in Yoruba. From her moodboards, she removed images with text artefacts.

Her logo concepts came from an image generator, but the final mark is a full vector redraw, with no traced shapes. The UI draft from Figma was rebuilt with components. And she rejected an error message that blamed the user.

Her decisions section explains why she overruled Claude's bright blue palette. Two text pairs failed contrast, and the colour looked too close to many existing water brands.

Her outcomes section links the prototype. Her tester could not find the delivery time, so she moved it to the confirm screen. One small test, one clear improvement. And the asset log shows the logo as needs check, with a trademark search recommended.

A common mistake is to write only about the final visuals, or to list AI tools without saying what they did. Both hide your judgement, and your judgement is the most valuable part. Show the process, including the moments when you rejected AI output.

Let's recap. First, structure your case study as problem, process, AI use log, decisions and outcomes. Second, be honest and specific about AI use, including where you overruled it, and never claim legal clearance you do not have. Third, protect data in the case study, with anonymised research, and client details only with approval.

Congratulations. You have completed AI for Brand and Product Design. For the last step of your capstone, write and lay out your case study in Figma, covering your brand identity, your key screen flow and your AI-assisted process. It takes about sixty minutes. Check it against the rubric, and then submit it. You have learned to use AI with craft and control. Well done, and good luck.
```
