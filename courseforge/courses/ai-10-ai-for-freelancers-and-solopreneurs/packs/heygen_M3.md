# HeyGen Batch Pack: AI-10 M3 (Automate and Build Your Workflow)

Course: AI for Freelancers and Solopreneurs. Make one HeyGen video per lesson below, using these settings for every video.

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

## L09 Mapping Your Client Workflow

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_M3_L09_presenter.mp4`
- **Expected length:** about 5.0 minutes (695 words). The quality gate accepts ±10%.

```text
Could you describe, step by step, what happens between a new enquiry and a paid invoice? For most freelancers, the steps live in their head. But you cannot improve, or automate, a process you have never written down.

Welcome to week three. Last week, you built templates and rules. Now you connect them into one workflow, and this is where your capstone begins.

A workflow map is a simple list of every step in your client process, in order, from first contact to final invoice. For each step, you write who does it, what tool you use, how long it takes, and how often it happens.

Then you give each step one of three labels. AI draft, where AI writes a first version and you finish it, like a proposal. Automation, where a tool follows fixed rules without you, like copying form answers into a spreadsheet. And human only, for steps that need judgement, trust or expertise, like a discovery call or a pricing decision.

Good automation candidates pass three tests. They are repeated, so they happen for every client. They are rule-based, so the same input always leads to the same action. And they are low risk, so a mistake is easy to notice and fix. If a step needs you to think or be personal, do not automate it.

Think of the route you drive to work every day. You know the way without thinking, so you never notice the slow junction or the extra turn. When you draw it on paper, you suddenly see where you lose time, and where a shortcut is possible.

Under your map, add two lines. Automation candidate one, and automation candidate two. For each, write the trigger, which is what starts it, and the action, which is what should happen next. You will build one of them in the next lesson.

And describe steps in general terms. Do not put real client names or personal details into a map you will share or paste into AI.

Let's see a real map. Meera is a freelance interior designer in Pune, India. She works with home owners on single-room projects. She writes down every step of her process.

An enquiry arrives through her website form, and she copies the details into her client spreadsheet. Then comes the discovery call, which is human only. The proposal from her call notes is an AI draft. So is the welcome email with her questionnaire.

The design concept and material choices take about eight hours, and they are human only. Weekly progress updates are AI drafts. She checks each invoice herself, using a template. Payment reminders could be automated later.

Steps one and two happen for every enquiry, follow a fixed rule, and are easy to check. So they become her two automation candidates. When a new form entry arrives, add a row to the client spreadsheet. Then send a standard thank-you email. Each one has a clear trigger and a clear action.

The design work and the discovery call stay fully human, because clients hire Meera for her taste and advice. Notice that the longest step, the design work, is not the one she automates. She saves time around her expertise, not in place of it.

A common mistake is to label too many steps as automation, because it sounds efficient. A proposal may be repeated, but it needs your judgement. Automating it would send unchecked work to clients. Start with one or two simple, rule-based steps.

Let's recap. First, a workflow map lists every step from first contact to final invoice, with the tool, time and frequency. Second, label each step AI draft, automation or human only, and give a reason. Third, good automation candidates are repeated, rule-based and low risk. Judgement steps stay human, or become AI drafts that you check.

Now it is your turn, and this is capstone step one. Copy the map template, list ten to fifteen steps for one typical project, and label each one with a reason. Then choose two automation candidates, and write the trigger and the action for each. In the next lesson, you will build your first automation with Zapier or n8n.
```

## L10 Your First Automation with Zapier or n8n

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_M3_L10_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
Every new enquiry means copying a name into a spreadsheet, and sending the same thank-you email. Imagine it happening by itself, correctly, while you sleep. Today, you will build that.

In the last lesson, you chose two automation candidates. Now you will build one, and this is capstone step two.

Every automation has two parts. A trigger, which is the event that starts it, such as a new form entry. And one or more actions, which happen next, such as adding a row to a spreadsheet, sending an email, or creating a task.

Tools such as Zapier and n8n connect your apps, so that a trigger in one app causes actions in others. Zapier runs in your browser. n8n can run online or on your own computer. Their free options, limits and app connections change often, so check the current plans before you choose.

Follow three safety rules. Test with example data, never real client details. Start small, with one trigger and two actions. And check the result every time in the first weeks, because automations can fail silently. Also, connect only accounts you trust, and collect only the data you need.

Think of a row of dominoes. The trigger is your finger pushing the first one. Each action is the next domino falling. If one domino is in the wrong place, the chain stops. So you test the whole row before a client ever touches it.

Let's build one. Sipho is a freelance video editor in Durban, South Africa. His map shows he copies every enquiry into a spreadsheet and sends a thank-you email by hand.

He has a form, a spreadsheet with matching columns, and a short welcome email with a space for the client's name. His plan is simple. New form entry, then add a spreadsheet row, then send a welcome email.

He signs in to Zapier and creates a new automation. For the trigger, he chooses his form app and the event for a new form response, then connects his account.

He submits a test entry in his form, called Test Client One, with his own email address. Then he tests the trigger, and checks that the test entry appears.

Now the first action. He chooses his spreadsheet app and the event to create a row. He picks his spreadsheet and matches each column to a form field. He tests it, and opens the spreadsheet to see the new row.

Then the second action. He chooses his email app, puts the form's email field in the To box, and inserts the name field into his welcome text. He tests it, and checks his own inbox.

He turns the automation on, and submits two more test entries. On the third test, the email says Dear, with no name, because he left the name field empty. So he makes the name field required in his form.

If you choose n8n, the idea is the same. You create a new workflow with a trigger for your form, then a spreadsheet step and an email step in a line. You run it with example data, and inspect each step's output.

A common mistake is to test once, turn it on, and never check again. Then a renamed column or a disconnected account stops it, and enquiries are lost without warning. So test three times with different example data, including an incomplete entry, and check the results regularly in the first weeks.

Let's recap. First, an automation is a trigger followed by one or more actions. Second, build small, test with example data only, and check the results in every connected app. Third, free limits, app connections and interfaces change often, so check the current plans before you choose.

Now it is your turn, with capstone step two. Choose one candidate from your map, and build the trigger and two actions. Test three times with example data only. One complete entry, one with an unusual name, and one with a missing field. Take screenshots as evidence. In the next lesson, we decide what to automate and what to keep human.
```

## L11 What to Automate and What to Keep Human

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (685 words). The quality gate accepts ±10%.

```text
You can now automate a step, and get AI to draft almost anything. So why not automate everything? Because one automatic message at the wrong moment can lose a client. The skill now is not building automations. It is deciding.

Last time, you built and tested your first automation. Now, in capstone step three, you judge every AI and automation step in your workflow.

Ask four questions. First, how often does the task happen? A task that happens once a year is rarely worth the setup and maintenance. A task that happens for every client, every week, is a stronger candidate.

Second, what happens if it goes wrong? Rate the damage as low, like a small delay you can fix. Medium, like confusion or extra work. Or high, like a lost client, a wrong figure in advice, or a privacy problem. The higher the risk, the more human checking you need.

Third, does the client expect a personal touch? Confirmations and reminders can be automatic. But advice, bad news, apologies and negotiations should come from you. Fourth, what does it cost? Count the tool price, setup time, checking time, and the risk of sharing client data with another service.

The checklist gives one of three decisions. Keep the step as it is. Change it, for example from automation to an AI draft that you check. Or remove it, and do the task by hand. Then write a one-line reason. That reason makes your workflow trustworthy, both to you and to a client who asks how you work.

Think of a washing machine. It is excellent for the weekly laundry. But you would not put your best silk shirt, or a child's drawing, in it. The machine is not bad. Some things simply need careful hands.

Let's see the checklist at work. Chidi is a freelance accountant in Enugu, Nigeria. He serves about thirty small business clients, and he checks three steps in his workflow.

First, appointment reminders, sent the day before each meeting. They happen many times a week. The risk is low, because the meeting is also in the client's calendar. No personal touch is expected, and it runs on a free option he already uses. Decision, keep as automation.

Second, advice messages, such as what a client should do about a tax question. The risk is high, because wrong advice could cost the client money. And clients expect Chidi's own judgement. Decision, keep fully human. He may use AI only to tidy wording he has already written, with names and figures removed.

Third, monthly summary notes for each client. The risk is medium to high, and clients expect a partly personal touch. Decision, change. It was an AI draft sent automatically. Now it is an AI draft from anonymised figures, checked and sent by Chidi himself.

His workflow is now faster where it is safe, and personal where it matters. He did not remove automation from his business. He put each step in the right place, and he can explain why to any client who asks.

A common mistake is to judge only by time saved. It saves twenty minutes, so I will automate it. This forgets the cost of setup, maintenance and mistakes, and the value of personal contact. But a step that sometimes sends a wrong or cold message to an important client is not a saving. Always ask all four questions.

Let's recap. First, judge each AI or automation step with four questions. How often, what if it goes wrong, is a personal touch expected, and what does it cost in money, time and risk. Second, repeated, low-risk, impersonal steps suit automation, while advice, bad news and high-risk work stay human. Third, decide to keep, change or remove each step, and write a reason.

Now it is your turn, with capstone step three. Add the four questions as columns in your workflow map, and answer them for every AI and automation step. Decide keep, change or remove, with a reason, and name a human check for every high-risk step. In the final lesson, we put together your complete proposal-to-invoice workflow.
```

## L12 Your Complete Proposal-to-Invoice Workflow

- **Filename:** `ai-10-ai-for-freelancers-and-solopreneurs_M3_L12_presenter.mp4`
- **Expected length:** about 4.8 minutes (671 words). The quality gate accepts ±10%.

```text
Over three weeks, you have built a proposal template, an onboarding pack, prompt templates, a policy, an invoice template and an automation. Separately, they are useful tools. Together, in one documented workflow, they become a system for taking on more work without longer hours.

Last time, you judged every step in your workflow. In this final lesson, you bring everything together, and prepare your capstone.

Your capstone is one workflow document with seven parts, and each part links to something you already made. Your workflow map. Your proposal template. Your onboarding pack. Your delivery prompt templates. Your quality checks and AI-use policy. Your automation, with test results. And your invoice template and payment reminder.

Start with one folder and one overview page. On your map, name the template, prompt or automation that each step uses. That way, anyone reading it can follow your process from start to finish.

Then you run one test client through the whole workflow, from proposal to invoice. Use a real client only if they agree, or a realistic example. For every step, record what you did, how long it took and what went wrong. A workflow only proves itself when it is used.

Finally, you evaluate. Which steps worked well, which need changing, and what would you do differently? This is the same keep, change or remove thinking from the last lesson, now based on real evidence.

Three final reminders. Keep confidential client information out of AI tools during the test. AI drafts of contracts, invoices and tax material are not legal or tax advice. And check your tool plans and settings before you rely on them, because they change.

Documenting your workflow is like writing down a family recipe you have cooked from memory for years. Once it is on paper, you can repeat it every time, notice where it can be better, and even hand it to a helper in the future.

Let's see a test run. Yuki is a freelance UX writer in Osaka, Japan. She writes app and website text for small software companies. She builds her workflow in one shared folder, and runs an example client through it, a small language-learning app.

For the proposal, her template and an AI draft from example call notes take twenty-five minutes. Her promise check replaces copy for all app screens with up to twenty screens. At onboarding, the enquiry form triggers her automation, which adds a spreadsheet row and sends her welcome email.

For delivery, her prompt template produces first drafts from anonymised notes, and she rewrites the key messages herself and runs her quality checklist. For the invoice, she fills her template, and notes which tax points she has confirmed with an official source.

Her evaluation finds one problem. The automation sent the full welcome email before she had read the enquiry, so a poor-fit enquiry got a warm welcome. She changes the action to a short thank-you, saying she will reply personally within one working day. The full welcome now comes after the discovery call.

A common mistake is to submit a folder of separate templates and call it a workflow. Without the map that links them, and a real test run, there is no evidence the parts work together. Record the problems honestly, and show what you changed.

Let's recap. First, your workflow document links seven parts, from the map to the invoice. Second, running one test client from proposal to invoice proves the workflow works, and shows you what to fix. Third, evaluate each step with evidence, keep confidential data out of AI tools, and keep legal and tax decisions in qualified hands.

Congratulations. You have finished AI for Freelancers and Solopreneurs. You started with a list of tasks from one week. Now you have a tested system. Now complete capstone step four. Build your folder and overview page, run your test client from proposal to invoice, and write your evaluation. Check your work against the rubric and the submission checklist, then submit your capstone. Well done, and good luck.
```
