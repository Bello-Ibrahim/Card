# L03 Fairness: Who Gets Helped and Who Gets Hurt

Course: AI-29 · Module: M1 · Objectives: O2, O5 · Video: 5 min

## Hook
A company tells you its AI tool is "90% accurate". That sounds good. But what if it is 98% accurate for one group of people and 60% accurate for another? One number can hide a big difference.

## Explanation
In L02 you saw how bias gets into a system. Now the question is: how do we notice it? The simplest method is to **compare results between groups**.

A group can be defined by gender, age, region, language, disability or any other characteristic that matters for the task. For each group, we look at a few simple numbers:

- **Selection rate (or approval rate):** out of everyone in the group, what share got the positive result? For example, 40 approved out of 100 applicants is a 40% approval rate.
- **Error rate:** out of everyone in the group, what share did the system get wrong?
- **Missed cases:** out of the people who really had a condition or really qualified, what share did the system miss? This matters when missing someone causes harm, such as a missed illness.

If these numbers are very different between groups, the system may be unfair, and you need to ask why.

There is a difficulty. **Fairness has more than one definition, and they can conflict.** For example:
- "Equal approval rates" means each group is approved at the same rate.
- "Equal error rates" means the system makes mistakes at the same rate for each group.

If the groups are different in real life, for example if one group really has more cases of a disease, a system usually cannot meet both definitions at the same time. People, not the computer, must decide which kind of fairness matters most for each use. A medical tool might focus on missing no sick patients. A hiring tool might focus on equal chances for equally qualified people.

**Analogy:** Think of a school exam with an average score of 75. That average says nothing about whether one classroom scored 90 and another scored 60. A head teacher who only looks at the average will never find the classroom that needs help. Fairness checks look inside the average.

## Worked Example
Dr Rafael Souza works for a hypothetical health network in Brazil. The network uses an AI tool that reads patient information and flags people at high risk of a heart problem, so they get an early check.

The vendor reports that the tool is 90% accurate overall. Rafael asks for the results by group: urban patients and rural patients. In a test of 1,000 hypothetical patients he gets this table:

| Group | Patients | Really at high risk | Correctly flagged | Missed |
|---|---|---|---|---|
| Urban | 800 | 100 | 90 | 10 |
| Rural | 200 | 50 | 25 | 25 |

For urban patients, the tool misses 10 of 100 high-risk patients: a 10% missed-case rate. For rural patients, it misses 25 of 50: a 50% missed-case rate. Because most patients are urban, the overall accuracy still looks good.

Rafael asks why. Rural patients visit clinics less often, so they have fewer test results in their records. The tool had less information and often guessed "low risk".

The network decides that, for this tool, "missing as few high-risk patients as possible in every group" is the fairness goal that matters most. Until the tool improves, every rural patient it rates as low risk also gets a short review by a nurse.

## Common Mistake
A common mistake is to trust one overall number, such as "90% accurate", and to stop there. Overall accuracy mixes all groups together, so a large group can hide poor results in a small group. The correction: always ask "accurate for whom?" and request results for each relevant group. Another mistake is to think there is one correct fairness number. There are several, and choosing between them is a human decision based on who could be hurt.

## Key Takeaways
1. You can check fairness by comparing results, such as approval rates, error rates and missed cases, between groups.
2. A good overall number can hide poor results for a smaller group, so always ask "accurate for whom?"
3. Different definitions of fairness can conflict, so people must choose which one matters most for each use.

## Hands-on Exercise
**Task:** Use a small table of hypothetical results for two groups to calculate approval rates and error rates, then write 2 sentences on whether the tool looks fair and why.
**Tools:** Pen and paper, a calculator, or any spreadsheet app.
**Steps:**
1. Read this hypothetical table for a scholarship tool that recommends students for interviews:

| Group | Applicants | Approved | Wrong decisions (checked later by staff) |
|---|---|---|---|
| Group A | 200 | 80 | 20 |
| Group B | 100 | 20 | 25 |

2. Calculate the approval rate for each group: approved divided by applicants.
3. Calculate the error rate for each group: wrong decisions divided by applicants.
4. Compare the two groups. Which group is approved less often? Which group has more errors?
5. Write 2 sentences: does the tool look fair, and why or why not? Name one question you would ask next.
**What good looks like:** Correct results: Group A approval 40% and error rate 10%; Group B approval 20% and error rate 25%. Your sentences say the tool looks unfair to Group B, because it approves them half as often and makes more mistakes for them. Your next question is specific, such as "Is Group B missing from the training data?"
**Time:** about 15 minutes

## Review Flags
- None. The health tool, the table and the scholarship data are hypothetical on purpose, as the curriculum requires, and no real statistics are used.
