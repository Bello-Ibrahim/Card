# L15 Common Training Problems and Fixes | Presenter Script

Course: AI-13 · Video: 5 min · Words: 617

## Hook
Your loss prints not a number at step eight. Or it never moves. Or memory runs out after ten minutes. Each looks like a disaster. But most have a small number of causes, and you can check them in a fixed order.

## Explain
First, NaN or exploding loss. The loss grows fast, becomes infinity, then not a number. Usual causes are a learning rate that is too high, inputs with very large values, or an invalid operation. Normalise the inputs, lower the learning rate, and add gradient clipping between backward and step.

Second, vanishing gradients. The loss hardly moves, and the early layers' gradients are close to zero. Gradients are multiplied layer by layer on the way back, and sigmoid makes each factor small. Use ReLU, normalisation layers, residual connections, or fewer layers. Diagnose by printing each layer's gradient norm.

Third, the wrong loss for the label shape. Cross-entropy wants logits with one column per class, and integer labels. The binary loss wants float labels with the same shape as the logits. Fourth, out of memory. Use a smaller batch, mixed precision, and do not keep graphs alive by accident.

Debugging is like a mechanic with a car that will not start. A good mechanic does not replace the engine first. They check the fuel, then the battery, then the spark plugs. Cheapest check first.

Here is the checklist. Read the full error, and print shapes, types and devices. Overfit one small batch. Check the loss and label format. Lower the learning rate by ten. Print gradient norms. Check memory per step.

## Demonstrate
Nguyen Thi Hoa is an engineer at a logistics firm in Da Nang, Vietnam. She inherits four broken notebooks. You can open the same four from the course page.

Notebook A trains a linear model on raw inputs in the thousands. The loss explodes to infinity within a few steps, then becomes not a number. She standardises the inputs and targets, adds clipping, and the loss falls smoothly.

Notebook B stops with an error. The target size must match the input size. The logits have an extra column, and the labels are integers. She squeezes the logits and turns the labels into floats.

In Notebook C, the loss stays flat, near the level of random guessing. Twenty sigmoid layers make the gradients vanish. She prints each layer's gradient norm, and the first layer's is almost zero. With ReLU and batch normalisation, the gradients recover and the loss starts to fall.

In Notebook D, training runs, but memory keeps rising every step. The loop logs an extra loss as a tensor, and that graph was never used for backward, so it is never freed. Logging the plain number with item fixes it, and memory stays flat.

A common mistake is answering every problem by changing the learning rate or the architecture, without reading the error first. A missing zero grad, or a stored loss tensor, can look like a tuning problem. Follow the checklist, one change at a time.

## Recap
Let's recap. First, NaN or exploding loss usually means a high learning rate or unscaled inputs. Normalise, lower the rate, and clip gradients. Second, vanishing gradients show as a flat loss and near-zero early gradients. Use ReLU, normalisation or fewer layers. Third, for memory problems, stop storing graphs, reduce the batch size and use mixed precision. And for any problem, follow a fixed checklist.

## CTA
Now it is your turn. In the exercise below this video, you will debug the four broken notebooks yourself, and record the symptom, the cause, the fix and the evidence for each one. It takes about forty minutes. In the next lesson, we tune hyperparameters and learning-rate schedules. See you there.

## Thumbnail
Headline: Debug Training in Order
Image: Navy background, a loss chart that shoots up to NaN with a teal numbered checklist beside it, headline in teal Inter Bold.

## Production Notes
- The demo uses the course team's ready-made notebooks assets/L15_broken_A.ipynb to assets/L15_broken_D.ipynb, all tested on CPU. The instructor answer key assets/L15_answer_key.md must not appear on screen or be published with the notebooks.
- Evidence numbers come from the answer key's CPU test run (PyTorch 2.14.0, seed 0) and will differ slightly on other versions; the voiceover gives no exact values. Notebook A reaches inf within a few steps (key: step 3).
- Notebook D: the leak comes from a logged loss whose graph was never used for backward(), as L15 now says. On CPU the symptom is RAM rising every step (key: about 790 MB to 1,020 MB over 45 steps); on a GPU runtime it shows as rising torch.cuda.memory_allocated(), not an actual OOM within one epoch. The voiceover says memory 'keeps rising', not that the GPU crashes. GPU behaviour was not tested by the team.
- [VERSION] PyTorch mixed-precision API: torch.amp.GradScaler("cuda") and torch.autocast; older code uses torch.cuda.amp. Check against the Colab PyTorch version at recording time.
- Nguyen Thi Hoa and the Da Nang logistics firm are hypothetical; stock footage must not show a real company name or logo.
