# Screen Demo Pack: AI-05 L05 Matrix Multiplication as Many Predictions

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L05_screen_1.mp4`
- **Target length:** about 24 seconds

**Steps**

1. Open a Colab notebook and a new code cell.
2. Type: import numpy as np
3. Type: X = np.array([[2, 1], [3, 4], [5, 2]]) and w = np.array([10, 3])
4. Type: print(X.shape, w.shape) and run the cell.
5. Zoom in on the output (3, 2) (2,).

**Narration over this clip (for pacing)**

> Now in Colab. Linh creates the matrix X from the three orders, and the weights w, ten and three. She prints both shapes. X is three by two. Notice that NumPy shows w as just two, comma. That is a plain vector with two numbers, and NumPy treats it as two by one when you multiply.

## Clip 2: scene 10

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L05_screen_2.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Type: print(X @ w)
2. Run the cell.
3. Zoom in on [23 42 56] and place the hand results beside it with green ticks.

**Narration over this clip (for pacing)**

> Next, she prints X at w. The output is twenty-three, forty-two, fifty-six. Exactly our hand calculation, in one short line.

## Clip 3: scene 11

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L05_screen_3.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Type: X @ np.array([10, 3, 1])
2. Run the cell.
3. Scroll to the last line of the ValueError.
4. Highlight 'mismatch in its core dimension' and 'size 3 is different from 2'.

**Narration over this clip (for pacing)**

> Now let's make a mistake on purpose. Linh adds a third weight and runs the cell again. NumPy stops with a value error. It says there is a mismatch in the core dimension, and that size three is different from two. In plain words: the matrix has two columns, but you gave three weights.

## Production notes for this lesson

- [VERSION] NumPy: the @ operator is stable, but confirm the exact wording of the shape-mismatch ValueError against the current NumPy version before recording scene 11. The message in content.md ('mismatch in its core dimension', 'size 3 is different from 2') was checked with NumPy 2.4; the voiceover paraphrases it so it survives small wording changes.
- [VERSION] Google Colab: confirm the interface before recording the screen scenes.
- Linh, the Hanoi clothing shop and the prices (shirt 10, socks 3) are hypothetical. No real brand names or logos in stock footage.
