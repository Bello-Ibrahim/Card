# Screen Demo Pack: AI-18 L15 Monitoring Model Services

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L15_screen_1.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Open app.py and add the log_requests middleware
2. Restart the service
3. Run the traffic script: 300 requests with random valid inputs, every 25th with alcohol = 40
4. Show a few JSON request lines in predictions.jsonl

**Narration over this clip (for pacing)**

> She adds the middleware to the app and restarts the service. Then a short script sends three hundred requests with random valid inputs. Every twenty-fifth request has an alcohol value of forty, so it should be rejected. Each request line records the time, the path, the status and the latency in milliseconds.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L15_screen_2.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Open a Jupyter notebook in the project folder
2. Run the dashboard cell that reads predictions.jsonl with pandas
3. Highlight the hourly table: requests 300, error_rate 0.04, p95_ms 3.9
4. Filter to show the 12 rejected requests with status 422

**Narration over this clip (for pacing)**

> In a Jupyter notebook, she loads the log and builds the hourly table. It shows three hundred requests, an error rate of zero point zero four, that is twelve rejected requests, all with status four twenty-two, and a p ninety-five latency of three point nine milliseconds on our machine.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L15_screen_3.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Highlight the value counts: 94, 64, 59, 71 across the four probability bands
2. Run hourly['requests'].plot(kind='bar')
3. Plot a histogram of pred.probability

**Narration over this clip (for pacing)**

> Next, the prediction distribution. The four probability bands hold ninety-four, sixty-four, fifty-nine and seventy-one predictions, two hundred and eighty-eight in total. She adds a bar chart of requests per hour and a histogram of the probabilities. Later, a large change in these bands without a known reason would be a warning.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L15_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Add a markdown cell under the charts
2. Write alert rule 1 with metric, threshold, time window and owner
3. Write alert rule 2 for the prediction distribution with metric, threshold, window and owner

**Narration over this clip (for pacing)**

> Under the charts, she writes two alert rules, each with a metric, a threshold, a window and an owner. The four percent error rate here was caused on purpose. In production, she would find out which client sends the bad inputs.

## Production notes for this lesson

- [VERSION] FastAPI middleware syntax and pandas resample with named aggregation were tested with FastAPI 0.141.1 and pandas 3.0.6. The middleware and dashboard code are shown on screen and never read aloud.
- Dashboard numbers (300 requests, error rate 0.04 with 12 rejected requests all 422, p95 3.9 ms, probability bands 94, 64, 59 and 71 for 288 predictions) are real outputs from a local test with synthetic traffic. The voiceover says 'on our machine' for the latency. If the recording gives different numbers, show the recorded numbers and update the voiceover.
- Alert thresholds (server error rate above 1% for 15 minutes) are examples, not standards; the voiceover says so.
- Judgement call carried from the curriculum: monitoring uses structured logs and a simple pandas dashboard, not a full Prometheus or Grafana stack. Do not show other monitoring products.
- Use synthetic traffic only; no real personal data in the log on screen.
- Amara Diallo and the Dakar telecom company are hypothetical.
