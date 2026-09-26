# L17 Capstone Part 1: Build and Automate | Presenter Script

Course: AI-18 · Video: 5 min · Words: 684

## Hook
You have built each part of a production ML system separately. Now you connect them, in one repository, where a single merge to main produces a tested, versioned, deployable model API, without any manual copying.

## Explain
Welcome to the capstone. You will deploy and monitor a model API. Part one, this lesson, covers the build and the automation. Part two, the final lesson, adds monitoring, a runbook and a short demo.

First, choose a dataset and a problem. Pick a public tabular dataset with a clear prediction target, a licence that allows your use, and no personal data. Write the source and licence in your README. You may continue with the wine example, but a new dataset shows more skill. If you cannot download data, use a synthetic dataset with a fixed seed, as in lesson three.

Your repository needs seven parts. Reproducible training with pinned packages and fixed seeds. Tracking and a registry, with at least three runs and a champion model tagged with its data hash and Git commit. A FastAPI service with validation and structured logs. And a slim container that runs as a non-root user.

Then the automation. Tests of all four types. CI that runs them on every push and pull request, with main protected. And publishing, so every merge builds and pushes an image tagged with the commit ID and the model version.

The rubric gives points for training and versioning, the containerised API with tests and CI and CD, monitoring and drift, the release and rollback plan, and the runbook and demo. Read it now, so you collect evidence while you build. Keep screenshots of your MLflow runs, the registry page, a blocked pull request and the published image.

The capstone is like assembling a car from parts you have already tested one by one. The engine, brakes and lights each worked on the bench. Now you fit them together, connect the wires, and prove that the whole car drives.

## Demonstrate
Leila Haddad is a data scientist at a hypothetical insurance company in Casablanca, Morocco. For her capstone, she predicts whether a household appliance will need repair within a year, using a public tabular dataset with no personal data.

She starts from her template from lesson three, replaces the data loader with one for her dataset, and writes the source and licence in the README. She trains twice and shows identical metrics.

She logs four runs to MLflow, compares them, and registers the best. The registry shows the champion alias, the data hash tag and the commit tag.

She exports the model, builds the image and runs the container. From the interactive docs page, she sends one valid request and one invalid request. Then she runs pytest, and all tests pass.

She pushes a branch with a broken quality gate and opens a pull request. The merge is blocked. She fixes it and merges. In Actions and Packages, the new image appears with its commit tag and model tag. She adds each screenshot to her evidence list, with one link or screenshot for each rubric criterion.

The common mistake is to build all the parts first and connect them on the last day. Then all the integration problems appear together. Connect the pipeline early, even with a simple model. A working thin pipeline is worth more than perfect parts that do not connect.

## Recap
Let's recap. First, capstone part one connects reproducible training, MLflow tracking and registry, a FastAPI service, Docker, tests and CI and CD, in one repository. Second, choose a public dataset with a clear licence and no personal data, and document the source. Third, connect the whole pipeline early, and collect evidence for each rubric criterion as you build.

## CTA
Your exercise is capstone step one. Build a repository where every push runs tests, a failing test blocks merging, and every merge publishes an image tagged with the commit and model version. Commit no secrets, personal data or large data files. Plan about two hours.

In the final lesson, Capstone Part 2: Monitor, Document and Present, you add monitoring, a runbook and your demo. See you there.

## Thumbnail
Headline: One Merge, Whole Pipeline
Image: Navy background, a single merge arrow feeding a chain of connected icons (tests, container, registry), headline in teal Inter Bold.

## Production Notes
- [VERSION] GitHub Actions, GitHub Container Registry and the Actions and Packages interface depend on plan and repository settings; check before recording.
- Learners choose their own dataset; the lesson asks them to check its licence and names no dataset. The screen recording of Leila's repair project must use a public tabular dataset with a licence that allows this use and no personal data, or a synthetic dataset with a fixed seed. Show the source and licence lines in the README but do not name a dataset in the voiceover.
- content.md gives no real metric values for Leila's project, so the voiceover states none. Show whatever the recording prints.
- No secrets on screen: blur tokens, account names and any tracking server address. Commands and workflow files are shown on screen and never read aloud.
- Leila Haddad and the Casablanca insurance company are hypothetical.
