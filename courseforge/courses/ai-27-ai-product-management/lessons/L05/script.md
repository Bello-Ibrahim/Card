# L05 Scoping an MVP AI Feature | Presenter Script

Course: AI-27 · Video: 5 min · Words: 713

## Hook
Every AI feature has two user journeys: the one where the AI is right, and the one where it is wrong. Most teams design the first one carefully, and discover the second one after launch. Today, we design both on day one.

## Explain
You now have a top idea. The next step is to scope it. An AI minimum viable product should be narrow, and four limits help. In the last lesson, a narrower scope lowered the error cost. Now we make that concrete.

One user: a single group with a clear need, such as new sellers, not all users. One task: one judgement task done well. A human in the loop: in the first version, a person approves the output before it has an effect. And a clear fallback: the product must still work when the AI is unsure, fails or is switched off.

Then design the experience for errors as carefully as the happy path. Ask four questions. When the AI is wrong, how does the user notice and correct it? When it is unsure, what does the user see? When it should not answer, what message appears? And when it is unavailable, what is the normal path?

For the unsure case, your team can often use a confidence score or a set of rules to decide when to show nothing at all.

Also design a feedback loop: a simple way for users to say this was helpful, or this was wrong. This becomes your first real evaluation data. Keep it light, with one tap, so users actually use it.

Here is a way to picture it. A new pilot does not fly passengers alone on the first day. They fly one route, with a senior pilot next to them, and they practise emergency procedures before normal flights.

An AI MVP flies one route, with a human next to it, and its emergency procedures are designed before launch.

## Demonstrate
Let's see an example. Nour Hassan is a PM at a hypothetical online marketplace in Egypt, where people sell used furniture and electronics. Sellers get many buyer questions, such as can you deliver to Giza, and slow replies lose sales.

The first idea was an AI assistant that handles all buyer conversations. Nour narrows it. The user is sellers with fewer than twenty listings, who reply from their phones. The task is to suggest up to three short reply drafts, in Arabic or English to match the buyer. The seller taps, edits and sends. Nothing is sent automatically.

Now the failure paths. Wrong: a suggestion makes a delivery promise the seller never made. So suggestions never include prices, dates or promises unless they come from the listing. Unsure: the message is unclear. So show one neutral suggestion, asking the buyer to say more, or show none.

Should not answer: the message contains abuse or asks for personal data. So there are no suggestions, and a report this message link appears. Unavailable: the normal reply box appears, with no error message for the seller. In each case, the seller always knows what to do next.

Every suggestion has a small not useful button. Nour will use those taps, and whether sellers edit suggestions or send them unchanged, as early quality signals. These signals cost almost nothing to collect, and they show real use from the first day.

A common mistake is thinking a human in the loop makes errors unimportant. Busy users stop checking carefully when suggestions are usually right. So make errors easy to see. For example, keep promises and numbers out of the drafts, and do not rely only on the user's attention.

## Recap
Let's recap. First, scope an AI MVP to one user, one task, a human in the loop and a clear fallback. Second, design four failure paths: wrong, unsure, should not answer and unavailable. Third, build a simple feedback signal into the first version, because it becomes your first real evaluation data.

## CTA
Now it is your turn. In the exercise below, sketch the happy path and the four failure paths for your feature in Figma or FigJam. Keep the board, because you will reuse it in the capstone. It takes about thirty minutes. In the next lesson, we look at data needs, and what your feature learns from. See you there.

## Thumbnail
Headline: Design the Wrong Path
Image: Navy background, a flow diagram splitting into one teal happy path and four orange failure branches, headline in teal Inter Bold.

## Production Notes
- [VERSION] Figma and FigJam free-plan limits must be checked before recording (exercise tool).
- Nour Hassan and the online marketplace in Egypt are hypothetical; no real marketplace interface or logo. Giza is mentioned only as a place in a buyer question.
- The phone mock-ups on the slides show reply drafts in both Arabic and English; any Arabic text on screen needs a native-speaker check and Noto Sans Arabic.
