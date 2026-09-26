# Screen Demo Pack: AI-13 L07 Convolutional Neural Networks

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-13-deep-learning-and-neural-networks_L07_screen_1.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Run the model cell from content.md: cnn = nn.Sequential(nn.Conv2d(1, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2), nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2), nn.Flatten(), nn.Linear(64 * 7 * 7, 10))
2. Same cell: mlp = nn.Sequential(nn.Flatten(), nn.Linear(784, 256), nn.ReLU(), nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, 10))

**Narration over this clip (for pacing)**

> In Colab, he defines the CNN. Two blocks of convolution, ReLU and pooling, with thirty-two and then sixty-four filters. Then flatten, and one linear layer to ten classes. He also defines the fully connected network for comparison.

## Clip 2: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L07_screen_2.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Run: count = lambda m: sum(p.numel() for p in m.parameters()); print(count(cnn), count(mlp))
2. Output: 50186 235146

**Narration over this clip (for pacing)**

> He counts the parameters. Fifty thousand, one hundred and eighty-six for the CNN, and two hundred and thirty-five thousand, one hundred and forty-six for the other network. The CNN has about one fifth of the parameters.

## Clip 3: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L07_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Run: x = torch.randn(8, 1, 28, 28); for layer in cnn: x = layer(x); print(type(layer).__name__, tuple(x.shape))
2. Point to (8, 32, 14, 14), then (8, 64, 7, 7), then Flatten (8, 3136), then Linear (8, 10)

**Narration over this clip (for pacing)**

> Next, the most useful debugging tool in this lesson. He passes a dummy batch through the CNN, one layer at a time, and prints the shape after each. He can see the image shrink and the channels grow, and the exact size the linear layer needs.

## Clip 4: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L07_screen_4.mp4`
- **Target length:** about 28 seconds

**Steps**

1. Run the L05 training loop for cnn, 5 epochs; then for mlp with the same optimiser and lr (on CPU: 10,000-image subset)
2. Show the final validation accuracy of each model side by side (expected output: CNN higher)

**Narration over this clip (for pacing)**

> He trains both models for five epochs with the loop from lesson five, the same optimiser and the same learning rate. You should see something like the CNN reaching a higher validation accuracy. Rafael reports his own measured numbers rather than assuming a result. If you are on a CPU, train on a subset of ten thousand images, so each epoch finishes in a few minutes.

## Production notes for this lesson

- [VERIFY] Fashion-MNIST licence and source (carried from L06): confirm before the dataset is used in the recording.
- Parameter counts on screen must match content.md: 50186 for the CNN and 235146 for the fully connected network.
- Accuracy: content.md gives no numbers. The voiceover says 'you should see something like the CNN reaching a higher validation accuracy'. Show the real measured values; do not add numbers in captions.
- Hook figures (about 150 million weights for a 224×224×3 → 1,000 fully connected layer; under 2,000 for 64 filters of 3×3×3 plus biases) are from content.md.
- On CPU, train on a 10,000-image subset so each epoch takes a few minutes; speed up the training segment in the edit.
- Rafael and the Recife e-commerce company are hypothetical; stock footage must not show a real company name or logo.
