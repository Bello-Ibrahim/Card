# L09 Data Subject Rights and Automated Decisions

Course: AI-30 · Module: M2 · Objectives: O3 · Video: 5 min

## Hook
A customer writes: "Your system refused my loan in two seconds. Why? And I want a real person to look at it." Your team has a response deadline and a trained model that nobody can easily explain. What do you do first?

## Explanation
This lesson is educational and is not legal advice. The rights, their exceptions and response deadlines are set out in [the GDPR rights articles] and [the NDPA rights sections] [VERIFY] [REGION].

You know the main rights already: **information, access, correction (rectification), erasure, restriction, objection and data portability**. AI makes some of them harder to honour.

- **Access.** People can ask for their personal data and information about the processing. For AI, this includes the inputs used about them and the outputs, such as a score, as well as meaningful information about the logic involved in automated decisions [VERIFY] [REGION].
- **Correction.** If the input data is wrong, correct it and consider whether the decision must be made again.
- **Erasure and objection.** Deleting a person's record from a database is simple. Removing their influence from a trained model is not. Organisations should decide in advance how they will respond: for example, removing the data from future training sets and recording when the model will be retrained.

**Automated decisions.** Both the GDPR and the NDPA include protections for decisions based **solely** on automated processing that produce legal or similarly significant effects on a person, such as refusing credit [VERIFY] [REGION]. These decisions are allowed only in certain situations, and people usually have safeguards such as the right to obtain **human intervention**, to **express their point of view** and to **contest the decision** [VERIFY] [REGION]. See [the GDPR article on automated decisions] and [the NDPA section on automated decisions] [VERIFY] [REGION].

**Meaningful human review.** A human reviewer who simply clicks "approve" on every AI output does not make the decision "not solely automated". The reviewer needs authority to change the outcome, access to the relevant information and enough time and training to use them.

**Analogy:** An automated decision without a human route is like a ticket machine that rejects your payment and has no staff nearby. The right to human intervention puts a person next to the machine who can look at your case, explain what happened and override the machine if it made a mistake.

## Worked Example
Funmilayo Adeyemi applies online for a personal loan from a hypothetical digital lender in Lagos. The AI system refuses her in seconds. She writes to the lender asking why, and asks for a human review.

The lender's DPO follows its procedure:

1. **Log and verify.** The request is logged with the date received. Her identity is confirmed using details the lender already holds.
2. **Identify the rights.** This is an access request and a request for human intervention in a solely automated decision with a significant effect.
3. **Gather the facts.** The team extracts the input data used, her score, and the main factors that affected it, such as a short credit history and a high number of recent applications.
4. **Check the data.** Funmilayo says one recorded loan was repaid. The team checks and finds the record out of date, and corrects it.
5. **Human review.** A trained credit officer with authority to change the outcome reviews the application with the corrected data and her comments. The officer approves a smaller loan.
6. **Respond.** The lender sends a plain-language letter within [the statutory deadline] [VERIFY] [REGION], explaining the main factors, the correction and the new decision, and how to complain to the regulator.
7. **Learn.** The DPO reports the out-of-date data source to the system owner for a wider check.

## Common Mistake
Many teams think explaining an AI decision means publishing the model's code or maths. That is rarely what people need. A meaningful explanation describes the main factors that affected this person's outcome, in words they can understand, and what they could do differently. Another mistake is to treat any human involvement as enough; a reviewer without real authority does not provide meaningful review.

## Key Takeaways
1. Rights such as access, correction, erasure and objection still apply to AI, but are harder to honour when data is inside a trained model, so plan responses in advance.
2. Both laws protect people from solely automated decisions with significant effects, including routes to human intervention and to contest the decision.
3. Human review must be meaningful: authority, information and training; this lesson is educational, not legal advice.

## Hands-on Exercise
**Task:** Write a step-by-step internal procedure for answering an access request and a request for human review of an automated decision, for a hypothetical AI system.
**Tools:** A word processor; official regulator guidance on rights and automated decisions [VERIFY].
**Steps:**
1. Choose a hypothetical system, such as an AI tool that decides insurance premiums for drivers in Portugal.
2. Write the procedure in numbered steps: receive, log, verify identity, identify the rights, gather data and main factors, check accuracy, human review, respond, learn.
3. For each step, name the responsible role (not a person) and the record to keep.
4. Use placeholders such as "[statutory deadline]" instead of guessing deadlines.
5. Use invented examples only. Do not paste real customer requests into any AI tool.
**What good looks like:** A one-page procedure with clear owners, records at each step, a meaningful human review step with authority to change the outcome, and deadline placeholders.
**Time:** about 25 minutes

## Review Flags
- Legal/compliance reviewer sign-off required before release.
- [VERIFY] [REGION] Data subject rights, their exceptions, response deadlines, and the GDPR article and NDPA section on solely automated decisions (including when such decisions are allowed and the safeguards) must be checked (curriculum flag).
- [VERIFY] [REGION] The "meaningful information about the logic involved" wording and the statutory deadline placeholder must be confirmed.
- [VERIFY] Official guidance source for the exercise must be chosen, with date recorded.
