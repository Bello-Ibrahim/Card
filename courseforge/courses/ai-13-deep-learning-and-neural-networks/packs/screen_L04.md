# Screen Demo Pack: AI-13 L04 How Networks Learn: Loss and Backpropagation

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L04_screen_1.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run: w = torch.tensor(0.0, requires_grad=True); loss = (w - 3) ** 2; loss.backward(); print(w.grad)
2. Output: tensor(-6.)

**Narration over this clip (for pacing)**

> In Colab, he creates w at zero and asks PyTorch to track its gradient. He computes the loss, calls backward, and prints the gradient. Minus six, exactly as the hand calculation said.

## Clip 2: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L04_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run the loop cell: lr, history = 0.1, []; w.grad.zero_(); for step in range(10): loss = (w - 3) ** 2; loss.backward(); with torch.no_grad(): w -= lr * w.grad; w.grad.zero_(); history.append(loss.item())
2. Highlight the with torch.no_grad() block and w.grad.zero_()

**Narration over this clip (for pacing)**

> Now the loop. For ten steps, he computes the loss, calls backward, moves w against the gradient inside a no-grad block, and resets the gradient to zero. The learning rate is zero point one.

## Clip 3: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L04_screen_3.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run: print(round(w.item(), 3)) → 2.678
2. Run: plt.plot(history); plt.xlabel("step"); plt.ylabel("loss"); plt.show()
3. Point to the curve falling fast, then flattening

**Narration over this clip (for pacing)**

> After ten steps, w is about two point six eight, close to three. The plot shows the loss falling quickly at first, and then more slowly. Each step moves w twenty percent of the remaining distance.

## Clip 4: scene 13

- **Filename:** `ai-13-deep-learning-and-neural-networks_L04_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Reset w to 0.0, change lr to 1.1 in the loop cell and re-run
2. Re-run the plot cell; point to the loss growing each step

**Narration over this clip (for pacing)**

> Then Bilal changes the learning rate to one point one. Now each step overshoots. W moves further from three every time, and the loss grows. You will see this same pattern in real learning curves in lesson eight.

## Production notes for this lesson

- Review flags: none. Run the snippet before recording and confirm the printed values: w.grad = tensor(-6.) and w after 10 steps = 2.678.
- For the lr = 1.1 comparison, change only the lr value in the same cell and re-run; the plotted loss must grow. Record both plots.
- Bilal and the Lahore logistics company are hypothetical; stock footage must not show a real company name or logo.
