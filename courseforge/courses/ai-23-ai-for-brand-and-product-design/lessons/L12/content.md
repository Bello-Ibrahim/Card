# L12 From Draft to Clickable Prototype

Course: AI-23 · Module: M3 · Objectives: O4, O7 · Video: 5 min (screen demo)

## Hook
Your screens look good in a row. But what happens when the user types the wrong phone number, or has no past orders yet? A prototype shows the answer before a developer writes any code.

## Explanation
A clickable prototype connects your screens into a flow that a person can use. For your capstone, it has three layers:

**1. The happy path.** Connect the main screens in order: for example, home, choose item, confirm, success. In Figma's Prototype mode, you drag a connection from a button to the next frame and choose a trigger (such as "On tap") and an animation. [VERSION]

**2. States and variations.** Real products have more than one state per screen. Important ones are:

- **Error states:** wrong input, network failure, payment declined.
- **Empty states:** no orders yet, no search results.
- **Loading states:** what the user sees while waiting.
- **Component states:** default, pressed, disabled, selected.

Build component states as variants and use interactive components, so a button can change state without new frames. [VERSION]

**3. Microcopy.** Microcopy is the small text: button labels, hints, error messages and empty-state messages. Claude is useful here, because it can produce many options quickly in your brand's tone from L06. Give it the situation and the rules: "Write 5 options for an error message when the phone number has the wrong number of digits. Tone: calm and practical. Maximum 60 characters. Tell the user how to fix it. No blame." Then choose and edit. Also ask Claude to list **edge cases** you may have missed: "List 8 things that can go wrong in this order flow." It often finds cases such as "the shop closes while the user is ordering".

**Quick task-based test.** When the flow works, test it with one person. Give them a task, not instructions: "Order lunch for pickup at 12:30." Watch without helping. Note where they hesitate, click the wrong place or ask a question. One test will not prove the design works, but it often finds the biggest problem. Ask for consent before you record anything, and do not put the recording or the person's details into AI tools. [REGION]

**Analogy:** A prototype is like a rehearsal before a play. The set is not finished and the costumes may be simple, but the actors walk through every scene, including the moment when something goes wrong. Problems found in rehearsal are cheap to fix.

## Worked Example
Nguyen Minh Anh is a UI designer in Hanoi, Viet Nam. Her hypothetical client is a street-food stall network with a pre-order app for office workers. Her key flow has 5 screens: menu, item detail, pickup time, confirm and success.

The presenter follows these steps on screen. Interface names may differ in the live tool. [VERSION]

1. Open the "final" page with the 5 rebuilt screens from L11.
2. Switch to Prototype mode. [VERSION]
3. Select the "Order" button on the item detail screen, drag the connection to the pickup time screen, and set "On tap" and a slide animation. Repeat for the other screens.
4. Set the menu screen as the flow's starting point and name the flow "Pre-order lunch". [VERSION]
5. Open Claude and ask: "List 8 edge cases in a lunch pre-order flow." From the list, Minh Anh chooses two: "chosen pickup time is now full" and "no past orders" (empty state).
6. Ask Claude for 5 microcopy options for the full-time-slot error, with the tone and length rules. She edits one: "12:30 is full. Choose 12:45 or later."
7. Duplicate the pickup time screen, add the error message and a disabled 12:30 option, and connect it.
8. Create the empty state for "My orders" with an illustration and a button to the menu.
9. Make the time-slot component interactive: selected and not selected. [VERSION]
10. Click Present and run the whole flow once. [VERSION]
11. Test with a colleague who agreed to take part: "Order a bowl of noodles for 12:30." He tries to tap the disabled 12:30 slot twice before he reads the message. Minh Anh moves the message above the time slots.

## Common Mistake
Many designers prototype only the happy path. The demo looks smooth, but the first real user meets an error nobody designed. Add at least one error and one empty state. Another mistake is to paste AI microcopy directly into the screens. Check it for tone, length, accuracy and whether it really tells the user what to do next.

## Key Takeaways
1. A clickable prototype connects the happy path and adds error, empty, loading and component states.
2. Use Claude to draft microcopy options and list edge cases, then choose and edit the text yourself.
3. A quick task-based test with one person, with their consent, often finds the biggest usability problem in the flow.

## Hands-on Exercise
**Task:** Capstone step 3: turn your key flow of 4 to 6 screens into a clickable prototype and test it with one person.
**Tools:** Figma (free plan) Prototype mode [VERSION]; Claude (free plan); one volunteer tester.
**Steps:**
1. Connect your happy path screens with triggers and animations.
2. Set a starting point and name the flow. [VERSION]
3. Ask Claude for 8 edge cases and choose at least 2, including one error and one empty state.
4. Ask Claude for microcopy options with tone and length rules, and edit the ones you use.
5. Build the new states and connect them.
6. Make at least one component interactive. [VERSION]
7. Test with one person who agreed to take part. Give a task, watch without helping, and note problems.
8. Fix the biggest problem and record what you changed.
**What good looks like:** A working prototype of 4 to 6 screens plus at least one error and one empty state, edited microcopy, and a short test note with one problem found and fixed.
**Time:** about 50 minutes

## Review Flags
- [VERSION] Figma Prototype mode, triggers, animations, flow starting points, variants, interactive components and Present mode names and plan limits must be checked against the live tool before scripting.
- [REGION] Rules on consent for recording test sessions and handling participant data differ by country; the lesson asks for consent and keeps test data out of AI tools as a principle.
