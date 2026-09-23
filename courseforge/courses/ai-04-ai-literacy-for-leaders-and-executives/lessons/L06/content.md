# L06 AI Risks Every Leader Must Manage

Course: AI-04 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
An AI tool saves your team many hours a week. Then one wrong output reaches a customer, a regulator or a journalist. Suddenly the conversation is not about time saved but about trust lost. Which risks should you manage before that day comes?

## Explanation
AI risk is manageable when you name it clearly, rate it and give it an owner. Six categories cover most situations.

**1. Wrong or invented outputs.** AI can give inaccurate predictions, and generative AI can invent facts, sources or numbers with confidence. Control: human review for any output that reaches customers or affects decisions, plus regular sample checks.

**2. Bias and unfair treatment.** A model trained on past decisions can repeat past unfairness towards certain groups. Control: test results across different groups before and after launch, and keep a person responsible for final decisions about people.

**3. Privacy and data leaks.** Staff may paste personal or confidential data into tools that store or reuse it. Control: clear rules on which data may enter which tools, approved business accounts, and training.

**4. Security.** AI systems can be attacked, for example with hidden instructions in documents or emails that change a tool's behaviour, or with access to data they should not see. Control: limit what each tool can access, involve your IT security team and keep logs.

**5. Legal and contractual exposure.** AI use can conflict with data protection, employment or consumer rules, or with contracts that limit how client data may be used. These rules differ by country and change over time. [REGION] Control: ask your legal team to review high-impact use cases and your contracts before launch.

**6. Damage to reputation.** Even a legal and accurate use can upset customers or staff if it feels hidden or unfair. Control: be open about where AI is used, and offer a way to reach a person.

A **risk register** is a simple table that lists each risk, rates its likelihood and impact from 1 to 5, names a control and names an owner. Multiply likelihood by impact to find the risks that need attention first.

**Analogy:** Managing AI risk is like managing risk on a building site. You do not stop building. You wear helmets, fence off dangerous areas and name a safety officer. Each hazard has a matching control and a person who checks it.

## Worked Example
Priya Sandhu is HR director at a hypothetical engineering company in Canada. Her team wants an AI tool that screens job applications and ranks candidates. Before any pilot, she builds a risk register.

| Risk | Likelihood | Impact | Control | Owner |
|---|---|---|---|---|
| Tool ranks strong candidates low because of unusual CV formats | 3 | 4 | Recruiters review every rejected CV in the pilot | Recruitment lead |
| Tool favours groups that were hired more often in the past | 3 | 5 | Test results across groups; no automatic rejections | HR director |
| Applicant data stored or reused by the vendor | 2 | 5 | Contract terms reviewed; data stays in agreed region | Data protection officer |
| Hidden text in a CV changes the ranking | 2 | 3 | IT security test before launch | IT security manager |
| Use conflicts with local employment or equality rules [REGION] | 2 | 5 | Legal review before pilot | Legal counsel |
| Candidates feel judged by a machine | 3 | 3 | Tell applicants AI assists screening; offer human contact | Head of employer brand |

The bias risk has the highest score, 15. Priya decides the tool may only sort applications for recruiters to review. It may not reject anyone automatically. She makes this a condition of the pilot.

## Common Mistake
Many leaders treat AI risk as a technical issue for the IT team. Most AI risks are business risks: unfair treatment, broken trust, legal exposure. Technical staff can help with controls, but a business leader must own each risk and decide how much risk is acceptable.

## Key Takeaways
1. The main AI risks are wrong outputs, bias, privacy, security, legal exposure and damage to reputation.
2. A risk register rates each risk on likelihood and impact and names one control and one owner.
3. Business leaders, not only technical teams, must own AI risks and decide what level is acceptable.

## Hands-on Exercise
**Task:** Build a risk register for one AI use case with at least five risks, rated for likelihood and impact, each with one control and one owner.
**Tools:** A spreadsheet or document table. Optional: Claude or ChatGPT to suggest risks you may have missed, using a general description with no confidential or personal data.
**Steps:**
1. Choose one of your top use cases from L04.
2. List at least one risk from each of the six categories where it applies, and at least five in total.
3. Rate likelihood and impact from 1 to 5 and multiply them.
4. For each risk, write one practical control.
5. Name an owner by role, not by name.
6. Mark the two highest-scoring risks and note what must be true before a pilot starts.
**What good looks like:** A table with at least five specific risks linked to your use case, realistic ratings, a clear control and owner for each, and pilot conditions for the top two risks.
**Time:** about 30 minutes

## Review Flags
- [REGION] Data protection, employment, equality and consumer rules differ by country and change often. The lesson names no specific laws; a reviewer may add sourced regional notes after checking them.
- The recruitment case is hypothetical on purpose, to avoid unverified claims about real companies.
