# Screen Demo Pack: AI-05 L18 Capstone Explain: Check, Interpret and Document

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 6

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L18_screen_1.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Open the L17 notebook in Colab.
2. Add a text cell: '3. Check with least squares'.
3. Type: w_ls, *_ = np.linalg.lstsq(X_tr, y_tr, rcond=None) and print(w_ls.round(2))
4. Run the cell and zoom in on [2.02 3.75 6.53].

**Narration over this clip (for pacing)**

> Back to Baraka's kiosk notebook in Colab. Add a text cell called Check with least squares, and run least squares on the training data. The first result is a list of values, and we keep only the weights. They are two point zero two, three point seven five and six point five three.

## Clip 2: scene 7

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L18_screen_2.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Type: print(np.allclose(w, w_ls, atol=0.001))
2. Run the cell and zoom in on True.

**Narration over this clip (for pacing)**

> Then n p dot all close compares both sets of weights, and prints True. They match to better than zero point zero zero one. Your loop was correct.

## Clip 3: scene 8

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L18_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Add a text cell: '4. Evaluate'.
2. Type the mse function and the three print lines: training, test and baseline with np.full(5, y_tr.mean()).
3. Run the cell and zoom in on 5.91, 11.2 and 348.01.

**Narration over this clip (for pacing)**

> Now a text cell called Evaluate. Using the m s e function, the training error is five point nine one. The test error is eleven point two. And the baseline on the test set is three hundred and forty-eight point zero one.

## Clip 4: scene 11

- **Filename:** `ai-05-math-and-statistics-for-ai-no-fear-edition_L18_screen_4.mp4`
- **Target length:** about 23 seconds

**Steps**

1. Add a text cell: 'Judgement'.
2. Type: 'Promising, but check again after one more month of data.'
3. Type a second sentence: the weights show links in this data, not causes.
4. Use Run all to run every cell from the top.

**Narration over this clip (for pacing)**

> Baraka writes his judgement in a text cell. The gain over the baseline is very large, so it is unlikely to be random. But there are only five test days, so: promising, but check again after one more month of data. The weights show links in this data, not proof that sunshine causes sales.

## Production notes for this lesson

- [VERSION] NumPy: confirm that np.linalg.lstsq with rcond=None returns four values, gives no warning, and matches the outputs shown (weights 2.02, 3.75, 6.53; MSE 5.91, 11.2, 348.01) in the current Colab NumPy version. Outputs were checked with NumPy 2.4.
- [VERSION] Google Colab: confirm the interface for adding text cells and running all cells before recording the screen scenes.
- Baraka and the Mombasa kiosk data are hypothetical. Weight interpretations must stay worded as links, not causes.
- The CTA points learners to the capstone rubric and submission checklist (capstone_rubric.md).
