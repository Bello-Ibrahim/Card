# L06 Describing Data: Mean, Median and Spread

Course: AI-05 · Module: M2 · Objectives: O1, O3 · Video: 5 min

## Hook
Five people work in a small team. Four of them earn about the same, and one earns six times more. Someone says, "The average income in this team is 10,000." Is that true? Yes. Is it a fair description? Not really. This lesson shows you why.

## Explanation
Before you train any model, you should describe your data with a few numbers. They answer two questions: where is the **centre** of the data, and how **spread out** is it?

**Centre.**

- The **mean** is the ordinary average. In words: add all the values and divide by how many there are.
- The **median** is the middle value after you sort the data. If there is an even number of values, it is the mean of the two middle values.

The mean uses every value, so one very large or very small value, called an **outlier**, can pull it a long way. The median only cares about the middle position, so outliers hardly move it.

**Spread.**

- The **variance** measures how far values are from the mean, on average. In words: find each value's distance from the mean, square each distance, then take the mean of those squares. Squaring makes all distances positive and makes big distances count more.
- The **standard deviation** is the square root of the variance. It is easier to read because it is in the same units as the data. A small standard deviation means the values are close together; a large one means they are spread out.

In NumPy: `np.mean(x)`, `np.median(x)`, `np.var(x)` and `np.std(x)`.

One detail to know: `np.std` divides by the number of values, n. Some tools, such as the spreadsheet function `STDEV`, divide by n − 1 instead, which gives a slightly larger answer for a sample. [VERSION] In NumPy you get the n − 1 version with `np.std(x, ddof=1)`. Both are correct; they answer slightly different questions. Just be consistent.

**Analogy:** The mean is like a see-saw's balance point. If one very heavy person sits at the far end, the balance point moves a long way towards them. The median is like the person standing in the middle of a queue sorted by height. It does not matter how tall the last person is; the middle person stays the same.

## Worked Example
Kwame leads a hypothetical team of five at a software company in Accra, Ghana. Monthly incomes, in thousands of Ghana cedis, are invented for this example: 4, 5, 5, 6 and 30. The last value belongs to a senior partner.

**Picture:** a dot plot with four dots close together near 5 and one dot far away at 30.

**Hand calculation (centre):**

- Mean: 4 + 5 + 5 + 6 + 30 = 50, and 50 ÷ 5 = 10.
- Median: the sorted values are 4, 5, **5**, 6, 30, so the middle value is 5.

The mean of 10 is higher than what four of the five people earn. The median of 5 describes a typical team member much better.

**Hand calculation (spread):** take each value minus the mean of 10: −6, −5, −5, −4 and 20. Square them: 36, 25, 25, 16 and 400. Their sum is 502, and 502 ÷ 5 = 100.4. That is the variance. The standard deviation is the square root of 100.4, about 10.02.

Without the senior partner, the values 4, 5, 5 and 6 have a mean of 5, a variance of 0.5 and a standard deviation of about 0.71. One value changed the spread enormously.

**Code:**

```python
import numpy as np
income = np.array([4, 5, 5, 6, 30])
print(np.mean(income))    # 10.0
print(np.median(income))  # 5.0
print(np.var(income))     # 100.4
print(np.std(income))     # 10.019980039900279
```

## Common Mistake
Many people report only the mean and assume it describes a "typical" value. When data has outliers or is uneven, such as incomes, house prices or delivery times, the mean can mislead. Always look at the median and the standard deviation too, and draw a quick plot. In machine learning this matters because outliers can pull a model's weights a long way, as you will see with squared error in L12.

## Key Takeaways
1. The mean is the sum divided by the count; the median is the middle sorted value and resists outliers.
2. The variance is the mean of the squared distances from the mean, and the standard deviation is its square root, in the original units.
3. Always report centre and spread together, and compare mean and median to spot outliers.

## Hands-on Exercise
**Task:** Calculate the mean, median and standard deviation of a 10-value dataset by hand or in a spreadsheet, then check the results with NumPy.
**Tools:** Pen and paper or a free spreadsheet (Google Sheets or similar); Google Colab with NumPy.
**Steps:**
1. Use these hypothetical delivery times in minutes: 12, 15, 11, 14, 13, 16, 12, 20, 14, 13.
2. Calculate the mean. Then sort the values and find the median.
3. Subtract the mean from each value, square the results, add them and divide by 10 to get the variance. Take the square root.
4. In Colab, check each result with `np.mean`, `np.median` and `np.std`.
5. Now change 20 to 60 and recalculate everything in NumPy. Write two sentences about which numbers changed a lot and which hardly changed.
**What good looks like:** Mean 14, median 13.5, variance 6 and standard deviation about 2.45, all matching NumPy. Your note explains that the outlier moved the mean and standard deviation but not the median.
**Time:** about 25 minutes

## Review Flags
- [VERSION] Spreadsheet functions: confirm that `STDEV` divides by n − 1 in the spreadsheet tools named (for example Google Sheets), and the name of the n version (`STDEV.P`), before recording.
- All incomes and delivery times are hypothetical.
