# L07 Routing and Decisions

Course: AI-16 · Module: M2 · Objectives: O2, O3 · Video: 5 min (screen demo)

## Hook
Your workflow can now label every message. But a label is only useful if something happens next. Who sees the urgent complaint? Who answers the simple question? And what happens when the model is not sure?

## Explanation
**Routing** means sending each item down a different path based on its data. n8n has two main nodes for this [VERSION]:

- **IF:** one condition, two outputs (true and false). Example: `valid` is true.
- **Switch:** several rules or values, several outputs. Example: one output each for "complaint", "question", "booking" and a fallback output for anything else.

The model produces the label; your workflow makes the decision. This keeps the path predictable and easy to test, as in L01.

**Use a rule when a rule is enough.** Before you ask the model, ask yourself if a simple condition already answers the question. Examples:

- An email from a known internal address: route by sender, no AI needed.
- A message that contains a policy number in a fixed format: extract it with a regular expression.
- An amount above a limit: compare numbers, as in L04.

Rules are free, instant and always give the same answer. Put them first, and send only the remaining items to the model. This saves cost and reduces the number of places where the model can be wrong.

**Plan for uncertainty.** Some items are hard for the model and for people. Give the model a way to say so:

- Add a `"not_sure"` value to the category list, and tell the model to use it when the message is unclear or fits several categories.
- Or add a `confidence` field ("high", "medium", "low") and route "low" to a person. A model's own confidence is only a rough signal, so check it against your test results before you rely on it.

Items marked "not sure" go to a **review tab** that a person checks every day. This is much safer than forcing every item into a category.

**Analogy:** Routing is like the triage desk in a hospital emergency department. Clear cases go straight to the right team. A patient who cannot be assessed quickly is not sent to a random ward; a senior nurse sees them. And some checks, such as "is the patient breathing?", follow a fixed rule and need no discussion.

## Worked Example
Andrea Santos leads customer care at a hypothetical insurance company in Manila, the Philippines. Claim messages arrive in English and Filipino. She uses 20 invented messages. On screen, she:

1. Starts from the L06 classification workflow.
2. Before the model call, adds an **IF** node: if the message contains a claim number that matches `CL-\d{6}` and the word "status", route it to an "auto status reply" path. No AI is needed for these. [VERSION]
3. Sends the other items to Claude with categories `claim_new`, `claim_status`, `complaint`, `document_question` and `not_sure`, and an `urgency` field.
4. Adds a **Switch** node on `category` with one output per value and a fallback output. [VERSION]
5. Connects outputs: `complaint` with high urgency to the "urgent_complaints" tab; `document_question` to a second Claude call that drafts a reply into a "drafts" tab (not sent); `not_sure` and the fallback to "review".
6. Runs the 20 messages and checks the counts in each tab.

One message says, "My car was hit, the other driver's insurer says you pay, and I also want to cancel my policy." The model returns `not_sure`, and it goes to review. Andrea thinks that is correct: it needs a person.

## Common Mistake
Learners often send every item to the model, even when a rule would be enough, and then route on a free-text label such as "Complaint (urgent)". A small change in wording breaks the Switch rules, and items fall into no path at all. Put simple rules first, route only on values from a closed list, and always connect the fallback output to a review tab so no item is lost.

## Key Takeaways
1. Use IF for one condition and Switch for several; the model labels the item, and the workflow decides the path.
2. Use a plain rule before the model whenever a rule can decide; it is cheaper, faster and fully predictable.
3. Give the model a "not sure" option or a confidence field, and send those items, plus any fallback items, to a person.

## Hands-on Exercise
**Task:** Extend your email workflow so that urgent complaints go to one sheet, simple questions get a drafted reply, and "not sure" items go to a review tab. Write down which decisions a rule could make without AI.
**Tools:** n8n self-hosted; Google Sheets; Claude API (keep the run small).
**Steps:**
1. Add `not_sure` to your allowed categories and update the validation code from L06.
2. Add a Switch node on `category`, with a fallback output. [VERSION]
3. Route high-urgency complaints to "urgent_complaints".
4. Route simple questions to a second Claude call that drafts a short reply into a "drafts" tab. Do not send anything.
5. Route `not_sure` and fallback items to "review".
6. Run on your 10 emails plus 3 new, deliberately unclear ones.
7. List at least two decisions in your workflow that a rule could make without AI, and move one of them before the model call.
**What good looks like:** Every email ends in exactly one tab, unclear emails reach "review", drafts are stored and not sent, and at least one decision now uses a rule instead of the model.
**Time:** about 45 minutes

## Review Flags
- [VERSION] n8n IF and Switch node options (rules mode, fallback output, regular expression conditions) must be checked against the current release.
