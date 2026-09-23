# Capstone Rubric: Deploy and Monitor a Model API

## Task
Deploy a model as a FastAPI service in Docker, with automated tests and image builds in GitHub Actions, model versioning in MLflow, and monitoring with drift detection and a rollback plan. You build and automate the service in L17 (capstone step 1), and add monitoring, a runbook and a demo in L18 (capstone step 2). Use a public tabular dataset with a licence that allows your use and no personal data, or a synthetic dataset with a fixed seed. Never commit secrets, credentials or personal data.

## Deliverables
- A GitHub repository with reproducible training (`train.py`, `config.yaml`, pinned `requirements.txt`, fixed seeds), a FastAPI service, a Dockerfile, tests and GitHub Actions workflows, plus a README with the dataset source and licence and an evidence list.
- MLflow evidence: at least 3 tracked runs and a registered model with at least 2 versions, `champion` and `previous` aliases, and data hash and Git commit tags on each version.
- CI/CD evidence: a pull request blocked by a failing test, and an image in GitHub Container Registry tagged with the commit ID and model version.
- A monitoring notebook or dashboard (requests per hour, error rate, p95 latency, prediction distribution) and two drift reports (normal batch and drifted batch) with a written decision.
- A one-page runbook with deploy, rollback, alert and drift-response sections.
- A demo video of at most 4 minutes that includes a rollback to the previous model version.

## Criteria
| Criterion | Objective | Excellent | Good | Developing | Not yet | Points |
|---|---|---|---|---|---|---|
| Reproducible training and model versioning | O3 | Training runs with one command and gives identical metrics twice; 3+ tracked runs with a justified choice; 2+ registered versions with aliases and data hash and commit tags. | Reproducible training, tracked runs and a registered model with aliases; minor gaps in tags or justification. | Runs are tracked, but training is not reproducible or versions lack aliases or tags. | No tracking or registry evidence. | 20 |
| Containerised API with tests and CI/CD | O4, O7 | FastAPI service with `/health`, `/predict`, Pydantic v2 validation and structured logs; slim multi-stage non-root image; all four test types; protected `main`; images published with commit and model tags; no secrets anywhere. | Working service, image, tests and CI/CD with small gaps, such as one missing test type or tag. | Service runs locally, but CI, image publishing or validation is incomplete. | No working API or no automation. | 25 |
| Monitoring and drift detection | O5 | Dashboard shows all four views and matches the logs; drift check uses PSI and KS on inputs and predictions, with a calibrated baseline; drifted feature is clearly identified. | Dashboard and drift check work, with one view or the calibration missing. | Partial dashboard or drift check without clear interpretation. | No monitoring or drift evidence. | 20 |
| Release, rollback and retraining decisions | O6 | Drift decision (retrain, investigate or ignore) is justified with evidence; rollback is demonstrated and timed; alert rules and release choice are measurable and justified. | Sound decisions and a working rollback, with limited justification. | Decisions stated without evidence, or rollback not demonstrated. | No decisions or rollback plan. | 20 |
| Runbook and demo | O7 | One-page runbook with exact, tested commands a colleague could follow; clear demo of at most 4 minutes covering publish, prediction, monitoring, drift and rollback; no secrets or personal data on screen. | Clear runbook and demo with small gaps in commands or coverage. | Runbook is vague or demo is incomplete or too long. | Runbook or demo missing. | 15 |

Total: 100

## Submission Checklist
- My README names the dataset, its source and its licence, and contains an evidence list.
- Running `python train.py` twice gives identical metrics.
- MLflow shows at least 3 runs and a registered model with 2+ versions, `champion` and `previous` aliases, and data hash and commit tags.
- My service has `/health` and `/predict`, validates inputs and writes structured logs without personal data.
- My Dockerfile uses a slim base image, a multi-stage build and a non-root user.
- I have unit, data, quality gate and API tests, and a screenshot of a blocked pull request.
- Every merge to `main` publishes an image tagged with the commit ID and model version.
- My dashboard shows requests per hour, error rate, p95 latency and the prediction distribution.
- I have drift reports for a normal and a drifted batch, with a written decision.
- My runbook fits on one page and I have tested every command in it.
- My demo is at most 4 minutes and includes a rollback.
- No secrets, credentials or personal data appear in my repository, images, logs or video.
