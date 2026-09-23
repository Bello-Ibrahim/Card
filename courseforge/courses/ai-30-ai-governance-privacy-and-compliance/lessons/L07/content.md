# L07 Lawful Basis for AI Processing

Course: AI-30 · Module: M2 · Objectives: O3 · Video: 5 min

## Hook
A retailer says, "Customers accepted our terms, so we can use their data to train our AI." Is that enough? Often it is not, because training a model and using it are different processing activities, and each one needs its own lawful basis.

## Explanation
This lesson is educational and is not legal advice. The lawful bases are listed in [the GDPR article on lawful basis] and [the NDPA section on lawful basis] [VERIFY] [REGION]. The two lists are similar, but check the exact wording and any conditions in each.

Under the GDPR, the lawful bases are **consent, contract, legal obligation, vital interests, public task and legitimate interests**. The NDPA contains a comparable list [VERIFY] [REGION]. For private-sector AI, three bases come up most often:

- **Consent** must be freely given, specific, informed and unambiguous, and people must be able to withdraw it easily. It is hard to use for training, because withdrawal may require you to remove a person's data from a model.
- **Contract** covers processing that is genuinely necessary to perform a contract with the person. Using data to personalise a service the person asked for may qualify; training a general model to improve future products usually does not.
- **Legitimate interests** needs a three-part test: a legitimate **purpose**, processing that is **necessary** for that purpose, and a **balancing test** in which the organisation's interest is not overridden by the person's interests, rights and freedoms. Regulators have published guidance on using this basis for AI model development [VERIFY] [REGION].

**Separate activities, separate bases.** Split your AI processing into activities, such as collecting data, training the model, and using the model on a person. Each needs a basis, and the answer may differ.

**Special categories.** Data such as health, biometric data used for identification, racial or ethnic origin, religion and sexual orientation needs a lawful basis *and* an extra condition, such as explicit consent, set out in [the special categories article and section] [VERIFY] [REGION]. AI can also infer special category data from ordinary data, which may bring it into scope.

**Analogy:** A lawful basis is like a ticket for a specific train. A ticket from Warsaw to Kraków does not let you continue to Vienna. If you want to take the data further, to a new purpose, you need to check whether your ticket covers the journey or whether you need a new one.

## Worked Example
Magdalena Nowak is a privacy lawyer for a hypothetical online fashion retailer in Poznań, Poland. The retailer wants an AI system that recommends products based on browsing and purchase history.

Magdalena separates two activities and compares three bases for each.

| Activity | Consent | Contract | Legitimate interests |
|---|---|---|---|
| Training the model on past purchases | Possible, but withdrawal is hard to honour in a trained model | Weak: training is not necessary to deliver past orders | Possible, if the balancing test is met |
| Showing recommendations to a logged-in customer | Possible | Weak unless recommendations are a core, requested feature | Possible, with a clear opt-out |

For **legitimate interests**, she runs the balancing test:

- **Purpose:** relevant product suggestions. Legitimate.
- **Necessity:** purchase and browsing history in the retailer's own shop are needed; data bought from third parties is not.
- **Balancing:** customers would reasonably expect some suggestions from a shop they use. Risks rise if the model infers sensitive facts, such as pregnancy or health conditions, from purchases. Controls: exclude sensitive product categories from training, give a simple opt-out, explain it clearly in the privacy notice.

Her conclusion: legitimate interests for both activities, with the controls recorded. She marks the conclusion for review against national regulator guidance [VERIFY] [REGION].

## Common Mistake
Many organisations choose consent "to be safe". Consent is not safer if people cannot really refuse, or if you cannot honour a withdrawal. Another common mistake is to change basis later: if consent is withdrawn, you usually cannot simply switch to legitimate interests. Choose the most suitable basis at the start and document why.

## Key Takeaways
1. Every processing activity needs a lawful basis, and training a model may need a different basis from using it.
2. Legitimate interests needs a documented three-part test: purpose, necessity and balancing, with controls that protect people.
3. Special category data needs an extra condition, and AI may infer it; this lesson is educational, not legal advice.

## Hands-on Exercise
**Task:** For 3 hypothetical AI processing activities, choose the most suitable lawful basis under the GDPR and under the NDPA, and justify each choice in two sentences.
**Tools:** Official texts of the GDPR and the NDPA, and regulator guidance on legitimate interests [VERIFY]; a table in a word processor.
**Steps:**
1. Activity A: a bank in Ireland uses customers' transaction history to train a fraud-detection model.
2. Activity B: a gym chain in Nigeria uses members' fingerprints to control entry.
3. Activity C: a telecoms company operating in both regions uses call-centre recordings to train a speech model.
4. For each, choose one basis under the GDPR and one under the NDPA, and write two sentences of justification.
5. Mark any special category data and state which extra condition you would check.
**What good looks like:** Six justified choices, correct identification of biometric data in Activity B, and honest notes where the NDPA answer needs checking.
**Time:** about 25 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [REGION] GDPR articles and NDPA sections on lawful basis and special categories, including any NDPA differences in the list of bases, must be checked (curriculum flag).
- [VERIFY] [REGION] Current EU and national regulator guidance on legitimate interests and AI model training must be checked (curriculum flag).
- [VERIFY] Official sources for the exercise must be chosen, with date recorded.
