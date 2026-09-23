# L06 Scoping the MVP

Course: AI-28 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
Your list of features is probably long: accounts, a dashboard, five languages, a mobile app, reports. If you build all of it, you may spend months before anyone uses it. What is the smallest thing you could build next week that would teach you the most?

## Explanation
**MVP** means **minimum viable product**. It is the smallest product that lets real users do one important job, so that you can test your **riskiest assumption**. An assumption is something you believe but have not yet proved. The riskiest one is the belief that, if it is wrong, would make the whole business fail.

Examples of risky assumptions:

- "Users will trust the AI's answer enough to act on it."
- "The AI can produce a good enough result for this document type."
- "Customers will upload their files instead of emailing them."

To scope an MVP, answer five questions:

1. **Core job**: what is the one task the user must complete? Write it as "The user can [do something] and get [result]."
2. **Riskiest assumption**: what must be true for the business to work, and is still uncertain?
3. **In**: what must you build so a user can complete the core job?
4. **By hand**: what can you or a team member do manually for now? Early on, manual work is often cheaper and teaches you more.
5. **Out**: what will you deliberately leave out, even if it is attractive?

Finally, define the **success measure**: the number that tells you whether the assumption is true. For example, "8 of 10 test users complete the core job without help, and 6 say they would use it again next month."

A lean MVP is not a poor-quality product. The part you build should work well. It is simply narrow.

**Analogy:** When a road engineer wants to know whether a new bridge is needed, she does not build the whole bridge. She may first run a small ferry and count how many people use it. The ferry is small, but it answers the real question: do people need to cross here?

## Worked Example
Valentina is a hypothetical founder in Buenos Aires, Argentina. Her interviews with small landlords and tenants showed that many people sign rental contracts they do not fully understand. Her big vision is an AI assistant that explains any legal document in plain Spanish.

That vision is too wide for an MVP. There are hundreds of document types, each with its own rules. So she writes a one-page scope:

- **Core job:** A tenant uploads one residential rental contract and receives a plain-language summary of the key terms, with a list of clauses to ask a lawyer about.
- **Riskiest assumption:** Tenants find the summary clear and useful enough to use before signing, and the summary is accurate.
- **In:** An upload form, one AI step that produces the summary using a fixed structure, and a results page with a clear notice that this is not legal advice.
- **By hand:** A lawyer friend reviews every summary before it is sent during the first month. Valentina sends results by email instead of building accounts.
- **Out:** Other document types, user accounts, payments, a mobile app, and contracts in other languages.
- **Success measure:** In one month, 20 tenants use it; the lawyer rates at least 17 summaries as accurate; and at least 12 tenants say it helped them ask better questions.

Because rental contract rules depend on local law, the lawyer review is part of the product, not an extra [REGION]. Valentina also plans to remove personal details from contracts before sending them to any AI model, and to tell users how their documents are handled.

## Common Mistake
Many founders define the MVP as "version 1 of the full product, but faster". They build accounts, payments and settings first, because those feel like "real" product work. None of this tests the riskiest assumption. Another mistake is refusing to do anything by hand because "it does not scale". In the MVP stage, manual work is a tool for learning. You can automate it once you know it is worth automating.

## Key Takeaways
1. An MVP is the smallest product that lets users complete one core job and tests your riskiest assumption.
2. Decide clearly what is in, what is done by hand, and what is out.
3. Set a measurable success measure before you start building.

## Hands-on Exercise
**Task:** Write a one-page MVP scope: the core job, the assumption you are testing, what is in, what is out, and the success measure.
**Tools:** A free document editor or notes app. Optional: Claude (free plan) as a reviewer.
**Steps:**
1. Write the core job in one sentence: "The user can [do something] and get [result]."
2. List three assumptions your business depends on, and circle the riskiest one.
3. Make three lists: In, By hand, and Out. Aim for no more than 3 or 4 items in "In".
4. Write a success measure with numbers and a time limit.
5. Optional: paste your scope into Claude (without confidential details) and ask: "Which items in the In list could I do by hand or leave out, and does my success measure really test the riskiest assumption?"
6. Cut at least one item from "In" if you can.
**What good looks like:** One page with a single core job, a clearly stated riskiest assumption, a short "In" list, specific "By hand" and "Out" items, and a success measure with numbers and a deadline.
**Time:** about 30 minutes

## Review Flags
- [REGION] Rental contract rules and the rules on who may give legal explanations differ by country; the Argentina example is illustrative and does not describe local law.
