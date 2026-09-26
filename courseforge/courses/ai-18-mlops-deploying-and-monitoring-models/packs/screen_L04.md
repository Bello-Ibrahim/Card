# Screen Demo Pack: AI-18 L04 Experiment Tracking with MLflow

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 7

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L04_screen_1.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Open a terminal in the wine-api folder with the virtual environment active
2. Run: pip install mlflow
3. Show track.py in the editor, scrolling past the loop over C values
4. Run: python track.py and let it finish

**Narration over this clip (for pacing)**

> In a terminal in the project folder, she installs MLflow. She creates a small tracking script with the loop you just saw, and runs it. Three runs are logged, one for each value of C. Each run gets a clear name that includes its setting, so she can find it again later without guessing.

## Clip 2: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L04_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run: mlflow ui --backend-store-uri sqlite:///mlflow.db
2. Open the printed local address, usually http://127.0.0.1:5000, in the browser
3. Click the wine-quality experiment
4. Show the runs table with logreg-C-1.0, logreg-C-0.1 and logreg-C-0.01

**Narration over this clip (for pacing)**

> Next, she starts the MLflow interface, pointing it at the same database file. She opens the local address that it prints, and clicks the wine quality experiment. The table shows all three runs, with their names.

## Clip 3: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L04_screen_3.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Tick the checkboxes of all three runs
2. Click Compare
3. Show the comparison view with the parameter C and the metric f1 side by side
4. Highlight the values 0.557, 0.538 and 0.461

**Narration over this clip (for pacing)**

> She selects all three runs and clicks Compare. Now the parameter C and the F1 score sit side by side. With C of one, F1 is zero point five five seven. With C of zero point one, it is zero point five three eight. With C of zero point zero one, it drops to zero point four six one.

## Clip 4: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L04_screen_4.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Go back to the runs table and open logreg-C-1.0
2. Click the Artifacts tab
3. Expand the model folder to show the saved model files

**Narration over this clip (for pacing)**

> Beatriz chooses C of one. The strongest regularisation clearly underfits. She opens the best run and shows the Artifacts tab, where the saved model folder waits. The difference between C of one and C of zero point one is small, so on more data she might check both again. Her scores on the real dataset will be different.

## Production notes for this lesson

- [VERIFY] Wine Quality dataset: confirm the licence, current location on the UCI Machine Learning Repository, and the description of its origin (Portuguese vinho verde). The voiceover does not state these; it only says the demo uses the offline synthetic data.
- [VERSION] MLflow interface labels (experiment list, Compare, Artifacts tab), the mlflow ui command and its default port 5000, the name= versus artifact_path= argument, and the skops default serialisation were checked against MLflow 3.16.1 only. Re-check before recording and update screen_steps if labels moved.
- F1 values 0.557, 0.538 and 0.461 are real results on the synthetic fallback data, not the real dataset; they must match on screen.
- Beatriz Carvalho and the wine cooperative are hypothetical.
- The tracking store is a local SQLite file; do not show any shared tracking server address or credentials on screen.
