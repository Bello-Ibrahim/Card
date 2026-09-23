# L18 Capstone Part 2: Monitor, Document and Present

Course: AI-18 · Module: M4 · Objectives: O5, O6, O7 · Video: 5 min (screen demo)

## Hook
It is 2 a.m., an alert fires, and the person who built the service is asleep. Can a colleague who has never seen your code understand the alert, decide what to do, and roll back safely in ten minutes? Your runbook and demo must make the answer "yes".

## Explanation
Part 2 completes the capstone with three additions.

**1. Monitoring.** Your service already writes structured logs (L07). Add the request-logging middleware and a dashboard notebook that shows requests per hour, error rate, p95 latency and the prediction distribution (L15). Add a drift check script that compares a recent batch of logged inputs with the training data using PSI and a KS test, and also checks the predictions (L16). Save its output as a small report that includes the date and model version.

**2. A one-page runbook.** A runbook is a short operational guide for the people who run the service. Use these headings:

- **Service summary:** what the model predicts, who uses it and the current model version.
- **Deploy:** the exact steps or workflow that publish a new version.
- **Roll back:** the exact commands to return to the previous image and model version, and who may run them.
- **Alerts:** for each alert, what it means, the likely causes and the first action.
- **Drift response:** your thresholds, calibrated on your data, and the retrain, investigate or ignore decision rules.
- **Contacts and secrets:** where credentials are stored (never the credentials themselves).

A rollback section can be this short:

```text
Rollback (target: under 10 minutes)
1. Find the previous tags in the MLflow registry (alias: previous) and in GHCR.
2. Move the alias: python rollback.py   # sets champion -> previous
3. Redeploy the previous image, for example:
   docker run -d -p 8000:8000 -e MODEL_VERSION=<previous> \
     ghcr.io/<owner>/<repo>:model-v<previous>
4. Check /health and send one known test request.
5. Record the time, reason and versions in the incident log.
```

`rollback.py` works like `promote.py` from L14 in reverse: it reads the `previous` alias and moves `champion` to that version.

**3. A 4-minute demo.** Show the system working, not slides about it. A clear order: the problem and dataset (20 seconds), a merge that publishes an image (40 seconds), a prediction and a rejected bad input (40 seconds), the dashboard and a drift report (60 seconds), a rollback to the previous model version (60 seconds), and one lesson learned (20 seconds).

**Analogy:** The runbook is like the emergency card in an aircraft seat pocket. It is short, it uses plain steps, and someone under stress who has never read it before can follow it.

## Worked Example
Kofi Mensah is an ML engineer at a hypothetical solar-energy distributor in Kumasi, Ghana. His capstone predicts which customer solar kits will need a service visit. He records his demo:

1. Show the README and the dataset licence note, then the architecture: training, MLflow, CI, GHCR and the running container.
2. Merge a small change and show the `publish` run creating an image tagged `model-v3`. [VERSION]
3. In `/docs`, send one valid request and one request with an out-of-range value that returns 422.
4. Open the dashboard notebook: requests per hour, error rate, p95 latency and the prediction histogram.
5. Run the drift script on a batch where he increased one feature on purpose. PSI for that feature is far above his calibrated normal value, and he reads out his decision: "Investigate before retraining."
6. Roll back: run `rollback.py`, start the `model-v2` image with `-e MODEL_VERSION=2`, call `/health`, and show that new lines in the prediction log record model version 2.
7. End with one lesson learned: his first rollback attempt failed because an old image had been deleted, so he added a rule to keep the last three images.

Kofi checks that no secret, token or personal data is visible in his terminal, browser tabs or notebook before recording.

## Common Mistake
Many learners write a runbook that describes the architecture in detail but gives no exact commands. Under pressure, "roll back to the previous version" is not enough: which version, which command, which permission? Write the real commands and test every one of them yourself, from a clean terminal, before you record the demo.

## Key Takeaways
1. Part 2 adds monitoring (dashboard and drift check), a one-page runbook and a 4-minute demo.
2. A good runbook gives exact deploy and rollback commands, the meaning and first action for each alert, and drift decision rules.
3. Demonstrate the real system, including a rollback, and never show secrets or personal data on screen.

## Hands-on Exercise
**Task:** Capstone step 2: add monitoring and a drift check to your service, write a one-page runbook, and record a 4-minute demo that includes a rollback to the previous model version.
**Tools:** Your capstone repository, pandas, SciPy, Jupyter, MLflow, Docker, and any free screen recorder (for example, OBS Studio) [VERSION].
**Steps:**
1. Add the request-logging middleware and generate at least 200 requests with synthetic inputs.
2. Build the dashboard notebook with the four required views.
3. Write the drift script, run it on a normal batch and a drifted batch, and save both reports.
4. Make sure the registry has at least two versions and a `previous` alias, and GHCR has two images.
5. Write the one-page runbook with the six headings above.
6. Rehearse the rollback from a clean terminal and time it.
7. Record the 4-minute demo in the suggested order.
8. Submit the repository link, runbook, dashboard, drift reports and video.
**What good looks like:** A dashboard that matches the logs, a drift report where the changed feature stands out with a clear decision, a runbook that a colleague could follow without asking you, and a demo under 4 minutes that includes a successful rollback.
**Time:** about 120 minutes

## Review Flags
- [VERSION] GitHub Actions and GHCR interfaces shown in the demo, and the named free screen recorder, should be checked before recording.
- The rollback commands follow the alias-based scripts tested locally with MLflow 3.16.1. The worked example is hypothetical.
