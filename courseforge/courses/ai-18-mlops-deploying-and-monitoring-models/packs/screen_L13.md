# Screen Demo Pack: AI-18 L13 Building and Publishing Images Automatically

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L13_screen_1.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Open Settings, then Secrets and variables, then Actions
2. Click New repository secret
3. Enter the name MLFLOW_TRACKING_URI (value typed off screen or blurred)
4. Save and show the secret listed by name only

**Narration over this clip (for pacing)**

> First, the secret. In the repository settings, under secrets and variables, he adds a secret for the tracking server address. We only show its name. GitHub stores the value encrypted.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L13_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Create .github/workflows/publish.yml with the workflow from content.md
2. Highlight the permissions block (contents: read, packages: write)
3. Highlight the two tags lines
4. Open a pull request and wait for the ci check

**Narration over this clip (for pacing)**

> He adds the publish workflow. It runs only on pushes to main, asks for permission to write packages, exports the model, logs in, and builds and pushes the image with the commit tag and the model tag. He commits it through a pull request, so CI runs first.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L13_screen_3.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Merge the pull request
2. Open the Actions tab and the publish run
3. Show the export, login, build and push steps completing
4. Open the repository's Packages section and show the two tags

**Narration over this clip (for pacing)**

> He merges the pull request. In the Actions tab, the publish run shows each step: export, login, build and push. In the Packages section, the new image has two tags, the commit ID and model v one.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L13_screen_4.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run: docker pull ghcr.io/<owner>/wine-api:model-v1
2. Run the container on port 8000
3. Call /health and show the response

**Narration over this clip (for pacing)**

> On his laptop, he pulls the image by its model tag, runs it, and calls the health endpoint. It answers. The image in the registry is the same one that passed the tests.

## Clip 5: scene 12

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L13_screen_5.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Open the publish job log
2. Scroll to the export step
3. Highlight the masked value shown as ***

**Narration over this clip (for pacing)**

> Finally, he opens the job log. Where the tracking server address would appear, GitHub shows three stars. The secret value never reaches the log.

## Production notes for this lesson

- [VERSION] GitHub Container Registry permissions (packages: write, GITHUB_TOKEN access), package visibility defaults and the Secrets and Packages interface depend on plan and repository settings. Check them before recording.
- [VERSION] Action versions (docker/login-action@v3, docker/build-push-action@v6) should be checked for newer releases. The YAML was checked for valid syntax with PyYAML but was not run on GitHub in the content review, so the publish run, the Packages page and the masked log must be recorded from a real run.
- No secrets on screen: when adding the MLFLOW_TRACKING_URI secret, type the value off camera or blur the value field. Show only the secret name. In the job log, show the masked '***' value. Blur account names and the real tracking server address if they appear.
- The export_model.py step was run locally against a SQLite tracking store and produced model/ and model_version.txt. The workflow file is shown on screen and never read aloud. The commit ID tag on screen will differ from the thumbnail example.
- Learners without a shared tracking server may use the course-only fallback (train.py and export_ci_model.py with a hand-written model_version.txt); the voiceover mentions it briefly and the lesson page has the details.
- Diego Hernández and the Guadalajara payments start-up are hypothetical.
