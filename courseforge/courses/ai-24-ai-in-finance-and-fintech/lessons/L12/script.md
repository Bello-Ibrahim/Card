# L12 Model Risk Management and Monitoring | Presenter Script

Course: AI-24 · Video: 5 min · Words: 682

## Hook
A fraud model passes every test at launch. Six months later, false alarms have doubled, and a new type of fraud is getting through. Nobody changed the model. So what changed, and whose job was it to notice?

## Explain
Last time, model risk management was one of our six principles. Now we look at it closely. Model risk is the risk of loss or harm because a model is wrong, is used wrongly, or stops working as intended. Managing it has four main parts.

Part one is a model inventory: a list of every model in use, with its purpose, owner, data, validation date and risk rating. You cannot manage a model you do not know exists, and that includes vendor models and AI assistants. Part two is independent validation. Before launch, and at regular intervals, people who did not build the model test it, and they can require changes before approval.

Part three is performance and drift monitoring. After launch, the owner measures the model regularly. For fraud, performance means the share of fraud caught and the false alarm rate. For credit, it means default rates by score band. The owner also watches data drift, score drift and fairness. An amber limit triggers investigation. A red limit triggers action, such as retraining, changing the threshold, or pausing the model.

Part four is the three lines of defence. The first line is the business and model owners, who build, use and monitor the model every day. The second line is independent risk and compliance, who set standards, validate and challenge. The third line is internal audit, which checks that the whole system works.

One question matters in every institution. Who has the authority to pause a model? Write it down before launch, with a fallback process ready, such as rules only or manual review.

Think of a regular vehicle safety inspection. A car that was safe when it left the factory can develop worn brakes and weak tyres. You inspect on a schedule, with clear pass and fail limits, and an inspector can take an unsafe car off the road.

## Demonstrate
Remember the Lagos card issuer from lesson three? Ifeoma Eze is its head of model risk, and she writes a monitoring plan for the fraud model. Her limits are illustrative, set by the issuer for this model. First, the share of fraud caught, measured monthly once labels mature after sixty days. Amber is below eighty percent. Red is below seventy.

The false alarm rate is checked weekly, with amber above three percent and red above five. The score distribution is compared with launch every month. Missing values in key fields are checked daily. And every quarter, the second line compares false alarm rates across customer groups. Amber is a ratio above one point two five, and red is above one point five.

Red limits go to the model risk committee within two working days. The chief risk officer has the authority to pause the model. If it is paused, the issuer falls back to its fraud rules and extra manual review. And internal audit reviews the whole process once a year.

A common mistake is to treat validation at launch as the end of model risk work. It is the start. Data, customers and fraud patterns change. And a plan without named people, limits and a pause authority is not a monitoring plan.

## Recap
Let's recap. First, model risk management needs an inventory, independent validation, ongoing monitoring with limits, and clear owners. Second, the three lines of defence separate the people who build and use models, the people who challenge them, and the people who audit the system. Third, decide before launch who can pause a model, and what the fallback process is.

## CTA
Now it is your turn. In the exercise below this video, you will draft a one-page monitoring plan for the fraud model from lesson three: what to measure, how often, which limits trigger action, and who acts. It takes about thirty minutes. In the next lesson, we start your capstone, by scoping your AI use case proposal. See you there.

## Thumbnail
Headline: Who Can Pause the Model?
Image: Navy background, a dashboard with green, amber and red gauges and a large teal pause button, headline in teal Inter Bold.

## Production Notes
- [REGION] [VERIFY] Content.md mentions US supervisory model risk guidance SR 11-7 as an example. The voiceover leaves it out and teaches the three lines of defence as a general framework; if a slide names it, confirm it is current first.
- [VERSION] Free-plan access and data-use terms of Claude and ChatGPT (optional in the exercise) must be checked before recording.
- Monitoring limits are illustrative, set by the hypothetical issuer for this model, not industry standards. Figures must match content.md (fraud caught amber below 80%, red below 70%; false alarm rate amber above 3%, red above 5%; missing values amber above 2%, red above 5%; group ratio amber above 1.25, red above 1.5; red limits to committee within two working days).
- Ifeoma Eze and the Lagos card issuer (from L03) are fictional.
