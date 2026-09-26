# Screen Demo Pack: AI-12 L03 Train/Test Split and Why It Matters

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L03_screen_1.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Open a new Colab notebook.
2. Type this exact code cell from content.md and run it with Shift+Enter:
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = make_classification(n_samples=1000, n_features=10, n_informative=4,
                           flip_y=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42)

for depth in [None, 3]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42)
    tree.fit(X_train, y_train)
    print(depth, round(tree.score(X_train, y_train), 3),
          round(tree.score(X_test, y_test), 3))

**Narration over this clip (for pacing)**

> In a new Colab cell, we create one thousand synthetic rows, split them, and train two decision trees. One tree has no depth limit. The other can ask only three questions in a row. For each tree, we print the training score and the test score.

## Clip 2: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L03_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Highlight the line X_train, X_test, y_train, y_test = train_test_split(...).
2. Number the four outputs 1 to 4 on screen and hold for three seconds.

**Narration over this clip (for pacing)**

> Before we read the results, look at the split. It returns four pieces, in a fixed order: training features, test features, then training targets and test targets. Mixing up this order is a common bug.

## Clip 3: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L03_screen_3.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Highlight the output line: None 1.0 0.728.
2. Draw a gap arrow between 1.0 and 0.728.

**Narration over this clip (for pacing)**

> Now the first line of output. The deep tree scores one point zero on training data. That is one hundred percent. But on the test data, it scores only zero point seven two eight. It memorised the training rows, including the noisy labels.

## Clip 4: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L03_screen_4.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Highlight the output line: 3 0.853 0.812.
2. Draw a short gap arrow between 0.853 and 0.812.

**Narration over this clip (for pacing)**

> The second line is the shallow tree. Its training score is lower, zero point eight five three. But its test score is higher, zero point eight one two. And its two scores are much closer together.

## Clip 5: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L03_screen_5.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Add a text cell below the output.
2. Type: The training score of 1.0 was a warning sign, not a success.

**Narration over this clip (for pacing)**

> Fatima chooses the shallow tree as her starting point, and she writes a note in her notebook. The training score of one point zero was a warning sign, not a success.

## Production notes for this lesson

- [VERSION] Outputs were recorded with scikit-learn 1.9.1 and Python 3.11. make_classification and train_test_split results can change between versions; re-run the cell in the current Colab version before recording and update every spoken and captioned score if the output differs.
- Screen scenes 8 to 12 use one Colab cell, copied exactly from the content.md Worked Example. It runs on its own and needs no earlier setup cell.
- Scene 9: content.md asks the presenter to point clearly to the order of the four outputs of the split; keep the highlight on screen for at least three seconds.
- Fatima Zahra and the Casablanca insurance company are fictional; the data is synthetic.
- Speak scores as decimals, for example 'zero point seven two eight'; the screen shows the exact output.
