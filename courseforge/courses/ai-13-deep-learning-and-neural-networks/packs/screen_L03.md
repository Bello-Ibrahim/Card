# Screen Demo Pack: AI-13 L03 Neurons, Layers and Activations

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L03_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Run the FaultNet cell from content.md: class FaultNet(nn.Module) with nn.Sequential(nn.Linear(n_in, 256), nn.ReLU(), nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, n_classes))
2. Highlight the comment '# logits, no activation' on the last layer
3. Highlight forward(self, x): return self.net(x)

**Narration over this clip (for pacing)**

> In Colab, she defines a model called FaultNet. Inside it, a sequential block goes from seven hundred and eighty-four inputs to two hundred and fifty-six, then to one hundred and twenty-eight, then to ten outputs. There is a ReLU after each hidden layer, and nothing after the last one.

## Clip 2: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L03_screen_2.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Run: model = FaultNet(); n_params = sum(p.numel() for p in model.parameters()); print(n_params)
2. Output: 235146

**Narration over this clip (for pacing)**

> Next, she counts the parameters by adding up the size of every weight and bias tensor. The total is two hundred and thirty-five thousand, one hundred and forty-six.

## Clip 3: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L03_screen_3.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Run: x = torch.randn(16, 784); logits = model(x); print(logits.shape)
2. Output: torch.Size([16, 10])
3. Run: probs = logits.softmax(dim=1); highlight the comment 'only for reading, not for the loss'

**Narration over this clip (for pacing)**

> Finally, a forward pass. She sends a random batch of sixteen events through the model and gets sixteen rows of ten logits. One row per event, one score per fault type. Softmax turns them into probabilities, but only for reading, never for the loss.

## Production notes for this lesson

- Review flags: none. Run the FaultNet cell once before recording and confirm the printed parameter count 235146 and the output shape torch.Size([16, 10]).
- Hand-count slide must match content.md exactly: 784×256 + 256 = 200,960; 256×128 + 128 = 32,896; 128×10 + 10 = 1,290; total 235,146.
- Aroha and the Wellington energy company are hypothetical; stock footage must not show a real company name or logo.
