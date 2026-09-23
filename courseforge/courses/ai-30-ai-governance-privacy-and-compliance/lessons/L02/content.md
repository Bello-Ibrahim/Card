# L02 The Regulatory Map: Three Laws, Different Jobs

Course: AI-30 · Module: M1 · Objectives: O1 · Video: 5 min

## Hook
A lending app is built in Lagos, runs on servers in Ireland and approves loans for customers in Portugal. Which law applies? The honest answer is often "more than one", and each law asks different questions. This lesson is educational and is not legal advice.

## Explanation
This course works with three legal frameworks. They overlap, but each one has a different job.

**The EU AI Act** regulates AI systems and certain AI models. Its main tool is risk: the greater the possible harm of an AI use, the stricter the rules. It focuses on the product and its use, and places duties on roles such as **providers** (who develop an AI system and place it on the market) and **deployers** (who use it under their authority). You will study these roles in L04.

**The GDPR** regulates the processing of personal data about people in the EU. It does not care whether processing is done by AI or by a spreadsheet. If an AI system collects, trains on or produces personal data, the GDPR applies to that processing. Its key roles are the **controller**, who decides why and how data is processed, and the **processor**, who processes data on the controller's behalf.

**Nigeria's NDPA** (Nigeria Data Protection Act) also regulates the processing of personal data, with a similar structure of principles, lawful bases, rights and duties for **data controllers** and **data processors**. It has its own regulator, its own rules on cross-border transfers and its own extra duties for some organisations. You will study it in L08.

**Analogy:** Think of a lorry that carries food across a border. Vehicle safety rules check the lorry itself. Food hygiene rules check what it carries. Customs rules check where it goes. The EU AI Act is like the vehicle rules for the AI system; the GDPR and the NDPA are like the hygiene rules for the personal data inside it. One journey can meet all three sets of inspectors.

**Territorial scope.** Each law decides for itself when it applies, and each one can reach organisations outside its home territory. At a high level:

- The EU AI Act can apply to providers that place AI systems on the EU market, to deployers in the EU, and in some cases to non-EU organisations whose system output is used in the EU [VERIFY] [REGION].
- The GDPR can apply to organisations established in the EU, and to organisations outside the EU that offer goods or services to people in the EU or monitor their behaviour [VERIFY] [REGION].
- The NDPA can apply to processing by organisations in Nigeria and, in some cases, to organisations outside Nigeria that process data of people in Nigeria [VERIFY] [REGION].

The exact tests are set out in [the relevant scope articles and sections] [VERIFY] [REGION]. Always check the text itself.

**Regulators.** Each law has its own supervisory structure: [the EU-level AI body and the national market surveillance authorities] for the AI Act, [the national data protection authorities and the EU-level board] for the GDPR, and [Nigeria's national data protection regulator] for the NDPA [VERIFY] [REGION]. Names and designations can change, so confirm them from official sources.

## Worked Example
Adaeze Okonkwo founds a hypothetical lending app in Lagos. It uses an AI model to score applicants. The company decides to accept customers in Portugal.

- **NDPA:** the company is based in Nigeria and processes data of Nigerian customers. It is a data controller, so the NDPA very likely applies [VERIFY] [REGION].
- **GDPR:** by offering loans to people in Portugal, the company may fall within the GDPR's reach even without an EU office [VERIFY] [REGION]. It may also need an EU representative [VERIFY] [REGION].
- **EU AI Act:** the company developed the scoring model, so it is likely a provider. Credit scoring of individuals is an example of a use that may be high-risk [VERIFY] [REGION]. When it uses the model on EU customers, it is also a deployer.

Adaeze's team now has three sets of questions, not one. Their first task is to record which law applies to which activity, and why.

## Common Mistake
Many people think "we comply with the GDPR, so our AI is covered". The GDPR protects personal data; it does not set the AI Act's product rules on risk management, documentation or human oversight. The opposite is also wrong: meeting AI Act duties does not give you a lawful basis for processing personal data. Map each law separately, then look for overlaps you can handle together.

## Key Takeaways
1. The EU AI Act regulates AI systems and models by risk; the GDPR and the NDPA regulate the processing of personal data, including inside AI systems.
2. Each law has its own territorial scope, so one AI system can fall under all three at the same time.
3. Roles differ by law: provider and deployer under the AI Act, controller and processor under the GDPR and the NDPA.

## Hands-on Exercise
**Task:** Fill in a comparison table for the three laws using official regulator guidance, marking any point you could not confirm.
**Tools:** Official guidance pages from the European Commission, EU and national data protection regulators, and Nigeria's data protection regulator [VERIFY]; a spreadsheet or a table in a word processor.
**Steps:**
1. Create a table with three columns (EU AI Act, GDPR, NDPA) and four rows: who it protects, what it regulates, key roles, main regulator.
2. Fill in each cell from an official source only. Write the source name and the date you read it.
3. Add a fifth row, "When it applies outside its home territory", in plain words.
4. Mark any cell you could not confirm with "[not confirmed]".
**What good looks like:** A complete 5-row table with a source and date for each cell, honest "[not confirmed]" marks, and no article numbers copied from unofficial websites.
**Time:** about 25 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [REGION] Territorial scope rules for the EU AI Act, the GDPR and the NDPA, including the scope placeholders, must be checked against the official texts (curriculum flag).
- [VERIFY] [REGION] EU AI Act supervisory structure and national designations, EU data protection authorities and board, and the name of Nigeria's regulator must be confirmed before the placeholders are replaced (curriculum flag).
- [VERIFY] [REGION] Whether credit scoring falls in a high-risk category, and whether an EU representative is needed in the worked example.
- [VERIFY] Official guidance sources must be chosen, with licence and date recorded.
