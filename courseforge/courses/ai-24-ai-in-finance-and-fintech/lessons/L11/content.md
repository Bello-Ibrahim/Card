# L11 Regulatory Principles for AI in Finance

Course: AI-24 · Module: M3 · Objectives: O5 · Video: 5 min

## Hook
Your fintech is launching an AI credit product in three countries. Each country has different laws, different regulators and different languages. Do you need to learn three rulebooks from zero? Not completely. Most rulebooks are built on the same small set of principles.

## Explanation
This lesson teaches principles that appear, in different words, in the rules of many countries. It is not legal advice. For any real product, always confirm the local rules with your compliance or legal team.

**1. Fair treatment.** Customers must not be treated unfairly, and decisions must not discriminate against protected groups, directly or indirectly. You practised this in L06 and L07.

**2. Explainability and transparency.** Customers should know when important decisions are made or supported by automated systems, and should receive understandable reasons, especially for declines (L10). Staff and supervisors must be able to understand how the model works.

**3. Data protection.** Personal data must be collected for a clear purpose, on a lawful basis, kept to the minimum needed, stored securely and kept only as long as necessary. People often have rights to access and correct their data and, in some places, rights about automated decisions.

**4. Model risk management.** Models can be wrong or become wrong over time. Institutions need an inventory of models, independent validation before use, ongoing monitoring and clear limits (L12).

**5. Accountability.** A named person or committee is responsible for each model and its outcomes. "The AI decided" is never an acceptable answer to a customer or a supervisor.

**6. Third-party risk.** Many AI tools come from outside vendors. The institution remains responsible for outcomes, so it must check the vendor's data use, security, testing and the right to audit.

Here are some named examples, given only as illustrations. Each one needs checking for scope and current status before use:

- **European Union:** the EU AI Act treats AI systems used to assess the creditworthiness of individuals as high-risk, with extra requirements such as risk management, data governance and human oversight [REGION] [VERIFY].
- **United States:** lenders must send applicants an adverse action notice that states the main reasons when credit is declined, under the Equal Credit Opportunity Act and Regulation B [REGION] [VERIFY].
- **Data protection laws:** the GDPR in the European Union, the LGPD in Brazil, the NDPA in Nigeria and POPIA in South Africa set rules for processing personal data [REGION] [VERIFY].

This course does not quote article numbers, dates or penalties, because these change and depend on the details of each case.

**Analogy:** The principles are like the rules of the road. Countries drive on different sides and have different speed limits, but almost all of them require a licence, working brakes, attention to pedestrians and responsibility for accidents. If you understand the shared principles, learning the local version is much faster.

## Worked Example
Thandiwe Nkosi is head of compliance at Kopano Credit, a hypothetical fintech in Johannesburg, South Africa. The company plans to offer an AI-supported small-business loan in South Africa, Nigeria and Brazil.

She builds a principles table for the product. For each principle, she notes what the company already does and what she must confirm locally.

| Principle | What we already do | What I must check locally |
|---|---|---|
| Fair treatment | Monthly approval and error rates by group | Protected characteristics in each country |
| Explainability | Top-three decline reasons in plain language | Required content and timing of decline notices |
| Data protection | Consent screen for bank-statement data | Lawful basis and rights under POPIA, NDPA and LGPD [REGION] [VERIFY] |
| Model risk | Annual validation by the risk team | Supervisor expectations for model risk in each country |
| Accountability | Chief risk officer owns the model | Who must sign off for each licence |
| Third-party risk | Vendor contract for bureau data | Rules on sending data across borders |

The table does not answer every question. It shows her exactly which questions to ask local lawyers, which saves time and money.

## Common Mistake
Many teams assume that if their product follows the rules of one country, it can launch anywhere. Principles travel well; details do not. Consent rules, data transfer limits and notice requirements can differ a lot. Use the principles to prepare, then check the local rules every time.

## Key Takeaways
1. Six principles appear in many countries: fair treatment, explainability, data protection, model risk management, accountability and third-party risk.
2. Named laws, such as the EU AI Act, US adverse action rules, the GDPR, LGPD, NDPA and POPIA, are examples to check with experts, not rules to copy.
3. A principles table turns general knowledge into a clear list of questions for your compliance or legal team.

## Hands-on Exercise
**Task:** Complete a principles table for your own country.
**Tools:** Google Sheets (free); the course's principles table template. Optional: Claude or ChatGPT (free plan) to suggest questions [VERSION].
**Steps:**
1. Copy the principles table template with the six principles as rows.
2. Choose one AI use case you know, such as a fraud model or a service assistant.
3. For each principle, write what you already know about how it applies in your country.
4. For each principle, write at least one specific question you must check with your compliance or legal team.
5. Optional: ask an AI assistant for extra questions. Do not accept its legal statements as facts; add them only as questions to check.
6. Mark any named law in your table with "to confirm".
**What good looks like:** All six principles completed, specific questions rather than "check the law", and no legal claim presented as confirmed without a source.
**Time:** about 25 minutes

## Review Flags
- [REGION] [VERIFY] EU AI Act treatment of creditworthiness assessment as high-risk, and the requirements listed; confirm scope and application dates before recording.
- [REGION] [VERIFY] US adverse action notice requirements under the Equal Credit Opportunity Act and Regulation B.
- [REGION] [VERIFY] Names and scope of the example data protection laws: GDPR (EU), LGPD (Brazil), NDPA (Nigeria), POPIA (South Africa).
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT must be checked before recording.
