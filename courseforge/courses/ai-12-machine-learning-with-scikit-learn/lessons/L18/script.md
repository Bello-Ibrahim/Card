# L18 Capstone Step 2: Report to Stakeholders | Presenter Script

Course: AI-12 · Video: 5 min · Words: 717

## Hook
ROC AUC zero point seven five, recall zero point six seven, at a threshold of zero point one five. To a data scientist, that is a clear result. To a sales director, it means nothing. And a model that nobody understands will not be used.

## Explain
In the last lesson, you built, tested and saved your model. Your last task is to explain it in the language of the business. A stakeholder report is one page, for people who make decisions, not for people who build models.

It answers six questions, in order. What decision does the model support? What does it do, in one or two sentences, with no algorithm names? How well does it perform, in business terms? What are its limits? What are the risks? And what do you recommend?

Performance in business terms means counts that people can picture. Precision becomes, of every hundred customers we call, about this many subscribe. Recall becomes, we reach about this many out of every ten who would subscribe. And always compare with the current way of working.

Write for a busy reader. Use short sentences and plain words. Put the most important numbers in one small table, and add a summary of three sentences at the top: what the model does, how much it helps, and what you recommend.

Be honest about uncertainty. Round your numbers, and say what they are based on, such as tested on five hundred past customers the model had not seen. If an AI assistant helps with wording, share only summary numbers and your own text, never customer data.

A good report is like a weather forecast on the evening news. The forecaster does not explain the physics of air pressure. She says, seventy percent chance of rain tomorrow afternoon, take an umbrella. You get the result, how sure it is, and what to do.

## Demonstrate
Kwame Mensah is a data analyst at a bank in Accra, Ghana. His model is the term-deposit pipeline from this course, with the threshold of zero point one five from lesson nine.

On a test set of five hundred past customers, sixty had subscribed. The model selected one hundred and thirty-seven customers to call, and forty of them had subscribed. It missed the other twenty subscribers.

Kwame turns these counts into business statements. If we call the customers the model selects, about twenty-nine of every hundred calls lead to a subscription. If we call customers at random, about twelve of every hundred do.

The model's list reaches about two out of every three customers who would subscribe, while calling only about a quarter of all customers. And it works less well for customers aged thirty-one to fifty, where it reaches about half of the subscribers.

His summary for the head of retail, Isabel Duarte, reads: We built a score that ranks customers by how likely they are to open a term deposit. In a test on five hundred past customers, calling the top-ranked quarter reached two thirds of the subscribers, with more than twice as many subscriptions per call as random calling.

We recommend a one-month trial in one region, with a monthly check of results by age group. His limits section notes that the test used past data only, some age groups had few subscribers, and call outcomes may change with interest rates.

A common mistake is to copy the classification report into the stakeholder report, or to describe the method in detail. Readers stop at the first unknown term. Another is to hide the limits. Stakeholders who later find a hidden weakness stop trusting both the model and its author.

## Recap
Let's recap. First, a one-page report covers the problem, what the model does, performance in business terms, limits, risks, and a recommendation. Second, turn metrics into counts people can picture, and compare with a baseline. Third, start with a three-sentence summary, avoid jargon, and state limits and risks honestly.

## CTA
Congratulations. You have finished Machine Learning with scikit-learn. Your last exercise is capstone step two: write your one-page report and three-sentence summary, and ask someone without a data background to read it. It takes about an hour. Then submit your notebook, your model file and your report as your capstone. Well done, and good luck.

## Thumbnail
Headline: Speak the Business Language
Image: Navy background, a one-page report with a small four-number table and a highlighted three-line summary at the top, headline in teal Inter Bold.

## Production Notes
- No facts to verify: the bank and all numbers are hypothetical or come from the course's synthetic data, run in L09 and L16 (content.md Review Flags: None).
- This lesson is not a screen demo: slides, stock and one hero clip only. No notebook is shown.
- Numbers check: 500 test customers, 60 subscribers; at the 0.15 threshold the model selects 137, of whom 40 subscribed (about 29 in 100), and misses 20 (reaches 40 of 60, about 2 in 3). Random calling gives about 12 in 100 (60 of 500). 137 of 500 is about a quarter.
- Scene 4 hero clip is 7 seconds and the scene is about 20 seconds: hold with a slow push-in, then cut.
- Kwame Mensah, Isabel Duarte and the Accra bank are fictional. Stock footage must not show a real bank's name or logo.
