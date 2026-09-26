# Screen Demo Pack: AI-18 L09 Batch vs Online Serving and Performance

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L09_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Start the service: uvicorn app:app --port 8000
2. Show locustfile.py with the ApiUser class posting a valid wine to /predict
3. Run: locust -f locustfile.py --host http://127.0.0.1:8000
4. Open http://localhost:8089

**Narration over this clip (for pacing)**

> She load-tests the online service with Locust, a free, open-source tool. A short Python file describes one user who keeps sending a valid wine to the predict endpoint. She starts the service, starts Locust, and opens its web page.

## Clip 2: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L09_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Start a test with 5 users and a spawn rate of 10
2. Let it run for 20 seconds
3. Open the Statistics tab and highlight 16 requests per second, median 6 ms, 95th percentile 11 ms

**Narration over this clip (for pacing)**

> The first test uses five users for twenty seconds. On our machine, the service handled sixteen requests per second, with a median of six milliseconds and a p ninety-five of eleven milliseconds.

## Clip 3: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L09_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Stop the test
2. Start a new test with 50 users
3. Open the Statistics tab and highlight 145 requests per second, median 9 ms, 95th percentile 30 ms
4. Place the two results side by side

**Narration over this clip (for pacing)**

> Then she repeats with fifty users. Now it handled one hundred and forty-five requests per second. The median rose only to nine milliseconds, but the p ninety-five nearly tripled, to thirty milliseconds. That is queueing, and an average from one user would hide it.

## Clip 4: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L09_screen_4.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Show batch_score.py loading models:/wine-quality-clf@champion
2. Run: python batch_score.py new_batch.csv scored.csv
3. Show the output 'scored 500 rows -> scored.csv'
4. Open scored.csv and show the probability column

**Narration over this clip (for pacing)**

> Finally, the batch path. A short script loads the same champion model, scores a whole file, and writes a probability column. It prints scored five hundred rows. Because both paths use the same model version, online and batch predictions agree.

## Production notes for this lesson

- [VERSION] Locust is not in the brief's tool list; it is used as a free load-testing tool. Its web interface (port 8089, Statistics tab) and HttpUser API were checked against Locust 2.46.6 only. Check the current interface before recording.
- Load-test results (5 users: 16 requests per second, median 6 ms, p95 11 ms; 50 users: 145 requests per second, median 9 ms, p95 30 ms) and 'scored 500 rows' are real outputs from one laptop test with a local Uvicorn process (not the container), one worker and the synthetic model. The voiceover says 'on our machine'. If the recording gives different numbers, show the recorded numbers and update the voiceover to match.
- Katarzyna Nowak and the Kraków online shop are hypothetical.
