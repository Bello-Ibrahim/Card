# Screen Demo Pack: AI-13 L02 Tensors: The Language of PyTorch

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-13-deep-learning-and-neural-networks_L02_screen_1.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run: import torch; device = "cuda" if torch.cuda.is_available() else "cpu"
2. Run: x = torch.rand(32, 64, 64, 3) and print(x.shape)
3. Run: x = x.permute(0, 3, 1, 2); print(x.shape, x.dtype, x.device)
4. Output: torch.Size([32, 3, 64, 64]) torch.float32 cpu

**Narration over this clip (for pacing)**

> He starts with a batch of thirty-two photos, sixty-four pixels square, with the channels last. One permute moves the channels to position one. Now the print shows thirty-two, three, sixty-four, sixty-four, as float numbers on the CPU.

## Clip 2: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L02_screen_2.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run: mean = torch.tensor([0.5, 0.4, 0.3]).view(3, 1, 1)
2. Run: x = (x - mean); print(x.shape)
3. Run: x = x.to(device); print(x.device) → cuda:0

**Narration over this clip (for pacing)**

> Next, he makes a mean with one value per channel, shaped three, one, one, and subtracts it. Broadcasting stretches it across the whole batch. Then he moves the batch to the GPU.

## Clip 3: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L02_screen_3.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Run: flat = x.reshape(x.shape[0], -1); print(flat.shape) → torch.Size([32, 12288])
2. Run: labels = torch.randint(0, 5, (32,)); print(labels.dtype) → torch.int64
3. Run: single = x[0].unsqueeze(0); print(single.shape) → torch.Size([1, 3, 64, 64])

**Narration over this clip (for pacing)**

> For a linear layer, he flattens each image into one long row. The minus one tells PyTorch to work out the size, which is twelve thousand two hundred and eighty-eight. He also creates class labels as whole numbers, and picks one image with a new batch dimension.

## Clip 4: scene 13

- **Filename:** `ai-13-deep-learning-and-neural-networks_L02_screen_4.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Run a cell that combines x on the GPU with labels on the CPU; show the error: Expected all tensors to be on the same device
2. Fix: labels = labels.to(device); re-run the cell with no error

**Narration over this clip (for pacing)**

> Now Tomás gets an error. Expected all tensors to be on the same device. His images are on the GPU, but the labels are still on the CPU. The fix is always the same. Move both to one device.

## Production notes for this lesson

- Review flags: none. Run every snippet once before recording and confirm the printed shape torch.Size([32, 3, 64, 64]) and the flattened size 12288.
- The device error message on screen must read: Expected all tensors to be on the same device. Trigger it on purpose by leaving labels on the CPU while x is on the GPU, then fix it with labels.to(device).
- On a CPU runtime the device prints cpu; record on a GPU runtime so cuda:0 appears.
- Tomás and the Valparaíso agritech start-up are hypothetical; stock footage must not show a real company name or logo.
