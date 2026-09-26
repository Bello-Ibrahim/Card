# HeyGen Batch Pack: AI-30 M3 (Building Your AI Governance Framework)

Course: AI Governance, Privacy and Compliance. Make one HeyGen video per lesson below, using these settings for every video.

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

## L11 Designing an AI Governance Framework

- **Filename:** `ai-30-ai-governance-privacy-and-compliance_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (664 words). The quality gate accepts ±10%.

```text
You now know the laws. But knowing the rules does not tell a product manager on a Tuesday afternoon who must approve her new AI tool. A framework turns legal knowledge into daily decisions: who approves what, and at which stage.

Welcome to module three, where we build your framework. As always, this course is educational and is not legal advice. Today's design is one practical example. Your organisation's size and legal position will change the details.

A practical framework uses the six building blocks from lesson one, and gives each one an owner. Start with roles. The accountable executive is a senior leader who owns AI risk and approves high-risk uses. The AI governance group brings together legal, privacy, security, risk, technology and the business, to review new systems and set standards.

The data protection officer advises on data protection, reviews DPIAs and monitors compliance, but does not own the business decision. And system owners are the business leaders responsible for each AI system, day to day.

Next come a short list of principles, then an inventory where every system is recorded, classified and assessed, as we practised in modules one and two. Monitoring covers regular checks, incident handling and a yearly review.

Lifecycle controls tie it together. The approval path follows the lifecycle: intake, classification, assessment, approval, launch, monitoring and retirement. Higher-risk systems pass more gates.

You do not need to design everything from nothing. Voluntary frameworks, such as an international management system standard for AI and a widely used AI risk management framework, can give structure. But neither is a legal requirement, and following them does not by itself prove compliance.

Think of flight procedures at an airport. Pilots, air traffic control, ground staff and safety inspectors each have a defined role, and every plane passes the same checks in the same order before take-off. Nobody invents the process for each flight.

From now on, your capstone uses one sample organisation: Velmora Tradeways Limited, a fictional logistics and trade-payments company. It has about six hundred staff, offices in Rotterdam and Lagos, and customers in both regions. It is a controller under the GDPR and the NDPA.

Velmora uses or plans six AI systems: a CV-screening tool bought from a vendor, a customer chatbot, a translation tool for staff, and a route-planning model built in-house.

It also has an in-house credit-risk model that scores small business customers for payment terms, and a proposed driver-monitoring camera that detects signs of tiredness. Notice that these systems range from minimal risk to possibly high-risk.

Olumide Bankole, Velmora's new Head of Risk, designs the approval path. At intake, the system owner registers the idea in the AI inventory. Then the governance group classifies it under the AI Act, and checks whether personal data is involved.

Next comes a DPIA and, where needed, an AI Act assessment, reviewed by the data protection officer. Minimal-risk systems are approved by the governance group. High-risk systems also need the accountable executive. After launch, the system owner runs the agreed checks and reports to the group.

A common mistake is to make the data protection officer the owner of every AI decision. That creates a conflict, because the officer must advise and check independently. Keep business ownership with system owners and the executive, and keep the officer in an advisory and monitoring role.

Let's recap. First, a practical framework has named roles, principles, an inventory, risk assessment, lifecycle controls and monitoring. Second, voluntary frameworks can give structure, but they are not legal requirements. Third, approval gates should match risk: higher-risk systems pass more gates and need more senior approval.

In the exercise below this video, you will draw a one-page framework diagram for Velmora, showing who approves a new AI system and at which stage. Then test it by tracing the driver-monitoring camera through your diagram.

Velmora is the centre of your capstone. In the next lesson, you start it by building an AI inventory and risk register. See you there.
```

## L12 Building an AI Inventory and Risk Register

- **Filename:** `ai-30-ai-governance-privacy-and-compliance_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (688 words). The quality gate accepts ±10%.

```text
A regulator asks: which AI systems do you use, and what are their main risks? If the answer takes three weeks and ten emails, your governance is not working. Two simple documents let you answer in minutes.

Last time, we met Velmora Tradeways and designed its approval path. Today, we build its two core records: an AI inventory and a risk register. This lesson is educational and is not legal advice. The classifications you record are your own judgements, and qualified advisers should review them.

The AI inventory lists every AI system in use or in development, one row per system. Useful columns are the system, its owner, its purpose, the personal data used, its role and tier under the AI Act, its role under the GDPR and the NDPA, and the assessments done. It answers the question, what do we have?

The risk register records the risks those systems create, one row per risk. Its columns are the risk, the AI system, likelihood, impact, owner, control and review date. For this course, add one more column, laws, to show whether each risk connects to the AI Act, the GDPR, the NDPA, or several.

Some practical rules. Write each risk as cause, event and effect. For example, biased training data leads the tool to rank some groups lower, so qualified candidates are rejected unfairly. A risk written as one word, like bias, cannot be managed.

Use a simple scale, such as one to five for likelihood and impact, and define what each number means. Name one owner per risk: a role that can act, not a committee. Write only the controls that actually exist today, and mark planned ones as planned. And set review dates by risk level.

Think of a hospital. The inventory is the list of rooms and equipment. The risk register is the list of what could go wrong in each room, who is responsible and what protects patients. You need the first list to write the second.

Let's see two entries. Priya Raman is the privacy analyst at Velmora. She starts with two rows in the inventory.

The CV-screening tool is owned by the Head of HR, ranks applicants and uses CVs and application data. Velmora is the deployer of a likely high-risk system, and a controller under both data protection laws. No DPIA is done yet. The translation tool is owned by the Head of IT, may contain personal data, and is likely minimal risk.

Her first register entry: the CV tool ranks candidates from some groups lower, because of patterns in past hiring data, which leads to unfair rejection. Likelihood three, impact five, owned by the Head of HR. Planned controls include vendor bias-test results, recruiter review of every rejection and a DPIA. It is reviewed every three months, and maps to all three laws.

Her second entry: staff paste confidential contracts containing personal data into the translation tool, and the vendor stores or reuses them. Likelihood three, impact four, owned by the Head of IT. Controls include a no-training contract term, a data processing agreement, staff guidance and a transfer check. It maps to the GDPR and the NDPA.

Priya notices something. The translation tool is minimal risk under the AI Act, yet it carries a real data protection risk. Tier and risk level are not the same thing. And a common mistake is to build the register once for an audit, and never update it. Keep it working.

Let's recap. First, the AI inventory lists every AI system with its owner, purpose, data, role under each law and risk tier. Second, the risk register records each risk with likelihood, impact, owner, control, review date and the relevant laws. Third, a low AI Act tier does not mean low data protection risk.

Now for capstone step one. In the exercise below this video, you will build an inventory of all six Velmora systems, and a register of at least six risks across at least four systems, each mapped to the relevant laws. Keep every detail fictional.

In the next lesson, capstone step two: drafting the AI governance policy. See you there.
```

## L13 Drafting the AI Governance Policy

- **Filename:** `ai-30-ai-governance-privacy-and-compliance_M3_L13_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
An AI tool can write a ten-page AI policy in less than a minute. It will look professional. It may also cite laws incorrectly and invent duties. Your job is not to generate the policy. Your job is to make it true.

Last time, you built Velmora's inventory and risk register. Today, we draft its policy. This course is educational and is not legal advice, so any policy you draft here is a learning exercise that qualified advisers must review before real use.

A good AI governance policy is short, specific and usable. It tells staff what they must do, not only what the organisation believes. Each section should fit your organisation's real facts. Here is an outline with eleven sections.

It starts with purpose and scope, covering built, bought and embedded AI. Then definitions, principles, and roles and responsibilities. Then the approval process, with its lifecycle gates, and acceptable and prohibited uses, including uses banned by law and uses the organisation bans by choice.

Next come personal data rules, including a clear rule never to paste personal or confidential data into unapproved AI tools. Then assessment triggers, training, monitoring and incidents, which you will add next lesson, and finally the review cycle and ownership.

Claude can speed up a first draft of a section. Here is a safe approach. Give it the outline, a template's structure and fictional facts only. Ask for plain-language clauses, with placeholders instead of legal references or deadlines. Then check every clause yourself, and mark what you changed and why.

For example, you might ask it to draft the roles section for a fictional logistics company in the Netherlands and Nigeria, in short, plain clauses, with a placeholder wherever a legal reference would appear, and without inventing legal requirements.

Think of an AI draft as a junior colleague's work on their first day. It saves time and gives you a structure, but you would never send it to the board without reading every line and correcting what they could not know.

Diego Álvarez is legal counsel at Velmora. He uses Claude to draft section six, acceptable and prohibited uses. The draft is clear and well organised. Then he reviews it, clause by clause.

He keeps a clause allowing staff to use approved AI tools for internal drafts, if a person reviews the output. He changes a clause that said staff must get consent before using AI on customer data. Consent is not always the right basis, so the new clause requires a documented lawful basis, confirmed by the data protection officer.

He removes a specific article number the draft had cited, and replaces it with a placeholder that points to the legal register. And he adds a Velmora rule banning use of the driver-monitoring camera for performance ratings, which the AI could not know about.

His change log shows fourteen clauses drafted: six kept, five changed, two removed and one added. That record shows his professional judgement, and it gives reviewers a clear trail to follow.

A common mistake is to check an AI-drafted policy only for style and grammar. The dangerous errors are in the substance. A policy that describes processes that do not exist is worse than no policy, because it records promises you do not keep. Check every clause against the law and the facts.

Let's recap. First, a good policy covers scope, principles, roles, approval, acceptable and prohibited uses, personal data rules, assessment triggers, training and review. Second, Claude can produce a useful first draft from fictional facts and a template, but never paste in personal or confidential data. Third, a person must check every AI-drafted clause against the law and the facts.

Now for capstone step two. In the exercise below this video, you will draft a two to three page policy for Velmora, using the outline. Ask Claude for a first draft of at least one section, then track every change and write a short change log. Use placeholders for all legal references.

In the final lesson, we cover accountability, monitoring and finalising your framework. See you there.
```

## L14 Accountability, Monitoring and Finalising Your Framework

- **Filename:** `ai-30-ai-governance-privacy-and-compliance_M3_L14_presenter.mp4`
- **Expected length:** about 4.9 minutes (681 words). The quality gate accepts ±10%.

```text
It is Friday evening. A customer reports that your chatbot showed them another customer's address and phone number. Who is called first? Who decides whether to notify a regulator? If you need to invent the answers tonight, your framework is not finished.

Welcome to the final lesson. Last time, you drafted Velmora's policy. Today, we finish the framework with accountability, monitoring and incident response. A final reminder: this course is educational and is not legal advice, and notification duties differ between laws, so always check them.

Accountability means being able to show compliance, not only to claim it. It rests on records: decisions, such as classification notes and approvals; assessments and residual-risk judgements; training records; audits and reviews; and incident logs, including incidents you did not report. If it is not recorded, you cannot show it.

Monitoring checks that systems keep working as expected after launch. Models drift as the world changes, vendors update tools and staff find new uses. So check performance and error rates for different groups, review complaints and human-review outcomes, watch vendor changes, and review the inventory and risk register regularly.

An incident process has five steps. First, detect and report: how staff and customers report problems, and to whom. Second, contain: who can pause or switch off a system, and how fast. Third, assess: is personal data involved, or is it a serious incident with a high-risk AI system? Both can apply.

Fourth, notify: decide with the data protection officer and legal team whether to notify regulators and affected people, within the legal time limits under each law. Providers and deployers of high-risk systems may have separate reporting duties. Fifth, recover and learn: fix the cause and update the risk register.

Think of a ship's logbook. It does not steer the ship, but after a storm it shows what the crew saw, what they decided and why. Monitoring is the crew watching the weather. And the incident process is the emergency drill everyone practised before the storm.

Ngozi Eze is the incident manager at Velmora, and the chatbot incident from the start of this lesson happens. In the first hour, the chatbot owner switches it to hand over every conversation to a human, and informs the vendor.

Assess: a name, address and phone number were shown, so this is a personal data breach. The affected customer lives in Nigeria, and the viewing customer in the Netherlands. The data protection officer checks whether it must be reported under the NDPA, the GDPR or both, and within which time limits.

Notify: the officer judges that the breach is likely to create a risk to the affected person, and recommends notifying the relevant regulator or regulators and the customer, with advice from counsel. Every step, time and decision is logged, including the reasons.

Learn: the cause is a session error in a vendor update. So Velmora adds a new register risk, vendor updates change chatbot behaviour without testing, with a new control that requires test results before any update goes live.

A common mistake is to log only the incidents you report. Log near misses too, and the incidents you decided not to report, with the reason. An empty log does not show that nothing happened. It may show that nobody was watching. So agree the roles and the log before anything goes wrong.

Let's recap. First, accountability means showing compliance with records: decisions, assessments, training, audits and incident logs. Second, monitoring checks that systems keep working, and an incident process says who contains, assesses and decides on notification. Third, notification duties differ by law and must always be checked.

Now for capstone step three. Add a monitoring and incident section to your policy, add at least one incident risk to your register, and check both against the rubric. Add the disclaimer line from the rubric to both documents. Then submit both.

Congratulations on finishing AI Governance, Privacy and Compliance. You can now map the laws, classify AI systems, assess risks and build a framework. Submit your capstone. It has been a pleasure learning with you, and well done.
```
