# L10 Your First Automation with Zapier or n8n | Presenter Script

Course: AI-10 · Video: 5 min · Words: 681

## Hook
Every new enquiry means copying a name into a spreadsheet, and sending the same thank-you email. Imagine it happening by itself, correctly, while you sleep. Today, you will build that.

## Explain
In the last lesson, you chose two automation candidates. Now you will build one, and this is capstone step two.

Every automation has two parts. A trigger, which is the event that starts it, such as a new form entry. And one or more actions, which happen next, such as adding a row to a spreadsheet, sending an email, or creating a task.

Tools such as Zapier and n8n connect your apps, so that a trigger in one app causes actions in others. Zapier runs in your browser. n8n can run online or on your own computer. Their free options, limits and app connections change often, so check the current plans before you choose.

Follow three safety rules. Test with example data, never real client details. Start small, with one trigger and two actions. And check the result every time in the first weeks, because automations can fail silently. Also, connect only accounts you trust, and collect only the data you need.

Think of a row of dominoes. The trigger is your finger pushing the first one. Each action is the next domino falling. If one domino is in the wrong place, the chain stops. So you test the whole row before a client ever touches it.

## Demonstrate
Let's build one. Sipho is a freelance video editor in Durban, South Africa. His map shows he copies every enquiry into a spreadsheet and sends a thank-you email by hand.

He has a form, a spreadsheet with matching columns, and a short welcome email with a space for the client's name. His plan is simple. New form entry, then add a spreadsheet row, then send a welcome email.

He signs in to Zapier and creates a new automation. For the trigger, he chooses his form app and the event for a new form response, then connects his account.

He submits a test entry in his form, called Test Client One, with his own email address. Then he tests the trigger, and checks that the test entry appears.

Now the first action. He chooses his spreadsheet app and the event to create a row. He picks his spreadsheet and matches each column to a form field. He tests it, and opens the spreadsheet to see the new row.

Then the second action. He chooses his email app, puts the form's email field in the To box, and inserts the name field into his welcome text. He tests it, and checks his own inbox.

He turns the automation on, and submits two more test entries. On the third test, the email says Dear, with no name, because he left the name field empty. So he makes the name field required in his form.

If you choose n8n, the idea is the same. You create a new workflow with a trigger for your form, then a spreadsheet step and an email step in a line. You run it with example data, and inspect each step's output.

A common mistake is to test once, turn it on, and never check again. Then a renamed column or a disconnected account stops it, and enquiries are lost without warning. So test three times with different example data, including an incomplete entry, and check the results regularly in the first weeks.

## Recap
Let's recap. First, an automation is a trigger followed by one or more actions. Second, build small, test with example data only, and check the results in every connected app. Third, free limits, app connections and interfaces change often, so check the current plans before you choose.

## CTA
Now it is your turn, with capstone step two. Choose one candidate from your map, and build the trigger and two actions. Test three times with example data only. One complete entry, one with an unusual name, and one with a missing field. Take screenshots as evidence. In the next lesson, we decide what to automate and what to keep human.

## Thumbnail
Headline: Trigger, Then Action
Image: Navy background, a row of dominoes falling from left to right, the first tipped by a fingertip, three small app icons (form, sheet, envelope) above them, headline in teal Inter Bold.

## Production Notes
- [VERSION] Zapier and n8n interfaces, menu names ('Zap', 'workflow', 'node', 'test', 'execute'), trigger and action names, and app connections must be checked against the live tools before the screen demo is recorded. Adjust screen_steps wording to match the live interface; keep the voiceover general.
- [VERSION] Free-tier task limits, steps per automation and available apps for Zapier and n8n change often. The voiceover makes no claim about limits or prices and tells learners to check current plans.
- [VERIFY] Whether a two-action (multi-step) automation is available on Zapier's free tier must be confirmed before recording. If it is not, record the demo in n8n with the same three nodes, or reduce the Zapier demo to one action and re-record scenes 12 and 13.
- [VERIFY] Whether n8n can be used free only by self-hosting, and whether its online version offers a free tier or a trial, must be confirmed. The voiceover deliberately does not state this; the lesson page carries the flagged text.
- Screen recording data: use only 'Test Client One', 'Test Client Two' and 'Test Client Three' with an email inbox owned by the production team. Blur account emails and any connected-account names. Use generic form, spreadsheet and email apps as available in the tool.
- Sipho is fictional.
