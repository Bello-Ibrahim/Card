# L15 Monitoring Model Services | Presenter Script

Course: AI-18 · Video: 5 min · Words: 690

## Hook
Your service has returned status two hundred for every request this week. Is the model working? Not necessarily. A service can be perfectly healthy while its predictions slowly become wrong. You need to watch two layers, not one.

## Explain
Welcome to the final week. The first layer is service health. It tells you whether the API works. Watch traffic, meaning requests per hour. A sudden drop may mean a broken client, and a sudden rise may mean a retry loop. Watch the error rate, and separate client errors from server errors. And watch latency, the median and p ninety-five, as in lesson nine.

The second layer is model behaviour. It tells you whether the predictions still make sense. Watch the prediction distribution, for example the share of wines predicted good. Watch the input values compared with training. And when the true labels arrive, weeks later, join them to the log by request ID and compute the real metric.

Our prediction log from lesson seven records predictions only. To measure every request, including rejected ones, we add a small middleware that logs the path, the status and the latency. Without it, rejected requests would never appear in our numbers. Then a short pandas script reads the log. Structured logs and a script are enough to learn the ideas.

Alerts turn charts into action. Each alert needs a metric, a threshold, a time window and an owner. For example, server error rate above one percent for fifteen minutes, page the on-call engineer. That number is only an example. Start from your own normal values.

Think of a patient. The heart rate and temperature can be normal while a slow illness develops that only a blood test shows. A good doctor checks both.

## Demonstrate
Amara Diallo is an ML engineer at a hypothetical telecom company in Dakar, Senegal. She builds a dashboard for the wine service.

She adds the middleware to the app and restarts the service. Then a short script sends three hundred requests with random valid inputs. Every twenty-fifth request has an alcohol value of forty, so it should be rejected. Each request line records the time, the path, the status and the latency in milliseconds.

In a Jupyter notebook, she loads the log and builds the hourly table. It shows three hundred requests, an error rate of zero point zero four, that is twelve rejected requests, all with status four twenty-two, and a p ninety-five latency of three point nine milliseconds on our machine.

Next, the prediction distribution. The four probability bands hold ninety-four, sixty-four, fifty-nine and seventy-one predictions, two hundred and eighty-eight in total. She adds a bar chart of requests per hour and a histogram of the probabilities. Later, a large change in these bands without a known reason would be a warning.

Under the charts, she writes two alert rules, each with a metric, a threshold, a window and an owner. The four percent error rate here was caused on purpose. In production, she would find out which client sends the bad inputs.

The common mistake is to monitor only service health, because platforms show it by default. Add at least one model-behaviour signal from day one. And avoid too many sensitive alerts. People start to ignore them. Start with a few alerts that each lead to a clear action.

## Recap
Let's recap. First, monitor two layers: service health, meaning traffic, errors and latency, and model behaviour, meaning predictions, inputs and accuracy when labels arrive. Second, structured logs and a short pandas script are enough for a useful dashboard. Third, every alert needs a metric, a threshold, a time window and an owner, based on your own normal values.

## CTA
In the exercise below this video, you will add the middleware, send at least two hundred synthetic requests with some invalid ones, and build a notebook with a table, two charts and two alert rules. It takes about forty minutes. This dashboard will also be part of your capstone.

Next, we check whether today's data still looks like the training data, in Detecting Data and Prediction Drift. See you there.

## Thumbnail
Headline: Healthy Service, Wrong Answers?
Image: Navy background, a green status light on the left and a shifting histogram with a warning icon on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] FastAPI middleware syntax and pandas resample with named aggregation were tested with FastAPI 0.141.1 and pandas 3.0.6. The middleware and dashboard code are shown on screen and never read aloud.
- Dashboard numbers (300 requests, error rate 0.04 with 12 rejected requests all 422, p95 3.9 ms, probability bands 94, 64, 59 and 71 for 288 predictions) are real outputs from a local test with synthetic traffic. The voiceover says 'on our machine' for the latency. If the recording gives different numbers, show the recorded numbers and update the voiceover.
- Alert thresholds (server error rate above 1% for 15 minutes) are examples, not standards; the voiceover says so.
- Judgement call carried from the curriculum: monitoring uses structured logs and a simple pandas dashboard, not a full Prometheus or Grafana stack. Do not show other monitoring products.
- Use synthetic traffic only; no real personal data in the log on screen.
- Amara Diallo and the Dakar telecom company are hypothetical.
