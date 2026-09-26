# Screen Demo Pack: AI-18 L08 Containerising the Model Service

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L08_screen_1.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Run: python export_model.py and show the output 'exported wine-quality-clf v1'
2. Show the new model/ folder and model_version.txt
3. Create .dockerignore with .venv, mlflow.db, mlruns, data, *.jsonl, .git and .env

**Narration over this clip (for pacing)**

> Let's watch Lars Eriksson, a platform engineer at a hypothetical energy company in Gothenburg, Sweden. First, he exports the champion model from the registry to a local model folder. Then he creates a docker ignore file that keeps out the virtual environment, the database, the data, the logs, the Git folder and any environment file.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L08_screen_2.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open the Dockerfile in the editor
2. Highlight Stage 1: FROM python:3.11-slim AS build and the pip wheel line
3. Highlight Stage 2: COPY --from=build, useradd appuser and chown
4. Highlight COPY app.py, COPY model/, ENV MODEL_URI=/app/model and USER appuser

**Narration over this clip (for pacing)**

> Now the Dockerfile, in two stages. The build stage turns the requirements into ready packages. The runtime stage installs them, creates a normal user, copies only the app and the model folder, and switches to that user before starting the server.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L08_screen_3.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Run: docker build -t wine-api:v1 .
2. Run: docker run --rm -p 8000:8000 -e MODEL_VERSION=1 wine-api:v1
3. Open http://127.0.0.1:8000/health and show model_loaded true

**Narration over this clip (for pacing)**

> He builds the image with a version tag, and runs it. In the browser, the health page answers from inside the container.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L08_screen_4.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Run: docker images wine-api and show the SIZE column
2. Show the size of a single-stage build on the full python:3.11 image and place the two side by side
3. Run: docker run --rm wine-api:v1 whoami and show the output appuser

**Narration over this clip (for pacing)**

> Next, he lists the image size, and compares it with a single-stage build on the full Python image. The slim, multi-stage image is clearly smaller. Record your own sizes, because they depend on your requirements and platform. Last, he checks the user. The container prints app user, not root.

## Production notes for this lesson

- [VERSION] Docker base image names and tags (python:3.11-slim, python:3.11) and multi-stage build features: check current tags and supported Python versions before recording. The Dockerfile was not built in the Stage 2 review environment, so build and record it before the shoot.
- No image sizes are given in content.md. The voiceover does not state sizes; the screen shows whatever the recording machine reports. Do not add numbers to the voiceover unless they come from the actual recording.
- [VERSION] Docker Desktop licence terms for organisations change; the voiceover does not discuss licensing.
- Screen recording: never show a real .env file or any secret value. If --env-file is shown, use an empty demo file with a placeholder name only.
- Lars Eriksson and the Gothenburg energy company are hypothetical. Docker basics are a prerequisite, so the lesson recaps them in one sentence (curriculum judgement call).
