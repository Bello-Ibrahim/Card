# L05 Scoping an MVP AI Feature

Course: AI-27 · Module: M1 · Objectives: O2, O3 · Video: 5 min

## Hook
Every AI feature has two user journeys: the one where the AI is right, and the one where it is wrong. Most teams design the first one carefully and discover the second one after launch. This lesson is about designing both on day one.

## Explanation
An AI minimum viable product (MVP) should be narrow. Use four limits:

1. **One user.** Choose one user group with a clear need, such as "new sellers" instead of "all users".
2. **One task.** Solve one judgement task well, such as "draft a reply to a buyer question", not "manage all seller communication".
3. **A human in the loop.** In the first version, a person reviews or approves the AI output before it has an effect. This lowers the error cost (L04) and gives you feedback data.
4. **A clear fallback.** Decide what happens when the AI is unsure, fails or is switched off. The product must still work without it.

Then design the **experience for errors** as carefully as the happy path. Ask four questions:

- **When the AI is wrong,** how can the user notice and correct it? Examples: editable drafts, visible sources, an "undo" option.
- **When the AI is unsure,** what does the user see? Options include asking a clarifying question, showing fewer suggestions, or showing none. Your team can often use a confidence score or a set of rules to decide when to show nothing.
- **When the AI should not answer,** such as a request outside the task or an unsafe request, what message appears, and where does the user go next?
- **When the AI is unavailable,** because of an outage or a usage limit, what is the normal non-AI path?

Also design the **feedback loop**: a simple way for users to say "this was helpful" or "this was wrong". This is your first source of real-world evaluation data.

**Analogy:** A new pilot does not fly passengers alone on the first day. They fly one route, with a senior pilot next to them, and they practise emergency procedures before normal flights. An AI MVP flies one route, with a human next to it, and has its emergency procedures designed before launch.

## Worked Example
Nour Hassan is a PM at a hypothetical online marketplace in Egypt where people sell used furniture and electronics. Sellers receive many buyer questions, such as "Is this still available?" and "Can you deliver to Giza?" Slow replies lose sales.

The first idea was "an AI assistant that handles all buyer conversations". Nour narrows it:

- **User:** sellers with fewer than 20 listings, who reply from their phones.
- **Task:** suggest up to three short reply drafts for a buyer's message, in Arabic or English to match the buyer.
- **Human in the loop:** the seller must tap a suggestion, can edit it, and then sends it. Nothing is sent automatically.
- **Fallback:** if no good suggestion is available, the normal empty reply box appears.

Nour's happy path: the buyer asks about delivery, three suggestions appear, the seller taps one, edits the price and sends it.

Her failure paths:

- **Wrong suggestion:** a suggestion states a delivery promise the seller never made. Design: suggestions never include prices, dates or promises unless they come from the listing; the seller always sees and edits the text before sending.
- **Unsure:** the buyer's message is unclear or mixes topics. Design: show one neutral suggestion, such as "Thank you for your message. Could you tell me more about what you need?", or show none.
- **Should not answer:** the buyer message contains abuse or asks for personal data. Design: no suggestions, plus a "Report this message" link.
- **Unavailable:** the normal reply box appears with no error message for the seller.

Every suggestion has a small "Not useful" button. Nour will use those taps, plus whether sellers edit or send suggestions unchanged, as early quality signals.

## Common Mistake
Teams often think a human in the loop makes the error experience unimportant, because "the user will check it". In practice, busy users stop checking carefully when suggestions are usually right. Design so that errors are easy to see, such as keeping promises and numbers out of drafts, and do not rely only on the user's attention.

## Key Takeaways
1. Scope an AI MVP to one user, one task, a human in the loop and a clear non-AI fallback.
2. Design four failure paths: wrong, unsure, should not answer, and unavailable.
3. Build a simple feedback signal into the first version, because it becomes your first real evaluation data.

## Hands-on Exercise
**Task:** Sketch the happy path and the failure paths for your chosen feature, including what the user sees when the AI is wrong or unsure.
**Tools:** Figma or FigJam (free plan) [VERSION]; paper sketches photographed also work.
**Steps:**
1. Take your top idea from L04. Write the scope in four lines: user, task, human in the loop, fallback.
2. In FigJam, draw the happy path as 4 to 6 boxes from the user's first action to the result.
3. Add a branch for each failure path: wrong, unsure, should not answer, unavailable.
4. For each branch, sketch or describe what the user sees on screen and what they can do next.
5. Mark where users give feedback and where a human reviews the output.
6. Keep the board. You will reuse it in the capstone (L13).
**What good looks like:** A readable flow with one happy path and four failure branches, each ending in a clear user action. The scope is narrow enough to build and test in a few weeks.
**Time:** about 30 minutes

## Review Flags
- [VERSION] Figma and FigJam free-plan limits must be checked before recording.
