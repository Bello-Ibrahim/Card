# L11 Designing an AI Governance Framework

Course: AI-30 · Module: M3 · Objectives: O2, O6 · Video: 5 min

## Hook
You now know the laws. But knowing the rules does not tell a product manager on a Tuesday afternoon who must approve her new AI tool. A framework turns legal knowledge into daily decisions: who approves what, and at which stage.

## Explanation
This lesson is educational and is not legal advice. It shows one practical design; your organisation's size and legal position will change the details.

A practical framework uses the six building blocks from L01 and gives each one an owner.

**Roles.**
- **Accountable executive:** a senior leader who owns AI risk and approves high-risk uses.
- **AI governance group:** a small group from legal, privacy, security, risk, technology and the business. It reviews new systems and sets standards.
- **Data protection officer (DPO):** advises on data protection, reviews DPIAs and monitors compliance. The DPO advises and checks, but does not own the business decision.
- **System owners:** the business leaders responsible for each AI system day to day.

**Principles.** A short list, for example: lawful, human oversight, fairness, transparency, privacy and security, accountability.

**Inventory and risk assessment.** Every system is recorded (L12), classified (L05) and assessed (L10).

**Lifecycle controls.** The approval path follows the lifecycle from L06: intake, classification, assessment, approval, launch, monitoring, retirement. Higher-risk systems pass more gates.

**Monitoring.** Regular checks, incident handling and an annual review (L14).

**Voluntary frameworks.** You do not need to design everything from nothing. Two widely referenced voluntary frameworks can give structure: **ISO/IEC 42001**, a management system standard for AI, and the **NIST AI Risk Management Framework**, organised around functions for governing, mapping, measuring and managing AI risk [VERIFY] [VERSION]. Neither is a legal requirement in the EU or Nigeria. They can help you organise your work and show good practice, but following them does not by itself prove legal compliance [VERIFY]. Check the current names, editions and content before relying on them [VERIFY] [VERSION].

**Analogy:** A framework is like the flight procedures at an airport. Pilots, air traffic control, ground staff and safety inspectors each have a defined role, and a plane passes the same checks in the same order before take-off. Nobody invents the process for each flight.

## Worked Example
**The capstone sample organisation.** From this lesson onward, you will work with **Velmora Tradeways Ltd**, a fictional logistics and trade-payments company. The name is invented for this course. Velmora has about 600 staff, offices in Rotterdam (the Netherlands) and Lagos (Nigeria), and customers in both regions. It acts as a controller for customer and staff data under the GDPR and the NDPA.

Velmora uses or plans these AI systems:

1. A **CV-screening tool** bought from a vendor, used by HR in both offices.
2. A **customer chatbot** on its website and mobile app.
3. A **translation tool** used by staff for emails and documents.
4. A **route-planning model** built in-house for delivery vans.
5. A **credit-risk model** built in-house that scores small business customers, including sole traders, for trade-payment terms.
6. A proposed **driver-monitoring camera** that detects signs of tiredness.

Olumide Bankole, Velmora's new Head of Risk, designs this approval path:

- **Intake:** the system owner registers the idea in the AI inventory.
- **Classification:** the governance group classifies it under the EU AI Act and checks whether personal data is involved.
- **Assessment:** DPIA and, where needed, an AI Act assessment, reviewed by the DPO.
- **Approval:** minimal-risk systems are approved by the governance group; high-risk systems also need the accountable executive's approval.
- **Launch and monitoring:** the system owner runs the agreed checks and reports to the group.

## Common Mistake
Many organisations make the DPO the owner of every AI decision. This creates a conflict: the DPO must be able to advise and check independently, which is hard if they also approved the system [VERIFY] [REGION]. Keep business ownership with system owners and the accountable executive, and keep the DPO in an advisory and monitoring role.

## Key Takeaways
1. A practical framework has named roles, principles, an inventory, risk assessment, lifecycle controls and monitoring.
2. ISO/IEC 42001 and the NIST AI RMF are voluntary frameworks that can give structure, but they are not legal requirements.
3. Approval gates should match risk: higher-risk systems pass more gates and need more senior approval; this lesson is educational, not legal advice.

## Hands-on Exercise
**Task:** Draw a one-page framework diagram for the capstone sample organisation, showing who approves a new AI system and at which stage.
**Tools:** Paper, a free diagram tool or a slide tool; the Velmora Tradeways description above.
**Steps:**
1. Draw the lifecycle stages from intake to retirement as a line of boxes.
2. Under each stage, write the responsible role and the record it produces, such as "classification note" or "DPIA".
3. Show two approval routes: one for minimal-risk systems and one for high-risk systems.
4. Mark where the DPO advises and where the accountable executive decides.
5. Test your diagram by tracing the proposed driver-monitoring camera through it.
**What good looks like:** A clear one-page diagram with roles, records and two approval routes, and a short note on how the driver-monitoring camera would pass through it.
**Time:** about 25 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [VERSION] Names, editions and content of ISO/IEC 42001 and the NIST AI Risk Management Framework must be checked; they are described as voluntary frameworks, not legal requirements (curriculum flag).
- [VERIFY] The statement that following voluntary frameworks does not by itself prove legal compliance must be confirmed by the legal reviewer.
- [VERIFY] [REGION] The DPO independence and conflict-of-interest point must be checked under the GDPR and the NDPA.
- [VERIFY] The name "Velmora Tradeways Ltd" must be checked against company registers in the EU, Nigeria and the UK so it does not match a real company.
