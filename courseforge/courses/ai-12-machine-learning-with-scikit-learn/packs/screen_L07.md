# Screen Demo Pack: AI-12 L07 Decision Trees and k-Nearest Neighbours

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L07_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Scroll past the L03 cell, already executed.
2. Type this exact code cell from content.md and run it with Shift+Enter:
import matplotlib.pyplot as plt

depths, train_acc, test_acc = range(1, 21), [], []
for d in depths:
    tree = DecisionTreeClassifier(max_depth=d, random_state=42).fit(X_train, y_train)
    train_acc.append(tree.score(X_train, y_train))
    test_acc.append(tree.score(X_test, y_test))

plt.plot(depths, train_acc, label="train")
plt.plot(depths, test_acc, label="test")
plt.xlabel("max_depth"); plt.ylabel("accuracy"); plt.legend(); plt.show()

**Narration over this clip (for pacing)**

> This cell trains twenty trees, with depths from one to twenty. For each tree, it records the training score and the test score. Then it plots both lines, so we can see the whole story at once.

## Clip 2: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L07_screen_2.mp4`
- **Target length:** about 21 seconds

**Steps**

1. Show the overlay table from content.md next to the plot.
2. Point to depth 1 on the plot: 0.689 / 0.648.
3. Point to depth 4: 0.865 / 0.828 and add a vertical marker.

**Narration over this clip (for pacing)**

> At depth one, the tree scores zero point six eight nine on training data and zero point six four eight on test data. Too simple. At depth four, the test score is at its highest, zero point eight two eight, with training at zero point eight six five.

## Clip 3: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L07_screen_3.mp4`
- **Target length:** about 20 seconds

**Steps**

1. Point to depth 8: 0.947 / 0.792.
2. Point to depths 13 to 20: 1.000 / 0.728.
3. Shade the area right of depth 4 and label it 'overfitting'.

**Narration over this clip (for pacing)**

> After that, training keeps rising. At depth eight, it is zero point nine four seven, but test has fallen to zero point seven nine two. From depth thirteen to twenty, training is a perfect one, and test drops to zero point seven two eight. That is overfitting.

## Clip 4: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L07_screen_4.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Type this exact code cell from content.md and run it with Shift+Enter:
from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

Xw, yw = load_wine(return_X_y=True)
Xw_tr, Xw_te, yw_tr, yw_te = train_test_split(
    Xw, yw, test_size=0.3, stratify=yw, random_state=0)
raw = KNeighborsClassifier(n_neighbors=5).fit(Xw_tr, yw_tr)
scaled = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
scaled.fit(Xw_tr, yw_tr)
print(round(raw.score(Xw_te, yw_te), 3), round(scaled.score(Xw_te, yw_te), 3))

**Narration over this clip (for pacing)**

> Next, k-nearest neighbours on the wine data. This cell trains the same model twice. Once on the raw measurements, and once inside a small pipeline that scales the features first. Then it prints both test scores.

## Clip 5: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L07_screen_5.mp4`
- **Target length:** about 17 seconds

**Steps**

1. Highlight the output 0.722 0.963.
2. Label 0.722 'raw' and 0.963 'scaled'.

**Narration over this clip (for pacing)**

> Without scaling, the test accuracy is zero point seven two two. With scaling, it jumps to zero point nine six three. One wine feature has values in the hundreds or thousands, so without scaling, it decides the distance almost alone.

## Production notes for this lesson

- Setup before recording: in a fresh Colab runtime, run the L03 cell first (content.md L03 Worked Example: make_classification, the stratified split with random_state=42, and the imports of train_test_split and DecisionTreeClassifier). The first L07 cell uses that X_train and X_test. Do not run the L05 bank setup cell in the same runtime, because it overwrites X_train and y_train.
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, matplotlib 3.11 and Python 3.11. Tree results and the wine split can change between versions; re-run before recording and update the spoken scores (depth table and 0.722 / 0.963) if they differ.
- Screen scenes 8 to 10 use the first L07 cell (depth loop and plot); scenes 11 and 12 use the second cell (KNN on wine), both copied exactly from content.md. The depth table values come from the train_acc and test_acc lists; show them as a small overlay table on the plot, as content.md lists them.
- Mateo Fernández and the Argentine farming cooperative are fictional; the data is synthetic and the wine data ships with scikit-learn.
