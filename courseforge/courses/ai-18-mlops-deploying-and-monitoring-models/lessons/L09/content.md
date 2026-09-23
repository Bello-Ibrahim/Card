# L09 Batch vs Online Serving and Performance

Course: AI-18 · Module: M2 · Objectives: O4, O6 · Video: 5 min (screen demo)

## Hook
Does your model need to answer in 50 milliseconds, or is tomorrow morning fast enough? The answer changes your architecture, your costs and what you must measure.

## Explanation
There are two main ways to serve predictions.

**Online serving** answers one request at a time, while a user or system waits. The API from L06 is online serving. It needs low **latency** (time per request) and must stay available all day.

**Batch serving** scores many rows together, on a schedule, and stores the results in a file or database table. Nobody waits for a single answer. It is simpler to run, easier to retry after a failure, and usually cheaper, but the predictions are only as fresh as the last run.

Choose online serving when the input exists only at request time and the answer is needed immediately. Choose batch serving when the inputs are known in advance and a delay of hours is acceptable.

For online services, measure two things under load:

- **Latency percentiles.** The **median** (50th percentile) is the typical request. The **95th percentile (p95)** is the time that 95% of requests stay under. Averages hide slow requests, and users notice the slow ones.
- **Throughput:** requests per second the service handles without errors.

Latency usually rises as load rises. A load test shows where it starts to rise sharply.

Locust is a free, open-source load-testing tool. You describe a user in Python: [VERSION]

```python
from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def predict(self):
        self.client.post("/predict", json={"alcohol": 11.2, "volatile_acidity": 0.45,
                                           "sulphates": 0.7, "citric_acid": 0.3})
```

A batch scoring script reuses the same registered model:

```python
import sys, mlflow, pandas as pd
from data import FEATURES

model = mlflow.sklearn.load_model("models:/wine-quality-clf@champion")
df = pd.read_csv(sys.argv[1])
df["probability"] = model.predict_proba(df[FEATURES])[:, 1].round(4)
df.to_csv(sys.argv[2], index=False)
print(f"scored {len(df)} rows -> {sys.argv[2]}")
```

Using the same model version for both paths means online and batch predictions agree.

**Analogy:** Online serving is a coffee bar that makes each drink while the customer waits. Batch serving is a bakery that bakes all the bread at night for the morning. The bakery is efficient, but it cannot make a fresh loaf at 3 p.m. for one customer.

## Worked Example
Katarzyna Nowak leads data science at a hypothetical online shop in Kraków, Poland. She owns two models:

- A **delivery-time model** that shows "arrives in 2 days" on the checkout page. The basket and address exist only at checkout, and the customer is waiting. This needs **online** serving with a p95 target agreed with the web team.
- A **monthly churn score** that tells the marketing team which customers may stop buying. The inputs are last month's orders, and marketing uses the list once a month. This needs **batch** serving: one scheduled job writes a table.

She load-tests the online service on screen:

1. Start the service: `uvicorn app:app --port 8000` (or run the container from L08).
2. Save the Locust class above as `locustfile.py`.
3. Run `locust -f locustfile.py --host http://127.0.0.1:8000` and open `http://localhost:8089`. [VERSION]
4. Start a test with 5 users and a spawn rate of 10. Let it run for 20 seconds and show the **Statistics** tab. [VERSION]
5. Stop, then repeat with 50 users. Compare the median and 95th percentile columns. [VERSION]
6. Run the batch script: `python batch_score.py new_batch.csv scored.csv`.

In our test (the service running directly on one laptop, one Uvicorn worker, synthetic model), the real results were:

| Users | Requests/s | Median | p95 |
|---|---|---|---|
| 5 | 16 | 6 ms | 11 ms |
| 50 | 145 | 9 ms | 30 ms |

The batch script printed "scored 500 rows -> scored.csv". Your numbers will differ with hardware, model and container settings.

## Common Mistake
Many learners report only the average latency from a single user. One user on a laptop hides queueing, which happens only when many requests arrive together. Always test at more than one load level, report the median and p95, and test the same way you will deploy: the container, not only the development server.

## Key Takeaways
1. Online serving answers each request immediately; batch serving scores many rows on a schedule and is simpler and cheaper when a delay is acceptable.
2. Measure median and 95th percentile latency and throughput at more than one load level.
3. Use the same registered model version for online and batch paths so their predictions agree.

## Hands-on Exercise
**Task:** Load-test your container, record median and 95th percentile latency at two load levels, and write a batch scoring script for the same model.
**Tools:** Locust (free, open source) [VERSION], Docker, MLflow, your `wine-api` project.
**Steps:**
1. Run your container from L08.
2. Write `locustfile.py` with valid inputs from your data range.
3. Run a test with a low load (for example 5 users) for at least 20 seconds and record requests per second, median and p95.
4. Repeat with a higher load (for example 50 users).
5. Write `batch_score.py` and score a CSV file of at least 100 rows.
6. Write three sentences: how latency changed with load, whether the service meets a target you choose, and one use case where batch serving would be better.
**What good looks like:** A table with two load levels and three measurements each, no failed requests, a scored CSV file with a probability column, and a justified serving choice.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Locust is not in the brief's tool list; it is used as a free load-testing tool. Its web interface (port 8089, Statistics tab) and `HttpUser` API were checked against Locust 2.46.6 only.
- Load-test and batch results are real outputs from one laptop test with a local Uvicorn process (not the container) and the synthetic fallback model.
