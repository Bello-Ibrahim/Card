# L07 Input Validation, Errors and Logging

Course: AI-18 · Module: M2 · Objectives: O4, O5 · Video: 5 min (screen demo)

## Hook
A client sends an alcohol value of 40 instead of 12.5. Your model does not complain. It returns a confident prediction for a wine that cannot exist. Nobody sees an error, and nobody can find the request later. This lesson closes both gaps.

## Explanation
A model will produce a number for almost any input. It cannot tell you that the input makes no sense. The API must do that job before the model sees the data. Reject three kinds of bad input early:

1. **Missing fields:** a required feature is absent.
2. **Wrong types:** a string such as `"high"` where a number is expected.
3. **Values outside the training range:** numbers the model never saw during training, where its behaviour is unknown.

With Pydantic v2, you add these rules to the schema. `Field(ge=..., le=...)` sets lower and upper limits, and `extra="forbid"` rejects unexpected fields, which also stops clients from sending personal data such as names or emails by mistake. [VERSION] FastAPI then returns status **422** with a clear, machine-readable message, and the model is never called.

```python
from pydantic import BaseModel, ConfigDict, Field

class WineIn(BaseModel):
    model_config = ConfigDict(extra="forbid")
    alcohol: float = Field(ge=8, le=15)
    volatile_acidity: float = Field(ge=0.1, le=1.6)
    sulphates: float = Field(ge=0.3, le=2.0)
    citric_acid: float = Field(ge=0, le=1)
```

Take the limits from your training data, for example the minimum and maximum of each feature, and write down where they came from.

The second job is **structured logging**. Write one JSON line per prediction, with the same fields every time. Later, in L15 and L16, you will read these lines to build a dashboard and to detect drift. Log what you need for monitoring: a request ID, a timestamp, the model version, the input features, the prediction and the latency. Do **not** log personal data, such as names, emails, addresses or free-text notes. If a feature is personal, log a coarse bucket or leave it out.

```python
import json, logging, time, uuid
log = logging.getLogger("predictions")
log.addHandler(logging.FileHandler("predictions.jsonl"))
log.setLevel(logging.INFO)

@app.post("/predict", response_model=PredictionOut)
def predict(wine: WineIn):
    start = time.perf_counter()
    p = float(state["model"].predict_proba(pd.DataFrame([wine.model_dump()]))[0, 1])
    log.info(json.dumps({
        "event": "prediction", "request_id": str(uuid.uuid4()), "ts": time.time(),
        "model_version": MODEL_VERSION, "features": wine.model_dump(),
        "probability": round(p, 4),
        "latency_ms": round((time.perf_counter() - start) * 1000, 2)}))
    return PredictionOut(good_wine=p >= 0.5, probability=round(p, 4))
```

`MODEL_VERSION` is read from an environment variable, like `MODEL_URI` in L06.

**Analogy:** Validation is the security check at an airport entrance, and logging is the boarding record. The check stops items that should not go on the plane. The record tells you later exactly who boarded which flight, without storing their private conversations.

## Worked Example
Chidi Okafor maintains a hypothetical price-prediction API for a farm marketplace in Lagos, Nigeria. He demonstrates the wine version on screen:

1. Replace the `WineIn` class in `app.py` with the validated version above, and add the logging code.
2. Restart Uvicorn and open `/docs`.
3. Send a request with `"alcohol": 40`. The response is status 422 with the message "Input should be less than or equal to 15".
4. Remove `sulphates` and send again. The response is 422 with "Field required".
5. Set `"citric_acid": "high"`. The response is 422 with "Input should be a valid number, unable to parse string as a number".
6. Add `"email": "a@b.c"`. The response is 422 with "Extra inputs are not permitted".
7. Send a valid request, then open `predictions.jsonl` and show the new line.

These messages are the real Pydantic 2.13 responses. A logged line looked like this (shortened, with `MODEL_VERSION` set to 1):

```json
{"event": "prediction", "model_version": "1", "features": {"alcohol": 12.5, "volatile_acidity": 0.3, "sulphates": 0.8, "citric_acid": 0.4}, "probability": 0.9318, "latency_ms": 18.83}
```

## Common Mistake
Many learners write logs as free text, such as `print(f"Predicted {p} for {wine}")`. A person can read these lines, but a program cannot analyse them reliably, and the format changes whenever someone edits the message. Use one JSON object per line with fixed field names. A second common mistake is logging the whole raw request body "just in case". This often captures personal data. Log a fixed list of fields that you chose on purpose.

## Key Takeaways
1. Validate inputs in the schema: missing fields, wrong types and values outside the training range return a clear 422 before the model runs.
2. Write one structured JSON log line per prediction, with a request ID, timestamp, model version, inputs, prediction and latency.
3. Never log personal data; choose the logged fields on purpose and forbid unexpected ones.

## Hands-on Exercise
**Task:** Add validation rules for 3 kinds of bad input, return clear error responses, and write each prediction to a structured log file. Send 10 test requests and inspect the log.
**Tools:** FastAPI, Pydantic v2, Python's `logging` module (all free); a terminal or the `/docs` page.
**Steps:**
1. Compute the minimum and maximum of each feature in your training data.
2. Add `Field` limits and `extra="forbid"` to your request schema.
3. Add structured logging to `/predict`.
4. Send 10 requests: 6 valid, and 1 each for missing field, wrong type, out-of-range value and unexpected field.
5. Record the status code and message for each request.
6. Open `predictions.jsonl`. Count the lines and check that each one parses as JSON.
**What good looks like:** 4 requests return 422 with clear messages; 6 return 200. The log has exactly 6 prediction lines with the same fields. No personal data appears in the log.
**Time:** about 35 minutes

## Review Flags
- [VERSION] Pydantic v2 syntax (`Field(ge, le)`, `ConfigDict(extra="forbid")`) and the exact 422 message texts were tested with Pydantic 2.13.5 and FastAPI 0.141.1; Pydantic v1 used different syntax and messages.
- The feature limits come from the synthetic fallback data and are approximate; learners should use their own training data.
