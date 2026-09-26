# Screen Demo Pack: AI-18 L12 GitHub Actions: CI for an ML Service

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L12_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open the wine-api repository in the editor
2. Create .github/workflows/ci.yml with the CI workflow from content.md
3. Highlight the on: push/pull_request block, then the four steps
4. Create export_ci_model.py (two lines)

**Narration over this clip (for pacing)**

> She creates the workflow file and the small export script. The file says: run on pushes to main and on every pull request, use Python three point eleven with a package cache, install, train, export and test.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L12_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Commit and push to main
2. Open the Actions tab on GitHub
3. Show the ci workflow running
4. Show the green check mark on the completed run

**Narration over this clip (for pacing)**

> She commits and pushes to main. In the Actions tab, the workflow starts on a fresh runner. When the run finishes, it shows a green check mark. Every step passed: install, train, export and test.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L12_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open Settings, then Branches (or Rules)
2. Add a rule for main
3. Tick 'require a pull request before merging'
4. Add the required status check: test
5. Save the rule

**Narration over this clip (for pacing)**

> Next, she protects main. In the repository settings, she adds a rule that requires a pull request and requires the test check to pass. The menu may be called Branches or Rules, depending on the interface.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L12_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run: git switch -c raise-gate
2. Change the quality gate to >= 0.90, commit and push
3. Open a pull request
4. Show the failing test check and the disabled merge button with its message

**Narration over this clip (for pacing)**

> Now she tests the gate. She creates a branch, raises the quality gate to zero point nine, commits, pushes and opens a pull request. The test check turns red, and the merge button is disabled because required checks have not passed.

## Clip 5: scene 12

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L12_screen_5.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open the failed job log and highlight the AssertionError from test_quality_gate
2. Revert the change, commit and push
3. Wait for the green test check
4. Merge the pull request

**Narration over this clip (for pacing)**

> She opens the failed job log and finds the assertion error from the quality gate. Then she reverts the change, pushes again, waits for the green check, and merges. The rule, not a person's memory, protects main.

## Production notes for this lesson

- [VERSION] GitHub Actions free minutes, runner types and the branch protection or rulesets interface (Settings, then Branches or Rules) depend on the plan and repository type. Check current labels and limits before recording. The voiceover states no free-minute numbers.
- [VERSION] Action versions (actions/checkout@v4, actions/setup-python@v5) and the ubuntu-latest runner image should be checked for newer releases. The YAML was checked for valid syntax with PyYAML but was not run on GitHub in the content review, so the Actions tab, the green check and the blocked merge message must be recorded from a real run.
- The CI steps (train, export, pytest) were run locally and passed. The workflow file is shown on screen and never read aloud.
- No secrets on screen: the CI workflow uses none. Make sure the recorded repository has no data files, model files or credentials committed, and hide account names and tokens in the browser.
- Nguyen Thi Lan and the Da Nang travel company are hypothetical.
