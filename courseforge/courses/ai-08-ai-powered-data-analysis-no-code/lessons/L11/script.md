# L11 Checking AI Insights for Errors | Presenter Script

Course: AI-08 · Video: 5 min · Words: 692

## Hook
The AI's answer is well written, uses exact numbers, and sounds certain. But three of its four sentences are wrong or misleading. Would you notice before your manager did?

## Explain
Welcome to week three. Last time, you built a dashboard. Now we learn to check AI insights before you share them.

AI analysis errors follow a few common patterns. The first is the wrong column, for example it reports units when you asked about revenue. The second is ignored rows. It skips blank or badly formatted rows, so counts and averages change. The third is mixing up totals and averages. It calls a total an average, or divides by the wrong count.

The fourth is an invented cause. The AI explains why something happened, with information that is not in the data. And the fifth is a trend from too little data. It sees strong growth in three months, or in one large value.

A short, five-point checking routine catches most of these. One, recalculate one number yourself, with a formula or a pivot table. Two, check row counts. Ask how many rows the AI used, and compare with your sheet. Three, look at the chart, and see whether one value drives the pattern.

Four, ask, compared with what? Is there a fair comparison, such as a previous period or another group? Five, look for other explanations. Is the cause in the data, or did the AI add it? Could a third factor or one unusual event explain it?

You do not need to check every sentence to the last decimal. But every number and claim you pass on to others should survive this routine.

It is like checking a restaurant bill before you pay. You do not redo every sum. But you check the total, count the dishes, and ask about any item you did not order.

## Demonstrate
Ingrid works in revenue management at a hotel in Bergen, Norway. She uploads a fictional, anonymised file of two hundred bookings.

The AI says, the average stay is three point five nights. Guests from Germany stay longest, so the hotel should advertise in Germany.

She applies the routine. First, row count. The AI used only one hundred and eighty-eight rows. Twelve bookings, all long stays for a company contract, had a blank nationality cell, and the AI dropped them. Her own average over all two hundred rows gives three point eight nights.

Next, compared with what? The German result is based on only four bookings. That is too few to support an advertising decision.

Then, other explanations. The data has no information about advertising. So the recommendation is the AI's idea, not a finding. Ingrid reports the corrected average, and marks the Germany point, needs more data. Notice that each check found a different problem. One check alone would not have been enough.

In your exercise, you will check an AI answer about the orders sheet. It has four insights. Total revenue and the average order. The strongest region. Monthly growth with a forecast. And the share from office chairs. Some of them contain planted errors. Your job is to find them.

A common mistake is to check only whether the numbers are correct. But a sentence can use correct numbers and still mislead, through a missing comparison, a trend built on one value, or an invented cause. Check the reasoning as well as the arithmetic.

## Recap
Let's recap. First, common AI errors are the wrong column, ignored rows, totals mixed with averages, invented causes, and trends from too little data. Second, use the five-point routine. Recalculate one number, check row counts, look at the chart, ask compared with what, and look for other explanations. Third, correct numbers can still support a misleading conclusion, so check the reasoning too.

## CTA
Now it is your turn. In the exercise below this video, you will review those four AI insights, and use the five-point routine to find and correct the planted errors. It takes about twenty-five minutes. This routine will also guide your capstone, a five-slide business insight report. You start it in the next lesson, Capstone, Explore Your Dataset. See you there.

## Thumbnail
Headline: Would You Spot It?
Image: Navy background, a confident AI chat answer with three of four lines underlined in amber and a teal magnifying glass over it, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the Bergen hotel case, the orders dataset and the AI answer are fictional, and the planted errors are deliberate teaching material (content.md Review Flags: None).
- Spoken numbers match content.md: 200 bookings; AI average 3.5 nights; 188 rows used; 12 blank-Nationality long stays dropped; Ingrid's average over 200 rows 3.8 nights; Germany based on 4 bookings.
- Scene 13 slide shows the four planted-error insights word for word from content.md. Do NOT show or speak the answer key in the video: learners find the errors in the exercise.
- Stock footage of the hotel must show no real hotel names or logos.
