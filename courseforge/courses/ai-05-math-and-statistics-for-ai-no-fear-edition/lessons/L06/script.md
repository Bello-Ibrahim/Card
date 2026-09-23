# L06 Describing Data: Mean, Median and Spread | Presenter Script

Course: AI-05 · Video: 5 min · Words: 706

## Hook
Five people work in a small team. Four of them earn about the same, and one earns six times more. Someone says: the average income in this team is ten thousand. Is that true? Yes. Is it fair? Not really.

## Explain
Welcome to Module 2, probability and statistics. Before you train any model, you describe your data with a few numbers. They answer two questions. Where is the centre of the data? And how spread out is it?

First, the centre. The mean is the ordinary average: add all the values, and divide by how many there are. The median is the middle value after you sort the data. With an even number of values, it is the mean of the two middle ones.

The mean uses every value, so one very large or very small value, called an outlier, can pull it a long way. The median only cares about the middle position, so outliers hardly move it.

Now the spread. The variance measures how far values are from the mean, on average. Find each distance from the mean, square it, then take the mean of those squares. Squaring makes every distance positive, and makes big distances count more. The standard deviation is the square root of the variance, so it is in the same units as the data.

In NumPy, you use mean, median, var and std. One detail: n p dot std divides by the number of values, n. Some tools divide by n minus one instead, which gives a slightly larger answer for a sample. Both are correct. Just be consistent.

Here is a picture. The mean is like the balance point of a see-saw. If one very heavy person sits at the far end, the balance point moves a long way. The median is like the person in the middle of a queue sorted by height. The tallest person does not change who stands in the middle.

## Demonstrate
Kwame leads a team of five at a software company in Accra, Ghana. Their monthly incomes, in thousands of Ghana cedis, are invented for this example: four, five, five, six and thirty. The last one belongs to a senior partner.

Picture a dot plot. Four dots sit close together near five, and one dot sits far away at thirty. Now the centre. Four plus five plus five plus six plus thirty is fifty, and fifty divided by five is ten. That is the mean. Sorted, the middle value is five. That is the median.

The mean of ten is higher than what four of the five people earn. The median of five describes a typical team member much better.

Now the spread. Subtract the mean of ten from each value: minus six, minus five, minus five, minus four, and twenty. Square them: thirty-six, twenty-five, twenty-five, sixteen and four hundred. They add up to five hundred and two. Divide by five, and the variance is one hundred point four. The standard deviation is about ten point zero two.

Without the senior partner, the values four, five, five and six have a mean of five, a variance of zero point five, and a standard deviation of about zero point seven one. One value changed the spread enormously. And in NumPy, the four functions give the same results as our hand calculation for the full team.

A common mistake is to report only the mean, and assume it is typical. With incomes, house prices or delivery times, the mean can mislead. Always look at the median and the standard deviation too, and draw a quick plot.

## Recap
Let's recap. First, the mean is the sum divided by the count, and the median is the middle sorted value, which resists outliers. Second, the variance is the mean of the squared distances from the mean, and the standard deviation is its square root, in the original units. Third, always report centre and spread together, and compare mean and median to spot outliers.

## CTA
Your turn. In the exercise, you take ten delivery times, find the mean, median and standard deviation by hand, check them in NumPy, then add an outlier and watch what changes. It takes about twenty-five minutes. Next: Probability and Conditional Probability. See you there.

## Thumbnail
Headline: Is the Average Fair?
Image: Navy background, a dot plot with four teal dots close together and one far to the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] Spreadsheet functions: the voiceover does not name spreadsheet functions. The code slide mentions ddof=1 only. If the editor adds STDEV (n − 1) or STDEV.P (n) to a slide, confirm them first in Google Sheets.
- Kwame, the Accra software team and the incomes (4, 5, 5, 6 and 30 thousand Ghana cedis) are hypothetical. Do not show real salary data or a real company logo.
- Not a screen demo lesson: code appears only on a code slide.
