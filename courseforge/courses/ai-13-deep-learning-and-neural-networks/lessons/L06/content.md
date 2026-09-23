# L06 Image Data and Transforms

Course: AI-13 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Flip a photo of a shirt from left to right and it is still a shirt. Your network does not know that until you show it. Data augmentation is how you teach it, but if you apply it in the wrong place, your validation scores stop meaning anything.

## Explanation
**Images as tensors.** A colour image is a tensor of shape `(3, H, W)`, and a greyscale image is `(1, H, W)`. Pixel values usually arrive as integers from 0 to 255 and are converted to floats from 0 to 1. A batch adds the first dimension: `(N, C, H, W)` (L02).

**torchvision datasets.** `torchvision.datasets` downloads common datasets with one line. In this module we use **Fashion-MNIST**: small 28×28 greyscale images of clothing items in 10 classes, with a standard training and test split. It is a harder drop-in replacement for the classic handwritten digits dataset. Check its licence before you reuse it outside the course. [VERIFY]

**Transforms** are functions applied to each image when it is loaded. You chain them with `transforms.Compose`. [VERSION] Newer torchvision versions also offer a `transforms.v2` module with the same main ideas.

- `ToTensor()` converts an image to a float tensor from 0 to 1.
- `Normalize(mean, std)` subtracts the per-channel mean and divides by the standard deviation, so inputs are centred near 0. This helps optimisation. The mean and standard deviation must be computed on the **training set only**.
- **Augmentations** create random variations each time an image is loaded: `RandomHorizontalFlip`, `RandomCrop` with padding, `RandomRotation`, `ColorJitter`. The model sees a slightly different version of each image in each epoch, which reduces overfitting (L09).

**Augment training data only.** Validation and test images must go through the same deterministic steps (`ToTensor`, `Normalize`, any resize) but no random changes. Otherwise your validation score changes from run to run and no longer measures performance on real images.

Choose augmentations that keep the label true. A horizontal flip is fine for clothing. A vertical flip is not, because an upside-down shoe is not a realistic input. For digits, flipping a 2 does not produce a 2.

**Analogy:** Augmentation is like a teacher who writes the same maths problem with different numbers and wording each time. The student learns the method, not the exact page. But the final exam must be a fixed paper; if you changed the exam questions randomly for each student, the marks would not be comparable.

## Worked Example
Mei Lin is an ML engineer at a hypothetical online clothing retailer in Penang, Malaysia. She wants to prototype a product-type classifier with Fashion-MNIST before using her company's own photos.

**Screen demo steps:**

1. Download the training set with only `ToTensor` and compute the mean and standard deviation.
2. Define separate training and evaluation transforms.
3. Show a grid of augmented samples.

```python
import torch
from torchvision import datasets, transforms
from torchvision.utils import make_grid
import matplotlib.pyplot as plt

raw = datasets.FashionMNIST("data", train=True, download=True)
pixels = raw.data.float() / 255            # (60000, 28, 28)
mean, std = pixels.mean().item(), pixels.std().item()
print(round(mean, 3), round(std, 3))

train_tf = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomCrop(28, padding=2),
    transforms.ToTensor(),
    transforms.Normalize((mean,), (std,)),
])
eval_tf = transforms.Compose([transforms.ToTensor(), transforms.Normalize((mean,), (std,))])

train_ds = datasets.FashionMNIST("data", train=True, transform=train_tf)
test_ds = datasets.FashionMNIST("data", train=False, transform=eval_tf)

imgs = torch.stack([train_ds[0][0] for _ in range(16)])   # same image, 16 augmentations
plt.imshow(make_grid(imgs * std + mean, nrow=8).permute(1, 2, 0)); plt.axis("off"); plt.show()
```

The expected output for the mean is roughly 0.29 and for the standard deviation roughly 0.35; confirm the exact values when you run it. The grid shows the same item shifted and sometimes flipped. Mei Lin notes that the grid is also a useful check: if the images look destroyed, the augmentation is too strong.

## Common Mistake
The most common mistake is passing the training transform, with augmentation, to the validation or test dataset as well. A related mistake is computing normalisation statistics on the full dataset, including the test set. Both make your evaluation less honest. Build two transform pipelines, compute statistics on training data only, and pass the right pipeline to each split. If you create a validation split with `random_split`, remember that both parts share one transform, so create two dataset objects instead.

## Key Takeaways
1. Images are tensors of shape `(C, H, W)`; convert them to floats and normalise with the training set's mean and standard deviation.
2. Augmentation creates label-preserving random variations of training images to reduce overfitting; choose changes that keep the label true.
3. Apply augmentation to training data only; validation and test data get the same fixed preprocessing and nothing random.

## Hands-on Exercise
**Task:** Load Fashion-MNIST, show a grid of augmented samples, and compute the mean and standard deviation for normalisation.
**Tools:** Google Colab (free; CPU is enough); PyTorch; torchvision; matplotlib.
**Steps:**
1. Download the Fashion-MNIST training set and compute the pixel mean and standard deviation on it.
2. Build a training transform with at least two augmentations and an evaluation transform with none.
3. Show a grid of 16 augmented versions of one image and a grid of 16 different evaluation images.
4. Try one augmentation that breaks the label, such as a vertical flip or a strong rotation, and describe why you would not use it.
5. Split 10% of the training set for validation, using separate dataset objects so that the validation part has no augmentation.
**What good looks like:** Correct statistics from the training set only, two clearly separated pipelines, readable image grids, and a reasoned choice of augmentations.
**Time:** about 25 minutes

## Review Flags
- [VERIFY] Fashion-MNIST licence and source must be confirmed before the dataset is named and used in recordings.
- [VERSION] torchvision transforms API (classic `transforms` compared with `transforms.v2`) must be checked against the version in Colab at recording time.
