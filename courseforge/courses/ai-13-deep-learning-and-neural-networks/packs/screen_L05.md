# Screen Demo Pack: AI-13 L05 The Training Loop

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-13-deep-learning-and-neural-networks_L05_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run: X, y = make_classification(n_samples=8000, n_features=20, n_informative=8, random_state=0)
2. Run: train_test_split(X, y, test_size=0.2, random_state=0); sc = StandardScaler().fit(Xtr); transform Xtr and Xva
3. Run: print("logreg:", LogisticRegression().fit(Xtr, ytr).score(Xva, yva))

**Narration over this clip (for pacing)**

> She creates the synthetic data, splits it, and fits the scaler on the training part only, as in the scikit-learn course. Then she fits the logistic regression baseline and prints its validation score.

## Clip 2: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L05_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run: train_dl = DataLoader(TensorDataset(... torch.float32 ..., ... torch.long ...), batch_size=64, shuffle=True)
2. Run: val_dl = DataLoader(TensorDataset(...), batch_size=256)

**Narration over this clip (for pacing)**

> Next, she wraps the arrays in tensor datasets, with float features and long integer labels. The training loader uses batches of sixty-four and shuffles. The validation loader uses bigger batches and does not shuffle.

## Clip 3: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L05_screen_3.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Run: model = nn.Sequential(nn.Linear(20, 64), nn.ReLU(), nn.Linear(64, 2)).to(device)
2. Run: opt = torch.optim.Adam(model.parameters(), lr=1e-3); loss_fn = nn.CrossEntropyLoss()

**Narration over this clip (for pacing)**

> The model is small. Twenty inputs, sixty-four hidden units with ReLU, and two outputs. She moves it to the device, and chooses the Adam optimiser and cross-entropy loss.

## Clip 4: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L05_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Run the loop cell: for epoch in range(10): model.train(); for xb, yb in train_dl: opt.zero_grad(); loss = loss_fn(model(xb), yb); loss.backward(); opt.step()
2. Highlight model.eval() and with torch.no_grad() in the validation part
3. Show the printed lines: epoch number and validation accuracy

**Narration over this clip (for pacing)**

> Now the loop, for ten epochs. Train mode, then for each batch, the five lines. After that, eval mode and no grad, and she counts correct predictions on the validation set. Each epoch prints its validation accuracy.

## Clip 5: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L05_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Scroll up to the logreg score and down to the last epoch accuracy; place them side by side (expected output: similar scores)

**Narration over this clip (for pacing)**

> She compares both scores on the same validation split. On data like this, you should see something like a network that is only slightly better, or about the same. Folasade records that honestly. The network costs more, so it must earn its place.

## Production notes for this lesson

- Review flags: none. content.md states no accuracy values. The voiceover gives no scores; it says the network may be only slightly better or about the same. Show whatever the notebook prints and do not add numbers in captions.
- The dataset is synthetic (make_classification); say so on screen. Folasade and the Ibadan microfinance lender are hypothetical; stock footage must not show a real company name or logo.
- Run the full cell once before recording. On CPU it finishes in well under a minute.
