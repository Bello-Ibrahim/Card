# L12 From Draft to Clickable Prototype | Presenter Script

Course: AI-23 · Video: 5 min · Words: 731

## Hook
Your screens look good in a row. But what happens when the user types the wrong phone number, or has no past orders yet? A prototype shows the answer before a developer writes any code.

## Explain
In the last lesson, you rebuilt your draft screens with your own components. Now we connect them. This lesson is about going from draft to clickable prototype.

A clickable prototype connects your screens into a flow that a person can use. It has three layers. The first is the happy path. Connect the main screens in order, such as home, choose item, confirm and success. In prototype mode, you link each button to the next screen.

The second layer is states. Real products have more than one state per screen. Error states, like wrong input or a declined payment. Empty states, like no orders yet. Loading states, while the user waits. And component states, such as pressed, disabled or selected.

The third layer is microcopy, the small text on buttons, hints and messages. Claude can give you many options in your brand's tone. Give it the situation and the rules, such as a calm tone, a maximum length, and a clear fix with no blame. Then choose and edit.

Also ask Claude to list edge cases you may have missed. It often finds cases like the shop closing while the user is ordering.

When the flow works, test it with one person. Give them a task, not instructions. Watch without helping, and note where they hesitate. One test will not prove the design works, but it often finds the biggest problem. Ask for consent before you record, and keep recordings out of AI tools.

Think of a prototype as a rehearsal before a play. The set is not finished, but the actors walk through every scene, including the moment when something goes wrong. Problems found in rehearsal are cheap to fix.

## Demonstrate
Let's build one. Nguyen Minh Anh is a UI designer in Hanoi, Viet Nam. Her client is a street-food stall network with a pre-order app for office workers. Her key flow has five screens: menu, item detail, pickup time, confirm and success.

Minh Anh opens her final page with the five rebuilt screens, and switches to prototype mode. She links the order button to the pickup time screen, on tap, with a slide animation, and repeats this for the other screens.

She sets the menu as the starting point, and names the flow pre-order lunch. Then she asks Claude to list eight edge cases. She picks two. The chosen pickup time is now full, and no past orders.

She asks Claude for five error messages for the full time slot, with her tone and length rules. She edits one to say: twelve thirty is full. Choose twelve forty-five or later.

She duplicates the pickup time screen, adds the error message and a disabled twelve thirty option, and connects it. Then she creates the empty state for my orders, with an illustration and a button back to the menu.

She makes the time-slot component interactive, with selected and not selected states. Then she clicks present, and runs the whole flow once.

Finally, she tests it with a colleague who agreed to take part. The task is: order a bowl of noodles for twelve thirty. He taps the disabled slot twice before he reads the message. So Minh Anh moves the message above the time slots.

A common mistake is to prototype only the happy path. The demo looks smooth, but the first real user meets an error nobody designed. Add at least one error and one empty state. And never paste AI microcopy straight in. Check its tone, length and accuracy.

## Recap
Let's recap. First, a clickable prototype connects the happy path, and adds error, empty, loading and component states. Second, use Claude to draft microcopy options and list edge cases, then choose and edit the text yourself. Third, a quick task-based test with one person, with their consent, often finds the biggest usability problem.

## CTA
Now it is your turn. This is step three of your capstone. You will turn your key flow of four to six screens into a clickable prototype, and test it with one person. It takes about fifty minutes. In the next lesson, we learn to critique AI output for usability, accessibility and originality. See you there.

## Thumbnail
Headline: Prototype the Error Too
Image: Navy background, five phone screens linked by teal arrows, with one branch leading to an error screen marked by a small amber icon, headline in teal Inter Bold.

## Production Notes
- [VERSION] Figma Prototype mode, triggers ('On tap'), animations, flow starting points, variants, interactive components and Present mode: check names and free-plan limits against the live tool before recording, and update the screen_steps to the live labels.
- [REGION] Rules on consent for recording test sessions and on handling participant data differ by country; the script asks for consent and keeps recordings out of AI tools as a principle only.
- The test in scene 15 is shown with the colleague's consent; do not show a real person's face or details unless they have signed a release. A re-enactment or screen-only view is fine.
- Times are spoken as 'twelve thirty' and 'twelve forty-five'; the screen shows 12:30 and 12:45.
- Nguyen Minh Anh (called Minh Anh) and the street-food pre-order app are fictional; stock footage must not show a real stall name or brand.
- This lesson is capstone step 3; the CTA says so.
