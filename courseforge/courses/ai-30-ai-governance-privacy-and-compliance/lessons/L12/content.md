# L12 Building an AI Inventory and Risk Register

Course: AI-30 · Module: M3 · Objectives: O4, O5, O6 · Video: 5 min

## Hook
A regulator asks: "Which AI systems do you use, and what are their main risks?" If the answer takes three weeks and ten emails, your governance is not working. Two simple documents, an AI inventory and a risk register, let you answer in minutes.

## Explanation
This lesson is educational and is not legal advice. The legal classifications you record in these documents are your organisation's own judgements and should be reviewed by qualified advisers.

**The AI inventory** is a list of every AI system in use or in development. One row per system. Useful columns:

| System | Owner | Purpose | Personal data used | EU AI Act role and tier | GDPR / NDPA role | Assessments done |
|---|---|---|---|---|---|---|

Include systems bought from vendors and AI features inside existing software, not only systems you built. The inventory answers the question "what do we have?".

**The risk register** records the risks those systems create and how you manage them. One row per risk. The core columns are:

| Risk | AI system | Likelihood | Impact | Owner | Control | Review date |
|---|---|---|---|---|---|---|

For this course, add one more column, **Law(s)**, to show whether the risk connects to the EU AI Act, the GDPR, the NDPA or several of them.

Some practical rules:

- **Write risks as cause, event and effect.** "Biased training data (cause) leads the tool to rank some groups lower (event), so qualified candidates are rejected unfairly (effect)." A risk written as one word, such as "bias", cannot be managed.
- **Use a simple scale.** For example, likelihood and impact from 1 (low) to 5 (high). Define what each number means so different people score in the same way.
- **Name one owner per risk:** a role that can act, not a committee.
- **Controls must be real.** Write what actually happens today. Planned controls go in a separate column or are marked "planned".
- **Set a review date** based on the level of risk: higher risks are reviewed more often.

**Analogy:** The inventory is like the list of rooms and equipment in a hospital. The risk register is like the list of things that could go wrong in each room, who is responsible and what protects patients. You need the first list to write the second.

## Worked Example
Priya Raman is the privacy analyst at Velmora Tradeways Ltd, the fictional capstone organisation from L11. She writes the first two register entries.

**Inventory rows (shortened):**
- **CV-screening tool:** owner Head of HR; ranks applicants; CVs and application data; deployer of a likely high-risk system [VERIFY] [REGION]; controller under the GDPR and the NDPA; DPIA not yet done.
- **Translation tool:** owner Head of IT; translates emails and documents; may contain customer and staff personal data; deployer of a likely minimal-risk system; controller, with the vendor as processor; no DPIA.

**Risk register entries:**

| Risk | AI system | Likelihood | Impact | Owner | Control | Review date | Law(s) |
|---|---|---|---|---|---|---|---|
| Tool ranks candidates from some groups lower because of patterns in historical hiring data, leading to unfair rejection | CV-screening tool | 3 | 5 | Head of HR | Planned: vendor bias-test results requested; recruiter reviews every rejection; DPIA before wider use | Every 3 months | EU AI Act, GDPR, NDPA |
| Staff paste confidential client contracts containing personal data into the translation tool, and the vendor stores or reuses them, causing a data breach or unlawful transfer | Translation tool | 3 | 4 | Head of IT | Enterprise contract with no-training term; data processing agreement; staff guidance; transfer check for Nigerian data | Every 6 months | GDPR, NDPA |

Priya notes that the translation tool is minimal risk under the AI Act, yet still carries a real data protection risk. Tier and risk level are not the same thing.

## Common Mistake
Many teams build the register once, for an audit, and never update it. A register is a working tool. Link each review date to a calendar reminder, update scores when controls change, and add new rows when the inventory changes. A register that still shows "planned" controls after a year is a warning sign, not evidence of compliance.

## Key Takeaways
1. The AI inventory lists every AI system with its owner, purpose, data, role under each law and risk tier.
2. The risk register records each risk with likelihood, impact, owner, control and review date, and here also the relevant law or laws.
3. A low AI Act tier does not mean low data protection risk; score each risk on its own facts, remembering this course is educational, not legal advice.

## Hands-on Exercise
**Task:** Capstone step 1: build an AI inventory and a risk register of at least 6 risks for the sample organisation, mapping each risk to the relevant law or laws.
**Tools:** A free spreadsheet tool, such as Google Sheets or LibreOffice Calc, or a free risk register template from an official or reputable source [VERIFY]; your notes from L03 to L11.
**Steps:**
1. Create an inventory sheet with the columns shown above, and add all six Velmora systems from L11.
2. Classify each system: likely AI Act tier, Velmora's role, and its GDPR and NDPA role. Mark uncertain points "[to confirm]".
3. Create a register sheet with the columns: risk, AI system, likelihood, impact, owner, control, review date, law(s).
4. Write at least 6 risks, covering at least 4 different systems, in cause, event and effect form.
5. Score each risk from 1 to 5 for likelihood and impact, and explain your scale in a note.
6. Keep all details fictional. Do not use real company or personal data.
**What good looks like:** A complete inventory of six systems, at least 6 well-written risks linked to the right laws, realistic controls, named owner roles and review dates that match the risk level.
**Time:** about 60 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [REGION] The likely tiers and roles for the CV-screening tool and translation tool in the worked example must be confirmed.
- [VERIFY] The free risk register template must be chosen from an official or reputable source, with licence and date recorded.
- Fictional organisation: "Velmora Tradeways Ltd" must be checked so it does not match a real company (see L11).
