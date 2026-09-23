# L04 Preprocessing: Scaling and Encoding | Presenter Script

Course: AI-12 · Video: 5 min · Words: 680

## Hook
Your data has income in the thousands, age in the tens, and a city column with text. Most models cannot read text at all, and some are confused by very different number sizes. Preprocessing fixes both, if you do it in the right order.

## Explain
In the last lesson, you split data into training and test sets. You already know how to clean data with pandas. Today we add two steps that prepare clean data for a model: scaling numbers, and encoding categories.

Some models compare distances or add up weighted features, for example k-nearest neighbours and logistic regression. If income is in thousands and age in tens, income dominates just because its numbers are bigger. A standard scaler rescales each column so it has an average of zero and a standard deviation of one.

Tree-based models, such as decision trees and random forests, do not need scaling, because they split on one column at a time. For text categories, a one-hot encoder turns a city column into one column per city, with one where the row has that city and zero elsewhere.

We tell the encoder to ignore unknown categories. Then a city that appears only in new data does not cause an error. That row simply gets zero in every city column.

Now the golden rule. A scaler learns averages, and an encoder learns the list of categories. If they learn from all the data, information from the test set leaks into training. So always fit them on the training set only, and then just transform the test set.

Scaling is like converting prices into one currency before you compare them. Five thousand in one currency is not bigger than fifty in another until you convert. And the exchange rate must come from the information you had at the time, not next month's rates.

## Demonstrate
Valentina Rojas is an analyst at a microfinance firm with offices in Lima, Quito and Bogotá. She has a small table of eight clients, and wants to prepare it for a model.

In Colab, this cell builds the table, splits it first, then fits a scaler on the training numbers and an encoder on the training cities. Only after that does it transform the test rows. Let's run it.

The first output line shows the shapes. The test set has two rows. They become two scaled number columns, and three city columns.

The second line shows readable names for the new columns, one for each city in the training set. You will need these names again when we look inside a model in lesson six.

The third line is the important one. The scaler learned an average income of three thousand, two hundred and sixty-six point seven, and an average age of thirty-seven point seven. These come from the six training rows only, not from all eight clients.

Valentina notices that doing this by hand, for every column, is slow and easy to get wrong. The next lesson shows how to do it all in one object.

The most common mistake is to scale or encode the whole dataset first, and then split it. The code runs, and the scores look normal, so the problem is hard to see. But the test rows have already shaped the average. With other steps, this habit leads to serious leakage. Split first, then fit.

## Recap
Let's recap. First, scale numbers for distance-based and linear models, but tree models do not need it. Second, turn categories into numbers with a one-hot encoder that ignores unknown values, and check the parameter names for your version. Third, fit preprocessing on the training set only, and transform the test set with the same fitted objects.

## CTA
Now it is your turn. In the exercise below this video, you will scale and encode a mixed table, fitting on the training set only, and add a new city to check that nothing breaks. It takes about twenty-five minutes. In the next lesson, Pipelines and ColumnTransformer, you will put all of this into one safe object. See you there.

## Thumbnail
Headline: Fit on Training Only
Image: Navy background, two currency notes converting into one common coin on the left, a city column turning into 0/1 columns on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] OneHotEncoder output parameter: sparse_output in recent releases, sparse in older ones. Check the current Colab version before recording; the cell uses sparse_output=False.
- [VERSION] Outputs were recorded with scikit-learn 1.9.1, pandas 3.0.6 and Python 3.11. Re-run the cell before recording and update the spoken shapes and means if the output differs.
- Screen scenes 9 to 13 use one Colab cell, copied exactly from the content.md Worked Example. It builds its own small table and needs no earlier setup cell.
- Valentina Rojas and the microfinance firm are fictional. The city names are typed without accents in the code (Bogota), as in content.md.
- Speak the learned means as 'three thousand, two hundred and sixty-six point seven' and 'thirty-seven point seven'; the screen shows [3266.7 37.7].
