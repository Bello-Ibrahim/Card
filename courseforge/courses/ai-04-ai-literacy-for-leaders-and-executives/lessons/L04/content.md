# L04 Finding and Prioritising Use Cases

Course: AI-04 · Module: M1 · Objectives: O3 · Video: 5 min

## Hook
After a workshop, your managers hand you twenty AI ideas. All of them sound promising. You have budget and attention for two. How do you choose without simply picking the idea from the loudest person in the room?

## Explanation
A simple scoring method makes the choice clear and fair. You score each use case on two dimensions and place it on a two-by-two matrix.

**Business value** asks: if this works, how much does it matter? Consider time saved, quality improved, cost reduced, risk lowered or customer experience improved. Also consider how closely it supports your strategy.

**Feasibility** asks: how easy is it to deliver safely? Score four factors:
- **Data available:** does the data exist, is it good enough and are we allowed to use it?
- **Risk:** how serious is a mistake, and can a person catch it?
- **Effort:** how much change to systems and workflows is needed?
- **Skills:** do we have, or can we easily get, the people to run it?

Score value and each feasibility factor from 1 (low) to 5 (high). For risk and effort, a high score means low risk or low effort, so that a higher number is always better. Average the four factors to get one feasibility score.

Then place each idea in one of four boxes:
- **High value, high feasibility: quick wins.** Start here.
- **High value, low feasibility: strategic projects.** Plan them, and fix the data or skills gaps first.
- **Low value, high feasibility: small improvements.** Do them only if they are almost free.
- **Low value, low feasibility: avoid.**

Here is a simple CertifAI scoring template you can copy into any spreadsheet:

| Use case | Value (1–5) | Data (1–5) | Risk (1–5) | Effort (1–5) | Skills (1–5) | Feasibility (average) | Box |
|---|---|---|---|---|---|---|---|

Scores are judgements, not facts. Their value is that they make your reasons visible, so others can challenge them.

**Analogy:** Think of planning a family trip with a fixed budget. Some destinations would be wonderful but need visas, long flights and months of planning. Others are close, affordable and still enjoyable. You would plan one easy trip now and save for the big one. The matrix does the same for AI ideas.

## Worked Example
Mei Ling is operations director of a hypothetical hotel group in Malaysia with twelve properties. Her managers suggest six ideas. She scores them with her team.

| Use case | Value | Feasibility | Box |
|---|---|---|---|
| Draft replies to guest reviews for staff to edit | 4 | 4.5 | Quick win |
| Summarise daily maintenance reports for managers | 3 | 4 | Quick win |
| Forecast room demand to set prices | 5 | 2.5 | Strategic |
| Personalised offers based on guest history | 4 | 2 | Strategic |
| Automatic translation of staff notices | 2 | 4.5 | Small improvement |
| Face recognition at check-in | 2 | 1.5 | Avoid |

The review replies score high on feasibility because staff check every draft and no personal guest data is needed. Demand forecasting has high value, but the booking data sits in three systems with different formats, so data scores 2. Face recognition scores low on risk because of privacy concerns and guest trust.

Mei Ling chooses two quick wins, review replies and maintenance summaries, to build skills and trust. She chooses demand forecasting as the longer-term project and starts a data clean-up now, so it will be ready for a pilot later.

## Common Mistake
Many leaders choose the highest-value idea first, even when feasibility is low. The project then stalls on data or skills, and the organisation decides "AI does not work here". Starting with quick wins builds skills, evidence and trust that make the strategic projects possible.

## Key Takeaways
1. Score each use case on business value and on feasibility, which covers data, risk, effort and skills.
2. Use the two-by-two matrix to find quick wins, strategic projects, small improvements and ideas to avoid.
3. Start with one or two quick wins and prepare the data and skills for one longer-term project.

## Hands-on Exercise
**Task:** Score at least five AI use cases for your organisation on value and feasibility, and choose your top two.
**Tools:** The CertifAI scoring template in this lesson, in a spreadsheet or on paper. Optional: Claude or ChatGPT to suggest more use cases, using general descriptions only.
**Steps:**
1. List at least five use cases. You can use your task list from L02.
2. Copy the scoring template and score each use case from 1 to 5 on value, data, risk, effort and skills.
3. Calculate the feasibility average for each use case.
4. Place each use case in one of the four boxes.
5. Choose your top two and write two sentences explaining each choice.
6. Ask a colleague to challenge one score, and change it if their argument is better.
**What good looks like:** A completed table with at least five use cases, scores with short reasons, at least one quick win in your top two, and one score that changed after discussion.
**Time:** about 30 minutes

## Review Flags
- [VERIFY] The curriculum refers to "free AI readiness or prioritisation templates" without naming one. This lesson uses a CertifAI-owned scoring template instead. A reviewer should confirm that this template replaces any third-party template, or choose one and confirm its licence allows use in a paid course.
