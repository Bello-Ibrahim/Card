# L12 Building an AI Inventory and Risk Register | Presenter Script

Course: AI-30 · Video: 5 min · Words: 692

## Hook
A regulator asks: which AI systems do you use, and what are their main risks? If the answer takes three weeks and ten emails, your governance is not working. Two simple documents let you answer in minutes.

## Explain
Last time, we met Velmora Tradeways and designed its approval path. Today, we build its two core records: an AI inventory and a risk register. This lesson is educational and is not legal advice. The classifications you record are your own judgements, and qualified advisers should review them.

The AI inventory lists every AI system in use or in development, one row per system. Useful columns are the system, its owner, its purpose, the personal data used, its role and tier under the AI Act, its role under the GDPR and the NDPA, and the assessments done. It answers the question, what do we have?

The risk register records the risks those systems create, one row per risk. Its columns are the risk, the AI system, likelihood, impact, owner, control and review date. For this course, add one more column, laws, to show whether each risk connects to the AI Act, the GDPR, the NDPA, or several.

Some practical rules. Write each risk as cause, event and effect. For example, biased training data leads the tool to rank some groups lower, so qualified candidates are rejected unfairly. A risk written as one word, like bias, cannot be managed.

Use a simple scale, such as one to five for likelihood and impact, and define what each number means. Name one owner per risk: a role that can act, not a committee. Write only the controls that actually exist today, and mark planned ones as planned. And set review dates by risk level.

Think of a hospital. The inventory is the list of rooms and equipment. The risk register is the list of what could go wrong in each room, who is responsible and what protects patients. You need the first list to write the second.

## Demonstrate
Let's see two entries. Priya Raman is the privacy analyst at Velmora. She starts with two rows in the inventory.

The CV-screening tool is owned by the Head of HR, ranks applicants and uses CVs and application data. Velmora is the deployer of a likely high-risk system, and a controller under both data protection laws. No DPIA is done yet. The translation tool is owned by the Head of IT, may contain personal data, and is likely minimal risk.

Her first register entry: the CV tool ranks candidates from some groups lower, because of patterns in past hiring data, which leads to unfair rejection. Likelihood three, impact five, owned by the Head of HR. Planned controls include vendor bias-test results, recruiter review of every rejection and a DPIA. It is reviewed every three months, and maps to all three laws.

Her second entry: staff paste confidential contracts containing personal data into the translation tool, and the vendor stores or reuses them. Likelihood three, impact four, owned by the Head of IT. Controls include a no-training contract term, a data processing agreement, staff guidance and a transfer check. It maps to the GDPR and the NDPA.

Priya notices something. The translation tool is minimal risk under the AI Act, yet it carries a real data protection risk. Tier and risk level are not the same thing. And a common mistake is to build the register once for an audit, and never update it. Keep it working.

## Recap
Let's recap. First, the AI inventory lists every AI system with its owner, purpose, data, role under each law and risk tier. Second, the risk register records each risk with likelihood, impact, owner, control, review date and the relevant laws. Third, a low AI Act tier does not mean low data protection risk.

## CTA
Now for capstone step one. In the exercise below this video, you will build an inventory of all six Velmora systems, and a register of at least six risks across at least four systems, each mapped to the relevant laws. Keep every detail fictional.

In the next lesson, capstone step two: drafting the AI governance policy. See you there.

## Thumbnail
Headline: Answer in Minutes
Image: Navy background, two stacked spreadsheet cards labelled inventory and risk register with a teal stopwatch, headline in teal Inter Bold.

## Production Notes
- Legal/compliance reviewer sign-off required before release.
- Disclaimer spoken once in scene 2 (educational, not legal advice).
- [VERIFY] [REGION] The likely AI Act tiers and roles for the CV-screening tool (likely high-risk, deployer) and the translation tool (likely minimal risk, deployer) in scenes 9 and 12 must be confirmed by the legal reviewer.
- [VERIFY] The free risk register template for the exercise must be chosen from an official or reputable source, with licence and date recorded.
- [VERIFY] Fictional organisation: Velmora Tradeways Ltd must be checked so it does not match a real company (see L11). Priya Raman is fictional.
- No screen demos. The inventory columns, the risk register columns and both register entries are shown on slides (scenes 3, 4, 9, 10 and 11); render the register as a clean table with large type. The 1 to 5 scores and review frequencies are Velmora's own fictional choices, not legal thresholds.
- Capstone step 1 is set in this lesson's exercise.
