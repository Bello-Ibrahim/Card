# Screen Demo Pack: AI-18 L17 Capstone Part 1: Build and Automate

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L17_screen_1.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Create the capstone-api repository from the L03 template
2. Replace data.py with a loader for her dataset
3. Show the source and licence lines in README.md
4. Run python train.py twice and show identical metrics

**Narration over this clip (for pacing)**

> She starts from her template from lesson three, replaces the data loader with one for her dataset, and writes the source and licence in the README. She trains twice and shows identical metrics.

## Clip 2: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L17_screen_2.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Log 4 runs to MLflow
2. Open the MLflow UI and compare the runs
3. Run python register.py
4. Show the registered model with the champion alias, data hash tag and Git commit tag

**Narration over this clip (for pacing)**

> She logs four runs to MLflow, compares them, and registers the best. The registry shows the champion alias, the data hash tag and the commit tag.

## Clip 3: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L17_screen_3.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run: python export_model.py
2. Run: docker build -t repair-api:dev .
3. Run: docker run -p 8000:8000 repair-api:dev
4. Open /docs and send one valid and one invalid request
5. Run: pytest -q and show all tests passing

**Narration over this clip (for pacing)**

> She exports the model, builds the image and runs the container. From the interactive docs page, she sends one valid request and one invalid request. Then she runs pytest, and all tests pass.

## Clip 4: scene 12

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L17_screen_4.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Push a branch with a deliberately broken quality gate
2. Open a pull request and show the blocked merge
3. Fix the gate, wait for the green check and merge
4. Open Actions and show the publish run
5. Open Packages and show the image with commit and model tags
6. Show the evidence list in README.md

**Narration over this clip (for pacing)**

> She pushes a branch with a broken quality gate and opens a pull request. The merge is blocked. She fixes it and merges. In Actions and Packages, the new image appears with its commit tag and model tag. She adds each screenshot to her evidence list, with one link or screenshot for each rubric criterion.

## Production notes for this lesson

- [VERSION] GitHub Actions, GitHub Container Registry and the Actions and Packages interface depend on plan and repository settings; check before recording.
- Learners choose their own dataset; the lesson asks them to check its licence and names no dataset. The screen recording of Leila's repair project must use a public tabular dataset with a licence that allows this use and no personal data, or a synthetic dataset with a fixed seed. Show the source and licence lines in the README but do not name a dataset in the voiceover.
- content.md gives no real metric values for Leila's project, so the voiceover states none. Show whatever the recording prints.
- No secrets on screen: blur tokens, account names and any tracking server address. Commands and workflow files are shown on screen and never read aloud.
- Leila Haddad and the Casablanca insurance company are hypothetical.
