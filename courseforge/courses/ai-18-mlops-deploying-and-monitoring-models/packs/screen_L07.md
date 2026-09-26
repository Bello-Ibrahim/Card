# Screen Demo Pack: AI-18 L07 Input Validation, Errors and Logging

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L07_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open app.py and replace the WineIn class with the validated version
2. Add the logging setup and the log call in /predict
3. Restart uvicorn app:app --reload
4. Open http://127.0.0.1:8000/docs and expand POST /predict

**Narration over this clip (for pacing)**

> Let's watch Chidi Okafor, who maintains a hypothetical price prediction API for a farm marketplace in Lagos. He replaces the wine schema with the validated version, adds the logging code, restarts the server and opens the docs page.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L07_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Try it out with "alcohol": 40 and click Execute
2. Highlight status 422 and the message 'Input should be less than or equal to 15'
3. Remove the sulphates field and click Execute
4. Highlight 422 and 'Field required'

**Narration over this clip (for pacing)**

> First, he sends an alcohol value of forty. The answer is four two two: input should be less than or equal to fifteen. Then he removes sulphates. Four two two again: field required.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L07_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Set "citric_acid": "high" and click Execute
2. Highlight 422 and 'Input should be a valid number, unable to parse string as a number'
3. Restore a valid body, add "email": "a@b.c" and click Execute
4. Highlight 422 and 'Extra inputs are not permitted'

**Narration over this clip (for pacing)**

> Next, he sets citric acid to the word high. The service says the input should be a valid number. Finally, he adds an email field. The answer: extra inputs are not permitted. Four clear errors, and the model was never called.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L07_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Send the valid body from L06 and show status 200
2. Open predictions.jsonl in the editor
3. Highlight model_version "1", the features, probability 0.9318 and latency_ms 18.83

**Narration over this clip (for pacing)**

> Now he sends a valid request, and opens the log file. There is one new line. It shows the event, model version one, the four features, a probability of zero point nine three one eight, and a latency of about nineteen milliseconds on our machine.

## Production notes for this lesson

- [VERSION] Pydantic v2 syntax (Field ge/le, ConfigDict extra=forbid) and the exact 422 message texts were tested with Pydantic 2.13.5 and FastAPI 0.141.1; Pydantic v1 used different syntax and messages. Re-check the message wording before recording.
- The feature limits come from the synthetic fallback data and are approximate; learners use their own training data.
- The logged line (probability 0.9318, latency 18.83 ms, model_version 1) is a real output; latency is spoken with 'on our machine'.
- Screen recording: the test email in step 6 is the dummy a@b.c; never type a real person's email or name.
- Chidi Okafor and the Lagos farm marketplace are hypothetical.
