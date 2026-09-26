# L13 Building and Publishing Images Automatically | Presenter Script

Course: AI-18 · Video: 5 min · Words: 695

## Hook
Production is running an image called wine API latest. Which model version is inside it? Which commit built it? If the tag cannot answer those questions, a rollback becomes guesswork.

## Explain
Continuous delivery extends CI. After the tests pass on main, the pipeline builds the Docker image and pushes it to a container registry, which is a store for images. We use GitHub Container Registry, because it works with the token that GitHub Actions gives to each run. Every merge to main then produces a new image, without anyone typing a Docker command.

Two rules make images traceable. First, tag every image with the Git commit ID. This tag is unique and never reused. Second, also tag it with the model version from the MLflow registry, for example model v three. Now the image name tells you both the code and the model. Avoid relying on latest. It moves with every build, so it cannot tell you what is running.

The workflow needs two kinds of credentials. To push to the registry, it uses the built-in token, with permission to write packages and nothing more. To read the champion model, it needs the address of your shared MLflow server. Store that as an encrypted repository secret, and never print it.

The steps are simple. Export the champion model with the script from lesson eight, which writes the model folder and a version file. Log in to the registry, then build and push the image with both tags. Image names must be lower case, so the workflow converts the repository name. If you have no shared tracking server, the lesson page shows a course-only fallback.

Tagging images is like labelling medicine batches with a batch number and the formula version. If a patient reports a problem, the pharmacy can find exactly which batch it was, and remove it, instead of removing every box on the shelf.

## Demonstrate
Diego Hernández runs the platform team at a hypothetical payments start-up in Guadalajara, Mexico. He publishes the wine API image.

First, the secret. In the repository settings, under secrets and variables, he adds a secret for the tracking server address. We only show its name. GitHub stores the value encrypted.

He adds the publish workflow. It runs only on pushes to main, asks for permission to write packages, exports the model, logs in, and builds and pushes the image with the commit tag and the model tag. He commits it through a pull request, so CI runs first.

He merges the pull request. In the Actions tab, the publish run shows each step: export, login, build and push. In the Packages section, the new image has two tags, the commit ID and model v one.

On his laptop, he pulls the image by its model tag, runs it, and calls the health endpoint. It answers. The image in the registry is the same one that passed the tests.

Finally, he opens the job log. Where the tracking server address would appear, GitHub shows three stars. The secret value never reaches the log.

The common mistake is to pass credentials into the image with a build argument or an environment line. Anyone who pulls the image can read them. Our image needs no secret at runtime, because the model is copied in. If a service needs one, give it when the container starts.

## Recap
Let's recap. First, after CI passes on main, build the image and push it to a container registry automatically. Second, tag each image with the commit ID and the model version, so you always know what is running and can roll back precisely. Third, store credentials as encrypted secrets, give the workflow the smallest permissions it needs, and never put secrets in images.

## CTA
In the exercise below this video, you will extend your workflow to push your image to the registry on every merge, with both tags. Then you pull it by its model tag, call predict, and write one sentence on how you would roll back. It takes about forty minutes.

Next, we let the pipeline train and promote models too, with a human in the loop, in Automating Retraining and Promotion. See you there.

## Thumbnail
Headline: What Is Running Now?
Image: Navy background, a shipping container with two labels, a commit ID and 'model-v1', headline in teal Inter Bold.

## Production Notes
- [VERSION] GitHub Container Registry permissions (packages: write, GITHUB_TOKEN access), package visibility defaults and the Secrets and Packages interface depend on plan and repository settings. Check them before recording.
- [VERSION] Action versions (docker/login-action@v3, docker/build-push-action@v6) should be checked for newer releases. The YAML was checked for valid syntax with PyYAML but was not run on GitHub in the content review, so the publish run, the Packages page and the masked log must be recorded from a real run.
- No secrets on screen: when adding the MLFLOW_TRACKING_URI secret, type the value off camera or blur the value field. Show only the secret name. In the job log, show the masked '***' value. Blur account names and the real tracking server address if they appear.
- The export_model.py step was run locally against a SQLite tracking store and produced model/ and model_version.txt. The workflow file is shown on screen and never read aloud. The commit ID tag on screen will differ from the thumbnail example.
- Learners without a shared tracking server may use the course-only fallback (train.py and export_ci_model.py with a hand-written model_version.txt); the voiceover mentions it briefly and the lesson page has the details.
- Diego Hernández and the Guadalajara payments start-up are hypothetical.
