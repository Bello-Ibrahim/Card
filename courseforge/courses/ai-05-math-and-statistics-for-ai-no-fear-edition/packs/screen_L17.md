# Screen Demo Pack: AI-05 L17 Capstone Build: Linear Regression from Scratch

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L17_screen_1.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Open a new Colab notebook named 'Linear regression from scratch'.
2. Add a text cell: '1. Data'.
3. Add a code cell with the sun, traffic and drinks arrays and X = np.column_stack([np.ones(15), sun, traffic]).
4. Print X.shape and show (15, 3).
5. Type the split: X_tr, y_tr = X[:10], drinks[:10] and X_te, y_te = X[10:], drinks[10:].

**Narration over this clip (for pacing)**

> In Colab, add a text cell called Data, then the data cell. It holds the three columns, then builds X with a column of ones in front. Check the shape: fifteen by three. Then split it into ten training rows and five test rows.

## Clip 2: scene 9

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L17_screen_2.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Type: w = np.zeros(3) with the comment [bias, w_sun, w_traffic].
2. Editor overlay: 'first predictions = 0 → first loss = mean of y_tr² ≈ 3,284.7'.

**Narration over this clip (for pacing)**

> Before any code runs, a hand check. All weights start at zero, so every first prediction is zero. The first loss is the mean of the squared sales of the ten training days, about three thousand two hundred and eighty-four point seven.

## Clip 3: scene 10

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L17_screen_3.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Add a text cell: '2. Training'.
2. Type: lr, losses = 0.01, [] and for step in range(5000):
3. Type the four loop lines with their comments: err = X_tr @ w - y_tr; losses.append(np.mean(err ** 2)); grad = 2 / len(y_tr) * X_tr.T @ err; w = w - lr * grad
4. Highlight each line as it is described.

**Narration over this clip (for pacing)**

> Now a text cell called Training, and the loop. The learning rate is zero point zero one, for five thousand steps. Each step calculates the error, prediction minus truth. It saves the mean squared error. It calculates the gradient. And it steps downhill. Four lines, four ideas you already know.

## Clip 4: scene 11

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L17_screen_4.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Add print(w.round(2)), the first and last loss, and plt.plot(losses); plt.yscale("log"); plt.show().
2. Run the cell.
3. Zoom in on [2.02 3.75 6.53] and 3284.7 5.91.
4. Show the loss curve falling steeply, then flattening.

**Narration over this clip (for pacing)**

> Run it. The weights are about two point zero two for the bias, three point seven five drinks per hour of sunshine, and six point five three drinks per hundred people passing. The loss falls from three thousand two hundred and eighty-four point seven to five point nine one. Steep, then flat.

## Clip 5: scene 12

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L17_screen_5.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Change lr to 0.02 and run the cell.
2. Show the overflow RuntimeWarning messages.
3. Change lr back to 0.01 and run again.

**Narration over this clip (for pacing)**

> One more test. Change the learning rate to zero point zero two and run again. The loss explodes, and NumPy prints overflow warnings. That is divergence, from lesson fourteen. Change it back.

## Production notes for this lesson

- [VERSION] Google Colab: confirm current sign-in requirements, free usage limits and the interface before recording the screen scenes.
- [VERSION] NumPy: confirm that a learning rate of 0.02 still produces overflow RuntimeWarning messages (scene 12), and that all outputs shown (weights 2.02, 3.75, 6.53; loss 3,284.7 to 5.91) match the current Colab NumPy version. Outputs were checked with NumPy 2.4.
- Baraka and the Mombasa cold-drink kiosk are fictional; the 15 days of data are invented.
- The presenter describes the code in words; the screen shows every line. Type at a readable speed or use a pre-typed cell revealed line by line.
