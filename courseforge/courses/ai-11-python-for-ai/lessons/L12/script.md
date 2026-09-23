# L12 Selecting and Filtering Rows and Columns | Presenter Script

Course: AI-11 · Video: 5 min · Words: 675

## Hook
Most questions about data start with, which ones? Which countries? Which year? Which customers spent more than one hundred? Filtering is how you turn a big table into the few rows that answer your question.

## Explain
Last time, we loaded a table and took a first look. Now we choose parts of it. One column name in square brackets gives a Series. A list of names gives a smaller DataFrame. That is why you see double brackets. The outer ones select, and the inner ones make the list.

Loc and iloc both select rows and columns. Loc uses labels, like index labels and column names. Iloc uses positions, counted from zero. And just like range, the end position is not included.

Now, filtering rows. A comparison on a column, such as year equals two thousand and seven, gives one True or False value for every row. This is called a mask. When you put the mask inside square brackets, pandas keeps only the rows marked True.

Think of a mask as a sieve with holes shaped by your question. You pour the whole table through it. Rows that match fall through into your result. Rows that don't match stay behind. Joining two conditions is like stacking two sieves. A row must pass through both.

To combine conditions, pandas uses symbols instead of words. The ampersand means and, the vertical bar means or, and the tilde means not. Put each condition in its own round brackets. And isin checks a column against a list of values. Finally, loc can filter rows and choose columns in one step. You give it the mask first, then the list of columns you want to keep.

## Demonstrate
Let's use it. Mateus is a public health student in Maputo, Mozambique. He wants the countries in Africa and the Americas with life expectancy above sixty, in the most recent year. He uses the invented practice sample from the last lesson.

First, we keep only the latest year. Instead of typing two thousand and seven, we ask for the maximum year, so the code still works when newer data is added.

Next, the mask. The continent must be in our list of two, and life expectancy must be above sixty. Then loc keeps the matching rows, and only three columns. We print the result and count its rows.

Run it. Ghana, Peru and Chile, and a count of three. The numbers on the left show which rows of the original table were kept. Kenya is not there, because its value, fifty-nine point six, is below sixty. Counting the rows is a quick check that the filter did what you meant.

One more. Asian countries in two thousand and seven, with the largest population first. We combine two conditions, each in its own brackets. Then we sort by population in descending order, and show two columns. Vietnam comes first, with eighty-five million people, then Nepal. Two rows, which is what we expected from the sample.

A common mistake is writing the word and instead of the ampersand, or forgetting the round brackets. Both give an error. The fix is always the same. Use the symbol, and wrap each condition in its own brackets. Also note that this data says Americas, not South America. Filter on the wrong name, and you get zero rows, with no error to warn you.

## Recap
Let's recap. First, single brackets give one column, and double brackets give several. Loc uses labels, and iloc uses positions. Second, a condition creates a True or False mask, and the table keeps the True rows. Third, combine conditions with ampersand, bar and tilde, with each one in round brackets, and check every filter by counting rows.

## CTA
Now it is your turn. In the exercise below this video, you will write five filters on the data, for example all Asian countries in two thousand and seven sorted by population, and check each result by counting rows. It takes about twenty-five minutes. In the next lesson, we learn sorting, grouping and summarising. See you there.

## Thumbnail
Headline: Which Rows Matter?
Image: Navy background, a table pouring through a sieve with three rows coming out below, headline in teal Inter Bold.

## Production Notes
- [VERIFY] Gapminder data source, access method and licence (carried from L11). The practice sample values are invented; label the table on screen as 'Invented practice data'.
- [VERSION] Outputs and error messages were produced with Python 3.11 and pandas 3.0.6. The voiceover mentions the 'truth value is ambiguous' error only in general terms; the second error (missing brackets) may be worded differently in other pandas versions and is not shown on screen.
- Printed outputs on screen must match content.md: the Ghana / Peru / Chile table with index labels 5, 8, 11, then '3'; the Vietnam 85000000 / Nepal 28000000 table with index 14 and 17.
- Before the demo, run the L11 sample cell on screen (or show it already run) so df exists.
- Mateus (Maputo) is fictional.
