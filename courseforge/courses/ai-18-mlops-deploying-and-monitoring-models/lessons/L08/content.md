# L08 Containerising the Model Service

Course: AI-18 · Module: M2 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
Your API runs on your laptop. Will it run on the server with the same Python version, the same libraries and the same model file? A container makes the answer "yes" by shipping all of them together. But a careless container can also be slow to start, too large, and a security risk.

## Explanation
You already know basic Docker: images, containers, `docker build` and `docker run`. For a production model service, four choices matter most.

1. **A small base image.** A "slim" Python image contains much less than the full image, so it downloads faster and has fewer packages that could contain vulnerabilities. [VERSION]
2. **A multi-stage build.** The first stage installs or compiles dependencies. The second, final stage copies only the results. Build tools and caches stay behind and do not enter the final image.
3. **A non-root user.** By default, processes in a container run as root. If an attacker breaks into the service, a non-root user limits what they can do.
4. **Where the model comes from.** You have two options:
   - **Copy the model into the image.** The image is self-contained and starts fast, and the image tag identifies exactly one model. You need a new image for every model version.
   - **Load from the registry at start-up.** One image can serve any version, but start-up depends on the registry being available, and the container needs registry credentials at runtime.

In this course we copy the model into the image, because it makes rollback simple: run the previous image. Before building, export the champion model from the registry to a local `model/` folder with a small script (`export_model.py`) that calls `mlflow.sklearn.load_model("models:/wine-quality-clf@champion")` and then `mlflow.sklearn.save_model(model, "model")`.

Image size and start-up time matter when a platform starts many copies of your service during a traffic peak.

Never put secrets in a Dockerfile or image. Anyone who can pull the image can read its layers and environment variables. Pass secrets at runtime, for example with `docker run --env-file`, and keep that file out of Git.

**Analogy:** A container is like a shipping container for goods. Everything the product needs travels inside it, so it arrives the same at every port. A multi-stage build packs the product without the factory tools.

## Worked Example
Lars Eriksson is a platform engineer at a hypothetical energy company in Gothenburg, Sweden. He containerises the wine API on screen:

1. Export the champion: `python export_model.py`. It prints "exported wine-quality-clf v1" and creates `model/` and `model_version.txt`.
2. Create `.dockerignore` with `.venv`, `mlflow.db`, `mlruns`, `data`, `*.jsonl`, `.git` and `.env`.
3. Create this `Dockerfile`: [VERSION]
```dockerfile
# Stage 1: build wheels
FROM python:3.11-slim AS build
WORKDIR /src
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Stage 2: runtime
FROM python:3.11-slim
WORKDIR /app
COPY --from=build /wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels \
    && useradd --create-home appuser && chown appuser /app
COPY app.py .
COPY model/ ./model/
ENV MODEL_URI=/app/model
USER appuser
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```
4. Build: `docker build -t wine-api:v1 .`
5. Run: `docker run --rm -p 8000:8000 -e MODEL_VERSION=1 wine-api:v1`, then open `http://127.0.0.1:8000/health`.
6. Show the size with `docker images wine-api`. Then show the size of a single-stage build that uses the full `python:3.11` base image, and compare the two.
7. Check the user: `docker run --rm wine-api:v1 whoami` prints `appuser`. The `chown` line lets this user write `predictions.jsonl` from L07.

Record your own sizes; they depend on your requirements and platform.

## Common Mistake
Many learners copy the whole project folder with `COPY . .`. This silently adds the virtual environment, the MLflow database, log files and sometimes a `.env` file with passwords. The image becomes large, and secrets leak to anyone who pulls it. Copy only the files the service needs, and use a `.dockerignore` file as a second safety net.

## Key Takeaways
1. Use a slim base image, a multi-stage build and a non-root user for model services.
2. Copying the model into the image makes each image tag identify one model and makes rollback simple; loading from the registry gives flexibility but adds a start-up dependency.
3. Never put secrets in a Dockerfile or image; pass them at runtime and exclude them with `.dockerignore`.

## Hands-on Exercise
**Task:** Write a Dockerfile for your service, build the image, run it locally, and reduce the image size by at least one technique. Record the size before and after.
**Tools:** Docker Desktop or Docker Engine (free for personal and many small-business uses; check the licence terms for your organisation) [VERSION], your `wine-api` project.
**Steps:**
1. Write a simple single-stage Dockerfile with the full `python:3.11` base image. Build it and record the size.
2. Export the champion model to `model/`.
3. Apply at least one technique: slim base image, multi-stage build, `--no-cache-dir`, or a `.dockerignore` file.
4. Build again and record the new size.
5. Run the container and call `/health` and `/predict`.
6. Confirm that the container runs as a non-root user.
7. Write two sentences: which technique saved the most space, and whether you would copy the model into the image or load it at start-up for your use case.
**What good looks like:** Two recorded image sizes with the technique that changed them. The container answers `/health` and `/predict`. `whoami` does not print `root`. No `.env` file, database or virtual environment is inside the image.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Docker base image names and tags (`python:3.11-slim`, `python:3.11`) and build features such as multi-stage builds: check current tags and supported Python versions before recording. The Dockerfile was not built in this review environment.
- [VERSION] Docker Desktop licence terms for organisations change; check before recommending it.
- Judgement call carried from the curriculum: Docker basics are a prerequisite, so the lesson recaps them in one sentence.
