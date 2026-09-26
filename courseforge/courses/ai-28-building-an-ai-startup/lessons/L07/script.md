# L07 Building with No-Code Tools | Presenter Script

Course: AI-28 · Video: 5 min · Words: 716

## Hook
Can you build a working AI product without writing a single line of code? In this lesson, you will watch a prototype being built from start to finish. Then you will build your own.

## Explain
In the last lesson, you scoped your MVP. Now we build it. A no-code builder is a tool where you build apps by choosing and connecting blocks on screen, instead of writing code.

Most no-code prototypes use four parts. A form, where the user enters information. A database, a table that saves each request, like a spreadsheet. An AI step, which sends the input and your instructions to an AI model. And an output page, where the user sees the result.

The AI step runs on a prompt, the instructions you give the model. In a product, the prompt runs every time a user presses the button, so it is part of your product. Write it carefully and save every version. Some builders connect to a provider with an API key, a secret password between programs. Keep it private.

A no-code builder is like construction toy bricks. You cannot make every shape, but you can quickly build a working model of a house and show it to people before you pour concrete.

## Demonstrate
Let's build one. Sipho is a made up founder in Durban, South Africa. Small plumbing businesses lose jobs because they send price quotes too slowly. His core job: a plumber enters job details and gets a clear, professional quote.

First, we draft the prompt with Claude. We ask for instructions that turn a plumber's short notes into a polite quote. Two rules matter most. Use only the prices the plumber enters, and never invent prices. If something is missing, list what is missing.

Next, in Glide, the builder we use here, we create a new blank app. Any no-code builder with a table, a form and an AI step will work. The buttons may simply have different names.

We add a table called Quotes. It has fields for the job description, materials and prices, labour hours, hourly rate, the quote text, and a status.

Then we add a form linked to the table, with the first four fields. All four are required, so a plumber cannot send an empty request.

Now the AI step. We add an AI column that generates text from each new row. We paste Prompt version one and insert the form fields where the builder allows. The answer is saved into the quote text field, and the status is set to draft.

Next, an output page shows the quote text, with a button to copy it. The core flow now runs from start to finish. It looks plain, and that is fine.

Time to test, with fake data only. Replace kitchen tap, tap four hundred and fifty, labour one hour at three hundred and fifty. We check that the quote uses only these numbers.

And here is a problem. The AI added a call out fee that Sipho never entered. So we add a rule to the prompt: do not add any fee that is not listed. We save it as Prompt version two and test again.

We also test a missing field. Without the hourly rate, the quote should ask for it, not invent it. Finally, we share the preview link with one test user and watch them finish the task without help.

If your free plan cannot run an AI step, you can still test the flow. Collect inputs with the form, make the result yourself with Claude, and send it back. That is the Wizard of Oz test from lesson four.

## Recap
Let's recap. First, a no-code prototype usually connects a form, a database, an AI step and an output page. Second, the prompt is part of your product, so write it carefully, test it and save each version. Third, build and test the core flow before you add colours or extra pages.

## CTA
Now it is your turn. In the exercise below this video, build a working prototype of your core flow with a free no-code builder and Claude. Test it with fake data, and watch one real user try it. Next, we look at making the AI part work, with prompts and quality checks. See you there.

## Thumbnail
Headline: An AI App, No Code
Image: Navy background, four connected blocks (form, table, AI step, output) snapping together like toy bricks, headline in teal Inter Bold.

## Production Notes
- Screen demo tool: Glide (free plan), per DECISIONS.md. content.md says 'a no-code builder of your choice'; the voiceover keeps that wording and names Glide only as the tool shown. Backup if Glide's free plan cannot run the AI step: Lovable (free credits), or the manual Wizard of Oz route described in scene 16.
- [VERSION] All Glide steps are adapted from content.md's generic steps 2 to 10 and must be checked against the live tool on the day of recording: the names 'New app', 'Glide Table', 'Data editor', 'Form' component, AI or 'Generate text' column, 'Actions', 'Preview' and 'Share' may differ or move.
- [VERSION] Check whether Glide's free plan includes its AI features (DECISIONS.md: VERIFY), and whether connecting Claude instead needs a paid API key. Never show a real API key on screen; blur it if one appears.
- [VERSION] Claude free-plan limits and data-use terms should be checked before recording.
- Test data is fake only (kitchen tap 450, labour 1 hour at 350). No real customer names or addresses on screen. Prices are placeholders in no named currency.
- Sipho (Durban, South Africa) is fictional. Record the screen at 1080p, zoom to 150% on the prompt and AI-column settings so text is readable.
