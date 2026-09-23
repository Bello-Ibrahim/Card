# L17 Capstone Part 1: Build and Automate

Course: AI-18 · Module: M4 · Objectives: O3, O4, O7 · Video: 5 min (screen demo)

## Hook
You have built each part of a production ML system separately. Now you connect them into one repository where a single merge to `main` produces a tested, versioned, deployable model API, without any manual copying.

## Explanation
The capstone asks you to **deploy and monitor a model API**. Part 1, this lesson, covers the build and automation. Part 2 (L18) adds monitoring, a runbook and a demo.

**Choose a dataset and a problem.** Pick a public tabular dataset with a clear prediction target, a licence that allows your use, and no personal data. You may continue with the wine example, but a new dataset shows more skill. Check and write down the licence and source of your dataset in the README. If you cannot download data, use a synthetic dataset with a fixed seed, as in L03.

**Required parts of the repository:**

1. **Reproducible training:** `train.py`, `config.yaml`, pinned `requirements.txt`, fixed seeds (L03).
2. **Tracking and registry:** at least 3 tracked runs in MLflow, and a registered model with a `champion` alias, a data hash tag and a Git commit tag (L04, L05).
3. **Service:** a FastAPI app with `/health` and `/predict`, Pydantic v2 schemas with range validation, and structured prediction logs (L06, L07).
4. **Container:** a multi-stage Dockerfile with a slim base image and a non-root user (L08).
5. **Tests:** unit, data, quality gate and API tests (L11).
6. **CI:** tests run on every push and pull request, and `main` is protected (L12).
7. **Publishing:** every merge to `main` builds and pushes an image tagged with the commit ID and model version (L13).

A suggested layout:

```text
capstone-api/
  .github/workflows/ci.yml, publish.yml
  data.py, train.py, register.py, export_model.py
  app.py, Dockerfile, .dockerignore
  config.yaml, requirements.txt, pytest.ini
  tests/test_model.py, tests/test_api.py
  README.md
```

The **rubric** gives points for reproducible training and model versioning, for the containerised API with tests and CI/CD, for monitoring and drift detection, for the release and rollback plan, and for the runbook and demo. Read it now, so you collect evidence while you build: screenshots of MLflow runs, the registry page, a blocked pull request and the published image.

**Analogy:** The capstone is like assembling a car from parts you have already tested one by one. The engine, brakes and lights each worked on the bench. Now you must fit them together, connect the wires and prove that the whole car drives.

## Worked Example
Leila Haddad is a data scientist at a hypothetical insurance company in Casablanca, Morocco. For her capstone, she predicts whether a household appliance will need repair within a year, using a public tabular dataset with no personal data. She records her progress on screen:

1. Create the repository from her L03 template and replace `data.py` with a loader for her dataset. She writes the dataset source and licence in `README.md`.
2. Run `python train.py` twice and show identical metrics.
3. Log 4 runs to MLflow, compare them, and run `register.py`. She shows the `champion` alias and the two tags in the registry.
4. Run `python export_model.py`, then `docker build -t repair-api:dev .` and `docker run -p 8000:8000 repair-api:dev`. She sends one valid and one invalid request from `/docs`.
5. Run `pytest -q` locally: all tests pass.
6. Push a branch with a deliberately broken quality gate, open a pull request and show that the merge is blocked. Fix it and merge.
7. Open **Actions** and **Packages** and show the published image with its commit and model tags. [VERSION]

She keeps a short evidence list in the README with a link or screenshot for each rubric criterion.

## Common Mistake
Many learners build all the parts first and connect them on the last day. Integration problems then appear together: the Docker image cannot find the model, CI cannot reach the tracking server, or the API test needs a model that CI never built. Connect the pipeline early, even with a simple model, and improve each part afterwards. A working thin pipeline is worth more than perfect parts that do not connect.

## Key Takeaways
1. Capstone Part 1 connects reproducible training, MLflow tracking and registry, a FastAPI service, Docker, tests and CI/CD in one repository.
2. Choose a public dataset with a clear licence and no personal data, and document the source.
3. Connect the whole pipeline early and collect evidence for each rubric criterion as you build.

## Hands-on Exercise
**Task:** Capstone step 1: build a repository where every push runs tests, and every merge builds and publishes an image of your model API, with the model version tracked in MLflow.
**Tools:** Git and GitHub, GitHub Actions and GitHub Container Registry [VERSION], MLflow, FastAPI, Docker, pytest (all free options).
**Steps:**
1. Choose your dataset and prediction problem. Record the source and licence in the README.
2. Build reproducible training and log at least 3 runs.
3. Register the best model with `champion`, data hash and commit tags.
4. Build the FastAPI service with validation and structured logging.
5. Write the Dockerfile and build the image locally.
6. Write at least 5 tests covering all four types.
7. Add the CI and publish workflows, protect `main`, and merge through a pull request.
8. Add an evidence list to the README with screenshots or links.
**What good looks like:** A public or shareable repository where a pull request runs tests, a failing test blocks merging, and a merge publishes an image tagged with the commit and model version. No secrets, personal data or large data files are committed.
**Time:** about 120 minutes

## Review Flags
- [VERSION] GitHub Actions, GitHub Container Registry and the Actions and Packages interface depend on plan and repository settings; check before recording.
- Learners choose their own dataset; the lesson asks them to check its licence rather than naming one. The worked example is hypothetical.
