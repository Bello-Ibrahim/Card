# Screen Demo Pack: AI-18 L06 Designing a Prediction API with FastAPI

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L06_screen_1.mp4`
- **Target length:** about 20 seconds

**Steps**

1. In the wine-api terminal, run: pip install fastapi uvicorn
2. Add fastapi and uvicorn with their versions to requirements.txt
3. Open app.py in the editor and scroll through: the WineIn and PredictionOut schemas, the lifespan function, /health and /predict

**Narration over this clip (for pacing)**

> Let's watch Mei Nakamura, a data scientist at a hypothetical agricultural technology start-up in Sapporo, Japan. She installs FastAPI and Uvicorn, the server that runs it, and adds both to the requirements file. Then she opens her app file, which contains the code you just saw.

## Clip 2: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L06_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Run: export MLFLOW_TRACKING_URI=sqlite:///mlflow.db (show the Windows PowerShell version as a caption)
2. Run: uvicorn app:app --reload and wait for the startup message
3. Open http://127.0.0.1:8000/health in the browser
4. Show the response {"status":"ok","model_loaded":true}

**Narration over this clip (for pacing)**

> She points MLflow at the local database through an environment variable, and starts the service. In the browser, the health page reports status ok, and model loaded, true. If the model had failed to load, this page would say so at once, before any client sent a real request.

## Clip 3: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L06_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open http://127.0.0.1:8000/docs
2. Show both endpoints and scroll to the WineIn schema
3. Expand POST /predict and click Try it out
4. Paste the body {"alcohol": 12.5, "volatile_acidity": 0.3, "sulphates": 0.8, "citric_acid": 0.4}
5. Click Execute

**Narration over this clip (for pacing)**

> Now the best part. She opens the docs page. FastAPI has built it automatically, with both endpoints and the input schema. She expands the predict endpoint, clicks Try it out, and sends one wine, with an alcohol value of twelve point five.

## Clip 4: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L06_screen_4.mp4`
- **Target length:** about 28 seconds

**Steps**

1. Scroll to the response body
2. Highlight {"good_wine": true, "probability": 0.9318}
3. Point to the 200 status code

**Narration over this clip (for pacing)**

> The response comes back. Good wine, true, with a probability of zero point nine three one eight. That is the real answer from our champion model, trained on the synthetic data. Every client, in any language, can now call the same model in the same way. The mobile team, the web team and the partner company all use one door, and one set of rules.

## Production notes for this lesson

- [VERSION] Code uses Pydantic v2 (model_dump, model_config) and the FastAPI lifespan hook; the older startup event is deprecated. Tested with FastAPI 0.141.1 and Pydantic 2.13.5; check current releases and the look of the /docs page before recording.
- [VERSION] The uvicorn command and MLflow model loading were tested with MLflow 3.16.1.
- The response {"good_wine": true, "probability": 0.9318} is a real output from the champion model trained on the synthetic fallback data; it must match on screen.
- Screen recording: the MLFLOW_TRACKING_URI shown is a local SQLite file only. Never show a remote tracking server address, password or token in the terminal or editor.
- Mei Nakamura and the Sapporo start-up are hypothetical.
