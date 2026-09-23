# L11 Testing ML Code and Models

Course: AI-18 · Module: M3 · Objectives: O4, O6 · Video: 5 min (screen demo)

## Hook
All your tests pass. You deploy the new model. A week later, the business reports that predictions are worse than before. How can every test be green when the model got worse? Because code tests check the code, not the model.

## Explanation
An ML service needs four kinds of test. Each one catches problems the others miss.

1. **Unit tests** check small pieces of code, such as "`load_data()` returns the expected columns". They are fast and run on every change.
2. **Data tests** check the inputs: no missing values, values in the expected range, the expected share of each label. They catch broken data before training.
3. **Model quality gates** train or load the model and check a metric on a **fixed** test set against a minimum, for example "F1 must be at least 0.50". This is the test that catches a worse model.
4. **API tests** send HTTP requests to the service and check status codes and response shapes. FastAPI's `TestClient` does this without starting a real server.

Use pytest for all four. Put tests in `tests/`, name files `test_*.py` and functions `test_*`, and run `pytest -q`. Add a `pytest.ini` file in the project root with the two lines `[pytest]` and `pythonpath = .`, so tests can import `data.py` and `app.py`.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from data import FEATURES, load_data

def test_load_data_columns():                 # unit
    X, _ = load_data()
    assert list(X.columns) == FEATURES

def test_no_missing_or_out_of_range():        # data
    X, _ = load_data()
    assert not X.isna().any().any()
    assert X["alcohol"].between(8, 15).all()

def test_quality_gate():                      # model
    X, y = load_data()
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(X_tr, y_tr)
    assert f1_score(y_te, model.predict(X_te)) >= 0.50
```

```python
from fastapi.testclient import TestClient
from app import app

GOOD = {"alcohol": 12.5, "volatile_acidity": 0.3, "sulphates": 0.8, "citric_acid": 0.4}

def test_rejects_out_of_range():              # API
    with TestClient(app) as client:           # "with" runs the lifespan start-up
        r = client.post("/predict", json={**GOOD, "alcohol": 40})
        assert r.status_code == 422
```

Set the quality gate from evidence: the current champion's score on the same fixed test set, minus a small margin you agree with the business. A gate that is too low catches nothing; one that is too high blocks every change.

**Analogy:** Testing an ML service is like inspecting a car. Unit tests check each part, data tests check the fuel, the quality gate is the road test, and API tests check that the doors and controls work for the driver. A car can pass every parts check and still fail the road test.

## Worked Example
Fatima Al-Sayed is an ML engineer at a hypothetical e-commerce company in Alexandria, Egypt. She shows the tests on screen:

1. Create `tests/test_model.py` and `tests/test_api.py` with the code above, plus a second unit test that labels are only 0 or 1, and an API test for a valid request.
2. Set the model location: `export MODEL_URI=model` (the folder exported in L08).
3. Run `pytest -q`. The real output was `6 passed`, with one deprecation warning from the test client. [VERSION]
4. Break the model on purpose: change the gate to `>= 0.90`.
5. Run `pytest -q` again. The real output shows `FAILED ... test_quality_gate` and `AssertionError: assert 0.5568181818181818 >= 0.9`.
6. Change the gate back and run again: all tests pass.

Step 5 is important. A test that has never failed has not proved that it can catch anything.

## Common Mistake
Many learners compute the quality gate on a new random split each time, or on data that also changes. The score then moves for reasons unrelated to the model, and the gate fails or passes by chance. Use a fixed test set with a fixed seed, and store its data hash, so every model is judged on the same examples. Keep the test data free of personal information, or use synthetic data.

## Key Takeaways
1. ML services need unit tests, data tests, model quality gates and API tests.
2. Only the quality gate, on a fixed test set, can catch a model that is worse but whose code still works.
3. Make each test fail on purpose once to prove that it can catch the problem.

## Hands-on Exercise
**Task:** Write at least 5 pytest tests: 2 unit tests, 1 data test, 1 model quality gate and 1 API test. Make one fail on purpose to check that it catches the problem.
**Tools:** pytest, FastAPI `TestClient` (with its HTTP client dependency), scikit-learn (all free) [VERSION], your `wine-api` project.
**Steps:**
1. Create a `tests/` folder and the `pytest.ini` file.
2. Write 2 unit tests for your data or helper functions.
3. Write 1 data test for missing values and value ranges.
4. Write 1 quality gate on a fixed test set. Base the threshold on your champion's score.
5. Write 1 API test with `TestClient`, inside a `with` block.
6. Run `pytest -q` and confirm that all tests pass.
7. Break one thing on purpose (the threshold, a column name or a validation rule), run again and screenshot the failure. Then fix it.
**What good looks like:** At least 5 passing tests covering all four types. A screenshot of one deliberate failure with a clear message. A one-line note explaining how you chose the quality threshold.
**Time:** about 40 minutes

## Review Flags
- [VERSION] FastAPI `TestClient` depends on an HTTP client library; with Starlette 1.7.0 it printed a deprecation warning about the `httpx` package. Check the current recommended dependency. Tested with pytest 9.1.1.
- Test results are real outputs from the synthetic fallback data.
