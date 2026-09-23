# L06 Designing a Prediction API with FastAPI

Course: AI-18 · Module: M2 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
Your model lives in the registry. The mobile team, the web team and a partner company all want predictions, and none of them uses Python. How do you give all of them the same model, safely, through one door?

## Explanation
The usual answer is a small web service, an **API**, that receives JSON and returns a prediction. FastAPI is a free Python framework that suits this well: it uses Python type hints to validate input and to generate interactive documentation automatically.

A good prediction API has four parts:

1. **A `/predict` endpoint** that accepts one input and returns one prediction.
2. **A `/health` endpoint** that returns quickly and says whether the service and the model are ready. Container platforms and load balancers call it.
3. **Request and response schemas**, written as Pydantic models. They define the exact fields and types, reject bad input, and appear in the documentation.
4. **Loading the model once at start-up**, not on every request. Loading a model can take seconds; doing it per request makes the service slow.

This course uses **Pydantic v2** syntax. Pydantic v1 used `class Config:` and `.dict()`; v2 uses `model_config` and `.model_dump()`. [VERSION] FastAPI's recommended start-up hook is the `lifespan` function; the older `@app.on_event("startup")` is deprecated. [VERSION]

```python
import os
from contextlib import asynccontextmanager
import mlflow, pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

MODEL_URI = os.getenv("MODEL_URI", "models:/wine-quality-clf@champion")
state = {}

class WineIn(BaseModel):
    alcohol: float
    volatile_acidity: float
    sulphates: float
    citric_acid: float

class PredictionOut(BaseModel):
    good_wine: bool
    probability: float

@asynccontextmanager
async def lifespan(app: FastAPI):
    state["model"] = mlflow.sklearn.load_model(MODEL_URI)   # once, at start-up
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": "model" in state}

@app.post("/predict", response_model=PredictionOut)
def predict(wine: WineIn):
    row = pd.DataFrame([wine.model_dump()])
    p = float(state["model"].predict_proba(row)[0, 1])
    return PredictionOut(good_wine=p >= 0.5, probability=round(p, 4))
```

`MODEL_URI` comes from an environment variable. The same code can load the registry alias on your laptop and a local model folder inside a container (L08). If you use a remote tracking server, MLflow reads its address from the `MLFLOW_TRACKING_URI` environment variable, so no address or password appears in the code.

**Analogy:** An API is like the service window of a restaurant kitchen. Customers do not enter the kitchen. They order from a fixed menu (the schema), the kitchen was prepared before opening (the model loaded at start-up), and a sign on the window says whether it is open (the health check).

## Worked Example
Mei Nakamura is a data scientist at a hypothetical agricultural technology start-up in Sapporo, Japan. She wraps the wine model in an API on screen:

1. Install packages: `pip install fastapi uvicorn` and add them to `requirements.txt`. [VERSION]
2. Save the code above as `app.py`.
3. Point MLflow at the local store: `export MLFLOW_TRACKING_URI=sqlite:///mlflow.db` (Windows PowerShell: `$env:MLFLOW_TRACKING_URI="sqlite:///mlflow.db"`).
4. Start the service: `uvicorn app:app --reload`. [VERSION]
5. Open `http://127.0.0.1:8000/health` in a browser. It shows `{"status":"ok","model_loaded":true}`.
6. Open `http://127.0.0.1:8000/docs`. Show the automatic documentation with both endpoints and the `WineIn` schema. [VERSION]
7. Expand **POST /predict**, click **Try it out**, and send `{"alcohol": 12.5, "volatile_acidity": 0.3, "sulphates": 0.8, "citric_acid": 0.4}`. [VERSION]
8. Show the response. With our champion model (trained on the synthetic fallback data), the real response was `{"good_wine": true, "probability": 0.9318}`.

## Common Mistake
Many learners load the model inside the `/predict` function. It works in a quick test, so the problem is hidden. Under real traffic, every request reads the model from disk or from the registry, latency rises sharply, and the registry receives many unnecessary calls. Load once in `lifespan`, keep the model in memory, and let `/health` report whether loading succeeded.

## Key Takeaways
1. A prediction API needs a `/predict` endpoint, a `/health` endpoint and clear request and response schemas.
2. FastAPI uses Pydantic models to validate input and to generate interactive documentation at `/docs`.
3. Load the model once at start-up, and pass its location and any server address through environment variables, not code.

## Hands-on Exercise
**Task:** Build a FastAPI service that loads your registered model and returns predictions for a JSON input, then test it through the automatic documentation page.
**Tools:** FastAPI and Uvicorn (free), MLflow, your `wine-api` project.
**Steps:**
1. Create `app.py` with the request and response schemas for your model's features.
2. Load the `champion` alias in a `lifespan` function.
3. Add `/health` and `/predict`.
4. Start the service with Uvicorn and check `/health` in a browser.
5. Use `/docs` to send three different inputs and note each response.
6. Send one input with a missing field and note the status code. You will improve error handling in L07.
**What good looks like:** `/health` returns `model_loaded: true`. Three valid inputs return a probability between 0 and 1. The missing field returns status 422, not a server error (500). No credentials appear in `app.py`.
**Time:** about 35 minutes

## Review Flags
- [VERSION] FastAPI and Pydantic syntax: code uses Pydantic v2 (`model_dump`, `model_config`) and the FastAPI `lifespan` hook. Tested with FastAPI 0.141.1 and Pydantic 2.13.5; check current releases and the look of the `/docs` page.
- [VERSION] Uvicorn command and MLflow model loading were tested with Uvicorn installed and MLflow 3.16.1.
- The prediction value is a real output from the model trained on synthetic fallback data.
