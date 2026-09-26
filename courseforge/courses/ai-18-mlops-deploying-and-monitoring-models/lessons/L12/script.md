# L12 GitHub Actions: CI for an ML Service | Presenter Script

Course: AI-18 · Video: 5 min · Words: 682

## Hook
Your tests from the last lesson are excellent, but they only help if someone runs them. On a busy Friday, someone will forget. Continuous integration runs them for you on every change, and can stop broken code from reaching the main branch.

## Explain
Continuous integration, or CI, means that every change is tested automatically. We use GitHub Actions. It runs workflows, which are YAML files in a special folder of your repository. Each workflow has three parts. Triggers are the events that start it, such as a push or a pull request.

Jobs are groups of steps that run on a runner, a fresh virtual machine provided by GitHub. And each step is either a shell command or a reusable action, such as checking out your code or setting up Python.

Our CI job installs the pinned dependencies, creates a small model, and runs all the tests. The runner cannot see the MLflow database on your laptop, so CI trains a model and saves it in MLflow format with a two-line script. It caches downloaded packages, so later runs install faster. The pinned requirements from lesson three make that cache reliable and the results repeatable.

One more thing. CI alone does not block anything. It only reports. To stop failing code from being merged, protect the main branch. Require pull requests, and require the test check to pass before merging. Now a red check means the change cannot enter main.

Think of an automatic safety gate at a factory door. Every box is scanned on the way in. A box that fails the scan is stopped at the door, not found later on a shop shelf.

## Demonstrate
Nguyen Thi Lan is a DevOps engineer at a hypothetical travel company in Da Nang, Viet Nam. She adds CI to our wine API. She wants every change tested the same way, whoever makes it.

She creates the workflow file and the small export script. The file says: run on pushes to main and on every pull request, use Python three point eleven with a package cache, install, train, export and test.

She commits and pushes to main. In the Actions tab, the workflow starts on a fresh runner. When the run finishes, it shows a green check mark. Every step passed: install, train, export and test.

Next, she protects main. In the repository settings, she adds a rule that requires a pull request and requires the test check to pass. The menu may be called Branches or Rules, depending on the interface.

Now she tests the gate. She creates a branch, raises the quality gate to zero point nine, commits, pushes and opens a pull request. The test check turns red, and the merge button is disabled because required checks have not passed.

She opens the failed job log and finds the assertion error from the quality gate. Then she reverts the change, pushes again, waits for the green check, and merges. The rule, not a person's memory, protects main.

The common mistake is to put credentials in the workflow file. Everyone with read access can see them, and they stay in Git history, even after you delete the line. Use encrypted repository secrets instead. This CI workflow needs no secrets at all, which is the safest design.

## Recap
Let's recap. First, a GitHub Actions workflow defines triggers, jobs and steps. Our CI installs pinned dependencies, builds a test model and runs pytest. Second, branch protection turns CI into a gate, so pull requests with failing checks cannot be merged. Third, cache dependencies to keep runs fast, and never write credentials in workflow files.

## CTA
In the exercise below this video, you will push your project to GitHub, with no data files, model files or secrets, add this workflow, protect main, open a pull request with a failing test, and screenshot the blocked merge. Then you fix it and merge. It takes about thirty-five minutes.

Once the tests pass, the next step is to ship. In the next lesson, Building and Publishing Images Automatically, we build and push the image on every merge. See you there.

## Thumbnail
Headline: Tests That Run Themselves
Image: Navy background, a closed gate in front of a branch line with a red cross and a green check mark, headline in teal Inter Bold.

## Production Notes
- [VERSION] GitHub Actions free minutes, runner types and the branch protection or rulesets interface (Settings, then Branches or Rules) depend on the plan and repository type. Check current labels and limits before recording. The voiceover states no free-minute numbers.
- [VERSION] Action versions (actions/checkout@v4, actions/setup-python@v5) and the ubuntu-latest runner image should be checked for newer releases. The YAML was checked for valid syntax with PyYAML but was not run on GitHub in the content review, so the Actions tab, the green check and the blocked merge message must be recorded from a real run.
- The CI steps (train, export, pytest) were run locally and passed. The workflow file is shown on screen and never read aloud.
- No secrets on screen: the CI workflow uses none. Make sure the recorded repository has no data files, model files or credentials committed, and hide account names and tokens in the browser.
- Nguyen Thi Lan and the Da Nang travel company are hypothetical.
