# L10 Your First Automation with Zapier or n8n

Course: AI-10 · Module: M3 · Objectives: O5, O4 · Video: 5 min (screen demo)

## Hook
Every time a new enquiry arrives, you copy the name into a spreadsheet and send the same thank-you email. It takes a few minutes. Now imagine it happening by itself, correctly, even while you sleep. Today you will build that.

## Explanation
Every automation has two parts:

- A **trigger**: the event that starts it. For example, "a new form entry arrives".
- One or more **actions**: what happens next. For example, "add a row to a spreadsheet", "send an email", "create a task".

Tools such as **Zapier** and **n8n** connect your apps so that a trigger in one app causes actions in others. Zapier runs in your browser as an online service. n8n can be used as an online service or installed on your own computer or server. [VERSION] Both offer ways to start without paying, but free-tier limits, trial periods and available app connections differ and change often. [VERSION] [VERIFY] For n8n, free use may require self-hosting, while the online version may be a paid service with a trial. [VERIFY] Check the current plans before you choose.

Three safety rules for your first automation:

1. **Test with example data**, never with real client details. Use names such as "Test Client One" and an email address that you own.
2. **Start small**: one trigger and two actions. You can add more later.
3. **Check the result every time** in the first weeks. Automations can fail silently, for example when you rename a spreadsheet column.

Also think about data. An automation copies client information between services. Only connect accounts you trust, and collect only the information you need.

**Analogy:** An automation is like a row of dominoes. The trigger is your finger pushing the first domino; each action is the next domino falling. If one domino is in the wrong place, the chain stops, which is why you test the whole row before a client ever touches it.

## Worked Example
Sipho is a freelance video editor in Durban, South Africa. His workflow map from L09 shows that every enquiry arrives through a form, and he copies each one into a spreadsheet and sends a thank-you email by hand. He builds: **new form entry → add spreadsheet row → send welcome email.**

He prepares three things first: a free online form with fields for name, email and project type; a spreadsheet with matching column headings; and a short welcome email with a placeholder for the name.

**Screen demo steps (Zapier version):** [VERSION] [VERIFY]
1. Sign in to Zapier and choose to create a new automation (Zapier calls it a "Zap"). [VERSION]
2. For the **trigger**, choose your form app and the event "new form response". Connect your account. [VERSION]
3. Submit a test entry in your form ("Test Client One", your own email). Click to test the trigger and check that the test entry appears. [VERSION]
4. Add the first **action**: your spreadsheet app, event "create row". Choose your spreadsheet and match each column to a form field. [VERSION]
5. Test the action and open the spreadsheet to check the new row.
6. Add the second **action**: your email app, event "send email". Put the form's email field in "To", and insert the name field into your welcome text. [VERSION]
7. Test the action and check your own inbox.
8. Turn the automation on. Submit two more test entries and check the spreadsheet and inbox each time.

**n8n version:** [VERSION] [VERIFY] Create a new workflow, add a trigger node for your form (or a webhook), then add a spreadsheet node and an email node, connected in a line. Use the test or execute option to run it with example data and inspect each node's output. [VERSION]

On the third test, Sipho finds the email says "Dear ," because he left the name field empty. He makes the name field required in his form.

## Common Mistake
Many beginners test once, see it work, turn it on and never check again. Then a changed column name or a disconnected account stops the automation, and enquiries are lost without any warning. Test three times with different example data, including an incomplete entry, and check the results regularly in the first weeks.

## Key Takeaways
1. An automation is a trigger followed by one or more actions, such as "new form entry, then add a row and send an email".
2. Build small, test with example data only, and check the results in every connected app.
3. Free-tier limits, app connections and interfaces for Zapier and n8n change often, so check the current plans before you choose.

## Hands-on Exercise
**Task:** Capstone step 2: build and test one automation for your workflow, for example "new enquiry form entry, then add to a spreadsheet and send a welcome email". Test it 3 times with example data.
**Tools:** Zapier (free tier) or n8n (free self-hosted version or trial); a free online form tool; a free spreadsheet; your email account. [VERSION] [VERIFY]
**Steps:**
1. Choose one automation candidate from your L09 map.
2. Prepare the form, the spreadsheet with matching columns, and your welcome email text (from your L05 onboarding pack).
3. Build the trigger and two actions, following the screen demo steps for your chosen tool.
4. Test 3 times with example data only: one complete entry, one with a long name or unusual characters, and one with a missing field.
5. After each test, check the spreadsheet and the inbox, and fix any problem.
6. Take screenshots of the automation steps and of one successful test result.
7. Write 2 lines: what you would check each week, and what you would do if it failed.
**What good looks like:** A working automation with one trigger and at least two actions, three documented tests with example data, fixes for any problems found, and screenshots as evidence. No real client data was used.
**Time:** about 50 minutes

## Review Flags
- [VERSION] Zapier and n8n interfaces, menu names ("Zap", "workflow", "node", "test", "execute"), trigger and action names, and app connections must be checked against the live tools before the screen demo is recorded.
- [VERSION] Free-tier task limits, number of steps allowed per automation, and available apps on Zapier's and n8n's free options change often and must be confirmed before scripting.
- [VERIFY] Whether n8n can be used free only by self-hosting, and whether its online version offers a free tier or a time-limited trial, must be confirmed.
- [VERIFY] Whether a two-action (multi-step) automation is available on Zapier's free tier must be confirmed; if not, the demo should use one action or n8n.
