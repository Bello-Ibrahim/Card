# Screen Demo Pack: AI-05 L09 Distributions: Normal and Binomial

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L09_screen_1.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open a Colab notebook and add a new code cell.
2. Type: import numpy as np and import matplotlib.pyplot as plt
3. Type: rng = np.random.default_rng(42)
4. Highlight the seed 42.

**Narration over this clip (for pacing)**

> Let's check in Colab. In a new code cell, Kofi imports NumPy and Matplotlib, the plotting library. Then he creates a random number generator with a fixed seed, forty-two, so the results can be repeated.

## Clip 2: scene 9

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L09_screen_2.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Type: correct = rng.binomial(n=20, p=0.8, size=1000)
2. Type: times = rng.normal(loc=30, scale=5, size=1000)
3. Type: print(correct.mean()) and print(times.mean().round(2))
4. Run the cell and zoom in on 16.023 and 29.61.

**Narration over this clip (for pacing)**

> Next, he simulates one thousand tests of twenty predictions with p of zero point eight, and one thousand delivery times with a mean of thirty and a standard deviation of five. He prints both averages. In this run, the number correct averages sixteen point zero two three, and the times average twenty-nine point six one.

## Clip 3: scene 10

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L09_screen_3.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Type: plt.hist(correct, bins=range(8, 22)) and plt.show()
2. Run the cell.
3. Point at the tall bars at 15, 16 and 17, then at the short bars near 10 and 20.

**Narration over this clip (for pacing)**

> Now he plots a histogram of the correct counts. Most tests score fifteen, sixteen or seventeen. But some score as low as ten, or as high as twenty.

## Clip 4: scene 11

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L09_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Edit the plot line to: plt.hist(times)
2. Run the cell.
3. Show the bell-shaped histogram centred near 30.
4. Shade the band from 25 to 35 as an editor overlay.

**Narration over this clip (for pacing)**

> Then he swaps correct for times, removes the bins setting, and runs again. The bell shape appears around thirty. In this run, about sixty-seven percent of the times fell between twenty-five and thirty-five minutes, close to the sixty-eight percent rule.

## Production notes for this lesson

- [VERSION] Google Colab: confirm current sign-in requirements, free usage limits and the interface before recording the screen scenes.
- [VERSION] NumPy random generator: the outputs 16.023 and 29.61 and the 'about 67%' share were produced with default_rng(42) in NumPy 2.4. Confirm they are the same in Colab's current NumPy version, and that Matplotlib is still pre-installed. If they differ, update the on-screen numbers and the voiceover in scenes 9 and 11.
- Kofi and the Kumasi logistics start-up are fictional; the 80% accuracy and the 30-minute, 5-minute delivery settings are invented.
- The 68% and 95% figures are the standard rule of thumb for normal distributions.
