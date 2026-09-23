# L07 Convolutional Neural Networks

Course: AI-13 · Module: M2 · Objectives: O2, O3 · Video: 6 min (screen demo)

## Hook
A fully connected layer that looks at a small 224×224 colour photo and outputs 1,000 features needs about 150 million weights for that one layer. A convolutional layer that finds 64 kinds of pattern in the same photo needs under 2,000. This lesson explains how that is possible, and why it also works better.

## Explanation
A fully connected network flattens the image into one long vector. It ignores the fact that nearby pixels belong together, and a pattern learned in the top-left corner must be learned again for every other position.

A **convolution** fixes both problems. A **filter** (also called a kernel) is a small grid of weights, for example 3×3. It slides across the image, and at each position it computes a weighted sum of the pixels under it. The result is a **feature map** that is high wherever the pattern appears. Two ideas make this efficient:

- **Local connections:** each output looks only at a small patch.
- **Weight sharing:** the same filter is used at every position, so a pattern learned once is detected everywhere.

`nn.Conv2d(in_channels, out_channels, kernel_size, padding)` learns `out_channels` filters, each with `in_channels × k × k` weights plus a bias. `padding=1` with a 3×3 kernel keeps the height and width the same.

**Pooling** (`nn.MaxPool2d(2)`) keeps the largest value in each 2×2 block, which halves the height and width. This reduces computation and makes the network less sensitive to small shifts.

A typical small CNN repeats **conv → ReLU → pool** a few times. The spatial size shrinks while the number of channels grows. Early layers learn edges and simple textures; later layers combine them into parts and shapes. At the end, the feature maps are flattened and passed to a linear layer for classification.

**Analogy:** A convolution filter is like a small stamp-shaped window that you move across a large map, looking for one symbol, such as a bridge. You use the same window everywhere, so you only need to learn once what a bridge looks like. A second person then scans your list of bridges, rivers and roads, and finds bigger patterns such as "town".

## Worked Example
Rafael is an ML engineer at a hypothetical e-commerce company in Recife, Brazil. He compares a CNN with the fully connected network from L03 on Fashion-MNIST, using the transforms from L06.

**Screen demo steps:**

1. Define the CNN and print the shape after each block with a dummy input.
2. Count parameters for both models.
3. Train both with the loop from L05 for the same number of epochs, and compare validation accuracy.

```python
import torch
from torch import nn

cnn = nn.Sequential(
    nn.Conv2d(1, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),   # 32 x 14 x 14
    nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2),  # 64 x 7 x 7
    nn.Flatten(),
    nn.Linear(64 * 7 * 7, 10),
)
mlp = nn.Sequential(nn.Flatten(), nn.Linear(784, 256), nn.ReLU(),
                    nn.Linear(256, 128), nn.ReLU(), nn.Linear(128, 10))

count = lambda m: sum(p.numel() for p in m.parameters())
print(count(cnn), count(mlp))            # 50186 235146

x = torch.randn(8, 1, 28, 28)
for layer in cnn:
    x = layer(x); print(type(layer).__name__, tuple(x.shape))
```

The CNN has about one fifth of the parameters of the fully connected network. Rafael trains both for 5 epochs with the same optimiser and learning rate. The expected output is that the CNN reaches a higher validation accuracy than the fully connected network, but he reports his own measured numbers rather than assuming a result. On CPU, he trains on a 10,000-image subset so that each epoch finishes in a few minutes.

The shape printout is the most useful debugging tool in this lesson. If the first linear layer has the wrong input size, the error appears at the `Flatten` step, and the printout shows the size you need.

## Common Mistake
Many learners calculate the input size of the first linear layer by hand and get it wrong after changing padding, kernel size or the number of pooling layers. The error message "mat1 and mat2 shapes cannot be multiplied (8x3136 and 1568x10)" tells you the real size: the first matrix is `(batch, features)`. Pass a dummy batch through the convolutional part and print the shape, or use `nn.LazyLinear(10)`, which works out its input size on the first forward pass. Another mistake is forgetting the channel dimension for greyscale images: the input must be `(N, 1, 28, 28)`, not `(N, 28, 28)`.

## Key Takeaways
1. A convolution slides a small shared filter across the image, so it detects a pattern anywhere with very few weights.
2. Stacks of conv → ReLU → pool shrink the spatial size and grow the channels, moving from edges to shapes to objects.
3. Print shapes with a dummy batch to size the final linear layer correctly, and compare models on parameters as well as accuracy.

## Hands-on Exercise
**Task:** Train a small CNN on Fashion-MNIST and compare its accuracy and parameter count with a fully connected network.
**Tools:** Google Colab with a GPU runtime (free; optional), or CPU with a 10,000-image training subset; PyTorch; torchvision.
**Steps:**
1. Reuse your datasets and transforms from L06 and your training loop from L05.
2. Build the CNN above and a fully connected network, and print both parameter counts.
3. Train each model for 5 epochs with the same optimiser, learning rate and batch size, and record training loss and validation accuracy per epoch.
4. Record the time per epoch for each model.
5. Fill a small table: model, parameters, best validation accuracy, time per epoch. Save the per-epoch values for L08.
**What good looks like:** Both models train without shape errors, the comparison uses identical settings and the same validation data, the table uses your own measured numbers, and you write two sentences explaining the difference using weight sharing and local connections.
**Time:** about 40 minutes

## Review Flags
- [VERIFY] Fashion-MNIST licence and source (carried from L06), because the dataset is used again in this lesson.
