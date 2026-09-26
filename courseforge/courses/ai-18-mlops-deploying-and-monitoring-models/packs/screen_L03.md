# Screen Demo Pack: AI-18 L03 Structuring an ML Project for Production

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L03_screen_1.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open a clean terminal
2. Run: mkdir wine-api && cd wine-api && git init
3. Run: python -m venv .venv, then activate the environment
4. Run: pip install scikit-learn pandas pyyaml joblib and let it finish

**Narration over this clip (for pacing)**

> Let's watch Aarav Mehta, an ML engineer at a hypothetical grocery chain in Pune, refactor the wine notebook. In a terminal, he creates the project folder and starts Git. Then he creates a virtual environment and installs four packages.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L03_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. In the code editor, create config.yaml
2. Show its contents: seed 42, test_size 0.2, model C 1.0, max_iter 1000
3. Highlight the seed line

**Narration over this clip (for pacing)**

> Next, the configuration file. It holds the seed, the test size and the model settings. When he wants to try a new setting, he changes this file, not the code. And because the seed lives here, every function that uses randomness gets the same value.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L03_screen_3.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Create train.py in the editor and show the full script
2. Highlight the line that reads config.yaml
3. Highlight train_test_split with random_state from the config and stratify=y
4. Highlight make_pipeline(StandardScaler(), LogisticRegression(...))
5. Highlight joblib.dump to model.joblib and json.dump to metrics.json

**Narration over this clip (for pacing)**

> Now the training script. It reads the configuration, loads the data, and splits it using the seed from the file. It builds the pipeline, trains it, and measures the F1 score. Then it saves the model and writes the score to a small metrics file. Notice that the scaler is inside the pipeline, so the saved file carries its own preprocessing.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L03_screen_4.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Run: pip freeze > requirements.txt
2. Open requirements.txt and scroll to the scikit-learn and pandas lines with exact versions

**Narration over this clip (for pacing)**

> He pins the exact versions he tested with, using pip freeze. The file now lists every library with an exact version number. Your versions may differ from ours. What matters is that you pin the ones you actually tested.

## Clip 5: scene 12

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L03_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run: python train.py and show the output F1 = 0.5568
2. Run: python train.py again and show the same output F1 = 0.5568
3. Place the two outputs side by side

**Narration over this clip (for pacing)**

> Now the real test. He runs the script twice. On our synthetic data, both runs print an F1 of zero point five five six eight. The score is modest, because the practice data is deliberately noisy. The point is that it is identical.

## Clip 6: scene 13

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L03_screen_6.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Open .gitignore and add model.joblib, metrics.json and data/*.csv
2. Run: git add . and git commit -m "Reproducible training project"
3. Run: git status and show a clean working tree

**Narration over this clip (for pacing)**

> Finally, he adds the model file, the metrics file and the data folder to the ignore file, and commits. Git status shows no model or data files.

## Production notes for this lesson

- [VERSION] The pinned versions in requirements.txt (scikit-learn 1.9.1, pandas 3.0.6) were the versions used to test the code; check and update them before recording. The voiceover does not say version numbers.
- [VERIFY] The Wine Quality dataset licence and location are checked in L04. The demo uses the offline synthetic fallback from data.py, so the voiceover makes no claim about the dataset itself.
- F1 = 0.5568 is a real output from two runs on the synthetic fallback data; it must match on screen. If the recording gives a different value, update the voiceover before release.
- Screen recording: use a clean terminal and editor with a large font. No personal folder names, usernames or tokens visible in the prompt or paths.
- Aarav Mehta and the Pune grocery chain are hypothetical. Git basics are a prerequisite, so the lesson gives a one-line recap only (curriculum judgement call).
