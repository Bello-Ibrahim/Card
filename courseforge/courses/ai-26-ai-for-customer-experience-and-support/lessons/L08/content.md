# L08 Automating Simple Tasks with n8n or Zapier

Course: AI-26 · Module: M2 · Objectives: O3, O4 · Video: 5 min (screen demo)

## Hook
Every morning, someone on many support teams opens the contact-form inbox, reads each message, decides which team should handle it and copies it into a spreadsheet. It takes time and nobody enjoys it. Today you will build a small automation that does this work for you, with no code.

## Explanation
An **automation tool** connects apps and runs steps for you when something happens. Two popular tools are **Zapier** and **n8n**. Both offer free or trial plans in the cloud, which means you use them in a web browser and do not install anything [VERSION] [VERIFY]. In this course we do not self-host n8n on our own server; we use its cloud version.

A simple AI automation has three parts:

1. **Trigger:** the event that starts the automation. For example, "a new response arrives in a form".
2. **AI step:** an AI model reads the message and does something with it, such as adding a label from a fixed list.
3. **Action:** the automation does something with the result. For example, "add a new row to a spreadsheet".

This is the same triage idea from L05, now running automatically. It also follows your map from L06: labelling is a good step to **automate** because a wrong label in a log is low risk, and a person still reads each message. Sending replies to customers automatically is a much bigger step, and we do not do it here.

Some practical points:

- **Free plan limits change often.** Free plans limit the number of runs per month, the number of steps, or the AI features included. Check the current plan before you start [VERSION].
- **AI steps may need an account or key.** Some AI steps are built into the tool; others need a separate account with an AI provider, which can cost money [VERSION] [VERIFY]. Use the built-in option if your plan includes it.
- **Test with made-up data only.** Do not connect a real customer inbox to a free trial account.

**Analogy:** An automation is like a row of dominoes. When the first one falls (the trigger), it knocks the next one (the AI step), which knocks the last one (the action). You set up the row once, and it runs every time the first domino falls. If one domino is in the wrong place, the chain stops, so you test the row before you rely on it.

## Worked Example
Aroha runs support for a hypothetical outdoor equipment shop in Wellington, New Zealand. Customers use a contact form on the website. She wants each message labelled as Order, Product question, Return or Other, and logged in a sheet, so that each team can filter its own messages.

The presenter follows these steps on screen, using Zapier as the example. Button and menu names may differ in the live tool [VERSION].

1. Create a Google Form called "Contact us (test)" with three questions: Name, Email and Message. Submit two test responses using made-up names.
2. Create a Google Sheet called "Support log" with column headers: Date, Email, Message, Label.
3. Log in to Zapier and click **Create** and then **Zap** (or the current button for a new automation) [VERSION].
4. Choose the trigger app **Google Forms** and the event **New Form Response**. Connect your Google account, choose the form, and click **Test trigger** to load a sample response.
5. Add a second step. Choose the built-in AI option (for example "AI by Zapier") [VERSION] [VERIFY]. Write the instruction: "Read the message. Reply with exactly one label from this list: Order, Product question, Return, Other. If unsure, reply Other." Map the Message field from step 1 into the input.
6. Click **Test step** and check that the output is one label only.
7. Add a third step. Choose **Google Sheets** and the event **Create Spreadsheet Row**. Choose the "Support log" sheet and map Date, Email, Message and the AI label to the columns.
8. Test the step and open the sheet to confirm that a new row appears.
9. Turn the automation on (publish it). Submit a new test form response and check the sheet again.

In n8n cloud, the same flow uses a **Form Trigger** or Google Forms trigger, an AI node, and a **Google Sheets** node with the action to append a row [VERSION] [VERIFY]. The logic is identical: trigger, AI step, action.

Aroha tests with 10 made-up messages. One message, "Is the blue tent waterproof and can I return it if not?", fits two labels. She decides that mixed messages should be labelled by the first question and updates her instruction.

## Common Mistake
Many beginners turn on the automation after one successful test and never look at it again. Automations fail silently: a form field is renamed, a connection expires or the free run limit is reached, and messages stop appearing in the sheet. Test with several different messages, check the tool's run history, and look at the sheet regularly for missing rows or strange labels.

## Key Takeaways
1. A simple AI automation has three parts: a trigger, an AI step and an action.
2. Start by automating low-risk steps, such as labelling and logging, and keep people responsible for replies to customers.
3. Free plans and interfaces change often, so check current limits, test with made-up data and check the run history.

## Hands-on Exercise
**Task:** Build a 3-step automation in n8n or Zapier's free tier that labels incoming form messages with AI and logs them in a sheet.
**Tools:** Zapier (free plan) or n8n (cloud free trial) [VERSION] [VERIFY]; Google Forms and Google Sheets (free with a Google account), or similar form and sheet tools.
**Steps:**
1. Create a test form with Name, Email and Message fields, and a sheet with Date, Email, Message and Label columns.
2. Create a new automation and set the trigger to "new form response".
3. Add an AI step with an instruction that returns exactly one label from 4 or 5 categories, including "Other".
4. Add an action that creates a new row in the sheet with the message and the AI label.
5. Test each step, then turn the automation on.
6. Submit 10 made-up messages, including 2 unclear ones. Use no real names, emails or customer data.
7. Check the sheet. Count correct labels and note any wrong ones.
8. Improve your AI instruction once and test again.
**What good looks like:** A working automation with three steps, 10 rows in the sheet with labels, a count of correct labels, and one improvement to your instruction based on the results. Screenshots of each step are saved for your records.
**Time:** about 40 minutes

## Review Flags
- [VERSION] n8n and Zapier free-tier limits, AI steps and interfaces: button names ("Create", "Zap", "Test trigger", "Test step", "Create Spreadsheet Row", "Form Trigger"), and the number of steps allowed on free plans, must be checked in the live tools before recording.
- [VERIFY] That Zapier's free plan currently allows a 3-step automation with a built-in AI step (for example "AI by Zapier"), and whether n8n cloud offers a free trial that includes AI nodes without a separate paid AI account.
- [VERSION] Whether AI steps need a separate AI provider account or key, and any cost.
- Judgement call (from curriculum): no coding and no self-hosting of n8n; learners use cloud versions and made-up data only.
