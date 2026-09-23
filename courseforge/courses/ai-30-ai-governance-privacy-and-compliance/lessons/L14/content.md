# L14 Accountability, Monitoring and Finalising Your Framework

Course: AI-30 · Module: M3 · Objectives: O5, O6 · Video: 5 min

## Hook
It is Friday evening. A customer reports that your chatbot showed them another customer's delivery address and phone number. Who is called first? Who decides whether to notify a regulator, and how quickly? If you need to invent the answers tonight, your framework is not finished.

## Explanation
This lesson is educational and is not legal advice. Notification duties and deadlines differ between laws and must be checked in [the GDPR breach notification articles], [the NDPA breach section] and [the EU AI Act serious-incident article] [VERIFY] [REGION].

**Accountability** means being able to show compliance, not only to claim it. It rests on records:

- **Decisions:** classification notes, approvals and the reasons for them.
- **Assessments:** DPIAs, AI Act assessments and residual-risk judgements.
- **Training:** who was trained, on what, and when.
- **Audits and reviews:** internal checks, findings and follow-up.
- **Incident logs:** every incident, including those not reported to a regulator, with the reasoning.

**Monitoring** checks that AI systems keep working as expected after launch. Models can drift as the world changes, vendors update tools, and staff find new uses. Practical monitoring includes:

- performance and error-rate checks, including for different groups of people;
- review of complaints and human-review outcomes (L09);
- vendor change notices and contract reviews;
- regular review of the inventory and the risk register (L12).

**Incident response.** An AI incident process should say:

1. **Detect and report:** how staff and customers report problems, and to whom.
2. **Contain:** who can pause or switch off a system, and how fast.
3. **Assess:** is personal data involved (a possible personal data breach)? Is it a high-risk AI system with a possible serious incident? Both can apply.
4. **Notify:** decide, with the DPO and legal team, whether to notify regulators and affected people, within [the statutory deadlines] under each law [VERIFY] [REGION]. Providers and deployers of high-risk systems may have separate duties to report serious incidents [VERIFY] [REGION].
5. **Recover and learn:** fix the cause, update the risk register and record the lessons.

**Analogy:** Accountability records are like a ship's logbook. The logbook does not steer the ship, but after a storm it shows what the crew saw, what they decided and why. Monitoring is the crew watching the weather. The incident process is the emergency drill that everyone practised before the storm.

## Worked Example
Ngozi Eze is the incident manager at Velmora Tradeways Ltd, the fictional capstone organisation. The chatbot incident from the Hook happens.

- **Contain (first hour):** the chatbot owner switches the chatbot to "handover to human" mode. The vendor is informed.
- **Assess:** another customer's name, address and phone number were shown. This is a personal data breach. The affected customer lives in Nigeria, and the viewing customer in the Netherlands. The DPO checks whether the breach must be reported under the NDPA, the GDPR or both, and within which deadlines [VERIFY] [REGION].
- **Notify:** the DPO judges that the breach is likely to create a risk to the affected person and recommends notifying the relevant regulator or regulators and the affected customer, with legal advice [VERIFY] [REGION].
- **Learn:** the cause is a session error in a vendor update. Velmora adds a register risk: "Vendor updates change chatbot behaviour without testing", with a new control requiring test results before updates go live.
- **Record:** every step, time and decision is logged, including the reasons.

## Common Mistake
Many teams log only incidents they report to regulators. A good incident log includes near misses and incidents you decided not to report, with the reason. If a regulator later asks why you did not notify, the recorded reasoning at the time is your evidence. An empty log does not show that nothing happened; it may show that nobody was watching.

## Key Takeaways
1. Accountability means showing compliance with records: decisions, assessments, training, audits and incident logs.
2. Monitoring checks that systems keep working as expected, and an incident process says who contains, assesses and decides on notification.
3. Breach and serious-incident notification duties differ by law and must be checked; this course is educational, not legal advice.

## Hands-on Exercise
**Task:** Capstone step 3: add a monitoring and incident-response section to your policy, review your risk register against the rubric, and submit both documents.
**Tools:** Your policy from L13 and your inventory and risk register from L12; the capstone rubric; a word processor and spreadsheet.
**Steps:**
1. Write section 10 of your policy, "Monitoring and incidents", covering monitoring checks, the five incident steps and who decides on notification.
2. Use placeholders for all notification deadlines, such as "[GDPR breach deadline]".
3. Add at least one incident-related risk to your register.
4. Check your policy and register against each rubric criterion, and fix any gaps.
5. Confirm every legal reference is a placeholder or has been checked, and add the line "This document is an educational exercise and is not legal advice."
6. Submit both documents.
**What good looks like:** A complete policy with a practical section 10, a register of at least 7 risks with owners, controls and review dates, and a self-check against every rubric criterion.
**Time:** about 60 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [REGION] Personal data breach notification duties and deadlines under the GDPR and the NDPA, and serious-incident reporting under the EU AI Act, must be checked (curriculum flag).
- [VERIFY] [REGION] The notification judgement in the worked example must be confirmed by the legal reviewer.
- Fictional organisation: "Velmora Tradeways Ltd" must be checked so it does not match a real company (see L11).
