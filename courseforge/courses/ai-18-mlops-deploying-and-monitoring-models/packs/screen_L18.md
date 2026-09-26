# Screen Demo Pack: AI-18 L18 Capstone Part 2: Monitor, Document and Present

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L18_screen_1.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show README.md and the dataset licence note
2. Show the architecture: training, MLflow, CI, GHCR, running container
3. Merge a small change and show the publish run creating an image tagged model-v3
4. Open /docs, send a valid request, then an out-of-range value returning 422

**Narration over this clip (for pacing)**

> He shows the README with the dataset licence note, and a simple architecture picture. Then he merges a small change, and the publish run creates an image tagged model v three. In the docs page, one valid request succeeds, and an out-of-range value returns four twenty-two.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L18_screen_2.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open the dashboard notebook: requests per hour, error rate, p95 latency, prediction histogram
2. Run the drift script on the drifted batch
3. Highlight the changed feature's PSI compared with the calibrated normal value
4. Show the written decision: Investigate before retraining

**Narration over this clip (for pacing)**

> He opens the dashboard with its four views. Then he runs the drift script on a batch where he increased one feature on purpose. PSI for that feature is far above his calibrated normal value, and he reads his decision: investigate before retraining.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L18_screen_3.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run: python rollback.py
2. Start the model-v2 image with -e MODEL_VERSION=2
3. Call /health
4. Send one request and show new log lines with model version 2

**Narration over this clip (for pacing)**

> Now the rollback. He runs the rollback script, starts the model v two image, and calls the health endpoint. New lines in the prediction log record model version two. The rollback worked.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L18_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Show the runbook rule: keep the last three images
2. Show a clean terminal, browser tabs and notebook with no secrets or personal data

**Narration over this clip (for pacing)**

> He ends with one lesson learned. His first rollback attempt failed, because an old image had been deleted. So he added a rule to keep the last three images. Before recording, he checked that no secret, token or personal data was visible anywhere.

## Production notes for this lesson

- [VERSION] GitHub Actions and GHCR interfaces shown in the demo should be checked before recording. The lesson page names a free screen recorder as an example; the voiceover says only 'any free screen recorder' and names no product.
- The rollback commands follow the alias-based scripts tested locally with MLflow 3.16.1. The rollback block and commands are shown on screen and never read aloud.
- content.md gives no real PSI value for Kofi's drifted feature, only that it is far above his calibrated normal value, so the voiceover states no number. Show whatever the recording prints.
- The ten-minute rollback target and the four-minute demo timings are course guidance, not industry standards.
- No secrets on screen: check the terminal, browser tabs and notebook for tokens, account names, tracking server addresses and personal data before recording, as Kofi does in the example.
- Kofi Mensah and the Kumasi solar-energy distributor are hypothetical.
