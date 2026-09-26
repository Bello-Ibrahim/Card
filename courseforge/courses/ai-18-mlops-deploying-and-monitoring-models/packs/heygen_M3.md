# HeyGen Batch Pack: AI-18 M3 (CI/CD for Machine Learning)

Course: MLOps: Deploying and Monitoring Models. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L11 Testing ML Code and Models

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M3_L11_presenter.mp4`
- **Expected length:** about 4.9 minutes (690 words). The quality gate accepts ±10%.

```text
All your tests pass. You deploy the new model. A week later, the business says predictions are worse than before. How can every test be green when the model got worse? Because code tests check the code, not the model.

Welcome to week three, where we automate. Automation needs tests first. An ML service needs four kinds of test, and each one catches problems the others miss. Unit tests check small pieces of code, for example that the data loader returns the expected columns. They are fast and run on every change.

Data tests check the inputs. No missing values, values in the expected range, and the expected share of each label. They catch broken data before training. API tests send requests to the service and check status codes and response shapes. FastAPI's test client does this without starting a real server.

The model quality gate is the one that catches a worse model. It trains or loads the model, and checks a metric on a fixed test set against a minimum, for example, F1 must be at least zero point five.

Set the minimum from evidence: the current champion's score on the same test set, minus a small margin you agree with the business. A gate that is too low catches nothing. One that is too high blocks every change.

Think of a car inspection. Unit tests check each part. Data tests check the fuel. The quality gate is the road test, and API tests check that the doors and controls work for the driver. A car can pass every parts check and still fail the road test.

Fatima Al-Sayed is an ML engineer at a hypothetical e-commerce company in Alexandria, Egypt. She adds tests to our wine API with pytest. All tests live in a tests folder, and a small settings file lets them import the project code.

The first file holds the unit, data and model tests. One checks the columns, one checks that labels are only zero or one, one checks missing values and the alcohol range, and the last trains a model on a fixed split and checks its F1 score.

The second file holds the API tests. It sends one valid wine and one wine with an alcohol value of forty, and expects the service to reject the second one. The test client runs inside a with block, so the start-up code loads the model.

She points the service at the exported model folder and runs pytest. On our machine, the result was six passed, with one deprecation warning from the test client.

Now the important step. She breaks the gate on purpose and raises the minimum to zero point nine. She runs pytest again. The quality gate fails, and the message shows the real score, about zero point five six, below zero point nine. This is exactly how a real, worse model would fail. The code still works, but the metric is below the minimum.

She changes the gate back and runs again, and all tests pass. A test that has never failed has not proved that it can catch anything.

The common mistake is to compute the gate on a new random split each time. The score then moves for reasons unrelated to the model, and the gate fails or passes by chance. Use a fixed test set with a fixed seed, store its data hash, and keep personal data out of it.

Let's recap. First, ML services need unit tests, data tests, model quality gates and API tests. Second, only the quality gate, on a fixed test set, can catch a model that is worse while its code still works. Third, make each test fail on purpose once, to prove that it can catch the problem.

In the exercise below this video, you will write at least five tests covering all four types, make one fail on purpose, screenshot it, and fix it. Add one line on how you chose your threshold. It takes about forty minutes.

Next, we make sure these tests run on every change, without anyone remembering, in GitHub Actions: CI for an ML Service. See you there.
```

## L12 GitHub Actions: CI for an ML Service

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M3_L12_presenter.mp4`
- **Expected length:** about 4.9 minutes (680 words). The quality gate accepts ±10%.

```text
Your tests from the last lesson are excellent, but they only help if someone runs them. On a busy Friday, someone will forget. Continuous integration runs them for you on every change, and can stop broken code from reaching the main branch.

Continuous integration, or CI, means that every change is tested automatically. We use GitHub Actions. It runs workflows, which are YAML files in a special folder of your repository. Each workflow has three parts. Triggers are the events that start it, such as a push or a pull request.

Jobs are groups of steps that run on a runner, a fresh virtual machine provided by GitHub. And each step is either a shell command or a reusable action, such as checking out your code or setting up Python.

Our CI job installs the pinned dependencies, creates a small model, and runs all the tests. The runner cannot see the MLflow database on your laptop, so CI trains a model and saves it in MLflow format with a two-line script. It caches downloaded packages, so later runs install faster. The pinned requirements from lesson three make that cache reliable and the results repeatable.

One more thing. CI alone does not block anything. It only reports. To stop failing code from being merged, protect the main branch. Require pull requests, and require the test check to pass before merging. Now a red check means the change cannot enter main.

Think of an automatic safety gate at a factory door. Every box is scanned on the way in. A box that fails the scan is stopped at the door, not found later on a shop shelf.

Nguyen Thi Lan is a DevOps engineer at a hypothetical travel company in Da Nang, Viet Nam. She adds CI to our wine API. She wants every change tested the same way, whoever makes it.

She creates the workflow file and the small export script. The file says: run on pushes to main and on every pull request, use Python three point eleven with a package cache, install, train, export and test.

She commits and pushes to main. In the Actions tab, the workflow starts on a fresh runner. When the run finishes, it shows a green check mark. Every step passed: install, train, export and test.

Next, she protects main. In the repository settings, she adds a rule that requires a pull request and requires the test check to pass. The menu may be called Branches or Rules, depending on the interface.

Now she tests the gate. She creates a branch, raises the quality gate to zero point nine, commits, pushes and opens a pull request. The test check turns red, and the merge button is disabled because required checks have not passed.

She opens the failed job log and finds the assertion error from the quality gate. Then she reverts the change, pushes again, waits for the green check, and merges. The rule, not a person's memory, protects main.

The common mistake is to put credentials in the workflow file. Everyone with read access can see them, and they stay in Git history, even after you delete the line. Use encrypted repository secrets instead. This CI workflow needs no secrets at all, which is the safest design.

Let's recap. First, a GitHub Actions workflow defines triggers, jobs and steps. Our CI installs pinned dependencies, builds a test model and runs pytest. Second, branch protection turns CI into a gate, so pull requests with failing checks cannot be merged. Third, cache dependencies to keep runs fast, and never write credentials in workflow files.

In the exercise below this video, you will push your project to GitHub, with no data files, model files or secrets, add this workflow, protect main, open a pull request with a failing test, and screenshot the blocked merge. Then you fix it and merge. It takes about thirty-five minutes.

Once the tests pass, the next step is to ship. In the next lesson, Building and Publishing Images Automatically, we build and push the image on every merge. See you there.
```

## L13 Building and Publishing Images Automatically

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M3_L13_presenter.mp4`
- **Expected length:** about 5.0 minutes (692 words). The quality gate accepts ±10%.

```text
Production is running an image called wine API latest. Which model version is inside it? Which commit built it? If the tag cannot answer those questions, a rollback becomes guesswork.

Continuous delivery extends CI. After the tests pass on main, the pipeline builds the Docker image and pushes it to a container registry, which is a store for images. We use GitHub Container Registry, because it works with the token that GitHub Actions gives to each run. Every merge to main then produces a new image, without anyone typing a Docker command.

Two rules make images traceable. First, tag every image with the Git commit ID. This tag is unique and never reused. Second, also tag it with the model version from the MLflow registry, for example model v three. Now the image name tells you both the code and the model. Avoid relying on latest. It moves with every build, so it cannot tell you what is running.

The workflow needs two kinds of credentials. To push to the registry, it uses the built-in token, with permission to write packages and nothing more. To read the champion model, it needs the address of your shared MLflow server. Store that as an encrypted repository secret, and never print it.

The steps are simple. Export the champion model with the script from lesson eight, which writes the model folder and a version file. Log in to the registry, then build and push the image with both tags. Image names must be lower case, so the workflow converts the repository name. If you have no shared tracking server, the lesson page shows a course-only fallback.

Tagging images is like labelling medicine batches with a batch number and the formula version. If a patient reports a problem, the pharmacy can find exactly which batch it was, and remove it, instead of removing every box on the shelf.

Diego Hernández runs the platform team at a hypothetical payments start-up in Guadalajara, Mexico. He publishes the wine API image.

First, the secret. In the repository settings, under secrets and variables, he adds a secret for the tracking server address. We only show its name. GitHub stores the value encrypted.

He adds the publish workflow. It runs only on pushes to main, asks for permission to write packages, exports the model, logs in, and builds and pushes the image with the commit tag and the model tag. He commits it through a pull request, so CI runs first.

He merges the pull request. In the Actions tab, the publish run shows each step: export, login, build and push. In the Packages section, the new image has two tags, the commit ID and model v one.

On his laptop, he pulls the image by its model tag, runs it, and calls the health endpoint. It answers. The image in the registry is the same one that passed the tests.

Finally, he opens the job log. Where the tracking server address would appear, GitHub shows three stars. The secret value never reaches the log.

The common mistake is to pass credentials into the image with a build argument or an environment line. Anyone who pulls the image can read them. Our image needs no secret at runtime, because the model is copied in. If a service needs one, give it when the container starts.

Let's recap. First, after CI passes on main, build the image and push it to a container registry automatically. Second, tag each image with the commit ID and the model version, so you always know what is running and can roll back precisely. Third, store credentials as encrypted secrets, give the workflow the smallest permissions it needs, and never put secrets in images.

In the exercise below this video, you will extend your workflow to push your image to the registry on every merge, with both tags. Then you pull it by its model tag, call predict, and write one sentence on how you would roll back. It takes about forty minutes.

Next, we let the pipeline train and promote models too, with a human in the loop, in Automating Retraining and Promotion. See you there.
```

## L14 Automating Retraining and Promotion

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M3_L14_presenter.mp4`
- **Expected length:** about 4.9 minutes (679 words). The quality gate accepts ±10%.

```text
Every month, someone retrains the model by hand, looks at one number, and deploys it. What if the new model is worse, and that person is on holiday? Automation can do the routine work. A person should still own the decision.

Last lesson, we published images automatically. Now we automate the model itself. A retraining pipeline has three steps. First, retrain on the latest data, and register the result as a new version with the alias challenger.

Second, compare the challenger with the current champion, on the same fixed test set, with the same metric. The challenger must win by a clear margin, not by noise. In our script, it must beat the champion's F1 score by more than zero point zero one.

Third, promote only if the challenger wins, and only after a person approves. Promotion moves the champion alias to the new version, and keeps the old one as previous. So rollback stays one simple step.

In GitHub Actions, a schedule trigger runs the workflow on a timetable, for example every Monday at three in the morning, UTC. A manual trigger adds a run button for testing. For the approval, the promote job uses an environment with required reviewers. It waits until an approved person clicks approve. The timetable uses UTC, so check the time in your own country.

Think of a sports team choosing a goalkeeper. The challenger and the champion play the same training match. The challenger replaces the champion only after a clearly better performance, and the coach still signs the decision.

Nimal Perera is an ML engineer at a hypothetical tea exporter in Kandy, Sri Lanka. He builds the pipeline for the wine model.

Before the workflow, he tests the three scripts locally. The first trains and registers a challenger, using the training script from lesson four. The second loads both models by alias, scores them on the fixed test set, and succeeds only on a clear win. The third moves the aliases.

First, he creates an environment called production in the repository settings, and adds himself as a required reviewer. Then he adds the retrain workflow, with the schedule, the manual trigger, and the two jobs.

He does not wait for Monday. In the Actions tab, he chooses the retrain workflow and clicks run workflow. In the job log, the comparison prints the champion F1 as zero point five five six eight, and the challenger F1 as zero point five three eight zero. The challenger lost.

So the promote job is skipped. In the MLflow registry, champion still points to the same version. Nothing changed, and nobody had to check.

Next, he changes the challenger's training settings so that it wins, and runs the workflow again. This time, the promote job stops and waits for review. Everything before this step ran on its own, but the final step needs a person. He clicks review deployments, then approve.

He refreshes the registry. Champion now points to the new version, and previous points to the old one. If the new model causes trouble, rollback is one alias change.

The common mistake is to compare the challenger's score from its own training run with the champion's score from months ago. Different test data makes the comparison meaningless. Score both models now, on the same fixed test set. If fairness across groups matters, compare that too.

Let's recap. First, a retraining pipeline retrains, compares challenger and champion on the same test set, and promotes only on a clear win. Second, promotion moves the champion alias and keeps the old version as previous, so rollback stays one step. Third, a scheduled workflow can do the routine work, but a person approves the final promotion.

In the exercise below this video, you will build this scheduled workflow, run it once when the challenger loses and once when it wins, approve the promotion, and check the aliases. Add two sentences on your winning margin. It takes about forty-five minutes.

That completes week three. Next week we watch our model in production, starting with Monitoring Model Services. See you there.
```
