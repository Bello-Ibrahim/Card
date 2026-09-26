# Screen Demo Pack: AI-13 L15 Common Training Problems and Fixes

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L15_screen_1.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Open assets/L15_broken_A.ipynb in Colab and run all cells unchanged
2. Point to the loss: huge values, then inf, then nan
3. In the 'Your fixed version here' cell: standardise X and y; add torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0) between backward() and step(); re-run and show the loss falling

**Narration over this clip (for pacing)**

> Notebook A trains a linear model on raw inputs in the thousands. The loss explodes to infinity within a few steps, then becomes not a number. She standardises the inputs and targets, adds clipping, and the loss falls smoothly.

## Clip 2: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L15_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open assets/L15_broken_B.ipynb and run all cells
2. Show the ValueError: Target size (torch.Size([32])) must be the same as input size (torch.Size([32, 1]))
3. In the 'Your fixed version here' cell: nn.BCEWithLogitsLoss()(model(xb).squeeze(1), yb.float()); run with no error

**Narration over this clip (for pacing)**

> Notebook B stops with an error. The target size must match the input size. The logits have an extra column, and the labels are integers. She squeezes the logits and turns the labels into floats.

## Clip 3: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L15_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Open assets/L15_broken_C.ipynb and run all cells; point to the loss stuck near 2.30
2. In the 'Your fixed version here' cell, after one backward(): for name, p in model.named_parameters(): print(name, p.grad.norm()); point to the near-zero first-layer weight gradient
3. Same cell: rebuild the model with nn.Linear(64, 64), nn.BatchNorm1d(64), nn.ReLU() per layer; re-run the loop and compare gradient norms and loss

**Narration over this clip (for pacing)**

> In Notebook C, the loss stays flat, near the level of random guessing. Twenty sigmoid layers make the gradients vanish. She prints each layer's gradient norm, and the first layer's is almost zero. With ReLU and batch normalisation, the gradients recover and the loss starts to fall.

## Clip 4: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L15_screen_4.mp4`
- **Target length:** about 25 seconds

**Steps**

1. Open assets/L15_broken_D.ipynb and run all cells; point to the memory printout rising every 5 steps (on CPU also the Colab resource panel)
2. Highlight losses.append(loss)  # keeps every graph alive
3. In the 'Your fixed version here' cell: copy the loop with losses.append(loss.item()), or compute the logged loss inside with torch.no_grad(); run and show memory staying flat

**Narration over this clip (for pacing)**

> In Notebook D, training runs, but memory keeps rising every step. The loop logs an extra loss as a tensor, and that graph was never used for backward, so it is never freed. Logging the plain number with item fixes it, and memory stays flat. Only if memory is still short, reduce the batch size or add mixed precision.

## Production notes for this lesson

- The demo uses the course team's ready-made notebooks assets/L15_broken_A.ipynb to assets/L15_broken_D.ipynb, all tested on CPU. The instructor answer key assets/L15_answer_key.md must not appear on screen or be published with the notebooks.
- Evidence numbers come from the answer key's CPU test run (PyTorch 2.14.0, seed 0) and will differ slightly on other versions; the voiceover gives no exact values. Notebook A reaches inf within a few steps (key: step 3).
- Notebook D: the leak comes from a logged loss whose graph was never used for backward(), as L15 now says. On CPU the symptom is RAM rising every step (key: about 790 MB to 1,020 MB over 45 steps); on a GPU runtime it shows as rising torch.cuda.memory_allocated(), not an actual OOM within one epoch. The voiceover says memory 'keeps rising', not that the GPU crashes. GPU behaviour was not tested by the team.
- [VERSION] PyTorch mixed-precision API: torch.amp.GradScaler("cuda") and torch.autocast; older code uses torch.cuda.amp. Check against the Colab PyTorch version at recording time.
- Nguyen Thi Hoa and the Da Nang logistics firm are hypothetical; stock footage must not show a real company name or logo.
