# L18 Capstone Part 2: Monitor, Document and Present | Presenter Script

Course: AI-18 · Video: 5 min · Words: 681

## Hook
It is two in the morning. An alert fires, and the person who built the service is asleep. Can a colleague who has never seen your code understand the alert, and roll back safely in ten minutes? Your runbook and demo must make the answer yes.

## Explain
In part one, you built and automated your service. Part two completes the capstone with three additions. First, monitoring. Add the request logging and a dashboard with requests per hour, error rate, p ninety-five latency and the prediction distribution. Then add a drift script that compares recent inputs and predictions with the training data, and saves a small report with the date and model version.

Second, a one-page runbook. It is a short operational guide for the people who run the service. It has six headings: a service summary, deploy, roll back, alerts, drift response, and contacts and secrets. That last one says where credentials are stored, never the credentials themselves.

The rollback section can be short. Find the previous tags. Move the champion alias back with a small rollback script, which is the promote script from lesson fourteen in reverse. Start the previous image, check the health endpoint, send one known request, and record what happened. Aim for under ten minutes.

Third, a four-minute demo. Show the system working, not slides about it. Start with the problem and the dataset, then a merge that publishes an image, a prediction and a rejected input, the dashboard and a drift report, a rollback, and one lesson learned. Keep each part short, and practise the order before you record.

The runbook is like the emergency card in an aircraft seat pocket. It is short, it uses plain steps, and someone under stress who has never read it before can follow it.

## Demonstrate
Kofi Mensah is an ML engineer at a hypothetical solar-energy distributor in Kumasi, Ghana. His capstone predicts which customer solar kits will need a service visit. Here is his demo, in the suggested order.

He shows the README with the dataset licence note, and a simple architecture picture. Then he merges a small change, and the publish run creates an image tagged model v three. In the docs page, one valid request succeeds, and an out-of-range value returns four twenty-two.

He opens the dashboard with its four views. Then he runs the drift script on a batch where he increased one feature on purpose. PSI for that feature is far above his calibrated normal value, and he reads his decision: investigate before retraining.

Now the rollback. He runs the rollback script, starts the model v two image, and calls the health endpoint. New lines in the prediction log record model version two. The rollback worked.

He ends with one lesson learned. His first rollback attempt failed, because an old image had been deleted. So he added a rule to keep the last three images. Before recording, he checked that no secret, token or personal data was visible anywhere.

The common mistake is a runbook full of architecture but with no exact commands. Under pressure, roll back to the previous version is not enough. Which version, which command, which permission? Write the real commands, and test each one from a clean terminal.

## Recap
Let's recap. First, part two adds monitoring, a one-page runbook and a four-minute demo. Second, a good runbook gives exact deploy and rollback commands, the meaning and first action for each alert, and drift decision rules. Third, demonstrate the real system, including a rollback, and never show secrets or personal data on screen.

## CTA
Your exercise is capstone step two. Add the dashboard and drift reports for a normal and a drifted batch, write the runbook, rehearse the rollback, and record your demo with any free screen recorder. Then submit your repository link, runbook, dashboard, drift reports and video. Plan about two hours.

Congratulations. You have taken a model from a notebook to a tested, versioned and monitored service, with a plan for when things go wrong. Submit your capstone, and be proud of it. Well done.

## Thumbnail
Headline: Ready for 2 a.m.?
Image: Navy background, a night-time clock at 2:00 beside a one-page checklist with a rollback arrow, headline in teal Inter Bold.

## Production Notes
- [VERSION] GitHub Actions and GHCR interfaces shown in the demo should be checked before recording. The lesson page names a free screen recorder as an example; the voiceover says only 'any free screen recorder' and names no product.
- The rollback commands follow the alias-based scripts tested locally with MLflow 3.16.1. The rollback block and commands are shown on screen and never read aloud.
- content.md gives no real PSI value for Kofi's drifted feature, only that it is far above his calibrated normal value, so the voiceover states no number. Show whatever the recording prints.
- The ten-minute rollback target and the four-minute demo timings are course guidance, not industry standards.
- No secrets on screen: check the terminal, browser tabs and notebook for tokens, account names, tracking server addresses and personal data before recording, as Kofi does in the example.
- Kofi Mensah and the Kumasi solar-energy distributor are hypothetical.
