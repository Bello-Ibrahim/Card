# Screen Demo Pack: AI-13 L01 Why Deep Learning?

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 11

- **Filename:** `ai-13-deep-learning-and-neural-networks_L01_screen_1.mp4`
- **Target length:** about 9 seconds

**Steps**

1. Open colab.research.google.com and click New notebook
2. Open Runtime > Change runtime type
3. Choose a GPU hardware accelerator and click Save

**Narration over this clip (for pacing)**

> Open a new Colab notebook. From the Runtime menu, choose Change runtime type, select a GPU hardware accelerator, and save.

## Clip 2: scene 12

- **Filename:** `ai-13-deep-learning-and-neural-networks_L01_screen_2.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Run the check cell: import torch, time; print(torch.__version__, torch.cuda.is_available()); device = "cuda" if torch.cuda.is_available() else "cpu"
2. Highlight True in the output

**Narration over this clip (for pacing)**

> Now run the check cell. It prints the PyTorch version, and whether PyTorch can see a GPU. If it says true, you are ready. If it says false, the code still runs, but on the CPU, and slowly.

## Clip 3: scene 13

- **Filename:** `ai-13-deep-learning-and-neural-networks_L01_screen_3.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Run the timing cell from content.md: a = torch.randn(4096, 4096); time a @ a on CPU
2. Same cell: g = a.to(device); torch.cuda.synchronize(); time g @ g; torch.cuda.synchronize()
3. Show printed 'CPU seconds:' and 'GPU seconds:'

**Narration over this clip (for pacing)**

> Next, the timing cell. It creates a large random matrix of about four thousand by four thousand numbers, multiplies it by itself on the CPU, and then does the same on the GPU.

## Clip 4: scene 14

- **Filename:** `ai-13-deep-learning-and-neural-networks_L01_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Run the timing cell a second time
2. Point to the second-run CPU and GPU times (expected output: GPU many times faster; exact numbers vary)

**Narration over this clip (for pacing)**

> Run it twice, because the first GPU run includes start-up time. On the second run, you should see something like a GPU that is many times faster. Exact numbers depend on your hardware.

## Clip 5: scene 15

- **Filename:** `ai-13-deep-learning-and-neural-networks_L01_screen_5.mp4`
- **Target length:** about 8 seconds

**Steps**

1. Highlight both torch.cuda.synchronize() calls in the timing cell

**Narration over this clip (for pacing)**

> Notice the synchronise calls. GPU work runs in the background, so without them the timer stops too early.

## Production notes for this lesson

- [VERSION] Check before recording: Colab free GPU access, the GPU type offered, usage limits, session timeouts and the menu path Runtime > Change runtime type. The voiceover says only that limits exist and change.
- [REGION] Google Colab and the Hugging Face Hub may not be available in every country. The voiceover points to a local Jupyter notebook on CPU as the fallback; the course page must offer it too.
- Timing output is hardware-dependent. The voiceover says 'you should see something like' and gives no fixed numbers; show the second run of the timing cell, not the first.
- Dilnoza and the Tashkent textile company are hypothetical; stock footage must not show a real company name or logo.
- Screen recording: clean Google account, browser zoomed so code and output are readable on a phone. Run every cell once before recording.
