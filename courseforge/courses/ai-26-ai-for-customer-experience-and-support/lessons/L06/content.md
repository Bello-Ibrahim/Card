# L06 Mapping the Workflow: Automate, Assist or Human

Course: AI-26 · Module: M2 · Objectives: O4 · Video: 5 min

## Hook
"Should AI handle refunds?" is the wrong question. A refund is not one task. It is a chain of small steps, and some of them are perfect for AI while others must stay with a person. This lesson shows you how to break a process into steps and decide who does each one.

## Explanation
A **workflow** is the list of steps from the moment a customer contacts you until the case is closed. To design where AI fits, you first write down the steps, then you give each step one of three labels:

- **Automate:** AI or a simple automation does the step with no person involved each time. People still check samples and results.
- **Assist:** AI prepares something, such as a draft, a summary or a suggested decision, and a person checks and decides.
- **Human:** a person does the step. AI may not be involved at all.

To choose a label, ask four questions about each step:

1. **How risky is a mistake?** If a wrong answer costs a lot of money, breaks a law or harms someone, the step needs a person, or at least a person's approval.
2. **How emotional is the situation?** An angry, worried or grieving customer needs real empathy and flexibility. AI can help the agent, but a person should lead.
3. **How complex is the case?** Simple cases follow one clear rule. Complex cases need judgement, exceptions or information from several systems.
4. **Could the customer be vulnerable?** For example, an older customer who is confused, a person in financial difficulty, or someone who mentions illness. Vulnerable customers need extra care and should reach a person easily.

If all four answers are "low", the step is a good candidate for **automate**. If one or two are "medium", **assist** is often right. If any answer is "high", the step usually stays **human**.

The labels are not fixed forever. You may start a step as "assist" and move it to "automate" later, after checking results for a period. It is safer to move steps towards automation slowly than to automate first and discover problems from customer complaints.

**Analogy:** Think of an airport. Automatic gates check passports for simple cases. When a passport is damaged or a traveller's case is unusual, the gate sends them to an officer. Staff also watch the gates. The airport did not ask "Should machines do border control?" It asked which part of the check a machine can do safely, and where a person is needed.

## Worked Example
Farah manages customer service for a hypothetical electronics retailer in Kuala Lumpur, Malaysia. She maps the refund process for items returned within the return period.

| Step | Risk | Emotion | Complexity | Vulnerable? | Label | Reason |
|---|---|---|---|---|---|---|
| 1. Customer asks for a refund in chat | Low | Varies | Low | Unknown | Automate | Chatbot collects order number and reason with a simple form. |
| 2. Check the order date and return period | Low | Low | Low | No | Automate | A fixed rule on data in the order system. |
| 3. Classify the reason (faulty, unwanted, damaged) | Medium | Low | Medium | No | Assist | AI suggests a reason; agent confirms. |
| 4. Decide on refunds above a set amount | High | Medium | Medium | Possible | Human | Money and exceptions; a supervisor approves. |
| 5. Reply to the customer with the decision | Medium | High if refused | Low | Possible | Assist | AI drafts; agent edits, especially for refusals. |
| 6. Customer disputes the decision | High | High | High | Possible | Human | Needs judgement and empathy. |

Farah notices that step 1 can become emotional. If a customer writes that the product caught fire, it is a safety issue, not a normal refund. She adds a rule: any mention of fire, injury or smoke goes straight to a person. She also sets the refund amount limit for step 4 together with the finance team, rather than choosing it alone.

## Common Mistake
Many teams label a whole process, such as "refunds" or "complaints", as either automated or human. This hides the details. Most processes contain simple steps that AI can do well and difficult steps that need a person. Always label each step, and write the reason next to the label so that others can question and improve it.

## Key Takeaways
1. Break each support process into steps and label each step automate, assist or human.
2. Use four questions to choose the label: risk of a mistake, emotion, complexity and customer vulnerability.
3. Start carefully, write down your reasons, and move steps towards automation only after checking the results.

## Hands-on Exercise
**Task:** Draw the workflow for one support process from your work and mark each step as automate, assist or human, with a reason.
**Tools:** Paper, a whiteboard, or a free diagram or spreadsheet tool (for example Google Sheets or Google Drawings).
**Steps:**
1. Choose one process from your list in L01, such as order changes, password resets or complaints. If you do not work in support, use a made-up online shop.
2. Write the steps in order, from first contact to case closed. Aim for 5 to 8 steps.
3. For each step, answer the four questions (risk, emotion, complexity, vulnerability) with low, medium or high.
4. Give each step a label: automate, assist or human.
5. Write one sentence of reason for each label.
6. Mark at least one point where the case must move to a person even if the step is usually automated, such as a safety word or a customer asking for a person. You will build on this in L07.
**What good looks like:** A clear table or diagram with 5 to 8 steps, a label and a reason for each, and at least one clear rule for moving a case to a person. High-risk or emotional steps are not labelled "automate".
**Time:** about 25 minutes

## Review Flags
- None. The worked example is hypothetical and makes no claims about specific tools, figures or laws.
- Judgement call (from curriculum): the exercise may use the learner's own process but no real customer data.
