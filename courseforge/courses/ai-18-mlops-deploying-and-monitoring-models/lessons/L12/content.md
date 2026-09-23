# L12 GitHub Actions: CI for an ML Service

Course: AI-18 · Module: M3 · Objectives: O4 · Video: 5 min (screen demo)

## Hook
Your tests from L11 are excellent, but they only help if someone runs them. On a busy Friday, someone will forget. Continuous integration (CI) runs them for you on every change, and can stop broken code from reaching the main branch.

## Explanation
**GitHub Actions** runs **workflows**: YAML files in `.github/workflows/`. A workflow has:

- **Triggers** (`on:`): events that start it, such as a push or a pull request.
- **Jobs:** groups of steps that run on a **runner**, a fresh virtual machine provided by GitHub (or your own machine).
- **Steps:** either a shell command (`run:`) or a reusable **action** (`uses:`), such as checking out the code.

For our service, CI must install the pinned dependencies, create a small model for the API tests, and run all tests. The runner has no access to your laptop's `mlflow.db`, so CI trains a model from `train.py` and saves it in MLflow format with a two-line script, `export_ci_model.py`:

```python
import joblib, mlflow
mlflow.sklearn.save_model(joblib.load("model.joblib"), "model")
```

The workflow, saved as `.github/workflows/ci.yml`: [VERSION]

```yaml
name: ci
on:
  push:
    branches: [main]
  pull_request:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip
      - run: pip install -r requirements.txt
      - run: python train.py && python export_ci_model.py
      - run: pytest -q
        env:
          MODEL_URI: model
```

`cache: pip` stores downloaded packages between runs, so later runs install faster. Pinned requirements (L03) make the cache reliable and the results repeatable.

CI alone does not block anything. To stop failing code from being merged, **protect the main branch**: require pull requests and require the `test` check to pass before merging. [VERSION]

GitHub Actions is free for public repositories on standard runners, and private repositories get a monthly allowance of free minutes that depends on the account plan. Check the current limits for your account. [VERSION]

**Analogy:** CI is like an automatic safety gate at a factory door. Every box is scanned on the way in. A box that fails the scan is stopped at the door, not found later on a shop shelf.

## Worked Example
Nguyen Thi Lan is a DevOps engineer at a hypothetical travel company in Da Nang, Viet Nam. She adds CI to the wine API on screen:

1. In the repository, create `.github/workflows/ci.yml` with the workflow above, and add `export_ci_model.py`.
2. Commit and push to `main`. Open the **Actions** tab and show the `ci` workflow running, then the green check mark. [VERSION]
3. Open **Settings**, then **Branches** (or **Rules**, depending on the interface), and add a rule for `main` that requires a pull request and the `test` status check. [VERSION]
4. Create a branch: `git switch -c raise-gate`. Change the quality gate to `>= 0.90`, commit and push.
5. Open a pull request. Show the failing `test` check and the disabled merge button with a message that required checks have not passed. [VERSION]
6. Open the failed job log and show the `AssertionError` from the quality gate.
7. Revert the change, push again, wait for the green check, and merge.

The whole cycle shows that the rule, not a person's memory, protects `main`.

## Common Mistake
Many learners put credentials directly in the workflow file, for example a tracking server password in an `env:` block. Workflow files are part of the repository, so everyone with read access can see them, and the secret stays in Git history even after you delete the line. Store credentials as encrypted repository secrets and read them with `${{ secrets.NAME }}`. You will do this in L13. This CI workflow needs no secrets at all, which is the safest design.

## Key Takeaways
1. A GitHub Actions workflow defines triggers, jobs and steps in YAML; our CI installs pinned dependencies, builds a test model and runs pytest.
2. Branch protection turns CI into a gate: pull requests with failing checks cannot be merged into `main`.
3. Cache dependencies to keep runs fast, and never write credentials in workflow files.

## Hands-on Exercise
**Task:** Add a CI workflow to your repository, open a pull request with a failing test, confirm that it is blocked, then fix it and merge.
**Tools:** GitHub (free account), GitHub Actions [VERSION], Git, your `wine-api` project.
**Steps:**
1. Push your project to a GitHub repository. Check that no data files, model files or secrets are committed.
2. Add `.github/workflows/ci.yml` and `export_ci_model.py`, then push.
3. Confirm that the workflow passes in the **Actions** tab.
4. Add a branch protection rule for `main` that requires the `test` check.
5. Create a branch with a deliberately failing test and open a pull request.
6. Screenshot the blocked pull request.
7. Fix the test, push, wait for the check to pass and merge.
**What good looks like:** A green workflow run on `main`, a screenshot of a blocked pull request with a red `test` check, and a merged pull request after the fix. The workflow file contains no credentials.
**Time:** about 35 minutes

## Review Flags
- [VERSION] GitHub Actions free minutes, runner types and the branch protection or rulesets interface depend on the plan and repository type; check current labels and limits before recording.
- [VERSION] Action versions (`actions/checkout@v4`, `actions/setup-python@v5`) and the `ubuntu-latest` runner image should be checked for newer releases. The YAML was checked for valid syntax with PyYAML but was not run on GitHub in this review.
- The CI steps (train, export, pytest) were run locally and passed.
