# L04 EU AI Act Roles and Obligations

Course: AI-30 · Module: M1 · Objectives: O2, O4 · Video: 5 min

## Hook
Two organisations use the same high-risk AI system. One built it; the other bought it. Do they have the same duties? No. Under the EU AI Act, your obligations depend on your role, and one organisation can hold several roles at once.

## Explanation
This lesson is educational and is not legal advice. Role definitions and duties are summarised here at a high level; the exact wording is in [the definitions article and the obligations chapters] [VERIFY] [REGION].

**The main roles** [VERIFY] [REGION]:

- **Provider:** develops an AI system (or has it developed) and places it on the market or puts it into service under its own name or trademark.
- **Deployer:** uses an AI system under its own authority in a professional activity.
- **Importer:** an EU-based organisation that places on the EU market an AI system from a provider outside the EU.
- **Distributor:** another organisation in the supply chain that makes a system available, such as a reseller.

Roles can change. For example, a deployer may be treated as a provider if it puts its own name on a high-risk system, makes a substantial modification, or changes the intended purpose so that the system becomes high-risk [VERIFY] [REGION].

**Provider duties for high-risk systems** include, at a high level [VERIFY] [REGION]:

- a **risk management** process across the system's life;
- **data governance** for training, validation and testing data, including checks for bias;
- **technical documentation** and **instructions for use** for deployers;
- automatic **logging** of events;
- design that allows effective **human oversight**;
- appropriate **accuracy, robustness and cybersecurity**;
- a quality management system, a conformity assessment before launch, registration where required, and **post-market monitoring**.

**Deployer duties** are lighter but real [VERIFY] [REGION]: use the system according to the instructions; assign human oversight to competent, trained people; make sure input data under their control is relevant; monitor operation and report serious problems; keep the logs they control; and inform affected people or workers where required. Some deployers must also carry out a fundamental rights impact assessment (see L10).

**Enforcement.** The Act sets penalty ranges for breaches in [the penalties article] [VERIFY] [REGION]. Do not quote penalty figures from memory. Supervision is shared between [the EU-level AI body] and [national market surveillance authorities] [VERIFY] [REGION].

**Analogy:** Think of a lift in an office building. The manufacturer must design it safely, test it and provide a manual. The building owner must use it as the manual says, arrange inspections and stop using it if it fails. If the owner rebuilds the lift's motor, the owner starts to carry some of the manufacturer's responsibility.

## Worked Example
Three hypothetical organisations are connected by one product: a triage-support tool that ranks hospital patients by urgency. Assume the tool is high-risk [VERIFY] [REGION].

- **Lucía Ferrer** leads compliance at a software vendor in Valencia, Spain, which built the tool and sells it under its brand. Her company is the **provider**. Main duties: risk management, data governance, documentation, logging, human oversight design, accuracy and robustness, conformity assessment and post-market monitoring.
- **Pieter de Vries** is the DPO at a hospital in Utrecht, the Netherlands, which buys the tool. The hospital is a **deployer**. Main duties: use it as instructed, assign trained staff to oversee its output, check input data, monitor it and report serious incidents. It is also a GDPR controller for the patient data.
- **Emeka Nwosu** runs a data science company in Lagos that develops a similar tool and sells it directly to EU clinics. His company is a **provider** from outside the EU, so it may need an authorised representative in the EU, and any EU importer will have its own checks [VERIFY] [REGION].

Each organisation writes down its role, the reason and the source it relied on.

## Common Mistake
Many buyers assume "the vendor is responsible for compliance". The provider carries the heaviest duties, but deployers have their own, and a deployer that customises or rebrands a system may become a provider. Check your role for each system, and check it again whenever you change how you use the system.

## Key Takeaways
1. EU AI Act duties depend on role: provider, deployer, importer or distributor, and one organisation can hold more than one role.
2. Providers of high-risk systems carry duties such as risk management, data governance, documentation, logging, human oversight, accuracy and robustness.
3. Deployers have their own duties, and a deployer can become a provider through rebranding or substantial changes; this summary is educational, not legal advice.

## Hands-on Exercise
**Task:** For 3 hypothetical organisations (a Spanish software vendor, a hospital in the Netherlands buying its tool, and a Nigerian company selling to EU clients), identify each one's likely role and list its main obligations at a high level.
**Tools:** Your notes from L03; the official text of the EU AI Act or an official summary [VERIFY]; a table in a word processor.
**Steps:**
1. Use the three organisations from the worked example, but change the product to an AI tool that screens job applicants.
2. For each organisation, write its likely role and one sentence explaining why.
3. List 3 to 5 main obligations for each, in plain words.
4. Add one "what would change our role?" note for each organisation.
**What good looks like:** Three correct roles with reasons, obligations that match the role (not a copy of the provider list for everyone), and a realistic role-change note, such as "if the hospital retrains the model on its own data".
**Time:** about 25 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [REGION] Role definitions, provider and deployer obligations for high-risk systems, and the conditions under which a deployer becomes a provider must be checked against the official text (curriculum flag).
- [VERIFY] [REGION] Penalty ranges must not be scripted without verification; the placeholder stays until checked (curriculum flag).
- [VERIFY] [REGION] EU AI Act supervisory structure and national designations must be checked (curriculum flag).
- [VERIFY] [REGION] Whether the triage tool is high-risk, and the authorised-representative and importer points for the Nigerian provider.
- [VERIFY] Official source for the exercise must be chosen, with date recorded.
