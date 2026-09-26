# Screen Demo Pack: AI-13 L06 Image Data and Transforms

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L06_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Run: raw = datasets.FashionMNIST("data", train=True, download=True)
2. Run: pixels = raw.data.float() / 255; mean, std = pixels.mean().item(), pixels.std().item(); print(round(mean, 3), round(std, 3))
3. Expected output: something like 0.286 0.353

**Narration over this clip (for pacing)**

> First, she downloads the training set with no transforms, turns the pixels into decimals, and computes the mean and standard deviation. You should see something like zero point two eight six and zero point three five three.

## Clip 2: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L06_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Run the train_tf cell: RandomHorizontalFlip(), RandomCrop(28, padding=2), ToTensor(), Normalize((mean,), (std,))
2. Run the eval_tf cell: ToTensor(), Normalize((mean,), (std,))
3. Show both side by side and highlight the two random steps

**Narration over this clip (for pacing)**

> Next, two pipelines. The training transform adds a random flip and a random crop with padding, then converts and normalises. The evaluation transform only converts and normalises.

## Clip 3: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L06_screen_3.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Run: train_ds = datasets.FashionMNIST("data", train=True, transform=train_tf)
2. Run: test_ds = datasets.FashionMNIST("data", train=False, transform=eval_tf)

**Narration over this clip (for pacing)**

> She passes the right pipeline to each split. The training set gets the training transform. The test set gets the evaluation transform.

## Clip 4: scene 13

- **Filename:** `ai-13-deep-learning-and-neural-networks_L06_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run: imgs = torch.stack([train_ds[0][0] for _ in range(16)])
2. Run: plt.imshow(make_grid(imgs * std + mean, nrow=8).permute(1, 2, 0)); plt.axis("off"); plt.show()
3. Point to shifted and flipped copies in the 2×8 grid

**Narration over this clip (for pacing)**

> Finally, she loads the same image sixteen times and shows them in a grid. Each copy is shifted a little, and some are flipped. The grid is also a useful check. If the images look destroyed, the augmentation is too strong.

## Production notes for this lesson

- [VERIFY] Fashion-MNIST licence and source must be confirmed before the dataset is named and used in the recording. The voiceover names the dataset but makes no licence claim; it only tells learners to check the licence before reuse.
- [VERSION] Check the torchvision transforms API in Colab at recording time: classic transforms compared with transforms.v2. The demo uses classic transforms, as in content.md.
- Mean and standard deviation are said as 'something like 0.286 and 0.353' (content.md: values from the team's CPU test run). Show the real printed values.
- Mei Lin and the Penang clothing retailer are hypothetical; stock footage must not show a real store name or logo.
