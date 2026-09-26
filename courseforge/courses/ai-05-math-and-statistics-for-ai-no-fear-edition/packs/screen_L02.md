# Screen Demo Pack: AI-05 L02 Vectors: Data as Lists of Numbers

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 10

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L02_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Open the Desmos graphing calculator in a browser.
2. Line 1: type a=(3,1).
3. Line 2: type b=(1,2).
4. Line 3: type vector((0,0),a).
5. Line 4: type vector((0,0),b).

**Narration over this clip (for pacing)**

> Now let's see it in 2D with Desmos. Open the Desmos graphing calculator in your browser. In the first line, type a equals three, one. In the second, b equals one, two. Desmos shows two points. Then use the vector function to draw an arrow from the origin to each point.

## Clip 2: scene 11

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L02_screen_2.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Type vector(a,a+b) to place arrow b at the tip of arrow a.
2. Type vector((0,0),a+b).
3. Hover over the end point to show (4, 3).

**Narration over this clip (for pacing)**

> To add them, place arrow b at the end of arrow a. Then draw one arrow from the origin to a plus b. It ends at four, three, which is exactly the sum we calculated by hand.

## Clip 3: scene 12

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L02_screen_3.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Type 2a on a new line.
2. Show the point (6, 2) on the same line as a.
3. Hover to show the coordinates (6, 2).

**Narration over this clip (for pacing)**

> Now type two a. The point six, two appears. It is in the same direction as a, but twice as far from the origin.

## Clip 4: scene 13

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L02_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Open a Colab notebook.
2. Type: import numpy as np; a = np.array([3, 1]); b = np.array([1, 2])
3. Type: print(a + b), print(2 * a), print(np.linalg.norm(np.array([3, 4])))
4. Run the cell and zoom in on [4 3], [6 2] and 5.0.

**Narration over this clip (for pacing)**

> Finally, Inês checks everything in Colab. She creates a and b as NumPy arrays, then prints a plus b, two times a, and the length of three, four. The output is four, three, then six, two, then five point zero. Everything agrees.

## Production notes for this lesson

- [VERSION] Desmos: confirm that typing a point such as a=(3,1), the vector() function and expressions such as a+b and 2a still work as described in the live graphing calculator before recording scenes 10 to 12.
- [VERSION] Google Colab: confirm the interface before recording scene 13.
- Inês and the Lisbon estate agency are hypothetical; the flat vector [75, 3, 20] is invented. Do not show a real agency name or logo in stock footage.
- Speak vectors as lists, for example 'seventy-five, three, twenty'; the slides and screen show the square brackets.
