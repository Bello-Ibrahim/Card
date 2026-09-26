# Screen Demo Pack: AI-12 L04 Preprocessing: Scaling and Encoding

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L04_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Type this exact code cell from content.md and run it with Shift+Enter:
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

df = pd.DataFrame({
    "income": [1200, 3400, 2500, 5100, 1800, 4200, 2900, 3900],
    "age": [23, 45, 31, 52, 27, 38, 60, 41],
    "city": ["Lima", "Quito", "Lima", "Bogota", "Quito", "Lima", "Bogota", "Quito"],
})
train, test = train_test_split(df, test_size=0.25, random_state=0)

scaler = StandardScaler().fit(train[["income", "age"]])
num_test = scaler.transform(test[["income", "age"]])

encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
encoder.fit(train[["city"]])
cat_test = encoder.transform(test[["city"]])

print(num_test.shape, cat_test.shape)
print(encoder.get_feature_names_out())
print(scaler.mean_.round(1))
2. Scroll so the whole cell and its three output lines are visible.

**Narration over this clip (for pacing)**

> In Colab, this cell builds the table, splits it first, then fits a scaler on the training numbers and an encoder on the training cities. Only after that does it transform the test rows. Let's run it.

## Clip 2: scene 10

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L04_screen_2.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Highlight the output line (2, 2) (2, 3).
2. Label the first pair 'income, age scaled' and the second pair 'three city columns'.

**Narration over this clip (for pacing)**

> The first output line shows the shapes. The test set has two rows. They become two scaled number columns, and three city columns.

## Clip 3: scene 11

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L04_screen_3.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Highlight the output line ['city_Bogota' 'city_Lima' 'city_Quito'].
2. Point to the call to get_feature_names_out() in the code.

**Narration over this clip (for pacing)**

> The second line shows readable names for the new columns, one for each city in the training set. You will need these names again when we look inside a model in lesson six.

## Clip 4: scene 12

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L04_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Highlight the output line [3266.7   37.7].
2. Point to StandardScaler().fit(train[["income", "age"]]) and add the caption 'learned from training rows only'.

**Narration over this clip (for pacing)**

> The third line is the important one. The scaler learned an average income of three thousand, two hundred and sixty-six point seven, and an average age of thirty-seven point seven. These come from the six training rows only, not from all eight clients.

## Clip 5: scene 13

- **Filename:** `ai-12-machine-learning-with-scikit-learn_L04_screen_5.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Scroll back up over the separate scaler and encoder lines to show how much manual work they take.

**Narration over this clip (for pacing)**

> Valentina notices that doing this by hand, for every column, is slow and easy to get wrong. The next lesson shows how to do it all in one object.

## Production notes for this lesson

- [VERSION] OneHotEncoder output parameter: sparse_output in recent releases, sparse in older ones. Check the current Colab version before recording; the cell uses sparse_output=False.
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11. Re-run the cell before recording and update the spoken shapes and means if the output differs.
- Screen scenes 9 to 13 use one Colab cell, copied exactly from the content.md Worked Example. It builds its own small table and needs no earlier setup cell.
- Valentina Rojas and the microfinance firm are fictional. The city names are typed without accents in the code (Bogota), as in content.md.
- Speak the learned means as 'three thousand, two hundred and sixty-six point seven' and 'thirty-seven point seven'; the screen shows [3266.7 37.7].
