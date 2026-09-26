# HeyGen Batch Pack: AI-18 M4 (Monitoring in Production: Capstone)

Course: MLOps: Deploying and Monitoring Models. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L15 Monitoring Model Services

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M4_L15_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
Your service has returned status two hundred for every request this week. Is the model working? Not necessarily. A service can be perfectly healthy while its predictions slowly become wrong. You need to watch two layers, not one.

Welcome to the final week. The first layer is service health. It tells you whether the API works. Watch traffic, meaning requests per hour. A sudden drop may mean a broken client, and a sudden rise may mean a retry loop. Watch the error rate, and separate client errors from server errors. And watch latency, the median and p ninety-five, as in lesson nine.

The second layer is model behaviour. It tells you whether the predictions still make sense. Watch the prediction distribution, for example the share of wines predicted good. Watch the input values compared with training. And when the true labels arrive, weeks later, join them to the log by request ID and compute the real metric.

Our prediction log from lesson seven records predictions only. To measure every request, including rejected ones, we add a small middleware that logs the path, the status and the latency. Without it, rejected requests would never appear in our numbers. Then a short pandas script reads the log. Structured logs and a script are enough to learn the ideas.

Alerts turn charts into action. Each alert needs a metric, a threshold, a time window and an owner. For example, server error rate above one percent for fifteen minutes, page the on-call engineer. That number is only an example. Start from your own normal values.

Think of a patient. The heart rate and temperature can be normal while a slow illness develops that only a blood test shows. A good doctor checks both.

Amara Diallo is an ML engineer at a hypothetical telecom company in Dakar, Senegal. She builds a dashboard for the wine service.

She adds the middleware to the app and restarts the service. Then a short script sends three hundred requests with random valid inputs. Every twenty-fifth request has an alcohol value of forty, so it should be rejected. Each request line records the time, the path, the status and the latency in milliseconds.

In a Jupyter notebook, she loads the log and builds the hourly table. It shows three hundred requests, an error rate of zero point zero four, that is twelve rejected requests, all with status four twenty-two, and a p ninety-five latency of three point nine milliseconds on our machine.

Next, the prediction distribution. The four probability bands hold ninety-four, sixty-four, fifty-nine and seventy-one predictions, two hundred and eighty-eight in total. She adds a bar chart of requests per hour and a histogram of the probabilities. Later, a large change in these bands without a known reason would be a warning.

Under the charts, she writes two alert rules, each with a metric, a threshold, a window and an owner. The four percent error rate here was caused on purpose. In production, she would find out which client sends the bad inputs.

The common mistake is to monitor only service health, because platforms show it by default. Add at least one model-behaviour signal from day one. And avoid too many sensitive alerts. People start to ignore them. Start with a few alerts that each lead to a clear action.

Let's recap. First, monitor two layers: service health, meaning traffic, errors and latency, and model behaviour, meaning predictions, inputs and accuracy when labels arrive. Second, structured logs and a short pandas script are enough for a useful dashboard. Third, every alert needs a metric, a threshold, a time window and an owner, based on your own normal values.

In the exercise below this video, you will add the middleware, send at least two hundred synthetic requests with some invalid ones, and build a notebook with a table, two charts and two alert rules. It takes about forty minutes. This dashboard will also be part of your capstone.

Next, we check whether today's data still looks like the training data, in Detecting Data and Prediction Drift. See you there.
```

## L16 Detecting Data and Prediction Drift

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M4_L16_presenter.mp4`
- **Expected length:** about 5.0 minutes (691 words). The quality gate accepts ±10%.

```text
Nothing in your code changed, and your tests still pass. But the data your model sees today is not the data it learned from. How do you notice, and what should you do?

In the last lesson, we watched our service. Now we look for drift. Drift means production data no longer looks like the training data. Three kinds matter. Data drift is when an input feature changes, for example average alcohol rises. Prediction drift is when the model's outputs change, for example many more good predictions.

Concept drift is when the relationship between the inputs and the true outcome changes. You can only measure it when true labels arrive. To detect data and prediction drift, compare a reference sample, your training data, with a current sample, your recent requests, one feature at a time.

Two methods are common. The Kolmogorov-Smirnov test, or KS, measures the largest gap between two distributions and gives a p-value. But with thousands of rows, even tiny, harmless differences look significant. So do not use the p-value alone.

The population stability index, or PSI, splits the reference into bins, and compares the share of rows in each bin. It measures the size of the shift, not only whether one exists. You will read common rules of thumb for PSI, but they are not a standard. Calibrate on your own data, for example between two normal weeks.

Drift is a signal, not a decision. For each alert, choose one of three responses. Retrain when the change is real, lasting and important, and you have new labels. Investigate when the cause is unclear, because it may be a pipeline bug. Ignore when the feature matters little, or the change is expected and short.

Think of a shop that sells winter coats and notices who walks in. If the customers suddenly look different, the shop first asks why, before it changes its stock.

Sofía Castro is a risk analyst at a hypothetical lender in Medellín, Colombia. After an online campaign, many younger applicants with shorter credit histories apply. PSI for age and credit history rises above her calibrated level. Her team investigates first, confirms the change is real, then retrains and reviews fairness, following local lending rules.

Let's simulate the same idea with the wine model. In a notebook, we load a reference sample and a new batch with a different seed. Then we add zero point eight to alcohol in the new batch only.

We run the PSI and KS loop for every feature. Alcohol has a PSI of zero point five zero five, and a KS p-value that is almost zero. The other features have PSI close to zero: zero point zero zero three, zero point zero one one and zero point zero zero six. Only alcohol shifted.

Next, we check prediction drift. We compute PSI on the model's predicted probabilities for both batches. This tells us whether the input shift is also changing the answers.

Finally, we write the decision in the notebook. Investigate. Check whether the alcohol measurement or unit changed at the source. Retrain only if the change is real and labels are available.

The common mistake is to retrain automatically every time a drift test fires. If the cause is a broken pipeline, retraining teaches the model the bug. Investigate first, and keep retraining behind the champion and challenger comparison from lesson fourteen.

Let's recap. First, data drift, prediction drift and concept drift are different, and only concept drift needs true labels. Second, use PSI for the size of a shift and KS as support, and calibrate any thresholds on your own data. Third, for each drift alert, decide to retrain, investigate or ignore, and investigate before retraining.

In the exercise below this video, you will change one feature in a batch of at least five hundred rows, compute PSI and KS for every feature and for the predictions, calibrate on unchanged data, and write a short decision. It takes about thirty-five minutes. Your capstone needs two drift reports like this.

Now you have every piece. In the next lesson, Capstone Part 1: Build and Automate, you put them together. See you there.
```

## L17 Capstone Part 1: Build and Automate

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M4_L17_presenter.mp4`
- **Expected length:** about 4.9 minutes (683 words). The quality gate accepts ±10%.

```text
You have built each part of a production ML system separately. Now you connect them, in one repository, where a single merge to main produces a tested, versioned, deployable model API, without any manual copying.

Welcome to the capstone. You will deploy and monitor a model API. Part one, this lesson, covers the build and the automation. Part two, the final lesson, adds monitoring, a runbook and a short demo.

First, choose a dataset and a problem. Pick a public tabular dataset with a clear prediction target, a licence that allows your use, and no personal data. Write the source and licence in your README. You may continue with the wine example, but a new dataset shows more skill. If you cannot download data, use a synthetic dataset with a fixed seed, as in lesson three.

Your repository needs seven parts. Reproducible training with pinned packages and fixed seeds. Tracking and a registry, with at least three runs and a champion model tagged with its data hash and Git commit. A FastAPI service with validation and structured logs. And a slim container that runs as a non-root user.

Then the automation. Tests of all four types. CI that runs them on every push and pull request, with main protected. And publishing, so every merge builds and pushes an image tagged with the commit ID and the model version.

The rubric gives points for training and versioning, the containerised API with tests and CI and CD, monitoring and drift, the release and rollback plan, and the runbook and demo. Read it now, so you collect evidence while you build. Keep screenshots of your MLflow runs, the registry page, a blocked pull request and the published image.

The capstone is like assembling a car from parts you have already tested one by one. The engine, brakes and lights each worked on the bench. Now you fit them together, connect the wires, and prove that the whole car drives.

Leila Haddad is a data scientist at a hypothetical insurance company in Casablanca, Morocco. For her capstone, she predicts whether a household appliance will need repair within a year, using a public tabular dataset with no personal data.

She starts from her template from lesson three, replaces the data loader with one for her dataset, and writes the source and licence in the README. She trains twice and shows identical metrics.

She logs four runs to MLflow, compares them, and registers the best. The registry shows the champion alias, the data hash tag and the commit tag.

She exports the model, builds the image and runs the container. From the interactive docs page, she sends one valid request and one invalid request. Then she runs pytest, and all tests pass.

She pushes a branch with a broken quality gate and opens a pull request. The merge is blocked. She fixes it and merges. In Actions and Packages, the new image appears with its commit tag and model tag. She adds each screenshot to her evidence list, with one link or screenshot for each rubric criterion.

The common mistake is to build all the parts first and connect them on the last day. Then all the integration problems appear together. Connect the pipeline early, even with a simple model. A working thin pipeline is worth more than perfect parts that do not connect.

Let's recap. First, capstone part one connects reproducible training, MLflow tracking and registry, a FastAPI service, Docker, tests and CI and CD, in one repository. Second, choose a public dataset with a clear licence and no personal data, and document the source. Third, connect the whole pipeline early, and collect evidence for each rubric criterion as you build.

Your exercise is capstone step one. Build a repository where every push runs tests, a failing test blocks merging, and every merge publishes an image tagged with the commit and model version. Commit no secrets, personal data or large data files. Plan about two hours.

In the final lesson, Capstone Part 2: Monitor, Document and Present, you add monitoring, a runbook and your demo. See you there.
```

## L18 Capstone Part 2: Monitor, Document and Present

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M4_L18_presenter.mp4`
- **Expected length:** about 4.9 minutes (672 words). The quality gate accepts ±10%.

```text
It is two in the morning. An alert fires, and the person who built the service is asleep. Can a colleague who has never seen your code understand the alert, and roll back safely in ten minutes? Your runbook and demo must make the answer yes.

In part one, you built and automated your service. Part two completes the capstone with three additions. First, monitoring. Add the request logging and a dashboard with requests per hour, error rate, p ninety-five latency and the prediction distribution. Then add a drift script that compares recent inputs and predictions with the training data, and saves a small report with the date and model version.

Second, a one-page runbook. It is a short operational guide for the people who run the service. It has six headings: a service summary, deploy, roll back, alerts, drift response, and contacts and secrets. That last one says where credentials are stored, never the credentials themselves.

The rollback section can be short. Find the previous tags. Move the champion alias back with a small rollback script, which is the promote script from lesson fourteen in reverse. Start the previous image, check the health endpoint, send one known request, and record what happened. Aim for under ten minutes.

Third, a four-minute demo. Show the system working, not slides about it. Start with the problem and the dataset, then a merge that publishes an image, a prediction and a rejected input, the dashboard and a drift report, a rollback, and one lesson learned. Keep each part short, and practise the order before you record.

The runbook is like the emergency card in an aircraft seat pocket. It is short, it uses plain steps, and someone under stress who has never read it before can follow it.

Kofi Mensah is an ML engineer at a hypothetical solar-energy distributor in Kumasi, Ghana. His capstone predicts which customer solar kits will need a service visit. Here is his demo, in the suggested order.

He shows the README with the dataset licence note, and a simple architecture picture. Then he merges a small change, and the publish run creates an image tagged model v three. In the docs page, one valid request succeeds, and an out-of-range value returns four twenty-two.

He opens the dashboard with its four views. Then he runs the drift script on a batch where he increased one feature on purpose. PSI for that feature is far above his calibrated normal value, and he reads his decision: investigate before retraining.

Now the rollback. He runs the rollback script, starts the model v two image, and calls the health endpoint. New lines in the prediction log record model version two. The rollback worked.

He ends with one lesson learned. His first rollback attempt failed, because an old image had been deleted. So he added a rule to keep the last three images. Before recording, he checked that no secret, token or personal data was visible anywhere.

The common mistake is a runbook full of architecture but with no exact commands. Under pressure, roll back to the previous version is not enough. Which version, which command, which permission? Write the real commands, and test each one from a clean terminal.

Let's recap. First, part two adds monitoring, a one-page runbook and a four-minute demo. Second, a good runbook gives exact deploy and rollback commands, the meaning and first action for each alert, and drift decision rules. Third, demonstrate the real system, including a rollback, and never show secrets or personal data on screen.

Your exercise is capstone step two. Add the dashboard and drift reports for a normal and a drifted batch, write the runbook, rehearse the rollback, and record your demo with any free screen recorder. Then submit your repository link, runbook, dashboard, drift reports and video. Plan about two hours.

Congratulations. You have taken a model from a notebook to a tested, versioned and monitored service, with a plan for when things go wrong. Submit your capstone, and be proud of it. Well done.
```
