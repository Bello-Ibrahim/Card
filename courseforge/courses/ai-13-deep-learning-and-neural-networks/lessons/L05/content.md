# L05 The Training Loop

Course: AI-13 · Module: M1 · Objectives: O2, O3 · Video: 6 min (screen demo)

## Hook
In scikit-learn, training is one line: `model.fit(X, y)`. In PyTorch, you write the loop yourself. That sounds like extra work, but it is the reason PyTorch is so flexible: every later lesson in this course is a small change to the loop you write today.

## Explanation
**Dataset and DataLoader.** A `Dataset` answers two questions: how many examples are there (`__len__`), and what is example number `i` (`__getitem__`)? For data already in tensors, `TensorDataset(X, y)` is enough. A `DataLoader` wraps a dataset and gives you **mini-batches**, shuffled for training and in fixed order for validation.

**Batches and epochs.** One **step** processes one batch and updates the weights once. One **epoch** is one full pass over the training data. With 8,000 examples and `batch_size=64`, one epoch has 125 steps. Smaller batches give noisier but more frequent updates; larger batches use the GPU better but need more memory.

**The core loop** has five lines, always in this order:

1. `optimizer.zero_grad()`: clear old gradients.
2. `logits = model(xb)`: forward pass.
3. `loss = loss_fn(logits, yb)`: compute the loss.
4. `loss.backward()`: compute gradients.
5. `optimizer.step()`: update the weights.

**Train and eval modes.** `model.train()` and `model.eval()` switch layers such as dropout (L09) and batch normalisation between their training and inference behaviour. `torch.no_grad()` stops autograd from recording, which saves memory and time during validation. You need both for validation: `eval()` changes layer behaviour, and `no_grad()` turns off gradient tracking.

**Analogy:** The training loop is like a language class. Each batch is one lesson with a few exercises (forward pass). The teacher marks them (loss), explains each error (backward), and the student adjusts (step). An epoch is the whole textbook once. The validation set is a mock exam: no feedback is given during it, and the student does not study from it.

## Worked Example
Folasade is a data scientist at a hypothetical microfinance lender in Ibadan, Nigeria. She has a table of 8,000 loans with 20 numeric features and a "repaid on time" label, and a logistic regression baseline from AI-12. She wants to see whether a small network does better. In the demo, a synthetic table stands in for her data.

**Screen demo steps:**

1. Create and scale the data, and fit the scikit-learn baseline.
2. Wrap the tensors in datasets and loaders.
3. Write the training and validation loop, and print the validation accuracy per epoch.

```python
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X, y = make_classification(n_samples=8000, n_features=20, n_informative=8, random_state=0)
Xtr, Xva, ytr, yva = train_test_split(X, y, test_size=0.2, random_state=0)
sc = StandardScaler().fit(Xtr); Xtr, Xva = sc.transform(Xtr), sc.transform(Xva)
print("logreg:", LogisticRegression().fit(Xtr, ytr).score(Xva, yva))

to_t = lambda a, t: torch.tensor(a, dtype=t)
train_dl = DataLoader(TensorDataset(to_t(Xtr, torch.float32), to_t(ytr, torch.long)), batch_size=64, shuffle=True)
val_dl = DataLoader(TensorDataset(to_t(Xva, torch.float32), to_t(yva, torch.long)), batch_size=256)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = nn.Sequential(nn.Linear(20, 64), nn.ReLU(), nn.Linear(64, 2)).to(device)
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(10):
    model.train()
    for xb, yb in train_dl:
        xb, yb = xb.to(device), yb.to(device)
        opt.zero_grad()
        loss = loss_fn(model(xb), yb)
        loss.backward()
        opt.step()
    model.eval(); correct = 0
    with torch.no_grad():
        for xb, yb in val_dl:
            preds = model(xb.to(device)).argmax(dim=1)
            correct += (preds == yb.to(device)).sum().item()
    print(epoch, round(correct / len(val_dl.dataset), 3))
```

The scaler is fitted on the training split only, as in AI-12. Folasade compares the two scores on the same validation split. On this kind of data, the network may be only slightly better or about the same, and she records that honestly: the network costs more to run and explain, so it must earn its place (L01).

## Common Mistake
Many learners forget `model.eval()` and `torch.no_grad()` during validation, or forget to switch back to `model.train()` at the start of the next epoch. With dropout in the model, validation scores then look noisy and too low, or the model trains with dropout switched off. Put `model.train()` at the top of the training part and `model.eval()` with `torch.no_grad()` around validation, every epoch. Also, never shuffle or augment the validation loader in a way that changes its content.

## Key Takeaways
1. A `Dataset` returns single examples, and a `DataLoader` turns them into shuffled mini-batches; a step is one batch, and an epoch is one full pass.
2. The core loop is always zero_grad, forward, loss, backward, step.
3. Use `model.train()` for training and `model.eval()` with `torch.no_grad()` for validation, and compare against a classical baseline on the same split.

## Hands-on Exercise
**Task:** Write a full training and validation loop for a small tabular classifier and compare its score with a scikit-learn logistic regression.
**Tools:** Google Colab (free; CPU is enough for this size); PyTorch; scikit-learn. Use a public or synthetic dataset, not personal or confidential data.
**Steps:**
1. Load a tabular classification dataset, for example `make_classification` or a public dataset from AI-12, and split it into train and validation sets.
2. Scale features using statistics from the training split only, then fit a logistic regression baseline.
3. Build a `TensorDataset` and `DataLoader` for each split.
4. Write the loop with the five core lines, and add a validation pass with `eval()` and `no_grad()`.
5. Train for 10 to 20 epochs, record training loss and validation accuracy per epoch, and save them in a list for L08.
6. Write three sentences comparing the network with the baseline on score, training time and ease of explanation.
**What good looks like:** A loop that runs on CPU or GPU without device errors, per-epoch metrics, a fair comparison on the same validation split, and an honest conclusion even if the baseline wins.
**Time:** about 35 minutes

## Review Flags
- None. The lesson uses core PyTorch and scikit-learn features and a synthetic dataset; no accuracy values are stated, and the snippet must be run before recording.
