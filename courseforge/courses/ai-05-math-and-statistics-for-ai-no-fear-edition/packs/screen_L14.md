# Screen Demo Pack: AI-05 L14 Gradient Descent Step by Step

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L14_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open a Colab notebook and a new code cell.
2. Type: import matplotlib.pyplot as plt
3. Type the descend(lr, steps=30) function line by line: w, losses = 0.0, []; for step in range(steps); grad = 2 * (w - 3); w = w - lr * grad; losses.append((w - 3) ** 2); return w, losses
4. Highlight the two comment lines: derivative, and step against the gradient.

**Narration over this clip (for pacing)**

> Now in Colab. Aroha types a function called descend. It starts w at zero. In a loop, it calculates the gradient, steps against it, and saves the loss after each step. It runs for thirty steps.

## Clip 2: scene 10

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L14_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Type the loop: for lr in [0.01, 0.1, 1.1]: w, losses = descend(lr); print(lr, round(w, 4)); plt.plot(losses, label=f"lr={lr}")
2. Type: plt.yscale("log"); plt.legend(); plt.show()
3. Run the cell.

**Narration over this clip (for pacing)**

> Then she runs it for three learning rates, zero point zero one, zero point one and one point one. She prints the final weight for each, and plots the loss curves. The vertical axis uses a log scale, where each grid line is ten times the one below.

## Clip 3: scene 11

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L14_screen_3.mp4`
- **Target length:** about 27 seconds

**Steps**

1. Zoom in on the printed lines: 0.01 1.3635, 0.1 2.9963, 1.1 -709.1289.
2. Point at the three loss curves: slow falling line, fast line that flattens, and a line that rises steeply.

**Narration over this clip (for pacing)**

> Look at the output. With zero point zero one, w has only reached about one point three six after thirty steps: too slow. With zero point one, it is two point nine nine six three, very close to three. With one point one, it is about minus seven hundred and nine. It jumped across the valley, further every time. That is divergence.

## Production notes for this lesson

- [VERSION] Google Colab and Matplotlib: confirm the current Colab interface and that plt.yscale("log") and plt.legend() behave as shown before recording the screen scenes. Outputs (0.01 → 1.3635, 0.1 → 2.9963, 1.1 → −709.1289) were checked with Python and NumPy 2.4.
- Aroha and the Wellington setting are fictional. The toy loss (w − 3)² is a teaching example.
- Say the update rule as 'the new weight equals the old weight minus the learning rate times the gradient'; the slide shows the formula.
- Optional hero B-roll (scene 5): if the stock search finds a suitable misty hillside walker, use stock instead and drop the hero clip.
