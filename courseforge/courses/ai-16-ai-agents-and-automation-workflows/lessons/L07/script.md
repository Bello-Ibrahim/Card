# L07 Routing and Decisions | Presenter Script

Course: AI-16 · Video: 5 min · Words: 685

## Hook
Your workflow can now label every message. But a label is only useful if something happens next. Who sees the urgent complaint? Who answers the simple question? And what happens when the model is not sure?

## Explain
Last time, we made the model return fields we can trust. Now we use them. Routing means sending each item down a different path, based on its data. n8n has two main nodes for this.

The IF node checks one condition, and has two outputs, true and false. The Switch node has several rules, and several outputs. For example, one output each for complaint, question and booking, plus a fallback for anything else.

Remember the key idea from lesson one. The model produces the label. Your workflow makes the decision. That keeps the path predictable, and easy to test.

Before you ask the model, ask yourself: can a simple rule decide this? An email from a known internal address can be routed by sender. A policy number in a fixed format can be found with a pattern. An amount above a limit is just a comparison. Rules are free, instant, and always give the same answer. So put them first, and send only the rest to the model.

Next, plan for uncertainty. Give the model a way to say it is not sure. Add a not sure category, or a confidence field, and route low confidence to a person. But a model's own confidence is only a rough signal, so check it against your test results.

Think of the triage desk in a hospital. Clear cases go straight to the right team. A patient who cannot be assessed quickly is not sent to a random ward. A senior nurse sees them. And some checks follow a fixed rule, and need no discussion.

## Demonstrate
Let's build it. Andrea Santos leads customer care at an insurance company in Manila, the Philippines. Claim messages arrive in English and Filipino. She uses twenty invented messages, and starts from the classification workflow from the last lesson.

First, a rule. Before the model call, she adds an IF node. If a message has a claim number in the standard format and the word status, it goes to an automatic status reply. No AI is needed.

The other messages go to Claude, with five categories: new claim, claim status, complaint, document question, and not sure, plus an urgency field. Then she adds a Switch node on the category, with one output per value, and a fallback.

She connects the outputs. High-urgency complaints go to an urgent complaints tab. Document questions go to a second Claude call that drafts a reply into a drafts tab. Nothing is sent. Not sure items and the fallback both go to review.

She runs all twenty, and checks the count in each tab. One message says: my car was hit, the other driver's insurer says you pay, and I also want to cancel my policy. You'll see something like not sure, so it goes to review. Andrea agrees. It needs a person.

A common mistake is to route on a free-text label, like complaint, urgent, in brackets. A small change in wording breaks the rules, and items fall into no path at all. Route only on values from a closed list, and always connect the fallback to a review tab, so no item is lost.

## Recap
Let's recap. First, use IF for one condition and Switch for several. The model labels the item, and the workflow decides the path. Second, use a plain rule before the model whenever a rule can decide. Third, give the model a not sure option, and send those items, plus any fallback items, to a person.

## CTA
Now it is your turn. In the exercise below this video, you will extend your email workflow so that urgent complaints, simple questions and unclear messages each go to the right place. Then list the decisions a rule could make without AI, and move one of them before the model. It takes about forty-five minutes. In the next lesson, we cover Batches, Loops and Rate Limits. See you there.

## Thumbnail
Headline: Who Handles This Message?
Image: Navy background, one incoming message splitting into four teal paths toward icons for urgent, draft, review and auto-reply, headline in teal Inter Bold.

## Production Notes
- [VERSION] n8n IF and Switch node options (rules mode, fallback output, regular expression conditions) must be checked against the current release.
- Screen recording: the regular expression CL-\d{6} is shown on screen only; the voiceover describes it as 'a claim number in a fixed format'. The not_sure result for the mixed message is an example output.
- Drafted replies are stored in the 'drafts' tab and never sent in this lesson; keep that visible on screen.
- Andrea Santos and her Manila insurance company are fictional; all 20 claim messages are invented.
