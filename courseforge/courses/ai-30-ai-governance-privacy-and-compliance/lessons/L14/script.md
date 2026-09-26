# L14 Accountability, Monitoring and Finalising Your Framework | Presenter Script

Course: AI-30 · Video: 5 min · Words: 685

## Hook
It is Friday evening. A customer reports that your chatbot showed them another customer's address and phone number. Who is called first? Who decides whether to notify a regulator? If you need to invent the answers tonight, your framework is not finished.

## Explain
Welcome to the final lesson. Last time, you drafted Velmora's policy. Today, we finish the framework with accountability, monitoring and incident response. A final reminder: this course is educational and is not legal advice, and notification duties differ between laws, so always check them.

Accountability means being able to show compliance, not only to claim it. It rests on records: decisions, such as classification notes and approvals; assessments and residual-risk judgements; training records; audits and reviews; and incident logs, including incidents you did not report. If it is not recorded, you cannot show it.

Monitoring checks that systems keep working as expected after launch. Models drift as the world changes, vendors update tools and staff find new uses. So check performance and error rates for different groups, review complaints and human-review outcomes, watch vendor changes, and review the inventory and risk register regularly.

An incident process has five steps. First, detect and report: how staff and customers report problems, and to whom. Second, contain: who can pause or switch off a system, and how fast. Third, assess: is personal data involved, or is it a serious incident with a high-risk AI system? Both can apply.

Fourth, notify: decide with the data protection officer and legal team whether to notify regulators and affected people, within the legal time limits under each law. Providers and deployers of high-risk systems may have separate reporting duties. Fifth, recover and learn: fix the cause and update the risk register.

Think of a ship's logbook. It does not steer the ship, but after a storm it shows what the crew saw, what they decided and why. Monitoring is the crew watching the weather. And the incident process is the emergency drill everyone practised before the storm.

## Demonstrate
Ngozi Eze is the incident manager at Velmora, and the chatbot incident from the start of this lesson happens. In the first hour, the chatbot owner switches it to hand over every conversation to a human, and informs the vendor.

Assess: a name, address and phone number were shown, so this is a personal data breach. The affected customer lives in Nigeria, and the viewing customer in the Netherlands. The data protection officer checks whether it must be reported under the NDPA, the GDPR or both, and within which time limits.

Notify: the officer judges that the breach is likely to create a risk to the affected person, and recommends notifying the relevant regulator or regulators and the customer, with advice from counsel. Every step, time and decision is logged, including the reasons.

Learn: the cause is a session error in a vendor update. So Velmora adds a new register risk, vendor updates change chatbot behaviour without testing, with a new control that requires test results before any update goes live.

A common mistake is to log only the incidents you report. Log near misses too, and the incidents you decided not to report, with the reason. An empty log does not show that nothing happened. It may show that nobody was watching. So agree the roles and the log before anything goes wrong.

## Recap
Let's recap. First, accountability means showing compliance with records: decisions, assessments, training, audits and incident logs. Second, monitoring checks that systems keep working, and an incident process says who contains, assesses and decides on notification. Third, notification duties differ by law and must always be checked.

## CTA
Now for capstone step three. Add a monitoring and incident section to your policy, add at least one incident risk to your register, and check both against the rubric. Add the disclaimer line from the rubric to both documents. Then submit both.

Congratulations on finishing AI Governance, Privacy and Compliance. You can now map the laws, classify AI systems, assess risks and build a framework. Submit your capstone. It has been a pleasure learning with you, and well done.

## Thumbnail
Headline: When Something Goes Wrong
Image: Navy background, a chat bubble with a red warning icon next to an open logbook with a teal pen, headline in teal Inter Bold.

## Production Notes
- Legal/compliance reviewer sign-off required before release.
- Disclaimer spoken once in scene 2 (educational, not legal advice).
- [VERIFY] [REGION] Notification duties: content.md placeholders [the GDPR breach notification articles], [the NDPA breach section], [the EU AI Act serious-incident article] and [the statutory deadlines]. No notification deadline is spoken or shown; scene 6 says only within the legal time limits under each law.
- [VERIFY] [REGION] Serious-incident reporting duties for providers and deployers of high-risk systems (scene 6) must be checked.
- [VERIFY] [REGION] The notification judgement in the worked example (scenes 9 and 10), including whether the NDPA, the GDPR or both apply, must be confirmed by the legal reviewer. No regulator is named.
- [VERIFY] Fictional organisation: Velmora Tradeways Ltd must be checked so it does not match a real company (see L11). Ngozi Eze is fictional. The first-hour containment is Velmora's own fictional procedure, not a legal deadline.
- No screen demos. The incident steps are shown on slides; the updated risk register row is shown on a slide (scene 11).
- Capstone step 3 and submission are set in this lesson's exercise; the rubric is on the lesson page.
