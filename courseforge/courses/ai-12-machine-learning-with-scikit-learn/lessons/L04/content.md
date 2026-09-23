# L04 Preprocessing: Scaling and Encoding

Course: AI-12 · Module: M1 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Your data has an income column in the thousands, an age column in the tens, and a city column with text. Most models cannot read text at all, and some models are confused when one column has much larger numbers than another. Preprocessing fixes both problems, but only if you do it in the right order.

## Explanation
You already know how to clean data with pandas from AI-11. Here we look at two steps that prepare clean data for a model.

**Scaling numbers.** Some models compare distances or add up weighted features, for example k-nearest neighbours, logistic regression with regularisation, and support vector machines. If income is measured in thousands and age in tens, income dominates only because its numbers are bigger. `StandardScaler` rescales each column so that it has a mean of 0 and a standard deviation of 1. Tree-based models, such as decision trees and random forests, do not need scaling, because they split on one column at a time.

**Encoding categories.** Models need numbers. `OneHotEncoder` turns a column such as `city` into one column per value: `city_Lima`, `city_Quito`, and so on, with 1 where the row has that value and 0 elsewhere. Set `handle_unknown="ignore"` so that a city that appears only in new data does not cause an error; that row simply gets 0 in all city columns.

**The golden rule: learn preprocessing settings from the training data only.** When you call `fit` on a scaler, it learns the mean and standard deviation. When you fit an encoder, it learns the list of categories. If you fit them on all data, information from the test set leaks into training. Always `fit` (or `fit_transform`) on the training set, then only `transform` the test set.

The encoder's parameter for dense output is `sparse_output=False` in recent releases. Older tutorials use `sparse=False`, which newer versions no longer accept. [VERSION]

**Analogy:** Scaling is like converting prices from different currencies into one currency before you compare them. A price of 5,000 in one currency is not bigger than 50 in another until you convert them. The exchange rate must be fixed from the information you had at the time, not from next month's rates.

## Worked Example
Valentina Rojas is an analyst at a hypothetical microfinance firm with offices in Lima, Quito and Bogotá. She has a small table of clients and wants to prepare it for a model. The presenter types this into Colab and runs it:

```python
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
```

Output (scikit-learn 1.9.1, pandas 3.0.6): [VERSION]

```
(2, 2) (2, 3)
['city_Bogota' 'city_Lima' 'city_Quito']
[3266.7   37.7]
```

The presenter points out three things:

1. The test set has 2 rows. It becomes 2 scaled number columns and 3 city columns.
2. `scaler.mean_` shows the averages learned from the **training rows only** (3,266.7 and 37.7), not from all 8 rows.
3. `get_feature_names_out()` gives readable names for the new columns, which you will need in L06.

Valentina notices that doing this by hand for every column is slow and easy to get wrong. L05 shows how to do it all in one object.

## Common Mistake
The most common mistake is to scale or encode the whole dataset first, and then split it. The code runs and the scores look normal, so the problem is hard to see. But the scaler has already used the test rows to compute its mean, so the test is no longer fully unseen. The difference is often small with a scaler, but the habit leads to serious leakage with other steps, such as imputation or feature selection. Split first, then fit preprocessing on the training set.

## Key Takeaways
1. Scale numbers with `StandardScaler` for distance-based and linear models; tree models do not need it.
2. Turn categories into numbers with `OneHotEncoder(handle_unknown="ignore")`, and check the output parameter name for your version.
3. Fit preprocessing on the training set only, then transform the test set with the same fitted objects.

## Hands-on Exercise
**Task:** Scale and one-hot encode a mixed dataset, fitting on the training set only, and check the shapes of the results.
**Tools:** Google Colab (free), scikit-learn, pandas.
**Steps:**
1. Create the table from the example, or build your own with at least 2 number columns and 1 category column and 10 or more rows.
2. Split it with `train_test_split` and `random_state=0`.
3. Fit a `StandardScaler` on the training number columns. Transform both the training and test columns.
4. Fit a `OneHotEncoder(handle_unknown="ignore", sparse_output=False)` on the training category column and transform both sets.
5. Print the shape of each result and the encoder's feature names.
6. Add one test row with a new city, such as "Cusco", and transform it. Confirm that all city columns are 0.
**What good looks like:** Printed shapes where the number of rows matches each set and the number of city columns matches the categories in the training set. The new city causes no error. A text cell explains why you fitted on the training set only.
**Time:** about 25 minutes

## Review Flags
- [VERSION] `OneHotEncoder` output parameter: `sparse_output` in recent releases, `sparse` in older ones. Check the current Colab version before scripting. Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11.
