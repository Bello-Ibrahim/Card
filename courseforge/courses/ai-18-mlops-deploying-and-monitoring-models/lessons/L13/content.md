# L13 Building and Publishing Images Automatically

Course: AI-18 · Module: M3 · Objectives: O3, O4 · Video: 5 min (screen demo)

## Hook
Production is running an image called `wine-api:latest`. Which model version is inside it? Which commit built it? If the tag cannot answer those questions, a rollback becomes guesswork.

## Explanation
Continuous delivery extends CI: after tests pass on `main`, the pipeline builds the Docker image and pushes it to a **container registry**, a store for images. We use **GitHub Container Registry (GHCR)**, at `ghcr.io`, because it works with the `GITHUB_TOKEN` that GitHub Actions provides to each run. [VERSION]

Two rules make images traceable:

1. **Tag every image with the Git commit ID** (`github.sha`). This tag is unique and never reused.
2. **Also tag it with the model version** from the MLflow registry, for example `model-v3`. Now the image name tells you both the code and the model.

Avoid relying on `latest`. It moves with every build, so it cannot tell you what is running.

The workflow needs two kinds of credentials:

- To **push to GHCR**, it uses the built-in `GITHUB_TOKEN`. You grant it `packages: write` in the workflow's `permissions` block. [VERSION]
- To **read the champion model**, it needs the address of your shared MLflow tracking server, and possibly a user name and password. Store these as **encrypted repository secrets** (Settings, then Secrets and variables, then Actions) and read them with `${{ secrets.NAME }}`. [VERSION] GitHub hides secret values in logs, but a careless `echo` can still expose them in other ways, so never print them.

The workflow first runs `export_model.py` from L08, which loads `models:/wine-quality-clf@champion` and writes `model/` and `model_version.txt`. Then it builds and pushes the image. Save it as `.github/workflows/publish.yml`: [VERSION]

```yaml
name: publish
on:
  push:
    branches: [main]
permissions:
  contents: read
  packages: write
jobs:
  image:
    runs-on: ubuntu-latest
    env:
      MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt && python export_model.py
      - run: |
          echo "MODEL_VERSION=$(cat model_version.txt)" >> "$GITHUB_ENV"
          echo "IMAGE=ghcr.io/${GITHUB_REPOSITORY,,}" >> "$GITHUB_ENV"
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: |
            ${{ env.IMAGE }}:${{ github.sha }}
            ${{ env.IMAGE }}:model-v${{ env.MODEL_VERSION }}
```

`${GITHUB_REPOSITORY,,}` converts the repository name to lower case, because image names must be lower case.

**If you have no shared tracking server:** the runner cannot read your laptop's `mlflow.db`. For the course only, you may replace the export step with `python train.py && python export_ci_model.py` from L12, and commit a `model_version.txt` that you write by hand. Note in your README that the image model is then rebuilt, not copied from the registry.

**Analogy:** Tagging images is like labelling medicine batches with a batch number and the formula version. If a patient reports a problem, the pharmacy can find exactly which batch it was and remove it, instead of removing every box on the shelf.

## Worked Example
Diego Hernández runs the platform team at a hypothetical payments start-up in Guadalajara, Mexico. He publishes the wine API image on screen:

1. In the repository, open **Settings**, then **Secrets and variables**, then **Actions**, and add a secret named `MLFLOW_TRACKING_URI`. [VERSION]
2. Add `.github/workflows/publish.yml` with the workflow above. Commit through a pull request, so CI runs first.
3. Merge the pull request. Open **Actions** and show the `publish` run: export, login, build and push. [VERSION]
4. Open the repository's **Packages** section and show the image with two tags: the commit ID and `model-v1`. [VERSION]
5. Pull the image on the laptop: `docker pull ghcr.io/<owner>/wine-api:model-v1`, run it and call `/health`.
6. Open the job log and show that the secret value appears as `***`.

## Common Mistake
Many learners pass credentials into the image with `--build-arg` or an `ENV` line, so the service can reach the registry later. Build arguments and environment variables are stored in the image metadata and layers, and anyone who pulls the image can read them. Our image does not need any secret at runtime, because the model is copied in. If a service must call another system at runtime, give it the secret when the container starts, from the platform's secret store.

## Key Takeaways
1. After CI passes on `main`, build the image and push it to a container registry automatically.
2. Tag each image with the Git commit ID and the model version so you always know what is running and can roll back precisely.
3. Store credentials as encrypted repository secrets, give the workflow the smallest permissions it needs, and never put secrets in images.

## Hands-on Exercise
**Task:** Extend your workflow to build and push the image to GitHub Container Registry on every merge to `main`, tagged with the commit ID and model version.
**Tools:** GitHub Actions and GitHub Container Registry [VERSION], Docker, MLflow, your `wine-api` project.
**Steps:**
1. Add the tracking server address as a repository secret, or choose the course-only fallback above.
2. Add `publish.yml` with `packages: write` permission.
3. Merge a change to `main` through a pull request.
4. Check that the workflow pushed an image with two tags.
5. Pull the image by its model tag, run it and call `/predict`.
6. Write one sentence explaining how you would roll back to the previous image.
**What good looks like:** A successful `publish` run, an image in GHCR with a commit tag and a model tag, a working container pulled from the registry, and no secret values in the workflow file, image or logs.
**Time:** about 40 minutes

## Review Flags
- [VERSION] GitHub Container Registry permissions (`packages: write`, `GITHUB_TOKEN` access), package visibility defaults and the Secrets and Packages interface depend on plan and repository settings; check before recording.
- [VERSION] Action versions (`docker/login-action@v3`, `docker/build-push-action@v6`) should be checked for newer releases. The YAML was checked for valid syntax with PyYAML but was not run on GitHub in this review.
- The `export_model.py` step was run locally against a SQLite tracking store and produced `model/` and `model_version.txt`.
