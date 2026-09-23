# L10 Transfer Learning with Pretrained CNNs

Course: AI-13 · Module: M2 · Objectives: O4 · Video: 6 min (screen demo)

## Hook
You have about a thousand labelled photos of bean leaves. That is far too few to train a deep CNN from scratch. But a network that has already seen a very large number of everyday photos knows a lot about edges, textures and shapes. What if you only had to teach it the last step?

## Explanation
**Transfer learning** reuses a network trained on a large dataset, such as ImageNet, for a new task. The early and middle layers have learned general visual features that are useful for almost any photo. Only the last layer is specific to the original 1,000 classes.

The standard recipe has two stages:

1. **Feature extraction:** load the pretrained model, **freeze** the backbone (`requires_grad = False`), and **replace the final layer** with a new one for your classes. Train only the new layer. This is fast and needs little data.
2. **Fine-tuning:** unfreeze the last block or two and train them together with the new layer, with a **smaller learning rate** for the pretrained layers, so that you adjust their features gently instead of destroying them.

Two details are easy to miss. First, preprocess images **the same way the model was trained**: same resize, crop, mean and standard deviation. In torchvision, each weights object gives you this with `weights.transforms()`. Second, use the new API for weights: `resnet18(weights=ResNet18_Weights.DEFAULT)`. Older tutorials use `pretrained=True`, which has been deprecated or removed in newer versions. [VERSION]

Pretrained checkpoints have their own licences and training data. Check both before you use a model in a product. [VERIFY]

**Analogy:** An experienced chef learns a new cuisine much faster than a beginner. The chef already knows how to cut, season and control heat, and only needs to learn the new dishes. Feature extraction is the chef following new recipes with old skills. Fine-tuning is the chef also adjusting some techniques, carefully, for the new cuisine.

## Worked Example
Grace is a data scientist at a hypothetical agricultural extension service in Mbale, Uganda. Farmers send leaf photos, and she wants to classify them as healthy, angular leaf spot or bean rust. She uses the bean-leaf disease dataset on the Hugging Face Hub, collected in Uganda. [VERIFY] The dataset ID and licence must be checked on its Hub page before use.

**Screen demo steps:**

1. Load ResNet-18 with pretrained weights and freeze it.
2. Replace `model.fc` with a 3-class layer and count trainable parameters.
3. Load the dataset and apply the weights' own transforms.
4. Train only the new head for a few epochs with the loop from L05.
5. Unfreeze `layer4` and continue with a lower learning rate for it.

```python
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision.models import resnet18, ResNet18_Weights
from datasets import load_dataset

weights = ResNet18_Weights.DEFAULT                    # [VERSION]
model = resnet18(weights=weights)
for p in model.parameters():
    p.requires_grad = False
model.fc = nn.Linear(model.fc.in_features, 3)         # new head, trainable
preprocess = weights.transforms()

ds = load_dataset("AI-Lab-Makerere/beans")            # [VERIFY] ID and licence
def to_tensors(batch):
    batch["x"] = [preprocess(img.convert("RGB")) for img in batch["image"]]
    return batch
ds = ds.with_transform(to_tensors)
collate = lambda b: (torch.stack([e["x"] for e in b]), torch.tensor([e["labels"] for e in b]))
train_dl = DataLoader(ds["train"], batch_size=32, shuffle=True, collate_fn=collate)

opt = torch.optim.AdamW(model.fc.parameters(), lr=1e-3)   # stage 1: head only
# ... train 3-5 epochs, then stage 2:
for p in model.layer4.parameters():
    p.requires_grad = True
opt = torch.optim.AdamW([
    {"params": model.layer4.parameters(), "lr": 1e-4},
    {"params": model.fc.parameters(), "lr": 1e-3},
])
```

In stage 1, only 1,539 parameters are trainable (512 × 3 + 3), so each epoch is fast, even on CPU. Grace compares three runs on the validation split: her CNN from L07 adapted to 3-channel images and trained from scratch, the frozen ResNet with a new head, and the fine-tuned ResNet. The expected result is that both pretrained runs do clearly better than training from scratch on this small dataset, but she reports her own measured numbers.

## Common Mistake
Many learners freeze the backbone but pass `model.parameters()` to the optimiser and then wonder what is trained, or unfreeze layers but forget to rebuild the optimiser, so the new parameters are never updated. Build the optimiser after you set `requires_grad`, and print the count of trainable parameters. Another common mistake is using your own normalisation values, such as Fashion-MNIST's, instead of the pretrained model's. The features then receive inputs in a range they never saw during pretraining.

## Key Takeaways
1. Transfer learning reuses a pretrained backbone's general features: freeze it, replace the final layer, and train the new head first.
2. Fine-tune a few top layers afterwards with a smaller learning rate, and rebuild the optimiser whenever you change what is trainable.
3. Preprocess with the pretrained weights' own transforms, and check the licences of both the checkpoint and the dataset.

## Hands-on Exercise
**Task:** Fine-tune a pretrained ResNet on the bean-leaf dataset and compare accuracy with your CNN trained from scratch.
**Tools:** Google Colab with a GPU runtime (free; optional); PyTorch; torchvision; Hugging Face `datasets`. CPU fallback: train the frozen-backbone stage only, or use half of the training images.
**Steps:**
1. Load the dataset and check its Hub page for the class names, split sizes and licence. [VERIFY]
2. Train your L07-style CNN from scratch (with 3 input channels) for 10 epochs as a baseline.
3. Load ResNet-18 with `weights=`, freeze it, replace the head, and train for 5 epochs. [VERSION]
4. Unfreeze `layer4`, rebuild the optimiser with a lower learning rate for it, and train for 3 to 5 more epochs.
5. Fill a table: run, trainable parameters, best validation accuracy, time per epoch.
6. Write three sentences on which run you would choose and why.
**What good looks like:** Three comparable runs on the same validation split, correct trainable-parameter counts, the weights' own preprocessing, and a justified choice based on your numbers.
**Time:** about 45 minutes

## Review Flags
- [VERSION] torchvision pretrained weights API: `weights=` and `ResNet18_Weights.DEFAULT` replaced `pretrained=True` in newer versions; check against the Colab version at recording time.
- [VERIFY] Bean-leaf disease dataset (Uganda): Hub dataset ID, source, class names and licence must be confirmed; also the licence of the ImageNet-pretrained ResNet-18 checkpoint.
