# L02 Tensors: The Language of PyTorch

Course: AI-13 · Module: M1 · Objectives: O1, O3 · Video: 5 min (screen demo)

## Hook
Your first PyTorch error will probably not be about maths. It will say something like "mat1 and mat2 shapes cannot be multiplied". Most beginner bugs in deep learning are shape bugs, and this lesson teaches you to read and fix them quickly.

## Explanation
A **tensor** is PyTorch's main data structure. If you know NumPy arrays, you already know most of it. A tensor has three properties you should check all the time:

- **shape**: the size of each dimension, for example `(32, 3, 64, 64)`.
- **dtype**: the number type, for example `torch.float32` for inputs and weights, or `torch.int64` (also called `long`) for class labels.
- **device**: where it lives, `cpu` or `cuda:0`.

Two tensors in one operation must have compatible shapes, and they must be on the **same device**. Two extra features make tensors different from NumPy arrays: they can run on a GPU, and they can record operations for automatic gradients (L04).

**Conventions.** In PyTorch, the first dimension is almost always the **batch**. Images use `(N, C, H, W)`: batch, channels, height, width. This is different from many image libraries, which use `(H, W, C)`.

**Reshaping.** `view` and `reshape` change the shape without changing the data. `-1` means "work out this size for me". `permute` reorders dimensions, for example from `(H, W, C)` to `(C, H, W)`. `unsqueeze(0)` adds a batch dimension of size 1; `squeeze` removes dimensions of size 1.

**Broadcasting** follows the same rules as NumPy: dimensions are compared from the right, and a size of 1 can stretch to match. This is how you subtract a per-channel mean of shape `(3, 1, 1)` from a batch of shape `(32, 3, 64, 64)`.

**Analogy:** A tensor's shape is like a stack of egg trays. One tray has rows and columns. A stack adds layers. A box of stacks adds one more dimension. Reshaping moves the eggs into trays of a different size, but the number of eggs never changes. If the numbers do not multiply to the same total, the reshape fails.

## Worked Example
Tomás is an ML engineer at a hypothetical agritech start-up in Valparaíso, Chile. He loads grape photos with an image library and wants to feed them to a network.

**Screen demo steps:** run each line and print `x.shape` after it.

```python
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"

x = torch.rand(32, 64, 64, 3)          # N, H, W, C from an image library
x = x.permute(0, 3, 1, 2)              # -> N, C, H, W
print(x.shape, x.dtype, x.device)      # torch.Size([32, 3, 64, 64]) float32 cpu

mean = torch.tensor([0.5, 0.4, 0.3]).view(3, 1, 1)
x = (x - mean)                         # broadcasting per channel
x = x.to(device)

flat = x.reshape(x.shape[0], -1)       # -> (32, 12288) for a linear layer
labels = torch.randint(0, 5, (32,))    # int64 class IDs
single = x[0].unsqueeze(0)             # one image with batch dim: (1, 3, 64, 64)
```

Tomás then gets this error: `Expected all tensors to be on the same device`. His model is on the GPU but `labels` is still on the CPU. He fixes it with `labels = labels.to(device)`. This error is common, and the fix is always to move both tensors to one device.

## Common Mistake
Many learners use `view` or `reshape` when they need `permute`. Both produce shape `(32, 3, 64, 64)` from `(32, 64, 64, 3)`, but `reshape` only reinterprets the numbers in memory order, so the pixels are mixed and the image is destroyed. No error appears; the model just learns badly. Use `permute` to reorder dimensions, and `reshape` only to merge or split dimensions that are already in the right order. A second common mistake is forgetting the batch dimension when predicting on one example: always pass `(1, C, H, W)`, not `(C, H, W)`.

## Key Takeaways
1. Check shape, dtype and device for every tensor you create; most bugs show up in one of the three.
2. PyTorch puts the batch first, and images use `(N, C, H, W)`; use `permute` to reorder dimensions and `reshape` or `view` only to merge or split them.
3. Broadcasting compares shapes from the right, and all tensors in one operation must be on the same device.

## Hands-on Exercise
**Task:** Create tensors for a batch of 32 colour images of 64×64 pixels, move them to the GPU, and fix 3 shape errors in a provided cell.
**Tools:** Google Colab with a GPU runtime (free), or CPU if no GPU is available; PyTorch.
**Steps:**
1. Create `imgs = torch.rand(32, 3, 64, 64)` and print its shape, dtype and device.
2. Move it to the GPU (or keep it on CPU) with `.to(device)` and print the device again.
3. Fix the three errors in the provided cell:
```python
w = torch.rand(3 * 64 * 64, 10, device=device)
out = imgs @ w                        # error 1: flatten first
one = imgs[0]; out1 = one.reshape(1, -1) @ w.T   # error 2: wrong matrix side
bias = torch.rand(10, 1); out + bias  # error 3: bias shape
```
4. For each fix, write one line explaining the shape rule you used.
5. Convert a `(64, 64, 3)` image to `(1, 3, 64, 64)` with `permute` and `unsqueeze`.
**What good looks like:** Three working fixes (flatten to `(32, 12288)`, use `w` not `w.T`, bias of shape `(10,)`), each with a correct one-line reason, and no `reshape` used where `permute` was needed.
**Time:** about 20 minutes

## Review Flags
- None. The content covers stable, core PyTorch tensor operations and uses a hypothetical example; snippets must still be run once before recording.
