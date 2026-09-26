# L03 Fairness: Who Gets Helped and Who Gets Hurt | Presenter Script

Course: AI-29 · Video: 5 min · Words: 693

## Hook
A company tells you its AI tool is ninety percent accurate. That sounds good. But what if it is ninety-eight percent accurate for one group of people, and sixty percent for another? One number can hide a big difference.

## Explain
In the last lesson, you saw how bias can get into a system through the data, the design and the use. Now the question is, how do we notice it? The simplest method is to compare results between groups. A group can be defined by gender, age, region, language, disability, or anything else that matters for the task.

For each group, we look at a few simple numbers. The approval rate is the share of people who got the positive result. Forty approved out of a hundred is a forty percent approval rate.

The error rate is the share the system got wrong. And missed cases are the people who really qualified, or really were ill, but the system missed them. If these numbers are very different between groups, the system may be unfair, and you need to ask why.

Here is the difficult part. Fairness has more than one definition, and they can conflict. Equal approval rates means each group is approved at the same rate. Equal error rates means the system makes mistakes at the same rate for each group. When groups are different in real life, a system usually cannot meet both at once.

So people, not the computer, must decide which kind of fairness matters most for each use. A medical tool might focus on missing no sick patients. A hiring tool might focus on equal chances for equally qualified people.

Think of a school exam with an average score of seventy-five. That average says nothing about whether one classroom scored ninety and another scored sixty. A head teacher who only looks at the average will never find the classroom that needs help. Fairness checks look inside the average.

## Demonstrate
Let's see this in practice. Doctor Rafael Souza works for a health network in Brazil. The network uses an AI tool that flags patients at high risk of a heart problem, so they get an early check. The vendor says it is ninety percent accurate overall. That sounds reassuring. But Rafael wants to look inside the average.

Rafael asks for results by group, urban and rural patients. For urban patients, one hundred were really at high risk, and the tool missed ten. That is a ten percent missed-case rate. For rural patients, fifty were really at high risk, and the tool missed twenty-five. That is half of them.

Because most patients are urban, the overall number still looks good. So why is the tool worse for rural patients? Rural patients visit clinics less often, so they have fewer test results in their records. The tool had less information, and often guessed low risk.

The network decides which fairness goal matters most here. Missing as few high-risk patients as possible, in every group. Until the tool improves, every rural patient it rates as low risk also gets a short review by a nurse.

A common mistake is to trust one overall number and stop there. A large group can hide poor results in a small group. So always ask, accurate for whom? Another mistake is to think there is one correct fairness number. There are several, and choosing between them is a human decision, based on who could be hurt.

## Recap
Let's recap. First, you can check fairness by comparing results, such as approval rates, error rates and missed cases, between groups. Second, a good overall number can hide poor results for a smaller group. Third, different definitions of fairness can conflict, so people must choose which one matters most for each use.

## CTA
Now it is your turn. In the exercise below this video, you will use a small table of results for a scholarship tool to calculate approval rates and error rates for two groups. Then you will write two sentences on whether the tool looks fair. It takes about fifteen minutes. In the next lesson, we will look at hallucinations, misinformation and deepfakes. See you there.

## Thumbnail
Headline: Accurate for Whom?
Image: Navy background, a big '90%' badge cracking open to reveal two smaller bars of very different heights, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the health tool, its results table and the scholarship data are hypothetical on purpose, and no real statistics are used (content.md Review Flags: None). On-screen figures must be labelled 'Hypothetical'.
- Dr Rafael Souza and his health network in Brazil are fictional; stock footage must not show a real hospital name or logo.
- Scene 9 table: urban 800 patients, 100 at high risk, 90 flagged, 10 missed; rural 200 patients, 50 at high risk, 25 flagged, 25 missed. Keep these numbers exactly as in content.md.
