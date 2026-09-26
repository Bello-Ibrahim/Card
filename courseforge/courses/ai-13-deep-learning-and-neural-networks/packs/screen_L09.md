# Screen Demo Pack: AI-13 L09 Regularisation: Dropout, Weight Decay and Early Stopping

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L09_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run the model cell from content.md: the L07 CNN with nn.Flatten(), nn.Dropout(0.3), nn.Linear(64 * 7 * 7, 10)
2. Run: opt = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)
3. Highlight nn.Dropout(0.3) and weight_decay=1e-2

**Narration over this clip (for pacing)**

> First, he adds a dropout layer with a rate of zero point three, just before the final linear layer. Then he switches the optimiser to AdamW, with a weight decay of zero point zero one.

## Clip 2: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L09_screen_2.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run the early-stopping loop from content.md: best_loss, best_state, patience, bad_epochs = float("inf"), None, 3, 0; for epoch in range(30): train_one_epoch(model, opt); val_loss = evaluate(model)
2. Highlight best_state = copy.deepcopy(model.state_dict())
3. Show the printed line: stopping at epoch …

**Narration over this clip (for pacing)**

> Next, the early-stopping block around his loop from lesson five, with a patience of three. After each epoch, if the validation loss improves, he saves a deep copy of the weights. If not, he counts a bad epoch, and after three in a row, he stops.

## Clip 3: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L09_screen_3.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run: model.load_state_dict(best_state)
2. Run the original model and the regularised model with the same data, seed and lr

**Narration over this clip (for pacing)**

> At the end, he loads the best weights back into the model. Then he runs two experiments with the same data, seed and learning rate. The original model, and the regularised one.

## Clip 4: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L09_screen_4.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Plot both validation loss curves on one chart with plot_curves from L08 (expected output: regularised curve lower for longer, smaller train–validation gap)
2. Add a two-row results table: run, best validation loss, best epoch

**Narration over this clip (for pacing)**

> He plots both validation curves on one chart. You should see something like this. The regularised model's validation loss stays lower for longer, and the gap between training and validation gets smaller. He compares the best scores, not the final ones, and records both runs in a small table.

## Production notes for this lesson

- Review flags: none. Hyperparameter ranges (dropout 0.1 to 0.5, weight decay about 1e-4 to 1e-2) are starting points for tuning, not claims about results.
- The comparison result is said as 'you should see something like' (content.md: expected result). Show the real curves from the two runs; do not add numbers in captions.
- train_one_epoch and evaluate are the learner's own helpers from L05; define them in a hidden cell above the demo cell before recording.
- Hamid and the Agadir argan-oil cooperative are hypothetical; stock footage must not show a real company name or logo.
