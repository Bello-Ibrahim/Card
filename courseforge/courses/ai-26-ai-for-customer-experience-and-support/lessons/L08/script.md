# L08 Automating Simple Tasks with n8n or Zapier | Presenter Script

Course: AI-26 · Video: 5 min · Words: 704

## Hook
On many support teams, someone reads every contact form message each morning, decides which team should handle it, and copies it into a spreadsheet. Today you build a small automation that does this for you, with no code at all.

## Explain
In the last lesson, we designed the hand-off. Today we automate a simple, low-risk task. An automation tool connects apps and runs steps for you when something happens. Two popular tools are Zapier and n8n, and we use them in the browser, with no installation.

A simple AI automation has three parts. The trigger is the event that starts it, such as a new form response. The AI step reads the message and does something with it, such as adding one label from a fixed list. And the action does something with the result, such as adding a row to a spreadsheet.

This is the triage idea from lesson five, running on its own. Following your workflow map, labelling is a good step to automate. A wrong label in a log is low risk, and a person still reads each message. We do not send automatic replies to customers here.

Some practical points. Free plan limits change often, so check the current plan before you start. Some AI steps may need a separate account. And test with made-up data only. Never connect a real customer inbox to a trial account.

Think of a row of dominoes. When the first one falls, the trigger, it knocks the next one, the AI step, which knocks the last one, the action. If one domino is in the wrong place, the chain stops. So test the row before you rely on it.

## Demonstrate
Let's build it. Aroha runs support for a hypothetical outdoor equipment shop in Wellington, New Zealand. She wants each contact form message labelled order, product question, return or other, and logged in a sheet.

First, the test data. I create a form called contact us test, with name, email and message. I submit two made-up responses. Then I create a sheet called support log, with four columns: date, email, message and label.

Now I log in to Zapier and create a new automation. For the trigger, I choose Google Forms, and the event new form response. I connect my test account, choose the form, and test the trigger. A sample response loads.

Next, the AI step. I add the built-in AI option and write the instruction. Read the message. Reply with exactly one label from this list: order, product question, return, other. If unsure, reply other. I map the message field into the input, and test. The output is one label only.

Then the action. I choose Google Sheets and the event create spreadsheet row. I pick the support log sheet and map the date, email, message and AI label to the columns. I test the step, open the sheet, and there is the new row.

Finally, I turn the automation on, submit a new test message, and check the sheet again. In n8n cloud, the same flow uses a form trigger, an AI node and a Google Sheets node.

Aroha tests ten made-up messages. One asks, is the blue tent waterproof, and can I return it if not? It fits two labels. So she updates her instruction: label mixed messages by the first question.

A common mistake is to turn an automation on after one good test, and never look again. A field is renamed, a connection expires, or a run limit is reached, and it stops without warning.

## Recap
Let's recap. First, a simple AI automation has three parts: a trigger, an AI step and an action. Second, start with low-risk steps like labelling and logging, and keep people responsible for replies. Third, plans and interfaces change often, so check the limits, test with made-up data, and check the run history, because automations can fail silently.

## CTA
Now build your own. In the exercise, you will create the same three-step automation in Zapier or n8n, submit ten made-up messages, count the correct labels, and improve your instruction once. Next week, you build your capstone, starting with the next lesson: build your support assistant. See you there.

## Thumbnail
Headline: Your First Support Automation
Image: Navy background, three connected teal blocks (form, AI spark, spreadsheet) linked by arrows like falling dominoes, headline in teal Inter Bold.

## Production Notes
- Screen demo lesson: record scenes 8 to 12 live in Zapier, following content.md's step list. Button and menu names in the screen_steps ('Create' then 'Zap', 'Test trigger', 'Test step', 'AI by Zapier', 'Create Spreadsheet Row', 'Publish') are [VERSION]: check them in the live tool on the recording day and update the steps if they differ.
- [VERIFY] That Zapier's free plan currently allows a three-step automation with a built-in AI step (for example 'AI by Zapier'), and whether n8n cloud offers a free trial that includes AI nodes without a separate paid AI account. The voiceover does not claim either; it tells learners to check the current plan.
- [VERSION] [VERIFY] n8n cloud equivalent (Form Trigger, AI node, Google Sheets append row) is only mentioned in the voiceover; show a still of the n8n canvas in scene 12 only if the node names are confirmed.
- [VERSION] Whether AI steps need a separate AI provider account or key, and any cost.
- Use a fresh test Google account with only the 'Contact us (test)' form and 'Support log' sheet. All form responses are made up; blur the email address of the test account. Never connect a real customer inbox.
- Aroha and the Wellington outdoor shop are fictional. Pronunciation: Aroha (ah-ROH-hah).
- Judgement call carried from curriculum: no coding and no self-hosting of n8n.
