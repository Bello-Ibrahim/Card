# L15 Monitoring Model Services

Course: AI-18 · Module: M4 · Objectives: O5 · Video: 5 min (screen demo)

## Hook
Your service has returned status 200 for every request this week. Is the model working? Not necessarily. A service can be perfectly healthy while its predictions are slowly becoming wrong. You need to watch two layers, not one.

## Explanation
**Layer 1: service health.** These signals tell you whether the API works:

- **Traffic:** requests per hour. A sudden drop may mean a client is broken; a sudden rise may mean a retry loop.
- **Error rate:** the share of responses with status 400 or above. Separate client errors (such as 422) from server errors (500).
- **Latency:** median and p95 per hour, as in L09.

**Layer 2: model behaviour.** These signals tell you whether the predictions still make sense:

- **Prediction distribution:** for example, the share of wines predicted "good". A large change without a known reason is a warning.
- **Input values:** the distribution of each feature compared with training. You will test this formally in L16.
- **Accuracy when labels arrive:** true outcomes often arrive later (tasters score the wine weeks after the prediction). Join them to the prediction log by `request_id` and compute the real metric.

The L07 log records predictions only. To measure traffic, errors and latency for every request, including rejected ones, add a small middleware to `app.py`:

```python
@app.middleware("http")
async def log_requests(request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    log.info(json.dumps({"event": "request", "ts": time.time(), "path": request.url.path,
                         "status": response.status_code,
                         "latency_ms": round((time.perf_counter() - start) * 1000, 2)}))
    return response
```

A simple dashboard is a script or notebook that reads the log with pandas. In this course we do not set up a full monitoring stack; structured logs and a short script are enough to learn the ideas.

```python
import pandas as pd

logs = pd.read_json("predictions.jsonl", lines=True)
logs["time"] = pd.to_datetime(logs["ts"], unit="s")
req = logs[logs.event == "request"].set_index("time")
pred = logs[logs.event == "prediction"]

hourly = req.resample("1h").agg(
    requests=("status", "size"),
    error_rate=("status", lambda s: (s >= 400).mean()),
    p95_ms=("latency_ms", lambda s: s.quantile(0.95)))
print(hourly.round(3))
print(pd.cut(pred.probability, [0, .25, .5, .75, 1]).value_counts().sort_index())
```

**Alert thresholds** turn charts into action. Each alert needs a metric, a threshold, a time window and an owner, for example "server error rate above 1% for 15 minutes: page the on-call engineer". Start from your normal values and your service targets. These numbers are examples, not standards.

**Analogy:** Monitoring a model service is like monitoring a patient. The heart rate and temperature (service health) can be normal while a slow illness develops that only a blood test (model behaviour) shows. A good doctor checks both.

## Worked Example
Amara Diallo is an ML engineer at a hypothetical telecom company in Dakar, Senegal. She builds the wine dashboard on screen:

1. Add the middleware above to `app.py` and restart the service.
2. Send test traffic: a short script sends 300 requests with random valid inputs, and every 25th request has `alcohol = 40`.
3. Open a Jupyter notebook in the project folder and run the dashboard code.
4. Show the hourly table. The real output was 300 requests, an error rate of 0.04 (12 rejected requests, all 422) and a p95 latency of 3.9 ms.
5. Show the prediction distribution: 94, 64, 59 and 71 predictions in the four probability bands, 288 in total.
6. Add a bar chart with `hourly["requests"].plot(kind="bar")` and a histogram of `pred.probability`.
7. Write two alert rules under the charts, with a threshold and an owner for each.

The 4% error rate here is caused on purpose by bad client inputs. In production, Amara would investigate which client sends them.

## Common Mistake
Many teams monitor only service health, because platforms show it by default. The model can then give wrong answers for weeks with perfect uptime, as in L01. Always add at least one model-behaviour signal, such as the prediction distribution, from the first day. A second mistake is setting too many sensitive alerts: people then ignore them. Start with a few alerts that each lead to a clear action.

## Key Takeaways
1. Monitor two layers: service health (traffic, error rate, latency) and model behaviour (predictions, inputs and accuracy when labels arrive).
2. Structured JSON logs are enough to build a useful dashboard with a short pandas script.
3. Every alert needs a metric, a threshold, a time window and an owner, based on your own normal values.

## Hands-on Exercise
**Task:** Build a simple monitoring notebook or dashboard from your prediction logs that shows requests per hour, error rate, latency and the distribution of predictions.
**Tools:** pandas and Jupyter (free), matplotlib or the pandas plotting functions, your `wine-api` service.
**Steps:**
1. Add the request-logging middleware to your service.
2. Send at least 200 requests, including some invalid ones. Use synthetic inputs, not real personal data.
3. Load the log in a notebook and build the hourly table.
4. Plot requests per hour and a histogram of predicted probabilities.
5. Report the error rate and p95 latency.
6. Write two alert rules with a metric, threshold, time window and owner.
**What good looks like:** A notebook that runs from top to bottom, with a table and two charts that match the log. Error rate counts only responses with status 400 or above. The alert rules are specific and actionable.
**Time:** about 40 minutes

## Review Flags
- [VERSION] FastAPI middleware syntax and pandas `resample` and named aggregation were tested with FastAPI 0.141.1 and pandas 3.0.6.
- Judgement call carried from the curriculum: monitoring uses structured logs and a simple dashboard rather than a full Prometheus/Grafana stack.
- Dashboard numbers are real outputs from a local test with synthetic traffic; alert thresholds are examples, not standards.
