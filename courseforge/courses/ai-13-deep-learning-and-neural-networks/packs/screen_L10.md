# Screen Demo Pack: AI-13 L10 Transfer Learning with Pretrained CNNs

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-13-deep-learning-and-neural-networks_L10_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run: weights = ResNet18_Weights.DEFAULT; model = resnet18(weights=weights)
2. Run: for p in model.parameters(): p.requires_grad = False
3. Run: model.fc = nn.Linear(model.fc.in_features, 3); preprocess = weights.transforms()

**Narration over this clip (for pacing)**

> In Colab, she loads ResNet eighteen with its default pretrained weights, and freezes every parameter. Then she replaces the final layer with a new one that has three outputs. Only this new head can learn. Everything else keeps what it learned before.

## Clip 2: scene 9

- **Filename:** `ai-13-deep-learning-and-neural-networks_L10_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run: print(sum(p.numel() for p in model.parameters() if p.requires_grad))
2. Output: 1539

**Narration over this clip (for pacing)**

> She counts the trainable parameters. Only one thousand five hundred and thirty-nine, which is five hundred and twelve features times three classes, plus three biases. So each epoch is fast, even on a CPU.

## Clip 3: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L10_screen_3.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Run: ds = load_dataset("AI-Lab-Makerere/beans") and show the dataset card on the Hub
2. Run: define to_tensors with preprocess(img.convert("RGB")); ds = ds.with_transform(to_tensors)
3. Run: collate = ...; train_dl = DataLoader(ds["train"], batch_size=32, shuffle=True, collate_fn=collate)

**Narration over this clip (for pacing)**

> Next, she loads the dataset and applies the pretrained model's own transforms to every image. A small collate function stacks the images and labels into batches of thirty-two.

## Clip 4: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L10_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run: opt = torch.optim.AdamW(model.fc.parameters(), lr=1e-3); train 3–5 epochs with the L05 loop
2. Run: for p in model.layer4.parameters(): p.requires_grad = True
3. Run: opt = torch.optim.AdamW([{"params": model.layer4.parameters(), "lr": 1e-4}, {"params": model.fc.parameters(), "lr": 1e-3}])

**Narration over this clip (for pacing)**

> Stage one trains only the head for a few epochs. For stage two, she unfreezes the last block, and builds a new optimiser with two learning rates. A small one for the pretrained block, and a larger one for the head.

## Clip 5: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L10_screen_5.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Show a results table with three rows: CNN from scratch (L07, 3-channel), frozen ResNet + new head, fine-tuned ResNet (expected output: both pretrained runs clearly better)

**Narration over this clip (for pacing)**

> Grace compares three runs on the validation split. Her CNN trained from scratch, the frozen ResNet, and the fine-tuned ResNet. You should see something like both pretrained runs doing clearly better on this small dataset. She reports her own measured numbers.

## Production notes for this lesson

- [VERSION] torchvision weights API: weights= and ResNet18_Weights.DEFAULT replaced pretrained=True in newer versions. Check against the Colab version at recording time.
- [VERIFY] Bean-leaf disease dataset: Hub dataset ID (AI-Lab-Makerere/beans in content.md), source (collected in Uganda), class names (healthy, angular leaf spot, bean rust) and licence must be confirmed on the Hub page before recording. The voiceover does not state the dataset's origin or licence as fact.
- [VERIFY] Licence of the ImageNet-pretrained ResNet-18 checkpoint. The voiceover only tells learners to check checkpoint licences.
- Results are said as 'you should see something like' (content.md: expected result). Show Grace's three real validation scores; do not add numbers in captions.
- The trainable-parameter count 1,539 (512 × 3 + 3) must match the printed output.
- Grace and the Mbale extension service are hypothetical; stock footage must not show a real organisation's name or logo.
