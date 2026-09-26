# Screen Demo Pack: AI-18 L11 Testing ML Code and Models

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L11_screen_1.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Show pytest.ini with [pytest] and pythonpath = .
2. Open tests/test_model.py
3. Highlight test_load_data_columns and the labels test
4. Highlight test_no_missing_or_out_of_range
5. Highlight test_quality_gate with random_state=42 and the check f1_score >= 0.50

**Narration over this clip (for pacing)**

> The first file holds the unit, data and model tests. One checks the columns, one checks that labels are only zero or one, one checks missing values and the alcohol range, and the last trains a model on a fixed split and checks its F1 score.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L11_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Open tests/test_api.py
2. Highlight the GOOD example wine
3. Highlight test_rejects_out_of_range expecting status 422
4. Highlight the with TestClient(app) as client block

**Narration over this clip (for pacing)**

> The second file holds the API tests. It sends one valid wine and one wine with an alcohol value of forty, and expects the service to reject the second one. The test client runs inside a with block, so the start-up code loads the model.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L11_screen_3.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Run: export MODEL_URI=model
2. Run: pytest -q
3. Highlight the output '6 passed' and the single warning

**Narration over this clip (for pacing)**

> She points the service at the exported model folder and runs pytest. On our machine, the result was six passed, with one deprecation warning from the test client.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L11_screen_4.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Edit test_quality_gate: change >= 0.50 to >= 0.90
2. Run: pytest -q
3. Highlight 'FAILED ... test_quality_gate'
4. Highlight 'AssertionError: assert 0.5568181818181818 >= 0.9'

**Narration over this clip (for pacing)**

> Now the important step. She breaks the gate on purpose and raises the minimum to zero point nine. She runs pytest again. The quality gate fails, and the message shows the real score, about zero point five six, below zero point nine. This is exactly how a real, worse model would fail. The code still works, but the metric is below the minimum.

## Clip 5: scene 12

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L11_screen_5.mp4`
- **Target length:** about 11 seconds

**Steps**

1. Change the gate back to >= 0.50
2. Run: pytest -q
3. Show all tests passing

**Narration over this clip (for pacing)**

> She changes the gate back and runs again, and all tests pass. A test that has never failed has not proved that it can catch anything.

## Production notes for this lesson

- [VERSION] FastAPI TestClient depends on an HTTP client library; with Starlette 1.7.0 it printed a deprecation warning about the httpx package. Check the current recommended dependency before recording. Tested with pytest 9.1.1. The voiceover mentions one warning but does not name the package.
- Test outputs ('6 passed' with one deprecation warning, and 'AssertionError: assert 0.5568181818181818 >= 0.9') are real outputs from the synthetic fallback data. The voiceover rounds the score to about zero point five six. If the recording gives different numbers, show the recorded output and update the voiceover to match.
- The test code is shown on screen, not read aloud. Set MODEL_URI=model before running pytest (the folder exported in L08).
- Fatima Al-Sayed and the Alexandria e-commerce company are hypothetical.
