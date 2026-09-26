# L04 False Alarms and Missed Fraud: The Cost Trade-off | Presenter Script

Course: AI-24 · Video: 5 min · Words: 690

## Hook
A fraud model that blocks every payment catches all the fraud. It also stops every honest customer from buying anything. So where exactly should the line be drawn, and who pays for each mistake?

## Explain
In the last lesson, a fraud model gave each payment a risk score. Today we decide what to do with that score, and what each kind of mistake costs.

Every fraud model makes two kinds of error. A false positive is a false alarm. A genuine payment is blocked, the customer is embarrassed at the till, calls the contact centre, and may move to another bank. A false negative is missed fraud. The money is lost, and there are investigation and chargeback costs.

A confusion matrix puts all outcomes in one table. Fraud the model catches is a true positive. Fraud it misses is a false negative. A genuine payment it blocks is a false positive. And a genuine payment it approves is a true negative.

The institution picks a threshold. Any score above it is treated as fraud. A strict threshold flags more payments. It catches more fraud, but creates more false alarms. A relaxed threshold creates fewer false alarms, but misses more fraud. Moving the threshold alone cannot reduce both errors. Only a better model or better data does that.

So the right threshold depends on costs, not only on accuracy. Total cost equals missed fraud times the cost of one missed fraud, plus false alarms times the cost of one false alarm. Then you compare the totals.

A threshold is like the sensitivity setting on a smoke alarm. Set it very sensitive and it warns you about every real fire, and also every time you make toast. Set it less sensitive and the toast is quiet, but a small fire may be missed.

## Demonstrate
Marta Kowalska is a risk manager at a hypothetical payments company in Warsaw, Poland. She studies a synthetic set of ten thousand card payments. Fifty of them are fraud. At a strict threshold, she catches forty-five, misses five, and has four hundred false alarms. At a relaxed threshold, she catches thirty-five, misses fifteen, and has one hundred false alarms.

Each missed fraud costs three hundred on average. The cost of a false alarm is less certain, so she tests two assumptions. In assumption A, a false alarm costs five. The strict threshold then costs three thousand five hundred in total. The relaxed one costs five thousand. Strict is cheaper.

In assumption B, a false alarm costs twenty, because the payment is blocked at the till and the customer may leave. Now the strict threshold costs nine thousand five hundred. The relaxed one costs six thousand five hundred. Relaxed is cheaper.

The model has not changed. Only the business assumption has changed. So Marta's recommendation starts with the cost assumptions, and she asks the customer experience team for better evidence on the true cost of a false alarm.

A common mistake is to choose the threshold with the highest accuracy. With fifty fraud cases in ten thousand payments, a model that approves everything is ninety-nine point five percent accurate, and catches no fraud at all.

Always look at the two error types separately, and put a cost on each. Also remember that false alarms may not fall evenly on all customers. We look at that in lessons six and seven.

## Recap
Let's recap. First, false positives block genuine customers, and false negatives let fraud through. Both have real costs for the institution and the customer. Second, moving the threshold trades one error for the other, and only a better model or better data reduces both. Third, choose the threshold by comparing total costs under clear, stated cost assumptions, not by accuracy alone.

## CTA
Now it is your turn. In the exercise below this video, you will use the confusion-matrix sheet to try two thresholds and calculate the total cost per ten thousand transactions under two cost assumptions. Then write one sentence on which threshold you would choose, and why. It takes about twenty-five minutes. In the next lesson, we look at credit scoring with AI. See you there.

## Thumbnail
Headline: Who Pays for Mistakes?
Image: Navy background, a balance scale with a blocked card on one side and a stolen-money icon on the other, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the company, counts and cost figures are hypothetical and synthetic; all calculations were checked in content.md (content.md Review Flags: None).
- On-screen cost figures must match content.md exactly: Assumption A strict 3,500 and relaxed 5,000; Assumption B strict 9,500 and relaxed 6,500.
- Costs are 'in the company's currency'; do not show a currency symbol. Marta Kowalska and her Warsaw payments company are fictional.
