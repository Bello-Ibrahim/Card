# Screen Demo Pack: AI-18 L16 Detecting Data and Prediction Drift

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L16_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open a Jupyter notebook in the wine-api project
2. Run: train, _ = load_data(seed=42)
3. Run: new, _ = load_data(seed=7)
4. Run: new['alcohol'] = new['alcohol'] + 0.8

**Narration over this clip (for pacing)**

> Let's simulate the same idea with the wine model. In a notebook, we load a reference sample and a new batch with a different seed. Then we add zero point eight to alcohol in the new batch only.

## Clip 2: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L16_screen_2.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Show the psi() function cell
2. Run the loop over train.columns
3. Highlight: alcohol PSI=0.505 KS p=1.54e-65
4. Highlight the other three rows: PSI 0.003, 0.011, 0.006

**Narration over this clip (for pacing)**

> We run the PSI and KS loop for every feature. Alcohol has a PSI of zero point five zero five, and a KS p-value that is almost zero. The other features have PSI close to zero: zero point zero zero three, zero point zero one one and zero point zero zero six. Only alcohol shifted.

## Clip 3: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L16_screen_3.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Load the champion model
2. Predict probabilities for train and new
3. Run psi() on the two probability arrays and show the result

**Narration over this clip (for pacing)**

> Next, we check prediction drift. We compute PSI on the model's predicted probabilities for both batches. This tells us whether the input shift is also changing the answers.

## Clip 4: scene 12

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L16_screen_4.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Add a markdown cell
2. Type the decision: Investigate: check whether the alcohol measurement or unit changed at the source; retrain only if the change is real and labels are available

**Narration over this clip (for pacing)**

> Finally, we write the decision in the notebook. Investigate. Check whether the alcohol measurement or unit changed at the source. Retrain only if the change is real and labels are available.

## Production notes for this lesson

- [VERIFY] PSI thresholds (below 0.1 little change, 0.1 to 0.25 moderate, above 0.25 large) are commonly quoted rules of thumb, not standards. The voiceover does not state the numbers; it says rules of thumb exist and must be calibrated. If a slide shows them, label them 'rule of thumb, not a standard'.
- [VERIFY] The credit-model drift example (Sofía Castro, Medellín consumer lender) is hypothetical; the voiceover says so and gives no real data.
- [REGION] Lending regulations and fairness review requirements differ by country; the voiceover says only that the review follows local lending rules and states no specific rule.
- PSI and KS outputs (alcohol PSI 0.505 with KS p 1.54e-65; volatile_acidity 0.003, sulphates 0.011, citric_acid 0.006) are real results from the synthetic fallback data (SciPy 1.17.1, NumPy 2.4.6). The voiceover says the KS p-value is almost zero rather than reading the exponent. content.md gives no real value for prediction PSI, so the voiceover states none; show whatever the recording prints.
- The PSI function and loop are shown on screen and never read aloud.
- Credit stock footage must not show identifiable customers, real bank names or logos.
