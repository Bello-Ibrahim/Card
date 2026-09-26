# L07 Measuring and Reducing Bias | Presenter Script

Course: AI-24 · Video: 5 min · Words: 707

## Hook
Two analysts check the same credit model. One reports that it is unfair to Group B. The other reports that it protects Group B from bad loans. Both used correct numbers. How can that be?

## Explain
In the last lesson, we measured the approval-rate ratio. But that only looks at decisions, not whether they were right. Error rates by group add that view. Today we measure them, and look at ways to reduce bias.

The false rejection rate asks: of the applicants who would have repaid, what share did the model decline? These are good customers wrongly turned away. The bad-loan approval rate asks: of the applicants who would not have repaid, what share did the model approve? These cause losses, and can leave borrowers with debt they cannot manage.

These measures can disagree. In general, you cannot make them all equal at once. So a team must choose which measure matters most for the decision, and explain why. Also, in real data we never see whether declined applicants would have repaid. In our synthetic data, we know the answer, which makes it good for learning.

You may hear of the four-fifths ratio, or zero point eight. It comes from US employment practice, not credit law. Treat it only as a rough rule of thumb that a gap needs investigating, never as a legal safe harbour for lending.

There are four main ways to reduce bias. Remove or change proxies. Rebalance the data, so the model learns from enough cases in each group. Add human review for applications near the threshold. And monitor the same fairness numbers every month, because they can change after launch.

## Demonstrate
Let's see this in Google Colab. Alejandro Ruiz is a risk analyst at Crédito Solar, a hypothetical consumer lender in Mexico. He uses the course's ready-made notebook, with one thousand three hundred synthetic loan decisions. No coding is needed. First, open the notebook link from the course page.

Next, save your own copy. Open the File menu and choose Save a copy in Drive. Now you can change it without affecting anyone else.

Here is what the code does. The first line lists how many applicants in each group repaid or not, and were approved or not. The rest builds a table and calculates three rates for each group, plus the approval-rate ratio. You do not need to change any of it yet.

Now open the Runtime menu and choose Run all. Wait a few seconds until the output table appears under the code. Check that your numbers match the table on the lesson page.

Group B's approval rate is fifty-six percent, against seventy-two point five percent for Group A. The ratio is zero point seven seven two. Group B's good payers are declined about twice as often: twenty-six point four percent, against thirteen point three. But the model approves far fewer bad loans for Group B: ten point seven percent, against thirty.

So both analysts were right. Alejandro reports the false rejection rate to his credit committee as the main measure, because it shows good customers being turned away. He recommends human review for Group B applications near the threshold.

Finally, try a change. In the counts line, change the number ninety-five to forty-five, and two hundred and sixty-five to three hundred and fifteen. Run all again. The ratio rises to zero point nine one, and Group B's false rejection rate falls to twelve point five percent.

## Recap
Let's recap. First, approval-rate ratios compare decisions, while error rates by group show whether those decisions were right. Second, fairness measures can disagree, so choose and justify the main measure, and treat the four-fifths ratio only as a rule of thumb. Third, reduce bias by removing proxies, rebalancing data, adding human review and monitoring results, and test again after every change.

## CTA
Now it is your turn. In the exercise below this video, you will run the same notebook, compare false rejection rates by group, and write three sentences on which fairness measure you would report to a credit committee, and why. It takes about thirty minutes. In the next lesson, we look at AI for customer service in banking. See you there.

## Thumbnail
Headline: Two Analysts, Two Answers
Image: Navy background, two report cards side by side with different teal and red bar charts for Group A and Group B, headline in teal Inter Bold.

## Production Notes
- [REGION] [VERIFY] The 'four-fifths' ratio comes from US employment practice and is not a general credit rule. The script presents it only as a rough rule of thumb and says it is not a legal safe harbour for lending; keep that wording and do not show any legal citation on screen.
- [VERSION] Google Colab free-tier limits and menu names (File > Save a copy in Drive, Runtime > Run all) must be checked against the live tool before recording.
- Screen demo: follow content.md Exercise steps 1 to 6 with the course's ready-made notebook on the 1,300 synthetic loan decisions. Record in a clean Google account with no personal files visible.
- Output figures must match content.md exactly: Group A 800 applicants, approval 0.725, false rejection 0.133, bad loans approved 0.300; Group B 500, 0.560, 0.264, 0.107; ratio 0.772 (spoken 'zero point seven seven two'). After the step 6 edit: ratio 0.91 and Group B false rejection 12.5%.
- Alejandro Ruiz and Crédito Solar are fictional. The presenter describes the code; it is never read aloud.
